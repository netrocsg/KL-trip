import json
from datetime import date

# Load existing activities
with open('assets/js/activities-data.json', 'r') as f:
    activities = json.load(f)

# New activities to add
new_activities = [
    {
        "id": 44,
        "name": "Petrosains, The Discovery Centre",
        "category": "Culture & Heritage",
        "subcategory": "Science Museum",
        "description": "An interactive science discovery center located in Suria KLCC, offering hands-on exhibits about space, geology, dinosaurs, robotics, and petroleum science. Perfect for families and science enthusiasts, Petrosains makes learning fun through engaging displays and activities that showcase Malaysia's oil and gas industry alongside general scientific principles.",
        "location": "Level 4, Suria KLCC, Kuala Lumpur City Centre",
        "cost_rm": 35,
        "cost_usd": 8,
        "duration_hours": 2.5,
        "best_time": "Weekday mornings to avoid school groups. Open 9:30 AM - 5:30 PM daily.",
        "tips": "Book tickets online for discounts. Allow 2-3 hours to explore all exhibits. Great for rainy days. Suitable for all ages. Located conveniently in KLCC shopping mall.",
        "photos": [
            "/KL-trip/assets/images/activities/petrosains-discovery-centre/1.jpg",
            "/KL-trip/assets/images/activities/petrosains-discovery-centre/2.jpg"
        ],
        "added_date": "2025-10-11",
        "source": "proactive_research"
    },
    {
        "id": 45,
        "name": "Bank Negara Malaysia Museum and Art Gallery",
        "category": "Culture & Heritage",
        "subcategory": "Museum",
        "description": "A fascinating FREE museum showcasing Malaysia's monetary history, rare coins, currency evolution, and contemporary Malaysian art. Located in the stunning Sasana Kijang building, the museum features interactive exhibits about economics and finance, making complex topics accessible and engaging. The art gallery displays rotating exhibitions of local artists.",
        "location": "Sasana Kijang, Jalan Dato Onn, Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 1.5,
        "best_time": "Open 10 AM - 5 PM, closed Mondays. Weekday afternoons are quieter.",
        "tips": "Completely FREE admission. Bring ID for registration. Photography allowed in most areas. Combine with nearby attractions. Air-conditioned and modern facilities.",
        "photos": [
            "/KL-trip/assets/images/activities/bank-negara-museum/1.jpg",
            "/KL-trip/assets/images/activities/bank-negara-museum/2.jpg"
        ],
        "added_date": "2025-10-11",
        "source": "proactive_research"
    },
    {
        "id": 46,
        "name": "National Textile Museum",
        "category": "Culture & Heritage",
        "subcategory": "Museum",
        "description": "Housed in a beautiful heritage building, this museum showcases Malaysia's rich textile traditions including batik, songket, pua kumbu, and traditional weaving techniques. The exhibits trace the evolution of Malaysian textiles from pre-historic times through trade influences, displaying intricate craftsmanship and cultural significance of fabrics from various ethnic communities.",
        "location": "Jalan Sultan Hishamuddin, near Merdeka Square",
        "cost_rm": 5,
        "cost_usd": 1.2,
        "duration_hours": 1.5,
        "best_time": "Open 9 AM - 5 PM daily. Morning visits recommended.",
        "tips": "Very affordable entry fee. Excellent for understanding Malaysian culture. Beautiful colonial architecture. Combine with Merdeka Square visit. Great photo opportunities.",
        "photos": [
            "/KL-trip/assets/images/activities/national-textile-museum/1.jpg",
            "/KL-trip/assets/images/activities/national-textile-museum/2.jpg",
            "/KL-trip/assets/images/activities/national-textile-museum/3.jpg"
        ],
        "added_date": "2025-10-11",
        "source": "proactive_research"
    },
    {
        "id": 47,
        "name": "Chan She Shu Yuen Temple",
        "category": "Culture & Heritage",
        "subcategory": "Historic Temple",
        "description": "A stunning Cantonese clan temple built between 1899-1906, featuring exquisite Shek Wan pottery decorations, intricate wood carvings, and traditional Chinese architecture. This protected heritage building showcases 100-year-old ceramic glazed tiles, curved gables resembling waves, and beautiful murals depicting Chinese folklore. A masterpiece of craftsmanship serving the Chan clan community.",
        "location": "172, Jalan Petaling, Chinatown, Kuala Lumpur",
        "cost_rm": 10,
        "cost_usd": 2.4,
        "duration_hours": 0.75,
        "best_time": "Open 10 AM - 6 PM daily. Morning light best for photography.",
        "tips": "Located in heart of Chinatown. Combine with Petaling Street market visit. Dress modestly. Excellent example of traditional Cantonese architecture. Bring camera for detailed carvings.",
        "photos": [
            "/KL-trip/assets/images/activities/chan-she-shu-yuen-temple/1.jpg",
            "/KL-trip/assets/images/activities/chan-she-shu-yuen-temple/2.jpg",
            "/KL-trip/assets/images/activities/chan-she-shu-yuen-temple/3.jpg"
        ],
        "added_date": "2025-10-11",
        "source": "proactive_research"
    },
    {
        "id": 48,
        "name": "National Art Gallery (Balai Seni Negara)",
        "category": "Culture & Heritage",
        "subcategory": "Art Gallery",
        "description": "Malaysia's premier art institution showcasing the best of Malaysian and Southeast Asian contemporary and traditional art. The gallery features rotating exhibitions, permanent collections of local artists, and cultural displays that trace the evolution of Malaysian art. Housed in a modern building with excellent facilities, it's a must-visit for art enthusiasts.",
        "location": "2 Jalan Temerloh, Off Jalan Tun Razak, Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 2,
        "best_time": "Open 9 AM - 5 PM daily (last entry 4 PM). Weekday mornings are quieter.",
        "tips": "Completely FREE admission and parking. Air-conditioned galleries. Allow 1.5-2 hours. Great for rainy days. Photography usually allowed. Check website for special exhibitions.",
        "photos": [
            "/KL-trip/assets/images/activities/national-art-gallery/1.jpg",
            "/KL-trip/assets/images/activities/national-art-gallery/2.jpg"
        ],
        "added_date": "2025-10-11",
        "source": "proactive_research"
    },
    {
        "id": 49,
        "name": "ILHAM Gallery",
        "category": "Culture & Heritage",
        "subcategory": "Contemporary Art Gallery",
        "description": "A contemporary art gallery in the heart of KL showcasing cutting-edge Malaysian and Southeast Asian art. Located in the modern Ilham Tower, the gallery features rotating exhibitions, emerging and established artists, and thought-provoking installations. The gallery also has a lovely gift shop with locally made products and art books.",
        "location": "Levels 3 & 5, Ilham Tower, 8 Jalan Binjai, Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 1.5,
        "best_time": "Open Tue-Sat 11 AM - 7 PM, Sun 11 AM - 5 PM. Closed Mondays.",
        "tips": "FREE admission. Excellent gift shop. Modern, air-conditioned space. Check website for current exhibitions. Great for contemporary art lovers. Easily accessible location.",
        "photos": [
            "/KL-trip/assets/images/activities/ilham-gallery/1.jpg",
            "/KL-trip/assets/images/activities/ilham-gallery/2.jpg"
        ],
        "added_date": "2025-10-11",
        "source": "proactive_research"
    },
    {
        "id": 50,
        "name": "Royal Selangor Visitor Centre",
        "category": "Culture & Heritage",
        "subcategory": "Cultural Experience",
        "description": "Experience Malaysia's pewter heritage at the world's largest pewter manufacturer. The FREE visitor center offers factory tours showing traditional pewter casting, design exhibits, and a massive gift shop. Watch skilled craftsmen at work and learn about the 130-year history of Royal Selangor. Optional hands-on workshops available for creating your own pewter piece.",
        "location": "4 Jalan Usahawan 6, Setapak Jaya, Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 1.5,
        "best_time": "Open 9 AM - 5 PM daily. Weekday mornings best to see craftsmen at work.",
        "tips": "Completely FREE entry and tour. Workshops available for fee. Great for souvenirs. Allow 1-2 hours. Combine with nearby attractions. Parking available.",
        "photos": [
            "/KL-trip/assets/images/activities/royal-selangor-visitor-centre/1.jpg",
            "/KL-trip/assets/images/activities/royal-selangor-visitor-centre/2.jpg"
        ],
        "added_date": "2025-10-11",
        "source": "proactive_research"
    }
]

# Add new activities to the list
activities.extend(new_activities)

# Save back to file
with open('assets/js/activities-data.json', 'w') as f:
    json.dump(activities, f, indent=2, ensure_ascii=False)

print(f"Successfully added {len(new_activities)} new activities!")
print(f"Total activities now: {len(activities)}")
print("\nNew activities added:")
for act in new_activities:
    print(f"  ID {act['id']}: {act['name']} - {act['subcategory']}")
