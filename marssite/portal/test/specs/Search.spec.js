import Vue from 'vue';
import Search from '../../vue/Search.vue';

Vue.config.productionTip = false;

var moment = require("moment");
var _ = require("lodash");

// jquery is required as it's used for the calendar widget
window.$ = window.jQuery = require('jquery');
require('jquery-ui');

window.moment = moment;
window._ = _;

// this is necessary to have ajax calls go to the right place
window.testing = true;

require('../../../theme/js/main.js');

function createVM(){
  var el = document.createElement("div");
  el.setAttribute("id", "mount");
  document.body.appendChild(el);


  return new Vue({
    template:"<div><h1>Testing...</h1><search></search></div>",
    components: {'search':Search}
  }).$mount("#mount");

}


describe('Search component should mount', function(){
  before(function(){
    this.server = sinon.fakeServer.create();
    this.server.autoRespond = true;

    this.server.respondWith("GET", /ti-pairs/, [
        200,
        { "Content-Type": "application/json" },
        "[\"soar,spartan\",\"ct4m,decam\",\"ct4m,mosaic\",\"soar,goodman\"]"
      ]);
    this.vm = createVM();
  });

  it('Should mount without issue', function(){
    expect(typeof this.vm.$children[0].getTelescopes).to.equal('function');
  });

  it('Should have an $el element',function(){
    assert.property(this.vm, '$el');
  });

  it('should have some telescopes', function(){
    // pass true to getTelescopes to prevent it fetching from cache
    this.vm.$children[0].getTelescopes(true);
    assert.lengthOf(this.vm.$children[0].telescopes, 4, 'Has 4 telescopes');
  });
});

describe('Object lookup should populate or fail gracefully', function(){
  before(function(){
    this.server = sinon.fakeServer.create();
    this.server.autoRespond = true;
    this.server.respondWith("GET", /object-lookup/, [
      200,
      {"Content-Type":"application/json"},
      "{\"ra\":432.1, \"dec\":234.5}"
    ]);

    this.vm = createVM();
  });

  it("Should return an ra,dec from an object", function(){
    var event = new MouseEvent("click");
    this.vm.$children[0].objectName = "orion";
    this.vm.$children[0].resolveObject(event).then((data)=>{
      data.should.have.property('ra').to.equal(432.1);
    });
  });
});


describe('Date range fields should react appropriately', function(){
  before(function(){
    this.vm = createVM();
    // select a range then check to see if showBothObsDateFields is true...
    var range = this.vm.$el.querySelector("[name=obs-date-interval]");
    range.selectedIndex = 3;
    var evt = document.createEvent("HTMLEvents");
    evt.initEvent("change", false, true);
    range.dispatchEvent(evt);
  });

  // check to make sure the display of both fields is working properly
  it("should have both fields showing", function(){
    expect(this.vm.$children[0].showBothObsDateFields).to.equal(true);
    var visible = document.querySelector("#obs-date-max").style.display;
    expect(visible).to.equal("none");
  });
});
