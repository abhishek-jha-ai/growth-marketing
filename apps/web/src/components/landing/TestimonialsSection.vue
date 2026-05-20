<template>
  <section class="w-full bg-[color:var(--surface-background)] py-16">
    <div class="max-w-5xl mx-auto px-4">
      <h2 class="text-3xl md:text-4xl font-bold text-[color:var(--text-primary)] text-center mb-12 font-heading"><ContentSlot content-key="apps_web_src_components.what_our_customers_say" fallback="What Our Customers Say" /></h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div
          v-for="testimonial in testimonials"
          :key="testimonial.name"
          class="bg-white rounded-xl shadow-md p-8 flex flex-col items-center"
        >
          <svg class="w-8 h-8 text-[color:var(--brand-accent)] mb-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M19 7v4a2 2 0 01-2 2h-3m-4 0H5a2 2 0 01-2-2V7m16 0a2 2 0 00-2-2H7a2 2 0 00-2 2m16 0v10a2 2 0 01-2 2H7a2 2 0 01-2-2V7" />
          </svg>
          <blockquote class="text-lg text-[color:var(--text-primary)] italic mb-6 text-center"><ContentSlot content-key="apps_web_src_components.testimonial_quote" fallback=""{{ testimonial.quote }}"" /></blockquote>
          <div class="mt-auto text-center">
            <div class="font-semibold text-[color:var(--brand-primary)]"><ContentSlot content-key="apps_web_src_components.testimonial_name" fallback="{{ testimonial.name }}" /></div>
            <div class="text-sm text-[color:var(--text-primary)] opacity-70"><ContentSlot content-key="apps_web_src_components.testimonial_role" fallback="{{ testimonial.role }}" /></div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const testimonials = [
  {
    name: 'Alex Kim',
    role: 'Head of Growth, Acme Corp',
    quote: 'This platform transformed our marketing ROI. The onboarding was seamless and the results were immediate.'
  },
  {
    name: 'Priya Patel',
    role: 'Founder, StartupX',
    quote: 'We saw a 3x increase in qualified leads within the first month. Highly recommended for fast-moving teams.'
  },
  {
    name: 'Jordan Lee',
    role: 'CMO, NextGen Ventures',
    quote: 'The analytics and automation features are best-in-class. Our team saves hours every week.'
  }
];
</script>
