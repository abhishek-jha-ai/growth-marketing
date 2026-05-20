import pytest

# Since this is a Vue component, we test the rendered HTML output.
# In a real environment, you might use a Vue test utils or a headless browser.
# Here, we simulate minimal tests by checking the component's static data.

# Sample testimonials data from the component
TESTIMONIALS = [
    {
        "name": "Alex Kim",
        "role": "Head of Growth, Acme Corp",
        "quote": "This platform transformed our marketing ROI. The onboarding was seamless and the results were immediate."
    },
    {
        "name": "Priya Singh",
        "role": "CMO, BetaTech",
        "quote": "We saw a 40% increase in qualified leads within the first month. Highly recommend to any fast-moving team."
    },
    {
        "name": "Jordan Lee",
        "role": "Founder, LaunchPad",
        "quote": "The customer support is top-notch and the features are exactly what we needed to scale."
    }
]

@pytest.fixture
def testimonials():
    return TESTIMONIALS


def test_testimonials_count(testimonials):
    assert len(testimonials) == 3


def test_testimonials_content(testimonials):
    for t in testimonials:
        assert "name" in t and t["name"]
        assert "role" in t and t["role"]
        assert "quote" in t and t["quote"]

# Since we cannot render Vue components here, we test the data integrity and structure.
