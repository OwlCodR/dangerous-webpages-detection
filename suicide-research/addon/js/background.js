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
            getCount('Python')
        }
    });
}

function getCount(word) {
    $.ajax({
        type: "POST",
        url: "python/get_count.py",
        data: { 
            param1: localStorage['page'],
            param2: word
        },
        success: function (response) {
            console.log(response);
        }
    }).done(function(data) {
        console.log(data);
    });
}