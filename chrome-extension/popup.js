var background_script = chrome.extension.getBackgroundPage();

function onWindowLoad() {
  const checkbox = document.querySelector('#autoCheck')
  const checkbutton = document.querySelector('#checkButton')
  let checked
  try{
    checked = localStorage.getItem("autoRun")
    checkbox.checked = checked == 'true'
    background_script.RUN = checkbox.checked
  } catch (error){
    //Don't care if it fails, means it should be false anyway
  }
  checkbox.addEventListener("click", () =>{
    localStorage.setItem('autoRun',checkbox.checked)
    background_script.RUN = checkbox.checked
  })
  checkbutton.addEventListener("click", () =>{
    chrome.tabs.executeScript(null, {
      file: "getPagesSource.js",
    });
  })
}

window.onload = onWindowLoad;
