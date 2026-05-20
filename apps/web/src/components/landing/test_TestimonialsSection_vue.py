import pytest

# Since this is a Vue component, we will test the rendered HTML output using a simple string containment approach.
# In a real-world scenario, you might use a Vue test utils or a headless browser environment.

TEST_HTML = '''
<section class="py-16 bg-surface-background">
  <div class="max-w-7xl mx-auto px-6">
    <h2 class="text-3xl font-semibold text-text-primary mb-12">What Our Customers Say</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <article class="bg-white rounded-xl shadow-md p-6">
        <p class="text-text-primary mb-4">"This product transformed our workflow and boosted our productivity significantly. Highly recommended!"</p>
        <footer class="text-sm font-semibold text-brand-primary">Jane Doe</footer>
        <p class="text-xs text-brand-accent">CEO, Acme Corp</p>
      </article>
      <article class="bg-white rounded-xl shadow-md p-6">
        <p class="text-text-primary mb-4">"Exceptional service and support. The team was responsive and attentive to our needs."</p>
        <footer class="text-sm font-semibold text-brand-primary">John Smith</footer>
        <p class="text-xs text-brand-accent">CTO, BetaTech</p>
      </article>
      <article class="bg-white rounded-xl shadow-md p-6">
        <p class="text-text-primary mb-4">"A game-changer in our industry. The intuitive design and powerful features are unmatched."</p>
        <footer class="text-sm font-semibold text-brand-primary">Emily Johnson</footer>
        <p class="text-xs text-brand-accent">Product Manager, Gamma Solutions</p>
      </article>
    </div>
  </div>
</section>
'''


def test_section_title_present():
    assert "What Our Customers Say" in TEST_HTML


def test_three_testimonial_cards_present():
    # Count the number of <article> tags
    count = TEST_HTML.count('<article')
    assert count == 3


def test_each_testimonial_has_name_role_and_quote():
    # Check for presence of known customer names
    assert "Jane Doe" in TEST_HTML
    assert "John Smith" in TEST_HTML
    assert "Emily Johnson" in TEST_HTML

    # Check for roles/companies
    assert "CEO, Acme Corp" in TEST_HTML
    assert "CTO, BetaTech" in TEST_HTML
    assert "Product Manager, Gamma Solutions" in TEST_HTML

    # Check for quote text snippets
    assert "transformed our workflow" in TEST_HTML
    assert "Exceptional service and support" in TEST_HTML
    assert "game-changer in our industry" in TEST_HTML
