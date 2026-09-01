/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        // Stitch Executive Scholar Palette
        space: {
          950: "#0b0f13", // Base dark background
          900: "#12181f", // Surface container
          850: "#18212b", // Surface high
          800: "#1f2a37", // Border / stroke
          700: "#334155", // Neutral muted
          100: "#f1f5f9", // Light surface container
          50: "#f8fafc",  // Base light background
        },
        brand: {
          cyan: "#38bdf8",
          blue: "#2563eb",
          sapphire: "#0284c7",
          emerald: "#10b981",
          amber: "#f59e0b",
          rose: "#f43f5e"
        }
      },
      fontFamily: {
        sans: ['Geist', 'Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        mono: ['JetBrains Mono', 'GeistMono', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'monospace']
      },
      maxWidth: {
        'container': '1440px'
      }
    },
  },
  plugins: [],
}
