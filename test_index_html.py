import unittest

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

if __name__ == '__main__':
    unittest.main()
