<script setup>
defineProps({
  currentView: {
    type: String,
    required: true
  },
  activeCourse: {
    type: Object,
    default: null
  },
  isDarkMode: {
    type: Boolean,
    required: true
  }
});

const emit = defineEmits([
  'navigate-view',
  'open-search',
  'toggle-theme'
]);
</script>

<template>
  <nav class="sticky top-0 z-40 w-full glass-panel border-b px-4 sm:px-8 py-3 transition-colors duration-200">
    <div class="max-w-container mx-auto flex items-center justify-between gap-4">
      
      <!-- Institutional Brand -->
      <div class="flex items-center gap-3.5 shrink-0">
        <button 
          @click="emit('navigate-view', 'directory')" 
          class="flex items-center gap-3 text-left group" 
          title="Ir al Plan de Estudios"
        >
          <img 
            src="/assets/images/logo_usta_seal.gif" 
            alt="Escudo USTA" 
            class="w-8 h-8 object-contain transition-transform group-hover:scale-105"
            onerror="this.style.display='none'"
          />
          <div class="flex flex-col">
            <span class="font-sans text-sm font-semibold tracking-tight leading-tight text-slate-900 dark:text-slate-100">
              Universidad Santo Tomás
            </span>
            <span class="font-mono text-[10px] text-slate-500 dark:text-slate-400 font-medium hidden sm:inline">
              Facultad de Ingeniería de Sistemas • Especialización en Ciencia de Datos
            </span>
          </div>
        </button>
      </div>

      <!-- Navigation Link: Plan de Estudios -->
      <div class="flex items-center gap-4 font-mono text-xs text-slate-600 dark:text-slate-400">
        <button 
          @click="emit('navigate-view', 'directory')"
          class="px-3 py-1 rounded-md transition-colors flex items-center gap-1.5"
          :class="currentView === 'directory' ? 'text-brand-cyan font-semibold bg-brand-cyan/10' : 'hover:text-brand-cyan hover:bg-slate-100 dark:hover:bg-space-900'"
        >
          <span class="material-symbols-outlined text-sm">school</span>
          <span>Plan de Estudios</span>
        </button>

        <div v-if="currentView === 'workspace' && activeCourse" class="flex items-center gap-2">
          <span class="text-slate-300 dark:text-slate-700">/</span>
          <span class="text-slate-900 dark:text-slate-200 font-semibold px-2 py-0.5 rounded bg-slate-100 dark:bg-space-900">
            {{ activeCourse.name }}
          </span>
        </div>
      </div>

      <!-- Action Tools: Global Search & Theme Toggle -->
      <div class="flex items-center gap-2.5">
        <!-- Global Search Trigger -->
        <button 
          @click="emit('open-search')"
          class="flex items-center gap-2 px-3 py-1.5 rounded-md bg-slate-100 dark:bg-space-900 border border-slate-200 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700 text-slate-500 dark:text-slate-400 text-xs font-mono transition-all w-28 sm:w-44 justify-between"
          title="Buscar en todo el ecosistema (Ctrl+K)"
        >
          <span class="flex items-center gap-1.5">
            <span class="material-symbols-outlined text-sm">search</span>
            <span class="hidden sm:inline">Buscar...</span>
          </span>
          <span class="text-[10px] bg-slate-200 dark:bg-space-850 px-1 py-0.5 rounded border border-slate-300 dark:border-slate-800">/</span>
        </button>

        <!-- Dark / Light Mode Toggle Button -->
        <button 
          @click="emit('toggle-theme')" 
          class="p-2 rounded-md bg-slate-100 dark:bg-space-900 border border-slate-200 dark:border-slate-800 hover:border-brand-cyan text-slate-600 dark:text-slate-300 hover:text-brand-cyan transition-all flex items-center justify-center"
          :title="isDarkMode ? 'Cambiar a Modo Claro' : 'Cambiar a Modo Oscuro'"
          aria-label="Alternar tema de color"
        >
          <span class="material-symbols-outlined text-base">
            {{ isDarkMode ? 'light_mode' : 'dark_mode' }}
          </span>
        </button>
      </div>

    </div>
  </nav>
</template>
