/**
 * Next-Gen Virtual Lab Platform - Core Application Controller
 * Stitch Minimalist Modern Design Architecture
 * Universidad Santo Tomás Seccional Tunja — Especialización en Ciencia de Datos
 */

(function initVirtualLabApp() {
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
  let currentCourseId = 'data-science-programming';
  let currentModality = 'standard'; // 'standard', 'dummies', 'homeworks'
  let currentModule = 'all';
  let currentSearch = '';
  let currentDiff = 'all';
  let courseSearchQuery = '';
  let courseSemesterFilter = 'all';
  let currentSnippetKey = 'cv';

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
  // 1. GESTIÓN DEL PORTAL DE MATERIAS (COURSE HUB)
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
      const modCount = (c.modules || []).length;

      const badgeStyle = isActive 
        ? 'bg-emerald-500/20 text-emerald-400 border-emerald-500/30' 
        : 'bg-amber-500/20 text-amber-300 border-amber-500/30';

      const borderGlow = isActive
        ? 'border-primary/30 hover:border-primary shadow-[0_0_20px_rgba(56,189,248,0.12)] hover:shadow-[0_0_30px_rgba(56,189,248,0.25)]'
        : 'border-outline-variant/50 hover:border-outline-variant hover:shadow-[0_0_15px_rgba(245,158,11,0.1)]';

      const animDelayClass = `delay-${Math.min((idx + 1) * 100, 500)}`;

      return `
        <div class="glass-card-interactive rounded-2xl p-6 border ${borderGlow} flex flex-col justify-between transition-all duration-300 group relative overflow-hidden bg-surface-container/60 animate-fade-in-up ${animDelayClass}">
          
          <!-- Ambient subtle glow -->
          <div class="absolute -right-10 -top-10 w-32 h-32 rounded-full ${isActive ? 'bg-primary/10 group-hover:bg-primary/20' : 'bg-amber-500/10 group-hover:bg-amber-500/20'} blur-3xl pointer-events-none transition-all"></div>

          <div>
            <!-- Header: Icon & Badges -->
            <div class="flex items-start justify-between gap-3 mb-4">
              <div class="w-12 h-12 rounded-xl bg-surface-container-highest/80 border border-outline-variant/60 flex items-center justify-center text-2xl shadow-inner group-hover:scale-105 transition-transform duration-300">
                ${c.icon || '📚'}
              </div>
              <div class="flex flex-col items-end gap-1">
                <span class="px-2.5 py-0.5 rounded-full text-[10px] font-code-md font-bold border ${badgeStyle}">
                  ${isActive ? '🟢 100% Desarrollado' : '🚧 En Construcción'}
                </span>
                <span class="text-[10px] font-code-md text-on-surface-variant font-semibold">
                  ${c.semester || 'Semestre I'}
                </span>
              </div>
            </div>

            <!-- Title & Subtitle -->
            <h3 class="font-display-sm text-lg font-bold text-on-surface group-hover:text-primary transition-colors leading-snug mb-1">
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
            <div class="grid grid-cols-3 gap-2 mb-6 font-code-md text-[11px]">
              <div class="p-2 rounded-lg bg-surface-dim/80 border border-outline-variant/40 text-center">
                <span class="block text-[9px] text-on-surface-variant">CUADERNOS</span>
                <span class="font-bold text-on-surface text-xs">${isActive ? nbCount : 'En Prep.'}</span>
              </div>
              <div class="p-2 rounded-lg bg-surface-dim/80 border border-outline-variant/40 text-center">
                <span class="block text-[9px] text-on-surface-variant">MÓDULOS</span>
                <span class="font-bold text-tertiary text-xs">${isActive ? modCount : 'En Prep.'}</span>
              </div>
              <div class="p-2 rounded-lg bg-surface-dim/80 border border-outline-variant/40 text-center">
                <span class="block text-[9px] text-on-surface-variant">DATASETS</span>
                <span class="font-bold text-primary text-xs">${isActive ? dsCount : 'En Prep.'}</span>
              </div>
            </div>
          </div>

          <!-- Bottom Action Button -->
          <div class="pt-4 border-t border-outline-variant/30 flex items-center justify-between gap-3">
            ${isActive ? `
              <button onclick="selectCourse('${c.id}')" class="w-full py-2.5 px-4 rounded-xl bg-primary text-on-primary font-label-caps text-xs font-bold hover:bg-primary-fixed active:scale-95 transition-all duration-300 flex items-center justify-center gap-2 group/btn shadow-[0_0_15px_rgba(56,189,248,0.25)]">
                <span>INGRESAR AL LABORATORIO</span>
                <span class="material-symbols-outlined text-sm group-hover/btn:translate-x-1 transition-transform">arrow_forward</span>
              </button>
            ` : `
              <button onclick="showToast('🚧 Materia en construcción. El contenido pedagógico se incorporará próximamente.')" class="w-full py-2.5 px-4 rounded-xl bg-amber-500/10 hover:bg-amber-500/20 text-amber-300 font-label-caps text-xs font-semibold border border-amber-500/30 transition-all flex items-center justify-center gap-2">
                <span class="material-symbols-outlined text-sm text-amber-400">construction</span>
                <span>EN CONSTRUCCIÓN</span>
              </button>
            `}
          </div>

        </div>
      `;
    }).join('');
  }

  function selectCourse(courseId) {
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

    // Alternar vistas
    const hubView = document.getElementById('coursesHubView');
    const courseView = document.getElementById('courseWorkspaceView');
    const navCourseSelector = document.getElementById('navCourseSelectorContainer');
    const navActiveCourseName = document.getElementById('navActiveCourseName');
    const navActiveCourseIcon = document.getElementById('navActiveCourseIcon');
    const heroTitle = document.getElementById('activeCourseHeroTitle');
    const heroDesc = document.getElementById('activeCourseHeroDesc');
    const heroIcon = document.getElementById('activeCourseHeroIcon');
    const heroSemester = document.getElementById('activeCourseHeroSemester');
    const heroNotebooks = document.getElementById('activeCourseHeroNotebooks');
    const heroModules = document.getElementById('activeCourseHeroModules');

    if (hubView) { hubView.classList.add('force-hidden'); }
    if (courseView) { courseView.classList.remove('force-hidden'); }
    if (navCourseSelector) { navCourseSelector.classList.remove('force-hidden'); navCourseSelector.classList.add('force-flex'); }

    if (navActiveCourseName) navActiveCourseName.textContent = course.name;
    if (navActiveCourseIcon) navActiveCourseIcon.textContent = course.icon || '🐍';
    if (heroTitle) heroTitle.textContent = course.name;
    if (heroDesc) heroDesc.textContent = course.description;
    if (heroIcon) heroIcon.textContent = course.icon || '🐍';
    if (heroSemester) heroSemester.textContent = course.semester || 'Semestre I';
    if (heroNotebooks) heroNotebooks.textContent = course.stats ? course.stats.total_notebooks : (course.notebooks || []).length;
    if (heroModules) heroModules.textContent = (course.modules || []).length;

    renderModulePills();
    renderCourseModules();

    window.scrollTo({ top: 0, behavior: 'smooth' });
    showToast(`Laboratorio Virtual: ${course.name} ⚡`);
  }

  function returnToCourseHub() {
    currentView = 'hub';

    const hubView = document.getElementById('coursesHubView');
    const courseView = document.getElementById('courseWorkspaceView');
    const navCourseSelector = document.getElementById('navCourseSelectorContainer');

    if (hubView) { hubView.classList.remove('force-hidden'); }
    if (courseView) { courseView.classList.add('force-hidden'); }
    if (navCourseSelector) { navCourseSelector.classList.add('force-hidden'); navCourseSelector.classList.remove('force-flex'); }

    renderCourseHub();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function filterCoursesBySemester(sem) {
    courseSemesterFilter = sem;
    const allBtns = [
      { id: 'courseFilterSemesterAll', value: 'all' },
      { id: 'courseFilterSemester1', value: 'Semestre I' },
      { id: 'courseFilterSemester2', value: 'Semestre II' }
    ];

    allBtns.forEach(item => {
      const btn = document.getElementById(item.id);
      if (!btn) return;
      if (item.value === sem) {
        btn.className = 'px-3 py-1 rounded-lg bg-primary/20 text-primary border border-primary/30 transition-all font-bold shadow-sm';
      } else {
        btn.className = 'px-3 py-1 rounded-lg text-on-surface-variant hover:text-on-surface transition-all';
      }
    });

    renderCourseHub();
  }

  // =========================================================================
  // 2. GESTIÓN DE MODALIDADES (ESTÁNDAR vs DUMMIES vs HOMEWORKS)
  // =========================================================================

  function switchModality(mode) {
    currentModality = mode;
    const btnStd = document.getElementById('modalityStandardBtn');
    const btnDum = document.getElementById('modalityDummiesBtn');
    const btnHw = document.getElementById('modalityHomeworksBtn');

    // Reset styles
    if (btnStd) btnStd.className = 'px-4 py-2 rounded-lg text-xs font-label-caps flex items-center gap-2 text-on-surface-variant hover:text-primary transition-all shrink-0';
    if (btnDum) btnDum.className = 'px-4 py-2 rounded-lg text-xs font-label-caps flex items-center gap-2 text-on-surface-variant hover:text-tertiary transition-all shrink-0';
    if (btnHw) btnHw.className = 'px-4 py-2 rounded-lg text-xs font-label-caps flex items-center gap-2 text-on-surface-variant hover:text-emerald-400 transition-all shrink-0';

    if (mode === 'standard' && btnStd) {
      btnStd.className = 'px-4 py-2 rounded-lg text-xs font-label-caps flex items-center gap-2 transition-all active-tab-glow shrink-0 font-bold';
      showToast("📘 Edición Estándar: Rigor matemático y derivaciones completas");
    } else if (mode === 'dummies' && btnDum) {
      btnDum.className = 'px-4 py-2 rounded-lg text-xs font-label-caps flex items-center gap-2 transition-all active-tab-amber shrink-0 font-bold';
      showToast("💡 Edición Para Dummies: Analogías y modelos intuitivos");
    } else if (mode === 'homeworks' && btnHw) {
      btnHw.className = 'px-4 py-2 rounded-lg text-xs font-label-caps flex items-center gap-2 transition-all active-tab-emerald shrink-0 font-bold';
      showToast("🧪 Hands-On Homeworks: Laboratorios evaluativos guiados");
    }

    renderModulePills();
    renderCourseModules();
  }

  // =========================================================================
  // 3. RENDERIZADO DE MÓDULOS Y CUADERNOS EN WORKSPACE
  // =========================================================================

  function renderModulePills() {
    const container = document.getElementById('moduleFilterButtonsContainer');
    const course = getActiveCourse();
    if (!container || !course || !course.modules) return;

    let totalNotebooks = (course.notebooks || []).length;
    if (currentModality === 'dummies') {
      totalNotebooks = (course.notebooks || []).filter(n => n.is_dummies).length;
    } else if (currentModality === 'homeworks') {
      totalNotebooks = (course.notebooks || []).filter(n => n.is_homework || n.path.includes('homeworks')).length;
    }

    let html = `
      <button onclick="filterByModule('all')" class="px-3 py-1.5 rounded-lg text-xs font-code-md transition-all flex items-center gap-1.5 shrink-0 ${currentModule === 'all' ? 'bg-primary/20 text-primary border border-primary/40 font-bold shadow-sm' : 'bg-surface-container-low text-on-surface-variant hover:text-on-surface border border-outline-variant/40'}">
        <span>🌟 Todos los Módulos</span>
        <span class="px-1.5 py-0.2 rounded-full text-[10px] bg-surface-container-highest text-on-surface-variant">${totalNotebooks}</span>
      </button>
    `;

    course.modules.forEach(m => {
      const isCurrent = currentModule === m.id;
      let count = (course.notebooks || []).filter(n => n.module_id === m.id).length;
      if (currentModality === 'dummies') {
        count = (course.notebooks || []).filter(n => n.module_id === m.id && n.is_dummies).length;
      } else if (currentModality === 'homeworks') {
        count = (course.notebooks || []).filter(n => n.module_id === m.id && (n.is_homework || n.path.includes('homeworks'))).length;
      }

      html += `
        <button onclick="filterByModule('${m.id}')" class="px-3 py-1.5 rounded-lg text-xs font-code-md transition-all flex items-center gap-1.5 shrink-0 ${isCurrent ? 'bg-primary/20 text-primary border border-primary/40 font-bold shadow-sm' : 'bg-surface-container-low text-on-surface-variant hover:text-on-surface border border-outline-variant/40'}">
          <span>${m.icon || '📁'} ${m.name}</span>
          <span class="px-1.5 py-0.2 rounded-full text-[10px] bg-surface-container-highest text-on-surface-variant">${count}</span>
        </button>
      `;
    });

    container.innerHTML = html;
  }

  function filterByModule(modId) {
    currentModule = modId;
    renderModulePills();
    renderCourseModules();
  }

  function filterNotebooks() {
    const searchInput = document.getElementById('notebookSearchInput');
    const diffSelect = document.getElementById('notebookDifficultyFilter');

    if (searchInput) currentSearch = searchInput.value;
    if (diffSelect) currentDiff = diffSelect.value;

    renderCourseModules();
  }

  function renderCourseModules() {
    const container = document.getElementById('courseModulesContainer');
    const course = getActiveCourse();
    if (!container || !course || !course.modules) return;

    let notebooks = course.notebooks || [];

    // Filtrar según modalidad activa
    if (currentModality === 'standard') {
      notebooks = notebooks.filter(n => !n.is_dummies && !n.is_homework && !n.path.includes('homeworks'));
    } else if (currentModality === 'dummies') {
      notebooks = notebooks.filter(n => n.is_dummies === true && !n.is_homework && !n.path.includes('homeworks'));
    } else if (currentModality === 'homeworks') {
      notebooks = notebooks.filter(n => n.is_homework === true || n.path.includes('homeworks'));
    }

    // Filtrar según módulo seleccionado
    let visibleModules = course.modules;
    if (currentModule !== 'all') {
      visibleModules = course.modules.filter(m => m.id === currentModule);
    }

    // Filtrar cuadernos según búsqueda y dificultad
    const q = currentSearch.toLowerCase().trim();
    const d = currentDiff.toLowerCase();

    const filteredNotebooks = notebooks.filter(nb => {
      if (d !== 'all' && !nb.difficulty.toLowerCase().includes(d)) return false;
      if (q !== '') {
        const inTitle = (nb.title || '').toLowerCase().includes(q);
        const inPath = (nb.path || '').toLowerCase().includes(q);
        const inModule = (nb.module_name || '').toLowerCase().includes(q);
        if (!inTitle && !inPath && !inModule) return false;
      }
      return true;
    });

    if (filteredNotebooks.length === 0) {
      container.innerHTML = `
        <div class="py-16 text-center glass-panel rounded-2xl border border-outline-variant/40 space-y-3">
          <span class="material-symbols-outlined text-primary text-4xl">search_off</span>
          <h3 class="font-headline-md text-on-surface text-base font-bold">No se encontraron cuadernos</h3>
          <p class="text-xs text-on-surface-variant max-w-md mx-auto">Prueba ajustando el término de búsqueda o cambiando la modalidad / dificultad.</p>
        </div>
      `;
      return;
    }

    // Agrupar por módulo
    container.innerHTML = visibleModules.map(mod => {
      const modNotebooks = filteredNotebooks.filter(nb => nb.module_id === mod.id);
      if (modNotebooks.length === 0) return '';

      return `
        <section class="space-y-4">
          
          <!-- Module Header Bar -->
          <div class="glass-panel rounded-xl px-5 py-3.5 border border-outline-variant/40 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 bg-surface-container/80">
            <div class="flex items-center gap-3">
              <span class="w-9 h-9 rounded-lg bg-surface-container-highest flex items-center justify-center text-lg border border-outline-variant/40">
                ${mod.icon || '📁'}
              </span>
              <div>
                <h3 class="font-display-sm text-base font-bold text-on-surface flex items-center gap-2">
                  ${mod.name}
                  <span class="px-2 py-0.5 rounded-full text-[10px] font-code-md bg-primary/10 text-primary border border-primary/20">
                    ${modNotebooks.length} ${modNotebooks.length === 1 ? 'Cuaderno' : 'Cuadernos'}
                  </span>
                </h3>
                <p class="text-xs text-on-surface-variant">${mod.description || 'Laboratorios computacionales interactivos'}</p>
              </div>
            </div>
          </div>

          <!-- Notebook Cards Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            ${modNotebooks.map((nb, nIdx) => {
              let diffBadge = 'bg-primary/10 text-primary border-primary/20';
              if (nb.difficulty.includes('Principiante') || nb.difficulty.includes('Básico')) {
                diffBadge = 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20';
              } else if (nb.difficulty.includes('Avanzado')) {
                diffBadge = 'bg-rose-500/10 text-rose-400 border-rose-500/20';
              } else if (nb.difficulty.includes('Intermedio')) {
                diffBadge = 'bg-amber-500/10 text-amber-300 border-amber-500/20';
              }

              const isDummies = Boolean(nb.is_dummies);
              const isHomework = Boolean(nb.is_homework || nb.path.includes('homeworks'));

              return `
                <div class="glass-card-interactive rounded-xl p-5 border border-outline-variant/40 flex flex-col justify-between gap-4 group">
                  
                  <div>
                    <!-- Top Tag & Difficulty -->
                    <div class="flex items-center justify-between gap-2 mb-2.5">
                      <span class="font-code-md text-[11px] text-primary font-bold">
                        #${String(nIdx + 1).padStart(2, '0')}
                      </span>
                      <div class="flex items-center gap-1.5">
                        <span class="px-2 py-0.5 rounded text-[10px] font-code-md font-bold border ${diffBadge}">
                          ${nb.difficulty}
                        </span>
                        ${isDummies ? '<span class="px-2 py-0.5 rounded text-[10px] font-code-md font-bold bg-amber-400/15 text-amber-300 border border-amber-400/30">💡 DUMMIES</span>' : ''}
                        ${isHomework ? '<span class="px-2 py-0.5 rounded text-[10px] font-code-md font-bold bg-emerald-400/15 text-emerald-300 border border-emerald-400/30">🧪 LAB</span>' : ''}
                      </div>
                    </div>

                    <!-- Notebook Title -->
                    <h4 class="font-headline-md text-sm font-bold text-on-surface group-hover:text-primary transition-colors leading-snug mb-2">
                      ${nb.title}
                    </h4>

                    <!-- File Path -->
                    <p class="font-code-md text-[11px] text-on-surface-variant/70 truncate">
                      ${nb.path}
                    </p>
                  </div>

                  <!-- Actions: Colab & GitHub & Copy -->
                  <div class="pt-3 border-t border-outline-variant/30 flex items-center justify-between gap-2">
                    <a 
                      href="${nb.colab_url}" 
                      target="_blank" 
                      rel="noopener noreferrer" 
                      class="px-3 py-1.5 rounded-lg bg-primary/10 hover:bg-primary text-primary hover:text-on-primary text-xs font-label-caps font-bold transition-all flex items-center gap-1.5 shadow-sm"
                    >
                      <span class="material-symbols-outlined text-sm">rocket_launch</span>
                      <span>COLAB</span>
                    </a>

                    <div class="flex items-center gap-1">
                      <a 
                        href="${nb.github_url}" 
                        target="_blank" 
                        rel="noopener noreferrer" 
                        class="p-1.5 rounded-lg hover:bg-surface-container-highest text-on-surface-variant hover:text-primary transition-colors" 
                        title="Ver Código en GitHub"
                      >
                        <span class="material-symbols-outlined text-base">code</span>
                      </a>
                      <button 
                        onclick="copyNotebookLink('${nb.colab_url}')" 
                        class="p-1.5 rounded-lg hover:bg-surface-container-highest text-on-surface-variant hover:text-primary transition-colors" 
                        title="Copiar enlace a Colab"
                      >
                        <span class="material-symbols-outlined text-base">content_copy</span>
                      </button>
                    </div>
                  </div>

                </div>
              `;
            }).join('')}
          </div>

        </section>
      `;
    }).join('');
  }

  // =========================================================================
  // 4. TERMINAL SANDBOX LOGIC
  // =========================================================================

  function switchSandboxSnippet(key) {
    currentSnippetKey = key;
    const snippet = SANDBOX_SNIPPETS[key];
    const codeContainer = document.getElementById('sandboxCodeContainer');
    const outputContainer = document.getElementById('sandboxOutputContainer');

    if (codeContainer) codeContainer.innerHTML = snippet.code;
    if (outputContainer) outputContainer.textContent = snippet.output;

    ['cv', 'eda', 'fe'].forEach(k => {
      const btn = document.getElementById(`sandboxTab${k.toUpperCase()}`);
      if (!btn) return;
      if (k === key) {
        btn.className = 'px-2 py-0.5 rounded bg-primary/20 text-primary border border-primary/30';
      } else {
        btn.className = 'px-2 py-0.5 rounded text-on-surface-variant hover:text-on-surface';
      }
    });
  }

  function runSandboxSnippet() {
    const btn = document.getElementById('sandboxRunBtn');
    const output = document.getElementById('sandboxOutputContainer');
    if (!btn) return;

    btn.classList.add('opacity-50', 'pointer-events-none');
    output.textContent = "⏳ Ejecutando kernel en entorno aislado...";

    setTimeout(() => {
      btn.classList.remove('opacity-50', 'pointer-events-none');
      if (output) output.textContent = SANDBOX_SNIPPETS[currentSnippetKey].output;
      showToast("Kernel completó la simulación en 38ms ⚡");
    }, 350);
  }

  // =========================================================================
  // 5. EXPLORADOR DE DATASETS MODAL
  // =========================================================================

  function openDatasetExplorer() {
    const modal = document.getElementById('datasetExplorerModal');
    const listContainer = document.getElementById('datasetListContainer');
    const course = getActiveCourse();

    if (!modal || !listContainer) return;
    modal.classList.remove('force-hidden');
    modal.classList.add('force-flex');

    const datasets = (course && course.datasets) ? course.datasets : (CATALOG.datasets || []);

    if (datasets.length === 0) {
      listContainer.innerHTML = `<p class="text-xs text-on-surface-variant p-4">No hay datasets cargados.</p>`;
      return;
    }

    listContainer.innerHTML = datasets.map((ds, idx) => `
      <button 
        onclick="previewDatasetItem(${idx})" 
        class="w-full text-left p-3 rounded-xl border border-outline-variant/30 hover:border-primary/40 bg-surface-container-low hover:bg-surface-container-high transition-all group"
      >
        <div class="flex items-center justify-between mb-1">
          <span class="font-code-md text-xs font-bold text-on-surface group-hover:text-primary transition-colors">${ds.name}</span>
          <span class="font-code-md text-[10px] text-on-surface-variant">${ds.size || 'CSV'}</span>
        </div>
        <p class="text-[11px] text-on-surface-variant line-clamp-2">${ds.description || 'Dataset para modelado y evaluación'}</p>
      </button>
    `).join('');

    previewDatasetItem(0);
  }

  function previewDatasetItem(idx) {
    const course = getActiveCourse();
    const datasets = (course && course.datasets) ? course.datasets : (CATALOG.datasets || []);
    const ds = datasets[idx];
    if (!ds) return;

    const metaContainer = document.getElementById('datasetMetadataContainer');
    const previewContainer = document.getElementById('datasetPreviewContainer');

    if (metaContainer) {
      metaContainer.innerHTML = `
        <div class="flex items-center justify-between flex-wrap gap-2 pb-3 border-b border-outline-variant/30">
          <div>
            <h4 class="font-display-sm text-base font-bold text-primary">${ds.name}</h4>
            <p class="text-xs text-on-surface-variant">${ds.description || ''}</p>
          </div>
          <div class="flex items-center gap-2">
            <span class="px-2.5 py-1 rounded bg-surface-container-highest font-code-md text-xs text-on-surface border border-outline-variant/40">
              📊 ${ds.rows ? ds.rows.toLocaleString() : 'N/A'} Filas × ${ds.columns || 'N/A'} Columnas
            </span>
          </div>
        </div>
      `;
    }

    if (previewContainer) {
      if (ds.sample_data && ds.sample_data.length > 0) {
        const headers = Object.keys(ds.sample_data[0]);
        previewContainer.innerHTML = `
          <table class="w-full text-left border-collapse font-code-md text-xs">
            <thead>
              <tr class="bg-surface-container-highest/80 text-on-surface border-b border-outline-variant/40">
                ${headers.map(h => `<th class="p-2.5 font-bold">${h}</th>`).join('')}
              </tr>
            </thead>
            <tbody class="divide-y divide-outline-variant/20 text-on-surface-variant">
              ${ds.sample_data.map(row => `
                <tr class="hover:bg-surface-container-high/50">
                  ${headers.map(h => `<td class="p-2.5">${row[h] !== undefined ? row[h] : ''}</td>`).join('')}
                </tr>
              `).join('')}
            </tbody>
          </table>
        `;
      } else {
        previewContainer.innerHTML = `
          <div class="p-6 text-center text-xs text-on-surface-variant font-code-md">
            📁 Dataset disponible para descarga o ejecución directa en cuadernos.
          </div>
        `;
      }
    }
  }

  function closeDatasetExplorer() {
    const modal = document.getElementById('datasetExplorerModal');
    if (modal) {
      modal.classList.add('force-hidden');
      modal.classList.remove('force-flex');
    }
  }

  // =========================================================================
  // 6. UTILIDADES, TOASTS & BÚSQUEDA GLOBAL
  // =========================================================================

  function copyNotebookLink(url) {
    if (navigator.clipboard) {
      navigator.clipboard.writeText(url).then(() => {
        showToast("¡Enlace a Google Colab copiado al portapapeles! 📋");
      });
    } else {
      showToast("Enlace: " + url);
    }
  }

  function showToast(msg) {
    let toast = document.getElementById('appGlobalToast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'appGlobalToast';
      toast.className = 'fixed bottom-6 right-6 z-50 glass-panel-elevated text-xs font-body-md font-semibold text-on-surface px-4 py-3 rounded-xl border border-primary/40 shadow-neon-cyan transition-all duration-300 opacity-0 translate-y-4 pointer-events-none max-w-sm';
      document.body.appendChild(toast);
    }

    toast.textContent = msg;
    toast.classList.remove('opacity-0', 'translate-y-4', 'pointer-events-none');
    toast.classList.add('opacity-100', 'translate-y-0');

    clearTimeout(toast._timeout);
    toast._timeout = setTimeout(() => {
      toast.classList.remove('opacity-100', 'translate-y-0');
      toast.classList.add('opacity-0', 'translate-y-4', 'pointer-events-none');
    }, 3200);
  }

  function toggleAmbientShader() {
    const wrapper = document.getElementById('ambientShaderWrapper');
    const icon = document.getElementById('shaderToggleIcon');
    if (!wrapper) return;

    if (wrapper.style.opacity === '0' || wrapper.classList.contains('opacity-0')) {
      wrapper.style.opacity = '0.35';
      wrapper.classList.remove('opacity-0');
      if (icon) icon.textContent = 'blur_on';
      showToast("WebGL Ambient Canvas: Activado ✨");
    } else {
      wrapper.style.opacity = '0';
      wrapper.classList.add('opacity-0');
      if (icon) icon.textContent = 'blur_off';
      showToast("WebGL Ambient Canvas: Pausado");
    }
  }

  // Atajos de teclado & Listeners
  window.addEventListener('keydown', (e) => {
    if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
      e.preventDefault();
      const s = document.getElementById('globalSearchInput');
      if (s) s.focus();
    }
    if (e.key === 'Escape') {
      closeDatasetExplorer();
      closeGlobalSearchModal();
    }
  });

  // Listener para búsqueda en curso y global
  const nbSearch = document.getElementById('notebookSearchInput');
  if (nbSearch) {
    nbSearch.addEventListener('input', () => {
      currentSearch = nbSearch.value;
      renderCourseModules();
    });
  }

  const gSearch = document.getElementById('globalSearchInput');
  if (gSearch) {
    gSearch.addEventListener('input', () => {
      handleGlobalSearch(gSearch.value);
    });
  }

  function handleGlobalSearch(query) {
    const modal = document.getElementById('globalSearchResultsModal');
    const list = document.getElementById('globalSearchResultsList');
    if (!modal || !list) return;

    if (query.trim().length < 2) {
      modal.classList.add('force-hidden');
      modal.classList.remove('force-flex');
      return;
    }

    modal.classList.remove('force-hidden');
    modal.classList.add('force-flex');

    const q = query.toLowerCase();
    const course = getActiveCourse();
    const allNbs = (course && course.notebooks) ? course.notebooks : [];

    const matches = allNbs.filter(nb => 
      (nb.title || '').toLowerCase().includes(q) ||
      (nb.path || '').toLowerCase().includes(q) ||
      (nb.module_name || '').toLowerCase().includes(q)
    );

    if (matches.length === 0) {
      list.innerHTML = `<p class="text-xs text-on-surface-variant p-4 text-center">No se encontraron resultados para "${query}".</p>`;
      return;
    }

    list.innerHTML = matches.slice(0, 10).map(nb => `
      <div class="p-3 rounded-lg bg-surface-container-low hover:bg-surface-container-high border border-outline-variant/30 flex justify-between items-center gap-3 transition-colors">
        <div>
          <span class="text-[10px] font-code-md text-primary font-bold">${nb.module_name}</span>
          <h5 class="text-xs font-bold text-on-surface">${nb.title}</h5>
          <p class="text-[10px] font-code-md text-on-surface-variant">${nb.path}</p>
        </div>
        <a href="${nb.colab_url}" target="_blank" class="px-2.5 py-1 rounded bg-primary text-on-primary text-[11px] font-label-caps font-bold shrink-0">
          ABRIR
        </a>
      </div>
    `).join('');
  }

  function closeGlobalSearchModal() {
    const modal = document.getElementById('globalSearchResultsModal');
    if (modal) {
      modal.classList.add('force-hidden');
      modal.classList.remove('force-flex');
    }
  }

  // Exponer funciones globales
  window.selectCourse = selectCourse;
  window.returnToCourseHub = returnToCourseHub;
  window.filterCoursesBySemester = filterCoursesBySemester;
  window.switchModality = switchModality;
  window.filterByModule = filterByModule;
  window.filterNotebooks = filterNotebooks;
  window.switchSandboxSnippet = switchSandboxSnippet;
  window.runSandboxSnippet = runSandboxSnippet;
  window.openDatasetExplorer = openDatasetExplorer;
  window.closeDatasetExplorer = closeDatasetExplorer;
  window.previewDatasetItem = previewDatasetItem;
  window.copyNotebookLink = copyNotebookLink;
  window.showToast = showToast;
  window.toggleAmbientShader = toggleAmbientShader;
  window.closeGlobalSearchModal = closeGlobalSearchModal;

  // Inicialización de la vista
  renderCourseHub();
  syncActiveCourseData();
})();
