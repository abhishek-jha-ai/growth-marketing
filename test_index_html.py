def test_index_html_contains_root_div():
    with open('apps/web/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    assert '<div id="app"></div>' in content


def test_index_html_no_inline_styles():
    with open('apps/web/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    assert 'style="' not in content
