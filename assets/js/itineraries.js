let itinerariesData = null;
let activitiesData = null;
let currentItinerary = 'cultural_foodie';

async function loadData() {
    try {
        const [itinResponse, actResponse] = await Promise.all([
            fetch('/KL-trip/assets/js/itineraries-data.json'),
            fetch('/KL-trip/assets/js/activities-data.json')
        ]);
        
        const itinData = await itinResponse.json();
        itinerariesData = itinData.itinerary_options;
        activitiesData = await actResponse.json();
        
        displayItinerary(currentItinerary);
        displayAccommodation(itinData.trip_info.accommodation_options);
        setupTabs();
    } catch (error) {
        console.error('Error loading data:', error);
    }
}

function displayItinerary(key) {
    const content = document.getElementById('itinerary-content');
    if (!content || !itinerariesData) return;
    
    const itinerary = itinerariesData[key];
    if (!itinerary) return;
    
    content.innerHTML = `
        <div class="itinerary-header">
            <h2>${itinerary.name}</h2>
            <p>${itinerary.description}</p>
            <div class="itinerary-cost">${itinerary.total_3day_cost.per_person_usd} per person</div>
        </div>
        
        ${itinerary.days.map(day => {
            const activities = day.activities.map(act => {
                const activityDetail = activitiesData.find(a => a.id === act.activity_id);
                return {
                    ...act,
                    detail: activityDetail
                };
            });
            
            return `
                <div class="day-card">
                    <div class="day-header">
                        <div class="day-title">
                            <h3>Day ${day.day}</h3>
                            <div class="day-theme">${day.theme}</div>
                            <div style="font-size: 14px; color: var(--gray); margin-top: 5px;">${day.date}</div>
                        </div>
                        <div class="day-cost">
                            <div class="day-cost-label">Estimated Cost</div>
                            <div class="day-cost-value">${day.estimated_cost_per_person.total_usd}</div>
                        </div>
                    </div>
                    
                    <div class="timeline">
                        ${activities.map(act => `
                            <div class="timeline-item">
                                <div class="timeline-time">${act.time}</div>
                                <div class="timeline-activity">
                                    <h4>${act.detail ? act.detail.name : 'Activity'}</h4>
                                    <p>${act.notes}</p>
                                    ${act.detail ? `
                                        <div style="margin-top: 10px; font-size: 13px; color: var(--gray);">
                                            📍 ${act.detail.location} | 💰 ${act.detail.cost_usd}
                                        </div>
                                    ` : ''}
                                </div>
                            </div>
                        `).join('')}
                    </div>
                    
                    <div class="meals-section">
                        <h4>🍽️ Meals for Day ${day.day}</h4>
                        <div class="meal-item"><strong>Breakfast:</strong> ${day.meals.breakfast}</div>
                        <div class="meal-item"><strong>Lunch:</strong> ${day.meals.lunch}</div>
                        <div class="meal-item"><strong>Dinner:</strong> ${day.meals.dinner}</div>
                    </div>
                </div>
            `;
        }).join('')}
        
        <div class="itinerary-summary" style="background: var(--light-color); padding: 30px; border-radius: 16px; margin-top: 40px;">
            <h3 style="font-size: 24px; margin-bottom: 20px; color: var(--secondary-color);">3-Day Total</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
                <div>
                    <div style="font-size: 14px; color: var(--gray);">Per Person</div>
                    <div style="font-size: 28px; font-weight: 700; color: var(--primary-color);">${itinerary.total_3day_cost.per_person_usd}</div>
                </div>
                <div>
                    <div style="font-size: 14px; color: var(--gray);">For 8 People</div>
                    <div style="font-size: 28px; font-weight: 700; color: var(--primary-color);">${itinerary.total_3day_cost.for_8_people_usd}</div>
                </div>
            </div>
        </div>
    `;
}

function displayAccommodation(options) {
    const container = document.getElementById('accommodation-options');
    if (!container || !options) return;
    
    container.innerHTML = options.map(option => `
        <div class="accommodation-card">
            <h3>${option.name}</h3>
            <p>${option.description}</p>
            <div style="font-size: 14px; color: var(--gray); margin-top: 10px;">
                <div>Per night: ${option.cost_per_night}</div>
                <div>3 nights total: ${option.cost_3_nights}</div>
            </div>
            <div class="accommodation-cost">${option.per_person_3_nights} per person</div>
        </div>
    `).join('');
}

function setupTabs() {
    const tabs = document.querySelectorAll('.tab-btn');
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            
            const itineraryKey = tab.dataset.itinerary;
            const keyMap = {
                'cultural': 'cultural_foodie',
                'instagram': 'instagram_worthy',
                'balanced': 'balanced_explorer'
            };
            
            currentItinerary = keyMap[itineraryKey];
            displayItinerary(currentItinerary);
        });
    });
}

document.addEventListener('DOMContentLoaded', () => {
    loadData();
});
