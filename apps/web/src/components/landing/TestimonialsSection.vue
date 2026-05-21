<template>
  <SectionContainer class="overflow-x-clip">
    <SectionHeading align="center">
      What Our Customers Say
    </SectionHeading>
    <ContentGrid :columns="1" md:columns="3" gap="lg">
      <TestimonialCard
        v-for="(testimonial, idx) in testimonials"
        :key="idx"
        :name="testimonial.name"
        :role="testimonial.role"
        :quote="testimonial.quote"
      />
    </ContentGrid>
  </SectionContainer>
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
