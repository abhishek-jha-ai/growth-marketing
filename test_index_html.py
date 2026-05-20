import pytest

# Test that index.html does not contain direct modifications for testimonials

def test_index_html_no_testimonials_section_modification():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    # The testimonials section should not be directly added in index.html
    assert 'What Our Customers Say' not in content
    assert 'testimonial' not in content.lower()
