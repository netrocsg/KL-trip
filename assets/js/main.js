// ===== VOTING SYSTEM =====
const STORAGE_KEY = 'kl_trip_votes';

// Initialize votes from localStorage
function getVotes() {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) {
        return JSON.parse(stored);
    }
    return {
        itineraries: {
            cultural: 0,
            instagram: 0,
            balanced: 0
        },
        activities: {}
    };
}

function saveVotes(votes) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(votes));
    updateVoteDisplay();
}

function vote(type, id = null) {
    const votes = getVotes();
    
    if (id) {
        // Activity vote
        if (!votes.activities[id]) {
            votes.activities[id] = 0;
        }
        votes.activities[id]++;
        
        // Visual feedback
        const button = document.querySelector(`[data-activity="${id}"] .btn-vote`);
        if (button) {
            button.classList.add('voted');
            button.textContent = '✓ Voted';
            setTimeout(() => {
                button.classList.remove('voted');
                button.textContent = '👍 Vote';
            }, 2000);
        }
    } else {
        // Itinerary vote
        if (votes.itineraries[type] !== undefined) {
            votes.itineraries[type]++;
        }
        
        // Visual feedback
        const button = document.querySelector(`[data-itinerary="${type}"] .btn-vote`);
        if (button) {
            button.classList.add('voted');
            button.textContent = '✓ Voted';
            setTimeout(() => {
                button.classList.remove('voted');
                button.textContent = '👍 Vote';
            }, 2000);
        }
    }
    
    saveVotes(votes);
}

function updateVoteDisplay() {
    const votes = getVotes();
    
    // Update itinerary votes
    Object.keys(votes.itineraries).forEach(key => {
        const element = document.getElementById(`votes-${key}`);
        if (element) {
            element.textContent = votes.itineraries[key];
        }
    });
    
    // Update activity votes
    Object.keys(votes.activities).forEach(id => {
        const element = document.getElementById(`votes-activity-${id}`);
        if (element) {
            element.textContent = votes.activities[id];
        }
    });
    
    // Update total votes
    const totalVotes = Object.values(votes.itineraries).reduce((a, b) => a + b, 0) +
                       Object.values(votes.activities).reduce((a, b) => a + b, 0);
    const totalElement = document.getElementById('total-votes');
    if (totalElement) {
        totalElement.textContent = totalVotes;
    }
    
    // Update top itinerary
    const topItinerary = Object.entries(votes.itineraries)
        .sort((a, b) => b[1] - a[1])[0];
    const topElement = document.getElementById('top-itinerary');
    if (topElement && topItinerary) {
        const names = {
            cultural: 'Cultural & Foodie',
            instagram: 'Instagram-Worthy',
            balanced: 'Balanced Explorer'
        };
        topElement.textContent = names[topItinerary[0]] || '-';
    }
}

// ===== TOP ACTIVITIES DATA =====
const topActivities = [
    {
        id: 1,
        name: 'Batu Caves',
        category: 'Cultural',
        description: '272 rainbow steps leading to ancient limestone caves with Hindu temples',
        image: 'https://images.unsplash.com/photo-1596422846543-75c6fc197f07?w=600',
        cost: 'Free',
        duration: '2-3 hours'
    },
    {
        id: 2,
        name: 'Petronas Twin Towers',
        category: 'Landmarks',
        description: 'Iconic 452m twin towers with skybridge and observation deck',
        image: 'https://images.unsplash.com/photo-1508062878650-88b52897f298?w=600',
        cost: '$31',
        duration: '1.5-2 hours'
    },
    {
        id: 4,
        name: 'Jalan Alor Food Street',
        category: 'Food',
        description: 'Famous night food street with authentic Malaysian street food',
        image: 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=600',
        cost: '$5-10',
        duration: '1.5-2 hours'
    },
    {
        id: 16,
        name: 'Food Tour Experience',
        category: 'Food',
        description: '4-hour guided tour with 15+ tastings through local neighborhoods',
        image: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=600',
        cost: '$48-60',
        duration: '4 hours'
    },
    {
        id: 3,
        name: 'KL Tower',
        category: 'Landmarks',
        description: '421m tower with 360° views and glass Sky Box',
        image: 'https://images.unsplash.com/photo-1583417319070-4a69db38a482?w=600',
        cost: '$19',
        duration: '1-2 hours'
    },
    {
        id: 17,
        name: 'SkyBar at Traders Hotel',
        category: 'Nightlife',
        description: 'Rooftop bar with best Petronas Towers views',
        image: 'https://images.unsplash.com/photo-1514933651103-005eec06c04b?w=600',
        cost: '$19-36',
        duration: '2-3 hours'
    }
];

// ===== LOAD ACTIVITIES =====
function loadActivities() {
    const grid = document.getElementById('activities-grid');
    if (!grid) return;
    
    const votes = getVotes();
    
    grid.innerHTML = topActivities.map(activity => `
        <div class="activity-card" data-activity="${activity.id}">
            <div class="activity-image" style="background-image: url('${activity.image}')">
                <div class="activity-category">${activity.category}</div>
            </div>
            <div class="activity-content">
                <h3>${activity.name}</h3>
                <p>${activity.description}</p>
                <div class="activity-meta">
                    <span class="activity-cost">${activity.cost}</span>
                    <span class="activity-duration">⏱️ ${activity.duration}</span>
                </div>
                <div class="activity-votes">
                    <div class="vote-count">
                        <span class="vote-number" id="votes-activity-${activity.id}">${votes.activities[activity.id] || 0}</span>
                        <span class="vote-label">votes</span>
                    </div>
                    <button class="btn-vote" onclick="vote(null, ${activity.id})">👍 Vote</button>
                </div>
            </div>
        </div>
    `).join('');
}

// ===== MOBILE MENU =====
function setupMobileMenu() {
    const toggle = document.querySelector('.mobile-menu-toggle');
    const menu = document.querySelector('.nav-menu');
    
    if (toggle && menu) {
        toggle.addEventListener('click', () => {
            menu.classList.toggle('active');
        });
    }
}

// ===== SMOOTH SCROLLING =====
function setupSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// ===== SCROLL ANIMATIONS =====
function setupScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
            }
        });
    }, {
        threshold: 0.1
    });
    
    document.querySelectorAll('.activity-card, .itinerary-card, .budget-card').forEach(el => {
        observer.observe(el);
    });
}

// ===== INITIALIZE =====
document.addEventListener('DOMContentLoaded', () => {
    loadActivities();
    updateVoteDisplay();
    setupMobileMenu();
    setupSmoothScroll();
    setupScrollAnimations();
    
    // Make vote function globally available
    window.vote = vote;
});

// ===== EXPORT VOTES (for future agent integration) =====
function exportVotes() {
    const votes = getVotes();
    const blob = new Blob([JSON.stringify(votes, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'kl-trip-votes.json';
    a.click();
    URL.revokeObjectURL(url);
}

// Make export function available globally
window.exportVotes = exportVotes;
