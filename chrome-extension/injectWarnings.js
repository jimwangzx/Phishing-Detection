function injectProblems(item){
  data = item.data
  aTags = document.querySelectorAll("a")
  i = 0
  for(key in data){
    i++
  }
  aTags.forEach(tag => {
    for(key in data){
      if (tag.href == key){
        if (data[key]){
          let parent = tag.parentElement
          let warning = document.createElement("P")
          warning.innerHTML = "WARNING may be an unsafe link"
          warning.style.color = "red"
          parent.insertBefore(warning,tag)
        }
      }
    }
  })
}


try {
  chrome.storage.local.get(["data"], injectProblems);

} catch(e){
  console.error(e)
}