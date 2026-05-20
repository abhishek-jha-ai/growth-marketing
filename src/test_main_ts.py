import pytest
import os

# Test that src/main.ts imports LandingPage.vue and does not import App.vue

def test_main_ts_imports_landing_page():
    main_ts_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'main.ts')
    with open(main_ts_path, 'r') as f:
        content = f.read()
    # It should import LandingPage.vue
    assert "import LandingPage from './LandingPage.vue'" in content
    # It should NOT import App.vue
    assert "import App from './App.vue'" not in content

