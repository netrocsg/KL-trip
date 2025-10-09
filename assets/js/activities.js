// Load and display all activities
let allActivities = [];

async function loadAllActivities() {
    try {
        const response = await fetch('/KL-trip/assets/js/activities-data.json');
        allActivities = await response.json();
        displayActivities(allActivities);
        setupFilters();
    } catch (error) {
        console.error('Error loading activities:', error);
    }
}

function displayActivities(activities) {
    const grid = document.getElementById('activities-full-grid');
    if (!grid) return;
    
    const votes = getVotes();
    
    grid.innerHTML = activities.map(activity => `
            <div class="activity-detail-card" data-category="${activity.category}">
                 <div class="activity-detail-image" style="background-image: url(\'${activity.photos[0]}\')">
                    <div class="activity-category">${activity.category}</div>
                </div>
                <div class="activity-detail-content">
                    <h3>${activity.name}</h3>
                    <p class="activity-description">${activity.description}</p>
                    
                    <div class="activity-info-grid">
                        <div class="info-item">
                            <span class="info-label">📍 Location</span>
                            <span class="info-value">${activity.location}</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">⏱️ Duration</span>
                            <span class="info-value">${activity.duration}</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">💰 Cost</span>
                            <span class="info-value">${activity.cost_usd}</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">🕐 Best Time</span>
                            <span class="info-value">${activity.best_time}</span>
                        </div>
                    </div>
                    
                    <div class="activity-highlights">
                        <h4>Highlights:</h4>
                        <ul>
                            ${activity.highlights.slice(0, 3).map(h => `<li>${h}</li>`).join('')}
                        </ul>
                    </div>
                    
                    <div class="activity-tips">
                        <h4>💡 Tips:</h4>
                        <ul>
                            ${activity.tips.slice(0, 2).map(t => `<li>${t}</li>`).join('')}
                        </ul>
                    </div>
                    
                    <div class="activity-footer">
                        <div class="activity-votes">
                            <div class="vote-count">
                                <span class="vote-number" id="votes-activity-${activity.id}">${votes.activities[activity.id] || 0}</span>
                                <span class="vote-label">votes</span>
                            </div>
                            <button class="btn-vote" onclick="vote(null, ${activity.id})">👍 Vote</button>
                        </div>
                        <div class="activity-difficulty">
                            <span class="difficulty-badge">${activity.difficulty}</span>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }).join('');
}

function setupFilters() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Update active state
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            // Filter activities
            const filter = btn.dataset.filter;
            if (filter === 'all') {
                displayActivities(allActivities);
            } else {
                const filtered = allActivities.filter(a => a.category === filter);
                displayActivities(filtered);
            }
        });
    });
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    loadAllActivities();
});
