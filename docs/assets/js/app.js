/**
 * Core Application Controller - Multi-Course Architecture
 * Next-Gen Virtual Lab Platform - Universidad Santo Tomás Seccional Tunja
 */

(function initApp() {
  // Asegurar objeto de catálogo base
  if (typeof window.VIRTUAL_LAB_CATALOG === 'undefined') {
    window.VIRTUAL_LAB_CATALOG = {
      active_course_id: "data-science-programming",
      courses: [],
      modules: [],
      notebooks: [],
      datasets: [],
      guias: [],
      videos: [],
      stats: {}
    };
  }

  const CATALOG = window.VIRTUAL_LAB_CATALOG;

  // Estado reactivo de la aplicación
  let currentView = 'hub'; // 'hub' o 'course'
  let currentCourseId = null;
  let currentTab = 'notebooks';
  let currentModule = 'all';
  let currentSearch = '';
  let currentDiff = 'all';
  let currentPlayingVideoId = null;
  let currentActiveGuiaId = null;
  let currentSnippetKey = 'cv';
  let searchGuiasQuery = '';
  let searchVideosQuery = '';
  let courseSearchQuery = '';
  let courseSemesterFilter = 'all';

  // Terminal Sandbox Snippets
  const SANDBOX_SNIPPETS = {
    cv: {
      code: `<div class="code-line"><span class="text-tertiary">import</span> <span class="text-on-surface">numpy as np, pandas as pd</span></div>
<div class="code-line"><span class="text-tertiary">from</span> <span class="text-on-surface">sklearn.model_selection</span> <span class="text-tertiary">import</span> <span class="text-on-surface">cross_val_score</span></div>
<div class="code-line"><span class="text-tertiary">from</span> <span class="text-on-surface">sklearn.ensemble</span> <span class="text-tertiary">import</span> <span class="text-on-surface">RandomForestRegressor</span></div>
<div class="code-line"></div>
<div class="code-line"><span class="text-on-surface-variant"># 🚀 Validación Cruzada 5-Fold Blindada contra Data Leakage</span></div>
<div class="code-line">model = RandomForestRegressor(n_estimators=<span class="text-primary">150</span>, max_depth=<span class="text-primary">12</span>, random_state=<span class="text-primary">42</span>)</div>
<div class="code-line">scores = cross_val_score(model, X_train, y_train, cv=<span class="text-primary">5</span>, scoring=<span class="text-tertiary-fixed">'r2'</span>)</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-tertiary">print</span>(<span class="text-tertiary-fixed">f"✨ R² Promedio 5-Fold CV: {scores.mean():.4f}"</span>)</div>`,
      output: "✨ R² Promedio 5-Fold CV: 0.8871 (Modelo Validado con Cero Data Leakage)"
    },
    eda: {
      code: `<div class="code-line"><span class="text-tertiary">import</span> <span class="text-on-surface">pandas as pd</span></div>
<div class="code-line"><span class="text-on-surface-variant"># 📊 Diagnóstico Estadístico Inicial & Matriz de Nulos</span></div>
<div class="code-line">df = pd.read_csv(<span class="text-emerald-400">"melb_data.csv"</span>)</div>
<div class="code-line">missing_summary = df.isnull().sum()[df.isnull().sum() &gt; <span class="text-primary">0</span>]</div>
<div class="code-line">stats = df[[<span class="text-emerald-400">'Rooms'</span>, <span class="text-emerald-400">'Price'</span>, <span class="text-emerald-400">'Distance'</span>]].describe().T</div>
<div class="code-line"><span class="text-tertiary">print</span>(<span class="text-tertiary-fixed">f"📈 Total Registros: {len(df):,} | Nulos detectados: {len(missing_summary)}"</span>)</div>`,
      output: "📈 Total Registros: 13,580 | Nulos detectados: 3 | Diagnóstico Completado"
    },
    fe: {
      code: `<div class="code-line"><span class="text-tertiary">import</span> <span class="text-on-surface">numpy as np, pandas as pd</span></div>
<div class="code-line"><span class="text-on-surface-variant"># ⚙️ Target Encoding con Suavizado Bayesiano m-estimate</span></div>
<div class="code-line"><span class="text-tertiary">def</span> <span class="text-on-surface">calc_smooth_target</span>(df, cat_col, target_col, weight=<span class="text-primary">10</span>):</div>
<div class="code-line">    global_mean = df[target_col].mean()</div>
<div class="code-line">    counts = df.groupby(cat_col)[target_col].count()</div>
<div class="code-line">    means = df.groupby(cat_col)[target_col].mean()</div>
<div class="code-line">    smooth = (counts * means + weight * global_mean) / (counts + weight)</div>
<div class="code-line">    <span class="text-tertiary">return</span> df[cat_col].map(smooth)</div>`,
      output: "⚙️ Target Encoding Regularizado: Reducción de Varianza y Prevención de Overfitting"
    }
  };

  function getActiveCourse() {
    if (!CATALOG.courses || CATALOG.courses.length === 0) return null;
    if (!currentCourseId) {
      return CATALOG.courses.find(c => c.id === CATALOG.active_course_id) || CATALOG.courses[0];
    }
    return CATALOG.courses.find(c => c.id === currentCourseId) || CATALOG.courses[0];
  }

  function syncActiveCourseData() {
    const course = getActiveCourse();
    if (!course) return;

    CATALOG.active_course_id = course.id;
    CATALOG.modules = course.modules || [];
    CATALOG.notebooks = course.notebooks || [];
    CATALOG.datasets = course.datasets || [];
    CATALOG.guias = course.guias || [];
    CATALOG.videos = course.videos || [];
    CATALOG.stats = course.stats || {};
  }

  // =========================================================================
  // 1. GESTIÓN DE CURSOS Y PORTAL HUB DE MATERIAS
  // =========================================================================

  function renderCourseHub() {
    const container = document.getElementById('coursesGridContainer');
    if (!container || !CATALOG.courses) return;

    const courses = CATALOG.courses.filter(c => {
      if (courseSemesterFilter !== 'all' && c.semester !== courseSemesterFilter) return false;
      if (courseSearchQuery.trim() !== '') {
        const q = courseSearchQuery.toLowerCase();
        const inName = (c.name || '').toLowerCase().includes(q);
        const inTitle = (c.title || '').toLowerCase().includes(q);
        const inDesc = (c.description || '').toLowerCase().includes(q);
        if (!inName && !inTitle && !inDesc) return false;
      }
      return true;
    });

    if (courses.length === 0) {
      container.innerHTML = `
        <div class="col-span-full py-12 text-center glass-panel rounded-2xl border border-outline-variant">
          <span class="material-symbols-outlined text-primary text-4xl mb-2">school</span>
          <h3 class="font-headline-md text-on-surface text-base">No se encontraron materias</h3>
          <p class="text-xs text-on-surface-variant max-w-sm mx-auto mt-1">Prueba con otro término de búsqueda o limpia los filtros de semestre.</p>
        </div>
      `;
      return;
    }

    container.innerHTML = courses.map((c, idx) => {
      const isActive = c.active !== false;
      const nbCount = c.stats ? (c.stats.total_notebooks || 0) : ((c.notebooks || []).length);
      const dsCount = c.stats ? (c.stats.total_datasets || 0) : ((c.datasets || []).length);
      const guiasCount = c.stats ? (c.stats.total_guias || 0) : ((c.guias || []).length);
      const vidCount = c.stats ? (c.stats.total_videos || 0) : ((c.videos || []).length);

      const badgeStyle = isActive 
        ? 'bg-emerald-500/20 text-emerald-400 border-emerald-500/30' 
        : 'bg-amber-500/20 text-amber-300 border-amber-500/30';

      const borderGlow = isActive
        ? 'border-primary/40 hover:border-primary shadow-[0_0_20px_rgba(56,189,248,0.15)] hover:shadow-[0_0_30px_rgba(56,189,248,0.3)]'
        : 'border-outline-variant/60 hover:border-outline-variant hover:shadow-[0_0_15px_rgba(245,158,11,0.15)]';

      const animDelayClass = `delay-${Math.min((idx + 1) * 100, 500)}`;

      return `
        <div class="glass-panel rounded-3xl p-6 sm:p-7 border ${borderGlow} flex flex-col justify-between transition-all duration-300 group hover:-translate-y-1.5 relative overflow-hidden bg-gradient-to-b ${c.gradient || 'from-surface-container/80 to-surface/90'} animate-fade-in-up ${animDelayClass}">
          
          <!-- Ambient card background glow -->
          <div class="absolute -right-12 -top-12 w-36 h-36 rounded-full ${isActive ? 'bg-primary/10 group-hover:bg-primary/20' : 'bg-amber-500/10 group-hover:bg-amber-500/20'} blur-3xl pointer-events-none transition-all"></div>

          <div>
            <!-- Header: Icon, Tags & Badge -->
            <div class="flex items-start justify-between gap-3 mb-4">
              <div class="w-14 h-14 rounded-2xl bg-surface-container-highest border border-outline-variant flex items-center justify-center text-3xl shadow-inner group-hover:scale-110 transition-transform duration-300">
                ${c.icon || '📚'}
              </div>
              <div class="flex flex-col items-end gap-1.5">
                <span class="px-2.5 py-0.5 rounded-full text-[11px] font-mono font-bold border ${badgeStyle}">
                  ${isActive ? '🟢 Activo / Disponible' : '🚧 En Construcción'}
                </span>
                <span class="text-[10px] font-mono text-on-surface-variant font-semibold tracking-wide">
                  ${c.semester || 'Semestre I'} • ${c.level || 'Especialización'}
                </span>
              </div>
            </div>

            <!-- Title & Subtitle -->
            <h3 class="font-display-sm text-xl sm:text-2xl font-bold text-on-surface group-hover:text-primary transition-colors leading-tight mb-2">
              ${c.name}
            </h3>
            <p class="text-xs font-headline-md ${isActive ? 'text-primary/90' : 'text-amber-300/90'} font-medium mb-3">
              ${c.title}
            </p>

            <!-- Description -->
            <p class="text-xs text-on-surface-variant leading-relaxed line-clamp-3 mb-5">
              ${c.description}
            </p>

            <!-- Metrics Pills Matrix -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 mb-6 font-mono text-[11px]">
              <div class="p-2 rounded-xl bg-surface-container/70 border border-outline-variant/60 text-center">
                <span class="block text-[9px] text-on-surface-variant">CUADERNOS</span>
                <span class="font-bold text-on-surface text-xs">${isActive ? nbCount : 'En Prep.'}</span>
              </div>
              <div class="p-2 rounded-xl bg-surface-container/70 border border-outline-variant/60 text-center">
                <span class="block text-[9px] text-on-surface-variant">DATASETS</span>
                <span class="font-bold text-primary text-xs">${isActive ? dsCount : 'En Prep.'}</span>
              </div>
              <div class="p-2 rounded-xl bg-surface-container/70 border border-outline-variant/60 text-center">
                <span class="block text-[9px] text-on-surface-variant">GUÍAS PDF</span>
                <span class="font-bold text-tertiary text-xs">${isActive ? guiasCount : 'En Prep.'}</span>
              </div>
              <div class="p-2 rounded-xl bg-surface-container/70 border border-outline-variant/60 text-center">
                <span class="block text-[9px] text-on-surface-variant">VIDEOS</span>
                <span class="font-bold text-purple-300 text-xs">${isActive ? vidCount : 'En Prep.'}</span>
              </div>
            </div>
          </div>

          <!-- Bottom Action Button -->
          <div class="pt-4 border-t border-outline-variant/40 flex items-center justify-between gap-3">
            ${isActive ? `
              <button onclick="selectCourse('${c.id}')" class="w-full py-3 px-4 rounded-xl bg-primary-container text-on-primary-container font-label-caps text-xs font-bold hover:shadow-neon-cyan active:scale-95 transition-all duration-300 flex items-center justify-center gap-2 group/btn">
                <span>INGRESAR AL LABORATORIO VIRTUAL</span>
                <span class="material-symbols-outlined text-sm group-hover/btn:translate-x-1 transition-transform">arrow_forward</span>
              </button>
            ` : `
              <button onclick="showToast('🚧 Materia en construcción. El material pedagógico se incorporará próximamente.')" class="w-full py-3 px-4 rounded-xl bg-amber-500/10 hover:bg-amber-500/20 text-amber-300 font-label-caps text-xs font-semibold border border-amber-500/30 transition-all flex items-center justify-center gap-2">
                <span class="material-symbols-outlined text-sm text-amber-400">construction</span>
                <span>EN CONSTRUCCIÓN</span>
              </button>
            `}
          </div>

        </div>
      `;
    }).join('');
  }

  function selectCourse(courseId, pushHash = true) {
    const course = (CATALOG.courses || []).find(c => c.id === courseId);
    if (!course || course.active === false) {
      showToast("🚧 Materia en construcción. El contenido se publicará próximamente.");
      return;
    }

    currentCourseId = courseId;
    currentView = 'course';
    currentModule = 'all';
    currentSearch = '';
    currentDiff = 'all';

    syncActiveCourseData();

    // Actualizar URL Hash para compartir o refrescar
    if (pushHash) {
      window.location.hash = `course=${courseId}`;
    }

    // Alternar visibilidad de vistas principales y barra de navegación
    const hubView = document.getElementById('view-course-hub');
    const courseView = document.getElementById('courseWorkspaceWrapper');
    const navCenter = document.getElementById('navbarCenterLinks');
    const navCourseSelector = document.getElementById('navCourseSelectorContainer');
    const navReturnHubBtn = document.getElementById('navReturnHubBtn');
    const navActiveCourseName = document.getElementById('navActiveCourseName');
    const navActiveCourseIcon = document.getElementById('navActiveCourseIcon');
    const bannerCourseName = document.getElementById('bannerCourseName');
    const bannerCourseIcon = document.getElementById('bannerCourseIcon');
    const bannerCourseDesc = document.getElementById('bannerCourseDesc');

    if (hubView) { hubView.classList.add('force-hidden'); hubView.classList.remove('force-block'); }
    if (courseView) { courseView.classList.remove('force-hidden'); courseView.classList.add('force-block'); }
    if (navCenter) { navCenter.classList.remove('force-hidden'); navCenter.classList.add('force-flex'); }
    if (navCourseSelector) { navCourseSelector.classList.remove('force-hidden'); navCourseSelector.classList.add('force-flex'); }
    if (navReturnHubBtn) { navReturnHubBtn.classList.remove('force-hidden'); navReturnHubBtn.classList.add('force-flex'); }

    if (navActiveCourseName) navActiveCourseName.textContent = course.name;
    if (navActiveCourseIcon) navActiveCourseIcon.textContent = course.icon || '🐍';
    if (bannerCourseName) bannerCourseName.textContent = course.name;
    if (bannerCourseIcon) bannerCourseIcon.textContent = course.icon || '🐍';
    if (bannerCourseDesc) bannerCourseDesc.textContent = course.description;

    // Resetear a la pestaña de notebooks
    switchTab('notebooks');
    renderPills();
    renderNotebooks();
    updateUiCounts();

    window.scrollTo({ top: 0, behavior: 'smooth' });
    showToast(`Laboratorio Virtual: ${course.name} ⚡`);
  }

  function returnToCourseHub(pushHash = true) {
    currentView = 'hub';
    if (pushHash) {
      window.location.hash = 'hub';
    }

    const hubView = document.getElementById('view-course-hub');
    const courseView = document.getElementById('courseWorkspaceWrapper');
    const navCenter = document.getElementById('navbarCenterLinks');
    const navCourseSelector = document.getElementById('navCourseSelectorContainer');
    const navReturnHubBtn = document.getElementById('navReturnHubBtn');

    if (hubView) { hubView.classList.remove('force-hidden'); hubView.classList.add('force-block'); }
    if (courseView) { courseView.classList.add('force-hidden'); courseView.classList.remove('force-block'); }
    if (navCenter) { navCenter.classList.add('force-hidden'); navCenter.classList.remove('force-flex'); }
    if (navCourseSelector) { navCourseSelector.classList.add('force-hidden'); navCourseSelector.classList.remove('force-flex'); }
    if (navReturnHubBtn) { navReturnHubBtn.classList.add('force-hidden'); navReturnHubBtn.classList.remove('force-flex'); }

    renderCourseHub();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function filterCoursesBySemester(sem) {
    courseSemesterFilter = sem;
    const allBtns = ['all', 'Semestre I', 'Semestre II'];
    allBtns.forEach(s => {
      const btn = document.getElementById(`btn-sem-${s === 'all' ? 'all' : (s === 'Semestre I' ? '1' : '2')}`);
      if (!btn) return;
      if (s === sem) {
        btn.className = 'px-3 py-1 rounded-full text-xs font-mono font-bold bg-primary text-on-primary shadow-neon-cyan transition-all';
      } else {
        btn.className = 'px-3 py-1 rounded-full text-xs font-mono bg-surface-container text-on-surface-variant hover:text-on-surface border border-outline-variant transition-all';
      }
    });
    renderCourseHub();
  }

  // =========================================================================
  // 2. TERMINAL SANDBOX & SIMULACIÓN
  // =========================================================================

  function setSandboxSnippet(key) {
    currentSnippetKey = key;
    const snippet = SANDBOX_SNIPPETS[key];
    const display = document.getElementById('sandboxCodeDisplay');
    const output = document.getElementById('sandboxOutputText');
    if (display) display.innerHTML = snippet.code;
    if (output) output.textContent = `Output: ${snippet.output}`;

    ['cv', 'eda', 'fe'].forEach(k => {
      const btn = document.getElementById(`tab-snippet-${k}`);
      if (!btn) return;
      if (k === key) {
        btn.className = 'px-2 py-0.5 rounded text-[10px] font-mono bg-primary/20 text-primary border border-primary/30';
      } else {
        btn.className = 'px-2 py-0.5 rounded text-[10px] font-mono text-on-surface-variant hover:text-on-surface';
      }
    });
  }

  function runSandboxSimulation() {
    const btn = document.getElementById('runSimulationBtn');
    const label = document.getElementById('runBtnLabel');
    const output = document.getElementById('sandboxOutputText');
    if (!btn) return;

    label.textContent = "EJECUTANDO...";
    btn.classList.add('opacity-75', 'animate-pulse');

    setTimeout(() => {
      btn.classList.remove('opacity-75', 'animate-pulse');
      label.textContent = "EJECUTAR SIMULACIÓN";
      if (output) output.textContent = `Output: ${SANDBOX_SNIPPETS[currentSnippetKey].output}`;
      showToast("Kernel ejecutó el script con éxito en 42ms ⚡");
    }, 400);
  }

  // =========================================================================
  // 3. CONTADORES Y NAVEGACIÓN EN PESTAÑAS
  // =========================================================================

  function updateUiCounts() {
    const course = getActiveCourse();
    const notebooksCount = (course && course.notebooks ? course.notebooks.length : 0);
    const guiasCount = (course && course.guias ? course.guias.length : 0);
    const videosCount = (course && course.videos ? course.videos.length : 0);
    const datasetsCount = (course && course.datasets ? course.datasets.length : 0);

    // Hero Cards
    const totalNbEl = document.getElementById('heroTotalNotebooks');
    if (totalNbEl) totalNbEl.textContent = notebooksCount;

    const totalDsEl = document.getElementById('heroTotalDatasets');
    if (totalDsEl) totalDsEl.textContent = datasetsCount;

    // Navbar Badges
    const navN = document.getElementById('nav-count-notebooks');
    if (navN) navN.textContent = notebooksCount;

    const navG = document.getElementById('nav-count-guias');
    if (navG) navG.textContent = guiasCount;

    const navV = document.getElementById('nav-count-videos');
    if (navV) navV.textContent = videosCount;

    const navD = document.getElementById('nav-count-datasets');
    if (navD) navD.textContent = datasetsCount;

    // Workspace Tab Pills
    const tabN = document.getElementById('tab-count-notebooks');
    if (tabN) tabN.textContent = notebooksCount;

    const tabG = document.getElementById('tab-count-guias');
    if (tabG) tabG.textContent = guiasCount;

    const tabV = document.getElementById('tab-count-videos');
    if (tabV) tabV.textContent = videosCount;

    const tabD = document.getElementById('tab-count-datasets');
    if (tabD) tabD.textContent = datasetsCount;

    // Playlist Sidebars
    const sideG = document.getElementById('guiasSidebarCount');
    if (sideG) sideG.textContent = guiasCount;

    const sideV = document.getElementById('videosSidebarCount');
    if (sideV) sideV.textContent = videosCount;
  }

  function switchTab(tabId) {
    currentTab = tabId;
    const allTabs = ['notebooks', 'guias', 'videos', 'datasets', 'quickstart', 'cheatsheet'];

    allTabs.forEach(t => {
      const viewEl = document.getElementById(`view-${t}`);
      const pillBtn = document.getElementById(`tab-pill-${t}`);
      const navBtn = document.getElementById(`nav-btn-${t}`);

      if (viewEl) {
        if (t === tabId) viewEl.classList.remove('hidden');
        else viewEl.classList.add('hidden');
      }

      if (pillBtn) {
        if (t === tabId) {
          pillBtn.className = 'bg-primary/20 text-primary px-3.5 py-1.5 rounded-full font-label-caps text-xs whitespace-nowrap border border-primary/30 cursor-pointer hover:bg-primary/30 transition-all flex items-center gap-1.5 shadow-neon-cyan shrink-0';
        } else {
          pillBtn.className = 'bg-surface-container px-3.5 py-1.5 rounded-full font-label-caps text-xs whitespace-nowrap text-on-surface-variant hover:text-on-surface border border-outline-variant cursor-pointer transition-all flex items-center gap-1.5 shrink-0';
        }
      }

      if (navBtn) {
        if (t === tabId) {
          navBtn.className = 'font-label-caps text-xs whitespace-nowrap text-primary border-b-2 border-primary pb-1 active:scale-95 duration-200 flex items-center gap-1.5 shrink-0';
        } else {
          navBtn.className = 'font-label-caps text-xs whitespace-nowrap text-on-surface-variant hover:text-primary transition-colors hover:bg-primary/10 duration-300 px-2.5 py-1 rounded flex items-center gap-1.5 shrink-0';
        }
      }
    });

    updateUiCounts();
    if (tabId === 'notebooks') renderNotebooks();
    if (tabId === 'guias') renderGuias();
    if (tabId === 'videos') renderVideos();
    if (tabId === 'datasets' && typeof window.renderDatasets === 'function') window.renderDatasets();
  }

  // =========================================================================
  // 4. RENDERIZADO DE CUADERNOS Y MÓDULOS
  // =========================================================================

  function renderPills() {
    const container = document.getElementById('modulePillsContainer');
    const course = getActiveCourse();
    if (!container || !course || !course.modules) return;

    const totalNotebooks = (course.notebooks || []).length;
    let html = `
      <button onclick="filterByModule('all')" class="px-3 py-1 rounded-full text-xs font-mono font-medium whitespace-nowrap transition-all flex items-center gap-1.5 ${currentModule === 'all' ? 'bg-primary text-on-primary font-bold shadow-neon-cyan' : 'bg-surface-container text-on-surface-variant hover:text-on-surface border border-outline-variant'}">
        <span>🌟 Todos</span>
        <span class="px-1.5 py-0.2 rounded-full text-[10px] ${currentModule === 'all' ? 'bg-black/20 text-black' : 'bg-surface-container-high text-on-surface-variant'}">${totalNotebooks}</span>
      </button>
    `;

    course.modules.forEach(m => {
      const isCurrent = currentModule === m.id;
      const count = (course.notebooks || []).filter(n => n.module_id === m.id).length;
      html += `
        <button onclick="filterByModule('${m.id}')" class="px-3 py-1 rounded-full text-xs font-mono font-medium whitespace-nowrap transition-all flex items-center gap-1.5 ${isCurrent ? 'bg-primary text-on-primary font-bold shadow-neon-cyan' : 'bg-surface-container text-on-surface-variant hover:text-on-surface border border-outline-variant'}">
          <span>${m.icon || '📁'} ${m.name}</span>
          <span class="px-1.5 py-0.2 rounded-full text-[10px] ${isCurrent ? 'bg-black/20 text-black' : 'bg-surface-container-high text-on-surface-variant'}">${count}</span>
        </button>
      `;
    });

    container.innerHTML = html;
  }

  function filterByModule(modId) {
    currentModule = modId;
    renderPills();
    renderNotebooks();
  }

  function renderNotebooks() {
    const container = document.getElementById('notebooksContainer');
    const course = getActiveCourse();
    if (!container || !course || !course.notebooks) return;

    const filtered = (course.notebooks || []).filter(nb => {
      if (currentModule !== 'all' && nb.module_id !== currentModule) return false;
      if (currentDiff !== 'all' && !nb.difficulty.toLowerCase().includes(currentDiff.toLowerCase())) return false;
      if (currentSearch.trim() !== '') {
        const q = currentSearch.toLowerCase();
        const inTitle = (nb.title || '').toLowerCase().includes(q);
        const inPath = (nb.path || '').toLowerCase().includes(q);
        const inModule = (nb.module_name || '').toLowerCase().includes(q);
        if (!inTitle && !inPath && !inModule) return false;
      }
      return true;
    });

    if (filtered.length === 0) {
      container.innerHTML = `
        <div class="col-span-full py-12 text-center glass-panel rounded-2xl border border-outline-variant">
          <span class="material-symbols-outlined text-primary text-4xl mb-2">search_off</span>
          <h3 class="font-headline-md text-on-surface text-base">No se encontraron cuadernos</h3>
          <p class="text-xs text-on-surface-variant max-w-sm mx-auto mt-1">Prueba con otro término de búsqueda o restablece los filtros.</p>
        </div>
      `;
      return;
    }

    container.innerHTML = filtered.map(nb => {
      let diffBadge = 'bg-primary/20 text-primary border-primary/30';
      if (nb.difficulty.includes('Básico')) diffBadge = 'bg-emerald-500/20 text-emerald-400 border-emerald-500/30';
      if (nb.difficulty.includes('Avanzado')) diffBadge = 'bg-error/20 text-error border-error/30';
      if (nb.difficulty.includes('Intermedio')) diffBadge = 'bg-tertiary/20 text-tertiary border-tertiary/30';

      return `
        <div class="glass-panel rounded-xl p-5 flex flex-col justify-between gap-4 group hover:-translate-y-1 transition-transform duration-300">
          <div>
            <div class="flex justify-between items-start mb-2">
              <div class="flex gap-2">
                <span class="bg-[#4d77cf]/20 text-[#4d77cf] border border-[#4d77cf]/30 px-2 py-0.5 rounded text-[10px] font-bold tracking-wider">${nb.module_name}</span>
                <span class="${diffBadge} border px-2 py-0.5 rounded text-[10px] font-bold tracking-wider">${nb.difficulty.toUpperCase()}</span>
              </div>
            </div>
            <h3 class="font-headline-md text-base text-on-surface group-hover:text-primary transition-colors leading-snug">
              ${nb.title}
            </h3>
            <p class="font-code-md text-on-surface-variant text-xs truncate mt-1">
              ${nb.path}
            </p>
          </div>
          <div class="mt-auto pt-3 flex items-center justify-between border-t border-outline-variant/50">
            <a href="${nb.colab_url}" target="_blank" rel="noopener noreferrer" class="flex items-center gap-1.5 text-xs font-label-caps text-primary hover:text-primary-fixed transition-colors">
              <span class="material-symbols-outlined text-[16px]">rocket_launch</span> COLAB 1-CLICK
            </a>
            <div class="flex gap-2">
              <a href="${nb.github_url}" target="_blank" rel="noopener noreferrer" class="text-on-surface-variant hover:text-primary transition-colors" title="Ver Código">
                <span class="material-symbols-outlined text-[18px]">visibility</span>
              </a>
              <button onclick="copyNotebookLink('${nb.colab_url}')" class="text-on-surface-variant hover:text-primary transition-colors" title="Copiar Enlace Colab">
                <span class="material-symbols-outlined text-[18px]">content_copy</span>
              </button>
            </div>
          </div>
        </div>
      `;
    }).join('');
  }

  function copyNotebookLink(url) {
    navigator.clipboard.writeText(url).then(() => {
      showToast("Enlace de Google Colab copiado 📋");
    });
  }

  // =========================================================================
  // 5. RENDERIZADO DE GUÍAS PDF Y VIDEOS
  // =========================================================================

  function renderGuias() {
    const container = document.getElementById('guiasPlaylistContainer');
    const course = getActiveCourse();
    if (!container || !course) return;

    let guiasList = course.guias || [];
    if (searchGuiasQuery.trim() !== '') {
      const q = searchGuiasQuery.toLowerCase();
      guiasList = guiasList.filter(g => 
        (g.title || '').toLowerCase().includes(q) || 
        (g.filename || '').toLowerCase().includes(q) ||
        (g.module || '').toLowerCase().includes(q)
      );
    }

    if (guiasList.length === 0) {
      container.innerHTML = `<div class="p-6 text-center text-on-surface-variant text-xs glass-panel rounded-xl border border-outline-variant">
        <span class="material-symbols-outlined text-2xl text-primary mb-1">search_off</span>
        <p>No se encontraron guías que coincidan con la búsqueda.</p>
      </div>`;
      return;
    }

    if (!currentActiveGuiaId || !guiasList.some(x => x.id === currentActiveGuiaId)) {
      loadGuia(guiasList[0].id);
    }

    container.innerHTML = guiasList.map(g => {
      const isCurrent = currentActiveGuiaId === g.id;
      return `
        <div onclick="loadGuia('${g.id}')" class="p-3.5 rounded-xl border border-outline-variant cursor-pointer transition-all hover:bg-surface-container ${isCurrent ? 'bg-primary/15 border-primary/50 shadow-[0_0_12px_rgba(56,189,248,0.15)]' : 'bg-surface-container-low'} flex items-start gap-3 group">
          <span class="material-symbols-outlined ${isCurrent ? 'text-primary' : 'text-on-surface-variant group-hover:text-primary'} text-lg mt-0.5 transition-colors">picture_as_pdf</span>
          <div class="min-w-0 flex-1">
            <div class="flex items-center justify-between gap-1 mb-0.5">
              <span class="text-[10px] font-mono text-primary font-semibold">${g.module || '🐍 Módulo 01'}</span>
              <span class="text-[10px] font-mono text-on-surface-variant">${g.size_str || ''}</span>
            </div>
            <div class="text-xs font-headline-md text-on-surface truncate group-hover:text-primary transition-colors">${g.title}</div>
          </div>
        </div>
      `;
    }).join('');
  }

  function loadGuia(guiaId) {
    const course = getActiveCourse();
    const g = (course && course.guias ? course.guias : []).find(x => x.id === guiaId);
    if (!g) return;

    currentActiveGuiaId = g.id;
    const iframe = document.getElementById('mainPdfViewer');
    const titleEl = document.getElementById('playerPdfTitle');
    const moduleEl = document.getElementById('playerPdfModule');
    const dlBtn = document.getElementById('playerPdfDownloadBtn');
    const openBtn = document.getElementById('playerPdfOpenNewTabBtn');

    const localPath = 'Guias/' + encodeURIComponent(g.filename);
    if (iframe) iframe.src = localPath;
    if (titleEl) titleEl.textContent = g.title;
    if (moduleEl) moduleEl.textContent = g.module || '🐍 Módulo 01: Python';
    if (dlBtn) dlBtn.href = localPath;
    if (openBtn) openBtn.href = localPath;

    renderGuias();
  }

  function renderVideos() {
    const container = document.getElementById('videoPlaylistContainer');
    const course = getActiveCourse();
    if (!container || !course) return;

    let videoList = course.videos || [];
    if (searchVideosQuery.trim() !== '') {
      const q = searchVideosQuery.toLowerCase();
      videoList = videoList.filter(v => 
        (v.title || '').toLowerCase().includes(q) || 
        (v.filename || '').toLowerCase().includes(q) ||
        (v.module || '').toLowerCase().includes(q)
      );
    }

    if (videoList.length === 0) {
      container.innerHTML = `<div class="p-6 text-center text-on-surface-variant text-xs glass-panel rounded-xl border border-outline-variant">
        <span class="material-symbols-outlined text-2xl text-purple-400 mb-1">movie_off</span>
        <p>No se encontraron videos que coincidan con la búsqueda.</p>
      </div>`;
      return;
    }

    if (!currentPlayingVideoId || !videoList.some(x => x.id === currentPlayingVideoId)) {
      currentPlayingVideoId = videoList[0].id;
      setupVideoPlayer(videoList[0]);
    }

    container.innerHTML = videoList.map(vid => {
      const isCurrent = currentPlayingVideoId === vid.id;
      const ytId = vid.youtube_id || (vid.youtube_url ? extractYouTubeId(vid.youtube_url) : '');
      const ytUrl = vid.youtube_url || (ytId ? `https://youtu.be/${ytId}` : null);
      const hasYoutube = Boolean(ytId || ytUrl);

      return `
        <div onclick="selectVideo('${vid.id}')" class="p-3 rounded-xl border border-outline-variant cursor-pointer transition-all hover:bg-surface-container ${isCurrent ? 'bg-primary/15 border-primary/50 shadow-[0_0_12px_rgba(56,189,248,0.15)]' : 'bg-surface-container-low'} flex items-start gap-3 group">
          <div class="relative w-9 h-9 rounded-lg ${hasYoutube ? 'bg-red-600/15 border border-red-500/30' : 'bg-primary/10 border border-primary/20'} flex items-center justify-center shrink-0 mt-0.5 group-hover:scale-105 transition-transform">
            ${hasYoutube 
              ? `<svg class="w-4 h-4 fill-current text-red-500" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>`
              : `<span class="material-symbols-outlined ${isCurrent ? 'text-primary' : 'text-purple-400 group-hover:text-primary'} text-base">${isCurrent ? 'play_circle' : 'movie'}</span>`
            }
          </div>
          <div class="min-w-0 flex-1">
            <div class="flex items-center justify-between gap-1 mb-0.5">
              <span class="text-[10px] font-mono text-purple-300 font-semibold">${vid.module || '🐍 Módulo 01'}</span>
              <span class="text-[9px] font-mono font-bold ${hasYoutube ? 'text-red-400 bg-red-500/10 px-1.5 py-0.2 rounded border border-red-500/20' : 'text-on-surface-variant'}">${hasYoutube ? 'YouTube HD' : (vid.size_mb ? vid.size_mb + ' MB' : '')}</span>
            </div>
            <div class="text-xs font-headline-md text-on-surface truncate group-hover:text-primary transition-colors">${vid.title}</div>
          </div>
          ${hasYoutube ? `
            <a href="${ytUrl}" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation()" title="Abrir directamente en YouTube" class="p-1 text-on-surface-variant hover:text-red-400 hover:bg-red-500/10 rounded transition-all mt-0.5 shrink-0">
              <span class="material-symbols-outlined text-sm">open_in_new</span>
            </a>
          ` : ''}
        </div>
      `;
    }).join('');
  }

  function extractYouTubeId(url) {
    if (!url) return '';
    const match = url.match(/(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))([\w-]{11})/);
    return match ? match[1] : '';
  }

  function setupVideoPlayer(vid) {
    const ytPlayer = document.getElementById('mainYoutubePlayer');
    const nativePlayer = document.getElementById('mainVideoPlayer');
    const titleEl = document.getElementById('playerVideoTitle');
    const moduleEl = document.getElementById('playerVideoModule');
    const ytBtn = document.getElementById('playerYoutubeBtn');
    const dlBtn = document.getElementById('playerDownloadBtn');

    if (titleEl) titleEl.textContent = vid.title;
    if (moduleEl) moduleEl.textContent = vid.module || '🐍 Módulo 01';

    const localUrl = 'Contenido/' + encodeURIComponent(vid.filename);
    if (dlBtn) dlBtn.href = localUrl;

    const ytId = vid.youtube_id || (vid.youtube_url ? extractYouTubeId(vid.youtube_url) : '');
    const ytUrl = vid.youtube_url || (ytId ? `https://youtu.be/${ytId}` : null);

    if (ytBtn) {
      if (ytUrl) {
        ytBtn.href = ytUrl;
        ytBtn.classList.remove('hidden');
      } else {
        ytBtn.classList.add('hidden');
      }
    }

    if (ytId && ytPlayer) {
      ytPlayer.classList.remove('hidden');
      ytPlayer.src = `https://www.youtube.com/embed/${ytId}?autoplay=1&rel=0&modestbranding=1`;
      if (nativePlayer) {
        nativePlayer.classList.add('hidden');
        nativePlayer.pause();
      }
    } else if (nativePlayer) {
      if (ytPlayer) {
        ytPlayer.classList.add('hidden');
        ytPlayer.src = '';
      }
      nativePlayer.classList.remove('hidden');
      nativePlayer.src = localUrl;
      nativePlayer.load();
    }
  }

  function selectVideo(vidId) {
    const course = getActiveCourse();
    const vid = (course && course.videos ? course.videos : []).find(v => v.id === vidId);
    if (!vid) return;
    currentPlayingVideoId = vid.id;
    setupVideoPlayer(vid);
    renderVideos();
  }

  function setCinemaMode(mode) {
    const container = document.getElementById('cinemaAmbientContainer');
    if (container) {
      container.className = 'p-2 sm:p-4 rounded-3xl cinema-ambient-shadow transition-all duration-500';
      showToast("Modo Cinema Ambient Glow Activado 🌌");
    }
  }

  // =========================================================================
  // 6. UTILIDADES, TOAST Y TEMA
  // =========================================================================

  function showToast(msg) {
    const existing = document.getElementById('app-toast');
    if (existing) existing.remove();

    let toast = document.createElement('div');
    toast.id = 'app-toast';
    toast.className = 'fixed bottom-6 right-6 z-50 px-4 py-2.5 rounded-xl bg-surface-container-highest text-on-surface font-mono text-xs border border-primary/40 shadow-neon-cyan flex items-center gap-2 backdrop-blur-xl animate-fade-in-up';
    toast.innerHTML = `<span class="material-symbols-outlined text-primary text-sm">bolt</span> <span>${msg}</span>`;
    document.body.appendChild(toast);
    setTimeout(() => { if (toast) toast.remove(); }, 3200);
  }

  function toggleTheme() {
    const html = document.documentElement;
    const isDark = html.classList.contains('dark');
    const themeIcon = document.getElementById('themeIcon');
    const shaderWrapper = document.getElementById('ambientShaderWrapper');
    
    if (isDark) {
      html.classList.remove('dark');
      localStorage.setItem('usta_theme', 'light');
      if (themeIcon) themeIcon.textContent = 'light_mode';
      if (shaderWrapper) shaderWrapper.style.opacity = '0.08';
      showToast('Modo Claro activado ☀️');
    } else {
      html.classList.add('dark');
      localStorage.setItem('usta_theme', 'dark');
      if (themeIcon) themeIcon.textContent = 'dark_mode';
      if (shaderWrapper) shaderWrapper.style.opacity = '0.40';
      showToast('Modo Oscuro activado 🌙');
    }
  }

  function initTheme() {
    const saved = localStorage.getItem('usta_theme');
    const themeIcon = document.getElementById('themeIcon');
    const shaderWrapper = document.getElementById('ambientShaderWrapper');
    if (saved === 'light') {
      document.documentElement.classList.remove('dark');
      if (themeIcon) themeIcon.textContent = 'light_mode';
      if (shaderWrapper) shaderWrapper.style.opacity = '0.08';
    } else {
      document.documentElement.classList.add('dark');
      if (themeIcon) themeIcon.textContent = 'dark_mode';
      if (shaderWrapper) shaderWrapper.style.opacity = '0.40';
    }
  }

  // =========================================================================
  // 7. INICIALIZACIÓN Y ENRUTAMIENTO
  // =========================================================================

  function handleRoute() {
    const hash = window.location.hash || '';
    if (hash.startsWith('#course=')) {
      const cId = hash.replace('#course=', '').trim();
      const course = (CATALOG.courses || []).find(c => c.id === cId);
      if (course && course.active !== false) {
        selectCourse(cId, false);
        return;
      }
    }
    // Por defecto, mostrar el Hub Inicial de bienvenida y selección de materias
    returnToCourseHub(false);
  }

  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    setSandboxSnippet('cv');
    renderCourseHub();

    // Comprobar ruta inicial en hash
    handleRoute();

    // Escuchar cambios de hash (navegación atrás/adelante del navegador)
    window.addEventListener('hashchange', () => {
      handleRoute();
    });

    // Iniciar auto-descubrimiento en segundo plano
    if (typeof window.autoDiscoverRepo === 'function') {
      window.autoDiscoverRepo(false);
    }

    // Buscador en Hub de Materias
    document.getElementById('courseSearchInput')?.addEventListener('input', (e) => {
      courseSearchQuery = e.target.value;
      renderCourseHub();
    });

    // Buscador global de notebooks dentro del curso
    document.getElementById('navSearchInput')?.addEventListener('input', (e) => {
      currentSearch = e.target.value;
      if (currentView !== 'course') {
        selectCourse(CATALOG.active_course_id || 'data-science-programming');
      }
      switchTab('notebooks');
      renderNotebooks();
    });

    // Filtros de guías y videos
    document.getElementById('searchGuiasInput')?.addEventListener('input', (e) => {
      searchGuiasQuery = e.target.value;
      renderGuias();
    });

    document.getElementById('searchVideosInput')?.addEventListener('input', (e) => {
      searchVideosQuery = e.target.value;
      renderVideos();
    });

    // Filtro de dificultad de notebooks
    document.getElementById('diffFilter')?.addEventListener('change', (e) => {
      currentDiff = e.target.value;
      renderNotebooks();
    });

    // Atajos de teclado globales
    document.addEventListener('keydown', (e) => {
      if (e.key === '/' && document.activeElement !== document.getElementById('navSearchInput') && document.activeElement !== document.getElementById('courseSearchInput')) {
        e.preventDefault();
        const searchInput = currentView === 'hub' ? document.getElementById('courseSearchInput') : document.getElementById('navSearchInput');
        if (searchInput) {
          searchInput.focus();
        }
      }
      if (e.key === 'Escape' && typeof window.closeDataExplorer === 'function') {
        window.closeDataExplorer();
      }
    });
  });

  // Exportar al scope global
  window.renderCourseHub = renderCourseHub;
  window.selectCourse = selectCourse;
  window.returnToCourseHub = returnToCourseHub;
  window.filterCoursesBySemester = filterCoursesBySemester;
  window.setSandboxSnippet = setSandboxSnippet;
  window.runSandboxSimulation = runSandboxSimulation;
  window.switchTab = switchTab;
  window.filterByModule = filterByModule;
  window.renderPills = renderPills;
  window.renderNotebooks = renderNotebooks;
  window.copyNotebookLink = copyNotebookLink;
  window.renderGuias = renderGuias;
  window.loadGuia = loadGuia;
  window.renderVideos = renderVideos;
  window.selectVideo = selectVideo;
  window.setCinemaMode = setCinemaMode;
  window.toggleTheme = toggleTheme;
  window.showToast = showToast;
  window.updateUiCounts = updateUiCounts;
})();
