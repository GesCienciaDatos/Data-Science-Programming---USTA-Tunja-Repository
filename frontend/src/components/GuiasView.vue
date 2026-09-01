<script setup>
defineProps({
  guias: {
    type: Array,
    required: true
  }
});

const emit = defineEmits(['open-pdf']);
</script>

<template>
  <div class="space-y-6 py-6 px-4 sm:px-8 max-w-container mx-auto">
    
    <!-- Header -->
    <div class="pb-3 border-b border-slate-200 dark:border-slate-800">
      <h2 class="text-xl font-semibold text-slate-900 dark:text-slate-100 flex items-center gap-2">
        <span class="material-symbols-outlined text-brand-cyan text-lg">description</span>
        Guías de Laboratorio & Documentación PDF
      </h2>
      <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
        Manuales técnicos de configuración de entornos, librerías y guías paso a paso.
      </p>
    </div>

    <!-- Guias Grid -->
    <div v-if="guias.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
      <div 
        v-for="guia in guias" 
        :key="guia.id"
        class="glass-card rounded-xl p-5 border flex flex-col justify-between transition-all duration-200 hover:border-slate-300 dark:hover:border-slate-700 space-y-4"
      >
        <div class="space-y-3">
          <div class="flex items-center justify-between gap-2">
            <span class="font-mono text-[10px] text-brand-cyan font-semibold">
              {{ guia.module || 'Documentación' }}
            </span>
            <span class="px-1.5 py-0.5 rounded text-[9px] font-mono border border-slate-200 dark:border-slate-700 text-slate-500">
              {{ guia.size_str || 'PDF' }}
            </span>
          </div>

          <div class="flex items-start gap-3">
            <div class="w-10 h-10 rounded-lg bg-rose-500/10 border border-rose-500/20 text-rose-500 flex items-center justify-center shrink-0">
              <span class="material-symbols-outlined text-xl">picture_as_pdf</span>
            </div>
            <div class="space-y-0.5">
              <h4 class="text-sm font-semibold text-slate-900 dark:text-slate-100 leading-snug">
                {{ guia.title }}
              </h4>
              <p class="font-mono text-[10px] text-slate-400 truncate">
                {{ guia.filename }}
              </p>
            </div>
          </div>
        </div>

        <div class="pt-3 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between gap-2">
          <button 
            @click="emit('open-pdf', guia)"
            class="px-3 py-1.5 rounded-md bg-slate-900 dark:bg-slate-100 hover:bg-slate-800 dark:hover:bg-white text-white dark:text-slate-950 font-mono text-xs font-semibold flex items-center gap-1.5 transition-all shadow-xs"
          >
            <span class="material-symbols-outlined text-sm">visibility</span>
            <span>VER EN VISOR</span>
          </button>

          <a 
            :href="guia.raw_url || guia.lfs_url || guia.path" 
            target="_blank" 
            rel="noopener noreferrer"
            download
            class="p-1.5 rounded-md bg-slate-100 dark:bg-space-900 hover:bg-slate-200 dark:hover:bg-space-850 text-slate-600 dark:text-slate-300 transition-colors"
            title="Descargar archivo PDF"
          >
            <span class="material-symbols-outlined text-base">download</span>
          </a>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-else class="py-12 text-center glass-panel rounded-xl border border-slate-200 dark:border-slate-800">
      <span class="material-symbols-outlined text-slate-400 text-3xl mb-2">description</span>
      <h3 class="text-sm font-semibold text-slate-800 dark:text-slate-200">No hay guías cargadas</h3>
      <p class="text-xs text-slate-500 mt-0.5">Los manuales se publicarán con el desarrollo de cada módulo.</p>
    </div>

  </div>
</template>
