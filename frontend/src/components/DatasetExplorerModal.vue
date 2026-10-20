<script setup>
import { ref, computed } from 'vue';
import { useI18n } from '../i18n/index.js';

const props = defineProps({
  datasets: {
    type: Array,
    required: true
  }
});

const emit = defineEmits(['close', 'show-toast']);
const { t } = useI18n();

const searchQuery = ref('');
const filterCleaning = ref('all'); // 'all' | 'dirty' | 'clean'
const selectedCourseFilter = ref('all');
const selectedIndex = ref(0);
const isDownloading = ref(false);

const courseCounts = computed(() => {
  const map = {};
  props.datasets.forEach(d => {
    const c = d.course_name || 'General';
    map[c] = (map[c] || 0) + 1;
  });
  return map;
});

const dirtyCount = computed(() => {
  let list = props.datasets;
  if (selectedCourseFilter.value !== 'all') {
    list = list.filter(d => (d.course_name || '') === selectedCourseFilter.value);
  }
  return list.filter(d => d.requires_cleaning).length;
});

const cleanCount = computed(() => {
  let list = props.datasets;
  if (selectedCourseFilter.value !== 'all') {
    list = list.filter(d => (d.course_name || '') === selectedCourseFilter.value);
  }
  return list.filter(d => !d.requires_cleaning).length;
});

const filteredDatasets = computed(() => {
  let list = props.datasets;
  if (selectedCourseFilter.value !== 'all') {
    list = list.filter(d => (d.course_name || '') === selectedCourseFilter.value);
  }
  if (filterCleaning.value === 'dirty') {
    list = list.filter(d => d.requires_cleaning);
  } else if (filterCleaning.value === 'clean') {
    list = list.filter(d => !d.requires_cleaning);
  }

  if (!searchQuery.value.trim()) return list;
  const q = searchQuery.value.toLowerCase().trim();
  return list.filter(ds => 
    (ds.name || '').toLowerCase().includes(q) ||
    (ds.module || '').toLowerCase().includes(q) ||
    (ds.description || '').toLowerCase().includes(q) ||
    (ds.target || '').toLowerCase().includes(q) ||
    (ds.features || '').toLowerCase().includes(q) ||
    (ds.cleaning_status || '').toLowerCase().includes(q)
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
  emit('show-toast', t('toasts.downloadStart', { name: filename }));

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
    emit('show-toast', t('toasts.downloadSuccess', { name: filename }));
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
    emit('show-toast', t('toasts.downloadStart', { name: filename }));
  } finally {
    isDownloading.value = false;
  }
}

function copySnippet(ds) {
  if (!ds) return;
  const code = ds.snippet || `df = pd.read_csv('${getDatasetDownloadUrl(ds)}')`;
  if (navigator.clipboard) {
    navigator.clipboard.writeText(code).then(() => {
      emit('show-toast', t('toasts.snippetCopied'));
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
              <span>{{ t('datasetExplorer.title') }}</span>
              <span class="text-[10px] px-2 py-0.5 rounded font-mono bg-slate-200 dark:bg-space-800 text-slate-700 dark:text-slate-300 font-normal">
                {{ datasets.length }} datasets
              </span>
            </h3>
            <p class="text-[11px] text-slate-500 font-mono">
              {{ t('datasetExplorer.subtitle') }}
            </p>
          </div>
        </div>

        <button 
          @click="emit('close')"
          class="p-1.5 rounded-lg text-slate-400 hover:text-slate-800 dark:hover:text-slate-100 hover:bg-slate-200 dark:hover:bg-space-800 transition-colors cursor-pointer"
          :title="t('common.close') + ' (Esc)'"
        >
          <span class="material-symbols-outlined text-base">close</span>
        </button>
      </div>

      <!-- Modal Body (2 Columns) -->
      <div class="flex-1 grid grid-cols-1 md:grid-cols-12 overflow-hidden">
        
        <!-- Left: Dataset List & Search -->
        <div class="md:col-span-4 border-r border-slate-200 dark:border-slate-800 flex flex-col bg-slate-50/70 dark:bg-space-950/60 overflow-hidden">
          <!-- Search input & Quality Filters -->
          <div class="p-3 border-b border-slate-200 dark:border-slate-800 space-y-2">
            <div class="relative">
              <span class="material-symbols-outlined absolute left-2.5 top-1/2 -translate-y-1/2 text-sm text-slate-400">search</span>
              <input 
                v-model="searchQuery"
                type="text"
                :placeholder="t('datasetExplorer.searchPlaceholder')"
                class="w-full pl-8 pr-3 py-1.5 rounded-lg bg-white dark:bg-space-900 border border-slate-200 dark:border-slate-800 text-xs font-mono text-slate-900 dark:text-slate-100 placeholder:text-slate-400 focus:outline-none focus:border-brand-cyan transition-colors"
              />
            </div>

            <!-- Course Filter Tabs -->
            <div class="flex items-center gap-1 overflow-x-auto text-[10px] font-mono scrollbar-none pb-0.5">
              <button 
                @click="selectedCourseFilter = 'all'; selectedIndex = 0"
                class="px-2 py-0.5 rounded transition-all shrink-0 cursor-pointer"
                :class="selectedCourseFilter === 'all' ? 'bg-brand-cyan/20 text-brand-cyan font-semibold border border-brand-cyan/30' : 'bg-slate-200/70 text-slate-600 dark:bg-space-900 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'"
              >
                {{ t('datasetExplorer.allCourses') }} ({{ datasets.length }})
              </button>
              <button 
                v-for="(cnt, cname) in courseCounts" 
                :key="cname"
                @click="selectedCourseFilter = cname; selectedIndex = 0"
                class="px-2 py-0.5 rounded transition-all shrink-0 cursor-pointer"
                :class="selectedCourseFilter === cname ? 'bg-brand-cyan/20 text-brand-cyan font-semibold border border-brand-cyan/30' : 'bg-slate-200/70 text-slate-600 dark:bg-space-900 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'"
              >
                {{ cname }} ({{ cnt }})
              </button>
            </div>

            <!-- Quality Filter Tabs -->
            <div class="flex items-center gap-1.5 pt-0.5 overflow-x-auto text-[10px] font-mono scrollbar-none">
              <button 
                @click="filterCleaning = 'all'; selectedIndex = 0"
                class="px-2 py-0.5 rounded transition-all shrink-0 cursor-pointer"
                :class="filterCleaning === 'all' ? 'bg-slate-900 text-white dark:bg-slate-100 dark:text-slate-900 font-semibold shadow-xs' : 'bg-slate-200/70 text-slate-600 dark:bg-space-900 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-100'"
              >
                {{ t('datasetExplorer.filterAll') }} ({{ filteredDatasets.length }})
              </button>
              <button 
                @click="filterCleaning = 'dirty'; selectedIndex = 0"
                class="px-2 py-0.5 rounded transition-all shrink-0 flex items-center gap-1 cursor-pointer"
                :class="filterCleaning === 'dirty' ? 'bg-rose-600 text-white font-semibold shadow-xs' : 'bg-rose-500/10 text-rose-600 dark:text-rose-400 border border-rose-500/20 hover:bg-rose-500/20'"
              >
                <span class="w-1.5 h-1.5 rounded-full" :class="filterCleaning === 'dirty' ? 'bg-white' : 'bg-rose-500'"></span>
                {{ t('datasetExplorer.filterDirty') }} ({{ dirtyCount }})
              </button>
              <button 
                @click="filterCleaning = 'clean'; selectedIndex = 0"
                class="px-2 py-0.5 rounded transition-all shrink-0 flex items-center gap-1 cursor-pointer"
                :class="filterCleaning === 'clean' ? 'bg-emerald-600 text-white font-semibold shadow-xs' : 'bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20 hover:bg-emerald-500/20'"
              >
                <span class="w-1.5 h-1.5 rounded-full" :class="filterCleaning === 'clean' ? 'bg-white' : 'bg-emerald-500'"></span>
                {{ t('datasetExplorer.filterClean') }} ({{ cleanCount }})
              </button>
            </div>
          </div>

          <!-- List items -->
          <div class="flex-1 p-2.5 space-y-1.5 overflow-y-auto">
            <div v-if="filteredDatasets.length === 0" class="py-8 text-center text-xs font-mono text-slate-400">
              {{ t('datasetExplorer.emptyList') }}
            </div>

            <button 
              v-for="(ds, idx) in filteredDatasets" 
              :key="ds.path || ds.name"
              @click="selectDataset(idx)"
              class="w-full text-left p-2.5 rounded-lg border transition-all text-xs font-mono group relative cursor-pointer"
              :class="selectedDataset?.path === ds.path || selectedDataset?.name === ds.name ? 'bg-white dark:bg-space-850 border-brand-cyan text-slate-900 dark:text-slate-100 font-semibold shadow-xs' : 'bg-transparent border-transparent text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-space-900'"
            >
              <div class="flex items-center justify-between mb-1 gap-1">
                <span class="truncate font-medium flex-1">{{ ds.name }}</span>
                <div class="flex items-center gap-1 shrink-0">
                  <span 
                    v-if="ds.requires_cleaning" 
                    class="text-[9px] px-1.5 py-0.2 rounded font-mono font-medium bg-rose-500/10 text-rose-600 dark:text-rose-400 border border-rose-500/20"
                    :title="t('datasetExplorer.filterDirty')"
                  >
                    {{ t('datasetExplorer.filterDirty') }}
                  </span>
                  <span 
                    v-else 
                    class="text-[9px] px-1.5 py-0.2 rounded font-mono font-medium bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20"
                    :title="t('datasetExplorer.filterClean')"
                  >
                    {{ t('datasetExplorer.filterClean') }}
                  </span>
                  <span class="text-[9px] px-1 py-0.2 rounded bg-slate-200 dark:bg-space-800 text-slate-700 dark:text-slate-300 font-mono">
                    {{ ds.format || 'CSV' }}
                  </span>
                </div>
              </div>
              <p class="text-[10px] text-slate-500 font-normal line-clamp-1">
                {{ ds.description }}
              </p>
              <div class="flex items-center gap-1.5 mt-1 text-[10px] text-slate-400 font-normal">
                <span v-if="ds.course_name" class="text-brand-cyan truncate max-w-[120px] font-medium">{{ ds.course_name }}</span>
                <span v-if="ds.course_name">•</span>
                <span>{{ ds.rows ? ds.rows.toLocaleString() : 'N/A' }} {{ t('common.rows') }}</span>
                <span>•</span>
                <span>{{ ds.cols || ds.columns || 'N/A' }} {{ t('common.cols') }}</span>
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
                <div class="flex flex-wrap items-center gap-2">
                  <span class="material-symbols-outlined text-brand-cyan text-lg">database</span>
                  <h4 class="text-base font-semibold text-slate-900 dark:text-slate-100 font-mono">
                    {{ selectedDataset.name }}
                  </h4>
                  <span v-if="selectedDataset.course_name" class="text-[10px] px-2 py-0.5 rounded-full font-mono font-medium bg-brand-cyan/10 text-brand-cyan border border-brand-cyan/20">
                    {{ selectedDataset.course_name }}
                  </span>
                  <span class="text-[10px] px-2 py-0.5 rounded-full font-mono font-medium bg-slate-100 dark:bg-space-800 text-slate-700 dark:text-slate-300 border border-slate-300 dark:border-slate-700">
                    {{ selectedDataset.format || 'CSV' }}
                  </span>
                  <!-- Quality Status Badge -->
                  <span 
                    v-if="selectedDataset.requires_cleaning" 
                    class="text-[10px] px-2.5 py-0.5 rounded-full font-mono font-semibold bg-rose-500/10 text-rose-600 dark:text-rose-400 border border-rose-500/20 flex items-center gap-1 shadow-xs"
                  >
                    <span class="w-1.5 h-1.5 rounded-full bg-rose-500 animate-pulse"></span>
                    {{ t('courseWorkspace.cleanBadgeDirty') }}
                  </span>
                  <span 
                    v-else 
                    class="text-[10px] px-2.5 py-0.5 rounded-full font-mono font-semibold bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20 flex items-center gap-1 shadow-xs"
                  >
                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                    {{ t('courseWorkspace.cleanBadgeClean') }}
                  </span>
                </div>
                <p class="text-xs text-slate-500 dark:text-slate-400">
                  {{ selectedDataset.description }}
                </p>
              </div>

              <!-- Header Action Area: Badges & Download Button -->
              <div class="flex flex-wrap items-center gap-2">
                <div class="flex items-center gap-1.5 font-mono text-[11px]">
                  <span class="px-2.5 py-1 rounded bg-slate-100 dark:bg-space-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700">
                    {{ selectedDataset.rows ? selectedDataset.rows.toLocaleString() : 'N/A' }} {{ t('courseWorkspace.rowsCountSuffix') }}
                  </span>
                  <span class="px-2.5 py-1 rounded bg-slate-100 dark:bg-space-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700">
                    {{ selectedDataset.cols || selectedDataset.columns || 'N/A' }} {{ t('courseWorkspace.colsCountSuffix') }}
                  </span>
                </div>

                <!-- Botón Descargar Dataset Principal -->
                <button 
                  @click="downloadDataset(selectedDataset)"
                  :disabled="isDownloading"
                  class="px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 active:bg-emerald-700 text-white font-mono text-xs font-semibold flex items-center gap-1.5 shadow-sm hover:shadow transition-all disabled:opacity-50 cursor-pointer"
                  :title="t('courseWorkspace.btnDownloadDataset') + ' ' + selectedDataset.name"
                >
                  <span class="material-symbols-outlined text-base">
                    {{ isDownloading ? 'sync' : 'download' }}
                  </span>
                  <span>{{ isDownloading ? t('courseWorkspace.btnDownloadingDataset') : t('courseWorkspace.btnDownloadDataset') }}</span>
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
                  class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white text-[11px] flex items-center gap-1 transition-colors cursor-pointer"
                  :title="t('courseWorkspace.btnCopySnippet')"
                >
                  <span class="material-symbols-outlined text-xs">content_copy</span>
                  <span>{{ t('courseWorkspace.btnCopySnippet') }}</span>
                </button>
                <a 
                  :href="getDatasetDownloadUrl(selectedDataset)"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="p-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition-colors"
                  :title="t('courseWorkspace.viewRawGithub')"
                >
                  <span class="material-symbols-outlined text-xs">open_in_new</span>
                </a>
              </div>
            </div>

            <!-- Variables & Features Metadata -->
            <div v-if="selectedDataset.target || selectedDataset.features" class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-mono">
              <div v-if="selectedDataset.target" class="p-2.5 rounded-lg bg-slate-50 dark:bg-space-850 border border-slate-200 dark:border-slate-800">
                <span class="text-[10px] text-slate-400 block uppercase tracking-wider mb-0.5">{{ t('courseWorkspace.targetVariable') }}</span>
                <span class="text-brand-cyan font-semibold">{{ selectedDataset.target }}</span>
              </div>
              <div v-if="selectedDataset.features" class="p-2.5 rounded-lg bg-slate-50 dark:bg-space-850 border border-slate-200 dark:border-slate-800">
                <span class="text-[10px] text-slate-400 block uppercase tracking-wider mb-0.5">{{ t('courseWorkspace.predictorFeatures') }}</span>
                <span class="text-slate-700 dark:text-slate-300 truncate block" :title="selectedDataset.features">{{ selectedDataset.features }}</span>
              </div>
            </div>

            <!-- Quality Diagnostic Card -->
            <div v-if="selectedDataset.requires_cleaning" class="p-3.5 rounded-xl bg-rose-500/5 dark:bg-rose-950/20 border border-rose-500/20 space-y-2 font-mono text-xs">
              <div class="flex items-center justify-between text-rose-600 dark:text-rose-400 font-semibold">
                <div class="flex items-center gap-2">
                  <span class="material-symbols-outlined text-base">warning</span>
                  <span>{{ t('courseWorkspace.qualityDirtyTitle') }}</span>
                </div>
                <span class="text-[10px] px-2 py-0.5 rounded bg-rose-500/10 border border-rose-500/20 uppercase tracking-wider font-semibold">
                  {{ t('courseWorkspace.severityPrefix') }} {{ selectedDataset.cleaning_level || 'Atención' }}
                </span>
              </div>
              <div class="space-y-1">
                <div class="text-[11px] text-slate-700 dark:text-slate-300 font-medium">{{ t('courseWorkspace.reasonsIdentified') }}</div>
                <ul class="list-disc list-inside text-[11px] text-slate-600 dark:text-slate-400 space-y-0.5 pl-1">
                  <li v-for="(reason, rIdx) in selectedDataset.cleaning_reasons" :key="rIdx">
                    {{ reason }}
                  </li>
                </ul>
              </div>
              <div v-if="selectedDataset.cleaning_actions && selectedDataset.cleaning_actions.length > 0" class="pt-2 border-t border-rose-500/15 flex items-start gap-1.5 text-[11px] text-emerald-700 dark:text-emerald-400">
                <span class="material-symbols-outlined text-sm shrink-0">build_circle</span>
                <span><strong>{{ t('courseWorkspace.recommendedAction') }}</strong> {{ selectedDataset.cleaning_actions.join('; ') }}</span>
              </div>
            </div>
            <div v-else class="p-3 rounded-xl bg-emerald-500/5 dark:bg-emerald-950/20 border border-emerald-500/20 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2 font-mono text-xs text-emerald-700 dark:text-emerald-300">
              <div class="flex items-center gap-2">
                <span class="material-symbols-outlined text-base text-emerald-500">verified</span>
                <span>{{ t('courseWorkspace.qualityOptimalMsg') }}</span>
              </div>
              <span class="text-[10px] px-2 py-0.5 rounded bg-emerald-500/10 border border-emerald-500/20 uppercase tracking-wider font-semibold shrink-0">
                {{ t('courseWorkspace.qualityOptimalTitle') }}
              </span>
            </div>

            <!-- Sample Data Table -->
            <div class="space-y-2">
              <div class="flex items-center justify-between">
                <span class="font-mono text-xs text-slate-500 uppercase tracking-wider block">
                  {{ t('courseWorkspace.samplePreviewTitle') }}
                </span>
                <span class="font-mono text-[10px] text-slate-400">
                  {{ t('courseWorkspace.tabularDelimited') }}
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
                {{ t('courseWorkspace.datasetFallbackDesc') }}
              </div>
            </div>

          </div>
          <div v-else class="p-12 text-center text-xs font-mono text-slate-400">
            {{ t('datasetExplorer.emptyList') }}
          </div>
        </div>

      </div>

      <!-- Modal Footer -->
      <div class="px-5 sm:px-6 py-3 border-t border-slate-200 dark:border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-3 bg-slate-50 dark:bg-space-900">
        <div v-if="selectedDataset" class="flex items-center gap-2 w-full sm:w-auto">
          <button 
            @click="downloadDataset(selectedDataset)"
            :disabled="isDownloading"
            class="w-full sm:w-auto px-4 py-1.5 rounded-md bg-emerald-600 hover:bg-emerald-500 text-white font-mono text-xs font-semibold flex items-center justify-center gap-1.5 transition-all shadow-xs cursor-pointer"
          >
            <span class="material-symbols-outlined text-sm">download</span>
            <span>{{ t('courseWorkspace.btnDownloadDataset') }}</span>
          </button>
          <button 
            @click="copySnippet(selectedDataset)"
            class="hidden sm:flex px-3 py-1.5 rounded-md border border-slate-300 dark:border-slate-700 hover:bg-slate-200 dark:hover:bg-space-800 text-slate-700 dark:text-slate-300 font-mono text-xs items-center gap-1 transition-colors cursor-pointer"
          >
            <span class="material-symbols-outlined text-sm">content_copy</span>
            <span>{{ t('courseWorkspace.btnCopySnippet') }}</span>
          </button>
        </div>
        <div v-else></div>

        <button 
          @click="emit('close')"
          class="w-full sm:w-auto px-4 py-1.5 rounded-md bg-slate-900 dark:bg-slate-100 hover:bg-slate-800 dark:hover:bg-white text-white dark:text-slate-950 font-mono text-xs font-semibold transition-colors cursor-pointer"
        >
          {{ t('common.close') }}
        </button>
      </div>

    </div>
  </div>
</template>
