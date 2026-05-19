import pytest

# Basic test to ensure index.html is not modified and contains expected root elements

def test_index_html_content():
    index_path = 'index.html'
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check that the root div for Vue app is present
    assert '<div id="app"' in content

    # Check that the title is present
    assert '<title>' in content

    # Check that no inline style attributes are present (enforce contract)
    assert 'style="' not in content
