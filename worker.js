importScripts('https://cdn.jsdelivr.net/npm/@huggingface/transformers@3.0.2');

let summarize;

async function init() {
    // Load the summarization pipeline inside the worker thread
    summarize = await pipeline('summarization');
}

// Listen for messages from the main thread
self.onmessage = async (event) => {
    if (event.data === 'init') {
        // Initialize the summarization model
        await init();
        self.postMessage('initialized');
    } else if (event.data.text) {
        // Summarize the text
        const summary = await summarize(event.data.text);
        self.postMessage(summary[0].summary_text);
    }
};
