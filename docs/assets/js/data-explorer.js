/**
 * Data Warehouse Explorer Modal & Multi-Framework Export
 * Next-Gen Python Virtual Lab - USTA Tunja
 */

(function initDataExplorerModule() {
  let currentExplorerDataset = null;
  let currentExportFramework = 'pandas';

  const DATASET_SAMPLES = {
    "Advertising.csv": {
      columns: ["TV", "Radio", "Newspaper", "Sales"],
      types: ["float64", "float64", "float64", "float64"],
      rows: [
        [230.1, 37.8, 69.2, 22.1],
        [44.5, 39.3, 45.1, 10.4],
        [17.2, 45.9, 69.3, 9.3],
        [151.5, 41.3, 58.5, 18.5],
        [180.8, 10.8, 58.4, 12.9]
      ],
      problem: "Supervisado (Regresión Lineal)"
    },
    "melb_data.csv": {
      columns: ["Rooms", "Price", "Distance", "Postcode", "Bedroom2"],
      types: ["int64", "float64", "float64", "float64", "float64"],
      rows: [
        [2, 1480000.0, 2.5, 3067.0, 2.0],
        [2, 1035000.0, 2.5, 3067.0, 2.0],
        [3, 1465000.0, 2.5, 3067.0, 3.0],
        [3, 850000.0, 2.5, 3067.0, 3.0],
        [4, 1600000.0, 2.5, 3067.0, 3.0]
      ],
      problem: "Supervisado (Regresión Inmobiliaria)"
    },
    "bikeshare.csv": {
      columns: ["season", "holiday", "workingday", "temp", "count"],
      types: ["int64", "int64", "int64", "float64", "int64"],
      rows: [
        [1, 0, 0, 9.84, 16],
        [1, 0, 0, 9.02, 40],
        [1, 0, 0, 9.02, 32],
        [1, 0, 0, 9.84, 13],
        [1, 0, 0, 9.84, 1]
      ],
      problem: "Supervisado (Regresión y Demanda)"
    },
    "winequality-red.csv": {
      columns: ["fixed acidity", "volatile acidity", "citric acid", "alcohol", "quality"],
      types: ["float64", "float64", "float64", "float64", "int64"],
      rows: [
        [7.4, 0.70, 0.00, 9.4, 5],
        [7.8, 0.88, 0.00, 9.8, 5],
        [7.8, 0.76, 0.04, 9.8, 5],
        [11.2, 0.28, 0.56, 9.8, 6],
        [7.4, 0.70, 0.00, 9.4, 5]
      ],
      problem: "Supervisado (Clasificación / Regresión)"
    }
  };

  function renderDatasets() {
    const container = document.getElementById('datasetsContainer');
    if (!container) return;

    const catalogDatasets = (window.VIRTUAL_LAB_CATALOG && window.VIRTUAL_LAB_CATALOG.datasets) || [];
    
    if (catalogDatasets.length === 0) {
      container.innerHTML = `
        <div class="col-span-full py-12 text-center glass-panel rounded-2xl border border-outline-variant">
          <span class="material-symbols-outlined text-primary text-4xl mb-2">database</span>
          <h3 class="font-headline-md text-on-surface text-base">No hay datasets cargados</h3>
          <p class="text-xs text-on-surface-variant max-w-sm mx-auto mt-1">Usa el botón de auto-descubrimiento para escanear el repositorio.</p>
        </div>
      `;
      return;
    }

    container.innerHTML = catalogDatasets.map(ds => {
      const rawDownloadUrl = `https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/main/${encodeURIComponent(ds.path).replace(/%2F/g, '/')}`;

      return `
        <div class="glass-panel rounded-2xl p-5 border border-outline-variant flex flex-col justify-between group hover:-translate-y-1 transition-all duration-300">
          <div>
            <div class="flex justify-between items-center mb-2">
              <h3 class="font-headline-md text-base text-on-surface flex items-center gap-2 group-hover:text-primary transition-colors">
                <span class="material-symbols-outlined text-primary text-sm">database</span> ${ds.name}
              </h3>
              <span class="text-[10px] font-mono text-primary bg-primary/10 px-2 py-0.5 rounded border border-primary/20">${ds.module || 'Dataset'}</span>
            </div>
            <div class="flex flex-wrap gap-2 text-xs font-mono mb-2 text-on-surface-variant">
              <span>📐 ${(ds.rows || 0).toLocaleString()} filas</span>
              <span>🔢 ${ds.cols || '-'} columnas</span>
              <span class="text-tertiary">🎯 Target: ${ds.target || 'N/A'}</span>
            </div>
            <p class="text-xs text-on-surface-variant leading-relaxed mb-3">${ds.description || 'Dataset de prácticas para análisis y modelado de datos.'}</p>
          </div>
          <div class="pt-3 border-t border-outline-variant flex gap-2">
            <button onclick="openDataExplorer('${ds.name}')" class="flex-1 py-2 px-3 rounded-lg bg-primary/20 text-primary hover:bg-primary/30 text-xs font-label-caps flex items-center justify-center gap-1 shadow-neon-cyan transition-all">
              <span class="material-symbols-outlined text-sm">analytics</span> Explorar Datos
            </button>
            <a href="${rawDownloadUrl}" download="${ds.name}" target="_blank" rel="noopener noreferrer" class="py-2 px-3 rounded-lg bg-surface-container hover:bg-surface-bright text-on-surface text-xs font-label-caps border border-outline-variant flex items-center justify-center gap-1 transition-colors">
              <span class="material-symbols-outlined text-sm">download</span> CSV
            </a>
          </div>
        </div>
      `;
    }).join('');
  }

  function openDataExplorer(datasetName) {
    const catalogDatasets = (window.VIRTUAL_LAB_CATALOG && window.VIRTUAL_LAB_CATALOG.datasets) || [];
    const ds = catalogDatasets.find(d => d.name === datasetName);
    if (!ds) return;

    currentExplorerDataset = ds;
    const modal = document.getElementById('dataExplorerModal');
    const titleEl = document.getElementById('modalDatasetTitle');
    const descEl = document.getElementById('modalDatasetDesc');
    const rowsEl = document.getElementById('modalDatasetRows');
    const colsEl = document.getElementById('modalDatasetCols');
    const targetEl = document.getElementById('modalDatasetTarget');
    const dlBtn = document.getElementById('modalDownloadDirectBtn');
    const tableEl = document.getElementById('modalTablePreview');

    const rawDownloadUrl = `https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/main/${encodeURIComponent(ds.path).replace(/%2F/g, '/')}`;

    if (titleEl) titleEl.textContent = ds.name;
    if (descEl) descEl.textContent = ds.description || 'Dataset exploratorio';
    if (rowsEl) rowsEl.textContent = (ds.rows || 0).toLocaleString();
    if (colsEl) colsEl.textContent = ds.cols || '-';
    if (targetEl) targetEl.textContent = ds.target || 'N/A';
    if (dlBtn) dlBtn.href = rawDownloadUrl;

    const sample = DATASET_SAMPLES[ds.name] || {
      columns: (ds.features || "Col1, Col2, Col3, Target").split(',').map(s => s.trim()).slice(0, 4).concat([ds.target || 'Target']),
      types: ["float64", "float64", "int64", "object", "float64"],
      rows: [
        [12.4, 45.1, 102, "Clase A", 0.88],
        [15.8, 38.9, 108, "Clase B", 0.74],
        [22.1, 51.3, 115, "Clase A", 0.95],
        [18.7, 42.0, 110, "Clase C", 0.81],
        [14.2, 36.5, 104, "Clase B", 0.69]
      ],
      problem: "Supervisado"
    };

    const problemEl = document.getElementById('modalDatasetType');
    if (problemEl) problemEl.textContent = sample.problem || "Supervisado";

    let tableHtml = `
      <thead>
        <tr class="bg-surface-container border-b border-outline-variant">
          ${sample.columns.map((c, i) => `
            <th class="p-2.5 text-on-surface font-semibold">
              <div>${c}</div>
              <span class="text-[9px] text-primary font-normal">${sample.types[i] || 'float64'}</span>
            </th>
          `).join('')}
        </tr>
      </thead>
      <tbody class="divide-y divide-outline-variant/40">
        ${sample.rows.map(r => `
          <tr class="hover:bg-surface-container/50 transition-colors">
            ${r.map(val => `<td class="p-2.5 text-on-surface-variant">${val}</td>`).join('')}
          </tr>
        `).join('')}
      </tbody>
    `;

    if (tableEl) tableEl.innerHTML = tableHtml;
    setExportFramework('pandas');

    if (modal) {
      modal.classList.remove('hidden');
      modal.classList.add('flex');
    }
  }

  function closeDataExplorer() {
    const modal = document.getElementById('dataExplorerModal');
    if (modal) {
      modal.classList.remove('flex');
      modal.classList.add('hidden');
    }
  }

  function setExportFramework(fw) {
    currentExportFramework = fw;
    const display = document.getElementById('modalExportCodeDisplay');
    if (!currentExplorerDataset) return;

    const rawUrl = `https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/main/${encodeURIComponent(currentExplorerDataset.path).replace(/%2F/g, '/')}`;

    let code = `import pandas as pd\ndf = pd.read_csv("${rawUrl}")`;
    if (fw === 'polars') code = `import polars as pl\ndf = pl.read_csv("${rawUrl}")`;
    if (fw === 'duckdb') code = `import duckdb\nrel = duckdb.read_csv("${rawUrl}")`;
    if (fw === 'pyspark') code = `from pyspark.sql import SparkSession\nspark = SparkSession.builder.getOrCreate()\ndf = spark.read.csv("${rawUrl}", header=True, inferSchema=True)`;

    if (display) display.textContent = code;

    ['pandas', 'polars', 'duckdb', 'pyspark'].forEach(k => {
      const btn = document.getElementById(`tab-exp-${k}`);
      if (!btn) return;
      if (k === fw) {
        btn.className = 'px-2 py-0.5 rounded text-[10px] font-mono bg-primary/20 text-primary border border-primary/30';
      } else {
        btn.className = 'px-2 py-0.5 rounded text-[10px] font-mono text-on-surface-variant hover:text-on-surface';
      }
    });
  }

  function copyExportedCode() {
    const display = document.getElementById('modalExportCodeDisplay');
    if (display && display.textContent) {
      navigator.clipboard.writeText(display.textContent).then(() => {
        if (typeof window.showToast === 'function') {
          window.showToast(`Snippet de ${currentExportFramework.toUpperCase()} copiado 📋`);
        }
      });
    }
  }

  // Exportar al scope global
  window.renderDatasets = renderDatasets;
  window.openDataExplorer = openDataExplorer;
  window.closeDataExplorer = closeDataExplorer;
  window.setExportFramework = setExportFramework;
  window.copyExportedCode = copyExportedCode;
})();
