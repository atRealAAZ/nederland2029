/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'anthropic-orange': '#FF6B35',
        'anthropic-blue': '#0F172A', 
        'anthropic-gray': '#64748B',
        'anthropic-light': '#F8FAFC',
      },
      animation: {
        'fade-in': 'fadeIn 0.8s ease-out',
        'slide-up': 'slideUp 0.6s ease-out',
        'float': 'float 6s ease-in-out infinite',
      },
    },
  },
  plugins: [],
}