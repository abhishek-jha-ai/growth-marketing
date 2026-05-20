import os
import pytest

# Test that App.vue does not exist in the workspace

def test_app_vue_missing():
    app_vue_path = os.path.join(os.path.dirname(__file__), '..', 'App.vue')
    assert not os.path.exists(app_vue_path), "App.vue should not exist in the generated workspace"
