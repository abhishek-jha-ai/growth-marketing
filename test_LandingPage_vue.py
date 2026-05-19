import pytest

# Assuming LandingPage.vue imports and uses TestimonialsSection
# We test that the TestimonialsSection is integrated and renders

def test_landing_page_includes_testimonials_section():
    from apps.web.src.views.LandingPage import default as LandingPage

    rendered_html = LandingPage.render()

    # Check that the testimonials section title is present
    assert "What Our Customers Say" in rendered_html

    # Check that at least one testimonial quote is present
    assert "This product has transformed our business" in rendered_html

    # Check that the testimonials section container is present
    assert '<section' in rendered_html
