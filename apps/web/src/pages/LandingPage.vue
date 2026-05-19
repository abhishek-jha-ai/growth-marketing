<template>
  <div class="landing-container">
    <header class="landing-header">
      <h1 class="landing-title"><ContentSlot content-key="apps_web_src_pages.growth_marketing_monorepo" fallback="Growth Marketing Monorepo" /></h1>
      <p class="landing-subtitle"><ContentSlot content-key="apps_web_src_pages.verify_monorepo_runtime_and_preview" fallback="Verify monorepo runtime and preview continuity" /></p>
    </header>
    <main>
      <section class="hero-section">
        <!-- HeroSection governed component (simulated) -->
        <div class="hero-content">
          <h2 class="hero-title"><ContentSlot content-key="apps_web_src_pages.seamless_monorepo_experience" fallback="Seamless Monorepo Experience" /></h2>
          <p class="hero-subtitle"><ContentSlot content-key="apps_web_src_pages.unified_runtime_preview_and_governance" fallback="Unified runtime, preview, and governance for modern teams." /></p>
        </div>
      </section>
      <CTASection tone="brand-accent" layout="inline" size="lg">
        <template #headline><ContentSlot content-key="apps_web_src_pages.ready_to_verify_your_monorepo" fallback="Ready to verify your monorepo runtime?" /></template>
        <template #supportingText><ContentSlot content-key="apps_web_src_pages.preview_validate_and_launch_with" fallback="Preview, validate, and launch with confidence using governed architecture." /></template>
        <template #primaryCta>
          <PrimaryButton><ContentSlot content-key="apps_web_src_pages.start_verification" fallback="Start Verification" /></PrimaryButton>
        </template>
      </CTASection>
    </main>
    <footer class="landing-footer">
      <span><ContentSlot content-key="apps_web_src_pages.2026_growth_marketing_all_rights" fallback="© 2026 Growth Marketing. All rights reserved." /></span>
    </footer>
  </div>
</template>

<script setup>
import CTASection from '../components/landing/CTASection.vue'
// PrimaryButton is assumed to be globally registered or imported from design system
</script>

<style src="../styles/landing.css"></style>
