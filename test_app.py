import unittest
from fastapi.testclient import TestClient
from app import router, capability_resolver
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

client = TestClient(app)

class TestAppRuntime(unittest.TestCase):
    def test_capture_lead_success(self):
        lead_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "source": "landing_page"
        }
        response = client.post("/capture-lead", json=lead_data)
        self.assertEqual(response.status_code, 200)
        json_resp = response.json()
        self.assertIn("status", json_resp)
        self.assertEqual(json_resp["status"], "success")

    def test_capture_lead_missing_capability(self):
        # Temporarily remove a capability to simulate failure
        original = capability_resolver.capabilities.get("lead_capture_storage")
        capability_resolver.capabilities["lead_capture_storage"] = None
        lead_data = {"name": "Jane Doe"}
        response = client.post("/capture-lead", json=lead_data)
        self.assertEqual(response.status_code, 200)
        json_resp = response.json()
        self.assertIn("error", json_resp)
        self.assertEqual(json_resp["error"], "Required capabilities are not available")
        # Restore capability
        capability_resolver.capabilities["lead_capture_storage"] = original

    def test_capture_lead_storage_failure(self):
        # Patch store_lead to simulate failure
        original_store_lead = capability_resolver.capabilities["lead_capture_storage"].store_lead
        def fail_store_lead(data):
            return False
        capability_resolver.capabilities["lead_capture_storage"].store_lead = fail_store_lead
        lead_data = {"name": "Fail Case"}
        response = client.post("/capture-lead", json=lead_data)
        self.assertEqual(response.status_code, 200)
        json_resp = response.json()
        self.assertIn("error", json_resp)
        self.assertEqual(json_resp["error"], "Failed to store lead")
        # Restore original method
        capability_resolver.capabilities["lead_capture_storage"].store_lead = original_store_lead

    def test_capture_lead_all_capabilities_present(self):
        # Verify all capabilities are present
        resolver = capability_resolver
        self.assertIsNotNone(resolver.get("lead_capture_storage"))
        self.assertIsNotNone(resolver.get("crm_sync"))
        self.assertIsNotNone(resolver.get("notification_dispatch"))
        self.assertIsNotNone(resolver.get("analytics_event_stream"))

    def test_capture_lead_partial_capability_absence(self):
        # Remove one capability and test error
        original = capability_resolver.capabilities.get("crm_sync")
        capability_resolver.capabilities["crm_sync"] = None
        lead_data = {"name": "Partial Fail"}
        response = client.post("/capture-lead", json=lead_data)
        self.assertEqual(response.status_code, 200)
        json_resp = response.json()
        self.assertIn("error", json_resp)
        self.assertEqual(json_resp["error"], "Required capabilities are not available")
        # Restore capability
        capability_resolver.capabilities["crm_sync"] = original

    def test_notification_and_analytics_invocation(self):
        # Patch notification_dispatch and analytics_event_stream to verify invocation
        calls = {"notification": False, "analytics": False}
        original_dispatch = capability_resolver.capabilities["notification_dispatch"].dispatch
        original_send_event = capability_resolver.capabilities["analytics_event_stream"].send_event

        def mock_dispatch(message):
            calls["notification"] = True

        def mock_send_event(event):
            calls["analytics"] = True

        capability_resolver.capabilities["notification_dispatch"].dispatch = mock_dispatch
        capability_resolver.capabilities["analytics_event_stream"].send_event = mock_send_event

        lead_data = {"name": "Notify Test"}
        response = client.post("/capture-lead", json=lead_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(calls["notification"])
        self.assertTrue(calls["analytics"])

        # Restore original methods
        capability_resolver.capabilities["notification_dispatch"].dispatch = original_dispatch
        capability_resolver.capabilities["analytics_event_stream"].send_event = original_send_event

if __name__ == '__main__':
    unittest.main()
