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
var el = document.createElement("div");
el.setAttribute("id", "mount");
document.body.appendChild(el);

function testSpy(greet, cb){
  cb("hi "+greet);
}

describe('Search component should mount', ()=>{
  before(function(){
    this.server = sinon.fakeServer.create();
    this.server.autoRespond = true;

    this.server.respondWith("GET", "//localhost:8000/dal/ti-pairs/", [
        200,
        { "Content-Type": "application/json" },
        '[{"soar,spartan","ct4m,decam","ct4m,mosaic","soar,goodman"}]'
      ]);
    this.vm = new Vue({
      template:"<div><h1>Testing...</h1><search></search></div>",
      components: {'search':Search}
    }).$mount("#mount");
  });


  it('Should mount without issue', ()=>{
    expect(typeof this.vm.$children[0].getTelescopes).to.equal('function');
  });

  it('Should have an $el element', ()=>{
    assert.property(this.vm, '$el');
  });

  it('should have some telescopes', function(){
    debugger
    assert.lengthOf(this.vm.telescope, 4, 'Has 4 telescopes');
  });
});

describe('Object lookup should populate or fail gracefully', ()=>{
  before(function(){
    this.server = sinon.fakeServer.create();
    this.server.autoRespond = true;
    this.server.respondWith("GET", /object-lookup/, [
      200,
      {"Content-Type":"application/json"},
      "{\"ra\":432.1, \"dec\":234.5}"
    ]);
    this.vm = new Vue({
      template:"<div><h1>Testing...</h1><search></search></div>",
      components: {'search':Search}
   });

  // test codeView, resolvingObject, datepicker, submitForm, submitQuery, clear
  it("Should return an ra,dec from an object", ()=>{
    console.log("called function with spy");
    var event = new MouseEvent("click");
    this.vm.$children[0].objectName = "orion";
    this.vm.$children[0].resolveObject(event).then((data)=>{
      data.should.have.property('ra').to.equal(432.1);
    });
    spy.should.have.been.calledWith("hi Person");
  });
});
