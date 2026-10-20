<script setup>
import { ref, computed, watch } from 'vue';
import { useI18n } from '../i18n/index.js';

const props = defineProps({
  courses: {
    type: Array,
    default: () => []
  },
  totalBooks: {
    type: Number,
    default: 122
  }
});

const emit = defineEmits(['open-datasets', 'open-books']);

const { currentLang, t } = useI18n();

const activeSnippetKey = ref('ml');
const isExecuting = ref(false);

// Dynamic metric aggregations across the entire academic ecosystem
const totalNotebooks = computed(() => {
  if (!props.courses || props.courses.length === 0) return 440;
  return props.courses.reduce((acc, c) => acc + (c.notebooks?.length || c.stats?.total_notebooks || 0), 0);
});

const totalModules = computed(() => {
  if (!props.courses || props.courses.length === 0) return 47;
  return props.courses.reduce((acc, c) => acc + (c.modules?.length || 0), 0);
});

const totalCourses = computed(() => {
  return props.courses?.length || 9;
});

// Interactive Multi-Subject Code Showcase (Bilingual)
const localizedSnippets = computed(() => {
  const isEn = currentLang.value === 'en';
  return {
    ml: {
      title: isEn ? 'Supervised Machine Learning' : 'Machine Learning Supervisado',
      code: isEn
        ? `<div class="code-line"><span class="text-brand-amber">import</span> numpy as np, pandas as pd</div>
<div class="code-line"><span class="text-brand-amber">from</span> sklearn.model_selection <span class="text-brand-amber">import</span> cross_val_score</div>
<div class="code-line"><span class="text-brand-amber">from</span> sklearn.ensemble <span class="text-brand-amber">import</span> RandomForestRegressor</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-slate-500"># Stratified 5-Fold Cross Validation</span></div>
<div class="code-line">model = RandomForestRegressor(n_estimators=<span class="text-brand-cyan">150</span>, max_depth=<span class="text-brand-cyan">12</span>, random_state=<span class="text-brand-cyan">42</span>)</div>
<div class="code-line">scores = cross_val_score(model, X_train, y_train, cv=<span class="text-brand-cyan">5</span>, scoring=<span class="text-emerald-400">'r2'</span>)</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-brand-amber">print</span>(<span class="text-emerald-400">f"Average 5-Fold CV R²: {scores.mean():.4f}"</span>)</div>`
        : `<div class="code-line"><span class="text-brand-amber">import</span> numpy as np, pandas as pd</div>
<div class="code-line"><span class="text-brand-amber">from</span> sklearn.model_selection <span class="text-brand-amber">import</span> cross_val_score</div>
<div class="code-line"><span class="text-brand-amber">from</span> sklearn.ensemble <span class="text-brand-amber">import</span> RandomForestRegressor</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-slate-500"># Validación Cruzada 5-Fold Estratificada</span></div>
<div class="code-line">model = RandomForestRegressor(n_estimators=<span class="text-brand-cyan">150</span>, max_depth=<span class="text-brand-cyan">12</span>, random_state=<span class="text-brand-cyan">42</span>)</div>
<div class="code-line">scores = cross_val_score(model, X_train, y_train, cv=<span class="text-brand-cyan">5</span>, scoring=<span class="text-emerald-400">'r2'</span>)</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-brand-amber">print</span>(<span class="text-emerald-400">f"R² Promedio 5-Fold CV: {scores.mean():.4f}"</span>)</div>`,
      output: isEn
        ? 'Average 5-Fold CV R²: 0.8871 (Model Validated with Zero Data Leakage)'
        : 'R² Promedio 5-Fold CV: 0.8871 (Modelo Validado con Cero Data Leakage)'
    },
    mining: {
      title: 'Data Mining & Clustering',
      code: isEn
        ? `<div class="code-line"><span class="text-brand-amber">from</span> sklearn.cluster <span class="text-brand-amber">import</span> KMeans</div>
<div class="code-line"><span class="text-brand-amber">from</span> sklearn.metrics <span class="text-brand-amber">import</span> silhouette_score</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-slate-500"># K-Means Clustering & Cohesion / Separation Validation</span></div>
<div class="code-line">kmeans = KMeans(n_clusters=<span class="text-brand-cyan">3</span>, n_init=<span class="text-brand-cyan">10</span>, random_state=<span class="text-brand-cyan">42</span>)</div>
<div class="code-line">clusters = kmeans.fit_predict(X_scaled)</div>
<div class="code-line">sil = silhouette_score(X_scaled, clusters)</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-brand-amber">print</span>(<span class="text-emerald-400">f"K-Means: k=3 | Silhouette Score: {sil:.4f}"</span>)</div>`
        : `<div class="code-line"><span class="text-brand-amber">from</span> sklearn.cluster <span class="text-brand-amber">import</span> KMeans</div>
<div class="code-line"><span class="text-brand-amber">from</span> sklearn.metrics <span class="text-brand-amber">import</span> silhouette_score</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-slate-500"># Clustering K-Means y Validación de Cohesión / Separación</span></div>
<div class="code-line">kmeans = KMeans(n_clusters=<span class="text-brand-cyan">3</span>, n_init=<span class="text-brand-cyan">10</span>, random_state=<span class="text-brand-cyan">42</span>)</div>
<div class="code-line">clusters = kmeans.fit_predict(X_scaled)</div>
<div class="code-line">sil = silhouette_score(X_scaled, clusters)</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-brand-amber">print</span>(<span class="text-emerald-400">f"K-Means: k=3 | Silhouette Score: {sil:.4f}"</span>)</div>`,
      output: isEn
        ? 'K-Means: k=3 | Silhouette Score: 0.6842 | Optimal Clusters Identified'
        : 'K-Means: k=3 | Silhouette Score: 0.6842 | Clusters Óptimos Identificados'
    },
    ia: {
      title: isEn ? 'Artificial Intelligence & A* Search' : 'Inteligencia Artificial & Búsqueda A*',
      code: isEn
        ? `<div class="code-line"><span class="text-brand-amber">from</span> logic <span class="text-brand-amber">import</span> Symbol, And, Or, Not, model_check</div>
<div class="code-line"><span class="text-brand-amber">from</span> search <span class="text-brand-amber">import</span> astar_search, PriorityQueue</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-slate-500"># Propositional Logic Inference & Heuristic A* Search</span></div>
<div class="code-line">kb = And(Or(Symbol(<span class="text-emerald-400">"rain"</span>), Symbol(<span class="text-emerald-400">"traffic"</span>)), Not(Symbol(<span class="text-emerald-400">"accident"</span>)))</div>
<div class="code-line">path = astar_search(start, goal, heuristic=dist_manhattan)</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-brand-amber">print</span>(<span class="text-emerald-400">f"Valid Inference: {model_check(kb, Symbol('rain'))} | A* Cost: 14.2"</span>)</div>`
        : `<div class="code-line"><span class="text-brand-amber">from</span> logic <span class="text-brand-amber">import</span> Symbol, And, Or, Not, model_check</div>
<div class="code-line"><span class="text-brand-amber">from</span> search <span class="text-brand-amber">import</span> astar_search, PriorityQueue</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-slate-500"># Inferencia Lógica Proposicional & Búsqueda Heurística A*</span></div>
<div class="code-line">kb = And(Or(Symbol(<span class="text-emerald-400">"lluvia"</span>), Symbol(<span class="text-emerald-400">"trafico"</span>)), Not(Symbol(<span class="text-emerald-400">"accidente"</span>)))</div>
<div class="code-line">camino = astar_search(origen, destino, heuristica=dist_manhattan)</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-brand-amber">print</span>(<span class="text-emerald-400">f"Inferencia Válida: {model_check(kb, Symbol('lluvia'))} | A* Costo: 14.2"</span>)</div>`,
      output: isEn
        ? 'Valid Inference: True | A* Optimal Cost: 14.2 (6 states expanded)'
        : 'Inferencia Válida: True | A* Costo Óptimo: 14.2 (6 estados expandidos)'
    },
    bigdata: {
      title: isEn ? 'Big Data & Distributed Computing' : 'Big Data & Computación Distribuida',
      code: isEn
        ? `<div class="code-line"><span class="text-brand-amber">from</span> pyspark.sql <span class="text-brand-amber">import</span> SparkSession</div>
<div class="code-line"><span class="text-brand-amber">from</span> pyspark.sql <span class="text-brand-amber">import</span> functions <span class="text-brand-amber">as</span> F</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-slate-500"># SparkSession & Real-time Stream Aggregation</span></div>
<div class="code-line">spark = SparkSession.builder.appName(<span class="text-emerald-400">"StreamingAnalytics"</span>).getOrCreate()</div>
<div class="code-line">df = spark.readStream.schema(schema).csv(<span class="text-emerald-400">"data/stream_logs/"</span>)</div>
<div class="code-line">summary = df.groupBy(<span class="text-emerald-400">"device_type"</span>).count()</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-brand-amber">print</span>(<span class="text-emerald-400">"Active Spark Engine: Micro-Batch Processing ready"</span>)</div>`
        : `<div class="code-line"><span class="text-brand-amber">from</span> pyspark.sql <span class="text-brand-amber">import</span> SparkSession</div>
<div class="code-line"><span class="text-brand-amber">from</span> pyspark.sql <span class="text-brand-amber">import</span> functions <span class="text-brand-amber">as</span> F</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-slate-500"># SparkSession & Agregación en Flujo Streaming</span></div>
<div class="code-line">spark = SparkSession.builder.appName(<span class="text-emerald-400">"StreamingAnalytics"</span>).getOrCreate()</div>
<div class="code-line">df = spark.readStream.schema(schema).csv(<span class="text-emerald-400">"data/stream_logs/"</span>)</div>
<div class="code-line">resumen = df.groupBy(<span class="text-emerald-400">"tipo_dispositivo"</span>).count()</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-brand-amber">print</span>(<span class="text-emerald-400">"Motor Spark Activo: Procesamiento en Micro-Lotes listo"</span>)</div>`,
      output: isEn
        ? 'Active Spark Engine: Micro-Batch Processing ready (0.012s latency)'
        : 'Motor Spark Activo: Procesamiento en Micro-Lotes listo (0.012s de latencia)'
    },
    va: {
      title: isEn ? 'Visual Analytics & Interactive Dashboards' : 'Visual Analytics & Dashboards Interactivos',
      code: isEn
        ? `<div class="code-line"><span class="text-brand-amber">import</span> plotly.express as px, pandas as pd</div>
<div class="code-line"><span class="text-brand-amber">import</span> seaborn as sns, matplotlib.pyplot as plt</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-slate-500"># Multidimensional Visualization & Perceptual Channels</span></div>
<div class="code-line">fig = px.scatter(df, x=<span class="text-emerald-400">"sales"</span>, y=<span class="text-emerald-400">"margin"</span>, color=<span class="text-emerald-400">"segment"</span>, size=<span class="text-emerald-400">"volume"</span>)</div>
<div class="code-line">fig.update_layout(template=<span class="text-emerald-400">"plotly_dark"</span>, hovermode=<span class="text-emerald-400">"closest"</span>)</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-brand-amber">print</span>(<span class="text-emerald-400">"Visual Analytics: 4 perceptual channels integrated"</span>)</div>`
        : `<div class="code-line"><span class="text-brand-amber">import</span> plotly.express as px, pandas as pd</div>
<div class="code-line"><span class="text-brand-amber">import</span> seaborn as sns, matplotlib.pyplot as plt</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-slate-500"># Visualización Multidimensional & Canales Perceptuales</span></div>
<div class="code-line">fig = px.scatter(df, x=<span class="text-emerald-400">"ventas"</span>, y=<span class="text-emerald-400">"margen"</span>, color=<span class="text-emerald-400">"segmento"</span>, size=<span class="text-emerald-400">"volumen"</span>)</div>
<div class="code-line">fig.update_layout(template=<span class="text-emerald-400">"plotly_dark"</span>, hovermode=<span class="text-emerald-400">"closest"</span>)</div>
<div class="code-line"></div>
<div class="code-line"><span class="text-brand-amber">print</span>(<span class="text-emerald-400">"Analítica Visual: 4 canales perceptuales integrados"</span>)</div>`,
      output: isEn
        ? 'Visual Analytics: 4 perceptual channels integrated (x, y, color, size)'
        : 'Analítica Visual: 4 canales perceptuales integrados (x, y, color, tamaño)'
    }
  };
});

const executionOutput = ref(localizedSnippets.value.ml.output);

watch([currentLang, activeSnippetKey], () => {
  executionOutput.value = localizedSnippets.value[activeSnippetKey.value].output;
});

function selectSnippet(key) {
  activeSnippetKey.value = key;
  executionOutput.value = localizedSnippets.value[key].output;
}

function runSimulation() {
  isExecuting.value = true;
  executionOutput.value = t('hero.sandboxRunning');
  setTimeout(() => {
    isExecuting.value = false;
    executionOutput.value = localizedSnippets.value[activeSnippetKey.value].output;
  }, 350);
}

function scrollToDirectory() {
  const el = document.getElementById('plan-de-estudios');
  if (el) {
    el.scrollIntoView({ behavior: 'smooth' });
  }
}
</script>

<template>
  <section class="pt-8 pb-6 px-4 sm:px-8 max-w-container mx-auto">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
      
      <!-- Left Column: Academic Manifesto & General Metrics -->
      <div class="lg:col-span-7 space-y-6">
        
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-100 dark:bg-space-900 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 font-mono text-xs">
          <span class="w-1.5 h-1.5 rounded-full bg-brand-cyan"></span>
          <span>{{ t('hero.badge') }}</span>
        </div>

        <div class="space-y-2">
          <h1 class="text-3xl sm:text-4xl lg:text-5xl font-semibold tracking-tight text-slate-900 dark:text-slate-50 leading-[1.15]">
            {{ t('hero.titlePart1') }} <br/>
            <span class="text-slate-500 dark:text-slate-400 font-normal">{{ t('hero.titlePart2') }}</span>
          </h1>
          <p class="text-sm sm:text-base text-slate-600 dark:text-slate-400 max-w-2xl leading-relaxed">
            {{ t('hero.lead') }}
          </p>
        </div>

        <!-- Action CTAs (General & Accessible) -->
        <div class="flex flex-wrap items-center gap-3 pt-1">
          <button 
            @click="scrollToDirectory"
            class="px-5 py-2.5 rounded-md bg-slate-900 dark:bg-slate-100 hover:bg-slate-800 dark:hover:bg-white text-white dark:text-slate-950 font-mono text-xs font-semibold flex items-center gap-2 transition-all shadow-sm group cursor-pointer"
          >
            <span>{{ t('hero.ctaExplore') }}</span>
            <span class="material-symbols-outlined text-sm transition-transform group-hover:translate-y-0.5">arrow_downward</span>
          </button>
          
          <button 
            @click="emit('open-books')"
            class="px-4 py-2.5 rounded-md bg-transparent hover:bg-slate-100 dark:hover:bg-space-900 border border-brand-amber/40 dark:border-brand-amber/30 text-amber-600 dark:text-brand-amber font-mono text-xs transition-all flex items-center gap-2 cursor-pointer"
          >
            <span class="material-symbols-outlined text-sm text-brand-amber">menu_book</span>
            <span>{{ t('hero.ctaLibrary') }} ({{ totalBooks }})</span>
          </button>

          <button 
            @click="emit('open-datasets')"
            class="px-4 py-2.5 rounded-md bg-transparent hover:bg-slate-100 dark:hover:bg-space-900 border border-slate-300 dark:border-slate-800 text-slate-700 dark:text-slate-300 font-mono text-xs transition-all flex items-center gap-2 cursor-pointer"
          >
            <span class="material-symbols-outlined text-sm text-brand-cyan">database</span>
            <span>{{ t('hero.ctaDatasets') }}</span>
          </button>
        </div>

        <!-- Metric Counters (General Specialization Metrics) -->
        <div class="grid grid-cols-2 sm:grid-cols-5 gap-3 pt-6 border-t border-slate-200 dark:border-slate-800/80">
          <div class="glass-card rounded-lg p-3.5 border text-center sm:text-left">
            <span class="block font-mono text-[10px] text-slate-500 dark:text-slate-400 uppercase tracking-wider">{{ t('hero.metricNotebooks') }}</span>
            <span class="font-mono text-xl font-semibold text-slate-900 dark:text-brand-cyan">{{ totalNotebooks }}</span>
          </div>
          <div class="glass-card rounded-lg p-3.5 border text-center sm:text-left">
            <span class="block font-mono text-[10px] text-slate-500 dark:text-slate-400 uppercase tracking-wider">{{ t('hero.metricBooks') }}</span>
            <span class="font-mono text-xl font-semibold text-amber-600 dark:text-brand-amber">{{ totalBooks }}</span>
          </div>
          <div class="glass-card rounded-lg p-3.5 border text-center sm:text-left">
            <span class="block font-mono text-[10px] text-slate-500 dark:text-slate-400 uppercase tracking-wider">{{ t('hero.metricModules') }}</span>
            <span class="font-mono text-xl font-semibold text-slate-900 dark:text-brand-amber">{{ totalModules }}</span>
          </div>
          <div class="glass-card rounded-lg p-3.5 border text-center sm:text-left">
            <span class="block font-mono text-[10px] text-slate-500 dark:text-slate-400 uppercase tracking-wider">{{ t('hero.metricCurriculum') }}</span>
            <span class="font-mono text-xl font-semibold text-slate-900 dark:text-slate-100">{{ totalCourses }} {{ t('hero.metricCoursesSuffix') }}</span>
          </div>
          <div class="glass-card rounded-lg p-3.5 border text-center sm:text-left col-span-2 sm:col-span-1">
            <span class="block font-mono text-[10px] text-slate-500 dark:text-slate-400 uppercase tracking-wider">{{ t('hero.metricPlatform') }}</span>
            <span class="font-mono text-xl font-semibold text-emerald-600 dark:text-brand-emerald">{{ t('hero.metricCloud') }}</span>
          </div>
        </div>

      </div>

      <!-- Right Column: Multi-Discipline Code Sandbox -->
      <div class="lg:col-span-5">
        <div class="glass-card rounded-xl border border-slate-200 dark:border-slate-800 overflow-hidden shadow-sm">
          
          <!-- Sandbox Header Bar -->
          <div class="px-4 py-2.5 bg-slate-100/90 dark:bg-space-900/90 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between">
            <div class="flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-slate-300 dark:bg-slate-700"></span>
              <span class="w-2.5 h-2.5 rounded-full bg-slate-300 dark:bg-slate-700"></span>
              <span class="w-2.5 h-2.5 rounded-full bg-slate-300 dark:bg-slate-700"></span>
              <span class="font-mono text-[11px] text-slate-600 dark:text-slate-400 ml-1.5">{{ t('hero.sandboxFilename') }}</span>
            </div>
            
            <div class="flex items-center gap-1 font-mono text-[10px]">
              <button 
                @click="selectSnippet('ml')"
                class="px-2 py-0.5 rounded transition-colors cursor-pointer"
                :class="activeSnippetKey === 'ml' ? 'bg-brand-cyan/15 text-brand-cyan font-semibold' : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-200'"
                :title="localizedSnippets.ml.title"
              >
                ML
              </button>
              <button 
                @click="selectSnippet('mining')"
                class="px-2 py-0.5 rounded transition-colors cursor-pointer"
                :class="activeSnippetKey === 'mining' ? 'bg-brand-cyan/15 text-brand-cyan font-semibold' : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-200'"
                :title="localizedSnippets.mining.title"
              >
                MINING
              </button>
              <button 
                @click="selectSnippet('ia')"
                class="px-2 py-0.5 rounded transition-colors cursor-pointer"
                :class="activeSnippetKey === 'ia' ? 'bg-brand-cyan/15 text-brand-cyan font-semibold' : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-200'"
                :title="localizedSnippets.ia.title"
              >
                IA
              </button>
              <button 
                @click="selectSnippet('va')"
                class="px-2 py-0.5 rounded transition-colors cursor-pointer"
                :class="activeSnippetKey === 'va' ? 'bg-brand-cyan/15 text-brand-cyan font-semibold' : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-200'"
                :title="localizedSnippets.va.title"
              >
                VISUAL
              </button>
              <button 
                @click="selectSnippet('bigdata')"
                class="px-2 py-0.5 rounded transition-colors cursor-pointer"
                :class="activeSnippetKey === 'bigdata' ? 'bg-brand-cyan/15 text-brand-cyan font-semibold' : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-200'"
                :title="localizedSnippets.bigdata.title"
              >
                SPARK
              </button>
            </div>
          </div>

          <!-- Code Display Body -->
          <div class="p-4 bg-slate-50 dark:bg-space-950 font-mono text-xs text-slate-800 dark:text-slate-200 overflow-x-auto min-h-[175px]">
            <div class="code-container space-y-1" v-html="localizedSnippets[activeSnippetKey].code"></div>
          </div>

          <!-- Sandbox Execution Footer -->
          <div class="px-4 py-2.5 bg-slate-100/90 dark:bg-space-900/90 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between gap-3">
            <span class="font-mono text-[11px] text-emerald-600 dark:text-emerald-400 truncate">
              {{ executionOutput }}
            </span>
            <button 
              @click="runSimulation" 
              :disabled="isExecuting"
              class="px-2.5 py-1 rounded bg-slate-900 dark:bg-slate-100 hover:bg-slate-800 dark:hover:bg-white text-white dark:text-slate-950 font-mono text-[11px] font-semibold flex items-center gap-1 shrink-0 transition-all disabled:opacity-50 cursor-pointer"
            >
              <span class="material-symbols-outlined text-xs">play_arrow</span>
              <span>{{ t('common.run') }}</span>
            </button>
          </div>

        </div>
      </div>

    </div>
  </section>
</template>
