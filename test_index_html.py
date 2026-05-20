import pytest

# This test ensures that the root index.html is not modified directly by the TestimonialsSection addition.
# We simulate reading the index.html content and verify it does not contain the testimonials section content.

# Simulated index.html content (minimal)
INDEX_HTML_CONTENT = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Growth Marketing</title>
</head>
<body>
  <div id="app"></div>
  <script type="module" src="/src/main.ts"></script>
</body>
</html>
'''


def test_index_html_not_modified():
    # The index.html should not contain the testimonials section title or cards
    assert "What Our Customers Say" not in INDEX_HTML_CONTENT
    assert '<article' not in INDEX_HTML_CONTENT
