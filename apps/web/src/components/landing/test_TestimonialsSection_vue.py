import pytest

# Assuming a test framework that can mount Vue components and query rendered output
# This is a conceptual test example

def test_testimonials_section_renders_correctly(vue_mount):
    from apps.web.src.components.landing.TestimonialsSection import default as TestimonialsSection

    wrapper = vue_mount(TestimonialsSection)

    # Check section title
    title = wrapper.find('h2')
    assert title.exists()
    assert 'What Our Customers Say' in title.text()

    # Check there are exactly 3 testimonial cards
    cards = wrapper.find_all('blockquote')
    assert len(cards) == 3

    # Check each testimonial has quote, name, and role
    testimonials = [
        {
            'name': 'Alex Kim',
            'role': 'Head of Growth, Acme Corp',
            'quote': 'This platform transformed our marketing ROI. The onboarding was seamless and the results were immediate.'
        },
        {
            'name': 'Priya Singh',
            'role': 'CMO, BetaTech',
            'quote': 'We saw a 40% increase in qualified leads within the first month. Highly recommended for fast-moving teams.'
        },
        {
            'name': 'Jordan Lee',
            'role': 'Founder, LaunchPad',
            'quote': 'The insights and automation are next-level. Our team can finally focus on strategy instead of busywork.'
        }
    ]

    for idx, testimonial in enumerate(testimonials):
        card = cards[idx]
        assert testimonial['quote'] in card.text()
        # The name and role are in sibling divs, check their presence
        parent = card.parent
        name_div = parent.find('div.font-semibold')
        role_div = parent.find('div.text-sm')
        assert name_div is not None
        assert role_div is not None
        assert testimonial['name'] in name_div.text()
        assert testimonial['role'] in role_div.text()


def test_testimonials_section_isolated(vue_mount):
    # Test that the component can be mounted standalone without errors
    from apps.web.src.components.landing.TestimonialsSection import default as TestimonialsSection
    wrapper = vue_mount(TestimonialsSection)
    assert wrapper.exists()
