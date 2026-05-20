import pytest

# Assuming a test client or rendering utility is available
# Here we use a hypothetical render_component function to render Vue components for testing

@pytest.fixture
def testimonials_section():
    # This fixture would render the TestimonialsSection component
    # For demonstration, we assume it returns a rendered HTML string
    from apps.web.src.components.landing.TestimonialsSection import testimonials
    return testimonials


def test_testimonials_data_structure(testimonials_section):
    # Check that there are exactly 3 testimonials
    assert len(testimonials_section) == 3

    for testimonial in testimonials_section:
        assert 'name' in testimonial
        assert isinstance(testimonial['name'], str)
        assert testimonial['name'] != ''

        assert 'role' in testimonial
        assert isinstance(testimonial['role'], str)
        assert testimonial['role'] != ''

        assert 'quote' in testimonial
        assert isinstance(testimonial['quote'], str)
        assert testimonial['quote'] != ''


def test_testimonials_content_keys():
    # Check that the testimonials have expected keys and values
    from apps.web.src.components.landing.TestimonialsSection import testimonials

    expected_names = {'Alex Kim', 'Priya Singh', 'Jordan Lee'}
    actual_names = {t['name'] for t in testimonials}
    assert expected_names == actual_names

    # Check that quotes contain expected substrings
    quotes = [t['quote'] for t in testimonials]
    assert any('transformed our marketing ROI' in q for q in quotes)
    assert any('3x increase in qualified leads' in q for q in quotes)
    assert any('intuitive dashboard and actionable insights' in q for q in quotes)
