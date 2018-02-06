/*
Author: Peter Peterson
Date: 2017-06-09
Description: Serves functionality for submitting and displaying archive query forms/results
*/

//import Vue from 'vue';
import Vue from "vue";
import VeeValidate, {Validator} from "vee-validate";
import Shared from "./mixins.js";

import ModalComponent from "../vue/ModalComponent.vue";
import ScrollWatcher from "./scrollwatcher.js";

var config = Shared.config;

const validateDependsOn = {
  getMessage(field, params, data){
    const id = params[0].replace("#", "");
    const dependsOn = document.querySelector(`label[for=${id}]`).innerText;
    return (data && data.message) || `This field depends on ${dependsOn}`;
  },
  validate(value, args){
    return (document.querySelector(args[0]).value !== "");
  }
};

// Self executing setup
(function(){
  // This gets called after the component has been mounted
  window.addEventListener('searchLoaded', function(e){
    console.log("Search loaded", e);
    // re-bind since the template will render after the page is loaded.
    return window.base.bindEvents();
  });
  Validator.extend('dependson', validateDependsOn);
  const validation = new Validator({dependant:"dependson"});
  // Use vee-validate, and assign before component is loaded
  Vue.use(VeeValidate, config.validatorConfig); // validation plugin
})();

// Date mappinng info for handling dynamic fields and their
// related data models
const dateLookup = {
      "obs-date": {
        "field" : "obs_date",
        "index" : 0
      },
      "obs-date-max": {
        "field" : 'obs_date',
        "index" : 1
      },
      "release-date": {
        "field": "release_date",
        "index": 0
      },
      "release-date-max":{
        "field": "release_date",
        "index": 1
      },
      "parent":{
        "obj": this
      }
};

// Vue component
var Search;
export default Search = {
  mixins: [Shared.mixin],
  components: {
    ModalComponent
  },
  created(){
    this.getTelescopes();
  },
  mounted(){
    // check if this is a new search
    if (window.search_again) {
      const oldSearch = JSON.parse(localStorage.getItem("searchData"));
      this.search = oldSearch;
      window.search_again = false;
    } else if (window.location.hash.indexOf("query") > -1) {
      this.$emit("displayform", ["results", []]);
    }
    window.base.bindEvents();

    document.onscroll = ScrollWatcher;

    $("input.date").datepicker({
            changeMonth: true,
            changeYear: true,
            onSelect: (dateText, datePicker)=> {
              const fieldName = datePicker.input[0].name;
              const field = this.search[dateLookup[fieldName].field];
              field[dateLookup[fieldName].index] = dateText;
              const e = new CustomEvent("datechanged", {'detail':{'date':dateText} });
              document.dispatchEvent(e);
              // this value is updated to force the computed values to refresh
              // for the code sample view
              return this.code = new Date().getTime();
            }
              //nothing = this.code
      });
    $("input.date").datepicker("option", "dateFormat", "yy-mm-dd");

    // for debugging/testing in the browser
    window.searchVue = this;

    // Datepicker doesn't trigger change in the model data, so...
    // bind to datepicker changes
    document.addEventListener("datechanged", ()=> console.log("update code view"));
  },

  computed: {
    hasFiltersSelected: {
      get(){
        return (this.search.image_filter.length > 0);
      }
    },
    hasTelescopeSelected: {
      get(){
        return (this.search.telescope_instrument.length > 0);
      }
    },
    code: {
      get(){
        this.codeView = JSON.stringify(this.stripData(), null, 2);
        return this.codeView;
      },
      set(update){
        // for some reason, the code view won't update unless we go through this mess
        this.codeUpdate = update;
        this.codeView = JSON.stringify(this.stripData(), null, 2);
        return null;
      }
    }
  },
  data(){
    return {
      url                      : config.apiUrl,
      visible                  : true,
      loading                  : false,
      codeUpdate               : 0,
      codeView                 : "",
      loadingMessage           : "Sweeping up star dust...",
      objectName               : "",
      search                   : JSON.parse(JSON.stringify(config.formData)), // deep copy
      showExposureMax          : false,
      showObsDateMax           : false,
      showReleaseDateMax       : false,
      showBothExposureFields   : false,
      showBothObsDateFields    : false,
      showBothReleaseDateFields: false,
      resolvingObject          : false,
      telescopes               : [],
      relatedSplitFieldFlags   : {
        "exposure_time":
          {"fieldFlag":'showExposureMax', "bothFieldFlag":"showBothExposureFields"},
        "obs_date":
          {"fieldFlag":"showObsDateMax", "bothFieldFlag":"showBothObsDateFields"},
        "release_date":
          {"fieldFlag":"showReleaseDateMax","bothFieldFlag":"showBothReleaseDateFields"}
      },
      option                    : {
        format: 'YYYY-MM-DD'
      }
    };
  },

  methods: {
    newSearch(){
      // clear current search and storage
      this.search = JSON.parse(JSON.stringify(this.config.formData));
      localStorage.setItem("searchData", JSON.stringify(this.search));
    },
    clearFilterSelection(){
      this.search.image_filter = [];
    },
    clearTelescopeSelection(){
      this.search.telescope_instrument = [];
    },
    /*
     * Gets the telescope list from the server
     *
     * returns promise object
     */
    getTelescopes(nocache){
      return new Promise((resolve, reject)=>{
        // check if we have a cached set to use
        let telescopes = JSON.parse(localStorage.getItem("telescopes")||"0");
        const self = this;
        const now = moment();
        if (!nocache && telescopes && (moment(telescopes != null ? telescopes.expires : undefined) > now)) {
          self.telescopes = telescopes.telescopes;
          resolve(self.telescopes);
        } else {
          var url = "//" + window.location.hostname;
          console.log("fetching telescopes");
          if( window.testing ){
            url += ":8000/dal/ti-pairs/";
          }else{
            url += ":"+window.location.port+"/dal/ti-pairs/";
          }
          Ajax({
            url   : url,
            method: "get",
            accept: "json"
          }).then(
            // resolve
            (data)=>{
              console.log("Got Telescopes", data);
              self.telescopes = data;
              telescopes = {
                expires: moment().add(7,'days'),
                telescopes: data
              };
              localStorage.setItem("telescopes", JSON.stringify(telescopes));
              resolve(data);
            },
            // reject
            (err)=>{
              console.error("failed");
              reject(err);
            }
          );// end Ajax
        }
      });// end promise

    },
    resolveObject(event){
      event.preventDefault();
      return new Promise((resolve, reject)=>{
        // get the object name
        this.resolvingObject = true;
        self = this;
        var url = window.location.origin+"/dal/object-lookup/?object_name="+encodeURIComponent(this.objectName);
        if( window.testing ){
          url = "//localhost:8000/dal/object-lookup/?object_name="+encodeURIComponent(this.objectName);
        }
        Ajax({
          url: url,
          method: "get",
          accept: "json"
        }).then(
          (data)=>{
            self.search.coordinates.ra = data.ra;
            self.search.coordinates.dec = data.dec;
            self.resolvingObject = false;
            resolve(data);
          },
          (err)=>{
            self.resolvingObject = false;
            console.dir(err.xhr);
            if(err.xhr.response.errorMessage){
              var modalTitle = "Couldn't find that object";
              var modalBody = "<div class='alert alert-danger'><strong>" + err.xhr.response.errorMessage + "</strong></div>";
              window.bus.$emit("open-modal", {title: modalTitle, body: modalBody});
            }
          }
        );
      });
    },
    splitSelection(val){
      // for toggling conditional form inputs, one and sometimes both
      const fieldFlag = this.relatedSplitFieldFlags[val]['fieldFlag'];
      const bothFlag = this.relatedSplitFieldFlags[val]['bothFieldFlag'];

      if ((this.search[val][2] === "(]") || (this.search[val][2] === "[]")) {
        this[fieldFlag] = true;
      } else {
        this[fieldFlag] = false;
      }

      if (this.search[val][2] === "[]") {
        return this[bothFlag] = true;
      } else {
        return this[bothFlag] = false;
      }
    },
    toggleCodeView(event){
      event.preventDefault();
      var cv = document.querySelector(".code-view");
      if( cv.offsetLeft < 0){
        cv.style.left = "0px";
      }else{
        cv.style.left = "-450px";
      }
      return false;
    }
    }

};
