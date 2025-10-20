#!/usr/bin/env python3.11
import json

# Read existing activities
with open('assets/js/activities-data.json', 'r') as f:
    activities = json.load(f)

# Get the next ID
next_id = max([a['id'] for a in activities]) + 1

# New culture & heritage activities
new_activities = [
    {
        "id": next_id,
        "name": "Islamic Arts Museum Malaysia",
        "category": "Culture & Heritage",
        "subcategory": "Museum",
        "description": "The largest museum of Islamic arts in Southeast Asia, housing over 7,000 artifacts from across the Islamic world. Features stunning architecture with intricate Islamic designs, multiple galleries showcasing textiles, ceramics, jewelry, manuscripts, and architectural elements from various Islamic civilizations.",
        "location": "Jalan Lembah Perdana, 50480 Kuala Lumpur, Malaysia",
        "cost_rm": 14,
        "cost_usd": 3.10,
        "duration_hours": 2.5,
        "best_time": "Weekday mornings for fewer crowds, any day 9:30 AM - 6:00 PM",
        "tips": "Don't miss the Islamic Architecture gallery with scale models of famous mosques. The museum restaurant serves excellent Middle Eastern cuisine. Photography allowed without flash. Very well-maintained and air-conditioned.",
        "photos": [
            "/KL-trip/assets/images/activities/islamic-arts-museum/1.jpg",
            "/KL-trip/assets/images/activities/islamic-arts-museum/2.jpg",
            "/KL-trip/assets/images/activities/islamic-arts-museum/3.jpg"
        ],
        "added_date": "2025-10-20",
        "source": "proactive_research"
    },
    {
        "id": next_id + 1,
        "name": "National Museum (Muzium Negara)",
        "category": "Culture & Heritage",
        "subcategory": "Museum",
        "description": "Malaysia's premier museum showcasing the country's history, culture, and heritage. Features traditional Malay architecture with four main galleries covering Early History, Malay Kingdoms, Colonial Era, and Malaysia Today. Extensive collection of artifacts, traditional costumes, and historical exhibits.",
        "location": "Jalan Damansara, 50566 Kuala Lumpur, Malaysia",
        "cost_rm": 2,
        "cost_usd": 0.45,
        "duration_hours": 2,
        "best_time": "Weekday afternoons, daily 9:00 AM - 6:00 PM",
        "tips": "Extremely affordable entry. The building itself is an architectural gem with traditional Minangkabau-style roof. Start from the top floor and work your way down. Air-conditioned and well-maintained. Great introduction to Malaysian history.",
        "photos": [
            "/KL-trip/assets/images/activities/national-museum/1.jpg",
            "/KL-trip/assets/images/activities/national-museum/2.jpg",
            "/KL-trip/assets/images/activities/national-museum/3.jpg"
        ],
        "added_date": "2025-10-20",
        "source": "proactive_research"
    },
    {
        "id": next_id + 2,
        "name": "Bank Negara Malaysia Museum and Art Gallery",
        "category": "Culture & Heritage",
        "subcategory": "Museum",
        "description": "A unique museum combining economics, numismatics (currency history), and contemporary art. Features interactive galleries on Malaysian economy, history of money, children's gallery, and rotating art exhibitions. Modern, engaging displays with multimedia elements housed in the architecturally impressive Sasana Kijang building.",
        "location": "Sasana Kijang, 2 Jalan Dato' Onn, 50480 Kuala Lumpur, Malaysia",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 1.5,
        "best_time": "Weekday mornings, Tuesday-Sunday 10:00 AM - 5:00 PM (closed Mondays)",
        "tips": "Completely free admission and free guided tours available. Bags not allowed inside but lockers provided. Very educational and family-friendly. The building architecture is worth seeing. Last admission at 4:30 PM.",
        "photos": [
            "/KL-trip/assets/images/activities/bank-negara-museum/1.jpg",
            "/KL-trip/assets/images/activities/bank-negara-museum/2.jpg",
            "/KL-trip/assets/images/activities/bank-negara-museum/3.jpg"
        ],
        "added_date": "2025-10-20",
        "source": "proactive_research"
    },
    {
        "id": next_id + 3,
        "name": "Thean Hou Temple",
        "category": "Culture & Heritage",
        "subcategory": "Temple",
        "description": "One of the largest and oldest Chinese temples in Southeast Asia. Six-tiered pagoda-style temple dedicated to the goddess Tian Hou (Mazu). Features ornate architecture, beautiful red lanterns, prayer halls, and stunning panoramic views of Kuala Lumpur skyline. Represents a harmonious blend of Buddhism, Taoism, and Confucianism.",
        "location": "65 Persiaran Endah, Taman Persiaran Desa, 50460 Kuala Lumpur, Malaysia",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 1.25,
        "best_time": "Late afternoon for sunset views, or during Chinese festivals for special decorations. Open daily 8:00 AM - 8:00 PM",
        "tips": "Not easily accessible by public transport - take Grab (RM5 parking fee). Beautiful photo opportunities especially with red lanterns. Respectful dress recommended. Incense available for purchase. Great city views from temple grounds.",
        "photos": [
            "/KL-trip/assets/images/activities/thean-hou-temple/1.jpg",
            "/KL-trip/assets/images/activities/thean-hou-temple/2.jpg"
        ],
        "added_date": "2025-10-20",
        "source": "proactive_research"
    },
    {
        "id": next_id + 4,
        "name": "Sri Mahamariamman Temple",
        "category": "Culture & Heritage",
        "subcategory": "Temple",
        "description": "The oldest functioning Hindu temple in Kuala Lumpur, founded in 1873. Features stunning South Indian Dravidian architecture with an ornate 5-tiered Raja Gopuram (tower) adorned with hundreds of colorful Hindu deities and intricate carvings. Active place of worship with daily rituals and ceremonies.",
        "location": "Jalan Tun H S Lee (Jalan Bandar), Chinatown, 50000 Kuala Lumpur, Malaysia",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 0.75,
        "best_time": "Morning or late afternoon, avoid peak prayer times. Open daily 6:00 AM - 9:00 PM",
        "tips": "Remove shoes before entering. Dress modestly (shoulders and knees covered). Photography of exterior allowed, ask permission for interior. Located in Chinatown, easy to combine with other attractions. Witness daily rituals if visiting early morning.",
        "photos": [
            "/KL-trip/assets/images/activities/sri-mahamariamman-temple/1.jpg",
            "/KL-trip/assets/images/activities/sri-mahamariamman-temple/2.jpg",
            "/KL-trip/assets/images/activities/sri-mahamariamman-temple/3.jpg"
        ],
        "added_date": "2025-10-20",
        "source": "proactive_research"
    },
    {
        "id": next_id + 5,
        "name": "Chan See Shu Yuen Temple",
        "category": "Culture & Heritage",
        "subcategory": "Heritage Building",
        "description": "The oldest and most ornate Chinese clan house in Kuala Lumpur, completed in 1906. Stunning example of traditional Cantonese architecture with intricate ceramic sculptures, detailed wood carvings, and elaborate roof decorations featuring mythical creatures and scenes from Chinese folklore. Originally built as a clan association for the Chan family.",
        "location": "172 Jalan Petaling, Chinatown, 50000 Kuala Lumpur, Malaysia",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 0.75,
        "best_time": "Morning light is best for photography. Open daily 9:00 AM - 5:00 PM",
        "tips": "Located at the southern end of Petaling Street (Chinatown). One of the best-preserved heritage buildings in KL. Amazing photo opportunities with detailed ceramic roof decorations. Often less crowded than other temples. Combine with Chinatown walking tour.",
        "photos": [
            "/KL-trip/assets/images/activities/chan-see-shu-yuen-temple/1.jpg",
            "/KL-trip/assets/images/activities/chan-see-shu-yuen-temple/2.jpg"
        ],
        "added_date": "2025-10-20",
        "source": "proactive_research"
    },
    {
        "id": next_id + 6,
        "name": "Kuala Lumpur City Gallery",
        "category": "Culture & Heritage",
        "subcategory": "Gallery",
        "description": "Interactive gallery showcasing Kuala Lumpur's history, architecture, and urban development. Features the famous 'I Love KL' sculpture outside, detailed miniature model of the city (KLCC model), historical exhibits, and rotating art displays. Great introduction to KL's transformation from tin mining town to modern metropolis.",
        "location": "27 Jalan Raja, Dataran Merdeka, 50050 Kuala Lumpur, Malaysia",
        "cost_rm": 10,
        "cost_usd": 2.20,
        "duration_hours": 1,
        "best_time": "Morning or late afternoon. Open daily 9:00 AM - 6:30 PM",
        "tips": "RM5 of the RM10 entry fee is redeemable at the gift shop. Must-see: the giant KLCC miniature model. Perfect starting point for Merdeka Square walking tour. The 'I Love KL' sculpture outside is a popular photo spot. Air-conditioned and well-curated. Gift shop has quality local souvenirs.",
        "photos": [
            "/KL-trip/assets/images/activities/kl-city-gallery/1.jpg",
            "/KL-trip/assets/images/activities/kl-city-gallery/2.jpg",
            "/KL-trip/assets/images/activities/kl-city-gallery/3.jpg"
        ],
        "added_date": "2025-10-20",
        "source": "proactive_research"
    }
]

# Add new activities to the list
activities.extend(new_activities)

# Write back to file
with open('assets/js/activities-data.json', 'w') as f:
    json.dump(activities, f, indent=2)

print(f"Successfully added {len(new_activities)} new Culture & Heritage activities!")
print(f"New IDs: {next_id} to {next_id + len(new_activities) - 1}")
print(f"Total activities in database: {len(activities)}")

