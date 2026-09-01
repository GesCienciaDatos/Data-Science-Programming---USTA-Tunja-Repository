<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  books: {
    type: Array,
    required: true
  }
});

const emit = defineEmits(['open-pdf']);

const searchQuery = ref('');
const selectedCategory = ref('all');

const categories = [
  { id: 'all', name: 'Todos los Libros' },
  { id: 'Para Dummies / Principiantes', name: 'Para Dummies / Principiantes' },
  { id: 'Fundamentos & Estructuras', name: 'Fundamentos & Estructuras' },
  { id: 'Recetas & Buenas Prácticas', name: 'Recetas & Buenas Prácticas' },
  { id: 'Ciencia de Datos & Análisis', name: 'Ciencia de Datos & Análisis' },
  { id: 'Rendimiento & Optimización', name: 'Rendimiento & Optimización' }
];

const filteredBooks = computed(() => {
  let list = props.books || [];

  if (selectedCategory.value !== 'all') {
    list = list.filter(b => b.category === selectedCategory.value || (selectedCategory.value === 'Para Dummies / Principiantes' && b.dummies_friendly));
  }

  if (searchQuery.value.trim() !== '') {
    const q = searchQuery.value.toLowerCase().trim();
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
</script>

<template>
  <div class="space-y-6 py-6 px-4 sm:px-8 max-w-container mx-auto">
    
    <!-- Header Bar -->
    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 pb-3 border-b border-slate-200 dark:border-slate-800">
      <div>
        <h2 class="text-xl font-semibold text-slate-900 dark:text-slate-100 flex items-center gap-2">
          <span class="material-symbols-outlined text-brand-cyan text-lg">menu_book</span>
          Biblioteca Digital de Libros & Referencias
        </h2>
        <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
          Bibliografía especializada en Python, Algoritmos, Machine Learning y Optimización.
        </p>
      </div>

      <!-- Search Input -->
      <div class="relative w-full sm:w-64">
        <span class="material-symbols-outlined absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-400 text-sm">search</span>
        <input 
          v-model="searchQuery"
          type="text" 
          placeholder="Buscar por libro o tema..."
          class="w-full pl-8 pr-3 py-1.5 rounded-md bg-slate-100 dark:bg-space-900 border border-slate-200 dark:border-slate-800 text-xs font-mono text-slate-800 dark:text-slate-200 placeholder:text-slate-400 focus:outline-none focus:border-brand-cyan"
        />
      </div>
    </div>

    <!-- Category Filter Pills -->
    <div class="flex items-center gap-1.5 overflow-x-auto pb-1 font-mono text-xs">
      <button 
        v-for="cat in categories"
        :key="cat.id"
        @click="selectedCategory = cat.id"
        class="px-3 py-1.5 rounded-md transition-colors whitespace-nowrap shrink-0"
        :class="selectedCategory === cat.id ? 'bg-slate-900 dark:bg-slate-100 text-white dark:text-slate-950 font-semibold' : 'bg-slate-100 dark:bg-space-900 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 border border-slate-200 dark:border-slate-800'"
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
          <!-- Category & Size Header -->
          <div class="flex items-center justify-between gap-2 mb-3">
            <span class="font-mono text-[10px] text-brand-cyan font-semibold truncate">
              {{ book.category }}
            </span>
            <div class="flex items-center gap-1.5 shrink-0">
              <span class="px-1.5 py-0.5 rounded text-[9px] font-mono border border-slate-200 dark:border-slate-700 text-slate-500">
                {{ book.size_mb || 'PDF' }}
              </span>
              <span v-if="book.dummies_friendly" class="px-1.5 py-0.5 rounded text-[9px] font-mono bg-brand-amber/10 text-brand-amber border border-brand-amber/30 font-semibold">
                DUMMIES
              </span>
            </div>
          </div>

          <!-- Book Showcase: Cover + Titles -->
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

          <!-- Summary -->
          <p class="text-xs text-slate-600 dark:text-slate-400 line-clamp-3 leading-relaxed mt-3">
            {{ book.summary_dummies || book.subtitle }}
          </p>

          <!-- Topics Tags -->
          <div v-if="book.topics && book.topics.length > 0" class="flex flex-wrap gap-1 mt-3 font-mono text-[10px]">
            <span 
              v-for="topic in book.topics.slice(0, 3)" 
              :key="topic"
              class="px-1.5 py-0.5 rounded bg-slate-100 dark:bg-space-950 text-slate-500 dark:text-slate-400 border border-slate-200 dark:border-slate-800"
            >
              {{ topic }}
            </span>
          </div>
        </div>

        <!-- Action Buttons: Leer PDF / Descargar -->
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

    <!-- Empty State -->
    <div v-else class="py-12 text-center glass-panel rounded-xl border border-slate-200 dark:border-slate-800">
      <span class="material-symbols-outlined text-slate-400 text-3xl mb-2">menu_book</span>
      <h3 class="text-sm font-semibold text-slate-800 dark:text-slate-200">No se encontraron libros</h3>
      <p class="text-xs text-slate-500 mt-0.5">Prueba ajustando el término de búsqueda o la categoría seleccionada.</p>
    </div>

  </div>
</template>
