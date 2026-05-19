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

if __name__ == '__main__':
    unittest.main()
