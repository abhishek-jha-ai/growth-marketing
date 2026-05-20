import pytest

# Test that index.html does not contain direct modifications related to testimonials

def test_index_html_no_testimonials_modifications():
    # Read index.html content
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # The testimonials section should not be directly present in index.html
    assert 'What Our Customers Say' not in content
    assert 'Alex Kim' not in content
    assert 'Priya Singh' not in content
    assert 'Jordan Lee' not in content

    # Ensure no inline styles are present
    assert 'style="' not in content
