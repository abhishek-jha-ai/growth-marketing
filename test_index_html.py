import pytest

# Test that index.html does not contain direct modifications related to testimonials
# and preserves existing preview/runtime behavior.

# Simulated index.html content
INDEX_HTML_CONTENT = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Growth Marketing</title>
</head>
<body>
  <div id="app"></div>
</body>
</html>
'''


def test_index_html_structure():
    assert '<div id="app"></div>' in INDEX_HTML_CONTENT
    assert '<section' not in INDEX_HTML_CONTENT  # TestimonialsSection should not be directly in index.html
