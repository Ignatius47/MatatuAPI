/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#e6fff9',
          100: '#b3ffef',
          300: '#66ffe2',
          500: '#00f5d4',
          700: '#00b39c',
          900: '#007a6b',
        },
        secondary: {
          50: '#f3e8ff',
          100: '#e9d5ff',
          300: '#c084fc',
          500: '#7b2cbf',
          700: '#5b21b6',
          900: '#4c1d95',
        },
        background: 'var(--color-background)',
        surface: 'var(--color-surface)',
        text: 'var(--color-text)',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        orbitron: ['Orbitron', 'sans-serif'],
      },
      animation: {
        'pulse-glow': 'pulse-glow 2s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
      keyframes: {
        'pulse-glow': {
          '0%, 100%': {
            opacity: '1',
            boxShadow: '0 0 15px rgba(0, 245, 212, 0.5)',
          },
          '50%': {
            opacity: '0.8',
            boxShadow: '0 0 25px rgba(0, 245, 212, 0.8)',
          },
        },
      },
    },
  },
  plugins: [],
}