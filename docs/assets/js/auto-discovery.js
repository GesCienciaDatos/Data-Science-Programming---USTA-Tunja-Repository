/**
 * Real-Time GitHub Repository Auto-Discovery Engine
 * Automatically scans and registers new Modules, Notebooks, Datasets, Guías, and Videos.
 * Next-Gen Python Virtual Lab - USTA Tunja
 */

(function initAutoDiscoveryEngine() {
  const REPO_OWNER = "sazuniga06";
  const REPO_NAME = "Data-Science-Programming---USTA-Tunja-Repository";
  const BRANCH = "main";
  const CACHE_KEY = "usta_catalog_discovery_cache";
  const CACHE_TTL_MS = 5 * 60 * 1000; // 5 minutos de caché

  const MODULE_PALETTE = [
    { icon: "🐍", color: "#3776AB" },
    { icon: "🔢", color: "#013243" },
    { icon: "🐼", color: "#150458" },
    { icon: "📊", color: "#388E3C" },
    { icon: "🧹", color: "#D97706" },
    { icon: "⚙️", color: "#7C3AED" },
    { icon: "📈", color: "#0284C7" },
    { icon: "🧠", color: "#8B5CF6" },
    { icon: "🤖", color: "#EC4899" },
    { icon: "🌐", color: "#14B8A6" },
    { icon: "📝", color: "#DC2626" }
  ];

  function formatTitle(str) {
    let clean = str
      .replace(/\.[^/.]+$/, '')
      .replace(/^\d+[a-z]?_/, '')
      .replace(/_compressed$/i, '')
      .replace(/[_-]/g, ' ')
      .trim();
    
    // Capitalización de palabras
    return clean.charAt(0).toUpperCase() + clean.slice(1);
  }

  function inferDifficulty(title, path) {
    const text = (title + " " + path).toLowerCase();
    if (text.includes("intro") || text.includes("conceptos") || text.includes("sintaxis") || text.includes("creacion") || text.includes("basico")) {
      return "Básico";
    }
    if (text.includes("avanzado") || text.includes("regularizacion") || text.includes("knn") || text.includes("pca") || text.includes("poo") || text.includes("clases")) {
      return "Avanzado";
    }
    return "Intermedio";
  }

  async function fetchRepoTree() {
    // 1. Verificar si hay caché en sesión
    const cached = sessionStorage.getItem(CACHE_KEY);
    if (cached) {
      try {
        const parsed = JSON.parse(cached);
        if (Date.now() - parsed.timestamp < CACHE_TTL_MS) {
          return parsed.tree;
        }
      } catch (e) {
        sessionStorage.removeItem(CACHE_KEY);
      }
    }

    // 2. Consultar API de árbol recursivo de GitHub (o master si falla main)
    const branches = [BRANCH, "master"];
    for (const b of branches) {
      try {
        const url = `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/git/trees/${b}?recursive=1`;
        const res = await fetch(url, { headers: { 'Accept': 'application/vnd.github.v3+json' } });
        if (res.ok) {
          const data = await res.json();
          if (data && Array.isArray(data.tree)) {
            sessionStorage.setItem(CACHE_KEY, JSON.stringify({
              timestamp: Date.now(),
              tree: data.tree
            }));
            return data.tree;
          }
        }
      } catch (err) {
        console.warn(`Error consultando rama ${b}:`, err);
      }
    }
    return null;
  }

  async function autoDiscoverRepo(showNotification = false) {
    if (showNotification && typeof window.showToast === 'function') {
      window.showToast("Escaneando repositorio en GitHub... 🔄");
    }

    const tree = await fetchRepoTree();
    if (!tree) {
      if (showNotification && typeof window.showToast === 'function') {
        window.showToast("No se pudo conectar con la API de GitHub (usando catálogo local)");
      }
      return;
    }

    if (!window.VIRTUAL_LAB_CATALOG) return;
    const cat = window.VIRTUAL_LAB_CATALOG;

    let newNotebooks = 0;
    let newDatasets = 0;
    let newGuias = 0;
    let newVideos = 0;
    let newModules = 0;

    // A. Detectar Módulos y Carpetas de la forma "XX - Nombre" o "homeworks"
    const modulePaths = new Set();
    tree.forEach(item => {
      if (item.type === 'tree') {
        const match = item.path.match(/^(\d{2})\s*-\s*(.+)$/);
        if (match) {
          const modId = match[1];
          const modName = item.path;
          if (!cat.modules.some(m => m.id === modId)) {
            const paletteItem = MODULE_PALETTE[cat.modules.length % MODULE_PALETTE.length];
            cat.modules.push({
              id: modId,
              name: modName,
              title: formatTitle(match[2]),
              icon: paletteItem.icon,
              color: paletteItem.color,
              description: `Módulo formativo sobre ${formatTitle(match[2])}.`
            });
            newModules++;
          }
        }
      }
    });

    // B. Detectar Cuadernos Jupyter (.ipynb)
    tree.forEach(item => {
      if (item.type === 'blob' && item.path.endsWith('.ipynb') && !item.path.includes('.ipynb_checkpoints')) {
        const pathParts = item.path.split('/');
        const filename = pathParts[pathParts.length - 1];
        
        // Excluir notebooks en carpetas temporales
        if (item.path.startsWith('tmp/') || item.path.startsWith('.gemini/')) return;

        const exists = cat.notebooks.some(n => n.path === item.path || n.filename === filename);
        if (!exists) {
          let moduleId = "01";
          let moduleName = "01 - Python";

          if (item.path.startsWith('homeworks/')) {
            moduleId = "hw";
            moduleName = "homeworks";
          } else {
            const modMatch = item.path.match(/^(\d{2})/);
            if (modMatch) {
              moduleId = modMatch[1];
              const foundMod = cat.modules.find(m => m.id === moduleId);
              if (foundMod) moduleName = foundMod.name;
            }
          }

          const cleanTitle = formatTitle(filename);
          const diff = inferDifficulty(cleanTitle, item.path);
          const encodedPath = encodeURIComponent(item.path).replace(/%2F/g, '/');

          cat.notebooks.push({
            id: filename,
            module_id: moduleId,
            module_name: moduleName,
            filename: filename,
            title: cleanTitle,
            path: item.path,
            difficulty: diff,
            type: moduleId === 'hw' ? 'Taller Evaluativo' : 'Teoría y Práctica',
            colab_url: `https://colab.research.google.com/github/${REPO_OWNER}/${REPO_NAME}/blob/${BRANCH}/${encodedPath}`,
            github_url: `https://github.com/${REPO_OWNER}/${REPO_NAME}/blob/${BRANCH}/${encodedPath}`
          });
          newNotebooks++;
        }
      }
    });

    // C. Detectar Datasets (.csv) en data/
    tree.forEach(item => {
      if (item.type === 'blob' && (item.path.endsWith('.csv') || item.path.endsWith('.parquet'))) {
        const pathParts = item.path.split('/');
        const filename = pathParts[pathParts.length - 1];
        
        const exists = cat.datasets.some(d => d.path === item.path || d.name === filename);
        if (!exists) {
          let moduleName = "General";
          const modMatch = item.path.match(/^(\d{2}\s*-\s*[^/]+)/);
          if (modMatch) moduleName = modMatch[1];

          cat.datasets.push({
            name: filename,
            module: moduleName,
            path: item.path,
            rows: 500,
            cols: 5,
            target: "Target Variable",
            features: "Feature_1, Feature_2, Feature_3...",
            description: `Dataset para análisis y entrenamiento en ${moduleName}.`,
            snippet: `df = pd.read_csv('https://raw.githubusercontent.com/${REPO_OWNER}/${REPO_NAME}/${BRANCH}/${encodeURIComponent(item.path).replace(/%2F/g, '/')}')`
          });
          newDatasets++;
        }
      }
    });

    // D. Detectar Guías PDF (.pdf) en Guias/ o docs/Guias/
    tree.forEach(item => {
      if (item.type === 'blob' && item.path.toLowerCase().endsWith('.pdf')) {
        const pathParts = item.path.split('/');
        const filename = pathParts[pathParts.length - 1];

        const exists = cat.guias.some(g => g.filename === filename);
        if (!exists) {
          const sizeKb = Math.round((item.size || 200000) / 1024);
          const sizeStr = sizeKb < 1024 ? `${sizeKb} KB` : `${(sizeKb/1024).toFixed(1)} MB`;
          const cleanTitle = formatTitle(filename);
          const title = cleanTitle.toLowerCase().startsWith('guia') ? cleanTitle : `Guía de ${cleanTitle}`;
          const encodedName = encodeURIComponent(filename);

          cat.guias.push({
            id: `guia_discovered_${cat.guias.length + 1}`,
            filename: filename,
            title: title,
            module: "🐍 Módulo 01: Python",
            size_str: sizeStr,
            path: `Guias/${filename}`,
            raw_url: `https://raw.githubusercontent.com/${REPO_OWNER}/${REPO_NAME}/${BRANCH}/Guias/${encodedName}`,
            lfs_url: `https://media.githubusercontent.com/media/${REPO_OWNER}/${REPO_NAME}/${BRANCH}/docs/Guias/${encodedName}`
          });
          newGuias++;
        }
      }
    });

    // E. Detectar Videos (.mp4, .webm, .mkv, .avi, .mov)
    const videoExts = ['.mp4', '.mkv', '.webm', '.avi', '.mov'];
    tree.forEach(item => {
      const isVid = videoExts.some(ext => item.path.toLowerCase().endsWith(ext));
      if (item.type === 'blob' && isVid) {
        const pathParts = item.path.split('/');
        const filename = pathParts[pathParts.length - 1];

        const exists = cat.videos.some(v => v.filename === filename);
        if (!exists) {
          const sizeMb = ((item.size || 35000000) / (1024 * 1024)).toFixed(1);
          const cleanTitle = formatTitle(filename);
          const encodedName = encodeURIComponent(filename);

          cat.videos.push({
            id: `vid_discovered_${cat.videos.length + 1}`,
            filename: filename,
            title: cleanTitle,
            module: "🐍 Módulo 01: Python",
            size_mb: parseFloat(sizeMb) || 25.0,
            path: `Contenido/${filename}`,
            lfs_url: `https://media.githubusercontent.com/media/${REPO_OWNER}/${REPO_NAME}/${BRANCH}/docs/Contenido/${encodedName}`,
            raw_url: `https://raw.githubusercontent.com/${REPO_OWNER}/${REPO_NAME}/${BRANCH}/docs/Contenido/${encodedName}`,
            github_url: `https://github.com/${REPO_OWNER}/${REPO_NAME}/blob/${BRANCH}/docs/Contenido/${encodedName}`
          });
          newVideos++;
        }
      }
    });

    // Actualizar Estadísticas
    if (cat.stats) {
      cat.stats.total_notebooks = cat.notebooks.length;
      cat.stats.total_modules = cat.modules.filter(m => m.id !== 'hw').length;
      cat.stats.total_datasets = cat.datasets.length;
      cat.stats.total_guias = cat.guias.length;
      cat.stats.total_videos = cat.videos.length;
    }

    // Re-renderizar Componentes de UI
    if (typeof window.updateUiCounts === 'function') window.updateUiCounts();
    if (typeof window.renderPills === 'function') window.renderPills();
    if (typeof window.renderNotebooks === 'function') window.renderNotebooks();
    if (typeof window.renderGuias === 'function') window.renderGuias();
    if (typeof window.renderVideos === 'function') window.renderVideos();
    if (typeof window.renderDatasets === 'function') window.renderDatasets();

    if (showNotification && typeof window.showToast === 'function') {
      const totalNew = newNotebooks + newDatasets + newGuias + newVideos + newModules;
      if (totalNew > 0) {
        window.showToast(`✨ Sincronizado: ${newNotebooks} notebooks, ${newGuias} guías, ${newVideos} videos nuevos`);
      } else {
        window.showToast(`✅ Catálogo actualizado: ${cat.notebooks.length} notebooks, ${cat.guias.length} guías, ${cat.videos.length} videos`);
      }
    }
  }

  function triggerFullSync() {
    sessionStorage.removeItem(CACHE_KEY);
    autoDiscoverRepo(true);
  }

  // Exportar al scope global
  window.autoDiscoverRepo = autoDiscoverRepo;
  window.triggerFullSync = triggerFullSync;
  window.autoDiscoverFiles = autoDiscoverRepo; // Compatibilidad
})();
