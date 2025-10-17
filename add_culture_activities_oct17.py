import json
from datetime import datetime

# Read existing activities
with open('assets/js/activities-data.json', 'r') as f:
    activities = json.load(f)

# Get the next ID
next_id = max([a['id'] for a in activities]) + 1

# New Culture & Heritage activities
new_activities = [
    {
        "id": next_id,
        "name": "Islamic Arts Museum Malaysia",
        "category": "Culture & Heritage",
        "subcategory": "Museum",
        "description": "One of Southeast Asia's finest Islamic art museums, housing over 7,000 artifacts including manuscripts, textiles, ceramics, and architecture models from across the Muslim world. The museum features stunning domed ceilings, intricate calligraphy displays, and beautifully curated galleries showcasing Islamic heritage from Malaysia and beyond.",
        "location": "Jalan Lembah Perdana, near KL Sentral (about 15 min from KLCC)",
        "cost_rm": 20,
        "cost_usd": 4.5,
        "duration_hours": 2,
        "best_time": "Weekday mornings for quieter experience, open 9:30 AM - 6:00 PM daily",
        "tips": "Don't miss the stunning domed ceilings and intricate calligraphy displays. The museum cafe offers a nice break. Allow 2-3 hours to fully appreciate the collection. Photography allowed in most areas. Student discounts available with ID.",
        "photos": [
            "/KL-trip/assets/images/activities/islamic-arts-museum/1.jpg",
            "/KL-trip/assets/images/activities/islamic-arts-museum/2.jpg",
            "/KL-trip/assets/images/activities/islamic-arts-museum/3.jpg"
        ],
        "added_date": "2025-10-17",
        "source": "proactive_research",
        "tags": ["museum", "Islamic art", "culture", "history", "indoor", "group friendly", "educational"]
    },
    {
        "id": next_id + 1,
        "name": "Batu Caves",
        "category": "Culture & Heritage",
        "subcategory": "Hindu Temple & Landmark",
        "description": "Malaysia's most iconic Hindu temple complex featuring 272 vibrant rainbow-colored steps leading to limestone caves housing shrines dedicated to Lord Murugan. The site includes the massive 42.7m golden statue of Lord Murugan, Cathedral Cave with ornate Hindu shrines, and stunning natural limestone formations. A must-visit cultural landmark combining spirituality, nature, and architectural beauty.",
        "location": "Gombak, Selangor (about 30 min from KLCC via KTM train or Grab)",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 2,
        "best_time": "Early morning (7-9 AM) to avoid crowds and heat. Avoid weekends and public holidays.",
        "tips": "Wear modest clothing covering shoulders and knees. Watch out for monkeys - don't feed them or show food. The climb is steep, take your time. Bring water. Free entry to main cave. Dark Cave tour costs extra (RM 35). Best reached by KTM train to Batu Caves station.",
        "photos": [
            "/KL-trip/assets/images/activities/batu-caves/1.jpg",
            "/KL-trip/assets/images/activities/batu-caves/2.jpg",
            "/KL-trip/assets/images/activities/batu-caves/3.jpg"
        ],
        "added_date": "2025-10-17",
        "source": "proactive_research",
        "tags": ["temple", "Hindu", "landmark", "free", "outdoor", "cultural", "iconic", "photography"]
    },
    {
        "id": next_id + 2,
        "name": "Batik Painting Workshop",
        "category": "Culture & Heritage",
        "subcategory": "Cultural Workshop",
        "description": "Hands-on traditional Malaysian batik painting workshop where you learn the ancient art of wax-resist dyeing. Create your own batik artwork on fabric using traditional canting tools and vibrant dyes. Instructors guide you through the process from design to coloring, teaching the basic principles of this UNESCO-recognized craft. Take home your unique creation as a meaningful souvenir.",
        "location": "Multiple locations in KL including Ampang and Central Market area",
        "cost_rm": 60,
        "cost_usd": 13.5,
        "duration_hours": 2.5,
        "best_time": "Book in advance, morning or afternoon sessions available",
        "tips": "Wear clothes you don't mind getting dye on. The workshop is suitable for all skill levels. English-speaking instructors available. Great for groups and team building. You'll receive a certificate upon completion. The batik piece needs time to dry, so factor that into your schedule.",
        "photos": [
            "/KL-trip/assets/images/activities/batik-painting-workshop/1.jpg",
            "/KL-trip/assets/images/activities/batik-painting-workshop/2.jpg",
            "/KL-trip/assets/images/activities/batik-painting-workshop/3.jpg"
        ],
        "added_date": "2025-10-17",
        "source": "proactive_research",
        "tags": ["workshop", "batik", "traditional art", "hands-on", "cultural experience", "souvenir", "group friendly", "indoor"]
    },
    {
        "id": next_id + 3,
        "name": "Royal Selangor School of Hard Knocks",
        "category": "Culture & Heritage",
        "subcategory": "Pewter Crafting Workshop",
        "description": "Unique hands-on pewter crafting workshop at the world's largest pewter manufacturer. Learn the traditional art of pewter smithing by creating your own pewter dish or bowl. Under expert guidance, you'll hammer, engrave, and polish your creation using techniques passed down through generations. The workshop includes a factory tour and museum visit showcasing Royal Selangor's 130-year heritage.",
        "location": "Royal Selangor Visitor Centre, Setapak Jaya (about 20-25 min from KLCC)",
        "cost_rm": 85,
        "cost_usd": 19,
        "duration_hours": 1.5,
        "best_time": "Book online in advance, sessions available throughout the day",
        "tips": "Wear comfortable clothes. The workshop is suitable for ages 12+. You'll receive a certificate and take home your pewter creation. Combine with a visit to the free museum and gift shop. Great for groups. English-speaking instructors. Highly rated experience (4.8/5 from 300+ reviews).",
        "photos": [
            "/KL-trip/assets/images/activities/royal-selangor-hard-knocks/1.jpg",
            "/KL-trip/assets/images/activities/royal-selangor-hard-knocks/2.jpg",
            "/KL-trip/assets/images/activities/royal-selangor-hard-knocks/3.jpg"
        ],
        "added_date": "2025-10-17",
        "source": "proactive_research",
        "tags": ["workshop", "pewter", "crafting", "hands-on", "cultural", "souvenir", "group friendly", "unique experience"]
    },
    {
        "id": next_id + 4,
        "name": "Thean Hou Temple",
        "category": "Culture & Heritage",
        "subcategory": "Chinese Temple",
        "description": "One of Southeast Asia's largest and most beautiful Chinese temples, perched on a hilltop with panoramic views of Kuala Lumpur. This six-tiered temple combines elements of Buddhism, Taoism, and Confucianism, featuring ornate dragon columns, red lanterns, intricate carvings, and stunning architecture. The temple is especially spectacular during Chinese New Year when decorated with thousands of lanterns.",
        "location": "Robson Heights, off Jalan Syed Putra (about 15-20 min from KLCC)",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 1.5,
        "best_time": "Late afternoon for golden hour photos, or during Chinese New Year for festive decorations. Open 8 AM - 8 PM daily.",
        "tips": "Free entry, donations welcome. Photography is encouraged. Wear modest clothing. The temple offers great city views. Visit the medicinal herb garden and wishing well. Small shops sell incense and religious items. Accessible by Grab or taxi. Less crowded on weekdays.",
        "photos": [
            "/KL-trip/assets/images/activities/thean-hou-temple/1.jpg",
            "/KL-trip/assets/images/activities/thean-hou-temple/2.jpg",
            "/KL-trip/assets/images/activities/thean-hou-temple/3.jpg"
        ],
        "added_date": "2025-10-17",
        "source": "proactive_research",
        "tags": ["temple", "Chinese", "free", "cultural", "photography", "city views", "architecture", "peaceful"]
    },
    {
        "id": next_id + 5,
        "name": "KL City Gallery",
        "category": "Culture & Heritage",
        "subcategory": "City Museum & Gallery",
        "description": "Charming gallery showcasing Kuala Lumpur's history, architecture, and urban development through interactive exhibits, miniature models, and multimedia displays. Home to the famous 'I Love KL' sculpture - the city's most popular photo spot. The gallery features a spectacular miniature model of KL's cityscape, historical photographs, and cultural exhibits. Includes a gift shop and cafe.",
        "location": "Merdeka Square area, Jalan Raja (about 10 min from KLCC)",
        "cost_rm": 10,
        "cost_usd": 2.25,
        "duration_hours": 1.5,
        "best_time": "Morning or late afternoon, open 9 AM - 6:30 PM daily",
        "tips": "RM 5 of the RM 10 entrance fee is redeemable at the gift shop or cafe. Don't miss the 'I Love KL' sculpture outside for photos. The miniature city model is impressive. Good air-conditioned break from the heat. Combine with a visit to nearby Merdeka Square and Sultan Abdul Samad Building.",
        "photos": [
            "/KL-trip/assets/images/activities/kl-city-gallery/1.jpg",
            "/KL-trip/assets/images/activities/kl-city-gallery/2.jpg",
            "/KL-trip/assets/images/activities/kl-city-gallery/3.jpg"
        ],
        "added_date": "2025-10-17",
        "source": "proactive_research",
        "tags": ["museum", "city history", "I Love KL", "photography", "indoor", "affordable", "central location", "family friendly"]
    },
    {
        "id": next_id + 6,
        "name": "National Textile Museum",
        "category": "Culture & Heritage",
        "subcategory": "Museum",
        "description": "Fascinating museum dedicated to Malaysia's rich textile heritage, showcasing traditional fabrics including batik, songket, pua kumbu, and other indigenous textiles. Exhibits feature intricate weaving techniques, historical costumes, traditional tools, and the cultural significance of Malaysian textiles. The museum occupies a beautifully restored colonial building and offers insights into the craftsmanship and artistry of Southeast Asian textile traditions.",
        "location": "Jalan Sultan Hishamuddin, near Merdeka Square (about 10 min from KLCC)",
        "cost_rm": 5,
        "cost_usd": 1.15,
        "duration_hours": 1.5,
        "best_time": "Weekday mornings for quieter experience, open 9 AM - 5 PM daily",
        "tips": "Very affordable entry fee. Photography allowed. The museum is housed in a beautiful colonial building. Great for understanding Malaysian textile traditions before buying batik or songket. Air-conditioned comfort. Combine with visits to nearby National Museum or Merdeka Square. Free guided tours available on request.",
        "photos": [
            "/KL-trip/assets/images/activities/national-textile-museum/1.jpg",
            "/KL-trip/assets/images/activities/national-textile-museum/2.jpg",
            "/KL-trip/assets/images/activities/national-textile-museum/3.jpg"
        ],
        "added_date": "2025-10-17",
        "source": "proactive_research",
        "tags": ["museum", "textiles", "batik", "traditional crafts", "affordable", "cultural", "indoor", "educational"]
    }
]

# Add new activities
activities.extend(new_activities)

# Write back to file
with open('assets/js/activities-data.json', 'w') as f:
    json.dump(activities, f, indent=2, ensure_ascii=False)

print(f"Successfully added {len(new_activities)} new Culture & Heritage activities!")
print(f"New activity IDs: {next_id} to {next_id + len(new_activities) - 1}")
print(f"Total activities in database: {len(activities)}")
