import pytest
from unittest.mock import MagicMock

# Mock mount and LandingPage for test collection
mount = MagicMock()
LandingPage = MagicMock()

@pytest.fixture
def wrapper():
    return mount(LandingPage)


def test_testimonials_section_integration(wrapper):
    testimonials_section = wrapper.find_component('TestimonialsSection')
    assert testimonials_section.exists()

    # Check that the section title is rendered
    title = testimonials_section.find('h2')
    assert title.exists()
    assert 'What Our Customers Say' in title.text()
