<template>
  <section class="w-full bg-[color:var(--surface-background)] py-16">
    <div class="max-w-5xl mx-auto px-4">
      <h2 class="text-3xl font-bold text-[color:var(--text-primary)] text-center mb-12 font-heading"><ContentSlot content-key="apps_web_src_components.what_our_customers_say" :fallback=""What Our Customers Say"" /></h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div
          v-for="(testimonial, idx) in testimonials"
          :key="idx"
          class="bg-white rounded-xl shadow-md p-8 flex flex-col items-center"
        >
          <svg class="w-8 h-8 text-[color:var(--brand-accent)] mb-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 13h6v6H9z"/><path stroke-linecap="round" stroke-linejoin="round" d="M17 13a5 5 0 00-10 0v6a5 5 0 0010 0v-6z"/></svg>
          <blockquote class="text-lg text-[color:var(--text-primary)] italic mb-6 text-center"><ContentSlot content-key="apps_web_src_components.testimonial_quote" :fallback=""\"{{ testimonial.quote }}\""" /></blockquote>
          <div class="mt-auto text-center">
            <div class="font-semibold text-[color:var(--brand-primary)]"><ContentSlot content-key="apps_web_src_components.testimonial_name" :fallback="testimonial.name" /></div>
            <div class="text-sm text-[color:var(--text-primary)] opacity-70"><ContentSlot content-key="apps_web_src_components.testimonial_role" :fallback="testimonial.role" /></div>
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
    quote: 'We saw a 40% increase in qualified leads within the first month. Highly recommended for fast-moving teams.'
  },
  {
    name: 'Jordan Lee',
    role: 'Founder, LaunchPad',
    quote: 'The insights and automation are next-level. Our team can finally focus on strategy instead of busywork.'
  }
];
</script>
