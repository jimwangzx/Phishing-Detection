let urls

// chrome.runtime.onMessage.addListener(function(request, sender) {
//   if (request.action == "markedURLS") {
//     urls = res.data
//   }
// });
// console.log(urls)
try {
  chrome.storage.sync.get(["data"], function(items){
    console.log(items)
});

} catch(e){
  console.log(e)
}