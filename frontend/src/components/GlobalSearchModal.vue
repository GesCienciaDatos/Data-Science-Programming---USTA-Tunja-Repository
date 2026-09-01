<script setup>
import { ref, computed, onMounted } from 'vue';

const props = defineProps({
  allNotebooks: {
    type: Array,
    required: true
  }
});

const emit = defineEmits(['close']);

const searchInputRef = ref(null);
const query = ref('');

onMounted(() => {
  if (searchInputRef.value) {
    searchInputRef.value.focus();
  }
});

const searchResults = computed(() => {
  if (query.value.trim().length < 2) return [];
  const q = query.value.toLowerCase().trim();

  return props.allNotebooks.filter(nb => 
    (nb.title || '').toLowerCase().includes(q) ||
    (nb.path || '').toLowerCase().includes(q) ||
    (nb.module_name || '').toLowerCase().includes(q)
  ).slice(0, 15);
});
</script>

<template>
  <div class="fixed inset-0 z-50 flex items-start justify-center pt-20 p-4 bg-black/60 backdrop-blur-sm animate-fade-in" @click.self="emit('close')">
    <div class="glass-panel rounded-2xl w-full max-w-2xl border border-slate-200 dark:border-slate-800 flex flex-col overflow-hidden shadow-2xl">
      
      <!-- Search Input Bar -->
      <div class="p-4 border-b border-slate-200 dark:border-slate-800 flex items-center gap-3 bg-white dark:bg-space-900">
        <span class="material-symbols-outlined text-brand-cyan text-xl">search</span>
        <input 
          ref="searchInputRef"
          v-model="query"
          type="text" 
          placeholder="Buscar por concepto, título, módulo o ruta..."
          class="flex-1 bg-transparent border-none text-sm font-mono text-slate-900 dark:text-slate-100 placeholder:text-slate-400 focus:outline-none"
        />
        <button 
          @click="emit('close')"
          class="font-mono text-xs text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 px-2 py-1 rounded bg-slate-100 dark:bg-space-850"
        >
          ESC
        </button>
      </div>

      <!-- Search Results List -->
      <div class="p-3 max-h-[60vh] overflow-y-auto space-y-2 bg-slate-50 dark:bg-space-950">
        <div v-if="query.trim().length < 2" class="py-8 text-center text-xs font-mono text-slate-400">
          Escribe al menos 2 caracteres para buscar en los 144 cuadernos computacionales.
        </div>

        <div v-else-if="searchResults.length === 0" class="py-8 text-center text-xs font-mono text-slate-400">
          No se encontraron coincidencias para "{{ query }}".
        </div>

        <div 
          v-else
          v-for="nb in searchResults"
          :key="nb.path"
          class="p-3 rounded-lg bg-white dark:bg-space-900 border border-slate-200 dark:border-slate-800 flex items-center justify-between gap-3 hover:border-brand-cyan transition-all"
        >
          <div class="space-y-0.5 overflow-hidden">
            <span class="font-mono text-[10px] text-brand-cyan font-semibold block">
              {{ nb.module_name }}
            </span>
            <h5 class="text-xs font-semibold text-slate-900 dark:text-slate-100 truncate">
              {{ nb.title }}
            </h5>
            <p class="font-mono text-[10px] text-slate-400 truncate">
              {{ nb.path }}
            </p>
          </div>

          <a 
            :href="nb.colab_url" 
            target="_blank" 
            rel="noopener noreferrer"
            class="px-2.5 py-1 rounded bg-slate-900 dark:bg-slate-100 hover:bg-slate-800 dark:hover:bg-white text-white dark:text-slate-950 font-mono text-[10px] font-semibold shrink-0 flex items-center gap-1"
          >
            <span>ABRIR</span>
            <span class="material-symbols-outlined text-xs">open_in_new</span>
          </a>
        </div>
      </div>

    </div>
  </div>
</template>
