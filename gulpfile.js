const { src, dest, watch } = require("gulp");
const if_ = require("gulp-if");
const sourcemaps = require("gulp-sourcemaps");
const sass = require("gulp-sass")(require("sass"));
const touch = require("gulp-touch-fd");
const cleanCSS = require("gulp-clean-css");

const isDev = !!process.env.DEBUG;

const build = () =>
    src("ckanext/zhulik/theme/style.scss")
        .pipe(if_(isDev, sourcemaps.init()))
        .pipe(sass())
        .pipe(!isDev ? cleanCSS({ compatibility: 'ie9', level: 2 }) : sourcemaps.write())
        .pipe(dest("ckanext/zhulik/assets/css"))
        .pipe(touch());

const watchSource = () =>
    watch(
        "ckanext/zhulik/theme/**/*.scss",
        { ignoreInitial: false },
        build
    );
exports.watch = watchSource;
exports.build = build;
