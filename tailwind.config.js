/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors:{
        'primary': '#002C54',
        'secondary': {
          100: '#E2E2D5',
          200: '#E6441B',
        }
      }
    },
    screens: {
      'lg': {'max': '1023px'},
      'sm': {'max': '1000px'},
    }
  },
  plugins: [],
}