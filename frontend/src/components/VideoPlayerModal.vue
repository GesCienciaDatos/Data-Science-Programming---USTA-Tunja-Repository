<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  video: {
    type: Object,
    required: true
  },
  allVideos: {
    type: Array,
    default: () => []
  }
});

const emit = defineEmits(['close', 'select-video']);

const currentVideo = ref(props.video);

function playVideo(v) {
  currentVideo.value = v;
}

const embedSrc = computed(() => {
  if (!currentVideo.value) return '';
  if (currentVideo.value.youtube_id) {
    return `https://www.youtube-nocookie.com/embed/${currentVideo.value.youtube_id}?autoplay=1&rel=0`;
  }
  return currentVideo.value.embed_url || '';
});
</script>

<template>
  <div class="fixed inset-0 z-50 flex items-center justify-center p-2 sm:p-4 bg-black/80 backdrop-blur-md animate-fade-in" @click.self="emit('close')">
    <div class="glass-panel rounded-2xl w-full max-w-5xl border border-slate-200 dark:border-slate-800 flex flex-col overflow-hidden shadow-2xl bg-white dark:bg-space-900 max-h-[92vh]">
      
      <!-- Header -->
      <div class="px-5 py-3 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between gap-3 bg-slate-50 dark:bg-space-950">
        <div class="flex items-center gap-2.5 overflow-hidden">
          <span class="material-symbols-outlined text-rose-500 text-xl shrink-0">smart_display</span>
          <div class="overflow-hidden">
            <h3 class="text-sm font-semibold text-slate-900 dark:text-slate-100 truncate font-mono">
              {{ currentVideo.title }}
            </h3>
            <p class="text-[11px] text-slate-500 truncate font-mono">
              {{ currentVideo.module || 'Masterclass de Programación' }} • {{ currentVideo.size_mb ? `${currentVideo.size_mb} MB` : 'YouTube HD' }}
            </p>
          </div>
        </div>

        <div class="flex items-center gap-2 shrink-0">
          <a 
            v-if="currentVideo.youtube_url"
            :href="currentVideo.youtube_url" 
            target="_blank" 
            rel="noopener noreferrer"
            class="px-3 py-1.5 rounded-md bg-rose-500/10 hover:bg-rose-500/20 text-rose-600 dark:text-rose-400 text-xs font-mono font-medium flex items-center gap-1.5 transition-colors border border-rose-500/30"
          >
            <span class="material-symbols-outlined text-sm">open_in_new</span>
            <span class="hidden sm:inline">Ver en YouTube</span>
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

      <!-- Video Player (16:9) + Playlist Sidebar -->
      <div class="grid grid-cols-1 lg:grid-cols-12 flex-1 overflow-hidden bg-black">
        
        <!-- Video Player Frame -->
        <div class="lg:col-span-8 flex items-center justify-center bg-black aspect-video lg:aspect-auto">
          <iframe 
            v-if="embedSrc"
            :src="embedSrc" 
            class="w-full h-full min-h-[300px] lg:min-h-[440px] border-none"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
            title="Reproductor de Video YouTube"
          ></iframe>
        </div>

        <!-- Playlist Sidebar -->
        <div class="lg:col-span-4 bg-slate-50 dark:bg-space-950 border-t lg:border-t-0 lg:border-l border-slate-200 dark:border-slate-800 p-4 space-y-3 overflow-y-auto max-h-64 lg:max-h-full">
          <span class="font-mono text-xs text-slate-500 uppercase tracking-wider block">
            Videos de la Asignatura ({{ allVideos.length }})
          </span>

          <div class="space-y-2">
            <button 
              v-for="v in allVideos"
              :key="v.id"
              @click="playVideo(v)"
              class="w-full p-2.5 rounded-lg border text-left flex items-start gap-3 transition-all"
              :class="currentVideo.id === v.id ? 'bg-white dark:bg-space-850 border-brand-cyan shadow-xs' : 'bg-transparent border-transparent hover:bg-slate-200/60 dark:hover:bg-space-900 text-slate-600 dark:text-slate-400'"
            >
              <div class="relative w-16 h-11 rounded bg-slate-800 shrink-0 overflow-hidden border border-slate-700">
                <img 
                  v-if="v.thumbnail"
                  :src="v.thumbnail" 
                  alt="Thumbnail" 
                  class="w-full h-full object-cover"
                />
                <span class="material-symbols-outlined absolute inset-0 flex items-center justify-center text-white/80 text-sm bg-black/30">
                  play_circle
                </span>
              </div>
              
              <div class="overflow-hidden space-y-0.5">
                <h5 class="text-xs font-semibold text-slate-900 dark:text-slate-100 truncate font-mono">
                  {{ v.title }}
                </h5>
                <p class="text-[10px] text-slate-500 truncate font-mono">
                  {{ v.module }}
                </p>
              </div>
            </button>
          </div>
        </div>

      </div>

    </div>
  </div>
</template>
