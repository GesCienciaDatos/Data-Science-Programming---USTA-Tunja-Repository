<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  course: {
    type: Object,
    required: true
  }
});

const emit = defineEmits([
  'return-directory',
  'show-toast',
  'open-pdf',
  'play-video'
]);

// Active Workspace Tab: 'notebooks' | 'books' | 'guias' | 'videos' | 'datasets'
const activeWorkspaceTab = ref('notebooks');

// Notebooks reactive state
const selectedModality = ref('standard'); // 'standard' | 'dummies' | 'homeworks'
const selectedModuleId = ref('all');
const notebookSearchQuery = ref('');
const selectedDifficulty = ref('all');

// Books reactive state
const bookSearchQuery = ref('');
const selectedBookCategory = ref('all');
const bookCategories = [
  { id: 'all', name: 'Todos' },
  { id: 'Para Dummies / Principiantes', name: 'Para Dummies / Principiantes' },
  { id: 'Fundamentos & Estructuras', name: 'Fundamentos & Estructuras' },
  { id: 'Recetas & Buenas Prácticas', name: 'Recetas & Buenas Prácticas' },
  { id: 'Ciencia de Datos & Análisis', name: 'Ciencia de Datos & Análisis' },
  { id: 'Rendimiento & Optimización', name: 'Rendimiento & Optimización' }
];

// Datasets reactive state
const selectedDatasetIndex = ref(0);

// Computed Filters
const filteredNotebooks = computed(() => {
  let list = props.course.notebooks || [];

  // Modality filter
  if (selectedModality.value === 'standard') {
    list = list.filter(n => !n.is_dummies && !n.is_homework && !n.path.includes('homeworks'));
  } else if (selectedModality.value === 'dummies') {
    list = list.filter(n => n.is_dummies === true && !n.is_homework && !n.path.includes('homeworks'));
  } else if (selectedModality.value === 'homeworks') {
    list = list.filter(n => n.is_homework === true || n.path.includes('homeworks'));
  }

  // Module filter
  if (selectedModuleId.value !== 'all') {
    list = list.filter(n => n.module_id === selectedModuleId.value);
  }

  // Difficulty filter
  if (selectedDifficulty.value !== 'all') {
    list = list.filter(n => (n.difficulty || '').toLowerCase().includes(selectedDifficulty.value.toLowerCase()));
  }

  // Search query
  if (notebookSearchQuery.value.trim() !== '') {
    const q = notebookSearchQuery.value.toLowerCase().trim();
    list = list.filter(n => 
      (n.title || '').toLowerCase().includes(q) ||
      (n.path || '').toLowerCase().includes(q) ||
      (n.module_name || '').toLowerCase().includes(q)
    );
  }

  return list;
});

const visibleModules = computed(() => {
  const modules = props.course.modules || [];
  if (selectedModuleId.value !== 'all') {
    return modules.filter(m => m.id === selectedModuleId.value);
  }
  return modules;
});

function getModuleNotebooks(moduleId) {
  return filteredNotebooks.value.filter(n => n.module_id === moduleId);
}

function getModuleTotalCount(moduleId) {
  let list = props.course.notebooks || [];
  if (selectedModality.value === 'dummies') {
    list = list.filter(n => n.is_dummies && n.module_id === moduleId);
  } else if (selectedModality.value === 'homeworks') {
    list = list.filter(n => (n.is_homework || n.path.includes('homeworks')) && n.module_id === moduleId);
  } else {
    list = list.filter(n => !n.is_dummies && !n.is_homework && !n.path.includes('homeworks') && n.module_id === moduleId);
  }
  return list.length;
}

const filteredBooks = computed(() => {
  let list = props.course.books || [];
  if (selectedBookCategory.value !== 'all') {
    list = list.filter(b => b.category === selectedBookCategory.value || (selectedBookCategory.value === 'Para Dummies / Principiantes' && b.dummies_friendly));
  }
  if (bookSearchQuery.value.trim() !== '') {
    const q = bookSearchQuery.value.toLowerCase().trim();
    list = list.filter(b => 
      (b.title || '').toLowerCase().includes(q) ||
      (b.author || '').toLowerCase().includes(q) ||
      (b.subtitle || '').toLowerCase().includes(q) ||
      (b.summary_dummies || '').toLowerCase().includes(q) ||
      (b.topics || []).some(t => t.toLowerCase().includes(q))
    );
  }
  return list;
});

const selectedDataset = computed(() => {
  const dsList = props.course.datasets || [];
  return dsList[selectedDatasetIndex.value] || dsList[0] || null;
});

const isDownloadingDataset = ref(false);

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
  isDownloadingDataset.value = true;
  emit('show-toast', `Iniciando descarga: ${filename}...`);

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
    isDownloadingDataset.value = false;
  }
}

function copyDatasetSnippet(ds) {
  if (!ds) return;
  const code = ds.snippet || `df = pd.read_csv('${getDatasetDownloadUrl(ds)}')`;
  if (navigator.clipboard) {
    navigator.clipboard.writeText(code).then(() => {
      emit('show-toast', 'Código de carga en Python copiado al portapapeles.');
    });
  } else {
    emit('show-toast', 'Snippet: ' + code);
  }
}

function copyColabLink(url) {
  if (navigator.clipboard) {
    navigator.clipboard.writeText(url).then(() => {
      emit('show-toast', 'Enlace Colab copiado al portapapeles.');
    });
  } else {
    emit('show-toast', 'Enlace: ' + url);
  }
}
</script>

<template>
  <div class="space-y-6 py-6 px-4 sm:px-8 max-w-container mx-auto">
    
    <!-- Course Workspace Header Banner -->
    <div class="glass-card rounded-xl p-6 border space-y-4">
      <div class="flex flex-col lg:flex-row justify-between items-start lg:items-center gap-4">
        <div class="space-y-1.5">
          <!-- Breadcrumb -->
          <div class="flex items-center gap-2 font-mono text-xs text-slate-500 dark:text-slate-400">
            <button @click="emit('return-directory')" class="hover:text-brand-cyan transition-colors">
              Plan de Estudios
            </button>
            <span>/</span>
            <span class="text-slate-800 dark:text-slate-200 font-semibold">{{ course.name }}</span>
          </div>

          <h1 class="text-2xl sm:text-3xl font-semibold tracking-tight text-slate-900 dark:text-slate-100">
            {{ course.name }}
          </h1>

          <p class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 max-w-3xl leading-relaxed">
            {{ course.description }}
          </p>
        </div>

        <div class="flex flex-row lg:flex-col items-center lg:items-end gap-3 shrink-0">
          <button 
            @click="emit('return-directory')"
            class="px-3 py-1.5 rounded-md bg-slate-100 dark:bg-space-900 hover:bg-slate-200 dark:hover:bg-space-850 border border-slate-200 dark:border-slate-800 text-xs font-mono text-slate-700 dark:text-slate-300 transition-all flex items-center gap-1.5"
          >
            <span class="material-symbols-outlined text-sm">arrow_back</span>
            <span>Volver al Plan de Estudios</span>
          </button>
          
          <div class="flex items-center gap-3 font-mono text-xs text-slate-500 dark:text-slate-400">
            <span><b class="text-slate-900 dark:text-brand-cyan">{{ (course.notebooks || []).length }}</b> Cuadernos</span>
            <span>•</span>
            <span><b class="text-slate-900 dark:text-slate-100">{{ (course.modules || []).length }}</b> Módulos</span>
          </div>
        </div>
      </div>

      <!-- Resource Navigation Tabs (Inside Course Workspace) -->
      <div class="pt-4 border-t border-slate-200 dark:border-slate-800 flex items-center gap-2 overflow-x-auto font-mono text-xs">
        <button 
          @click="activeWorkspaceTab = 'notebooks'"
          class="px-3.5 py-1.5 rounded-md flex items-center gap-1.5 transition-all whitespace-nowrap"
          :class="activeWorkspaceTab === 'notebooks' ? 'bg-slate-900 dark:bg-slate-100 text-white dark:text-slate-950 font-semibold shadow-xs' : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-100 bg-slate-100 dark:bg-space-900 border border-slate-200 dark:border-slate-800'"
        >
          <span class="material-symbols-outlined text-sm">code</span>
          <span>Cuadernos ({{ (course.notebooks || []).length }})</span>
        </button>

        <button 
          @click="activeWorkspaceTab = 'books'"
          class="px-3.5 py-1.5 rounded-md flex items-center gap-1.5 transition-all whitespace-nowrap"
          :class="activeWorkspaceTab === 'books' ? 'bg-slate-900 dark:bg-slate-100 text-white dark:text-slate-950 font-semibold shadow-xs' : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-100 bg-slate-100 dark:bg-space-900 border border-slate-200 dark:border-slate-800'"
        >
          <span class="material-symbols-outlined text-sm">menu_book</span>
          <span>Libros ({{ (course.books || []).length }})</span>
        </button>

        <button 
          @click="activeWorkspaceTab = 'guias'"
          class="px-3.5 py-1.5 rounded-md flex items-center gap-1.5 transition-all whitespace-nowrap"
          :class="activeWorkspaceTab === 'guias' ? 'bg-slate-900 dark:bg-slate-100 text-white dark:text-slate-950 font-semibold shadow-xs' : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-100 bg-slate-100 dark:bg-space-900 border border-slate-200 dark:border-slate-800'"
        >
          <span class="material-symbols-outlined text-sm">description</span>
          <span>Guías PDF ({{ (course.guias || []).length }})</span>
        </button>

        <button 
          @click="activeWorkspaceTab = 'videos'"
          class="px-3.5 py-1.5 rounded-md flex items-center gap-1.5 transition-all whitespace-nowrap"
          :class="activeWorkspaceTab === 'videos' ? 'bg-slate-900 dark:bg-slate-100 text-white dark:text-slate-950 font-semibold shadow-xs' : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-100 bg-slate-100 dark:bg-space-900 border border-slate-200 dark:border-slate-800'"
        >
          <span class="material-symbols-outlined text-sm">smart_display</span>
          <span>Videos YouTube ({{ (course.videos || []).length }})</span>
        </button>

        <button 
          @click="activeWorkspaceTab = 'datasets'"
          class="px-3.5 py-1.5 rounded-md flex items-center gap-1.5 transition-all whitespace-nowrap"
          :class="activeWorkspaceTab === 'datasets' ? 'bg-slate-900 dark:bg-slate-100 text-white dark:text-slate-950 font-semibold shadow-xs' : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-100 bg-slate-100 dark:bg-space-900 border border-slate-200 dark:border-slate-800'"
        >
          <span class="material-symbols-outlined text-sm">database</span>
          <span>Datasets ({{ (course.datasets || []).length }})</span>
        </button>
      </div>

    </div>

    <!-- ========================================================================= -->
    <!-- TAB 1: CUADERNOS COMPUTACIONALES                                           -->
    <!-- ========================================================================= -->
    <div v-if="activeWorkspaceTab === 'notebooks'" class="space-y-6">
      
      <!-- Modality Selector & Filter Bar (Segmented Control) -->
      <div class="glass-panel rounded-xl p-3 border space-y-3">
        
        <!-- Top Row: Modality Tabs & Search/Difficulty Filter -->
        <div class="flex flex-col lg:flex-row justify-between items-stretch lg:items-center gap-3">
          
          <!-- Segmented Modality Tabs -->
          <div class="flex items-center p-1 rounded-lg bg-slate-100 dark:bg-space-950 border border-slate-200 dark:border-slate-800 font-mono text-xs overflow-x-auto">
            <button 
              @click="selectedModality = 'standard'"
              class="px-3 py-1.5 rounded-md transition-all whitespace-nowrap flex items-center gap-1.5"
              :class="selectedModality === 'standard' ? 'bg-white dark:bg-space-850 text-slate-900 dark:text-brand-cyan font-semibold shadow-xs border border-slate-200 dark:border-slate-700' : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-300'"
            >
              <span class="material-symbols-outlined text-sm">menu_book</span>
              <span>Edición Estándar (Académica)</span>
            </button>
            
            <button 
              @click="selectedModality = 'dummies'"
              class="px-3 py-1.5 rounded-md transition-all whitespace-nowrap flex items-center gap-1.5"
              :class="selectedModality === 'dummies' ? 'bg-white dark:bg-space-850 text-slate-900 dark:text-brand-amber font-semibold shadow-xs border border-slate-200 dark:border-slate-700' : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-300'"
            >
              <span class="material-symbols-outlined text-sm">lightbulb</span>
              <span>Edición Conceptual (Intuitiva)</span>
            </button>

            <button 
              @click="selectedModality = 'homeworks'"
              class="px-3 py-1.5 rounded-md transition-all whitespace-nowrap flex items-center gap-1.5"
              :class="selectedModality === 'homeworks' ? 'bg-white dark:bg-space-850 text-slate-900 dark:text-brand-emerald font-semibold shadow-xs border border-slate-200 dark:border-slate-700' : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-300'"
            >
              <span class="material-symbols-outlined text-sm">science</span>
              <span>Laboratorios Prácticos (Hands-On)</span>
            </button>
          </div>

          <!-- Filter and Search Inputs -->
          <div class="flex items-center gap-2.5">
            <div class="relative flex-1 sm:w-56">
              <span class="material-symbols-outlined absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-400 text-sm">search</span>
              <input 
                v-model="notebookSearchQuery"
                type="text" 
                placeholder="Buscar cuaderno..."
                class="w-full pl-8 pr-3 py-1.5 rounded-md bg-slate-100 dark:bg-space-950 border border-slate-200 dark:border-slate-800 text-xs font-mono text-slate-800 dark:text-slate-200 placeholder:text-slate-400 focus:outline-none focus:border-brand-cyan"
              />
            </div>

            <select 
              v-model="selectedDifficulty"
              class="px-3 py-1.5 rounded-md bg-slate-100 dark:bg-space-950 border border-slate-200 dark:border-slate-800 text-xs font-mono text-slate-700 dark:text-slate-300 focus:outline-none focus:border-brand-cyan"
            >
              <option value="all">Todas las Dificultades</option>
              <option value="Principiante">Principiante</option>
              <option value="Intermedio">Intermedio</option>
              <option value="Avanzado">Avanzado</option>
            </select>
          </div>

        </div>

        <!-- Module Filter Pills -->
        <div class="flex items-center gap-1.5 overflow-x-auto pb-1 font-mono text-xs">
          <button 
            @click="selectedModuleId = 'all'"
            class="px-2.5 py-1 rounded-md transition-colors whitespace-nowrap flex items-center gap-1 shrink-0"
            :class="selectedModuleId === 'all' ? 'bg-slate-900 dark:bg-slate-100 text-white dark:text-slate-950 font-semibold' : 'bg-slate-100 dark:bg-space-900 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 border border-slate-200 dark:border-slate-800'"
          >
            <span>Todos los Módulos</span>
            <span class="text-[10px] opacity-75">({{ filteredNotebooks.length }})</span>
          </button>

          <button 
            v-for="mod in course.modules" 
            :key="mod.id"
            @click="selectedModuleId = mod.id"
            class="px-2.5 py-1 rounded-md transition-colors whitespace-nowrap flex items-center gap-1 shrink-0"
            :class="selectedModuleId === mod.id ? 'bg-slate-900 dark:bg-slate-100 text-white dark:text-slate-950 font-semibold' : 'bg-slate-100 dark:bg-space-900 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 border border-slate-200 dark:border-slate-800'"
          >
            <span>{{ mod.name }}</span>
            <span class="text-[10px] opacity-75">({{ getModuleTotalCount(mod.id) }})</span>
          </button>
        </div>

      </div>

      <!-- Modules and Notebook List -->
      <div v-if="filteredNotebooks.length > 0" class="space-y-8">
        <div 
          v-for="mod in visibleModules" 
          :key="mod.id"
          v-show="getModuleNotebooks(mod.id).length > 0"
          class="space-y-3"
        >
          <!-- Module Header -->
          <div class="flex items-center justify-between gap-3 pb-2 border-b border-slate-200 dark:border-slate-800">
            <div class="space-y-0.5">
              <h3 class="text-base font-semibold text-slate-900 dark:text-slate-100">
                {{ mod.name }}
              </h3>
              <p class="text-xs text-slate-500 dark:text-slate-400">
                {{ mod.description }}
              </p>
            </div>
            <span class="font-mono text-xs text-slate-400">
              {{ getModuleNotebooks(mod.id).length }} {{ getModuleNotebooks(mod.id).length === 1 ? 'cuaderno' : 'cuadernos' }}
            </span>
          </div>

          <!-- Notebook Cards Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            <div 
              v-for="(nb, nIdx) in getModuleNotebooks(mod.id)"
              :key="nb.path"
              class="glass-card rounded-lg p-4 border flex flex-col justify-between transition-all duration-200 hover:border-slate-300 dark:hover:border-slate-700"
            >
              <div>
                <div class="flex items-center justify-between gap-2 mb-2">
                  <span class="font-mono text-[10px] text-brand-cyan font-semibold">
                    #{{ String(nIdx + 1).padStart(2, '0') }}
                  </span>
                  
                  <div class="flex items-center gap-1.5">
                    <span class="px-1.5 py-0.5 rounded text-[9px] font-mono border border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-400 font-medium">
                      {{ nb.difficulty }}
                    </span>
                    <span v-if="nb.is_dummies" class="px-1.5 py-0.5 rounded text-[9px] font-mono bg-brand-amber/10 text-brand-amber border border-brand-amber/30 font-semibold">
                      DUMMIES
                    </span>
                    <span v-if="nb.is_homework || nb.path.includes('homeworks')" class="px-1.5 py-0.5 rounded text-[9px] font-mono bg-brand-emerald/10 text-brand-emerald border border-brand-emerald/30 font-semibold">
                      LAB
                    </span>
                  </div>
                </div>

                <h4 class="text-xs sm:text-sm font-semibold text-slate-900 dark:text-slate-100 leading-snug mb-1">
                  {{ nb.title }}
                </h4>

                <p class="font-mono text-[10px] text-slate-500 dark:text-slate-400 truncate">
                  {{ nb.path }}
                </p>
              </div>

              <!-- Action Buttons -->
              <div class="pt-3 mt-3 border-t border-slate-200 dark:border-slate-800/80 flex items-center justify-between gap-2">
                <a 
                  :href="nb.colab_url" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  class="px-2.5 py-1 rounded bg-slate-900 dark:bg-slate-100 hover:bg-slate-800 dark:hover:bg-white text-white dark:text-slate-950 font-mono text-[10px] font-semibold flex items-center gap-1 transition-all"
                >
                  <span>COLAB</span>
                  <span class="material-symbols-outlined text-xs">rocket_launch</span>
                </a>

                <div class="flex items-center gap-1 text-slate-500 dark:text-slate-400">
                  <a 
                    :href="nb.github_url" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    class="p-1 rounded hover:bg-slate-100 dark:hover:bg-space-850 hover:text-slate-900 dark:hover:text-slate-100 transition-colors"
                    title="Ver Código Fuente"
                  >
                    <span class="material-symbols-outlined text-sm">code</span>
                  </a>
                  <button 
                    @click="copyColabLink(nb.colab_url)"
                    class="p-1 rounded hover:bg-slate-100 dark:hover:bg-space-850 hover:text-slate-900 dark:hover:text-slate-100 transition-colors"
                    title="Copiar Enlace Colab"
                  >
                    <span class="material-symbols-outlined text-sm">content_copy</span>
                  </button>
                </div>
              </div>

            </div>
          </div>

        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="py-12 text-center glass-panel rounded-xl border border-slate-200 dark:border-slate-800">
        <span class="material-symbols-outlined text-slate-400 text-3xl mb-2">search_off</span>
        <h3 class="text-sm font-semibold text-slate-800 dark:text-slate-200">No se encontraron cuadernos</h3>
        <p class="text-xs text-slate-500 mt-0.5">Prueba ajustando el término de búsqueda o la modalidad seleccionada.</p>
      </div>

    </div>

    <!-- ========================================================================= -->
    <!-- TAB 2: BIBLIOTECA DIGITAL DE LIBROS                                       -->
    <!-- ========================================================================= -->
    <div v-else-if="activeWorkspaceTab === 'books'" class="space-y-6">
      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
        <div>
          <h3 class="text-lg font-semibold text-slate-900 dark:text-slate-100">
            Biblioteca Digital de Referencia
          </h3>
          <p class="text-xs text-slate-500">Bibliografía técnica oficial y libros de soporte.</p>
        </div>

        <div class="relative w-full sm:w-64">
          <span class="material-symbols-outlined absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-400 text-sm">search</span>
          <input 
            v-model="bookSearchQuery"
            type="text" 
            placeholder="Buscar por libro..."
            class="w-full pl-8 pr-3 py-1.5 rounded-md bg-slate-100 dark:bg-space-900 border border-slate-200 dark:border-slate-800 text-xs font-mono text-slate-800 dark:text-slate-200 placeholder:text-slate-400 focus:outline-none focus:border-brand-cyan"
          />
        </div>
      </div>

      <!-- Category Filter Pills -->
      <div class="flex items-center gap-1.5 overflow-x-auto pb-1 font-mono text-xs">
        <button 
          v-for="cat in bookCategories"
          :key="cat.id"
          @click="selectedBookCategory = cat.id"
          class="px-3 py-1.5 rounded-md transition-colors whitespace-nowrap shrink-0"
          :class="selectedBookCategory === cat.id ? 'bg-slate-900 dark:bg-slate-100 text-white dark:text-slate-950 font-semibold' : 'bg-slate-100 dark:bg-space-900 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 border border-slate-200 dark:border-slate-800'"
        >
          {{ cat.name }}
        </button>
      </div>

      <!-- Books Grid -->
      <div v-if="filteredBooks.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        <div 
          v-for="book in filteredBooks" 
          :key="book.id"
          class="glass-card rounded-xl p-5 border flex flex-col justify-between transition-all duration-200 hover:border-slate-300 dark:hover:border-slate-700 space-y-4"
        >
          <div>
            <div class="flex items-center justify-between gap-2 mb-3">
              <span class="font-mono text-[10px] text-brand-cyan font-semibold truncate">
                {{ book.category }}
              </span>
              <span class="px-1.5 py-0.5 rounded text-[9px] font-mono border border-slate-200 dark:border-slate-700 text-slate-500">
                {{ book.size_mb || 'PDF' }}
              </span>
            </div>

            <div class="flex items-start gap-4">
              <div class="w-20 h-28 rounded-md bg-slate-800 shrink-0 overflow-hidden border border-slate-700 shadow-sm flex items-center justify-center text-center p-1">
                <img 
                  v-if="book.cover_image"
                  :src="book.cover_image" 
                  :alt="book.title"
                  class="w-full h-full object-cover"
                  onerror="this.style.display='none'"
                />
                <span class="material-symbols-outlined text-slate-500 text-2xl" v-else>
                  menu_book
                </span>
              </div>

              <div class="space-y-1 overflow-hidden">
                <h4 class="text-sm font-semibold text-slate-900 dark:text-slate-100 leading-snug">
                  {{ book.title }}
                </h4>
                <p class="text-xs text-slate-500 dark:text-slate-400 font-medium">
                  {{ book.author }}
                </p>
                <p class="font-mono text-[10px] text-slate-400">
                  {{ book.publisher }} • {{ book.year }}
                </p>
              </div>
            </div>

            <p class="text-xs text-slate-600 dark:text-slate-400 line-clamp-3 leading-relaxed mt-3">
              {{ book.summary_dummies || book.subtitle }}
            </p>
          </div>

          <div class="pt-3 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between gap-2">
            <button 
              @click="emit('open-pdf', book)"
              class="px-3 py-1.5 rounded-md bg-slate-900 dark:bg-slate-100 hover:bg-slate-800 dark:hover:bg-white text-white dark:text-slate-950 font-mono text-xs font-semibold flex items-center gap-1.5 transition-all shadow-xs"
            >
              <span class="material-symbols-outlined text-sm">visibility</span>
              <span>LEER EN VISOR</span>
            </button>

            <a 
              :href="book.download_url || book.pdf_url" 
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
    </div>

    <!-- ========================================================================= -->
    <!-- TAB 3: GUÍAS DE LABORATORIO PDF                                           -->
    <!-- ========================================================================= -->
    <div v-else-if="activeWorkspaceTab === 'guias'" class="space-y-6">
      <div class="pb-3 border-b border-slate-200 dark:border-slate-800">
        <h3 class="text-lg font-semibold text-slate-900 dark:text-slate-100">
          Guías Técnicas & Manuales de Laboratorio
        </h3>
        <p class="text-xs text-slate-500">Documentos oficiales de configuración y metodología.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        <div 
          v-for="guia in course.guias" 
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
    </div>

    <!-- ========================================================================= -->
    <!-- TAB 4: VIDEOS Y MASTERCLASSES                                             -->
    <!-- ========================================================================= -->
    <div v-else-if="activeWorkspaceTab === 'videos'" class="space-y-6">
      <div class="pb-3 border-b border-slate-200 dark:border-slate-800">
        <h3 class="text-lg font-semibold text-slate-900 dark:text-slate-100">
          Masterclasses & Talleres en Video
        </h3>
        <p class="text-xs text-slate-500">Sesiones grabadas y explicaciones en YouTube.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        <div 
          v-for="v in course.videos" 
          :key="v.id"
          class="glass-card rounded-xl p-4 border flex flex-col justify-between transition-all duration-200 hover:border-slate-300 dark:hover:border-slate-700 space-y-3 group"
        >
          <div class="space-y-3">
            <div 
              @click="emit('play-video', v)"
              class="relative w-full aspect-video rounded-lg overflow-hidden bg-slate-900 border border-slate-700/80 cursor-pointer shadow-sm group-hover:border-brand-cyan transition-colors"
            >
              <img 
                v-if="v.thumbnail"
                :src="v.thumbnail" 
                :alt="v.title" 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
              />
              <div class="absolute inset-0 bg-black/40 flex items-center justify-center group-hover:bg-black/20 transition-colors">
                <div class="w-12 h-12 rounded-full bg-rose-600/90 text-white flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform">
                  <span class="material-symbols-outlined text-2xl">play_arrow</span>
                </div>
              </div>
            </div>

            <div class="space-y-1">
              <div class="flex items-center justify-between gap-2">
                <span class="font-mono text-[10px] text-brand-cyan font-semibold">
                  {{ v.module || 'Masterclass' }}
                </span>
                <span class="px-1.5 py-0.5 rounded text-[9px] font-mono border border-slate-200 dark:border-slate-700 text-slate-500">
                  {{ v.size_mb ? `${v.size_mb} MB` : 'YouTube HD' }}
                </span>
              </div>

              <h4 class="text-sm font-semibold text-slate-900 dark:text-slate-100 leading-snug group-hover:text-brand-cyan transition-colors">
                {{ v.title }}
              </h4>
            </div>
          </div>

          <div class="pt-3 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between gap-2">
            <button 
              @click="emit('play-video', v)"
              class="px-3 py-1.5 rounded-md bg-slate-900 dark:bg-slate-100 hover:bg-slate-800 dark:hover:bg-white text-white dark:text-slate-950 font-mono text-xs font-semibold flex items-center gap-1.5 transition-all shadow-xs"
            >
              <span class="material-symbols-outlined text-sm">play_circle</span>
              <span>REPRODUCIR VIDEO</span>
            </button>

            <a 
              v-if="v.youtube_url"
              :href="v.youtube_url" 
              target="_blank" 
              rel="noopener noreferrer"
              class="p-1.5 rounded-md bg-slate-100 dark:bg-space-900 hover:bg-slate-200 dark:hover:bg-space-850 text-slate-600 dark:text-slate-300 transition-colors"
              title="Abrir en YouTube"
            >
              <span class="material-symbols-outlined text-base">open_in_new</span>
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- ========================================================================= -->
    <!-- TAB 5: DATASETS                                                           -->
    <!-- ========================================================================= -->
    <div v-else-if="activeWorkspaceTab === 'datasets'" class="space-y-6">
      <div class="pb-3 border-b border-slate-200 dark:border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h3 class="text-lg font-semibold text-slate-900 dark:text-slate-100 flex items-center gap-2">
            <span>Datasets Oficiales de la Asignatura</span>
            <span class="text-xs px-2 py-0.5 rounded font-mono bg-slate-100 dark:bg-space-800 text-slate-700 dark:text-slate-300 font-medium">
              {{ (course.datasets || []).length }} disponibles
            </span>
          </h3>
          <p class="text-xs text-slate-500 mt-0.5">
            Conjuntos de datos estructurados para experimentación estadística, feature engineering y Machine Learning.
          </p>
        </div>

        <div v-if="selectedDataset" class="flex items-center gap-2">
          <button 
            @click="downloadDataset(selectedDataset)"
            :disabled="isDownloadingDataset"
            class="px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 active:bg-emerald-700 text-white font-mono text-xs font-semibold flex items-center gap-2 shadow-xs hover:shadow transition-all disabled:opacity-50 cursor-pointer"
            :title="'Descargar ' + selectedDataset.name"
          >
            <span class="material-symbols-outlined text-base">
              {{ isDownloadingDataset ? 'sync' : 'download' }}
            </span>
            <span>{{ isDownloadingDataset ? 'Descargando...' : 'Descargar Dataset' }}</span>
          </button>
        </div>
      </div>

      <!-- If course has no datasets -->
      <div v-if="!course.datasets || course.datasets.length === 0" class="p-12 text-center border border-dashed border-slate-200 dark:border-slate-800 rounded-xl space-y-2 font-mono text-xs text-slate-500">
        <span class="material-symbols-outlined text-3xl text-slate-400">database</span>
        <p>No hay datasets registrados actualmente para esta asignatura.</p>
      </div>

      <div v-else class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <!-- Left: Datasets Selector -->
        <div class="lg:col-span-4 space-y-2">
          <button 
            v-for="(ds, idx) in course.datasets"
            :key="ds.name"
            @click="selectedDatasetIndex = idx"
            class="w-full text-left p-3 rounded-lg border transition-all text-xs font-mono group relative"
            :class="selectedDatasetIndex === idx ? 'bg-white dark:bg-space-850 border-brand-cyan text-slate-900 dark:text-slate-100 font-semibold shadow-xs' : 'bg-slate-50 dark:bg-space-950 border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-space-900'"
          >
            <div class="flex items-center justify-between mb-1">
              <span class="truncate pr-2 font-medium">{{ ds.name }}</span>
              <span class="text-[10px] px-1.5 py-0.2 rounded bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 shrink-0 font-medium">
                CSV
              </span>
            </div>
            <p class="text-[10px] text-slate-500 line-clamp-1 font-normal mb-1.5">
              {{ ds.description }}
            </p>
            <div class="flex items-center justify-between text-[10px] text-slate-400 font-normal">
              <span>{{ ds.rows ? ds.rows.toLocaleString() : 'N/A' }} filas • {{ ds.cols || ds.columns || 'N/A' }} cols</span>
              <span 
                @click.stop="downloadDataset(ds)"
                class="hover:text-emerald-500 transition-colors p-0.5 rounded"
                title="Descargar este archivo CSV"
              >
                <span class="material-symbols-outlined text-sm">download</span>
              </span>
            </div>
          </button>
        </div>

        <!-- Right: Dataset Preview & Action Details -->
        <div class="lg:col-span-8 glass-card rounded-xl p-5 border space-y-5">
          <div v-if="selectedDataset" class="space-y-5">
            
            <!-- Dataset Header & Action Bar -->
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 pb-4 border-b border-slate-200 dark:border-slate-800">
              <div class="space-y-1">
                <div class="flex items-center gap-2">
                  <span class="material-symbols-outlined text-brand-cyan text-lg">database</span>
                  <h4 class="text-base font-semibold text-slate-900 dark:text-slate-100 font-mono">
                    {{ selectedDataset.name }}
                  </h4>
                  <span class="text-[10px] px-2 py-0.5 rounded-full font-mono font-medium bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20">
                    CSV
                  </span>
                </div>
                <p class="text-xs text-slate-500 dark:text-slate-400">{{ selectedDataset.description }}</p>
              </div>

              <!-- Action Buttons & Badges -->
              <div class="flex flex-wrap items-center gap-2">
                <div class="flex items-center gap-1.5 font-mono text-[11px]">
                  <span class="px-2.5 py-1 rounded bg-slate-100 dark:bg-space-800 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300">
                    {{ selectedDataset.rows ? selectedDataset.rows.toLocaleString() : 'N/A' }} Filas
                  </span>
                  <span class="px-2.5 py-1 rounded bg-slate-100 dark:bg-space-800 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300">
                    {{ selectedDataset.cols || selectedDataset.columns || 'N/A' }} Columnas
                  </span>
                </div>

                <!-- Botón Principal Descargar Dataset -->
                <button 
                  @click="downloadDataset(selectedDataset)"
                  :disabled="isDownloadingDataset"
                  class="px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 active:bg-emerald-700 text-white font-mono text-xs font-semibold flex items-center gap-2 shadow-sm hover:shadow transition-all disabled:opacity-50 cursor-pointer"
                  :title="'Descargar ' + selectedDataset.name + ' en formato CSV'"
                >
                  <span class="material-symbols-outlined text-base">
                    {{ isDownloadingDataset ? 'sync' : 'download' }}
                  </span>
                  <span>{{ isDownloadingDataset ? 'Descargando...' : 'Descargar Dataset' }}</span>
                </button>
              </div>
            </div>

            <!-- Python Code Snippet Box -->
            <div class="bg-slate-900 rounded-lg p-3 text-slate-100 font-mono text-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2.5 border border-slate-800 shadow-inner">
              <div class="flex items-center gap-2 overflow-x-auto w-full sm:w-auto">
                <span class="text-brand-cyan select-none">$</span>
                <span class="text-slate-400 select-none">Python:</span>
                <code class="text-emerald-400 text-[11px] whitespace-nowrap">
                  {{ selectedDataset.snippet || `df = pd.read_csv('${getDatasetDownloadUrl(selectedDataset)}')` }}
                </code>
              </div>
              <div class="flex items-center gap-1.5 shrink-0">
                <button 
                  @click="copyDatasetSnippet(selectedDataset)"
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
                <span class="text-[10px] text-slate-400 block uppercase tracking-wider mb-0.5">Variables Predictoras / Features:</span>
                <span class="text-slate-700 dark:text-slate-300 truncate block" :title="selectedDataset.features">{{ selectedDataset.features }}</span>
              </div>
            </div>

            <!-- Table Preview -->
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
                Dataset disponible para descarga inmediata y carga directa mediante <code>pd.read_csv()</code> en los cuadernos del curso.
              </div>
            </div>

            <!-- Bottom Action Footer Strip -->
            <div class="pt-3 border-t border-slate-200 dark:border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-3 font-mono text-xs">
              <span class="text-slate-500 text-[11px]">
                Archivo: <span class="text-slate-900 dark:text-slate-200 font-semibold">{{ selectedDataset.name }}</span> ({{ selectedDataset.rows ? selectedDataset.rows.toLocaleString() : 'N/A' }} filas)
              </span>
              <div class="flex items-center gap-2 w-full sm:w-auto">
                <button 
                  @click="copyDatasetSnippet(selectedDataset)"
                  class="px-3 py-1.5 rounded-lg border border-slate-300 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-space-800 text-slate-700 dark:text-slate-300 transition-colors flex items-center gap-1.5"
                >
                  <span class="material-symbols-outlined text-sm">content_copy</span>
                  <span>Copiar Snippet</span>
                </button>
                <button 
                  @click="downloadDataset(selectedDataset)"
                  :disabled="isDownloadingDataset"
                  class="px-4 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 active:bg-emerald-700 text-white font-semibold flex items-center gap-1.5 transition-all shadow-xs"
                >
                  <span class="material-symbols-outlined text-sm">download</span>
                  <span>Descargar Dataset</span>
                </button>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>

  </div>
</template>
