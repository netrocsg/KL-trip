#!/usr/bin/env python3
"""
Add 7 Culture & Heritage activities for Day 10 (October 18, 2025)
"""

import json
from datetime import datetime

# Load existing activities
with open('assets/js/activities-data.json', 'r') as f:
    activities = json.load(f)

# New activities to add (IDs 43-49)
new_activities = [
    {
        "id": 43,
        "name": "Islamic Arts Museum Malaysia",
        "category": "Culture & Heritage",
        "subcategory": "Museum",
        "description": "The largest Islamic arts museum in Southeast Asia, featuring over 12 galleries showcasing more than a millennium of Islamic art, design, and culture. Collections include textiles, manuscripts, ceramics, jewelry, and architectural elements from across the Islamic world.",
        "location": "Jalan Lembah Perdana, 50480 Kuala Lumpur (near National Mosque and Perdana Botanical Gardens)",
        "cost_rm": 20,
        "cost_usd": 4.50,
        "duration_hours": 1.5,
        "best_time": "Weekday mornings for quieter experience. Open 9:30 AM - 6:00 PM daily.",
        "tips": "No booking required for general visits. Museum shop and cafe on site. Photography allowed without flash. Combine with visit to National Mosque nearby. Near Pasar Seni LRT station (10-minute walk).",
        "photos": [
            "/KL-trip/assets/images/activities/islamic-arts-museum/1.jpg",
            "/KL-trip/assets/images/activities/islamic-arts-museum/2.jpg",
            "/KL-trip/assets/images/activities/islamic-arts-museum/3.jpg"
        ],
        "added_date": "2025-10-18",
        "source": "proactive_research"
    },
    {
        "id": 44,
        "name": "Bank Negara Malaysia Museum and Art Gallery",
        "category": "Culture & Heritage",
        "subcategory": "Museum",
        "description": "A unique combination of museum and art gallery focusing on Malaysian economic history, currency, and contemporary art. Features interactive exhibits on banking, economics, and financial literacy, plus rotating art exhibitions.",
        "location": "Sasana Kijang, 2 Jalan Dato' Onn, 50480 Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 1.5,
        "best_time": "Weekday mornings. Open Tuesday-Sunday, 10:00 AM - 5:00 PM (Closed Mondays).",
        "tips": "FREE admission. Free guided tours available by trained museum guides. Educational and family-friendly. Air-conditioned. Photography allowed. Last admission at 4:30 PM. Near KL Sentral, accessible by LRT/MRT.",
        "photos": [
            "/KL-trip/assets/images/activities/bank-negara-museum/1.jpg",
            "/KL-trip/assets/images/activities/bank-negara-museum/2.jpg",
            "/KL-trip/assets/images/activities/bank-negara-museum/3.jpg"
        ],
        "added_date": "2025-10-18",
        "source": "proactive_research"
    },
    {
        "id": 45,
        "name": "Thean Hou Temple",
        "category": "Culture & Heritage",
        "subcategory": "Temple",
        "description": "One of the oldest and largest Chinese temples in Southeast Asia, this six-tiered Buddhist temple is dedicated to the goddess Tian Hou (Mazu). Features stunning traditional architecture, ornate decorations, beautiful gardens, and panoramic city views.",
        "location": "65 Persiaran Endah, Off Jalan Syed Putra, 50460 Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 1,
        "best_time": "Early morning or late afternoon for best lighting. Open 8:00 AM - 8:00 PM daily.",
        "tips": "FREE admission (RM5 parking fee per vehicle). Not accessible by public transport - take Grab/taxi (15-20 min from city center). Dress modestly. Great for photography. Especially beautiful during Chinese New Year and Mid-Autumn Festival.",
        "photos": [
            "/KL-trip/assets/images/activities/thean-hou-temple/1.jpg",
            "/KL-trip/assets/images/activities/thean-hou-temple/2.jpg",
            "/KL-trip/assets/images/activities/thean-hou-temple/3.jpg"
        ],
        "added_date": "2025-10-18",
        "source": "proactive_research"
    },
    {
        "id": 46,
        "name": "National Textile Museum",
        "category": "Culture & Heritage",
        "subcategory": "Museum",
        "description": "Housed in a beautiful colonial building, this museum showcases Malaysia's rich textile heritage across 4 galleries. Exhibits include traditional Malay textiles, batik, songket, ceremonial costumes, and the evolution of Malaysian fashion.",
        "location": "Jalan Sultan Hishamuddin, 50050 Kuala Lumpur (near Merdeka Square)",
        "cost_rm": 5,
        "cost_usd": 1.20,
        "duration_hours": 1,
        "best_time": "Weekday mornings. Open 9:00 AM - 6:00 PM daily.",
        "tips": "Free entrance with registration (sign-in required). Well-displayed exhibits with good descriptions. Near Masjid Jamek LRT Station (5-minute walk). Combine with Merdeka Square visit.",
        "photos": [
            "/KL-trip/assets/images/activities/national-textile-museum/1.jpg",
            "/KL-trip/assets/images/activities/national-textile-museum/2.jpg",
            "/KL-trip/assets/images/activities/national-textile-museum/3.jpg"
        ],
        "added_date": "2025-10-18",
        "source": "proactive_research"
    },
    {
        "id": 47,
        "name": "Kuala Lumpur City Gallery",
        "category": "Culture & Heritage",
        "subcategory": "Gallery",
        "description": "An architectural gallery showcasing KL's history, development, and future through exhibits, models, and multimedia displays. Features the famous 'I Love KL' sign and a spectacular miniature model of the city.",
        "location": "27 Jalan Raja, Dataran Merdeka, 50050 Kuala Lumpur",
        "cost_rm": 10,
        "cost_usd": 2.25,
        "duration_hours": 1,
        "best_time": "Morning or late afternoon. Open 9:00 AM - 6:30 PM daily.",
        "tips": "RM10 per person (RM5 redeemable at gift shop or cafe). Great introduction to KL's history. Photo opportunity with 'I Love KL' sign outside. Gift shop has unique KL souvenirs. Located at Merdeka Square. Near Masjid Jamek LRT Station (5-minute walk).",
        "photos": [
            "/KL-trip/assets/images/activities/kl-city-gallery/1.jpg",
            "/KL-trip/assets/images/activities/kl-city-gallery/2.jpg",
            "/KL-trip/assets/images/activities/kl-city-gallery/3.jpg"
        ],
        "added_date": "2025-10-18",
        "source": "proactive_research"
    },
    {
        "id": 48,
        "name": "Royal Selangor Visitor Centre",
        "category": "Culture & Heritage",
        "subcategory": "Cultural Workshop",
        "description": "Discover Malaysia's pewter heritage at the world's largest pewter manufacturer. Includes factory tour, museum showcasing Royal Selangor's 140-year history, and hands-on workshops where visitors can craft their own pewter items.",
        "location": "4 Jalan Usahawan 6, Setapak Jaya, 53300 Kuala Lumpur",
        "cost_rm": 80,
        "cost_usd": 18,
        "duration_hours": 2.5,
        "best_time": "Weekday mornings for less crowded workshops. Open 9:00 AM - 5:00 PM daily.",
        "tips": "Factory tour FREE, Workshops RM80-150. Book workshops online in advance (popular). Most popular: The Foundry Workshop (30 mins, RM80). Take home your handmade pewter creation. Gift shop with full product range. 15-20 min drive from city center (Grab/taxi recommended).",
        "photos": [
            "/KL-trip/assets/images/activities/royal-selangor-centre/1.jpg",
            "/KL-trip/assets/images/activities/royal-selangor-centre/2.jpg",
            "/KL-trip/assets/images/activities/royal-selangor-centre/3.jpg"
        ],
        "added_date": "2025-10-18",
        "source": "proactive_research"
    },
    {
        "id": 49,
        "name": "Sri Mahamariamman Temple",
        "category": "Culture & Heritage",
        "subcategory": "Temple",
        "description": "Kuala Lumpur's oldest and largest Hindu temple, built in 1873. Features stunning Dravidian architecture with an ornate 5-tier gopuram (tower) adorned with colorful Hindu deities. The interior is richly decorated with gold, silver, and precious stones.",
        "location": "Jalan Tun H S Lee, Chinatown, 50000 Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 0.5,
        "best_time": "Early morning or evening for prayer ceremonies. Open 6:00 AM - 9:00 PM daily.",
        "tips": "FREE admission (small donation appreciated). Dress modestly (shoulders and knees covered). Remove shoes before entering. Photography allowed but be respectful during prayers. Located in Chinatown - combine with Petaling Street visit. Beautiful from outside at night when lit up. Pasar Seni LRT Station (5-minute walk).",
        "photos": [
            "/KL-trip/assets/images/activities/sri-mahamariamman-temple/1.jpg",
            "/KL-trip/assets/images/activities/sri-mahamariamman-temple/2.jpg",
            "/KL-trip/assets/images/activities/sri-mahamariamman-temple/3.jpg"
        ],
        "added_date": "2025-10-18",
        "source": "proactive_research"
    }
]

# Add new activities to the list
activities.extend(new_activities)

# Save updated activities
with open('assets/js/activities-data.json', 'w') as f:
    json.dump(activities, f, indent=2)

print(f"✅ Successfully added 7 new Culture & Heritage activities!")
print(f"📊 Total activities in database: {len(activities)}")
print(f"🆔 New activity IDs: 43-49")
print("\nNew activities added:")
for activity in new_activities:
    print(f"  - {activity['name']} (ID: {activity['id']})")

