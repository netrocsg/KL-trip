#!/usr/bin/env python3.11
import json
from datetime import datetime

# Read existing activities
with open('/home/ubuntu/KL-trip/assets/activities.json', 'r') as f:
    data = json.load(f)

# New Culture & Heritage activities for Oct 18, 2025
new_activities = [
    {
        "id": 36,
        "name": "Islamic Arts Museum Malaysia",
        "category": "Culture & Heritage",
        "subcategory": "Museum",
        "description": "Southeast Asia's largest Islamic arts museum featuring over 7,000 artifacts including Islamic manuscripts, textiles, ceramics, architecture models, and treasures from across the Muslim world. The museum's stunning architecture and comprehensive collection make it a must-visit for culture enthusiasts.",
        "location": "Jalan Lembah Perdana, 50480 Kuala Lumpur",
        "cost_rm": 20,
        "cost_usd": 4.5,
        "duration_hours": 2.5,
        "best_time": "Weekday mornings for fewer crowds. Museum open 9:30 AM – 6:00 PM daily.",
        "tips": "Allow at least 2 hours to explore the galleries. The museum cafe serves excellent Middle Eastern cuisine. Photography allowed in most areas. Guided tours available. Combine with nearby Lake Gardens visit.",
        "photos": [
            "/KL-trip/assets/images/activities/islamic-arts-museum/1.jpg",
            "/KL-trip/assets/images/activities/islamic-arts-museum/2.jpg",
            "/KL-trip/assets/images/activities/islamic-arts-museum/3.jpg"
        ],
        "added_date": "2025-10-18",
        "source": "proactive_research"
    },
    {
        "id": 37,
        "name": "Thean Hou Temple",
        "category": "Culture & Heritage",
        "subcategory": "Temple",
        "description": "A magnificent six-tiered Chinese temple dedicated to the Goddess of Heaven, blending Buddhism, Taoism, and Confucianism. Built in 1989 by the Hainanese community, it features ornately decorated pillars, intricate roof carvings, vibrant red lanterns, and spectacular panoramic views of Kuala Lumpur.",
        "location": "65, Persiaran Endah, Taman Persiaran Desa, 50460 Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 1.5,
        "best_time": "Early morning (8 AM) for peaceful atmosphere and soft light, or sunset for spectacular city views. Especially beautiful during Chinese New Year and Mid-Autumn Festival.",
        "tips": "Free admission. Dress modestly. Best photos from the upper levels. Visit the souvenir shop for unique gifts. The temple is beautifully lit at night. Accessible by Grab or taxi.",
        "photos": [
            "/KL-trip/assets/images/activities/thean-hou-temple/1.jpg",
            "/KL-trip/assets/images/activities/thean-hou-temple/2.jpg",
            "/KL-trip/assets/images/activities/thean-hou-temple/3.jpg"
        ],
        "added_date": "2025-10-18",
        "source": "proactive_research"
    },
    {
        "id": 38,
        "name": "National Museum of Malaysia (Muzium Negara)",
        "category": "Culture & Heritage",
        "subcategory": "Museum",
        "description": "Malaysia's premier museum showcasing the nation's history and cultural heritage through extensive collections of historical artifacts, traditional costumes, weapons, colonial-era exhibits, and cultural displays. The museum building itself is an architectural landmark with traditional Malay design elements.",
        "location": "Jalan Damansara, 50566 Kuala Lumpur",
        "cost_rm": 5,
        "cost_usd": 1.1,
        "duration_hours": 2.5,
        "best_time": "Morning hours (9 AM - 12 PM) for comfortable exploration. Open 9:00 AM – 5:00 PM daily.",
        "tips": "Very affordable admission. Audio guides available. Well air-conditioned. Photography allowed. Nearby attractions include Lake Gardens and National Mosque. Allow 2-3 hours for thorough visit.",
        "photos": [
            "/KL-trip/assets/images/activities/national-museum/1.jpg",
            "/KL-trip/assets/images/activities/national-museum/2.jpg",
            "/KL-trip/assets/images/activities/national-museum/3.jpg"
        ],
        "added_date": "2025-10-18",
        "source": "proactive_research"
    },
    {
        "id": 39,
        "name": "Bank Negara Malaysia Museum and Art Gallery",
        "category": "Culture & Heritage",
        "subcategory": "Museum",
        "description": "A world-class museum featuring rare coins, currency history, Malaysian art, and interactive exhibits about economics and finance. Housed in the striking Sasana Kijang building, this free museum offers engaging displays on Malaysia's monetary heritage and contemporary art collections.",
        "location": "Sasana Kijang, 2, Jalan Dato Onn, 50480 Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 2,
        "best_time": "Tuesday to Sunday, 10:00 AM – 5:00 PM (Closed Mondays). Weekday mornings are quietest.",
        "tips": "Free admission. Modern, well-curated exhibits. Interactive displays great for all ages. The numismatics collection is exceptional. On-site cafe. Registration required at entrance. Photography policies vary by gallery.",
        "photos": [
            "/KL-trip/assets/images/activities/bank-negara-museum/1.jpg",
            "/KL-trip/assets/images/activities/bank-negara-museum/2.jpg",
            "/KL-trip/assets/images/activities/bank-negara-museum/3.jpg"
        ],
        "added_date": "2025-10-18",
        "source": "proactive_research"
    },
    {
        "id": 40,
        "name": "Sri Kandaswamy Temple",
        "category": "Culture & Heritage",
        "subcategory": "Temple",
        "description": "The spiritual heart of Little India (Brickfields), this South Indian Hindu temple features stunning Dravidian architecture with a colorful gopuram (entrance tower) adorned with intricate sculptures of Hindu deities. Dedicated to Lord Murugan, the temple is a vibrant center of Tamil culture and community life.",
        "location": "Jalan Scott, Brickfields, 50470 Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 1,
        "best_time": "Morning or evening prayer times for authentic atmosphere. Spectacular during Thaipusam and Panguni Uthiram festivals.",
        "tips": "Free admission. Dress modestly. Remove shoes before entering. The temple canteen serves authentic South Indian vegetarian meals on banana leaves. Explore Little India neighborhood for shopping and dining. Respectful photography allowed outside.",
        "photos": [
            "/KL-trip/assets/images/activities/sri-kandaswamy-temple/1.jpg",
            "/KL-trip/assets/images/activities/sri-kandaswamy-temple/2.jpg",
            "/KL-trip/assets/images/activities/sri-kandaswamy-temple/3.jpg"
        ],
        "added_date": "2025-10-18",
        "source": "proactive_research"
    },
    {
        "id": 41,
        "name": "Masjid Jamek Sultan Abdul Samad",
        "category": "Culture & Heritage",
        "subcategory": "Mosque",
        "description": "Kuala Lumpur's oldest mosque, built in 1909 at the historic confluence of the Gombak and Klang rivers where the city was founded. Designed by Arthur Benison Hubback, the mosque beautifully blends Moorish, Indo-Saracenic, and Islamic architectural styles with onion-shaped domes, elegant minarets, and a peaceful courtyard.",
        "location": "Jalan Tun Perak, 50050 Kuala Lumpur (near Masjid Jamek LRT station)",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 0.75,
        "best_time": "Outside prayer times. Best visited in morning or late afternoon. Closed to non-Muslims during prayer times.",
        "tips": "Free admission. Modest dress required (robes and headscarves provided for visitors). Non-Muslims welcome outside prayer times. Beautiful riverside setting. Combine with nearby Central Market and Merdeka Square. Easily accessible by LRT.",
        "photos": [
            "/KL-trip/assets/images/activities/masjid-jamek/1.jpg",
            "/KL-trip/assets/images/activities/masjid-jamek/2.jpg",
            "/KL-trip/assets/images/activities/masjid-jamek/3.jpg"
        ],
        "added_date": "2025-10-18",
        "source": "proactive_research"
    },
    {
        "id": 42,
        "name": "Wilayah Mosque (Masjid Wilayah Persekutuan)",
        "category": "Culture & Heritage",
        "subcategory": "Mosque",
        "description": "A stunning modern mosque featuring magnificent blue domes and a fusion of Ottoman and Malay architectural styles. Completed in 2000, the mosque incorporates design elements from Turkey's Blue Mosque, India's Taj Mahal, and the Sheikh Zayed Grand Mosque. Known for its beautiful Islamic calligraphy, intricate geometric patterns, spectacular chandeliers, and visitor-friendly guided tours.",
        "location": "Jalan Duta, 50480 Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 1,
        "best_time": "Outside prayer times. The mosque offers special 'Mosque Tour Experience' programs with knowledgeable guides.",
        "tips": "Free admission. Guided tours available explaining Islamic architecture and practices. Dress modestly (robes provided). The interior is breathtaking with stunning marble and chandeliers. Photography allowed. Accessible by Grab/taxi (limited public transport).",
        "photos": [
            "/KL-trip/assets/images/activities/wilayah-mosque/1.jpg",
            "/KL-trip/assets/images/activities/wilayah-mosque/2.jpg"
        ],
        "added_date": "2025-10-18",
        "source": "proactive_research"
    }
]

# Add new activities to the list
data.extend(new_activities)

# Write back to file
with open('/home/ubuntu/KL-trip/assets/activities.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Successfully added {len(new_activities)} new Culture & Heritage activities!")
print(f"Total activities in database: {len(data)}")
