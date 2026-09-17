<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  datasets: {
    type: Array,
    required: true
  }
});

const emit = defineEmits(['close', 'show-toast']);

const searchQuery = ref('');
const selectedIndex = ref(0);
const isDownloading = ref(false);

const filteredDatasets = computed(() => {
  if (!searchQuery.value.trim()) return props.datasets;
  const q = searchQuery.value.toLowerCase().trim();
  return props.datasets.filter(ds => 
    (ds.name || '').toLowerCase().includes(q) ||
    (ds.module || '').toLowerCase().includes(q) ||
    (ds.description || '').toLowerCase().includes(q) ||
    (ds.target || '').toLowerCase().includes(q) ||
    (ds.features || '').toLowerCase().includes(q)
  );
});

const selectedDataset = computed(() => {
  const list = filteredDatasets.value;
  return list[selectedIndex.value] || list[0] || null;
});

function selectDataset(idx) {
  selectedIndex.value = idx;
}

function getDatasetDownloadUrl(ds) {
  if (!ds) return '#';
  if (ds.download_url) return ds.download_url;
  if (ds.raw_url) return ds.raw_url;
  if (ds.snippet) {
    const match = ds.snippet.match(/https:\/\/[^')]+/);
    if (match) return match[0];
  }
  if (ds.path) {
    const encoded = ds.path.split('/').map(encodeURIComponent).join('/');
    return `https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/main/${encoded}`;
  }
  return '#';
}

async function downloadDataset(ds) {
  if (!ds) return;
  const url = getDatasetDownloadUrl(ds);
  const filename = ds.name || 'dataset.csv';
  isDownloading.value = true;
  emit('show-toast', `Iniciando descarga de ${filename}...`);

  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error(`HTTP error ${response.status}`);
    const blob = await response.blob();
    const blobUrl = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = blobUrl;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(blobUrl);
    emit('show-toast', `Dataset descargado con éxito: ${filename}`);
  } catch (err) {
    console.warn('Descarga por blob falló, aplicando fallback directo:', err);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', filename);
    link.setAttribute('target', '_blank');
    link.setAttribute('rel', 'noopener noreferrer');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    emit('show-toast', `Descarga iniciada: ${filename}`);
  } finally {
    isDownloading.value = false;
  }
}

function copySnippet(ds) {
  if (!ds) return;
  const code = ds.snippet || `df = pd.read_csv('${getDatasetDownloadUrl(ds)}')`;
  if (navigator.clipboard) {
    navigator.clipboard.writeText(code).then(() => {
      emit('show-toast', 'Código de carga en Python copiado al portapapeles.');
    });
  } else {
    emit('show-toast', 'Código: ' + code);
  }
}
</script>

<template>
  <div class="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-black/60 backdrop-blur-sm animate-fade-in" @click.self="emit('close')">
    <div class="glass-panel rounded-2xl w-full max-w-5xl border border-slate-200 dark:border-slate-800 flex flex-col max-h-[90vh] overflow-hidden shadow-2xl">
      
      <!-- Modal Header -->
      <div class="px-5 sm:px-6 py-4 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between bg-slate-50 dark:bg-space-900">
        <div class="flex items-center gap-3">
          <div class="w-9 h-9 rounded-lg bg-brand-cyan/10 border border-brand-cyan/20 flex items-center justify-center text-brand-cyan">
            <span class="material-symbols-outlined text-xl">database</span>
          </div>
          <div>
            <h3 class="text-sm sm:text-base font-semibold text-slate-900 dark:text-slate-100 flex items-center gap-2">
              <span>Explorador de Datasets Oficiales</span>
              <span class="text-[10px] px-2 py-0.5 rounded font-mono bg-slate-200 dark:bg-space-800 text-slate-700 dark:text-slate-300 font-normal">
                {{ datasets.length }} datasets
              </span>
            </h3>
            <p class="text-[11px] text-slate-500 font-mono">
              Conjuntos de datos para modelado estadístico, análisis exploratorio y Machine Learning
            </p>
          </div>
        </div>

        <button 
          @click="emit('close')"
          class="p-1.5 rounded-lg text-slate-400 hover:text-slate-800 dark:hover:text-slate-100 hover:bg-slate-200 dark:hover:bg-space-800 transition-colors"
          title="Cerrar modal (Esc)"
        >
          <span class="material-symbols-outlined text-base">close</span>
        </button>
      </div>

      <!-- Modal Body (2 Columns) -->
      <div class="flex-1 grid grid-cols-1 md:grid-cols-12 overflow-hidden">
        
        <!-- Left: Dataset List & Search -->
        <div class="md:col-span-4 border-r border-slate-200 dark:border-slate-800 flex flex-col bg-slate-50/70 dark:bg-space-950/60 overflow-hidden">
          <!-- Search input -->
          <div class="p-3 border-b border-slate-200 dark:border-slate-800">
            <div class="relative">
              <span class="material-symbols-outlined absolute left-2.5 top-1/2 -translate-y-1/2 text-sm text-slate-400">search</span>
              <input 
                v-model="searchQuery"
                type="text"
                placeholder="Filtrar datasets..."
                class="w-full pl-8 pr-3 py-1.5 rounded-lg bg-white dark:bg-space-900 border border-slate-200 dark:border-slate-800 text-xs font-mono text-slate-900 dark:text-slate-100 placeholder:text-slate-400 focus:outline-none focus:border-brand-cyan transition-colors"
              />
            </div>
          </div>

          <!-- List items -->
          <div class="flex-1 p-2.5 space-y-1.5 overflow-y-auto">
            <div v-if="filteredDatasets.length === 0" class="py-8 text-center text-xs font-mono text-slate-400">
              No se encontraron datasets.
            </div>

            <button 
              v-for="(ds, idx) in filteredDatasets" 
              :key="ds.name"
              @click="selectDataset(idx)"
              class="w-full text-left p-2.5 rounded-lg border transition-all text-xs font-mono group relative"
              :class="selectedDataset?.name === ds.name ? 'bg-white dark:bg-space-850 border-brand-cyan text-slate-900 dark:text-slate-100 font-semibold shadow-xs' : 'bg-transparent border-transparent text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-space-900'"
            >
              <div class="flex items-center justify-between mb-0.5">
                <span class="truncate font-medium pr-2">{{ ds.name }}</span>
                <span class="text-[10px] px-1.5 py-0.2 rounded bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 font-mono shrink-0">
                  CSV
                </span>
              </div>
              <p class="text-[10px] text-slate-500 font-normal line-clamp-1">
                {{ ds.description }}
              </p>
              <div class="flex items-center gap-2 mt-1 text-[10px] text-slate-400 font-normal">
                <span>{{ ds.rows ? ds.rows.toLocaleString() : 'N/A' }} filas</span>
                <span>•</span>
                <span>{{ ds.cols || ds.columns || 'N/A' }} cols</span>
              </div>
            </button>
          </div>
        </div>

        <!-- Right: Dataset Preview Table & Details -->
        <div class="md:col-span-8 p-5 space-y-4 overflow-y-auto bg-white dark:bg-space-900">
          <div v-if="selectedDataset" class="space-y-4">
            
            <!-- Dataset Header & Main Download Button -->
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 pb-4 border-b border-slate-200 dark:border-slate-800">
              <div class="space-y-1">
                <div class="flex items-center gap-2">
                  <span class="material-symbols-outlined text-brand-cyan text-lg">description</span>
                  <h4 class="text-base font-semibold text-slate-900 dark:text-slate-100 font-mono">
                    {{ selectedDataset.name }}
                  </h4>
                  <span class="text-[10px] px-2 py-0.5 rounded-full font-mono font-medium bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20">
                    CSV
                  </span>
                </div>
                <p class="text-xs text-slate-500 dark:text-slate-400">
                  {{ selectedDataset.description }}
                </p>
              </div>

              <!-- Header Action Area: Badges & Download Button -->
              <div class="flex flex-wrap items-center gap-2">
                <div class="flex items-center gap-1.5 font-mono text-[11px]">
                  <span class="px-2 py-1 rounded bg-slate-100 dark:bg-space-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700">
                    {{ selectedDataset.rows ? selectedDataset.rows.toLocaleString() : 'N/A' }} Filas
                  </span>
                  <span class="px-2 py-1 rounded bg-slate-100 dark:bg-space-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700">
                    {{ selectedDataset.cols || selectedDataset.columns || 'N/A' }} Columnas
                  </span>
                </div>

                <!-- Botón Descargar Dataset Principal -->
                <button 
                  @click="downloadDataset(selectedDataset)"
                  :disabled="isDownloading"
                  class="px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 active:bg-emerald-700 text-white font-mono text-xs font-semibold flex items-center gap-1.5 shadow-sm hover:shadow transition-all disabled:opacity-50 cursor-pointer"
                  :title="'Descargar ' + selectedDataset.name"
                >
                  <span class="material-symbols-outlined text-base">
                    {{ isDownloading ? 'sync' : 'download' }}
                  </span>
                  <span>{{ isDownloading ? 'Descargando...' : 'Descargar Dataset' }}</span>
                </button>
              </div>
            </div>

            <!-- Python Code Snippet Box -->
            <div class="bg-slate-900 rounded-lg p-3 text-slate-100 font-mono text-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2.5 border border-slate-800">
              <div class="flex items-center gap-2 overflow-x-auto w-full sm:w-auto">
                <span class="text-brand-cyan select-none">$</span>
                <span class="text-slate-400 select-none">Python:</span>
                <code class="text-emerald-400 text-[11px] whitespace-nowrap">
                  {{ selectedDataset.snippet || `df = pd.read_csv('${getDatasetDownloadUrl(selectedDataset)}')` }}
                </code>
              </div>
              <div class="flex items-center gap-1.5 shrink-0">
                <button 
                  @click="copySnippet(selectedDataset)"
                  class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white text-[11px] flex items-center gap-1 transition-colors"
                  title="Copiar código de carga en Python"
                >
                  <span class="material-symbols-outlined text-xs">content_copy</span>
                  <span>Copiar Snippet</span>
                </button>
                <a 
                  :href="getDatasetDownloadUrl(selectedDataset)"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="p-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition-colors"
                  title="Ver archivo Raw en GitHub"
                >
                  <span class="material-symbols-outlined text-xs">open_in_new</span>
                </a>
              </div>
            </div>

            <!-- Variables & Features Metadata -->
            <div v-if="selectedDataset.target || selectedDataset.features" class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-mono">
              <div v-if="selectedDataset.target" class="p-2.5 rounded-lg bg-slate-50 dark:bg-space-850 border border-slate-200 dark:border-slate-800">
                <span class="text-[10px] text-slate-400 block uppercase tracking-wider mb-0.5">Variable Objetivo (Target):</span>
                <span class="text-brand-cyan font-semibold">{{ selectedDataset.target }}</span>
              </div>
              <div v-if="selectedDataset.features" class="p-2.5 rounded-lg bg-slate-50 dark:bg-space-850 border border-slate-200 dark:border-slate-800">
                <span class="text-[10px] text-slate-400 block uppercase tracking-wider mb-0.5">Características Principales:</span>
                <span class="text-slate-700 dark:text-slate-300 truncate block" :title="selectedDataset.features">{{ selectedDataset.features }}</span>
              </div>
            </div>

            <!-- Sample Data Table -->
            <div class="space-y-2">
              <div class="flex items-center justify-between">
                <span class="font-mono text-xs text-slate-500 uppercase tracking-wider block">
                  Previsualización de Muestra (Primeros Registros)
                </span>
                <span class="font-mono text-[10px] text-slate-400">
                  Formato tabular delimitado
                </span>
              </div>

              <div v-if="selectedDataset.sample_data && selectedDataset.sample_data.length > 0" class="border border-slate-200 dark:border-slate-800 rounded-lg overflow-x-auto shadow-xs">
                <table class="w-full text-left border-collapse font-mono text-xs">
                  <thead>
                    <tr class="bg-slate-100 dark:bg-space-950 border-b border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300">
                      <th v-for="key in Object.keys(selectedDataset.sample_data[0])" :key="key" class="p-2.5 font-semibold whitespace-nowrap bg-slate-100 dark:bg-space-950">
                        {{ key }}
                      </th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-slate-100 dark:divide-slate-800 text-slate-600 dark:text-slate-400">
                    <tr v-for="(row, rIdx) in selectedDataset.sample_data" :key="rIdx" class="hover:bg-slate-50 dark:hover:bg-space-850/60 transition-colors">
                      <td v-for="key in Object.keys(selectedDataset.sample_data[0])" :key="key" class="p-2.5 whitespace-nowrap">
                        {{ row[key] }}
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div v-else class="p-8 text-center border border-dashed border-slate-200 dark:border-slate-800 rounded-lg text-xs font-mono text-slate-500">
                Dataset disponible para descarga inmediata y carga directa mediante <code>pd.read_csv()</code> en los cuadernos.
              </div>
            </div>

          </div>
          <div v-else class="p-12 text-center text-xs font-mono text-slate-400">
            Selecciona un dataset de la lista para visualizar sus detalles y descargarlo.
          </div>
        </div>

      </div>

      <!-- Modal Footer -->
      <div class="px-5 sm:px-6 py-3 border-t border-slate-200 dark:border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-3 bg-slate-50 dark:bg-space-900">
        <div v-if="selectedDataset" class="flex items-center gap-2 w-full sm:w-auto">
          <button 
            @click="downloadDataset(selectedDataset)"
            :disabled="isDownloading"
            class="w-full sm:w-auto px-4 py-1.5 rounded-md bg-emerald-600 hover:bg-emerald-500 text-white font-mono text-xs font-semibold flex items-center justify-center gap-1.5 transition-all shadow-xs"
          >
            <span class="material-symbols-outlined text-sm">download</span>
            <span>Descargar {{ selectedDataset.name }}</span>
          </button>
          <button 
            @click="copySnippet(selectedDataset)"
            class="hidden sm:flex px-3 py-1.5 rounded-md border border-slate-300 dark:border-slate-700 hover:bg-slate-200 dark:hover:bg-space-800 text-slate-700 dark:text-slate-300 font-mono text-xs items-center gap-1 transition-colors"
          >
            <span class="material-symbols-outlined text-sm">content_copy</span>
            <span>Copiar Snippet</span>
          </button>
        </div>
        <div v-else></div>

        <button 
          @click="emit('close')"
          class="w-full sm:w-auto px-4 py-1.5 rounded-md bg-slate-900 dark:bg-slate-100 hover:bg-slate-800 dark:hover:bg-white text-white dark:text-slate-950 font-mono text-xs font-semibold transition-colors"
        >
          Cerrar
        </button>
      </div>

    </div>
  </div>
</template>
