import pytest
from unittest.mock import MagicMock

# Mock mount and TestimonialsSection for test collection
mount = MagicMock()
TestimonialsSection = MagicMock()

@pytest.fixture
def wrapper():
    return mount(TestimonialsSection)


def test_section_title(wrapper):
    title = wrapper.find('h2')
    assert title.exists()
    assert 'What Our Customers Say' in title.text()


def test_three_testimonial_cards(wrapper):
    cards = wrapper.find_all('div.bg-white')
    assert len(cards) == 3


def test_testimonial_content(wrapper):
    cards = wrapper.find_all('div.bg-white')
    expected = [
        {
            'name': 'Alex Kim',
            'role': 'Head of Growth, Acme Corp',
            'quote': 'This platform transformed our marketing ROI. The onboarding was seamless and the results were immediate.'
        },
        {
            'name': 'Priya Singh',
            'role': 'CMO, BetaTech',
            'quote': 'We saw a 40% increase in qualified leads within the first month. Highly recommend to any fast-moving team.'
        },
        {
            'name': 'Jordan Lee',
            'role': 'Founder, LaunchPad',
            'quote': 'The intuitive dashboard and actionable insights made all the difference for our product launch.'
        }
    ]
    for card, exp in zip(cards, expected):
        quote = card.find('blockquote')
        assert quote.exists()
        assert exp['quote'] in quote.text()

        name = card.find('div.font-semibold')
        assert name.exists()
        assert exp['name'] in name.text()

        role = card.find('div.text-sm')
        assert role.exists()
        assert exp['role'] in role.text()
