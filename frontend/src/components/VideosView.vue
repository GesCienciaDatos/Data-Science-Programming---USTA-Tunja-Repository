<script setup>
defineProps({
  videos: {
    type: Array,
    required: true
  }
});

const emit = defineEmits(['play-video']);
</script>

<template>
  <div class="space-y-6 py-6 px-4 sm:px-8 max-w-container mx-auto">
    
    <!-- Header -->
    <div class="pb-3 border-b border-slate-200 dark:border-slate-800">
      <h2 class="text-xl font-semibold text-slate-900 dark:text-slate-100 flex items-center gap-2">
        <span class="material-symbols-outlined text-rose-500 text-lg">smart_display</span>
        Masterclasses & Talleres en Video
      </h2>
      <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
        Sesiones grabadas y explicaciones en video transmitidas en YouTube.
      </p>
    </div>

    <!-- Videos Grid -->
    <div v-if="videos.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
      <div 
        v-for="v in videos" 
        :key="v.id"
        class="glass-card rounded-xl p-4 border flex flex-col justify-between transition-all duration-200 hover:border-slate-300 dark:hover:border-slate-700 space-y-3 group"
      >
        <div class="space-y-3">
          <!-- Thumbnail Video Frame -->
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

          <!-- Video Info -->
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

    <!-- Empty State -->
    <div v-else class="py-12 text-center glass-panel rounded-xl border border-slate-200 dark:border-slate-800">
      <span class="material-symbols-outlined text-slate-400 text-3xl mb-2">smart_display</span>
      <h3 class="text-sm font-semibold text-slate-800 dark:text-slate-200">No hay videos disponibles</h3>
      <p class="text-xs text-slate-500 mt-0.5">Las grabaciones de clase se irán subiendo gradualmente.</p>
    </div>

  </div>
</template>
