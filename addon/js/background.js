chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
    getText(tabId);
});

chrome.tabs.onCreated.addListener(function(tabId, changeInfo, tab) {
    getText(tabId);
});

function getText(tabId) {
    chrome.tabs.sendMessage(tabId, {method: "getText"}, function(response) {
        if (!response)
            return;
        if (response.method == "getText") {
            console.log(response.data);
            localStorage.setItem('page', response.data);
            sendTextToServer()
        }
    });
}

function sendTextToServer() {
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8080/",
        data: { 
            text: localStorage.getItem(['page'])
        }
    }).done(function(data) {
        console.log(data);
    });
}