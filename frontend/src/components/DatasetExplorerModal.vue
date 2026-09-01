<script setup>
import { ref } from 'vue';

const props = defineProps({
  datasets: {
    type: Array,
    required: true
  }
});

const emit = defineEmits(['close']);

const selectedIndex = ref(0);
const selectedDataset = ref(props.datasets[0] || null);

function selectDataset(idx) {
  selectedIndex.value = idx;
  selectedDataset.value = props.datasets[idx] || null;
}
</script>

<template>
  <div class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-fade-in">
    <div class="glass-panel rounded-2xl w-full max-w-4xl border border-slate-200 dark:border-slate-800 flex flex-col max-h-[85vh] overflow-hidden shadow-xl">
      
      <!-- Modal Header -->
      <div class="px-6 py-4 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between bg-slate-50 dark:bg-space-900">
        <div class="flex items-center gap-2.5">
          <span class="material-symbols-outlined text-brand-cyan text-lg">database</span>
          <div>
            <h3 class="text-sm font-semibold text-slate-900 dark:text-slate-100">
              Explorador de Datasets Oficiales
            </h3>
            <p class="text-[11px] text-slate-500 font-mono">
              Conjuntos de datos para modelado estadístico y Machine Learning
            </p>
          </div>
        </div>

        <button 
          @click="emit('close')"
          class="p-1.5 rounded-md text-slate-400 hover:text-slate-800 dark:hover:text-slate-100 hover:bg-slate-200 dark:hover:bg-space-800 transition-colors"
          title="Cerrar modal (Esc)"
        >
          <span class="material-symbols-outlined text-base">close</span>
        </button>
      </div>

      <!-- Modal Body (2 Columns) -->
      <div class="flex-1 grid grid-cols-1 md:grid-cols-12 overflow-hidden">
        
        <!-- Left: Dataset List -->
        <div class="md:col-span-4 border-r border-slate-200 dark:border-slate-800 p-3 space-y-1.5 overflow-y-auto bg-slate-50/50 dark:bg-space-950/50">
          <button 
            v-for="(ds, idx) in datasets" 
            :key="ds.name"
            @click="selectDataset(idx)"
            class="w-full text-left p-2.5 rounded-lg border transition-all text-xs font-mono"
            :class="selectedIndex === idx ? 'bg-white dark:bg-space-850 border-brand-cyan text-slate-900 dark:text-slate-100 font-semibold shadow-xs' : 'bg-transparent border-transparent text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-space-900'"
          >
            <div class="flex items-center justify-between mb-0.5">
              <span class="truncate">{{ ds.name }}</span>
              <span class="text-[10px] opacity-75 font-normal">{{ ds.size || 'CSV' }}</span>
            </div>
            <p class="text-[10px] text-slate-500 font-normal line-clamp-1">
              {{ ds.description }}
            </p>
          </button>
        </div>

        <!-- Right: Dataset Preview Table & Details -->
        <div class="md:col-span-8 p-5 space-y-4 overflow-y-auto bg-white dark:bg-space-900">
          <div v-if="selectedDataset" class="space-y-4">
            
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
              <div>
                <h4 class="text-base font-semibold text-slate-900 dark:text-slate-100 font-mono">
                  {{ selectedDataset.name }}
                </h4>
                <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                  {{ selectedDataset.description }}
                </p>
              </div>

              <div class="flex items-center gap-2 font-mono text-[11px]">
                <span class="px-2 py-1 rounded bg-slate-100 dark:bg-space-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700">
                  {{ selectedDataset.rows ? selectedDataset.rows.toLocaleString() : 'N/A' }} Filas
                </span>
                <span class="px-2 py-1 rounded bg-slate-100 dark:bg-space-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700">
                  {{ selectedDataset.columns || 'N/A' }} Columnas
                </span>
              </div>
            </div>

            <!-- Sample Data Table -->
            <div class="space-y-2">
              <span class="font-mono text-xs text-slate-500 uppercase tracking-wider block">
                Previsualización de Muestra (Primeros Registros)
              </span>

              <div v-if="selectedDataset.sample_data && selectedDataset.sample_data.length > 0" class="border border-slate-200 dark:border-slate-800 rounded-lg overflow-x-auto">
                <table class="w-full text-left border-collapse font-mono text-xs">
                  <thead>
                    <tr class="bg-slate-100 dark:bg-space-950 border-b border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300">
                      <th v-for="key in Object.keys(selectedDataset.sample_data[0])" :key="key" class="p-2 font-semibold">
                        {{ key }}
                      </th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-slate-100 dark:divide-slate-800 text-slate-600 dark:text-slate-400">
                    <tr v-for="(row, rIdx) in selectedDataset.sample_data" :key="rIdx" class="hover:bg-slate-50 dark:hover:bg-space-850">
                      <td v-for="key in Object.keys(selectedDataset.sample_data[0])" :key="key" class="p-2 whitespace-nowrap">
                        {{ row[key] }}
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div v-else class="p-8 text-center border border-dashed border-slate-200 dark:border-slate-800 rounded-lg text-xs font-mono text-slate-500">
                Dataset disponible para carga directa mediante <code>pd.read_csv()</code> en los cuadernos del curso.
              </div>
            </div>

          </div>
        </div>

      </div>

      <!-- Modal Footer -->
      <div class="px-6 py-3 border-t border-slate-200 dark:border-slate-800 flex justify-end bg-slate-50 dark:bg-space-900">
        <button 
          @click="emit('close')"
          class="px-4 py-1.5 rounded-md bg-slate-900 dark:bg-slate-100 hover:bg-slate-800 dark:hover:bg-white text-white dark:text-slate-950 font-mono text-xs font-semibold"
        >
          Cerrar
        </button>
      </div>

    </div>
  </div>
</template>
