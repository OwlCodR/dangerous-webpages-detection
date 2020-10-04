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
        if (response.method=="getText") {
            console.log(response.data);
            localStorage.setItem('page', response.data);
            find('File')
        }
    });
}

function find(word) {
    let page = localStorage['page'].split(' ');
    
    for (let i = 0; i < page.length; i++) {
        if (page[i].includes(word)) {
            console.log("I have found word");
        }
    }
}