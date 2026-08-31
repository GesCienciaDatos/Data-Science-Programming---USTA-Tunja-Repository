/**
 * Real-Time GitHub Repository Multi-Course Auto-Discovery Engine
 * Automatically scans and registers Courses, Modules, Notebooks, Datasets, Guías, and Videos.
 * Next-Gen Multi-Course Virtual Lab - USTA Tunja
 */

(function initAutoDiscoveryEngine() {
  const REPO_OWNER = "sazuniga06";
  const REPO_NAME = "Data-Science-Programming---USTA-Tunja-Repository";
  const BRANCH = "main";
  const CACHE_KEY = "usta_multicourse_catalog_cache";
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

  const KNOWN_TITLES = {
    "Instalacion Python_compressed.mp4": "Instalación y Configuración de Python",
    "Creacion de Venv.mp4": "Creación y Gestión de Entornos Virtuales (VENV)",
    "Creacion_Venv.mp4": "Creación y Gestión de Entornos Virtuales (VENV)",
    "Instalación_Python.pdf": "Guía de Instalación y Configuración de Python",
    "Creacion_VENV.pdf": "Guía de Creación de Entornos Virtuales (VENV)"
  };

  function formatTitle(str) {
    for (const [k, v] of Object.entries(KNOWN_TITLES)) {
      if (k.toLowerCase() === str.toLowerCase()) return v;
    }
    let clean = str
      .replace(/\.[^/.]+$/, '')
      .replace(/^\d+[a-z]?_/, '')
      .replace(/_compressed$/i, '')
      .replace(/[_-]/g, ' ')
      .trim();
    
    // Capitalización de palabras
    const words = clean.split(' ');
    const capitalized = words.map(w => w.length > 2 ? w.charAt(0).toUpperCase() + w.slice(1) : w.toLowerCase()).join(' ');
    return capitalized.charAt(0).toUpperCase() + capitalized.slice(1);
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

  function normalizeKey(str) {
    return (str || '')
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .replace(/[\s_\-\.]+/g, '');
  }

  function findCourseForPath(courses, path) {
    if (!courses || !Array.isArray(courses)) return null;
    const pathLower = path.toLowerCase();
    for (const c of courses) {
      if (c.folder && pathLower.startsWith(c.folder.toLowerCase() + '/')) {
        return c;
      }
    }
    // Fallback: Default to Data Science Programming if path matches modules or first course
    const dsp = courses.find(c => c.id === 'data-science-programming') || courses[0];
    return dsp || null;
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

    // 2. Consultar API de árbol recursivo de GitHub
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
    if (!cat.courses) cat.courses = [];

    let newNotebooks = 0;
    let newDatasets = 0;
    let newGuias = 0;
    let newVideos = 0;
    let newModules = 0;

    // A. Detectar Módulos y Carpetas "XX - Nombre" dentro de los cursos
    tree.forEach(item => {
      if (item.type === 'tree') {
        const parts = item.path.split('/');
        if (parts.length >= 2) {
          const courseFolder = parts[0];
          const moduleFolder = parts[1];
          const match = moduleFolder.match(/^(\d{2})\s*-\s*(.+)$/);
          if (match) {
            const targetCourse = cat.courses.find(c => (c.folder || '').toLowerCase() === courseFolder.toLowerCase());
            if (targetCourse) {
              if (!targetCourse.modules) targetCourse.modules = [];
              const modId = match[1];
              if (!targetCourse.modules.some(m => m.id === modId)) {
                const paletteItem = MODULE_PALETTE[targetCourse.modules.length % MODULE_PALETTE.length];
                targetCourse.modules.push({
                  id: modId,
                  name: moduleFolder,
                  title: formatTitle(match[2]),
                  icon: paletteItem.icon,
                  color: paletteItem.color,
                  description: `Módulo formativo sobre ${formatTitle(match[2])}.`
                });
                newModules++;
              }
            }
          }
        }
      }
    });

    // B. Detectar Cuadernos Jupyter (.ipynb)
    tree.forEach(item => {
      if (item.type === 'blob' && item.path.endsWith('.ipynb') && !item.path.includes('.ipynb_checkpoints')) {
        const pathParts = item.path.split('/');
        const filename = pathParts[pathParts.length - 1];
        
        // Excluir notebooks en carpetas temporales o internas
        if (item.path.startsWith('tmp/') || item.path.startsWith('.gemini/') || item.path.startsWith('.agents/')) return;

        const targetCourse = findCourseForPath(cat.courses, item.path);
        if (!targetCourse) return;
        if (!targetCourse.notebooks) targetCourse.notebooks = [];

        const exists = targetCourse.notebooks.some(n => 
          normalizeKey(n.path) === normalizeKey(item.path) || 
          normalizeKey(n.filename) === normalizeKey(filename)
        );

        if (!exists) {
          let moduleId = "01";
          let moduleName = "01 - Python";

          if (item.path.toLowerCase().includes('/homeworks/')) {
            moduleId = "hw";
            moduleName = "homeworks";
          } else {
            const modMatch = item.path.match(/(\d{2})\s*-\s*[^/]+/);
            if (modMatch) {
              moduleId = modMatch[1];
              const foundMod = (targetCourse.modules || []).find(m => m.id === moduleId);
              if (foundMod) moduleName = foundMod.name;
            }
          }

          const cleanTitle = formatTitle(filename);
          const diff = inferDifficulty(cleanTitle, item.path);
          const encodedPath = encodeURIComponent(item.path).replace(/%2F/g, '/');

          const isDummies = filename.toLowerCase().includes('_dummies');

          targetCourse.notebooks.push({
            id: `${moduleId}_${filename}`,
            module_id: moduleId,
            module_name: moduleName,
            filename: filename,
            title: cleanTitle,
            path: item.path,
            difficulty: isDummies ? "Básico" : diff,
            is_dummies: isDummies,
            edition: isDummies ? "Para Dummies / Para No Ingenieros" : "Estándar / Ingeniería",
            type: moduleId === 'hw' ? 'Taller Evaluativo' : 'Teoría y Práctica',
            colab_url: `https://colab.research.google.com/github/${REPO_OWNER}/${REPO_NAME}/blob/${BRANCH}/${encodedPath}`,
            github_url: `https://github.com/${REPO_OWNER}/${REPO_NAME}/blob/${BRANCH}/${encodedPath}`
          });
          newNotebooks++;
        }
      }
    });

    // C. Detectar Datasets (.csv, .parquet)
    tree.forEach(item => {
      if (item.type === 'blob' && (item.path.endsWith('.csv') || item.path.endsWith('.parquet'))) {
        if (item.path.startsWith('.agents/') || item.path.startsWith('.git/') || item.path.startsWith('docs/')) return;
        const pathParts = item.path.split('/');
        const filename = pathParts[pathParts.length - 1];
        
        const targetCourse = findCourseForPath(cat.courses, item.path);
        if (!targetCourse) return;
        if (!targetCourse.datasets) targetCourse.datasets = [];

        const exists = targetCourse.datasets.some(d => 
          normalizeKey(d.path) === normalizeKey(item.path) || 
          normalizeKey(d.name) === normalizeKey(filename)
        );

        if (!exists) {
          let moduleName = "General";
          const modMatch = item.path.match(/(\d{2}\s*-\s*[^/]+)/);
          if (modMatch) moduleName = modMatch[1];

          targetCourse.datasets.push({
            name: filename,
            module: moduleName,
            path: item.path,
            rows: 500,
            cols: 5,
            target: "Target Variable",
            features: "Feature_1, Feature_2, Feature_3...",
            description: `Dataset para análisis y modelado en ${moduleName}.`,
            snippet: `df = pd.read_csv('https://raw.githubusercontent.com/${REPO_OWNER}/${REPO_NAME}/${BRANCH}/${encodeURIComponent(item.path).replace(/%2F/g, '/')}')`
          });
          newDatasets++;
        }
      }
    });

    // D. Detectar Guías PDF (.pdf)
    tree.forEach(item => {
      if (item.type === 'blob' && item.path.toLowerCase().endsWith('.pdf')) {
        const pathParts = item.path.split('/');
        const filename = pathParts[pathParts.length - 1];

        const targetCourse = findCourseForPath(cat.courses, item.path);
        if (!targetCourse) return;
        if (!targetCourse.guias) targetCourse.guias = [];

        const exists = targetCourse.guias.some(g => 
          normalizeKey(g.filename) === normalizeKey(filename) || 
          normalizeKey(g.path) === normalizeKey(item.path) ||
          normalizeKey(g.title) === normalizeKey(formatTitle(filename))
        );

        if (!exists) {
          const sizeKb = Math.round((item.size || 200000) / 1024);
          const sizeStr = sizeKb < 1024 ? `${sizeKb} KB` : `${(sizeKb/1024).toFixed(1)} MB`;
          const cleanTitle = formatTitle(filename);
          const encodedName = encodeURIComponent(filename);

          targetCourse.guias.push({
            id: `guia_discovered_${targetCourse.guias.length + 1}`,
            filename: filename,
            title: cleanTitle,
            module: "🐍 Módulo 01: Python",
            size_str: sizeStr,
            path: `Guias/${filename}`,
            raw_url: `https://raw.githubusercontent.com/${REPO_OWNER}/${REPO_NAME}/${BRANCH}/${encodeURIComponent(targetCourse.folder || '')}/Guias/${encodedName}`,
            lfs_url: `https://media.githubusercontent.com/media/${REPO_OWNER}/${REPO_NAME}/${BRANCH}/docs/Guias/${encodedName}`
          });
          newGuias++;
        }
      }
    });

    // E. Detectar Videos
    const videoExts = ['.mp4', '.mkv', '.webm', '.avi', '.mov'];
    tree.forEach(item => {
      const isVid = videoExts.some(ext => item.path.toLowerCase().endsWith(ext));
      if (item.type === 'blob' && isVid) {
        const pathParts = item.path.split('/');
        const filename = pathParts[pathParts.length - 1];

        const targetCourse = findCourseForPath(cat.courses, item.path);
        if (!targetCourse) return;
        if (!targetCourse.videos) targetCourse.videos = [];

        const exists = targetCourse.videos.some(v => 
          normalizeKey(v.filename) === normalizeKey(filename) || 
          normalizeKey(v.path) === normalizeKey(item.path) ||
          normalizeKey(v.title) === normalizeKey(formatTitle(filename))
        );

        if (!exists) {
          const sizeMb = ((item.size || 35000000) / (1024 * 1024)).toFixed(1);
          const cleanTitle = formatTitle(filename);
          const encodedName = encodeURIComponent(filename);

          const ytMapping = {
            "instalacion python_compressed.mp4": { id: "4GN9WlumZ7o", url: "https://youtu.be/4GN9WlumZ7o" },
            "instalacion python.mp4": { id: "4GN9WlumZ7o", url: "https://youtu.be/4GN9WlumZ7o" },
            "creacion_venv.mp4": { id: "GX0rf6HjdcU", url: "https://youtu.be/GX0rf6HjdcU" },
            "creacion de venv.mp4": { id: "GX0rf6HjdcU", url: "https://youtu.be/GX0rf6HjdcU" }
          };
          const yt = ytMapping[filename.toLowerCase()] || { id: "", url: "" };

          targetCourse.videos.push({
            id: `vid_discovered_${targetCourse.videos.length + 1}`,
            filename: filename,
            title: cleanTitle,
            module: "🐍 Módulo 01: Python",
            size_mb: parseFloat(sizeMb) || 25.0,
            path: `Contenido/${filename}`,
            youtube_id: yt.id,
            youtube_url: yt.url,
            embed_url: yt.id ? `https://www.youtube.com/embed/${yt.id}` : "",
            thumbnail: yt.id ? `https://img.youtube.com/vi/${yt.id}/hqdefault.jpg` : "",
            lfs_url: `https://media.githubusercontent.com/media/${REPO_OWNER}/${REPO_NAME}/${BRANCH}/docs/Contenido/${encodedName}`,
            raw_url: `https://raw.githubusercontent.com/${REPO_OWNER}/${REPO_NAME}/${BRANCH}/docs/Contenido/${encodedName}`,
            github_url: `https://github.com/${REPO_OWNER}/${REPO_NAME}/blob/${BRANCH}/docs/Contenido/${encodedName}`
          });
          newVideos++;
        }
      }
    });

    // Actualizar Estadísticas por Curso
    cat.courses.forEach(c => {
      c.stats = {
        total_notebooks: (c.notebooks || []).length,
        total_modules: (c.modules || []).filter(m => m.id !== 'hw').length,
        total_homeworks: (c.notebooks || []).filter(n => n.module_id === 'hw').length,
        total_datasets: (c.datasets || []).length,
        total_guias: (c.guias || []).length,
        total_videos: (c.videos || []).length
      };
    });

    // Sincronizar compatibilidad con curso activo
    const activeCourse = cat.courses.find(c => c.id === cat.active_course_id) || cat.courses[0];
    if (activeCourse) {
      cat.modules = activeCourse.modules || [];
      cat.notebooks = activeCourse.notebooks || [];
      cat.datasets = activeCourse.datasets || [];
      cat.guias = activeCourse.guias || [];
      cat.videos = activeCourse.videos || [];
      cat.stats = activeCourse.stats || {};
    }

    // Re-renderizar Componentes de UI
    if (typeof window.renderCourseHub === 'function') window.renderCourseHub();
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
        window.showToast(`✅ Catálogo actualizado: ${cat.notebooks.length} notebooks disponibles`);
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
  window.autoDiscoverFiles = autoDiscoverRepo;
})();
