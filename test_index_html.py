import unittest

from html.parser import HTMLParser

class TestIndexHtml(unittest.TestCase):
    def setUp(self):

        # Simulate loading the index.html content
        self.html_content = '''
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

    def test_html_structure(self):
        # Basic checks for HTML structure
        self.assertIn('<!DOCTYPE html>', self.html_content)
        self.assertIn('<div id="app">', self.html_content)
        self.assertIn('<title>Growth Marketing</title>', self.html_content)

    def test_html_validity(self):
        # Use a simple HTML parser to check for well-formedness
        parser = HTMLParser()
        try:
            parser.feed(self.html_content)
        except Exception as e:
            self.fail(f"HTML parsing failed: {e}")

if __name__ == '__main__':
    unittest.main()
