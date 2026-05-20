import os
import pytest

# Test that LandingPage.vue exists in the workspace

def test_landing_page_vue_exists():
    landing_page_path = os.path.join(os.path.dirname(__file__), '..', 'LandingPage.vue')
    assert os.path.exists(landing_page_path), "LandingPage.vue should exist in the generated workspace"
