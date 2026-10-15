<script setup>
import { ref, computed, onMounted } from 'vue';

const props = defineProps({
  allNotebooks: {
    type: Array,
    required: true
  },
  allBooks: {
    type: Array,
    default: () => []
  },
  allVideos: {
    type: Array,
    default: () => []
  }
});

const emit = defineEmits(['close', 'open-pdf', 'play-video']);

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
    (nb.module_name || '').toLowerCase().includes(q) ||
    (nb.course_name || '').toLowerCase().includes(q)
  ).slice(0, 12);
});

const searchBookResults = computed(() => {
  if (query.value.trim().length < 2 || !props.allBooks) return [];
  const q = query.value.toLowerCase().trim();

  return props.allBooks.filter(b => 
    (b.title || '').toLowerCase().includes(q) ||
    (b.author || '').toLowerCase().includes(q) ||
    (b.subtitle || '').toLowerCase().includes(q) ||
    (b.subject || '').toLowerCase().includes(q) ||
    (b.category || '').toLowerCase().includes(q) ||
    (b.topics || []).some(t => t.toLowerCase().includes(q))
  ).slice(0, 6);
});

const searchVideoResults = computed(() => {
  if (query.value.trim().length < 2 || !props.allVideos) return [];
  const q = query.value.toLowerCase().trim();

  return props.allVideos.filter(v => 
    (v.title || '').toLowerCase().includes(q) ||
    (v.module || '').toLowerCase().includes(q) ||
    (v.filename || '').toLowerCase().includes(q)
  ).slice(0, 4);
});

function handleOpenBook(book) {
  emit('open-pdf', book);
  emit('close');
}

function handlePlayVideo(video) {
  emit('play-video', video);
  emit('close');
}
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
      <div class="p-3 max-h-[60vh] overflow-y-auto space-y-4 bg-slate-50 dark:bg-space-950">
        <div v-if="query.trim().length < 2" class="py-8 text-center text-xs font-mono text-slate-400">
          Escribe al menos 2 caracteres para buscar en cuadernos, libros y videos masterclasses.
        </div>

        <div v-else-if="searchResults.length === 0 && searchBookResults.length === 0 && searchVideoResults.length === 0" class="py-8 text-center text-xs font-mono text-slate-400">
          No se encontraron coincidencias para "{{ query }}".
        </div>

        <div v-else class="space-y-4">
          <!-- Videos Matches Section -->
          <div v-if="searchVideoResults.length > 0" class="space-y-2">
            <div class="flex items-center gap-2 px-1 font-mono text-[11px] text-rose-500 uppercase tracking-wider font-semibold">
              <span class="material-symbols-outlined text-sm text-rose-500">smart_display</span>
              <span>Masterclasses & Videos YouTube ({{ searchVideoResults.length }})</span>
            </div>

            <div 
              v-for="v in searchVideoResults"
              :key="v.id"
              class="p-3 rounded-lg bg-white dark:bg-space-900 border border-slate-200 dark:border-slate-800 flex items-center justify-between gap-3 hover:border-rose-500/50 transition-all"
            >
              <div class="flex items-center gap-3 overflow-hidden">
                <div 
                  @click="handlePlayVideo(v)"
                  class="w-16 h-10 rounded bg-slate-900 border border-slate-700/80 overflow-hidden shrink-0 flex items-center justify-center relative cursor-pointer group"
                >
                  <img 
                    v-if="v.thumbnail" 
                    :src="v.thumbnail" 
                    :alt="v.title" 
                    class="w-full h-full object-cover group-hover:scale-105 transition-transform" 
                  />
                  <span class="material-symbols-outlined absolute inset-0 flex items-center justify-center text-white text-sm bg-black/30 group-hover:bg-black/10">
                    play_circle
                  </span>
                </div>
                <div class="space-y-0.5 overflow-hidden">
                  <div class="flex items-center gap-1.5 font-mono text-[10px] text-rose-500 font-semibold">
                    <span>{{ v.module || 'Masterclass' }}</span>
                  </div>
                  <h5 class="text-xs font-semibold text-slate-900 dark:text-slate-100 truncate">
                    {{ v.title }}
                  </h5>
                </div>
              </div>

              <button 
                @click="handlePlayVideo(v)"
                class="px-2.5 py-1 rounded bg-rose-600 hover:bg-rose-500 text-white font-mono text-[10px] font-semibold shrink-0 flex items-center gap-1 cursor-pointer"
              >
                <span>VER</span>
                <span class="material-symbols-outlined text-xs">play_arrow</span>
              </button>
            </div>
          </div>

          <!-- Notebooks Matches Section -->
          <div v-if="searchResults.length > 0" class="space-y-2">
            <div class="flex items-center gap-2 px-1 font-mono text-[11px] text-slate-500 uppercase tracking-wider font-semibold">
              <span class="material-symbols-outlined text-sm text-brand-cyan">code</span>
              <span>Cuadernos Computacionales ({{ searchResults.length }})</span>
            </div>

            <div 
              v-for="nb in searchResults"
              :key="nb.path"
              class="p-3 rounded-lg bg-white dark:bg-space-900 border border-slate-200 dark:border-slate-800 flex items-center justify-between gap-3 hover:border-brand-cyan transition-all"
            >
              <div class="space-y-0.5 overflow-hidden">
                <div class="flex items-center gap-1.5 font-mono text-[10px] text-brand-cyan font-semibold">
                  <span v-if="nb.course_name" class="text-slate-500 dark:text-slate-400 font-normal">{{ nb.course_name }} •</span>
                  <span>{{ nb.module_name }}</span>
                </div>
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

          <!-- Books Matches Section -->
          <div v-if="searchBookResults.length > 0" class="space-y-2">
            <div class="flex items-center gap-2 px-1 font-mono text-[11px] text-amber-600 dark:text-brand-amber uppercase tracking-wider font-semibold">
              <span class="material-symbols-outlined text-sm">menu_book</span>
              <span>Libros de Referencia & Bibliografía ({{ searchBookResults.length }})</span>
            </div>

            <div 
              v-for="book in searchBookResults"
              :key="book.id"
              class="p-3 rounded-lg bg-white dark:bg-space-900 border border-slate-200 dark:border-slate-800 flex items-center justify-between gap-3 hover:border-brand-amber transition-all"
            >
              <div class="flex items-center gap-3 overflow-hidden">
                <div class="w-8 h-11 rounded bg-slate-100 dark:bg-space-950 border border-slate-200 dark:border-slate-800 overflow-hidden shrink-0 flex items-center justify-center">
                  <img 
                    v-if="book.cover_image" 
                    :src="book.cover_image" 
                    :alt="book.title" 
                    class="w-full h-full object-cover" 
                  />
                  <span v-else class="material-symbols-outlined text-sm text-slate-400">menu_book</span>
                </div>
                <div class="space-y-0.5 overflow-hidden">
                  <div class="flex items-center gap-1.5 font-mono text-[10px] text-brand-amber font-semibold">
                    <span>{{ book.subject || 'Especialización' }}</span>
                    <span>•</span>
                    <span class="text-slate-500 font-normal">{{ book.author }}</span>
                  </div>
                  <h5 class="text-xs font-semibold text-slate-900 dark:text-slate-100 truncate">
                    {{ book.title }}
                  </h5>
                  <p class="font-mono text-[10px] text-slate-400 truncate">
                    {{ book.publisher }} ({{ book.year }}) • {{ book.size_mb }}
                  </p>
                </div>
              </div>

              <button 
                @click="handleOpenBook(book)"
                class="px-2.5 py-1 rounded bg-amber-500 hover:bg-amber-600 text-slate-950 font-mono text-[10px] font-semibold shrink-0 flex items-center gap-1 cursor-pointer"
              >
                <span>LEER</span>
                <span class="material-symbols-outlined text-xs">visibility</span>
              </button>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>
