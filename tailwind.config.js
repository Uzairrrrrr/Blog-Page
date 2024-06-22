module.exports = {
  content: [
    './templates/**/*.html',
    './static/css/**/*.css',
    './static/js/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
  ]
}
