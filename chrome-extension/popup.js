var bkg = chrome.extension.getBackgroundPage();

chrome.runtime.onMessage.addListener( async function(request, sender) {
  if (request.action == "scrapeLinks") {
    bkg.log(JSON.stringify(request.source))
    //bkg.log(request.source);
  let response;
  try {
    response = await fetch('http://18.222.221.147/8081/test', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(request.source),
    })
    } catch (error) {
      bkg.log(error);
    }
  }
});

function onWindowLoad() {
  chrome.tabs.executeScript(null, {
    file: "getPagesSource.js"
  });
}

window.onload = onWindowLoad;