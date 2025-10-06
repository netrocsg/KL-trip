// Suggestions System - GitHub Issues based
// Users submit suggestions which create GitHub Issues automatically

async function submitSuggestion() {
    const textarea = document.getElementById('suggestion-text');
    const typeSelect = document.getElementById('suggestion-type');
    const submitBtn = document.getElementById('submit-suggestion');
    const statusDiv = document.getElementById('suggestion-status');
    
    const text = textarea.value.trim();
    const type = typeSelect.value;
    
    // Validation
    if (!text || text.length < 10) {
        showStatus('Please provide more details (at least 10 characters)', 'error');
        return;
    }
    
    // Disable button
    submitBtn.disabled = true;
    submitBtn.textContent = 'Submitting...';
    showStatus('Submitting your suggestion...', 'info');
    
    try {
        // Create GitHub Issue via API
        const issueTitle = `[${type.toUpperCase()}] ${text.substring(0, 60)}${text.length > 60 ? '...' : ''}`;
        const issueBody = `## Suggestion Type
${getTypeEmoji(type)} **${type.charAt(0).toUpperCase() + type.slice(1)}**

## Details
${text}

## Metadata
- **Submitted**: ${new Date().toLocaleString()}
- **Status**: 🔄 Pending Review
- **Processed**: No

---
*This suggestion was submitted via the KL Trip website. The daily AI agent will research this and add it to the activities database.*`;

        const response = await fetch('https://api.github.com/repos/netrocsg/KL-trip/issues', {
            method: 'POST',
            headers: {
                'Accept': 'application/vnd.github.v3+json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                title: issueTitle,
                body: issueBody,
                labels: ['suggestion', type, 'pending']
            })
        });
        
        if (response.ok) {
            const issue = await response.json();
            showStatus(`✅ Suggestion submitted successfully! Track it at: ${issue.html_url}`, 'success');
            textarea.value = '';
            
            // Track locally
            trackSuggestion({
                id: issue.number,
                type: type,
                text: text,
                url: issue.html_url,
                timestamp: new Date().toISOString()
            });
            
        } else {
            // Fallback to localStorage if API fails
            console.warn('GitHub API failed, using localStorage fallback');
            const suggestion = {
                id: Date.now().toString(),
                timestamp: new Date().toISOString(),
                type: type,
                suggestion: text,
                processed: false
            };
            
            let all = JSON.parse(localStorage.getItem('kl_trip_all_suggestions') || '[]');
            all.push(suggestion);
            localStorage.setItem('kl_trip_all_suggestions', JSON.stringify(all));
            
            showStatus('✅ Suggestion saved locally! Please export and share with team lead.', 'success');
            textarea.value = '';
            trackSuggestion(suggestion);
            showExportButton();
        }
        
    } catch (error) {
        console.error('Submission error:', error);
        showStatus('❌ Error submitting. Please try again or contact team lead.', 'error');
    } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = '🚀 Submit Suggestion';
    }
}

function getTypeEmoji(type) {
    const emojis = {
        'food': '🍜',
        'activity': '🎯',
        'accommodation': '🏨',
        'transport': '🚗',
        'other': '💭'
    };
    return emojis[type] || '💡';
}

function showStatus(message, type) {
    const statusDiv = document.getElementById('suggestion-status');
    statusDiv.innerHTML = message;
    statusDiv.className = `suggestion-status ${type}`;
    statusDiv.style.display = 'block';
    
    if (type === 'success') {
        setTimeout(() => {
            statusDiv.style.display = 'none';
        }, 15000);
    }
}

function trackSuggestion(suggestion) {
    const STORAGE_KEY = 'kl_trip_my_suggestions';
    let mySuggestions = [];
    
    try {
        const stored = localStorage.getItem(STORAGE_KEY);
        if (stored) {
            mySuggestions = JSON.parse(stored);
        }
    } catch (e) {
        console.error('Error reading suggestions:', e);
    }
    
    mySuggestions.push({
        id: suggestion.id,
        timestamp: suggestion.timestamp,
        type: suggestion.type,
        text: suggestion.text || suggestion.suggestion,
        url: suggestion.url || null,
        status: 'pending'
    });
    
    localStorage.setItem(STORAGE_KEY, JSON.stringify(mySuggestions));
    updateMySuggestionsList();
}

function updateMySuggestionsList() {
    const listContainer = document.getElementById('my-suggestions-list');
    if (!listContainer) return;
    
    const STORAGE_KEY = 'kl_trip_my_suggestions';
    let mySuggestions = [];
    
    try {
        const stored = localStorage.getItem(STORAGE_KEY);
        if (stored) {
            mySuggestions = JSON.parse(stored);
        }
    } catch (e) {
        console.error('Error reading suggestions:', e);
    }
    
    if (mySuggestions.length === 0) {
        listContainer.innerHTML = '<p style="color: #666; font-style: italic;">No suggestions yet. Be the first to suggest something!</p>';
        return;
    }
    
    mySuggestions.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
    
    listContainer.innerHTML = mySuggestions.map(s => {
        const date = new Date(s.timestamp).toLocaleDateString();
        const emoji = getTypeEmoji(s.type);
        const linkHtml = s.url ? `<a href="${s.url}" target="_blank" style="color: #FF6B35; text-decoration: none;">View on GitHub →</a>` : '';
        
        return `
            <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; margin-bottom: 10px; border-left: 3px solid #FF6B35;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                    <span style="background: #FF6B35; color: white; padding: 3px 10px; border-radius: 12px; font-size: 12px; font-weight: 600;">
                        ${emoji} ${s.type.toUpperCase()}
                    </span>
                    <span style="color: #666; font-size: 14px;">⏳ Pending</span>
                </div>
                <div style="color: #333; margin-bottom: 5px;">${s.text}</div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #999; font-size: 13px;">${date}</span>
                    ${linkHtml}
                </div>
            </div>
        `;
    }).join('');
}

function exportSuggestions() {
    const all = JSON.parse(localStorage.getItem('kl_trip_all_suggestions') || '[]');
    if (all.length === 0) { 
        alert('No suggestions to export'); 
        return; 
    }
    
    const blob = new Blob([JSON.stringify(all, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `kl-trip-suggestions-${Date.now()}.json`;
    link.click();
    URL.revokeObjectURL(url);
    
    alert(`Exported ${all.length} suggestion(s). Please share this file with your team lead.`);
}

function showExportButton() {
    let exportBtn = document.getElementById('export-suggestions-btn');
    if (!exportBtn) {
        const statusDiv = document.getElementById('suggestion-status');
        exportBtn = document.createElement('button');
        exportBtn.id = 'export-suggestions-btn';
        exportBtn.className = 'btn-secondary';
        exportBtn.style.marginTop = '10px';
        exportBtn.style.marginLeft = '10px';
        exportBtn.textContent = '📥 Export Suggestions';
        exportBtn.onclick = exportSuggestions;
        statusDiv.parentNode.insertBefore(exportBtn, statusDiv.nextSibling);
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('submit-suggestion');
    if (btn) {
        btn.addEventListener('click', submitSuggestion);
    }
    updateMySuggestionsList();
});

// Make functions globally available
window.submitSuggestion = submitSuggestion;
window.exportSuggestions = exportSuggestions;
