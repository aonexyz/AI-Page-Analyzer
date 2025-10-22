async function analyze(payload) {
  document.getElementById('status').innerText = 'Analyzing...';
  const resp = await fetch('/api/analyze', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(payload)
  });
  const j = await resp.json();
  document.getElementById('status').innerText = '';
  return j;
}

document.getElementById('analyzeBtn').addEventListener('click', async () => {
  const url = document.getElementById('urlInput').value.trim();
  const text = document.getElementById('textInput').value.trim();
  if (!url && !text) {
    alert('Provide URL or text');
    return;
  }
  const res = await analyze({url, text});
  if (res.error) {
    document.getElementById('status').innerText = 'Error: ' + res.error;
    return;
  }
  const r = res.result;
  // If analyzer returned structured JSON:
  const title = r.title || r.suggested_title || '—';
  const summary = r.summary || r.final_summary || r.raw || 'No summary';
  const kp = r.key_points || r.key_points || (r.keyPoints ? r.keyPoints : []);
  const tags = r.suggested_tags || r.tags || '';

  document.getElementById('title').innerText = title;
  document.getElementById('summary').innerText = summary;
  const ul = document.getElementById('keyPoints');
  ul.innerHTML = '';
  if (Array.isArray(kp)) {
    kp.slice(0,10).forEach(p => {
      const li = document.createElement('li');
      li.innerText = p;
      ul.appendChild(li);
    });
  } else if (typeof kp === 'string') {
    const li = document.createElement('li'); li.innerText = kp; ul.appendChild(li);
  }

  document.getElementById('tags').innerText = tags;
  document.getElementById('preview').innerText = res.preview || '';
});
