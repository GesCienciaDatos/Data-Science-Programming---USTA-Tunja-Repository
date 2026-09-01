<script setup>
import { computed } from 'vue';

const props = defineProps({
  doc: {
    type: Object,
    required: true
  }
});

const emit = defineEmits(['close']);

const pdfSrc = computed(() => {
  if (!props.doc) return '';
  const path = props.doc.pdf_url || props.doc.path || props.doc.download_url || '';
  if (path.startsWith('http')) return path;
  return `./${path}`;
});

const downloadUrl = computed(() => {
  if (!props.doc) return '#';
  return props.doc.download_url || props.doc.raw_url || props.doc.lfs_url || pdfSrc.value;
});
</script>

<template>
  <div class="fixed inset-0 z-50 flex items-center justify-center p-2 sm:p-4 bg-black/75 backdrop-blur-md animate-fade-in" @click.self="emit('close')">
    <div class="glass-panel rounded-2xl w-full max-w-5xl h-[90vh] border border-slate-200 dark:border-slate-800 flex flex-col overflow-hidden shadow-2xl bg-white dark:bg-space-900">
      
      <!-- Modal Header -->
      <div class="px-5 py-3 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between gap-3 bg-slate-50 dark:bg-space-950">
        <div class="flex items-center gap-2.5 overflow-hidden">
          <span class="material-symbols-outlined text-brand-cyan text-xl shrink-0">picture_as_pdf</span>
          <div class="overflow-hidden">
            <h3 class="text-sm font-semibold text-slate-900 dark:text-slate-100 truncate font-mono">
              {{ doc.title || doc.filename }}
            </h3>
            <p class="text-[11px] text-slate-500 truncate font-mono">
              {{ doc.author ? `${doc.author} • ` : '' }}{{ doc.size_mb || doc.size_str || 'Documento PDF' }}
            </p>
          </div>
        </div>

        <div class="flex items-center gap-2 shrink-0">
          <a 
            :href="downloadUrl" 
            target="_blank" 
            rel="noopener noreferrer"
            download
            class="px-3 py-1.5 rounded-md bg-slate-100 dark:bg-space-850 hover:bg-slate-200 dark:hover:bg-space-800 text-slate-700 dark:text-slate-200 text-xs font-mono font-medium flex items-center gap-1.5 transition-colors"
            title="Descargar archivo PDF"
          >
            <span class="material-symbols-outlined text-sm">download</span>
            <span class="hidden sm:inline">Descargar</span>
          </a>

          <a 
            :href="pdfSrc" 
            target="_blank" 
            rel="noopener noreferrer"
            class="px-3 py-1.5 rounded-md bg-slate-100 dark:bg-space-850 hover:bg-slate-200 dark:hover:bg-space-800 text-slate-700 dark:text-slate-200 text-xs font-mono font-medium flex items-center gap-1.5 transition-colors"
            title="Abrir en pestaña nueva"
          >
            <span class="material-symbols-outlined text-sm">open_in_new</span>
            <span class="hidden sm:inline">Pestaña</span>
          </a>

          <button 
            @click="emit('close')"
            class="p-1.5 rounded-md text-slate-400 hover:text-slate-800 dark:hover:text-slate-100 hover:bg-slate-200 dark:hover:bg-space-800 transition-colors"
            title="Cerrar (Esc)"
          >
            <span class="material-symbols-outlined text-lg">close</span>
          </button>
        </div>
      </div>

      <!-- Embedded PDF Iframe / Fallback -->
      <div class="flex-1 w-full h-full bg-slate-200 dark:bg-space-950 relative">
        <iframe 
          :src="pdfSrc" 
          class="w-full h-full border-none"
          title="Visor de Documento PDF"
        ></iframe>
      </div>

    </div>
  </div>
</template>
