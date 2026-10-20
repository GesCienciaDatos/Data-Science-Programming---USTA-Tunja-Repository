<script setup>
import { useI18n } from '../i18n/index.js';

const { t } = useI18n();
</script>

<template>
  <footer class="mt-auto border-t border-slate-200 dark:border-slate-800 bg-white/70 dark:bg-space-950/70 py-8 px-4 sm:px-8 transition-colors duration-200">
    <div class="max-w-container mx-auto flex flex-col md:flex-row justify-between items-center gap-6">
      
      <!-- Left: Institutional Identity -->
      <div class="flex items-center gap-3.5 text-center md:text-left">
        <img 
          src="/assets/images/logo_usta_seal.gif" 
          alt="Escudo USTA" 
          class="w-8 h-8 object-contain opacity-85"
          onerror="this.style.display='none'"
        />
        <div>
          <p class="font-sans text-xs font-semibold text-slate-900 dark:text-slate-100">
            {{ t('footer.institution') }}
          </p>
          <p class="font-mono text-[11px] text-slate-500 dark:text-slate-400">
            {{ t('footer.faculty') }}
          </p>
        </div>
      </div>

      <!-- Right: Developer Credit & Copyright -->
      <div class="flex flex-col md:items-end text-center md:text-right space-y-1">
        <p class="font-mono text-xs text-slate-700 dark:text-slate-300 font-medium">
          {{ t('footer.developedBy') }} <span class="font-semibold text-slate-900 dark:text-brand-cyan">{{ t('footer.developerName') }}</span>
        </p>
        <p class="font-mono text-[10px] text-slate-400">
          {{ t('footer.copyright') }}
        </p>
      </div>

    </div>
  </footer>
</template>
