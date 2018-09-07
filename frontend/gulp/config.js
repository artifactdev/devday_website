/*
 * Task params:
 *
 * gulp --env development (default)
 * gulp --env production (minify/uglify version)
 *
 */

var basepath           = './';
var assets             = '../devday/devday/static';
var srcDir             = 'src';
var bower              = 'bower_components';
var srcTest            = 'src-test';
var fs                 = require('fs');
var pkg                = JSON.parse(fs.readFileSync('./package.json'));

module.exports = {
    basepath: basepath,
    strings: {
        banner: [
            '/**',
            ' * Build on <%= new Date().getFullYear() %>-<%= new Date().getMonth() + 1 %>-<%= new Date().getDate() %>',
            ' * @package ' + pkg.name + '',
            ' * @version v' + pkg.version  + '',
            ' */',
            ''].join('\n')
    },


    environment: {
        string: 'env',
        default: { env: process.env.NODE_ENV || 'development' },
        production: 'production',
        development: 'development'
    },

    sass: {
        src:  srcDir + '/scss/style.scss',
        allsrc: [
                srcDir + '/scss/*.scss',
                srcDir + '/scss/components/*.scss',
        ],
        dest: assets + '/css',
        options: {
            autoprefixer: {
                browsers: [
                    'last 2 versions',
                    'safari 8',
                    'ie 10',
                    'ios 9',
                    'android 4'
                ],
                cascade: true
            }
        }
    },

    sasslint: {
        src: [
            srcDir + '/scss/*.scss'
        ],
        dest: './report',
        options: {
            config: srcDir + '/scss/.scss-lint.yml',
            filePipeOutput: 'scss-lint-report.json',
            reporterOutputFormat: 'JSON',
            maxBuffer: 600*1024,
            endless: true
        }
    },

    js: {
        src:  [
            bower  + '/jquery/dist/jquery.js',
            bower  + '/bootstrap-sass-official/assets/javascripts/bootstrap.min.js',
            srcDir + '/js/libs/detectizr.min.js',
            srcDir + '/js/libs/modernizr.min.js',
            srcDir + '/js/libs/tether.min.js',
            srcDir + '/js/libs/twitterFetcher_min.js',
            srcDir + '/js/libs/jquery.bsPhotoGallery.js',
            srcDir + '/js/core/layer.js',
            srcDir + '/js/core/files.js',
            srcDir + '/js/core/js-registry.js'
        ],
        dest: assets + '/js',
        filename: 'main.js',
        minFilename: 'main.min.js'
    },

    jslint: {
        src: [
            srcDir + '/js/components/*.js',
            srcDir + '/js/core/*.js'
        ],
        options: {
            format: 'jslint',
            filePath: './report/js-lint-report.xml'
        }
    },

    jquery: {
        src:  [
            'bower_components/jquery/dist/jquery.js'
        ],
        dest: assets + '/js/'
    },

    images: {
        src:  [
            srcDir + '/images/*.*',
            srcDir + '/images/sponsors/*.*',
            srcDir + '/images/gallery/*.*'
        ],
        dest: assets + '/images'
    },

    fonts: {
        src:  [
            srcDir + '/fonts/*.*',
            'bower_components/simple-line-icons/fonts/*.*'
        ],
        dest: assets + '/fonts'
    },

    browsersync: {
        // your array of files and folders to watch for changes
        watchjs: [
            assets + '/js/*.js'
        ]
    }


};
