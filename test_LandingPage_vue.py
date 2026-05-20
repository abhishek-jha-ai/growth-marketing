import pytest

# Assuming LandingPage.vue imports and uses TestimonialsSection

def test_landing_page_includes_testimonials(vue_mount):
    from apps.web.src.views.LandingPage import default as LandingPage

    wrapper = vue_mount(LandingPage)

    # Check that TestimonialsSection is rendered inside LandingPage
    testimonials_section = wrapper.find_component('TestimonialsSection')
    assert testimonials_section.exists()

    # Optionally check the section title inside LandingPage
    title = testimonials_section.find('h2')
    assert title.exists()
    assert 'What Our Customers Say' in title.text()
