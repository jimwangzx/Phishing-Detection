function log(message) {
  console.log(message);
}
const SERVER_URL = "http://3.139.57.29/";


var RUN = localStorage.getItem("autoRun") == 'true';

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action == "scrapeLinks") {
    let urls = request.source;
    console.log(urls)
    let response;
    try {
      fetch(SERVER_URL + "/multi-predict", {
        method: "post",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(urls),
      }).then(response => {
        return response.json();
      }).then(data => {
        // localStorage.setItem("results", data)
        sendResponse({res: data})
      }); 
    } catch (error) {
      log(error);
    }
  }
});

chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
  if ((changeInfo.status == 'complete') && tab.active && RUN){
    if (tab.url.startsWith("http")){
      chrome.tabs.executeScript(null, {
        file: "getPagesSource.js",
      });
    }
  }
})
