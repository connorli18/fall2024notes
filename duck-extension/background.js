// background.js

// Listen for extension installation or updates
chrome.runtime.onInstalled.addListener(() => {
    console.log("Ducklings Playground extension installed!");
});

// Optional: Respond to messages from content scripts
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type === "greet") {
        console.log(`Received message: ${message.greeting}`);
        sendResponse({ response: "Hello from the background script!" });
    }
});
