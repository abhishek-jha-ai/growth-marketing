import pytest
from pathlib import Path

# Assuming a test utility to mount and render Vue components in test environment
# This is a placeholder for actual test setup

def test_testimonials_section_renders_correctly():
    # Import the component
    from apps.web.src.components.landing.TestimonialsSection import default as TestimonialsSection

    # Render the component (mocked or shallow mount)
    # Here we simulate rendering and check for expected text content
    rendered_html = TestimonialsSection.render()

    # Check section title
    assert "What Our Customers Say" in rendered_html

    # Check for 3 testimonial quotes
    assert "This product has transformed our business" in rendered_html
    assert "Exceptional quality and fantastic customer service" in rendered_html
    assert "A game changer in our industry" in rendered_html

    # Check for customer names and roles
    assert "Jane Doe, CEO at Acme Corp" in rendered_html
    assert "John Smith, Marketing Director at Beta LLC" in rendered_html
    assert "Emily Johnson, Product Manager at Gamma Inc" in rendered_html


def test_testimonials_section_structure():
    from apps.web.src.components.landing.TestimonialsSection import default as TestimonialsSection
    rendered_html = TestimonialsSection.render()

    # Check that there are exactly 3 testimonial cards
    # This is a simple count of article tags
    assert rendered_html.count('<article') == 3

    # Check that each testimonial card has blockquote and footer
    assert rendered_html.count('<blockquote') == 3
    assert rendered_html.count('<footer') == 3
