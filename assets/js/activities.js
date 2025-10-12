// Load and display all activities

let allActivities = [
  {
    "id": 1,
    "name": "District 21",
    "category": "Adventure & Sports",
    "subcategory": "Indoor Theme Park",
    "description": "An apocalypse-themed indoor adventure park featuring 8 attractions such as Tubby Ride, Launch Pad, Power Station, Free Fall, Maze, Ninja Warrior Course, Sky Trail, and Roller Glider. It offers activities for all ages and skill levels, encouraging climbing, jumping, riding, sliding, and flying.",
    "location": "AT 6, Level 1, IOI City Mall, Lebuh IRC, IOI Resort City, 62502 Putrajaya, Malaysia.",
    "cost_rm": {
      "weekday_active": 64,
      "weekend_active": 80,
      "non_active": 10
    },
    "cost_usd": {
      "weekday_active": 14.25,
      "weekend_active": 16.6,
      "non_active": 2.2
    },
    "duration_hours": 3,
    "best_time": "Weekdays for fewer crowds, any time during opening hours.",
    "tips": "Wear comfortable clothing and closed-toe shoes. Arrive early, especially on weekends. Book tickets online to secure a slot. Suitable for groups.",
    "photos": [
      "/KL-trip/assets/images/activities/district-21/1.jpg",
      "/KL-trip/assets/images/activities/district-21/2.jpg",
      "/KL-trip/assets/images/activities/district-21/3.jpg"
    ],
    "added_date": "2025-10-09",
    "source": "proactive_research",
    "difficulty": "Moderate"
  },
  {
    "id": 2,
    "name": "SuperPark Malaysia",
    "category": "Adventure & Sports",
    "subcategory": "Indoor Activity Park",
    "description": "A unique, purpose-built indoor activity park from Finland, offering over 20 activities across three themed areas: Adventure Area, Game Arena, and Freestyle Hall. Activities include trampolines, zip wires, climbing walls, and more.",
    "location": "Unit 4-1, Level 4, Avenue K Shopping Mall, 156, Jalan Ampang, 50450 Kuala Lumpur, Malaysia.",
    "cost_rm": {
      "weekday": 60,
      "weekend": 75
    },
    "cost_usd": {
      "weekday": 14.00,
      "weekend": 16.60
    },
    "duration_hours": 3,
    "best_time": "Weekdays for fewer crowds. Check session times online.",
    "tips": "Wear comfortable sports attire and grip socks (available for purchase). Book online in advance. Lockers are available.",
    "photos": [
      "/KL-trip/assets/images/activities/superpark-malaysia/1.jpg",
      "/KL-trip/assets/images/activities/superpark-malaysia/2.jpg",
      "/KL-trip/assets/images/activities/superpark-malaysia/3.jpg"
    ],
    "added_date": "2025-10-09",
    "source": "proactive_research",
    "difficulty": "Easy to Moderate"
  },
  {
    "id": 3,
    "name": "ESCAPE Petaling Jaya",
    "category": "Adventure & Sports",
    "subcategory": "Indoor Theme Park",
    "description": "An indoor adventure park with thrilling rides and games, promoting play and challenging physical activities. Features include a high-ropes course, zip lines, climbing zones, and a variety of obstacle courses.",
    "location": "Paradigm Mall, Level 1, 1, Jalan SS 7/26a, SS 7, 47301 Petaling Jaya, Selangor, Malaysia.",
    "cost_rm": {
      "junior": 100,
      "adult": 120
    },
    "cost_usd": {
      "junior": 20.87,
      "adult": 24.42
    },
    "duration_hours": 8,
    "best_time": "Weekdays for a less crowded experience. Arrive early to maximize play time.",
    "tips": "Wear comfortable sports attire. Grip socks are required. Book tickets online. Lockers are available. Facial recognition for entry.",
    "photos": [
      "/KL-trip/assets/images/activities/escape-petaling-jaya/1.jpg",
      "/KL-trip/assets/images/activities/escape-petaling-jaya/2.jpg",
      "/KL-trip/assets/images/activities/escape-petaling-jaya/3.jpg"
    ],
    "added_date": "2025-10-09",
    "source": "proactive_research",
    "difficulty": "Moderate to Challenging"
  },
  {
    "id": 4,
    "name": "LYL International Karting Circuit",
    "category": "Adventure & Sports",
    "subcategory": "Go-Karting",
    "description": "An FIA-certified outdoor karting circuit offering a professional racing experience for both beginners and experienced drivers. Features a challenging track layout and well-maintained karts.",
    "location": "Lot 600, Jalan Sungai Long, Kampung Sungai Long, 43000 Kajang, Selangor, Malaysia.",
    "cost_rm": {
      "single_kart_10min": 70,
      "double_kart_10min": 90
    },
    "cost_usd": {
      "single_kart_10min": 15.00,
      "double_kart_10min": 19.00
    },
    "duration_hours": 0.5,
    "best_time": "Evenings for cooler weather. Check availability and book in advance.",
    "tips": "Wear comfortable clothing and closed-toe shoes. Mandatory balaclava and gloves (available for rent/purchase). Minimum age/height requirements apply.",
    "photos": [
      "/KL-trip/assets/images/activities/lyl-karting/1.jpg",
      "/KL-trip/assets/images/activities/lyl-karting/2.jpg",
      "/KL-trip/assets/images/activities/lyl-karting/3.jpg"
    ],
    "added_date": "2025-10-09",
    "source": "proactive_research",
    "difficulty": "Moderate"
  },
  {
    "id": 5,
    "name": "Skytrex Adventure Sg Congkak",
    "category": "Adventure & Sports",
    "subcategory": "Zipline & Forest Adventure",
    "description": "An eco-adventure park set in a lush rainforest, offering various aerial obstacle courses and ziplines. Participants navigate through different circuits with varying difficulty levels.",
    "location": "Hulu Langat, 43100 Selangor, Malaysia.",
    "cost_rm": {
      "little_adventure": 55,
      "big_thrill": 75,
      "extreme_challenge": 110
    },
    "cost_usd": {
      "little_adventure": 12.00,
      "big_thrill": 16.50,
      "extreme_challenge": 24.00
    },
    "duration_hours": 1.5,
    "best_time": "Mornings for cooler weather. Book online in advance, especially on weekends.",
    "tips": "Wear comfortable outdoor clothing and closed-toe shoes. Bring insect repellent and water. Arrive 30 minutes before your session.",
    "photos": [
      "/KL-trip/assets/images/activities/skytrex-adventure-sg-congkak/1.jpg",
      "/KL-trip/assets/images/activities/skytrex-adventure-sg-congkak/2.jpg",
      "/KL-trip/assets/images/activities/skytrex-adventure-sg-congkak/3.jpg"
    ],
    "added_date": "2025-10-09",
    "source": "proactive_research",
    "difficulty": "Varies by circuit (Easy to Extreme)"
  },
  {
    "id": 6,
    "name": "Jump Street Trampoline Park",
    "category": "Adventure & Sports",
    "subcategory": "Trampoline Park",
    "description": "Malaysia's first indoor trampoline park, offering a variety of trampoline-based activities including free jumping, dodgeball, basketball, and a foam pit. Suitable for all ages.",
    "location": "No. 8, Jalan 13/6, Seksyen 13, 46200 Petaling Jaya, Selangor, Malaysia.",
    "cost_rm": {
      "per_hour": 30,
      "grip_socks": 5
    },
    "cost_usd": {
      "per_hour": 6.50,
      "grip_socks": 1.00
    },
    "duration_hours": 1,
    "best_time": "Weekdays for fewer crowds. Check session availability online.",
    "tips": "Wear comfortable clothing. Grip socks are mandatory (can be purchased on-site). Book online to guarantee a spot.",
    "photos": [
      "/KL-trip/assets/images/activities/jump-street-trampoline-park/1.jpg",
      "/KL-trip/assets/images/activities/jump-street-trampoline-park/2.jpg",
      "/KL-trip/assets/images/activities/jump-street-trampoline-park/3.jpg"
    ],
    "added_date": "2025-10-09",
    "source": "proactive_research",
    "difficulty": "Easy to Moderate"
  },
  {
    "id": 7,
    "name": "Sunway Lagoon Theme Park",
    "category": "Adventure & Sports",
    "subcategory": "Theme Park",
    "description": "A massive multi-park destination featuring over 90 attractions across 6 themed zones: Water Park, Amusement Park, Wildlife Park, Extreme Park, Scream Park, and Nickelodeon Lost Lagoon. Offers a full day of entertainment.",
    "location": "3, Jalan PJS 11/11, Bandar Sunway, 47500 Subang Jaya, Selangor, Malaysia.",
    "cost_rm": {
      "adult": 202,
      "child_senior": 170
    },
    "cost_usd": {
      "adult": 40.00,
      "child_senior": 35.00
    },
    "duration_hours": 8,
    "best_time": "Weekdays for fewer crowds. Arrive early to enjoy all attractions. Avoid public holidays.",
    "tips": "Wear swimwear and comfortable walking shoes. Bring sunscreen, hat, and sunglasses. Lockers are available for rent. Book tickets online for discounts.",
    "photos": [
      "/KL-trip/assets/images/activities/sunway-lagoon-theme-park/1.jpg",
      "/KL-trip/assets/images/activities/sunway-lagoon-theme-park/2.jpg",
      "/KL-trip/assets/images/activities/sunway-lagoon-theme-park/3.jpg"
    ],
    "added_date": "2025-10-09",
    "source": "proactive_research",
    "difficulty": "Varies by attraction"
  }
];

function loadAllActivities() {
    displayActivities(allActivities);
    setupFilters();
}

function displayActivities(activities) {
    const grid = document.getElementById('activities-full-grid');
    if (!grid) return;
    
    const votes = getVotes();
    
    grid.innerHTML = activities.map(activity => `
            <div class="activity-detail-card" data-category="${activity.category}">
                 <div class="activity-detail-image" style="background-image: url('${activity.photos[0]}')">
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
                            <span class="info-value">${activity.duration_hours} hours</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">💰 Cost</span>
                            <span class="info-value">$${activity.cost_usd.weekend_active || activity.cost_usd.adult || activity.cost_usd.per_hour}</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">🕐 Best Time</span>
                            <span class="info-value">${activity.best_time}</span>
                        </div>
                    </div>
                    
                    <div class="activity-tips">
                        <h4>💡 Tips:</h4>
                        <ul>
                            ${activity.tips.split('. ').slice(0, 2).map(t => `<li>${t}</li>`).join('')}
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
        `)
    .join('');
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

