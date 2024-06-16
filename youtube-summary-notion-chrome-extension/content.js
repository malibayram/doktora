/* chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'summarize') {
    const videoTitle = document.querySelector('h1.title').innerText;
    const videoUrl = window.location.href;
    const videoChannel = document.querySelector('ytd-channel-name a').innerText;
    const videoChannelUrl = document.querySelector('ytd-channel-name a').href;
    const videoUploadDate = document.querySelector('meta[itemprop="uploadDate"]').getAttribute('content');
    const videoDescription = document.querySelector('#description').innerText;

    // Video bilgilerinin özetlenmesi için Gemini API çağrısı
    fetch('https://api.gemini.com/summarize', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer AIzaSyBilToCwJ93UwBjI7r7okqgLr8aFn8Vp1Q'
      },
      body: JSON.stringify({
        text: videoDescription,
        videoUrl: videoUrl,
        title: videoTitle
      })
    })
    .then(response => response.json())
    .then(data => {
      const summary = data.summary.trim();
      const tldr = summary.split('. ').slice(0, 2).join('. ') + '.';
      const keywords = data.keywords;  // Assuming the API returns keywords as well
      sendResponse({ 
        title: videoTitle, 
        url: videoUrl, 
        channelName: videoChannel,
        channelUrl: videoChannelUrl,
        uploadDate: videoUploadDate, 
        summary, 
        tldr, 
        keywords 
      });
    })
    .catch(error => console.error('Error with Gemini:', error));
    return true; // keep the message channel open for sendResponse
  }
});
 */

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'getInfo') {
    const videoTitle = document.querySelector('h1.title').innerText;
    const videoUrl = window.location.href;
    const videoChannel = document.querySelector('ytd-channel-name a').innerText;
    const videoChannelUrl = document.querySelector('ytd-channel-name a').href;
    const videoUploadDate = document.querySelector('meta[itemprop="uploadDate"]').getAttribute('content');
    
    sendResponse({ 
      title: videoTitle, 
      url: videoUrl, 
      channelName: videoChannel,
      channelUrl: videoChannelUrl,
      uploadDate: videoUploadDate 
    });
  }
  
  if (request.action === 'summarize') {
    const videoTitle = document.querySelector('h1.title').innerText;
    const videoDescription = document.querySelector('#description').innerText;

    fetch('https://api.gemini.com/summarize', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer AIzaSyBilToCwJ93UwBjI7r7okqgLr8aFn8Vp1Q'
      },
      body: JSON.stringify({
        text: videoDescription,
        title: videoTitle
      })
    })
    .then(response => response.json())
    .then(data => {
      const summary = data.summary.trim();
      const tldr = summary.split('. ').slice(0, 2).join('. ') + '.';
      const keywords = data.keywords;  // Assuming the API returns keywords as well
      sendResponse({ summary, tldr, keywords });
    })
    .catch(error => console.error('Error with Gemini:', error));
    return true; // keep the message channel open for sendResponse
  }
});
