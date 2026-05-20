def test_index_html_contains_basic_structure():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Check that the index.html contains the root div for Vue app
    assert '<div id="app">' in content

    # Check that the title tag is present
    assert '<title>' in content and '</title>' in content

    # Check that no direct inline styles are present (enforce contract)
    assert 'style="' not in content
