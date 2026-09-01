<script setup>
import { ref } from 'vue';

const emit = defineEmits(['explore-course', 'open-datasets']);

const activeSnippetKey = ref('cv');
const isExecuting = ref(false);
const executionOutput = ref('R² Promedio 5-Fold CV: 0.8871 (Modelo Validado con Cero Data Leakage)');

const snippets = {
  cv: {
    code: `<div class="code-line"><span class="text-brand-amber">import</span> numpy as np, pandas as pd</div>
<div class="code-line"><span class="text-brand-amber">from</span> sklearn.model_selection <span class="text-brand-amber">import</span> cross_val_score</div>
<div class="code-line"><span class="text-brand-amber">from</span> sklearn.ensemble <span class="text-brand-amber">import</span> RandomForestRegressor</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-slate-500"># Validación Cruzada 5-Fold Estratificada</span></div>
<div class="code-line">model = RandomForestRegressor(n_estimators=<span class="text-brand-cyan">150</span>, max_depth=<span class="text-brand-cyan">12</span>, random_state=<span class="text-brand-cyan">42</span>)</div>
<div class="code-line">scores = cross_val_score(model, X_train, y_train, cv=<span class="text-brand-cyan">5</span>, scoring=<span class="text-emerald-400">'r2'</span>)</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-brand-amber">print</span>(<span class="text-emerald-400">f"R² Promedio 5-Fold CV: {scores.mean():.4f}"</span>)</div>`,
    output: 'R² Promedio 5-Fold CV: 0.8871 (Modelo Validado con Cero Data Leakage)'
  },
  eda: {
    code: `<div class="code-line"><span class="text-brand-amber">import</span> pandas as pd</div>
<div class="code-line"><span class="text-slate-500"># Diagnóstico Estadístico Inicial & Matriz de Nulos</span></div>
<div class="code-line">df = pd.read_csv(<span class="text-emerald-400">"melb_data.csv"</span>)</div>
<div class="code-line">missing = df.isnull().sum()[df.isnull().sum() &gt; <span class="text-brand-cyan">0</span>]</div>
<div class="code-line">stats = df[[<span class="text-emerald-400">'Rooms'</span>, <span class="text-emerald-400">'Price'</span>, <span class="text-emerald-400">'Distance'</span>]].describe().T</div>
<div class="code-line"><span class="text-brand-amber">print</span>(<span class="text-emerald-400">f"Registros: {len(df):,} | Nulos: {len(missing)}"</span>)</div>`,
    output: 'Registros: 13,580 | Nulos detectados: 3 | Diagnóstico Completado'
  },
  fe: {
    code: `<div class="code-line"><span class="text-brand-amber">import</span> numpy as np, pandas as pd</div>
<div class="code-line"><span class="text-slate-500"># Target Encoding con Suavizado Bayesiano m-estimate</span></div>
<div class="code-line"><span class="text-brand-amber">def</span> <span class="text-brand-cyan">calc_smooth_target</span>(df, cat_col, target_col, weight=<span class="text-brand-cyan">10</span>):</div>
<div class="code-line">    global_mean = df[target_col].mean()</div>
<div class="code-line">    counts = df.groupby(cat_col)[target_col].count()</div>
<div class="code-line">    means = df.groupby(cat_col)[target_col].mean()</div>
<div class="code-line">    smooth = (counts * means + weight * global_mean) / (counts + weight)</div>
<div class="code-line">    <span class="text-brand-amber">return</span> df[cat_col].map(smooth)</div>`,
    output: 'Target Encoding Regularizado: Reducción de Varianza y Prevención de Overfitting'
  }
};

function selectSnippet(key) {
  activeSnippetKey.value = key;
  executionOutput.value = snippets[key].output;
}

function runSimulation() {
  isExecuting.value = true;
  executionOutput.value = 'Ejecutando kernel en entorno aislado...';
  setTimeout(() => {
    isExecuting.value = false;
    executionOutput.value = snippets[activeSnippetKey.value].output;
  }, 350);
}
</script>

<template>
  <section class="pt-8 pb-6 px-4 sm:px-8 max-w-container mx-auto">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
      
      <!-- Left Column: Academic Manifesto & Metrics -->
      <div class="lg:col-span-7 space-y-6">
        
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-100 dark:bg-space-900 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 font-mono text-xs">
          <span class="w-1.5 h-1.5 rounded-full bg-brand-cyan"></span>
          <span>Especialización en Ciencia de Datos • Posgrados USTA Tunja</span>
        </div>

        <div class="space-y-2">
          <h1 class="text-3xl sm:text-4xl lg:text-5xl font-semibold tracking-tight text-slate-900 dark:text-slate-50 leading-[1.15]">
            Ecosistema de Laboratorios <br/>
            <span class="text-slate-500 dark:text-slate-400 font-normal">Computacionales & Analítica</span>
          </h1>
          <p class="text-sm sm:text-base text-slate-600 dark:text-slate-400 max-w-2xl leading-relaxed">
            Entorno académico integral para la investigación y experimentación avanzada. Acceso estructurado a 144 cuadernos pedagógicos con rigor matemático, datasets reales y ejecución en la nube.
          </p>
        </div>

        <!-- Action CTAs -->
        <div class="flex flex-wrap items-center gap-3 pt-1">
          <button 
            @click="emit('explore-course', 'data-science-programming')"
            class="px-5 py-2.5 rounded-md bg-slate-900 dark:bg-slate-100 hover:bg-slate-800 dark:hover:bg-white text-white dark:text-slate-950 font-mono text-xs font-semibold flex items-center gap-2 transition-all shadow-sm"
          >
            <span>INGRESAR A PROGRAMACIÓN PARA CIENCIA DE DATOS</span>
            <span class="material-symbols-outlined text-sm">arrow_forward</span>
          </button>
          
          <button 
            @click="emit('open-datasets')"
            class="px-4 py-2.5 rounded-md bg-transparent hover:bg-slate-100 dark:hover:bg-space-900 border border-slate-300 dark:border-slate-800 text-slate-700 dark:text-slate-300 font-mono text-xs transition-all flex items-center gap-2"
          >
            <span class="material-symbols-outlined text-sm text-brand-cyan">database</span>
            <span>EXPLORAR DATASETS</span>
          </button>
        </div>

        <!-- Metric Counters (Executive 4-Column Grid) -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-6 border-t border-slate-200 dark:border-slate-800/80">
          <div class="glass-card rounded-lg p-3.5 border text-center sm:text-left">
            <span class="block font-mono text-[10px] text-slate-500 dark:text-slate-400 uppercase tracking-wider">Cuadernos</span>
            <span class="font-mono text-xl font-semibold text-slate-900 dark:text-brand-cyan">144</span>
          </div>
          <div class="glass-card rounded-lg p-3.5 border text-center sm:text-left">
            <span class="block font-mono text-[10px] text-slate-500 dark:text-slate-400 uppercase tracking-wider">Módulos DSP</span>
            <span class="font-mono text-xl font-semibold text-slate-900 dark:text-brand-amber">10</span>
          </div>
          <div class="glass-card rounded-lg p-3.5 border text-center sm:text-left">
            <span class="block font-mono text-[10px] text-slate-500 dark:text-slate-400 uppercase tracking-wider">Asignaturas</span>
            <span class="font-mono text-xl font-semibold text-slate-900 dark:text-slate-100">9</span>
          </div>
          <div class="glass-card rounded-lg p-3.5 border text-center sm:text-left">
            <span class="block font-mono text-[10px] text-slate-500 dark:text-slate-400 uppercase tracking-wider">Plataforma</span>
            <span class="font-mono text-xl font-semibold text-emerald-600 dark:text-brand-emerald">100% Cloud</span>
          </div>
        </div>

      </div>

      <!-- Right Column: Interactive Code Sandbox -->
      <div class="lg:col-span-5">
        <div class="glass-card rounded-xl border border-slate-200 dark:border-slate-800 overflow-hidden shadow-sm">
          
          <!-- Sandbox Header Bar -->
          <div class="px-4 py-2.5 bg-slate-100/90 dark:bg-space-900/90 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between">
            <div class="flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-slate-300 dark:bg-slate-700"></span>
              <span class="w-2.5 h-2.5 rounded-full bg-slate-300 dark:bg-slate-700"></span>
              <span class="w-2.5 h-2.5 rounded-full bg-slate-300 dark:bg-slate-700"></span>
              <span class="font-mono text-[11px] text-slate-600 dark:text-slate-400 ml-1.5">sandbox_interactive.py</span>
            </div>
            
            <div class="flex items-center gap-1 font-mono text-[10px]">
              <button 
                @click="selectSnippet('cv')"
                class="px-2 py-0.5 rounded transition-colors"
                :class="activeSnippetKey === 'cv' ? 'bg-brand-cyan/15 text-brand-cyan font-semibold' : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-200'"
              >
                CV
              </button>
              <button 
                @click="selectSnippet('eda')"
                class="px-2 py-0.5 rounded transition-colors"
                :class="activeSnippetKey === 'eda' ? 'bg-brand-cyan/15 text-brand-cyan font-semibold' : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-200'"
              >
                EDA
              </button>
              <button 
                @click="selectSnippet('fe')"
                class="px-2 py-0.5 rounded transition-colors"
                :class="activeSnippetKey === 'fe' ? 'bg-brand-cyan/15 text-brand-cyan font-semibold' : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-200'"
              >
                FE
              </button>
            </div>
          </div>

          <!-- Code Display Body -->
          <div class="p-4 bg-slate-50 dark:bg-space-950 font-mono text-xs text-slate-800 dark:text-slate-200 overflow-x-auto min-h-[175px]">
            <div class="code-container space-y-1" v-html="snippets[activeSnippetKey].code"></div>
          </div>

          <!-- Sandbox Execution Footer -->
          <div class="px-4 py-2.5 bg-slate-100/90 dark:bg-space-900/90 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between gap-3">
            <span class="font-mono text-[11px] text-emerald-600 dark:text-emerald-400 truncate">
              {{ executionOutput }}
            </span>
            <button 
              @click="runSimulation" 
              :disabled="isExecuting"
              class="px-2.5 py-1 rounded bg-slate-900 dark:bg-slate-100 hover:bg-slate-800 dark:hover:bg-white text-white dark:text-slate-950 font-mono text-[11px] font-semibold flex items-center gap-1 shrink-0 transition-all disabled:opacity-50"
            >
              <span class="material-symbols-outlined text-xs">play_arrow</span>
              <span>RUN</span>
            </button>
          </div>

        </div>
      </div>

    </div>
  </section>
</template>
