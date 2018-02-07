/*
Author: Peter Peterson
Date: 2017-06-09
Description: Base functionality/interactions + helper functions
 */
var Ajax, Base, ToggleModal;
  //bind = function (fn, me) { return function () { return fn.apply(me, arguments); }; };

ToggleModal = function (selector) {
  var b, backdrop, body, m;
  m = document.querySelector(selector);
  b = document.querySelector('.modal-backdrop');
  m.style.display = 'block';
  m.classList.toggle('in');
  if (b === null) {
    backdrop = document.createElement('div');
    body = document.querySelector('body');
    backdrop.setAttribute('class', 'modal-backdrop fade in');
    body.appendChild(backdrop);
  } else {
    b.remove();
    m.style.display = 'none';
  }
};

Ajax = function (_opts) {
    return new Promise(function(resolve, reject){
      var settings;
      this.settings = {
        url: window.location.path,
        method: "GET",
        accept: "html",
        data: {},
      };
      settings = _.extend(this.settings, _opts);
      this.settings = settings;
      this.xhr = new XMLHttpRequest();
      this.xhr.open(settings.method.toUpperCase(), settings.url, true);
      this.xhr.onload = function(){
        if( this.status >= 200 && this.status < 300){
          resolve(xhr.response);
        }else{
          console.log("Reponse FOOBARD");
          reject({
            status: this.status,
            statusText: this.statusText,
            xhr: xhr
          });
        }
      };
      this.xhr.onerror = function(){
        reject({
          status: this.status,
          statusText: this.statusText,
          xhr: xhr
        });
      };
      this.xhr.setRequestHeader('Content-Type', 'application/json');
      this.xhr.setRequestHeader('Accept', 'text/html;application/json');
      this.xhr.setRequestHeader('x-mars-ajax-handler', '1.0');
      this.xhr.responseType = settings.accept;
      this.xhr.send(JSON.stringify(settings.data));
    });
};

Base = (function () {
  function Base() {

    /*
    Bind multiple events to one function
    Usage: addMutiEventListener($el, "click blur", function(){})
     */
    var nohup;
    window.addMultiEventListener = function (elem, events, fn) {
      return events.split(' ').forEach(function (e) {
        if (elem.events && elem.events[e]) {
          elem.removeEventListener(e, elem.events[e], false);
        }
        elem.addEventListener(e, fn, false);
        if (!elem.events) {
          elem.events = [];
        }
        return elem.events[e] = fn;
      });
    };
    if (window.location.hostname.indexOf('local') < 0) {
      nohup = function () {
        return "Console commands (log, info, dir, debug) have been mapped into `console.live` in production environments";
      };
      console.live = {
        log: console.log,
        info: console.info,
        dir: console.dir,
        debug: console.debug
      };
      console.debug = nohup;
      console.log = nohup;
      console.info = nohup;
      console.dir = nohup;
      console.live.info("%c " + nohup(), "color: red");
    }
    return "";
  }

  Base.prototype.bindEvents = function () {
    var el, els, i, j, len, len1, results, section, sections, toggle;
    els = document.querySelectorAll("input[type=text],input[type=textarea],input[type=password],input[type=date]");
    for (i = 0, len = els.length; i < len; i++) {
      el = els[i];
      addMultiEventListener(el, 'keyup blur', function (event) {
        var ref, ref1, target, targetId;
        targetId = event.currentTarget.id;
        target = event.currentTarget;
        if (!targetId) {
          return false;
        }
        if (target.value === "") {
          return (ref = document.querySelector("label[for=" + targetId + "].floating")) != null ? ref.classList.remove("open") : void 0;
        } else {
          return (ref1 = document.querySelector("label[for=" + targetId + "].floating")) != null ? ref1.classList.add("open") : void 0;
        }
      });
    }
    sections = document.querySelectorAll(".collapsible");
    results = [];
    for (j = 0, len1 = sections.length; j < len1; j++) {
      section = sections[j];
      toggle = section.querySelector(".section-toggle");
      results.push((function (thisSection) {
        var colsection, fn;
        colsection = thisSection.querySelector(".section-heading");
        fn = function (e) {
          return thisSection.classList.toggle("open");
        };
        if (colsection.clickevent) {
          colsection.removeEventListener("click", colsection.clickevent, false);
        }
        colsection.addEventListener("click", fn, false);
        return colsection.clickevent = fn;
      })(section));
    }
    return results;
  };

  return Base;

})();

window.Ajax = Ajax;
window.base = new Base();

window.base.bindEvents();
