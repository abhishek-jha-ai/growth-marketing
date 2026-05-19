<template>
  <section class="py-16 bg-surface-background">
    <div class="max-w-7xl mx-auto px-6">
      <h2 class="text-3xl font-semibold text-text-primary mb-12"><ContentSlot content-key="apps_web_src_components.what_our_customers_say" fallback="What Our Customers Say" /></h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <article class="bg-white rounded-xl shadow-md p-6">
          <blockquote class="text-text-primary mb-4"><ContentSlot content-key="apps_web_src_components.this_product_has_transformed_our" fallback="“This product has transformed our business. The ease of use and support are outstanding.”" /></blockquote>
          <footer class="text-sm text-text-primary font-semibold"><ContentSlot content-key="apps_web_src_components.jane_doe_ceo_at_acme" fallback="Jane Doe, CEO at Acme Corp" /></footer>
        </article>
        <article class="bg-white rounded-xl shadow-md p-6">
          <blockquote class="text-text-primary mb-4"><ContentSlot content-key="apps_web_src_components.exceptional_quality_and_fantastic_customer" fallback="“Exceptional quality and fantastic customer service. Highly recommend to anyone looking to grow.”" /></blockquote>
          <footer class="text-sm text-text-primary font-semibold"><ContentSlot content-key="apps_web_src_components.john_smith_marketing_director_at" fallback="John Smith, Marketing Director at Beta LLC" /></footer>
        </article>
        <article class="bg-white rounded-xl shadow-md p-6">
          <blockquote class="text-text-primary mb-4"><ContentSlot content-key="apps_web_src_components.a_game_changer_in_our" fallback="“A game changer in our industry. The features and reliability are unmatched.”" /></blockquote>
          <footer class="text-sm text-text-primary font-semibold"><ContentSlot content-key="apps_web_src_components.emily_johnson_product_manager_at" fallback="Emily Johnson, Product Manager at Gamma Inc" /></footer>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup>
// No props or state needed for this static testimonials section
</script>
