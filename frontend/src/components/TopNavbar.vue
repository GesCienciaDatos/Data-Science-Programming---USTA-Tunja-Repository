<script setup>
import { computed } from 'vue';
import { useI18n } from '../i18n/index.js';

const props = defineProps({
  currentView: {
    type: String,
    required: true
  },
  activeCourse: {
    type: Object,
    default: null
  },
  totalBooks: {
    type: Number,
    default: 122
  },
  isDarkMode: {
    type: Boolean,
    required: true
  }
});

const emit = defineEmits([
  'navigate-view',
  'open-search',
  'toggle-theme',
  'toggle-language'
]);

const { currentLang, toggleLanguage, t, getCourseLocalized } = useI18n();

const localizedActiveCourse = computed(() => {
  return props.activeCourse ? getCourseLocalized(props.activeCourse) : null;
});

function handleLanguageToggle() {
  const newLang = toggleLanguage();
  emit('toggle-language', newLang);
}
</script>

<template>
  <nav class="sticky top-0 z-40 w-full glass-panel border-b px-4 sm:px-8 py-3 transition-colors duration-200">
    <div class="max-w-container mx-auto flex items-center justify-between gap-4">
      
      <!-- Institutional Brand -->
      <div class="flex items-center gap-3.5 shrink-0">
        <button 
          @click="emit('navigate-view', 'directory')" 
          class="flex items-center gap-3 text-left group" 
          :title="t('navbar.goToCurriculum')"
        >
          <img 
            src="/assets/images/logo_usta_seal.gif" 
            alt="Escudo USTA" 
            class="w-8 h-8 object-contain transition-transform group-hover:scale-105"
            onerror="this.style.display='none'"
          />
          <div class="flex flex-col">
            <span class="font-sans text-sm font-semibold tracking-tight leading-tight text-slate-900 dark:text-slate-100">
              {{ t('navbar.brandTitle') }}
            </span>
            <span class="font-mono text-[10px] text-slate-500 dark:text-slate-400 font-medium hidden sm:inline">
              {{ t('navbar.brandSubtitle') }}
            </span>
          </div>
        </button>
      </div>

      <!-- Navigation Links: Plan de Estudios & Biblioteca Digital -->
      <div class="flex items-center gap-2 sm:gap-4 font-mono text-xs text-slate-600 dark:text-slate-400">
        <button 
          @click="emit('navigate-view', 'directory')"
          class="px-2.5 sm:px-3 py-1.5 rounded-md transition-colors flex items-center gap-1.5"
          :class="currentView === 'directory' ? 'text-brand-cyan font-semibold bg-brand-cyan/10 border border-brand-cyan/20' : 'hover:text-brand-cyan hover:bg-slate-100 dark:hover:bg-space-900'"
        >
          <span class="material-symbols-outlined text-sm">school</span>
          <span>{{ t('navbar.curriculum') }}</span>
        </button>

        <button 
          @click="emit('navigate-view', 'books')"
          class="px-2.5 sm:px-3 py-1.5 rounded-md transition-colors flex items-center gap-1.5"
          :class="currentView === 'books' ? 'text-brand-cyan font-semibold bg-brand-cyan/10 border border-brand-cyan/20' : 'hover:text-brand-cyan hover:bg-slate-100 dark:hover:bg-space-900'"
          :title="t('navbar.library')"
        >
          <span class="material-symbols-outlined text-sm">menu_book</span>
          <span>{{ t('navbar.library') }}</span>
          <span class="px-1.5 py-0.5 rounded text-[10px] font-mono bg-brand-cyan/15 text-brand-cyan font-semibold">
            {{ totalBooks }}
          </span>
        </button>

        <div v-if="currentView === 'workspace' && localizedActiveCourse" class="hidden md:flex items-center gap-2">
          <span class="text-slate-300 dark:text-slate-700">/</span>
          <span class="text-slate-900 dark:text-slate-200 font-semibold px-2 py-0.5 rounded bg-slate-100 dark:bg-space-900 border border-slate-200 dark:border-slate-800">
            {{ localizedActiveCourse.name }}
          </span>
        </div>
      </div>

      <!-- Action Tools: Global Search, Language Switcher & Theme Toggle -->
      <div class="flex items-center gap-2 sm:gap-2.5">
        <!-- Global Search Trigger -->
        <button 
          @click="emit('open-search')"
          class="flex items-center gap-2 px-3 py-1.5 rounded-md bg-slate-100 dark:bg-space-900 border border-slate-200 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700 text-slate-500 dark:text-slate-400 text-xs font-mono transition-all w-28 sm:w-44 justify-between"
          :title="t('navbar.searchTooltip')"
        >
          <span class="flex items-center gap-1.5">
            <span class="material-symbols-outlined text-sm">search</span>
            <span class="hidden sm:inline">{{ t('navbar.searchPlaceholder') }}</span>
          </span>
          <span class="text-[10px] bg-slate-200 dark:bg-space-850 px-1 py-0.5 rounded border border-slate-300 dark:border-slate-800">/</span>
        </button>

        <!-- Language Switcher Button (ES / EN) -->
        <button 
          @click="handleLanguageToggle"
          class="flex items-center gap-1 px-2.5 py-1.5 rounded-md bg-slate-100 dark:bg-space-900 border border-slate-200 dark:border-slate-800 hover:border-brand-cyan text-slate-700 dark:text-slate-300 font-mono text-xs transition-all cursor-pointer shadow-xs"
          :title="t('navbar.langSwitchTooltip')"
          :aria-label="t('navbar.langAria')"
        >
          <span class="material-symbols-outlined text-sm text-brand-cyan">translate</span>
          <span :class="currentLang === 'es' ? 'text-brand-cyan font-bold underline decoration-brand-cyan decoration-2 underline-offset-2' : 'text-slate-400 hover:text-slate-600 dark:hover:text-slate-200'">ES</span>
          <span class="text-slate-300 dark:text-slate-700">/</span>
          <span :class="currentLang === 'en' ? 'text-brand-cyan font-bold underline decoration-brand-cyan decoration-2 underline-offset-2' : 'text-slate-400 hover:text-slate-600 dark:hover:text-slate-200'">EN</span>
        </button>

        <!-- Dark / Light Mode Toggle Button -->
        <button 
          @click="emit('toggle-theme')" 
          class="p-2 rounded-md bg-slate-100 dark:bg-space-900 border border-slate-200 dark:border-slate-800 hover:border-brand-cyan text-slate-600 dark:text-slate-300 hover:text-brand-cyan transition-all flex items-center justify-center cursor-pointer"
          :title="isDarkMode ? t('navbar.themeToLight') : t('navbar.themeToDark')"
          :aria-label="t('navbar.themeAria')"
        >
          <span class="material-symbols-outlined text-base">
            {{ isDarkMode ? 'light_mode' : 'dark_mode' }}
          </span>
        </button>
      </div>

    </div>
  </nav>
</template>
