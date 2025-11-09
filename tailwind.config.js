/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        primary: '#1E3A8A', // 深蓝色 - 更优雅的主色调
        secondary: '#3B82F6', // 亮蓝色 - 更现代的辅助色
        accent: '#06B6D4', // 青色 - 科技感强
        dark: '#0F172A',
        light: '#F8FAFC',
        gray: {
          50: '#F8FAFC',
          100: '#F1F5F9',
          200: '#E2E8F0',
          300: '#CBD5E1',
          400: '#94A3B8',
          500: '#64748B',
          600: '#475569',
          700: '#334155',
          800: '#1E293B',
          900: '#0F172A',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        display: ['"Inter"', 'system-ui', 'sans-serif'],
      },
      typography: {
        DEFAULT: {
          css: {
            maxWidth: '65ch',
          },
        },
      },
      animation: {
        'float': 'float 6s ease-in-out infinite',
        'fade-in': 'fadeIn 0.8s ease-in-out',
        'slide-up': 'slideUp 0.8s ease-out',
        'glow': 'glow 2s ease-in-out infinite alternate',
        'bounce-gentle': 'bounceGentle 3s ease-in-out infinite',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-10px)' },
        },
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        glow: {
          '0%': { boxShadow: '0 0 20px rgba(30, 58, 138, 0.3)' },
          '100%': { boxShadow: '0 0 30px rgba(30, 58, 138, 0.5)' },
        },
        bounceGentle: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-5px)' },
        },
      },
      boxShadow: {
        'elegant': '0 20px 40px -12px rgba(30, 58, 138, 0.15), 0 8px 16px -8px rgba(30, 58, 138, 0.1)',
        'card': '0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03)',
        'premium': '0 25px 50px -12px rgba(30, 58, 138, 0.25), 0 0 0 1px rgba(30, 58, 138, 0.1)',
        'soft': '0 2px 15px -3px rgba(30, 58, 138, 0.1), 0 10px 20px -2px rgba(30, 58, 138, 0.05)',
      },
      transitionProperty: {
        'height': 'height',
        'spacing': 'margin, padding',
      },
      backdropFilter: {
        'none': 'none',
        'blur': 'blur(8px)',
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
