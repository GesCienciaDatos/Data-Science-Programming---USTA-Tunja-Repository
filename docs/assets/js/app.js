/**
 * Core Application Controller
 * Next-Gen Python Virtual Lab - USTA Tunja
 */

(function initApp() {
  // Asegurar objeto de catálogo base
  if (typeof window.VIRTUAL_LAB_CATALOG === 'undefined') {
    window.VIRTUAL_LAB_CATALOG = {
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
  let currentTab = 'notebooks';
  let currentModule = 'all';
  let currentSearch = '';
  let currentDiff = 'all';
  let currentPlayingVideoId = null;
  let currentActiveGuiaId = null;
  let currentSnippetKey = 'cv';
  let searchGuiasQuery = '';
  let searchVideosQuery = '';

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

  function updateUiCounts() {
    const notebooksCount = (CATALOG.notebooks || []).length;
    const guiasCount = (CATALOG.guias || []).length;
    const videosCount = (CATALOG.videos || []).length;
    const datasetsCount = (CATALOG.datasets || []).length;

    // Header & Stat Cards
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
          pillBtn.className = 'bg-primary/20 text-primary px-3.5 py-1.5 rounded-full font-label-caps text-label-caps border border-primary/30 cursor-pointer hover:bg-primary/30 transition-all flex items-center gap-1.5 shadow-neon-cyan';
        } else {
          pillBtn.className = 'bg-surface-container px-3.5 py-1.5 rounded-full font-label-caps text-label-caps text-on-surface-variant hover:text-on-surface border border-outline-variant cursor-pointer transition-all flex items-center gap-1.5';
        }
      }

      if (navBtn) {
        if (t === tabId) {
          navBtn.className = 'font-label-caps text-label-caps text-primary border-b-2 border-primary pb-1 active:scale-95 duration-200 flex items-center gap-1';
        } else {
          navBtn.className = 'font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors hover:bg-primary/10 duration-300 px-2 py-1 rounded flex items-center gap-1';
        }
      }
    });

    updateUiCounts();
    if (tabId === 'notebooks') renderNotebooks();
    if (tabId === 'guias') renderGuias();
    if (tabId === 'videos') renderVideos();
    if (tabId === 'datasets' && typeof window.renderDatasets === 'function') window.renderDatasets();
  }

  function renderPills() {
    const container = document.getElementById('modulePillsContainer');
    if (!container || !CATALOG.modules) return;

    const totalNotebooks = (CATALOG.notebooks || []).length;
    let html = `
      <button onclick="filterByModule('all')" class="px-3 py-1 rounded-full text-xs font-mono font-medium whitespace-nowrap transition-all flex items-center gap-1.5 ${currentModule === 'all' ? 'bg-primary text-on-primary font-bold shadow-neon-cyan' : 'bg-surface-container text-on-surface-variant hover:text-on-surface border border-outline-variant'}">
        <span>🌟 Todos</span>
        <span class="px-1.5 py-0.2 rounded-full text-[10px] ${currentModule === 'all' ? 'bg-black/20 text-black' : 'bg-surface-container-high text-on-surface-variant'}">${totalNotebooks}</span>
      </button>
    `;

    CATALOG.modules.forEach(m => {
      const isCurrent = currentModule === m.id;
      const count = (CATALOG.notebooks || []).filter(n => n.module_id === m.id).length;
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
    if (!container || !CATALOG.notebooks) return;

    const filtered = (CATALOG.notebooks || []).filter(nb => {
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

  function renderGuias() {
    const container = document.getElementById('guiasPlaylistContainer');
    if (!container || !CATALOG.guias) return;

    let guiasList = CATALOG.guias || [];
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

    container.innerHTML = guiasList.map((g, idx) => {
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
    const g = (CATALOG.guias || []).find(x => x.id === guiaId);
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
    if (!container || !CATALOG.videos) return;

    let videoList = CATALOG.videos || [];
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

    container.innerHTML = videoList.map((vid, idx) => {
      const isCurrent = currentPlayingVideoId === vid.id;
      return `
        <div onclick="selectVideo('${vid.id}')" class="p-3.5 rounded-xl border border-outline-variant cursor-pointer transition-all hover:bg-surface-container ${isCurrent ? 'bg-primary/15 border-primary/50 shadow-[0_0_12px_rgba(56,189,248,0.15)]' : 'bg-surface-container-low'} flex items-start gap-3 group">
          <span class="material-symbols-outlined ${isCurrent ? 'text-primary' : 'text-purple-400 group-hover:text-primary'} text-lg mt-0.5 transition-colors">${isCurrent ? 'play_circle' : 'movie'}</span>
          <div class="min-w-0 flex-1">
            <div class="flex items-center justify-between gap-1 mb-0.5">
              <span class="text-[10px] font-mono text-purple-300 font-semibold">${vid.module || '🐍 Módulo 01'}</span>
              <span class="text-[10px] font-mono text-on-surface-variant">${vid.size_mb ? vid.size_mb + ' MB' : ''}</span>
            </div>
            <div class="text-xs font-headline-md text-on-surface truncate group-hover:text-primary transition-colors">${vid.title}</div>
          </div>
        </div>
      `;
    }).join('');
  }

  function setupVideoPlayer(vid) {
    const player = document.getElementById('mainVideoPlayer');
    const titleEl = document.getElementById('playerVideoTitle');
    const moduleEl = document.getElementById('playerVideoModule');
    const dlBtn = document.getElementById('playerDownloadBtn');

    const url = 'Contenido/' + encodeURIComponent(vid.filename);
    if (titleEl) titleEl.textContent = vid.title;
    if (moduleEl) moduleEl.textContent = vid.module || '🐍 Módulo 01';
    if (dlBtn) dlBtn.href = url;
    if (player) {
      player.src = url;
      player.load();
    }
  }

  function selectVideo(vidId) {
    const vid = (CATALOG.videos || []).find(v => v.id === vidId);
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

  function showToast(msg) {
    const existing = document.getElementById('app-toast');
    if (existing) existing.remove();

    let toast = document.createElement('div');
    toast.id = 'app-toast';
    toast.className = 'fixed bottom-6 right-6 z-50 px-4 py-2.5 rounded-xl bg-surface-container-highest text-on-surface font-mono text-xs border border-primary/40 shadow-neon-cyan flex items-center gap-2 backdrop-blur-xl';
    toast.innerHTML = `<span class="material-symbols-outlined text-primary text-sm">bolt</span> <span>${msg}</span>`;
    document.body.appendChild(toast);
    setTimeout(() => { if (toast) toast.remove(); }, 3000);
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

  // Inicialización de la aplicación
  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    setSandboxSnippet('cv');
    renderPills();
    renderNotebooks();
    updateUiCounts();

    // Iniciar auto-descubrimiento en segundo plano
    if (typeof window.autoDiscoverRepo === 'function') {
      window.autoDiscoverRepo(false);
    }

    // Buscador global de notebooks
    document.getElementById('navSearchInput')?.addEventListener('input', (e) => {
      currentSearch = e.target.value;
      switchTab('notebooks');
      renderNotebooks();
    });

    // Filtros de guias y videos
    document.getElementById('searchGuiasInput')?.addEventListener('input', (e) => {
      searchGuiasQuery = e.target.value;
      renderGuias();
    });

    document.getElementById('searchVideosInput')?.addEventListener('input', (e) => {
      searchVideosQuery = e.target.value;
      renderVideos();
    });

    // Filtro de dificultad
    document.getElementById('diffFilter')?.addEventListener('change', (e) => {
      currentDiff = e.target.value;
      renderNotebooks();
    });

    // Atajos de teclado globales
    document.addEventListener('keydown', (e) => {
      if (e.key === '/' && document.activeElement !== document.getElementById('navSearchInput')) {
        e.preventDefault();
        const searchInput = document.getElementById('navSearchInput');
        if (searchInput) {
          searchInput.focus();
          switchTab('notebooks');
        }
      }
      if (e.key === 'Escape' && typeof window.closeDataExplorer === 'function') {
        window.closeDataExplorer();
      }
    });
  });

  // Exportar funciones principales a window para uso en eventos HTML
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
