/* document.getElementById('summarize').addEventListener('click', () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(tabs[0].id, { action: 'summarize' }, (response) => {
      if (response) {
        document.getElementById('summary').innerText = 
          `Title: ${response.title}\n` +
          `YouTube Link: ${response.url}\n` +
          `Channel: ${response.channelName}\n` +
          `Channel Link: ${response.channelUrl}\n` +
          `Uploaded At: ${response.uploadDate}\n` +
          `Watched At: ${new Date().toISOString()}\n` +
          `Keywords: ${response.keywords.join(', ')}\n` +
          `Summary: ${response.summary}\n` +
          `tldr: ${response.tldr}`;
        document.getElementById('sendToNotion').style.display = 'block';
        document.getElementById('sendToNotion').addEventListener('click', () => {
          fetch('https://api.notion.com/v1/pages', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer secret_wYIGVq7PsMfONJNMR2AWnmojPAKzUexPaHTzqT3Yr1Z`
            },
            body: JSON.stringify({
              parent: { database_id: '4ec0e7679a1746dfaf2d62f40266bc91' },
              properties: {
                'Title': { title: [{ text: { content: response.title } }] },
                'YouTube Link': { url: response.url },
                'Channel': { rich_text: [{ text: { content: response.channelName } }] },
                // 'Channel Link': { url: response.channelUrl },
                'Uploaded At': { date: { start: response.uploadDate } },
                'Watched At': { date: { start: new Date().toISOString() } },
                'Keywords': { multi_select: response.keywords.map(keyword => ({ name: keyword })) },
                'Summary': { rich_text: [{ text: { content: response.summary } }] },
                'tldr': { rich_text: [{ text: { content: response.tldr } }] }
              }
            })
          })
          .then(() => alert('Summary added to Notion!'))
          .catch(error => console.error('Error adding to Notion:', error));
        });
      }
    });
  });
});
 */

document.getElementById('getInfo').addEventListener('click', () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(tabs[0].id, { action: 'getInfo' }, (response) => {
      if (response) {
        document.getElementById('info').innerText = 
          `Title: ${response.title}\n` +
          `YouTube Link: ${response.url}\n` +
          `Channel: ${response.channelName}\n` +
          `Channel Link: ${response.channelUrl}\n` +
          `Uploaded At: ${response.uploadDate}`;
        document.getElementById('summarize').style.display = 'block';
      }
    });
  });
});

document.getElementById('summarize').addEventListener('click', () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(tabs[0].id, { action: 'summarize' }, (response) => {
      if (response) {
        document.getElementById('summary').innerText = 
          `Summary: ${response.summary}\n` +
          `tldr: ${response.tldr}`;
        document.getElementById('sendToNotion').style.display = 'block';
      }
    });
  });
});

document.getElementById('sendToNotion').addEventListener('click', () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(tabs[0].id, { action: 'getInfo' }, (response) => {
      if (response) {
        fetch('https://api.notion.com/v1/pages', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer secret_wYIGVq7PsMfONJNMR2AWnmojPAKzUexPaHTzqT3Yr1Z`,
            'Notion-Version': '2022-06-28'
          },
          body: JSON.stringify({
            parent: { database_id: '4ec0e7679a1746dfaf2d62f40266bc91' },
            properties: {
              'Title': { title: [{ text: { content: response.title } }] },
              'YouTube Link': { url: response.url },
              'Channel': { rich_text: [{ text: { content: response.channelName } }] },
              'Channel Link': { url: response.channelUrl },
              'Uploaded At': { date: { start: response.uploadDate } },
              'Watched At': { date: { start: new Date().toISOString() } },
              'Keywords': { multi_select: response.keywords.map(keyword => ({ name: keyword })) },
              'Summary': { rich_text: [{ text: { content: response.summary } }] },
              'tldr': { rich_text: [{ text: { content: response.tldr } }] }
            }
          })
        })
        .then(() => alert('Summary added to Notion!'))
        .catch(error => console.error('Error adding to Notion:', error));
      }
    });
  });
});
