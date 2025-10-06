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
    
    grid.innerHTML = activities.map(activity => {
        const imageMap = {
            1: 'https://images.unsplash.com/photo-1596422846543-75c6fc197f07?w=800',
            2: 'https://images.unsplash.com/photo-1508062878650-88b52897f298?w=800',
            3: 'https://images.unsplash.com/photo-1583417319070-4a69db38a482?w=800',
            4: 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800',
            5: 'https://images.unsplash.com/photo-1548013146-72479768bada?w=800',
            6: 'https://images.unsplash.com/photo-1555217851-4f3c0f2e0f5e?w=800',
            7: 'https://images.unsplash.com/photo-1583417319070-4a69db38a482?w=800',
            8: 'https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=800',
            9: 'https://images.unsplash.com/photo-1564769625905-50e93615e769?w=800',
            10: 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800',
            11: 'https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=800',
            12: 'https://images.unsplash.com/photo-1552728089-57bdde30beb3?w=800',
            13: 'https://images.unsplash.com/photo-1555421689-d68471e189f2?w=800',
            14: 'https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=800',
            15: 'https://images.unsplash.com/photo-1582555172866-f73bb12a2ab3?w=800',
            16: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800',
            17: 'https://images.unsplash.com/photo-1514933651103-005eec06c04b?w=800',
            18: 'https://images.unsplash.com/photo-1555421689-d68471e189f2?w=800',
            19: 'https://images.unsplash.com/photo-1509023464722-18d996393ca8?w=800',
            20: 'https://images.unsplash.com/photo-1533090161767-e6ffed986c88?w=800'
        };
        
        return `
            <div class="activity-detail-card" data-category="${activity.category}">
                <div class="activity-detail-image" style="background-image: url('${imageMap[activity.id] || imageMap[1]}')">
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
