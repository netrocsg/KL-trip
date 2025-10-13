#!/usr/bin/env python3.11
"""
Script to add 7 Nature & Parks activities to the KL Trip database
October 13, 2025
"""

import json
from datetime import date

# Load existing activities
with open('assets/js/activities-data.json', 'r') as f:
    activities = json.load(f)

# Get the last ID
last_id = activities[-1]['id'] if activities else 0

# Define new Nature & Parks activities
new_activities = [
    {
        "id": last_id + 1,
        "name": "KL Bird Park",
        "category": "Nature & Parks",
        "subcategory": "Wildlife Park",
        "description": "Asia's largest walk-in free-flight aviary, home to over 3,000 local and foreign birds of approximately 200 different species. Features free-flight zones where birds roam naturally in an environment that closely resembles their natural habitat. Located in the scenic Lake Gardens, just 10 minutes from the city center.",
        "location": "920 Jalan Cenderawasih, Taman Tasik Perdana, 50480 Kuala Lumpur",
        "cost_rm": 90,
        "cost_usd": 20.00,
        "duration_hours": 2.5,
        "best_time": "Morning (9-11am) when birds are most active. Weekdays for fewer crowds.",
        "tips": "Book online for 10% discount. Bring sunscreen and hat. Don't miss the bird shows at 12:30pm and 3:30pm. Feeding sessions available throughout the day. Wear comfortable walking shoes.",
        "photos": [
            "/KL-trip/assets/images/activities/kl-bird-park/1.jpg",
            "/KL-trip/assets/images/activities/kl-bird-park/2.jpg",
            "/KL-trip/assets/images/activities/kl-bird-park/3.jpg"
        ],
        "added_date": "2025-10-13",
        "source": "proactive_research"
    },
    {
        "id": last_id + 2,
        "name": "KL Butterfly Park",
        "category": "Nature & Parks",
        "subcategory": "Wildlife Park",
        "description": "A beautiful butterfly sanctuary featuring thousands of butterflies in a lush tropical garden setting. Home to various species of butterflies flying freely in their natural habitat, surrounded by exotic plants and flowers. A peaceful escape perfect for nature lovers and photographers.",
        "location": "Jalan Cenderawasih, Taman Tasik Perdana, 50480 Kuala Lumpur",
        "cost_rm": 18,
        "cost_usd": 4.00,
        "duration_hours": 1.5,
        "best_time": "Morning (9-11am) for most butterfly activity. Avoid rainy days.",
        "tips": "Bring cash as card payment may not be available. Wear bright colors to attract butterflies. Great for photography. Combine with nearby Bird Park for a full day.",
        "photos": [
            "/KL-trip/assets/images/activities/kl-butterfly-park/1.jpg",
            "/KL-trip/assets/images/activities/kl-butterfly-park/2.jpg",
            "/KL-trip/assets/images/activities/kl-butterfly-park/3.jpg"
        ],
        "added_date": "2025-10-13",
        "source": "proactive_research"
    },
    {
        "id": last_id + 3,
        "name": "Perdana Botanical Gardens",
        "category": "Nature & Parks",
        "subcategory": "Botanical Garden",
        "description": "Kuala Lumpur's first large-scale recreational park, opened in 1889 during the British colonial era. This expansive garden features themed areas, serene lakes, cascading waterfalls, jungle trails, and diverse flora. A peaceful green oasis in the heart of the city, perfect for relaxation and outdoor activities.",
        "location": "Jalan Perdana, 50480 Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0.00,
        "duration_hours": 2.5,
        "best_time": "Early morning (7-9am) or late afternoon (4-6pm) to avoid heat. Weekdays for quieter experience.",
        "tips": "Bring water and comfortable walking shoes. Great for jogging, picnics, and photography. Free entry. Contains several attractions including Bird Park, Butterfly Park, and Deer Park.",
        "photos": [
            "/KL-trip/assets/images/activities/perdana-botanical-gardens/1.jpg",
            "/KL-trip/assets/images/activities/perdana-botanical-gardens/2.jpg",
            "/KL-trip/assets/images/activities/perdana-botanical-gardens/3.jpg"
        ],
        "added_date": "2025-10-13",
        "source": "proactive_research"
    },
    {
        "id": last_id + 4,
        "name": "KL Forest Eco Park",
        "category": "Nature & Parks",
        "subcategory": "Forest Reserve",
        "description": "A 9-hectare virgin rainforest reserve in the heart of Kuala Lumpur, home to over 200 tree species and diverse wildlife. Features a spectacular 200-meter canopy walkway suspended 21 meters above ground, offering stunning views of the city skyline through the forest canopy. One of the oldest permanent forest reserves in Malaysia.",
        "location": "Jalan Raja Chulan, next to KL Tower, 50250 Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0.00,
        "duration_hours": 1.5,
        "best_time": "Early morning (7-9am) for cooler weather and better wildlife spotting. Avoid after rain as walkway can be slippery.",
        "tips": "Wear proper walking shoes with good grip. The canopy walk can be slippery when wet. Free entry. Combine with KL Tower visit. Bring insect repellent.",
        "photos": [
            "/KL-trip/assets/images/activities/kl-forest-eco-park/1.jpg",
            "/KL-trip/assets/images/activities/kl-forest-eco-park/2.jpg",
            "/KL-trip/assets/images/activities/kl-forest-eco-park/3.jpg"
        ],
        "added_date": "2025-10-13",
        "source": "proactive_research"
    },
    {
        "id": last_id + 5,
        "name": "FRIM Forest Skywalk",
        "category": "Nature & Parks",
        "subcategory": "Forest Reserve",
        "description": "Malaysia's premier forestry research institute featuring the impressive Forest Skywalk - a 250-meter canopy walkway with 11 towers reaching up to 50 meters high. Set within beautiful botanical gardens with extensive hiking trails through diverse ecosystems. An educational and adventurous experience for nature enthusiasts.",
        "location": "Kepong Botanic Gardens, 52109 Kepong, Selangor",
        "cost_rm": 10,
        "cost_usd": 2.20,
        "duration_hours": 2.5,
        "best_time": "Morning (8-10am) for cooler weather and clearer views. Weekdays less crowded.",
        "tips": "About 30-45 minutes from city center by car or Grab. Bring insect repellent and water. Great for nature photography and hiking. Wear comfortable shoes. Book skywalk tickets in advance on weekends.",
        "photos": [
            "/KL-trip/assets/images/activities/frim-forest-skywalk/1.jpg",
            "/KL-trip/assets/images/activities/frim-forest-skywalk/2.jpg",
            "/KL-trip/assets/images/activities/frim-forest-skywalk/3.jpg"
        ],
        "added_date": "2025-10-13",
        "source": "proactive_research"
    },
    {
        "id": last_id + 6,
        "name": "Taman Tugu",
        "category": "Nature & Parks",
        "subcategory": "Urban Forest Park",
        "description": "A 66-acre rehabilitated secondary rainforest in the heart of Kuala Lumpur with over 5 kilometers of well-maintained trails. This conservation site features diverse flora and fauna, offering a peaceful escape from the city. Multiple trail options cater to different fitness levels, making it accessible for all visitors.",
        "location": "Off Jalan Tun Razak, near Chow Kit, Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0.00,
        "duration_hours": 1.5,
        "best_time": "Early morning (7-9am) for bird watching and cooler weather. Avoid midday heat.",
        "tips": "Bring water and mosquito repellent. Well-marked trails suitable for all fitness levels. Free entry. Great for morning walks and nature photography. Download trail map from website before visiting.",
        "photos": [
            "/KL-trip/assets/images/activities/taman-tugu/1.jpg",
            "/KL-trip/assets/images/activities/taman-tugu/2.jpg",
            "/KL-trip/assets/images/activities/taman-tugu/3.jpg"
        ],
        "added_date": "2025-10-13",
        "source": "proactive_research"
    },
    {
        "id": last_id + 7,
        "name": "Titiwangsa Lake Gardens",
        "category": "Nature & Parks",
        "subcategory": "Urban Park",
        "description": "An attractive urban park centered around a large scenic lake, offering stunning views of the Petronas Twin Towers and KL Tower. Popular recreational area for jogging, cycling, paddle boating, and picnics. Features well-maintained facilities including playgrounds, exercise equipment, and walking paths around the lake.",
        "location": "Jalan Temerloh, Titiwangsa, 53200 Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0.00,
        "duration_hours": 1.5,
        "best_time": "Early morning (6-8am) or sunset (5-7pm) for best photography and cooler weather. Popular with locals for exercise.",
        "tips": "Great for photography of city skyline, especially at sunset. Paddle boats available for rent. Free entry. Popular with locals for jogging and cycling. Bring camera for Twin Towers views.",
        "photos": [
            "/KL-trip/assets/images/activities/titiwangsa-lake-gardens/1.jpg",
            "/KL-trip/assets/images/activities/titiwangsa-lake-gardens/2.jpg",
            "/KL-trip/assets/images/activities/titiwangsa-lake-gardens/3.jpg"
        ],
        "added_date": "2025-10-13",
        "source": "proactive_research"
    }
]

# Add new activities to the list
activities.extend(new_activities)

# Save updated activities
with open('assets/js/activities-data.json', 'w') as f:
    json.dump(activities, f, indent=2)

print(f"✅ Successfully added {len(new_activities)} Nature & Parks activities!")
print(f"Total activities in database: {len(activities)}")
print(f"\nNew activities added (IDs {last_id + 1} to {last_id + 7}):")
for activity in new_activities:
    print(f"  - {activity['name']} (ID: {activity['id']})")

