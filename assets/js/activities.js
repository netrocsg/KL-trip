console.log('activities.js script started');

function initializeActivities(allActivities) {
    console.log("allActivities array is now loaded with", allActivities.length, "activities.");

    document.addEventListener('DOMContentLoaded', () => {
        console.log('DOM fully loaded and parsed');
        const grid = document.getElementById('activities-full-grid');
        const filterButtons = document.querySelectorAll('.filter-btn');

        if (!grid) {
            console.error('Error: The element with ID \'activities-full-grid\' was not found.');
            return;
        }

        function displayActivities(activities) {
            console.log(`Displaying ${activities.length} activities.`);
            grid.innerHTML = '';
            if (activities.length === 0) {
                grid.innerHTML = '<p class="no-activities-found">No activities found for this category.</p>';
                return;
            }

            activities.forEach(activity => {
                const card = document.createElement('div');
                card.className = 'activity-card';
                card.dataset.category = activity.category;

                let costText = 'Free';
                if (activity.cost_rm) {
                    if (typeof activity.cost_rm === 'number') {
                        costText = `RM ${activity.cost_rm}`;
                    } else if (typeof activity.cost_rm === 'object') {
                        const costs = Object.entries(activity.cost_rm).map(([key, value]) => `${key.replace('_', ' ')}: RM ${value}`);
                        costText = costs.join('<br>');
                    }
                }

                card.innerHTML = `
                    <div class="card-image-container">
                        <img src="${activity.photos[0]}" alt="${activity.name}" class="card-image">
                        <div class="card-overlay">
                            <p class="card-description">${activity.description}</p>
                            <a href="#" class="btn-view-details">View Details</a>
                        </div>
                    </div>
                    <div class="card-content">
                        <h3 class="card-title">${activity.name}</h3>
                        <p class="card-category">${activity.category} - ${activity.subcategory}</p>
                        <div class="card-details">
                            <p><strong><i class="fas fa-money-bill-wave"></i> Cost:</strong> ${costText}</p>
                            <p><strong><i class="fas fa-clock"></i> Duration:</strong> ${activity.duration_hours} hours</p>
                            <p><strong><i class="fas fa-map-marker-alt"></i> Location:</strong> ${activity.location}</p>
                        </div>
                    </div>
                `;
                grid.appendChild(card);
            });
        }

        function filterActivities() {
            const filter = this.dataset.filter;
            console.log(`Filtering by: ${filter}`);

            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            if (filter === 'all') {
                displayActivities(allActivities);
            } else {
                const filteredActivities = allActivities.filter(activity => activity.category === filter);
                displayActivities(filteredActivities);
            }
        }

        console.log('Adding event listeners to filter buttons.');
        filterButtons.forEach(button => button.addEventListener('click', filterActivities));

        console.log('Initial display of all activities.');
        displayActivities(allActivities);
    });
}

