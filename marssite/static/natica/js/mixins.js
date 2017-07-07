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
  defaultColumns: [
    {
      "mapping": "dec",
      "name": "Dec"
    }, {
      "mapping": "depth",
      "name": "Depth"
    }, {
      "mapping": "exposure",
      "name": "Exposure"
    }, {
      "mapping": "filename",
      "name": "Filename"
    }, {
      "mapping": "filesize",
      "name": "File size"
    }, {
      "mapping": "filter",
      "name": "Filter"
    }, {
      "mapping": "image_type",
      "name": "Image Type"
    }, {
      "mapping": "instrument",
      "name": "Instrument"
    }, {
      "mapping": "md5sum",
      "name": "MD5 sum"
    }, {
      "mapping": "obs_date",
      "name": "Observed date"
    }, {
      "mapping": "original_filename",
      "name": "Original filename"
    }, {
      "mapping": "pi",
      "name": "Principle Investigator"
    }, {
      "mapping": "product",
      "name": "Product"
    }, {
      "mapping": "prop_id",
      "name": "Program Number"
    }, {
      "mapping": "ra",
      "name": "RA"
    }, {
      "mapping": "reference",
      "name": "Reference"
    }, {
      "mapping": "release_date",
      "name": "Release Date"
    }, {
      "mapping": "seeing",
      "name": "Seeing"
    }, {
      "mapping": "telescope",
      "name": "Telescope"
    }, {
      "mapping": "survey_id",
      "name": "Survey Id"
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

export default {
  config: _config,
  mixin: {
    data: function() {
      return {
        config: _config
      };
    },
    methods: {
      submitForm: function(event, paging, cb) {
        var key, message, msgs, newFormData, page, ref, search, self, url;
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
        } else {
          page = localStorage.getItem("currentPage");
        }
        newFormData = this.search ? JSON.parse(JSON.stringify(this.search)) : JSON.parse(localStorage.getItem("search"));
        search = newFormData;
        localStorage.setItem('search', JSON.stringify(search));
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
        if ((ref = newFormData.coordinates) != null ? ref.ra : void 0) {
          newFormData.coordinates.ra = parseFloat(newFormData.coordinates.ra);
          newFormData.coordinates.dec = parseFloat(newFormData.coordinates.dec);
        }
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
            window.location.hash = "#query";
            self.loading = false;
            localStorage.setItem('results', JSON.stringify(data));
            self.$emit("displayform", ["results", data]);
            if (cb) {
              return cb(data);
            }
          }
        }).send();
      }
    }
  }
};