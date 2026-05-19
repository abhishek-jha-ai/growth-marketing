<template>
  <section
    class="cta-section"
    :class="[
      `tone-${tone}`,
      layout ? `layout-${layout}` : '',
      size ? `size-${size}` : ''
    ]"
  >
    <div class="content">
      <div class="headline">
        <slot name="headline" />
      </div>
      <div class="supporting-text">
        <slot name="supportingText" />
      </div>
      <div class="primary-cta">
        <slot name="primaryCta" />
      </div>
    </div>
  </section>
</template>

<script setup>
defineProps({
  tone: {
    type: String,
    default: 'brand-accent'
  },
  layout: {
    type: String,
    default: 'inline'
  },
  size: {
    type: String,
    default: 'lg'
  }
})
</script>

<style scoped>
.cta-section {
  background-color: var(--color-cta-bg, var(--brand-accent));
  color: var(--color-cta-text, var(--surface-background));
  border-radius: var(--radius-lg, 1rem);
  padding: var(--space-lg, 1.5rem);
  display: flex;
  justify-content: center;
  align-items: center;
}

.content {
  max-width: 600px;
  text-align: center;
}

.headline {
  font-size: 1.5rem;
  margin-bottom: var(--space-md, 1rem);
  font-weight: 700;
}

.supporting-text {
  font-size: 1rem;
  margin-bottom: var(--space-md, 1rem);
}

.primary-cta {
  display: inline-block;
}

.tone-brand-accent {
  background-color: var(--brand-accent);
  color: var(--surface-background);
}

.tone-brand-primary {
  background-color: var(--brand-primary);
  color: var(--surface-background);
}

.tone-text-primary {
  background-color: var(--text-primary);
  color: var(--surface-background);
}
</style>
