###
Author: Peter Peterson
Date: 2017-07-24
Description: Code for interactions with the staging page
Original file: staging.coffee
###

import Shared from './mixins.coffee'
import Vue from 'vue'


generateResultsSet = ()->
  results = []
  for x in [1..100]
    results.push {count:x, filename: Math.random().toString(36).substring(7)}

  return results

stagingComponent = {
  mixins:[Shared.mixin]
  data: ()->
      return
        stagingAllFiles: false
        loading: false
        selectAll: false
        results: []
        selected: []

  created: ()->
    window.staging = @
    console.log "Staging created"
  mounted: ()->
    console.log "Component mounted"
    window.base.bindEvents()
    if localStorage.getItem("stage") is "selectedFiles"
      # Files array is generated by the staging django template
      files = JSON.parse(localStorage.getItem("selectedFiles"))
      for file in files
        @results.push {'selected':false, 'file':file}
    else
      # show a loading screen
      @stagingAllFiles = true
      @loading = true
      querydata = localStorage.getItem("searchData")

      
      new Ajax
        url: "/portal/stageall/"
        method: "post"
        accept: "json"
        data: {searchData:JSON.parse(querydata)}
        success: (data)=>
          console.log "got this data back from the request"
          console.log data
          @loading = false
        fail: (statusMsg, status, xhr)->
          console.log "ajax failed"


      # call api to start staging process...

  methods:
    toggleAll:()->
      @selectAll = !@selectAll
      if @selectAll
        for file in @results
          file.selected = true
          @selected.push(file)
      else
        for file in @results
          file.selected = false
        @selected = []

    downloadSingleFile: (file, event)->
      # identify which file...
      event.stopPropagation()
      window.open("/portal/downloadsinglefile/?f="+file.reference, "_blank")
      return false # prevent bubbling up

    _confirmDownloadSelected: ()->
      selected = @selected # scope resolution
      query = {"files":selected.slice(0, 10)}
      form = document.createElement("form")
      form.setAttribute("method", "post")
      #form.setAttribute("target", "_blank")
      form.setAttribute("action", "/portal/downloadselected")
      data = document.createElement("input")
      data.setAttribute("type", "hidden")
      data.setAttribute("name", "selected")
      data.setAttribute("value", JSON.stringify(selected.slice(0,10)))
      form.appendChild(data)
      document.querySelector("body").appendChild(form)
      form.submit()
      ###
      new Ajax
        url: "/portal/downloadselected"
        method: "post"
        accept: "json"
        data: query
        success: (data)=>
          console.log "Got this from the server"
          console.log data
        fail: (statusmsg, status, xhr)->
          console.log "request failed"
      ###    


    downloadSelected: ()->
      console.log "downloading selected"
      self = @
      if @selected.length > 10
        BootstrapDialog.confirm("Only ten files can be downloaded at one time. See download instructions for downloading more at one time",
        (goAhead)->
           if goAhead
            self._confirmDownloadSelected()
        )
      else
        self._confirmDownloadSelected()


    toggleSelected:(item)->
      item.selected = !item.selected
      if item.selected
        @selected.push(item)
      else
        indx = _.indexOf(@selected, item)
        @selected.splice(indx, 1)

}


export default stagingComponent