const gulp = require('gulp');
const cleanCss = require('gulp-clean-css');
const concat = require('gulp-concat');
const uglify = require('gulp-uglify');
const source = require('vinyl-source-stream');
const buffer = require('vinyl-buffer');
const browserify = require('browserify');

const css = [
  'static/css/chessboard-0.3.0.css',
  'static/css/chessground.css',
  'static/css/cburnett.css',
  'static/css/style.css'
];

gulp.task('css', () => {
  return gulp.src(css)
    .pipe(cleanCss({
      compability: 'ie8',
      level: {
        1: {
          specialComments: 0
        }
      }
    }, (details) => {
      console.log(`${details.name}: ${details.stats.originalSize} -> ${details.stats.minifiedSize}`);
    }))
    .pipe(concat('style.min.css'))
    .pipe(gulp.dest('static/css'));
});

gulp.task('js', () => {
  return browserify('src/client.js', { debug: true })
    .bundle()
    .pipe(source('client.min.js'))
    .pipe(buffer())
    //.pipe(uglify())
    .pipe(gulp.dest('static/js'));
});

gulp.task('watch', ['css', 'js'], () => {
  gulp.watch(css, ['css']);
  gulp.watch('src/client.js', ['js']);
});

gulp.task('default', ['css', 'js']);
