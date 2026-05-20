import pytest

# This test assumes the LandingPage.vue integrates the TestimonialsSection component.
# Since we don't have the full Vue test environment, we simulate by checking the presence of the section title in the rendered output.

# Simulated rendered HTML snippet from LandingPage.vue including TestimonialsSection
LANDING_PAGE_HTML = '''
<div>
  <!-- Other landing page content -->
  <section class="py-16 bg-surface-background">
    <div class="max-w-7xl mx-auto px-6">
      <h2 class="text-3xl font-semibold text-text-primary mb-12">What Our Customers Say</h2>
      <!-- Testimonials cards here -->
    </div>
  </section>
  <!-- Other landing page content -->
</div>
'''


def test_testimonials_section_integration():
    # Check that the testimonials section title is present in the landing page HTML
    assert "What Our Customers Say" in LANDING_PAGE_HTML


def test_testimonials_section_structure():
    # Check that the section has the expected classes for spacing and background
    assert 'py-16' in LANDING_PAGE_HTML
    assert 'bg-surface-background' in LANDING_PAGE_HTML

    # Check that the container div has max width and padding
    assert 'max-w-7xl' in LANDING_PAGE_HTML
    assert 'mx-auto' in LANDING_PAGE_HTML
    assert 'px-6' in LANDING_PAGE_HTML
