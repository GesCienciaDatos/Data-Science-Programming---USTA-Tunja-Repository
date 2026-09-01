<script setup>
import { ref, computed, onMounted } from 'vue';
import { CATALOG_DATA } from './data/catalog.js';

import TopNavbar from './components/TopNavbar.vue';
import HeroSection from './components/HeroSection.vue';
import CourseDirectory from './components/CourseDirectory.vue';
import CourseWorkspace from './components/CourseWorkspace.vue';
import DatasetExplorerModal from './components/DatasetExplorerModal.vue';
import GlobalSearchModal from './components/GlobalSearchModal.vue';
import PdfViewerModal from './components/PdfViewerModal.vue';
import VideoPlayerModal from './components/VideoPlayerModal.vue';
import FooterInstitutional from './components/FooterInstitutional.vue';

// Reactive State
const isDarkMode = ref(true);
const currentView = ref('directory'); // 'directory' | 'workspace'
const activeCourseId = ref(CATALOG_DATA.active_course_id || 'data-science-programming');

// Modals State
const isDatasetModalOpen = ref(false);
const isGlobalSearchOpen = ref(false);
const activePdfDoc = ref(null);
const activeVideo = ref(null);

// Toast Notification State
const toastMessage = ref('');
const isToastVisible = ref(false);
let toastTimeout = null;

// Courses & Datasets Data
const courses = ref(CATALOG_DATA.courses || []);
const datasets = ref(CATALOG_DATA.datasets || []);

const activeCourse = computed(() => {
  return courses.value.find(c => c.id === activeCourseId.value) || courses.value[0];
});

const allNotebooks = computed(() => {
  return activeCourse.value?.notebooks || [];
});

const allVideos = computed(() => {
  return activeCourse.value?.videos || CATALOG_DATA.videos || [];
});

// Theme Management
function initTheme() {
  const savedTheme = localStorage.getItem('usta_theme');
  if (savedTheme) {
    isDarkMode.value = savedTheme === 'dark';
  } else {
    isDarkMode.value = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
  applyTheme();
}

function toggleTheme() {
  isDarkMode.value = !isDarkMode.value;
  localStorage.setItem('usta_theme', isDarkMode.value ? 'dark' : 'light');
  applyTheme();
  showToast(isDarkMode.value ? 'Tema Oscuro activado' : 'Tema Claro activado');
}

function applyTheme() {
  if (isDarkMode.value) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
}

// Navigation Handlers
function navigateView(view) {
  currentView.value = view;
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function selectCourse(courseId) {
  const course = courses.value.find(c => c.id === courseId);
  if (!course || course.active === false) {
    showToast('Asignatura en desarrollo curricular.');
    return;
  }
  activeCourseId.value = courseId;
  currentView.value = 'workspace';
  window.scrollTo({ top: 0, behavior: 'smooth' });
  showToast(`Laboratorio: ${course.name}`);
}

// Media & Document Handlers
function openPdfViewer(doc) {
  activePdfDoc.value = doc;
}

function playVideo(video) {
  activeVideo.value = video;
}

// Toast Notifications
function showToast(msg) {
  toastMessage.value = msg;
  isToastVisible.value = true;
  clearTimeout(toastTimeout);
  toastTimeout = setTimeout(() => {
    isToastVisible.value = false;
  }, 3000);
}

// Global Keyboard Shortcuts
onMounted(() => {
  initTheme();

  window.addEventListener('keydown', (e) => {
    if ((e.key === '/' || (e.ctrlKey && e.key === 'k')) && document.activeElement.tagName !== 'INPUT') {
      e.preventDefault();
      isGlobalSearchOpen.value = true;
    }
    if (e.key === 'Escape') {
      isDatasetModalOpen.value = false;
      isGlobalSearchOpen.value = false;
      activePdfDoc.value = null;
      activeVideo.value = null;
    }
  });
});
</script>

<template>
  <div class="min-h-screen flex flex-col justify-between selection:bg-brand-cyan/20 selection:text-brand-cyan">
    
    <!-- Top Fixed Navigation -->
    <TopNavbar 
      :current-view="currentView"
      :active-course="activeCourse"
      :is-dark-mode="isDarkMode"
      @navigate-view="navigateView"
      @open-search="isGlobalSearchOpen = true"
      @toggle-theme="toggleTheme"
    />

    <!-- Main View Content -->
    <main class="flex-1">
      
      <!-- 1. Directory View (Landing + Course Bento Grid) -->
      <div v-if="currentView === 'directory'" class="space-y-4">
        <HeroSection 
          @explore-course="selectCourse"
          @open-datasets="isDatasetModalOpen = true"
        />

        <CourseDirectory 
          :courses="courses"
          @select-course="selectCourse"
        />
      </div>

      <!-- 2. Course Workspace View (All Resources scoped to the Active Course) -->
      <div v-else-if="currentView === 'workspace' && activeCourse">
        <CourseWorkspace 
          :course="activeCourse"
          @return-directory="navigateView('directory')"
          @show-toast="showToast"
          @open-pdf="openPdfViewer"
          @play-video="playVideo"
        />
      </div>

    </main>

    <!-- Institutional Footer -->
    <FooterInstitutional />

    <!-- Modals -->
    <DatasetExplorerModal 
      v-if="isDatasetModalOpen"
      :datasets="datasets"
      @close="isDatasetModalOpen = false"
    />

    <GlobalSearchModal 
      v-if="isGlobalSearchOpen"
      :all-notebooks="allNotebooks"
      @close="isGlobalSearchOpen = false"
    />

    <PdfViewerModal 
      v-if="activePdfDoc"
      :doc="activePdfDoc"
      @close="activePdfDoc = null"
    />

    <VideoPlayerModal 
      v-if="activeVideo"
      :video="activeVideo"
      :all-videos="allVideos"
      @close="activeVideo = null"
    />

    <!-- Toast Notification Banner -->
    <div 
      class="fixed bottom-6 right-6 z-50 px-4 py-2.5 rounded-lg font-mono text-xs shadow-lg transition-all duration-300 border flex items-center gap-2"
      :class="isToastVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4 pointer-events-none'"
      style="background-color: var(--toast-bg, rgba(18, 24, 31, 0.9)); color: #f8fafc; border-color: rgba(56, 189, 248, 0.3); backdrop-filter: blur(12px);"
    >
      <span class="w-2 h-2 rounded-full bg-brand-cyan"></span>
      <span>{{ toastMessage }}</span>
    </div>

  </div>
</template>
