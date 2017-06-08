'use strict';
var gulp = require('gulp');
var sass = require('gulp-sass');
var minifyCSS = require('gulp-csso');
var coffee = require('gulp-coffee');

var sassSrc = "./marssite/**/*.scss";
var cssDest = "./marssite/static";

var coffeeSrc = "./marssite/**/*.coffee";
var jsDest = cssDest; // save both assets in the same root

var node_module_collections = ["./node_modules/*font-awesome/**/*", "./node_modules/*vue/dist/*.js"];

gulp.task('collect', function(){
  gulp.src(node_module_collections )
    .pipe(gulp.dest("./marssite/static"));
});

gulp.task('sass', function(){
  return gulp.src(sassSrc)
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest(cssDest));
});

gulp.task('coffee', function(){
  return gulp.src(coffeeSrc)
    .pipe(coffee({bare:true}))
    .pipe(gulp.dest(jsDest));
});

gulp.task('sass:watch', function(){
  gulp.watch(sassSrc, ['sass']);
});

gulp.task('coffee:watch', function(){
  gulp.watch(coffeeSrc, ['coffee']);
});

gulp.task('watch', ["coffee:watch", "sass:watch"]);
