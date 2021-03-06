webpackJsonp([0],[
/* 0 */,
/* 1 */,
/* 2 */,
/* 3 */,
/* 4 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
var _config;

_config = {
  apiUrl: "/dal/search/",
  rangeInputs: ["obs_date", "exposure_time", "release_date"],
  validatorConfig: {
    delay: 800,
    events: "input|blur",
    inject: true,
    dependsOn: "dependson"
  },
  allColumns: [
    {
      "checked": true,
      "mapping": "prop_id",
      "name": "Program Number",
      "num": 1
    }, {
      "checked": true,
      "mapping": "obs_date",
      "name": "Observed date",
      "num": 2
    }, {
      "checked": false,
      "mapping": "pi",
      "name": "Principle Investigator",
      "num": 3
    }, {
      "checked": false,
      "mapping": "ra",
      "name": "RA",
      "num": 4
    }, {
      "checked": false,
      "mapping": "dec",
      "name": "Dec",
      "num": 5
    }, {
      "checked": false,
      "mapping": "product",
      "name": "Product",
      "num": 6
    }, {
      "checked": false,
      "mapping": "depth",
      "name": "Depth",
      "num": 7
    }, {
      "checked": true,
      "mapping": "exposure",
      "name": "Exposure",
      "num": 8
    }, {
      "checked": true,
      "mapping": "filter",
      "name": "Filter",
      "num": 9
    }, {
      "checked": true,
      "mapping": "telescope",
      "name": "Telescope",
      "num": 10
    }, {
      "checked": true,
      "mapping": "instrument",
      "name": "Instrument",
      "num": 11
    }, {
      "checked": false,
      "mapping": "image_type",
      "name": "Image Type",
      "num": 12
    }, {
      "checked": false,
      "mapping": "filename",
      "name": "Filename",
      "num": 13
    }, {
      "checked": false,
      "mapping": "md5sum",
      "name": "MD5 sum",
      "num": 14
    }, {
      "checked": false,
      "mapping": "filesize",
      "name": "File size",
      "num": 15
    }, {
      "checked": false,
      "mapping": "original_filename",
      "name": "Original filename",
      "num": 16
    }, {
      "checked": false,
      "mapping": "reference",
      "name": "Reference",
      "num": 17
    }, {
      "checked": true,
      "mapping": "survey_id",
      "name": "Survey Id",
      "num": 18
    }, {
      "checked": false,
      "mapping": "release_date",
      "name": "Release Date",
      "num": 19
    }, {
      "checked": false,
      "mapping": "seeing",
      "name": "Seeing",
      "num": 20
    }
  ],
  formData: {
    coordinates: {
      ra: "",
      dec: ""
    },
    pi: null,
    search_box_min: null,
    prop_id: null,
    obs_date: ['', '', "="],
    filename: null,
    original_filename: null,
    telescope_instrument: [],
    exposure_time: ['', '', "="],
    release_date: ['', '', "="],
    image_filter: []
  },
  loadingMessages: ["Searching the cosmos...", "Deploying deep space probes...", "Is that you Dave?...", "There's so much S P A C E!"]
};

/* harmony default export */ __webpack_exports__["a"] = ({
  config: _config,
  mixin: {
    data: function() {
      return {
        config: _config
      };
    },
    methods: {
      stripData: function() {
        var key, newFormData, ref;
        newFormData = this.search ? JSON.parse(JSON.stringify(this.search)) : JSON.parse(localStorage.getItem("search"));
        for (key in newFormData) {
          if (_.isEqual(newFormData[key], this.config.formData[key])) {
            delete newFormData[key];
          } else {
            if (this.config.rangeInputs.indexOf(key) >= 0) {
              if (newFormData[key][2] === "=") {
                newFormData[key] = newFormData[key][0];
              }
            }
          }
        }
        if (newFormData.telescope_instrument) {
          newFormData.telescope_instrument = _.map(newFormData.telescope_instrument, (function(_this) {
            return function(item) {
              return item.split(",");
            };
          })(this));
        }
        if ((ref = newFormData.coordinates) != null ? ref.ra : void 0) {
          newFormData.coordinates.ra = parseFloat(newFormData.coordinates.ra);
          newFormData.coordinates.dec = parseFloat(newFormData.coordinates.dec);
        }
        localStorage.setItem('search', JSON.stringify(newFormData));
        return newFormData;
      },
      submitForm: function(event, paging, cb) {
        var message, msgs, newFormData, page, self, url;
        if (paging == null) {
          paging = null;
        }
        if (cb == null) {
          cb = null;
        }
        if (event != null) {
          event.preventDefault();
        }
        if (!paging) {
          this.loading = true;
          this.url = this.config.apiUrl;
          window.location.hash = "";
          this.$emit('setpagenum', 1);
          page = 1;
          localStorage.setItem("currentPage", 1);
          localStorage.setItem("searchData", JSON.stringify(this.search));
        } else {
          page = localStorage.getItem("currentPage");
        }
        newFormData = this.stripData();
        msgs = this.config.loadingMessages;
        message = Math.floor(Math.random() * msgs.length);
        this.loadingMessage = msgs[message];
        self = this;
        url = this.config.apiUrl + ("?page=" + page);
        return new Ajax({
          url: url,
          method: "post",
          accept: "json",
          data: {
            search: newFormData
          },
          success: function(data) {
            var saveData;
            window.location.hash = "#query";
            self.loading = false;
            saveData = typeof data === "object" ? JSON.stringify(data) : data;
            localStorage.setItem('results', saveData);
            self.$emit("displayform", ["results", saveData]);
            if (cb) {
              return cb(data);
            }
          },
          fail: function(statusMsg, status, xhr) {
            console.log("Request failed, got this");
            message = "" + statusMsg;
            if (xhr.response) {
              message += ":  " + xhr.response.errorMessage;
            }
            self.loading = false;
            self.modalTitle = "Request Error";
            self.modalBody = "<div class='alert alert-danger'>There was an error with your request.<br> <strong>" + message + "</strong></div>";
            ToggleModal("#search-modal");
            return console.dir(arguments);
          }
        });
      }
    }
  }
});


/***/ }),
/* 5 */,
/* 6 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_vue__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_vue___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_vue__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_moment__ = __webpack_require__(2);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_moment___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_moment__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__vue_Search_vue__ = __webpack_require__(9);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__vue_Search_vue___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_2__vue_Search_vue__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__vue_Results_vue__ = __webpack_require__(13);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__vue_Results_vue___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_3__vue_Results_vue__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__styles_search_scss__ = __webpack_require__(5);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__styles_search_scss___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_4__styles_search_scss__);
var App;











App = (function() {
  function App() {
    window.moment = __WEBPACK_IMPORTED_MODULE_1_moment___default.a;
    new __WEBPACK_IMPORTED_MODULE_0_vue___default.a({
      el: "#content",
      template: "<component compdata='componentData' v-bind:is='currentView' v-on:displayform='switchComponent' />",
      methods: {
        switchComponent: function(data) {
          this.componentData = data[1];
          return this.currentView = data[0];
        }
      },
      data: {
        currentView: "search",
        componentData: []
      },
      components: {
        search: __WEBPACK_IMPORTED_MODULE_2__vue_Search_vue___default.a,
        results: __WEBPACK_IMPORTED_MODULE_3__vue_Results_vue___default.a
      }
    });
  }

  return App;

})();

new App();


/***/ }),
/* 7 */,
/* 8 */,
/* 9 */
/***/ (function(module, exports, __webpack_require__) {

var disposed = false
var Component = __webpack_require__(1)(
  /* script */
  __webpack_require__(10),
  /* template */
  __webpack_require__(12),
  /* styles */
  null,
  /* scopeId */
  null,
  /* moduleIdentifier (server only) */
  null
)
Component.options.__file = "/Users/ppeterson/Workspace/dev-env/mars/marssite/portal/vue/Search.vue"
if (Component.esModule && Object.keys(Component.esModule).some(function (key) {return key !== "default" && key.substr(0, 2) !== "__"})) {console.error("named exports are not supported in *.vue files.")}
if (Component.options.functional) {console.error("[vue-loader] Search.vue: functional components are not supported with templates, they should use render functions.")}

/* hot reload */
if (false) {(function () {
  var hotAPI = require("vue-hot-reload-api")
  hotAPI.install(require("vue"), false)
  if (!hotAPI.compatible) return
  module.hot.accept()
  if (!module.hot.data) {
    hotAPI.createRecord("data-v-b46fd354", Component.options)
  } else {
    hotAPI.reload("data-v-b46fd354", Component.options)
  }
  module.hot.dispose(function (data) {
    disposed = true
  })
})()}

module.exports = Component.exports


/***/ }),
/* 10 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__js_search_coffee__ = __webpack_require__(11);
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//



/* harmony default export */ __webpack_exports__["default"] = (__WEBPACK_IMPORTED_MODULE_0__js_search_coffee__["a" /* default */]);

/***/ }),
/* 11 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_vue__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_vue___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_vue__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_vee_validate__ = __webpack_require__(3);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_vee_validate___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_vee_validate__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__mixins_coffee__ = __webpack_require__(4);

/*
Author: Peter Peterson
Date: 2017-06-09
Description: Serves functionality for submitting and displaying archive query forms/results
Original file: search.coffee
 */
var config, dateLookup, searchFormComponent, validateDependsOn;







validateDependsOn = {
  getMessage: function(field, params, data) {
    var dependsOn, id;
    id = params[0].replace("#", "");
    dependsOn = document.querySelector("label[for=" + id + "]").innerText;
    return (data && data.message) || ("This field depends on " + dependsOn);
  },
  validate: function(value, args) {
    return document.querySelector(args[0]).value !== "";
  }
};

config = __WEBPACK_IMPORTED_MODULE_2__mixins_coffee__["a" /* default */].config;

(function() {
  var validation;
  window.addEventListener('searchLoaded', function(e) {
    console.log("Search loaded", e);
    return window.base.bindEvents();
  });
  __WEBPACK_IMPORTED_MODULE_1_vee_validate__["Validator"].extend('dependson', validateDependsOn);
  validation = new __WEBPACK_IMPORTED_MODULE_1_vee_validate__["Validator"]({
    dependant: "dependson"
  });
  return __WEBPACK_IMPORTED_MODULE_0_vue___default.a.use(__WEBPACK_IMPORTED_MODULE_1_vee_validate___default.a, config.validatorConfig);
})();

dateLookup = {
  "obs-date": {
    "field": "obs_date",
    "index": 0
  },
  "obs-date-max": {
    "field": 'obs_date',
    "index": 1
  },
  "release-date": {
    "field": "release_date",
    "index": 0
  },
  "release-date-max": {
    "field": "release_date",
    "index": 1
  },
  "parent": {
    "obj": this
  }
};

searchFormComponent = {
  mixins: [__WEBPACK_IMPORTED_MODULE_2__mixins_coffee__["a" /* default */].mixin],
  created: function() {
    return this.getTelescopes();
  },
  mounted: function() {
    var oldSearch;
    if (window.location.hash.indexOf("search_again") > -1) {
      oldSearch = JSON.parse(localStorage.getItem("searchData"));
      this.search = oldSearch;
    } else if (window.location.hash.indexOf("query") > -1) {
      this.$emit("displayform", ["results", []]);
    }
    window.base.bindEvents();
    $("input.date").datepicker({
      onSelect: (function(_this) {
        return function(dateText, datePicker) {
          var e, field, fieldName;
          fieldName = datePicker.input[0].name;
          field = _this.search[dateLookup[fieldName].field];
          field[dateLookup[fieldName].index] = dateText;
          e = new CustomEvent("datechanged", {
            'detail': {
              'date': dateText
            }
          });
          document.dispatchEvent(e);
          return _this.code = new Date().getTime();
        };
      })(this)
    });
    $("input.date").datepicker("option", "dateFormat", "yy-mm-dd");
    window.searchVue = this;
    return document.addEventListener("datechanged", function() {
      return console.log("update code view");
    });
  },
  computed: {
    code: {
      get: function() {
        this.codeView = JSON.stringify({
          search: this.stripData()
        }, null, 2);
        return this.codeView;
      },
      set: function(update) {
        this.codeUpdate = update;
        this.codeView = JSON.stringify({
          search: this.stripData()
        }, null, 2);
        return null;
      }
    }
  },
  data: function() {
    return {
      url: config.apiUrl,
      visible: true,
      loading: false,
      codeUpdate: 0,
      codeView: "",
      modalTitle: "",
      modalBody: "",
      loadingMessage: "Sweeping up star dust...",
      search: JSON.parse(JSON.stringify(config.formData)),
      showExposureMax: false,
      showObsDateMax: false,
      showReleaseDateMax: false,
      showBothExposureFields: false,
      showBothObsDateFields: false,
      showBothReleaseDateFields: false,
      telescopes: [],
      relatedSplitFieldFlags: {
        "exposure_time": {
          "fieldFlag": 'showExposureMax',
          "bothFieldFlag": "showBothExposureFields"
        },
        "obs_date": {
          "fieldFlag": "showObsDateMax",
          "bothFieldFlag": "showBothObsDateFields"
        },
        "release_date": {
          "fieldFlag": "showReleaseDateMax",
          "bothFieldFlag": "showBothReleaseDateFields"
        }
      },
      option: {
        format: 'YYYY-MM-DD'
      }
    };
  },
  methods: {
    closeModal: function() {
      return ToggleModal("#search-modal");
    },
    newSearch: function() {
      this.search = JSON.parse(JSON.stringify(this.config.formData));
      return localStorage.setItem("searchData", JSON.stringify(this.search));
    },
    getTelescopes: function() {
      var now, self, telescopes;
      telescopes = JSON.parse(localStorage.getItem("telescopes") || "0");
      self = this;
      now = moment();
      if (telescopes && moment(telescopes != null ? telescopes.expires : void 0) > now) {
        return self.telescopes = telescopes.telescopes;
      } else {
        return new Ajax({
          url: window.location.origin + "/dal/ti-pairs",
          method: "get",
          accept: "json",
          success: function(data) {
            self.telescopes = data;
            telescopes = {
              expires: moment().add(7, 'days'),
              telescopes: data
            };
            return localStorage.setItem("telescopes", JSON.stringify(telescopes));
          }
        });
      }
    },
    splitSelection: function(val) {
      var bothFlag, fieldFlag;
      fieldFlag = this.relatedSplitFieldFlags[val]['fieldFlag'];
      bothFlag = this.relatedSplitFieldFlags[val]['bothFieldFlag'];
      if (this.search[val][2] === "(]" || this.search[val][2] === "[]") {
        this[fieldFlag] = true;
      } else {
        this[fieldFlag] = false;
      }
      if (this.search[val][2] === "[]") {
        return this[bothFlag] = true;
      } else {
        return this[bothFlag] = false;
      }
    }
  }
};

/* harmony default export */ __webpack_exports__["a"] = (searchFormComponent);


/***/ }),
/* 12 */
/***/ (function(module, exports, __webpack_require__) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('div', {
    staticClass: "container",
    attrs: {
      "id": "search-form"
    }
  }, [_c('transition', {
    attrs: {
      "name": "fade"
    }
  }, [_c('div', {
    directives: [{
      name: "show",
      rawName: "v-show",
      value: (_vm.loading),
      expression: "loading"
    }],
    staticClass: "loading"
  }, [_c('div', {
    staticClass: "loading-message"
  }, [_c('small', [_vm._v("Loading...")]), _vm._v(" "), _c('div', {
    staticClass: "message",
    attrs: {
      "text": _vm.loadingMessage
    }
  }, [_vm._v(_vm._s(_vm.loadingMessage))])])])]), _vm._v(" "), _c('transition', {
    attrs: {
      "name": "fade"
    }
  }, [(_vm.visible) ? _c('form', {
    attrs: {
      "method": "post",
      "action": ""
    }
  }, [_c('div', {
    staticClass: "form-head row"
  }, [_c('div', {
    staticClass: "col-xs-12 col-md-6"
  }, [_c('h1', [_vm._v("NOAO Science Archive")]), _vm._v(" "), _c('p', {
    staticClass: "lead"
  }, [_vm._v("Raw and reduced data from NOAO telescopes and instruments")])]), _vm._v(" "), _c('div', {
    staticClass: "col-xs-12 col-md-6 text-right",
    attrs: {
      "rel": "form-submit"
    }
  }, [_c('div', {
    staticClass: "form-inline"
  }, [_c('label', {
    staticClass: "form-group"
  }, [_vm._v("Search wihin collections:\n                            "), _c('select', {
    staticClass: "form-control",
    attrs: {
      "id": "search-collections",
      "name": "collections"
    }
  }, [_c('option', {
    attrs: {
      "value": "all"
    }
  }, [_vm._v("All Holdings")]), _vm._v(" "), _c('option', {
    attrs: {
      "value": "my"
    }
  }, [_vm._v("My Collection")]), _vm._v(" "), _c('option', {
    attrs: {
      "value": ""
    }
  }, [_vm._v("Decam...")])])]), _vm._v(" "), _c('button', {
    staticClass: "btn btn-primary",
    attrs: {
      "id": "submit-form",
      "type": "submit"
    },
    on: {
      "click": _vm.submitForm
    }
  }, [_vm._v("Search")]), _vm._v(" "), _c('div', [_c('a', {
    attrs: {
      "href": "#"
    },
    on: {
      "click": _vm.newSearch
    }
  }, [_vm._v("Clear Search")])])])])]), _vm._v(" "), _c('div', {
    staticClass: "row"
  }, [_c('div', {
    staticClass: "col-xs-12 form-section panel panel-default"
  }, [_c('div', {
    staticClass: "collapsible open container-fluid"
  }, [_c('div', {
    staticClass: "section-heading row"
  }, [_c('div', {
    staticClass: "col-xs-6"
  }, [_c('h4', [_vm._v("Target "), _c('small', [_vm._v("Search via coordinates or by object name")])])]), _vm._v(" "), _c('div', {
    staticClass: "col-xs-6"
  }, [_c('div', {
    staticClass: "section-toggle"
  }, [_c('span', {
    staticClass: "icon open"
  })])])]), _vm._v(" "), _c('div', {
    staticClass: "section-content row"
  }, [_c('div', {
    staticClass: "col-md-6"
  }, [_c('div', {
    staticClass: "form-group"
  }, [_c('label', {
    staticClass: "floating",
    attrs: {
      "for": "object-name"
    }
  }, [_vm._v("Object Name")]), _vm._v(" "), _c('input', {
    staticClass: "form-control",
    attrs: {
      "name": "object-name",
      "type": "text",
      "value": "",
      "placeholder": "Object Name",
      "id": "object-name"
    }
  })]), _vm._v(" "), _c('button', {
    staticClass: "btn btn-default"
  }, [_vm._v("Resolve object")])]), _vm._v(" "), _c('div', {
    staticClass: "col-md-6"
  }, [_c('div', {
    staticClass: "col-md-6"
  }, [_c('div', {
    staticClass: "form-group"
  }, [_c('label', {
    staticClass: "floating",
    attrs: {
      "for": "ra"
    }
  }, [_vm._v("Ra")]), _vm._v(" "), _c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.search.coordinates.ra),
      expression: "search.coordinates.ra"
    }, {
      name: "validate",
      rawName: "v-validate",
      value: ('decimal|dependson:#dec'),
      expression: "'decimal|dependson:#dec'"
    }],
    staticClass: "form-control",
    attrs: {
      "placeholder": "RA",
      "name": "ra",
      "id": "ra",
      "type": "text",
      "value": ""
    },
    domProps: {
      "value": (_vm.search.coordinates.ra)
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        _vm.search.coordinates.ra = $event.target.value
      }
    }
  }), _vm._v(" "), (_vm.errors.has('ra')) ? _c('span', {
    staticClass: "error-message"
  }, [_vm._v("\n                                            " + _vm._s(_vm.errors.first('ra')) + "\n                                        ")]) : _vm._e()])]), _vm._v(" "), _c('div', {
    staticClass: "col-md-6"
  }, [_c('div', {
    staticClass: "form-group"
  }, [_c('label', {
    staticClass: "floating",
    attrs: {
      "for": "dec"
    }
  }, [_vm._v("Dec")]), _vm._v(" "), _c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.search.coordinates.dec),
      expression: "search.coordinates.dec"
    }, {
      name: "validate",
      rawName: "v-validate",
      value: ('decimal|dependson:#ra'),
      expression: "'decimal|dependson:#ra'"
    }],
    staticClass: "form-control",
    attrs: {
      "placeholder": "Dec",
      "name": "dec",
      "id": "dec",
      "type": "text",
      "value": ""
    },
    domProps: {
      "value": (_vm.search.coordinates.dec)
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        _vm.search.coordinates.dec = $event.target.value
      }
    }
  }), _vm._v(" "), (_vm.errors.has('dec')) ? _c('span', {
    staticClass: "error-message"
  }, [_vm._v("\n                                            " + _vm._s(_vm.errors.first('dec')) + "\n                                        ")]) : _vm._e()])])])])])])]), _vm._v(" "), _c('div', {
    staticClass: "row"
  }, [_c('div', {
    staticClass: "col-xs-12 form-section"
  }, [_c('div', {
    staticClass: "collapsible open container-fluid"
  }, [_c('div', {
    staticClass: "section-heading row"
  }, [_c('div', {
    staticClass: "col-xs-6"
  }, [_c('h4', [_vm._v("Obervation "), _c('small', [_vm._v("Search by obervation details")])])]), _vm._v(" "), _c('div', {
    staticClass: "col-xs-6"
  }, [_c('div', {
    staticClass: "section-toggle"
  }, [_c('div', {
    staticClass: "icon"
  })])])]), _vm._v(" "), _c('div', {
    staticClass: "section-content row"
  }, [_c('div', {
    staticClass: "col-md-6"
  }, [_c('div', {
    staticClass: "form-group"
  }, [_c('label', {
    staticClass: "floating",
    attrs: {
      "for": "program-number"
    }
  }, [_vm._v("Program Number (Prop ID)")]), _vm._v(" "), _c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.search.prop_id),
      expression: "search.prop_id"
    }],
    staticClass: "form-control",
    attrs: {
      "name": "program-number",
      "id": "program-number",
      "placeholder": "Program Number (Prop ID)",
      "type": "text",
      "value": ""
    },
    domProps: {
      "value": (_vm.search.prop_id)
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        _vm.search.prop_id = $event.target.value
      }
    }
  })]), _vm._v(" "), _c('div', {
    staticClass: "form-group"
  }, [_c('label', {
    staticClass: "floating",
    attrs: {
      "for": "principle-investigator"
    }
  }, [_vm._v("Principle Investigator")]), _vm._v(" "), _c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.search.pi),
      expression: "search.pi"
    }],
    staticClass: "form-control",
    attrs: {
      "name": "principle-investigator",
      "id": "principle-investigator",
      "placeholder": "Principle Investigator",
      "type": "text",
      "value": ""
    },
    domProps: {
      "value": (_vm.search.pi)
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        _vm.search.pi = $event.target.value
      }
    }
  })]), _vm._v(" "), _c('div', {
    staticClass: "form-group"
  }, [_c('label', {
    staticClass: "floating",
    attrs: {
      "for": "original-filename"
    }
  }, [_vm._v("Original Filename")]), _vm._v(" "), _c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.search.original_filename),
      expression: "search.original_filename"
    }],
    staticClass: "form-control",
    attrs: {
      "id": "original-filename",
      "name": "original-filename",
      "type": "text",
      "value": "",
      "placeholder": "Original Filename"
    },
    domProps: {
      "value": (_vm.search.original_filename)
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        _vm.search.original_filename = $event.target.value
      }
    }
  })]), _vm._v(" "), _c('div', {
    staticClass: "form-group"
  }, [_c('label', {
    staticClass: "floating",
    attrs: {
      "for": "archive-filename"
    }
  }, [_vm._v("Archive Filename")]), _vm._v(" "), _c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.search.filename),
      expression: "search.filename"
    }],
    staticClass: "form-control",
    attrs: {
      "id": "archive-filename",
      "name": "archive-filename",
      "type": "text",
      "value": "",
      "placeholder": "Archive Filename"
    },
    domProps: {
      "value": (_vm.search.filename)
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        _vm.search.filename = $event.target.value
      }
    }
  })])]), _vm._v(" "), _c('div', {
    staticClass: "col-md-6"
  }, [_c('div', {
    staticClass: "form-group"
  }, [_c('div', {
    staticClass: "input-group select-group split-val",
    class: {
      'display-hidden': _vm.showBothObsDateFields
    }
  }, [_c('label', {
    staticClass: "floating",
    attrs: {
      "for": "obs-date"
    }
  }, [_vm._v("Observation Date "), _c('small', [_vm._v("(YYYY-MM-DD)")])]), _vm._v(" "), _c('select', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.search.obs_date[2]),
      expression: "search.obs_date[2]"
    }],
    staticClass: "form-control input-group-addon",
    attrs: {
      "name": "obs-date-interval"
    },
    on: {
      "change": [function($event) {
        var $$selectedVal = Array.prototype.filter.call($event.target.options, function(o) {
          return o.selected
        }).map(function(o) {
          var val = "_value" in o ? o._value : o.value;
          return val
        });
        var $$exp = _vm.search.obs_date,
          $$idx = 2;
        if (!Array.isArray($$exp)) {
          _vm.search.obs_date[2] = $event.target.multiple ? $$selectedVal : $$selectedVal[0]
        } else {
          $$exp.splice($$idx, 1, $event.target.multiple ? $$selectedVal : $$selectedVal[0])
        }
      }, function($event) {
        _vm.splitSelection('obs_date')
      }]
    }
  }, [_c('option', {
    attrs: {
      "value": "="
    }
  }, [_vm._v("On Date")]), _vm._v(" "), _c('option', {
    attrs: {
      "value": "(]"
    }
  }, [_vm._v("Before Date")]), _vm._v(" "), _c('option', {
    attrs: {
      "value": "[)"
    }
  }, [_vm._v("After Date")]), _vm._v(" "), _c('option', {
    staticClass: "toggle-option",
    attrs: {
      "value": "[]"
    }
  }, [_vm._v("Between")])]), _vm._v(" "), (_vm.search.obs_date[2] !== '(]') ? _c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.search.obs_date[0]),
      expression: "search.obs_date[0]"
    }, {
      name: "validate",
      rawName: "v-validate",
      value: ('date_format:YYYY-MM-DD'),
      expression: "'date_format:YYYY-MM-DD'"
    }],
    staticClass: "date form-control",
    attrs: {
      "id": "obs-date",
      "data-polyfill": "all",
      "name": "obs-date",
      "type": "text",
      "value": "",
      "placeholder": "Obervation date"
    },
    domProps: {
      "value": (_vm.search.obs_date[0])
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        var $$exp = _vm.search.obs_date,
          $$idx = 0;
        if (!Array.isArray($$exp)) {
          _vm.search.obs_date[0] = $event.target.value
        } else {
          $$exp.splice($$idx, 1, $event.target.value)
        }
      }
    }
  }) : _vm._e(), _vm._v(" "), _c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.search.obs_date[1]),
      expression: "search.obs_date[1]"
    }, {
      name: "show",
      rawName: "v-show",
      value: (_vm.showObsDateMax),
      expression: "showObsDateMax"
    }, {
      name: "validate",
      rawName: "v-validate",
      value: ('date_format:YYYY-MM-DD'),
      expression: "'date_format:YYYY-MM-DD'"
    }],
    staticClass: "date form-control",
    class: {
      'hidden-split': _vm.showBothObsDateFields
    },
    attrs: {
      "id": "obs-date-max",
      "name": "obs-date-max",
      "type": "text",
      "value": "",
      "placeholder": "Max Observation Date"
    },
    domProps: {
      "value": (_vm.search.obs_date[1])
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        var $$exp = _vm.search.obs_date,
          $$idx = 1;
        if (!Array.isArray($$exp)) {
          _vm.search.obs_date[1] = $event.target.value
        } else {
          $$exp.splice($$idx, 1, $event.target.value)
        }
      }
    }
  }), _vm._v(" "), (_vm.errors.has('obs-date')) ? _c('span', {
    staticClass: "error-message"
  }, [_vm._v(_vm._s(_vm.errors.first('obs-date')))]) : _vm._e(), _vm._v(" "), (_vm.errors.has('obs-date-max')) ? _c('span', {
    staticClass: "error-message"
  }, [_vm._v(_vm._s(_vm.errors.first('obs-date-max')))]) : _vm._e()])]), _vm._v(" "), _c('div', {
    staticClass: "form-group"
  }, [_c('div', {
    staticClass: "input-group select-group split-val",
    class: {
      'display-hidden': _vm.showBothExposureFields
    }
  }, [_c('label', {
    staticClass: "floating",
    attrs: {
      "for": "exposure"
    }
  }, [_vm._v("Exposure")]), _vm._v(" "), _c('select', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.search.exposure_time[2]),
      expression: "search.exposure_time[2]"
    }],
    staticClass: "form-control input-group-addon",
    attrs: {
      "id": "",
      "name": "expore-interval"
    },
    on: {
      "change": [function($event) {
        var $$selectedVal = Array.prototype.filter.call($event.target.options, function(o) {
          return o.selected
        }).map(function(o) {
          var val = "_value" in o ? o._value : o.value;
          return val
        });
        var $$exp = _vm.search.exposure_time,
          $$idx = 2;
        if (!Array.isArray($$exp)) {
          _vm.search.exposure_time[2] = $event.target.multiple ? $$selectedVal : $$selectedVal[0]
        } else {
          $$exp.splice($$idx, 1, $event.target.multiple ? $$selectedVal : $$selectedVal[0])
        }
      }, function($event) {
        _vm.splitSelection('exposure_time')
      }]
    }
  }, [_c('option', {
    attrs: {
      "value": "="
    }
  }, [_vm._v("Exactly")]), _vm._v(" "), _c('option', {
    attrs: {
      "value": "(]"
    }
  }, [_vm._v("Less Than")]), _vm._v(" "), _c('option', {
    attrs: {
      "value": "[)"
    }
  }, [_vm._v("Greater Than")]), _vm._v(" "), _c('option', {
    staticClass: "toggle-option",
    attrs: {
      "value": "[]"
    }
  }, [_vm._v("Between")])]), _vm._v(" "), (_vm.search.exposure_time[2] !== '(]') ? _c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.search.exposure_time[0]),
      expression: "search.exposure_time[0]"
    }, {
      name: "validate",
      rawName: "v-validate",
      value: ('numeric'),
      expression: "'numeric'"
    }],
    staticClass: "form-control",
    attrs: {
      "id": "exposure",
      "name": "exposure",
      "type": "text",
      "value": "",
      "placeholder": "Exposure in seconds"
    },
    domProps: {
      "value": (_vm.search.exposure_time[0])
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        var $$exp = _vm.search.exposure_time,
          $$idx = 0;
        if (!Array.isArray($$exp)) {
          _vm.search.exposure_time[0] = $event.target.value
        } else {
          $$exp.splice($$idx, 1, $event.target.value)
        }
      }
    }
  }) : _vm._e(), _vm._v(" "), _c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.search.exposure_time[1]),
      expression: "search.exposure_time[1]"
    }, {
      name: "show",
      rawName: "v-show",
      value: (_vm.showExposureMax),
      expression: "showExposureMax"
    }, {
      name: "validate",
      rawName: "v-validate",
      value: ('numeric'),
      expression: "'numeric'"
    }],
    staticClass: "form-control",
    class: {
      'hidden-split': _vm.showBothExposureFields
    },
    attrs: {
      "id": "exposure-max",
      "name": "exposure-max",
      "type": "text",
      "value": "",
      "placeholder": "Max exposure"
    },
    domProps: {
      "value": (_vm.search.exposure_time[1])
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        var $$exp = _vm.search.exposure_time,
          $$idx = 1;
        if (!Array.isArray($$exp)) {
          _vm.search.exposure_time[1] = $event.target.value
        } else {
          $$exp.splice($$idx, 1, $event.target.value)
        }
      }
    }
  }), _vm._v(" "), (_vm.errors.has('exposure')) ? _c('span', {
    staticClass: "error-message"
  }, [_vm._v(_vm._s(_vm.errors.first('exposure')))]) : _vm._e(), _vm._v(" "), (_vm.errors.has('exposure-max')) ? _c('span', {
    staticClass: "error-message"
  }, [_vm._v(_vm._s(_vm.errors.first('exposure-max')))]) : _vm._e()])])])])])])]), _vm._v(" "), _c('div', {
    staticClass: "row"
  }, [_c('div', {
    staticClass: "col-xs-12 form-section panel panel-default"
  }, [_c('div', {
    staticClass: "collapsible open container-fluid"
  }, [_c('div', {
    staticClass: "section-heading row"
  }, [_c('div', {
    staticClass: "col-xs-6"
  }, [_c('h4', [_vm._v("Image & Telescope / Instrument "), _c('small', [_vm._v("Search a image processing and specific telelscope and instrument")])])]), _vm._v(" "), _c('div', {
    staticClass: "col-xs-6"
  }, [_c('div', {
    staticClass: "section-toggle"
  }, [_c('span', {
    staticClass: "icon"
  })])])]), _vm._v(" "), _c('div', {
    staticClass: "section-content row"
  }, [_c('div', {
    staticClass: "col-sm-6"
  }, [_c('div', {
    staticClass: "form-group"
  }, [_c('div', {
    staticClass: "input-group select-group split-val",
    class: {
      'display-hidden': _vm.showBothReleaseDateFields
    }
  }, [_c('label', {
    staticClass: "floating",
    attrs: {
      "for": "release-date"
    }
  }, [_vm._v("Public Release Date "), _c('small', [_vm._v("(YYYY-MM-DD)")])]), _vm._v(" "), _c('select', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.search.release_date[2]),
      expression: "search.release_date[2]"
    }],
    staticClass: "form-control input-group-addon",
    attrs: {
      "id": "",
      "name": "release-date-interval"
    },
    on: {
      "change": [function($event) {
        var $$selectedVal = Array.prototype.filter.call($event.target.options, function(o) {
          return o.selected
        }).map(function(o) {
          var val = "_value" in o ? o._value : o.value;
          return val
        });
        var $$exp = _vm.search.release_date,
          $$idx = 2;
        if (!Array.isArray($$exp)) {
          _vm.search.release_date[2] = $event.target.multiple ? $$selectedVal : $$selectedVal[0]
        } else {
          $$exp.splice($$idx, 1, $event.target.multiple ? $$selectedVal : $$selectedVal[0])
        }
      }, function($event) {
        _vm.splitSelection('release_date')
      }]
    }
  }, [_c('option', {
    attrs: {
      "value": "="
    }
  }, [_vm._v("On Date")]), _vm._v(" "), _c('option', {
    attrs: {
      "value": "(]"
    }
  }, [_vm._v("Before Date")]), _vm._v(" "), _c('option', {
    attrs: {
      "value": "[)"
    }
  }, [_vm._v("After Date")]), _vm._v(" "), _c('option', {
    staticClass: "toggle-option",
    attrs: {
      "value": "[]"
    }
  }, [_vm._v("Between")])]), _vm._v(" "), (_vm.search.release_date[2] !== '(]') ? _c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.search.release_date[0]),
      expression: "search.release_date[0]"
    }, {
      name: "validate",
      rawName: "v-validate",
      value: ('date_format:YYYY-MM-DD'),
      expression: "'date_format:YYYY-MM-DD'"
    }],
    staticClass: "date form-control",
    attrs: {
      "id": "release-date",
      "data-polyfill": "all",
      "name": "release-date",
      "type": "text",
      "value": "",
      "placeholder": "Release date"
    },
    domProps: {
      "value": (_vm.search.release_date[0])
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        var $$exp = _vm.search.release_date,
          $$idx = 0;
        if (!Array.isArray($$exp)) {
          _vm.search.release_date[0] = $event.target.value
        } else {
          $$exp.splice($$idx, 1, $event.target.value)
        }
      }
    }
  }) : _vm._e(), _vm._v(" "), _c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.search.release_date[1]),
      expression: "search.release_date[1]"
    }, {
      name: "show",
      rawName: "v-show",
      value: (_vm.showReleaseDateMax),
      expression: "showReleaseDateMax"
    }, {
      name: "validate",
      rawName: "v-validate",
      value: ('date_format:YYYY-MM-DD'),
      expression: "'date_format:YYYY-MM-DD'"
    }],
    staticClass: "date form-control",
    class: {
      'hidden-split': _vm.showBothReleaseDateFields
    },
    attrs: {
      "id": "release-date-max",
      "data-polyfill": "all",
      "name": "release-date-max",
      "type": "text",
      "value": "",
      "placeholder": "Max release date"
    },
    domProps: {
      "value": (_vm.search.release_date[1])
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        var $$exp = _vm.search.release_date,
          $$idx = 1;
        if (!Array.isArray($$exp)) {
          _vm.search.release_date[1] = $event.target.value
        } else {
          $$exp.splice($$idx, 1, $event.target.value)
        }
      }
    }
  })])])]), _vm._v(" "), _c('div', {
    staticClass: "col-sm-3"
  }, [_c('div', {
    staticClass: "form-group"
  }, [_c('div', {
    staticClass: "input-group"
  }, [_c('label', {
    attrs: {
      "for": "image-filter"
    }
  }, [_vm._v("Image Filter")]), _vm._v(" "), _c('select', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.search.image_filter),
      expression: "search.image_filter"
    }],
    staticClass: "form-control",
    attrs: {
      "multiple": "",
      "name": "image-filter",
      "size": "10 ",
      "id": "image-filter"
    },
    on: {
      "change": function($event) {
        var $$selectedVal = Array.prototype.filter.call($event.target.options, function(o) {
          return o.selected
        }).map(function(o) {
          var val = "_value" in o ? o._value : o.value;
          return val
        });
        _vm.search.image_filter = $event.target.multiple ? $$selectedVal : $$selectedVal[0]
      }
    }
  }, [_c('option', {
    attrs: {
      "value": "raw"
    }
  }, [_vm._v("Raw image")]), _vm._v(" "), _c('option', {
    attrs: {
      "value": "calibrated"
    }
  }, [_vm._v("Calibrated")]), _vm._v(" "), _c('option', {
    attrs: {
      "value": "reprojected"
    }
  }, [_vm._v("Reprojected")]), _vm._v(" "), _c('option', {
    attrs: {
      "value": "stacked"
    }
  }, [_vm._v("Stacked")]), _vm._v(" "), _c('option', {
    attrs: {
      "value": "master_calibration"
    }
  }, [_vm._v("Master Calibration")]), _vm._v(" "), _c('option', {
    attrs: {
      "value": "image_tiles"
    }
  }, [_vm._v("Image Tiles")]), _vm._v(" "), _c('option', {
    attrs: {
      "value": "sky_subtracted"
    }
  }, [_vm._v("Sky Subtracted (Newfirm)")])]), _vm._v(" "), _c('p', {
    staticClass: "help-block"
  }, [_vm._v("\n                                        * "), _c('em', [_vm._v("Calibrated, Reprojected, Stacked, Master calibration, Image Tiles")]), _vm._v(" are for "), _c('strong', [_vm._v("Mosiac, NEWFIRM and DECam")]), _vm._v(".\n                                    ")])])])]), _vm._v(" "), _c('div', {
    staticClass: "col-sm-3"
  }, [_c('div', {
    staticClass: "form-group"
  }, [_c('div', {
    staticClass: "input-group"
  }, [_c('label', {
    attrs: {
      "for": "telescope"
    }
  }, [_vm._v("Telescope & Intrument")]), _vm._v(" "), _c('select', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.search.telescope_instrument),
      expression: "search.telescope_instrument"
    }],
    staticClass: "form-control",
    attrs: {
      "id": "telescope",
      "name": "telescope[]",
      "multiple": "",
      "size": "10"
    },
    on: {
      "change": function($event) {
        var $$selectedVal = Array.prototype.filter.call($event.target.options, function(o) {
          return o.selected
        }).map(function(o) {
          var val = "_value" in o ? o._value : o.value;
          return val
        });
        _vm.search.telescope_instrument = $event.target.multiple ? $$selectedVal : $$selectedVal[0]
      }
    }
  }, _vm._l((_vm.telescopes), function(tel) {
    return _c('option', {
      attrs: {
        "value": ""
      },
      domProps: {
        "value": tel[0] + ',' + tel[1]
      }
    }, [_vm._v(_vm._s(tel[0]) + " + " + _vm._s(tel[1]))])
  }))])])])])])])])]) : _vm._e()]), _vm._v(" "), _c('div', {
    staticClass: "code-view"
  }, [_c('pre', {
    staticClass: "code"
  }, [_vm._v(_vm._s(_vm.code))])]), _vm._v(" "), _c('div', {
    staticClass: "modal fade",
    attrs: {
      "id": "search-modal",
      "tabindex": "-1",
      "role": "dialog",
      "aria-labelledby": "searchModelLabel"
    }
  }, [_c('div', {
    staticClass: "modal-dialog",
    attrs: {
      "role": "document"
    }
  }, [_c('div', {
    staticClass: "modal-content"
  }, [_c('div', {
    staticClass: "modal-header"
  }, [_c('button', {
    staticClass: "close",
    attrs: {
      "type": "button",
      "data-dismiss": "modal",
      "aria-label": "Close"
    },
    on: {
      "click": _vm.closeModal
    }
  }, [_c('span', {
    attrs: {
      "aria-hidden": "true"
    }
  }, [_vm._v("×")])]), _vm._v(" "), _c('h4', {
    staticClass: "modal-title",
    attrs: {
      "id": "myModalLabel"
    }
  }, [_vm._v(_vm._s(_vm.modalTitle))])]), _vm._v(" "), _c('div', {
    staticClass: "modal-body",
    domProps: {
      "innerHTML": _vm._s(_vm.modalBody)
    }
  }), _vm._v(" "), _c('div', {
    staticClass: "modal-footer"
  }, [_c('button', {
    staticClass: "btn btn-default",
    attrs: {
      "type": "button",
      "data-dismiss": "modal"
    },
    on: {
      "click": _vm.closeModal
    }
  }, [_vm._v("Close")])])])])])], 1)
},staticRenderFns: []}
module.exports.render._withStripped = true
if (false) {
  module.hot.accept()
  if (module.hot.data) {
     require("vue-hot-reload-api").rerender("data-v-b46fd354", module.exports)
  }
}

/***/ }),
/* 13 */
/***/ (function(module, exports, __webpack_require__) {

var disposed = false
var Component = __webpack_require__(1)(
  /* script */
  __webpack_require__(14),
  /* template */
  __webpack_require__(16),
  /* styles */
  null,
  /* scopeId */
  null,
  /* moduleIdentifier (server only) */
  null
)
Component.options.__file = "/Users/ppeterson/Workspace/dev-env/mars/marssite/portal/vue/Results.vue"
if (Component.esModule && Object.keys(Component.esModule).some(function (key) {return key !== "default" && key.substr(0, 2) !== "__"})) {console.error("named exports are not supported in *.vue files.")}
if (Component.options.functional) {console.error("[vue-loader] Results.vue: functional components are not supported with templates, they should use render functions.")}

/* hot reload */
if (false) {(function () {
  var hotAPI = require("vue-hot-reload-api")
  hotAPI.install(require("vue"), false)
  if (!hotAPI.compatible) return
  module.hot.accept()
  if (!module.hot.data) {
    hotAPI.createRecord("data-v-17073438", Component.options)
  } else {
    hotAPI.reload("data-v-17073438", Component.options)
  }
  module.hot.dispose(function (data) {
    disposed = true
  })
})()}

module.exports = Component.exports


/***/ }),
/* 14 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__js_results_coffee__ = __webpack_require__(15);
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//



/* harmony default export */ __webpack_exports__["default"] = (__WEBPACK_IMPORTED_MODULE_0__js_results_coffee__["a" /* default */]);

/***/ }),
/* 15 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_vue__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_vue___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_vue__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__mixins_coffee__ = __webpack_require__(4);

/*
Author: Peter Peterson
Date: 2017-06-09
Description: Serves functionality for displaying and filtering result sets
Original file: results.coffee
 */
var config;






/*
  Helper functions
 */

Number.prototype.pad = function(size, char) {
  var s;
  if (char == null) {
    char = '0';
  }
  s = String(this);
  while (s.length < (size || 2)) {
    s = "0" + s;
  }
  return s;
};


/*
   Vue components
 */

__WEBPACK_IMPORTED_MODULE_0_vue___default.a.component("table-header", {
  props: ['name'],
  template: "<span>{{ name }}</span>"
});

__WEBPACK_IMPORTED_MODULE_0_vue___default.a.component("table-cell", {
  props: ['data', 'field'],
  template: "<td v-if='data' v-bind:rel='field'>{{ format }}</td><td class='empty' v-else></td>",
  computed: {
    format: function() {
      var d, dateStr;
      if (this.data === null) {
        return this.data;
      }
      if (this.field === 'obs_date' || this.field === 'release_date') {
        try {
          d = moment(this.data);
          dateStr = d.format("YYYY-MM-DD");
          return dateStr;
        } catch (error) {
          return this.data;
        }
      } else {
        return this.data;
      }
    }
  }
});

__WEBPACK_IMPORTED_MODULE_0_vue___default.a.component("table-row", {
  props: ['row', 'cols'],
  template: "<tr v-on:click='selectRow' v-bind:class='{selected:isSelected}'><td class='select-row'><input type='checkbox' name='' v-bind:checked='isSelected' v-bind:name='row.reference'></td><table-cell v-for='vis in cols' v-bind:data='row[vis.mapping]' v-bind:field='vis.mapping' :key='row.id'></table-cell></tr>",
  data: function() {
    return {
      isSelected: false
    };
  },
  created: function() {
    console.log('created');
    return bus.$on("toggleSelected", (function(_this) {
      return function(onoff) {
        console.log("Gettin' toggled", onoff);
        return _this.isSelected = onoff;
      };
    })(this));
  },
  methods: {
    selectRow: function() {
      this.isSelected = !this.isSelected;
      console.log("Row selected");
      bus.$emit("rowselected", {
        stuff: 'hi',
        thing: this.row
      });
      return this.$emit("rowselected", this);
    }
  }
});

__WEBPACK_IMPORTED_MODULE_0_vue___default.a.component("table-body", {
  props: ['data', 'visibleCols'],
  template: "<tbody ><table-row v-for='(item,idx) in data' v-bind:cols='visibleCols' v-bind:row='item' :key='item.id'></table-row></tbody>",
  methods: {
    iheardthat: function() {
      console.log("I heard that");
      return console.log(arguments);
    }
  }
});


/*
   App - Results
 */

config = __WEBPACK_IMPORTED_MODULE_1__mixins_coffee__["a" /* default */].config;

window.bus = new __WEBPACK_IMPORTED_MODULE_0_vue___default.a();

/* harmony default export */ __webpack_exports__["a"] = ({
  props: ['componentData'],
  mixins: [__WEBPACK_IMPORTED_MODULE_1__mixins_coffee__["a" /* default */].mixin],
  data: function() {
    return {
      visibleColumns: [],
      allColumns: config.allColumns,
      visible: false,
      pageNum: 1,
      isLoading: false,
      recordsFrom: 1,
      recordsTo: 100,
      results: [],
      selected: [],
      searchObj: JSON.parse(localStorage.getItem('search')),
      totalItems: 0,
      toggle: false,
      error: ""
    };
  },
  methods: {
    toggleColumn: function(column) {
      var col, first, found, i, j, last, len, len1, n, ref, ref1;
      if (column.checked) {
        ref = this.visibleColumns;
        for (n = i = 0, len = ref.length; i < len; n = ++i) {
          col = ref[n];
          if (_.isEqual(col, column)) {
            this.visibleColumns.splice(n, 1);
          }
        }
      } else {
        found = false;
        ref1 = this.visibleColumns;
        for (n = j = 0, len1 = ref1.length; j < len1; n = ++j) {
          col = ref1[n];
          if (column.num < col.num) {
            first = this.visibleColumns.slice(0, n);
            last = this.visibleColumns.slice(n);
            this.visibleColumns = first.concat(column, last);
            found = true;
            break;
          }
        }
        if (found !== true) {
          this.visibleColumns.push(column);
        }
      }
      return column.checked = !column.checked;
    },
    toggleResults: function() {
      this.toggle = !this.toggle;
      console.log("toggle");
      return bus.$emit("toggleSelected", this.toggle);
    },
    displayForm: function() {
      window.location.hash = "#search_again";
      return this.$emit("displayform", ["search", JSON.parse(localStorage.getItem('search'))]);
    },
    handleError: function(e) {
      return console.log("There was an error", e);
    },
    pageNext: function() {
      return this.pageTo(this.pageNum + 1);
    },
    pageBack: function() {
      return this.pageTo(this.pageNum - 1);
    },
    pageTo: function(page) {
      var self;
      this.pageNum = page;
      localStorage.setItem('currentPage', page);
      this.$emit("pageto", page);
      this.isLoading = true;
      self = this;
      return this.submitForm(null, "paging", function(data) {
        self.isLoading = false;
        self.results = data;
        self.recordsFrom = data.meta.to_here_count - data.meta.page_result_count + 1;
        return self.recordsTo = data.meta.to_here_count;
      });
    }
  },
  created: function() {
    var col, i, len, ref, results;
    ref = this.allColumns;
    results = [];
    for (i = 0, len = ref.length; i < len; i++) {
      col = ref[i];
      if (col.checked) {
        results.push(this.visibleColumns.push(col));
      } else {
        results.push(void 0);
      }
    }
    return results;
  },
  mounted: function() {
    var e, ref;
    window.base.bindEvents();
    window.results = this;
    bus.$on("rowselected", function(data) {
      console.dir(data);
      return console.log("bus called");
    });
    if (window.location.hash === "#query") {
      try {
        this.results = JSON.parse(localStorage.getItem('results')) || [];
        this.totalItems = (ref = this.results) != null ? ref.meta.total_count : void 0;
        this.visible = true;
        return this.pageNum = parseInt(localStorage.getItem("currentPage"));
      } catch (error) {
        e = error;
        this.results = [];
        this.totalItems = 0;
        this.visible = true;
        this.error = "There was an error parsing results from server";
        return this.handleError(e);
      }
    }
  }
});


/***/ }),
/* 16 */
/***/ (function(module, exports, __webpack_require__) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('div', {
    attrs: {
      "id": "query-results"
    }
  }, [_c('transition', {
    attrs: {
      "name": "fade"
    }
  }, [(_vm.visible) ? _c('div', [_c('div', {
    staticClass: "container"
  }, [_c('div', {
    staticClass: "row heading"
  }, [_c('div', {
    staticClass: "col-xs-10"
  }, [_c('h2', {
    staticClass: "text-warn"
  }, [_vm._v("Query returned "), _c('em', [_vm._v(_vm._s(_vm.totalItems))]), _vm._v(" records")])]), _vm._v(" "), _c('div', {
    staticClass: "col-xs-2 text-right"
  }, [_c('button', {
    staticClass: "btn btn-primary",
    on: {
      "click": _vm.displayForm
    }
  }, [_vm._v("Search Again")])])]), _vm._v(" "), _c('div', {
    staticClass: "row results-controls"
  }, [_c('div', {
    staticClass: "col-sm-5"
  }, [_c('button', {
    staticClass: "btn-link btn page-prev",
    on: {
      "click": _vm.pageBack
    }
  }, [_vm._v("Prev")]), _vm._v(" "), _c('span', {
    staticClass: "page-num"
  }, [_vm._v(_vm._s(_vm.pageNum))]), _vm._v(" "), _c('button', {
    staticClass: "btn-link btn page-next",
    on: {
      "click": _vm.pageNext
    }
  }, [_vm._v("Next")]), _vm._v(" "), _c('span', {
    staticClass: "records-from"
  }, [_vm._v(_vm._s(_vm.recordsFrom))]), _vm._v(" to "), _c('span', {
    staticClass: "records-to"
  }, [_vm._v(_vm._s(_vm.recordsTo))]), _vm._v(" "), (_vm.isLoading) ? _c('span', {
    staticClass: "fa fa-spinner fa-spin fa-1x fa-fw"
  }) : _vm._e()]), _vm._v(" "), _c('div', {
    staticClass: "col-sm-7 "
  })]), _vm._v(" "), _c('div', {
    staticClass: "row table-filters"
  }), _vm._v(" "), _c('hr')]), _vm._v(" "), _c('div', {
    staticClass: "container"
  }, [_c('div', {
    staticClass: "row"
  }, [_c('div', {
    staticClass: "col-xs-12 results-wrapper"
  }, [_c('div', {
    staticClass: "filters panel"
  }, [_c('div', {
    staticClass: "panel-body"
  }, [_c('h4', [_vm._v("Toggle visibility of columns")]), _vm._v(" "), _c('ul', {
    staticClass: "list-unstyled columns"
  }, _vm._l((_vm.allColumns), function(column) {
    return _c('li', [_c('label', [_c('input', {
      attrs: {
        "name": "",
        "type": "checkbox",
        "value": "",
        "name": column.mapping
      },
      domProps: {
        "checked": column.checked
      },
      on: {
        "change": function($event) {
          _vm.toggleColumn(column)
        }
      }
    }), _vm._v(" " + _vm._s(column.name))])])
  }))])]), _vm._v(" "), _c('div', [_c('label', [_c('input', {
    attrs: {
      "name": "",
      "type": "checkbox",
      "value": ""
    },
    on: {
      "change": _vm.toggleResults
    }
  }), _vm._v(" Select all")])]), _vm._v(" "), ((_vm.results.resultset.length > 0)) ? _c('table', {
    staticClass: "results"
  }, [_c('thead', [_c('tr', [_c('th', [_vm._v("Selected")]), _vm._v(" "), _vm._l((_vm.visibleColumns), function(col) {
    return _c('th', [_c("table-header", {
      tag: "span",
      attrs: {
        "name": col.name
      }
    })])
  })], 2)]), _vm._v(" "), _c("table-body", {
    tag: "tbody",
    attrs: {
      "data": _vm.results.resultset,
      "visible-cols": _vm.visibleColumns
    }
  }), _vm._v(" "), _c('tfoot')], 1) : _c('div', [_c('h1', {
    staticClass: "text-center"
  }, [_vm._v("No results found")]), _vm._v(" "), (_vm.error) ? _c('div', {
    staticClass: "alert alert-danger text-center"
  }, [_vm._v(_vm._s(_vm.error))]) : _vm._e(), _vm._v(" "), _c('pre', {
    staticClass: "code"
  }, [_vm._v(_vm._s(_vm.searchObj) + "\n                      ")]), _vm._v(" "), _c('div', {
    staticClass: "text-center"
  }, [_c('h5', [_vm._v("You might try and adjust your paramaters and search again")]), _vm._v(" "), _c('button', {
    staticClass: "btn btn-success",
    on: {
      "click": _vm.displayForm
    }
  }, [_vm._v("Adjust Paramaters")])])])])])])]) : _vm._e()])], 1)
},staticRenderFns: []}
module.exports.render._withStripped = true
if (false) {
  module.hot.accept()
  if (module.hot.data) {
     require("vue-hot-reload-api").rerender("data-v-17073438", module.exports)
  }
}

/***/ })
],[6]);