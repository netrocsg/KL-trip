// Suggestions System - localStorage based
function submitSuggestion() {
    const textarea = document.getElementById('suggestion-text');
    const typeSelect = document.getElementById('suggestion-type');
    const statusDiv = document.getElementById('suggestion-status');
    
    const text = textarea.value.trim();
    if (!text || text.length < 10) {
        statusDiv.textContent = 'Please provide more details (at least 10 characters)';
        statusDiv.className = 'suggestion-status error';
        statusDiv.style.display = 'block';
        return;
    }
    
    const suggestion = {
        id: Date.now().toString(),
        timestamp: new Date().toISOString(),
        type: typeSelect.value,
        suggestion: text,
        processed: false
    };
    
    let all = JSON.parse(localStorage.getItem('kl_trip_all_suggestions') || '[]');
    all.push(suggestion);
    localStorage.setItem('kl_trip_all_suggestions', JSON.stringify(all));
    
    statusDiv.textContent = '✅ Suggestion saved! Use the Export button below to download for the agent.';
    statusDiv.className = 'suggestion-status success';
    statusDiv.style.display = 'block';
    textarea.value = '';
}

function exportSuggestions() {
    const all = JSON.parse(localStorage.getItem('kl_trip_all_suggestions') || '[]');
    if (all.length === 0) { alert('No suggestions to export'); return; }
    
    const blob = new Blob([JSON.stringify(all, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `kl-trip-suggestions-${Date.now()}.json`;
    link.click();
    URL.revokeObjectURL(url);
}

document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('submit-suggestion');
    if (btn) btn.addEventListener('click', submitSuggestion);
});
