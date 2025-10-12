#!/usr/bin/env python3
import json
from datetime import datetime

# Load existing activities
with open('assets/js/activities-data.json', 'r') as f:
    activities = json.load(f)

# Get the last ID
last_id = max(activity['id'] for activity in activities)
print(f"Last ID: {last_id}")

# New shopping activities to add
new_activities = [
    {
        "id": 51,
        "name": "Mid Valley Megamall",
        "category": "Shopping & Markets",
        "subcategory": "Shopping Mall",
        "description": "One of Southeast Asia's largest shopping malls with over 430 stores across 5 floors. This family-friendly mega mall features major anchor tenants including Golden Screen Cinemas (18 screens), Metrojaya, Harvey Norman, and one of KL's largest MPH bookstores. The mall also includes a bowling center, food courts, and countless dining options. Connected to KL Komuter Mid Valley station for easy access.",
        "location": "Lingkaran Syed Putra, Mid Valley City, 59200 Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 3,
        "best_time": "Daily 10 AM - 10 PM. Weekdays less crowded. Evenings and weekends busiest.",
        "tips": "FREE entry. Accessible by KL Komuter train. Connected to The Gardens Mall via pedestrian bridge. Huge variety for all budgets. Air-conditioned comfort. Great for groups with diverse interests. Allow 3-4 hours minimum.",
        "photos": [
            "/KL-trip/assets/images/activities/mid-valley-megamall/1.jpg",
            "/KL-trip/assets/images/activities/mid-valley-megamall/2.jpg"
        ],
        "added_date": "2025-10-12",
        "source": "proactive_research"
    },
    {
        "id": 52,
        "name": "Sungei Wang Plaza",
        "category": "Shopping & Markets",
        "subcategory": "Shopping Mall",
        "description": "One of Kuala Lumpur's oldest and most iconic shopping malls in the heart of Bukit Bintang, offering authentic local shopping experience. With over 500 retail outlets, the mall is famous for affordable fashion, accessories, electronics, and local brands. The top floor is dedicated to youth fashion with homegrown labels. Popular with locals and budget-conscious shoppers seeking good deals and unique finds.",
        "location": "Jalan Sultan Ismail, Bukit Bintang, 55100 Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 2,
        "best_time": "Daily 10 AM - 10 PM. Best for afternoon shopping and exploring.",
        "tips": "FREE entry. Walking distance from Bukit Bintang hotels. Great for budget shopping. Bargaining possible in some stores. Cash preferred. Near Pavilion and other malls. Authentic local shopping vibe. Good for souvenirs and affordable fashion.",
        "photos": [
            "/KL-trip/assets/images/activities/sungei-wang-plaza/1.webp"
        ],
        "added_date": "2025-10-12",
        "source": "proactive_research"
    },
    {
        "id": 53,
        "name": "Plaza Low Yat",
        "category": "Shopping & Markets",
        "subcategory": "Electronics Mall",
        "description": "Kuala Lumpur's premier destination for electronics, gadgets, and technology. This 12-storey mall is Malaysia's largest IT lifestyle mall, featuring hundreds of inter-connected stores selling computers, smartphones, cameras, gaming equipment, accessories, and software. Popular with tech enthusiasts and anyone looking for competitive prices on electronics. Knowledgeable staff and wide selection make it ideal for tech shopping.",
        "location": "7, Jalan Bintang, Bukit Bintang, 55100 Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 1.5,
        "best_time": "Daily 10:30 AM - 9:30 PM. Weekday afternoons less crowded.",
        "tips": "FREE entry. Compare prices between stores. Bargaining possible. Check warranty and authenticity. Bring cash for better deals. Walking distance from Bukit Bintang area. Great for electronics, phone accessories, and gadgets. Staff generally speak English.",
        "photos": [
            "/KL-trip/assets/images/activities/plaza-low-yat/1.jpg"
        ],
        "added_date": "2025-10-12",
        "source": "proactive_research"
    },
    {
        "id": 54,
        "name": "Bangsar Village",
        "category": "Shopping & Markets",
        "subcategory": "Boutique Shopping",
        "description": "A trendy, upscale neighborhood shopping complex consisting of Bangsar Village I and II, connected by a walkway. Known as KL's friendliest and trendiest neighborhood mall, it features boutique stores, specialty shops, international brands, gourmet cafes, and fine dining restaurants. Popular with expats and locals for its relaxed atmosphere, quality shops, and excellent food options. Great for leisurely shopping and dining.",
        "location": "1 Jalan Telawi Satu, Bangsar Baru, 59100 Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 2.5,
        "best_time": "Daily 10 AM - 10 PM. Weekends popular for brunch and shopping.",
        "tips": "FREE entry. Upscale but not overly expensive. Excellent cafes and restaurants. Good for boutique shopping. Relaxed, neighborhood vibe. Parking available. Combine shopping with dining. Popular brunch destination. Easy Grab access from city center (RM 15-25).",
        "photos": [
            "/KL-trip/assets/images/activities/bangsar-village/1.jpg"
        ],
        "added_date": "2025-10-12",
        "source": "proactive_research"
    },
    {
        "id": 55,
        "name": "Publika Shopping Gallery",
        "category": "Shopping & Markets",
        "subcategory": "Art & Boutique Mall",
        "description": "A unique lifestyle shopping gallery in Solaris Dutamas blending retail, art, dining, and culture. Known for its contemporary design, art galleries, boutique stores, independent shops, and creative spaces. Features regular art exhibitions, cultural events, and a strong focus on local designers and artisans. Popular with the creative community and those seeking unique, non-mainstream shopping experiences.",
        "location": "1, Jalan Dutamas 1, Solaris Dutamas, 50480 Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 2,
        "best_time": "Daily 10 AM - 10 PM. Weekends often have special events and exhibitions.",
        "tips": "FREE entry. Unique boutiques and local designers. Art galleries worth visiting. Great cafes and restaurants. Less crowded than mainstream malls. Check for weekend events and exhibitions. Good for unique gifts and souvenirs. Parking available. Grab from city center RM 15-20.",
        "photos": [
            "/KL-trip/assets/images/activities/publika-shopping-gallery/1.jpg"
        ],
        "added_date": "2025-10-12",
        "source": "proactive_research"
    },
    {
        "id": 56,
        "name": "Chow Kit Market",
        "category": "Shopping & Markets",
        "subcategory": "Local Wet Market",
        "description": "Kuala Lumpur's largest and most vibrant traditional wet market, offering an authentic local experience. Located at the northern end of Jalan Tunku Abdul Rahman, the market has two main sections: fresh produce (fruits and vegetables) and the wet market (meat, seafood, poultry). A sensory experience showcasing Malaysian daily life, local ingredients, tropical fruits, spices, and traditional market culture. Popular with locals and adventurous tourists.",
        "location": "Jalan Raja Alang, Chow Kit, Kuala Lumpur (near Chow Kit Monorail station)",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 1,
        "best_time": "Daily 6 AM - 6 PM. Early morning (7-9 AM) best for freshest produce and authentic atmosphere.",
        "tips": "FREE entry. Take monorail to Chow Kit station. Go early for best experience. Bring cash. Watch your belongings. Not for squeamish (wet market has raw meat/seafood). Great for photography and cultural immersion. Try tropical fruits. Nearby food stalls for breakfast.",
        "photos": [
            "/KL-trip/assets/images/activities/chow-kit-market/1.jpg"
        ],
        "added_date": "2025-10-12",
        "source": "proactive_research"
    },
    {
        "id": 57,
        "name": "Taman Connaught Night Market (Pasar Malam)",
        "category": "Shopping & Markets",
        "subcategory": "Night Market",
        "description": "Malaysia's longest night market stretching over 2 kilometers with 700+ stalls. This legendary Wednesday night market in Cheras offers an incredible variety of street food, local snacks, fresh produce, clothing, accessories, household items, and more. A true Malaysian cultural experience with authentic local atmosphere, affordable prices, and endless food options. Popular with locals and increasingly with tourists seeking authentic pasar malam experience.",
        "location": "Jalan Cerdas, Taman Connaught, Cheras, Kuala Lumpur",
        "cost_rm": 0,
        "cost_usd": 0,
        "duration_hours": 2,
        "best_time": "Wednesdays only, 5 PM - 1 AM. Best time 6-9 PM for full atmosphere.",
        "tips": "FREE entry. ONLY on Wednesday evenings. Bring cash. Come hungry - incredible street food variety. Wear comfortable shoes (2km walking). Crowded but worth it. Bargaining acceptable for non-food items. Try local snacks and desserts. About 20-30 min from city center by Grab (RM 25-35).",
        "photos": [],
        "added_date": "2025-10-12",
        "source": "proactive_research"
    }
]

# Add new activities to the list
activities.extend(new_activities)

# Save updated activities
with open('assets/js/activities-data.json', 'w') as f:
    json.dump(activities, f, indent=2, ensure_ascii=False)

print(f"\nSuccessfully added {len(new_activities)} new shopping activities!")
print(f"New total: {len(activities)} activities")
print("\nAdded activities:")
for activity in new_activities:
    print(f"  {activity['id']}. {activity['name']} - {activity['subcategory']}")

