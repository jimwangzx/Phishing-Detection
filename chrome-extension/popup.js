var background_script = chrome.extension.getBackgroundPage();
const SERVER_URL = "http://3.17.188.42/";

chrome.runtime.onMessage.addListener(async function (request, sender) {
  if (request.action == "scrapeLinks") {
    background_script.log(request.source);
    let urls = request.source;
    background_script.log("updated");
    let response;
    try {
      response = await fetch(SERVER_URL + "/multi-predict", {
        method: "post",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(urls),
      });

      background_script.log(response);
    } catch (error) {
      background_script.log(error);
    }
  }
});

function onWindowLoad() {
  chrome.tabs.executeScript(null, {
    file: "getPagesSource.js",
  });
}

window.onload = onWindowLoad;
