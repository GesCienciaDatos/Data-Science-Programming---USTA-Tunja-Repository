<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  courses: {
    type: Array,
    required: true
  }
});

const emit = defineEmits(['select-course']);

const searchQuery = ref('');
const selectedSemester = ref('all');

const filteredCourses = computed(() => {
  return props.courses.filter(course => {
    if (selectedSemester.value !== 'all' && course.semester !== selectedSemester.value) {
      return false;
    }
    if (searchQuery.value.trim() !== '') {
      const q = searchQuery.value.toLowerCase();
      const inName = (course.name || '').toLowerCase().includes(q);
      const inTitle = (course.title || '').toLowerCase().includes(q);
      const inDesc = (course.description || '').toLowerCase().includes(q);
      if (!inName && !inTitle && !inDesc) return false;
    }
    return true;
  });
});
</script>

<template>
  <section class="py-8 px-4 sm:px-8 max-w-container mx-auto space-y-6">
    
    <!-- Directory Header & Filters Bar -->
    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 pb-3 border-b border-slate-200 dark:border-slate-800">
      <div>
        <h2 class="text-xl font-semibold text-slate-900 dark:text-slate-100 flex items-center gap-2">
          <span class="material-symbols-outlined text-brand-cyan text-lg">school</span>
          Plan de Estudios & Asignaturas
        </h2>
        <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
          Estructura curricular de la Especialización en Ciencia de Datos.
        </p>
      </div>

      <!-- Semester & Search Controls -->
      <div class="flex flex-wrap items-center gap-2.5">
        <!-- Semester Filter -->
        <div class="flex items-center p-1 rounded-md bg-slate-100 dark:bg-space-900 border border-slate-200 dark:border-slate-800 font-mono text-xs">
          <button 
            @click="selectedSemester = 'all'"
            class="px-2.5 py-1 rounded transition-colors"
            :class="selectedSemester === 'all' ? 'bg-white dark:bg-space-800 text-slate-900 dark:text-slate-100 font-semibold shadow-xs' : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-300'"
          >
            Todos (9)
          </button>
          <button 
            @click="selectedSemester = 'Semestre I'"
            class="px-2.5 py-1 rounded transition-colors"
            :class="selectedSemester === 'Semestre I' ? 'bg-white dark:bg-space-800 text-slate-900 dark:text-slate-100 font-semibold shadow-xs' : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-300'"
          >
            Semestre I (5)
          </button>
          <button 
            @click="selectedSemester = 'Semestre II'"
            class="px-2.5 py-1 rounded transition-colors"
            :class="selectedSemester === 'Semestre II' ? 'bg-white dark:bg-space-800 text-slate-900 dark:text-slate-100 font-semibold shadow-xs' : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-300'"
          >
            Semestre II (4)
          </button>
        </div>

        <!-- Course Search Input -->
        <div class="relative">
          <span class="material-symbols-outlined absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-400 text-sm">search</span>
          <input 
            v-model="searchQuery"
            type="text" 
            placeholder="Filtrar materia..."
            class="pl-8 pr-3 py-1.5 rounded-md bg-slate-100 dark:bg-space-900 border border-slate-200 dark:border-slate-800 text-xs font-mono text-slate-800 dark:text-slate-200 placeholder:text-slate-400 focus:outline-none focus:border-brand-cyan w-40 sm:w-48"
          />
        </div>
      </div>
    </div>

    <!-- Course Cards Grid (Bento Grid) -->
    <div v-if="filteredCourses.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
      <div 
        v-for="course in filteredCourses" 
        :key="course.id"
        class="glass-card rounded-xl p-5 border flex flex-col justify-between transition-all duration-200 hover:border-slate-300 dark:hover:border-slate-700"
      >
        <div>
          <!-- Card Header -->
          <div class="flex items-start justify-between gap-3 mb-3">
            <div class="space-y-0.5">
              <span class="font-mono text-[11px] text-brand-cyan font-semibold block">
                {{ course.code || 'DSP-2026' }}
              </span>
              <h3 class="text-base font-semibold text-slate-900 dark:text-slate-100 leading-snug">
                {{ course.name }}
              </h3>
            </div>

            <span 
              class="px-2 py-0.5 rounded text-[10px] font-mono font-semibold shrink-0"
              :class="course.active !== false ? 'bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20' : 'bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-400 border border-slate-300 dark:border-slate-700'"
            >
              {{ course.active !== false ? 'Disponible' : 'En Desarrollo' }}
            </span>
          </div>

          <!-- Academic Title / Focus -->
          <p class="text-xs font-medium text-slate-700 dark:text-slate-300 mb-2">
            {{ course.title }}
          </p>

          <!-- Description -->
          <p class="text-xs text-slate-500 dark:text-slate-400 line-clamp-3 leading-relaxed mb-4">
            {{ course.description }}
          </p>

          <!-- Metrics Matrix -->
          <div class="grid grid-cols-3 gap-2 mb-5 font-mono text-[11px]">
            <div class="p-2 rounded bg-slate-50 dark:bg-space-950 border border-slate-200/80 dark:border-slate-800 text-center">
              <span class="block text-[9px] text-slate-400 uppercase">Cuadernos</span>
              <span class="font-semibold text-slate-800 dark:text-slate-200">{{ course.active !== false ? (course.stats?.total_notebooks || 144) : '—' }}</span>
            </div>
            <div class="p-2 rounded bg-slate-50 dark:bg-space-950 border border-slate-200/80 dark:border-slate-800 text-center">
              <span class="block text-[9px] text-slate-400 uppercase">Módulos</span>
              <span class="font-semibold text-slate-800 dark:text-slate-200">{{ (course.modules || []).length || '—' }}</span>
            </div>
            <div class="p-2 rounded bg-slate-50 dark:bg-space-950 border border-slate-200/80 dark:border-slate-800 text-center">
              <span class="block text-[9px] text-slate-400 uppercase">Semestre</span>
              <span class="font-semibold text-brand-cyan">{{ course.semester === 'Semestre I' ? 'I' : 'II' }}</span>
            </div>
          </div>
        </div>

        <!-- Card Action Button -->
        <div class="pt-3 border-t border-slate-200 dark:border-slate-800">
          <button 
            v-if="course.active !== false"
            @click="emit('select-course', course.id)"
            class="w-full py-2 px-3 rounded-md bg-slate-900 dark:bg-slate-100 hover:bg-slate-800 dark:hover:bg-white text-white dark:text-slate-950 font-mono text-xs font-semibold flex items-center justify-center gap-1.5 transition-all shadow-xs"
          >
            <span>INGRESAR AL LABORATORIO</span>
            <span class="material-symbols-outlined text-sm">arrow_forward</span>
          </button>
          <div 
            v-else
            class="w-full py-2 px-3 rounded-md bg-slate-100 dark:bg-space-900 border border-slate-200 dark:border-slate-800 text-slate-500 font-mono text-xs text-center font-medium"
          >
            Material en construcción
          </div>
        </div>

      </div>
    </div>

    <!-- Empty State -->
    <div v-else class="py-12 text-center glass-panel rounded-xl border border-slate-200 dark:border-slate-800">
      <span class="material-symbols-outlined text-slate-400 text-3xl mb-2">school</span>
      <h3 class="text-sm font-semibold text-slate-800 dark:text-slate-200">No se encontraron asignaturas</h3>
      <p class="text-xs text-slate-500 mt-0.5">Intenta con otro término de búsqueda o selecciona otro semestre.</p>
    </div>

  </section>
</template>
