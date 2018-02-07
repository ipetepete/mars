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

    this.server.respondWith("GET", /ti-pairs/, [
        200,
        { "Content-Type": "application/json" },
        "[\"soar,spartan\",\"ct4m,decam\",\"ct4m,mosaic\",\"soar,goodman\"]"
      ]);

    this.vm = new Vue({
      template:"<div><h1>Testing...</h1><search></search></div>",
      components: {'search':Search}
    }).$mount("#mount");
  });


  it('Should mount without issue', function(){
    debugger
    expect(typeof this.vm.$children[0].getTelescopes).to.equal('function');
  });

  it('Should have an $el element',function(){
    assert.property(this.vm, '$el');
  });

  it('should have some telescopes', function(){
    assert.lengthOf(this.vm.$children[0].telescopes, 4, 'Has 4 telescopes');
  });

  // test codeView, resolvingObject, datepicker, submitForm, submitQuery, clear
  it("Should return an ra,dec from an object", function(){
    var spy = sinon.spy();
    testSpy("Person", spy);
    console.log("called function with spy");
    spy.should.have.been.calledWith("hi Person");
  });
});
