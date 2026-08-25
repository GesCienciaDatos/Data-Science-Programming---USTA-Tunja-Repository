/**
 * Virtual Data Science Laboratory - Interactive Controller (USTA Tunja)
 */

document.addEventListener('DOMContentLoaded', () => {
  // State
  let activeModuleId = 'all';
  let searchQuery = '';
  let selectedDifficulty = 'all';
  let selectedType = 'all';
  let activeMainTab = 'notebooks'; // 'notebooks' | 'datasets' | 'cheatsheets'

  // DOM Elements
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  const searchInput = document.getElementById('globalSearchInput');
  const tabsWrapper = document.getElementById('moduleTabsWrapper');
  const notebooksGrid = document.getElementById('notebooksGrid');
  const datasetsGrid = document.getElementById('datasetsGrid');
  const difficultyFilter = document.getElementById('difficultyFilter');
  const typeFilter = document.getElementById('typeFilter');
  const resultsCount = document.getElementById('resultsCount');
  const navNotebooksTab = document.getElementById('navNotebooksTab');
  const navDatasetsTab = document.getElementById('navDatasetsTab');
  const navCheatsheetsTab = document.getElementById('navCheatsheetsTab');
  const sectionNotebooks = document.getElementById('sectionNotebooks');
  const sectionDatasets = document.getElementById('sectionDatasets');
  const sectionCheatsheets = document.getElementById('sectionCheatsheets');

  // 1. Theme Management (Dark / Light)
  const savedTheme = localStorage.getItem('usta_lab_theme') || 
    (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  setTheme(savedTheme);

  themeToggleBtn.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    setTheme(newTheme);
  });

  function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('usta_lab_theme', theme);
    themeToggleBtn.innerHTML = theme === 'dark' ? '☀️ Modo Claro' : '🌙 Modo Oscuro';
  }

  // 2. Main Navigation Tabs (Notebooks / Datasets / Cheatsheets)
  function switchMainSection(tabName) {
    activeMainTab = tabName;
    
    // Update active nav styles
    [navNotebooksTab, navDatasetsTab, navCheatsheetsTab].forEach(btn => btn?.classList.remove('active'));
    [sectionNotebooks, sectionDatasets, sectionCheatsheets].forEach(sec => {
      if (sec) sec.style.display = 'none';
    });

    if (tabName === 'notebooks') {
      navNotebooksTab?.classList.add('active');
      if (sectionNotebooks) sectionNotebooks.style.display = 'block';
    } else if (tabName === 'datasets') {
      navDatasetsTab?.classList.add('active');
      if (sectionDatasets) sectionDatasets.style.display = 'block';
      renderDatasets();
    } else if (tabName === 'cheatsheets') {
      navCheatsheetsTab?.classList.add('active');
      if (sectionCheatsheets) sectionCheatsheets.style.display = 'block';
    }
  }

  navNotebooksTab?.addEventListener('click', () => switchMainSection('notebooks'));
  navDatasetsTab?.addEventListener('click', () => switchMainSection('datasets'));
  navCheatsheetsTab?.addEventListener('click', () => switchMainSection('cheatsheets'));

  // 3. Render Module Tabs
  function renderModuleTabs() {
    if (!tabsWrapper) return;
    
    let html = `
      <button class="tab-btn ${activeModuleId === 'all' ? 'active' : ''}" data-module="all">
        🌟 Todos los Módulos
      </button>
    `;

    VIRTUAL_LAB_CATALOG.modules.forEach(mod => {
      const isActive = activeModuleId === mod.id ? 'active' : '';
      html += `
        <button class="tab-btn ${isActive}" data-module="${mod.id}" style="--tab-color: ${mod.color}">
          <span>${mod.icon}</span> ${mod.name}
        </button>
      `;
    });

    tabsWrapper.innerHTML = html;

    // Attach click events
    tabsWrapper.querySelectorAll('.tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        tabsWrapper.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeModuleId = btn.getAttribute('data-module');
        renderNotebooks();
      });
    });
  }

  // 4. Render Notebook Cards
  function renderNotebooks() {
    if (!notebooksGrid) return;

    let filtered = VIRTUAL_LAB_CATALOG.notebooks.filter(nb => {
      // Module filter
      if (activeModuleId !== 'all' && nb.module_id !== activeModuleId) {
        return false;
      }
      // Difficulty filter
      if (selectedDifficulty !== 'all') {
        if (!nb.difficulty.toLowerCase().includes(selectedDifficulty.toLowerCase())) {
          return false;
        }
      }
      // Type filter
      if (selectedType !== 'all' && nb.type !== selectedType) {
        return false;
      }
      // Search query
      if (searchQuery.trim() !== '') {
        const q = searchQuery.toLowerCase();
        const inTitle = nb.title.toLowerCase().includes(q);
        const inPath = nb.path.toLowerCase().includes(q);
        const inModule = nb.module_name.toLowerCase().includes(q);
        if (!inTitle && !inPath && !inModule) return false;
      }
      return true;
    });

    if (resultsCount) {
      resultsCount.textContent = `Mostrando ${filtered.length} de ${VIRTUAL_LAB_CATALOG.notebooks.length} cuadernos`;
    }

    if (filtered.length === 0) {
      notebooksGrid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 3rem; color: var(--text-muted);">
          <p style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔍</p>
          <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-primary);">No se encontraron cuadernos</h3>
          <p style="font-size: 0.9rem;">Prueba con otros términos de búsqueda o selecciona otro módulo.</p>
        </div>
      `;
      return;
    }

    notebooksGrid.innerHTML = filtered.map(nb => {
      const mod = VIRTUAL_LAB_CATALOG.modules.find(m => m.id === nb.module_id) || {};
      const modColor = mod.color || '#3b82f6';
      
      let diffClass = 'diff-intermedio';
      if (nb.difficulty.includes('Básico')) diffClass = 'diff-basico';
      if (nb.difficulty.includes('Avanzado')) diffClass = 'diff-avanzado';

      return `
        <div class="notebook-card" style="--card-accent: ${modColor};">
          <div>
            <div class="card-header">
              <span class="card-module-tag">${nb.module_name}</span>
              <span class="card-difficulty ${diffClass}">${nb.difficulty}</span>
            </div>
            <h3 class="card-title">${nb.title}</h3>
            <p class="card-path">📁 ${nb.path}</p>
          </div>
          <div class="card-actions">
            <a href="${nb.colab_url}" target="_blank" rel="noopener noreferrer" class="btn-action btn-colab" title="Ejecutar en Google Colab">
              🚀 Colab
            </a>
            <a href="${nb.github_url}" target="_blank" rel="noopener noreferrer" class="btn-action btn-github" title="Ver código en GitHub">
              👁️ GitHub
            </a>
          </div>
        </div>
      `;
    }).join('');
  }

  // 5. Render Datasets Catalog
  function renderDatasets() {
    if (!datasetsGrid) return;

    datasetsGrid.innerHTML = VIRTUAL_LAB_CATALOG.datasets.map(ds => {
      return `
        <div class="dataset-card">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.4rem;">
              <h3 style="font-family: var(--font-heading); font-size: 1.2rem; font-weight: 700; color: var(--primary);">
                📊 ${ds.name}
              </h3>
              <span style="font-size: 0.75rem; font-weight: 700; background: var(--bg-tertiary); padding: 0.2rem 0.5rem; border-radius: var(--radius-sm);">
                ${ds.module}
              </span>
            </div>
            <div class="dataset-meta">
              <span class="dataset-meta-badge">📐 ${ds.rows.toLocaleString()} filas</span>
              <span class="dataset-meta-badge">🔢 ${ds.cols} columnas</span>
              <span class="dataset-meta-badge">🎯 Target: ${ds.target}</span>
            </div>
            <p class="dataset-desc">${ds.description}</p>
            <p style="font-size: 0.78rem; color: var(--text-muted); margin-bottom: 0.8rem;">
              <b>Características:</b> ${ds.features}
            </p>
          </div>
          <div>
            <button class="copy-snippet-btn" onclick="copySnippet('${ds.name}', '${ds.snippet}')">
              <span>📋 Copiar pd.read_csv()</span>
              <span style="font-size: 0.9rem;">⚡</span>
            </button>
          </div>
        </div>
      `;
    }).join('');
  }

  // 6. Search & Filters
  searchInput?.addEventListener('input', (e) => {
    searchQuery = e.target.value;
    if (activeMainTab !== 'notebooks') switchMainSection('notebooks');
    renderNotebooks();
  });

  difficultyFilter?.addEventListener('change', (e) => {
    selectedDifficulty = e.target.value;
    renderNotebooks();
  });

  typeFilter?.addEventListener('change', (e) => {
    selectedType = e.target.value;
    renderNotebooks();
  });

  // Global Keyboard Shortcut: '/' or 'Ctrl+K'
  document.addEventListener('keydown', (e) => {
    if (e.key === '/' && document.activeElement !== searchInput) {
      e.preventDefault();
      searchInput?.focus();
    }
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      searchInput?.focus();
    }
  });

  // Init
  renderModuleTabs();
  renderNotebooks();
});

// Helper: Copy Snippet to Clipboard with Toast Notification
window.copySnippet = function(name, snippet) {
  navigator.clipboard.writeText(snippet).then(() => {
    showToast(`Código de carga para ${name} copiado al portapapeles 📋`);
  }).catch(err => {
    console.error('Error al copiar:', err);
  });
};

function showToast(message) {
  let container = document.getElementById('toastContainer');
  if (!container) {
    container = document.createElement('div');
    container.id = 'toastContainer';
    container.className = 'toast-container';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.innerHTML = `<span>✅</span> <span>${message}</span>`;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 3200);
}
