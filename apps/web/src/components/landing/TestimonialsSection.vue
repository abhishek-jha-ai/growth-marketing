<template>
  <section class="w-full bg-[color:var(--surface-background)] py-16">
    <div class="max-w-5xl mx-auto px-4">
      <h2 class="text-3xl font-bold text-[color:var(--text-primary)] text-center mb-10 font-heading"><ContentSlot content-key="apps_web_src_components.what_our_customers_say" fallback="What Our Customers Say" /></h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div
          v-for="testimonial in testimonials"
          :key="testimonial.name"
          class="bg-white rounded-[1.25rem] shadow-lg p-8 flex flex-col items-center"
        >
          <svg class="w-8 h-8 text-[color:var(--brand-accent)] mb-4" fill="currentColor" viewBox="0 0 24 24">
            <path d="M7.17 15A4.17 4.17 0 013 10.83V10a7 7 0 017-7v2a5 5 0 00-5 5v.83A2.17 2.17 0 007.17 15zm9 0A4.17 4.17 0 0112 10.83V10a7 7 0 017-7v2a5 5 0 00-5 5v.83A2.17 2.17 0 0016.17 15z" />
          </svg>
          <blockquote class="text-lg text-center text-[color:var(--text-primary)] mb-6 font-body"><ContentSlot content-key="apps_web_src_components.testimonial_quote" fallback=""{{ testimonial.quote }}"" /></blockquote>
          <div class="text-center">
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
    name: 'Priya Singh',
    role: 'CMO, BetaTech',
    quote: 'We saw a 40% increase in qualified leads within the first month. Highly recommend to any fast-moving team.'
  },
  {
    name: 'Jordan Lee',
    role: 'Founder, LaunchPad',
    quote: 'The intuitive dashboard and actionable insights made all the difference for our product launch.'
  }
];
</script>
