<template>
  <footer class="mt-auto border-t border-slate-200 dark:border-slate-800 bg-white/70 dark:bg-space-950/70 py-8 px-4 sm:px-8 transition-colors duration-200">
    <div class="max-w-container mx-auto flex flex-col md:flex-row justify-between items-center gap-6">
      
      <!-- Left: Institutional Identity -->
      <div class="flex items-center gap-3.5 text-center md:text-left">
        <img 
          src="/assets/images/logo_usta_seal.gif" 
          alt="Escudo USTA" 
          class="w-8 h-8 object-contain opacity-85"
          onerror="this.style.display='none'"
        />
        <div>
          <p class="font-sans text-xs font-semibold text-slate-900 dark:text-slate-100">
            Universidad Santo Tomás — Seccional Tunja
          </p>
          <p class="font-mono text-[11px] text-slate-500 dark:text-slate-400">
            Facultad de Ingeniería de Sistemas • Especialización en Ciencia de Datos
          </p>
        </div>
      </div>

      <!-- Right: Developer Credit & Copyright -->
      <div class="flex flex-col md:items-end text-center md:text-right space-y-1">
        <p class="font-mono text-xs text-slate-700 dark:text-slate-300 font-medium">
          Desarrollado por: <span class="font-semibold text-slate-900 dark:text-brand-cyan">Ing. Santiago Alejandro Zúñiga Melo</span>
        </p>
        <p class="font-mono text-[10px] text-slate-400">
          © 2026 USTA Tunja. Entorno Académico de Posgrado.
        </p>
      </div>

    </div>
  </footer>
</template>
