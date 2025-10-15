import json
from datetime import date

# Read existing activities
with open('/home/ubuntu/KL-trip/assets/js/activities-data.json', 'r') as f:
    activities = json.load(f)

# Get the next ID
next_id = max([a['id'] for a in activities]) + 1

# New cultural heritage activities
new_activities = [
    {
        "id": next_id,
        "name": "Islamic Arts Museum Malaysia",
        "category": "Culture & Heritage",
        "subcategory": "Museum",
        "description": "The largest Islamic art museum in Southeast Asia, featuring an extensive collection of Islamic manuscripts, textiles, ceramics, architecture models, and artifacts from across the Muslim world. The building itself is a stunning work of art with intricate Islamic architectural details and peaceful galleries.",
        "location": "Jalan Lembah Perdana, Kuala Lumpur",
        "cost_rm": 20,
        "cost_usd": 4.4,
        "duration_hours": 2.5,
        "best_time": "Weekday mornings for fewer crowds",
        "tips": "Dress modestly out of respect for the culture. Photography allowed without flash. The museum cafe serves excellent Middle Eastern cuisine. Allow extra time to explore the beautiful architecture.",
        "photos": [
            "/KL-trip/assets/images/activities/islamic-arts-museum/1.jpg",
            "/KL-trip/assets/images/activities/islamic-arts-museum/2.jpg",
            "/KL-trip/assets/images/activities/islamic-arts-museum/3.jpg"
        ],
        "added_date": str(date.today()),
        "source": "proactive_research"
    },
    {
        "id": next_id + 1,
        "name": "National Museum (Muzium Negara)",
        "category": "Culture & Heritage",
        "subcategory": "Museum",
        "description": "Malaysia's premier national museum showcasing the country's journey from prehistoric times to modern independence. Features four galleries with historical artifacts, traditional costumes, weapons, colonial-era exhibits, and cultural displays housed in a building with traditional Malay-style architecture and bold murals.",
        "location": "Jalan Damansara, Kuala Lumpur",
        "cost_rm": 5,
        "cost_usd": 1.1,
        "duration_hours": 2.5,
        "best_time": "Mornings to avoid afternoon heat",
        "tips": "Photography allowed without flash. No pets. Dress modestly. Very affordable and educational. Perfect for understanding Malaysian history and culture.",
        "photos": [
            "/KL-trip/assets/images/activities/national-museum/1.jpg",
            "/KL-trip/assets/images/activities/national-museum/2.jpg",
            "/KL-trip/assets/images/activities/national-museum/3.jpg"
        ],
        "added_date": str(date.today()),
        "source": "proactive_research"
    },
    {
        "id": next_id + 2,
        "name": "Thean Hou Temple",
        "category": "Culture & Heritage",
        "subcategory": "Temple",
        "description": "One of the oldest and largest Chinese temples in Southeast Asia, this six-tiered Buddhist temple is dedicated to the goddess Thean Hou. Features stunning traditional Chinese architecture with ornate decorations, red lanterns, and panoramic views of Kuala Lumpur from its hilltop location. Especially beautiful during festivals.",
        "location": "65, Persiaran Endah, Taman Persiaran Desa, Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 1.5,
        "best_time": "Early morning or late afternoon to avoid midday heat. Spectacular during Chinese New Year and Mid-Autumn Festival.",
        "tips": "Wear sunscreen and bring a hat as it's exposed on a hilltop. Not accessible via public transport - take Grab (parking RM5). Respectful dress recommended. Great for photography.",
        "photos": [
            "/KL-trip/assets/images/activities/thean-hou-temple/1.jpg",
            "/KL-trip/assets/images/activities/thean-hou-temple/2.jpg",
            "/KL-trip/assets/images/activities/thean-hou-temple/3.jpg"
        ],
        "added_date": str(date.today()),
        "source": "proactive_research"
    },
    {
        "id": next_id + 3,
        "name": "Bank Negara Malaysia Museum and Art Gallery",
        "category": "Culture & Heritage",
        "subcategory": "Museum",
        "description": "An engaging museum that makes economics and finance fascinating through interactive exhibits about Malaysian currency history, rare coins, and financial education. Also features a beautiful art gallery showcasing works by local Malaysian artists. Surprisingly interesting even for non-finance enthusiasts.",
        "location": "Sasana Kijang, Jalan Dato Onn, Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 1.75,
        "best_time": "Weekdays (closed Mondays)",
        "tips": "Large groups should book in advance. Photography allowed without flash. No pets. Free admission makes this a great value activity. Interactive exhibits are engaging for all ages.",
        "photos": [
            "/KL-trip/assets/images/activities/bank-negara-museum/1.jpg",
            "/KL-trip/assets/images/activities/bank-negara-museum/2.jpg",
            "/KL-trip/assets/images/activities/bank-negara-museum/3.jpg"
        ],
        "added_date": str(date.today()),
        "source": "proactive_research"
    },
    {
        "id": next_id + 4,
        "name": "Textile Museum (Muzium Tekstil Negara)",
        "category": "Culture & Heritage",
        "subcategory": "Museum",
        "description": "A beautiful museum housed in a historic building near Merdeka Square, showcasing Malaysia's rich textile heritage including traditional batik, songket, pua kumbu fabrics, weaving tools, and the evolution of Malaysian fashion. The intricate handwoven pieces demonstrate exceptional craftsmanship and cultural significance.",
        "location": "Jalan Sultan Hishamuddin, Kuala Lumpur (near Merdeka Square)",
        "cost_rm": 5,
        "cost_usd": 1.1,
        "duration_hours": 1.25,
        "best_time": "Mornings",
        "tips": "Keep noise down. No flash photography. Very affordable and culturally enriching. Great for appreciating traditional Malaysian crafts and textiles.",
        "photos": [
            "/KL-trip/assets/images/activities/textile-museum/1.jpg",
            "/KL-trip/assets/images/activities/textile-museum/2.jpg",
            "/KL-trip/assets/images/activities/textile-museum/3.jpg"
        ],
        "added_date": str(date.today()),
        "source": "proactive_research"
    },
    {
        "id": next_id + 5,
        "name": "Sri Mahamariamman Temple",
        "category": "Culture & Heritage",
        "subcategory": "Temple",
        "description": "Malaysia's oldest functioning Hindu temple, dating back to 1873. This intricately detailed South Indian temple features a magnificent 75-foot tall gopuram (entrance tower) adorned with colorful statues of Hindu deities. The temple is dedicated to Goddess Mariamman and remains an active place of worship in the heart of Chinatown.",
        "location": "Jalan Tun H.S. Lee, Chinatown, Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 0.75,
        "best_time": "Morning or late afternoon, avoid prayer times",
        "tips": "Remove shoes before entering. Dress modestly (shoulders and knees covered). Photography allowed in courtyard but ask permission inside. Still an active place of worship - be respectful and quiet.",
        "photos": [
            "/KL-trip/assets/images/activities/sri-mahamariamman-temple/1.jpg",
            "/KL-trip/assets/images/activities/sri-mahamariamman-temple/2.jpg",
            "/KL-trip/assets/images/activities/sri-mahamariamman-temple/3.jpg"
        ],
        "added_date": str(date.today()),
        "source": "proactive_research"
    },
    {
        "id": next_id + 6,
        "name": "Petrosains, The Discovery Centre",
        "category": "Culture & Heritage",
        "subcategory": "Science Museum",
        "description": "An award-winning interactive science discovery center created by Petronas, featuring hands-on exhibits about space, geology, dinosaurs, robotics, and petroleum science. The experience starts with a ride through the history and future of energy, making it feel like a theme park for learning. Perfect for all ages.",
        "location": "Level 4, Suria KLCC, Kuala Lumpur",
        "cost_rm": 35,
        "cost_usd": 7.7,
        "duration_hours": 3,
        "best_time": "Weekend mornings or afternoons for fewer crowds",
        "tips": "No cash accepted - card only. Book online tickets 24 hours in advance. Tickets are time-based, arrive 15 minutes early. Perfect for groups and all ages. Can easily spend 4-5 hours here.",
        "photos": [
            "/KL-trip/assets/images/activities/petrosains/1.jpg",
            "/KL-trip/assets/images/activities/petrosains/2.jpg",
            "/KL-trip/assets/images/activities/petrosains/3.jpg"
        ],
        "added_date": str(date.today()),
        "source": "proactive_research"
    }
]

# Add new activities
activities.extend(new_activities)

# Write back to file
with open('/home/ubuntu/KL-trip/assets/js/activities-data.json', 'w') as f:
    json.dump(activities, f, indent=2)

print(f"Successfully added {len(new_activities)} new cultural heritage activities!")
print(f"New activity IDs: {next_id} to {next_id + len(new_activities) - 1}")
print(f"Total activities in database: {len(activities)}")
