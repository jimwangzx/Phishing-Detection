
function getLinks(document_root) {
  let aTags = []
  let urls = document.querySelectorAll('a')
  for (url in urls){
    aTags.push(urls[url].href)
  }
  return aTags
}

function handleResponse(res) {
  console.log(res.res)
}

function handleError(err) {
  console.error(err)
}

(function(){
  console.log("here")
  let message = chrome.runtime.sendMessage({
    action: "scrapeLinks",
    source: getLinks(document)
  })
  console.log(message)
  //message.then(handleResponse, handleError);
})()
