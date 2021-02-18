
function getLinks(document_root) {
  let aTags = []
  let urls = document.querySelectorAll('a')
  for (url in urls){
    aTags.push(urls[url].href)
  }
  return aTags
}

chrome.runtime.sendMessage({
  action: "scrapeLinks",
  source: getLinks(document)
});