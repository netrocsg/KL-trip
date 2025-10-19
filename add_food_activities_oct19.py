import json
from datetime import datetime

# Read existing activities
with open('assets/js/activities-data.json', 'r') as f:
    activities = json.load(f)

# New activities to add
new_activities = [
    {
        "id": 57,
        "name": "Bijan Bar & Restaurant",
        "category": "Food & Dining",
        "subcategory": "Fine Malay Cuisine",
        "description": "A pioneer of fine Malay dining since 2003, offering exquisite traditional Malay cuisine in a refined setting with wine pairing options. Features beloved everyday favorites, forgotten heritage recipes, and regional-inspired dishes in a tranquil oasis away from bustling Changkat Bukit Bintang.",
        "location": "3 Jalan Ceylon, Kuala Lumpur (near KLCC and Bukit Bintang)",
        "cost_rm": 100,
        "cost_usd": 22,
        "duration_hours": 2,
        "best_time": "Dinner for the full fine dining experience",
        "tips": "Book in advance for groups of 8. Wine pairing available. Recently renovated in 2024 with elegant ambiance. Perfect for experiencing authentic Malay cuisine in upscale setting.",
        "photos": [
            "/KL-trip/assets/images/activities/bijan-restaurant/1.jpg",
            "/KL-trip/assets/images/activities/bijan-restaurant/2.jpg",
            "/KL-trip/assets/images/activities/bijan-restaurant/3.jpg"
        ],
        "added_date": "2025-10-19",
        "source": "proactive_research"
    },
    {
        "id": 58,
        "name": "Old China Cafe",
        "category": "Food & Dining",
        "subcategory": "Nyonya/Peranakan Cuisine",
        "description": "A charming heritage restaurant serving authentic Nyonya and Peranakan cuisine in a nostalgic colonial-era setting. Known for traditional dishes like Nyonya fried rice, curry chicken, pineapple prawns, and classic Hainanese-style preparations in Chinatown's historic atmosphere.",
        "location": "11 Jalan Balai Polis, Chinatown, Kuala Lumpur",
        "cost_rm": 20,
        "cost_usd": 4.5,
        "duration_hours": 1.5,
        "best_time": "Lunch or early dinner to avoid crowds",
        "tips": "Try the lunch combo sets for best value. Historic ambiance perfect for cultural experience. Can get busy during peak hours. Cash preferred. Great for experiencing Peranakan heritage.",
        "photos": [
            "/KL-trip/assets/images/activities/old-china-cafe/1.jpg",
            "/KL-trip/assets/images/activities/old-china-cafe/2.jpg",
            "/KL-trip/assets/images/activities/old-china-cafe/3.jpg"
        ],
        "added_date": "2025-10-19",
        "source": "proactive_research"
    },
    {
        "id": 59,
        "name": "Merchant's Lane",
        "category": "Food & Dining",
        "subcategory": "Hipster Cafe",
        "description": "A modern cafe tucked in a heritage shophouse above Petaling Street (formerly a brothel!), offering excellent coffee selection and contemporary meals. One of KL's most popular and Instagrammable cafes with a unique blend of local charm and modern aesthetics.",
        "location": "150 Jalan Petaling, Chinatown, Kuala Lumpur (upstairs)",
        "cost_rm": 35,
        "cost_usd": 7.8,
        "duration_hours": 1.5,
        "best_time": "Brunch or afternoon coffee",
        "tips": "Better suited for meals than just coffee. Closed Mondays. Book ahead for groups. Great for photos. Arrive early on weekends. Try their specialty coffee and brunch dishes.",
        "photos": [
            "/KL-trip/assets/images/activities/merchants-lane/1.jpg",
            "/KL-trip/assets/images/activities/merchants-lane/2.jpg"
        ],
        "added_date": "2025-10-19",
        "source": "proactive_research"
    },
    {
        "id": 60,
        "name": "Songket Restaurant",
        "category": "Food & Dining",
        "subcategory": "Traditional Malay with Cultural Show",
        "description": "Authentic Malay restaurant featuring traditional family recipes with optional Malaysian cultural dance performances. Offers diverse menu from rendang and satay to modern interpretations in a charming traditional bungalow setting, perfect for groups wanting culture and cuisine together.",
        "location": "No. 8, Jalan Yap Kwan Seng, Kuala Lumpur",
        "cost_rm": 55,
        "cost_usd": 12,
        "duration_hours": 2,
        "best_time": "Dinner with cultural show (check schedule)",
        "tips": "Book the cultural show package for groups - great value. Combines authentic Malay food with live traditional dance performances. Reservations recommended for groups of 8.",
        "photos": [
            "/KL-trip/assets/images/activities/songket-restaurant/1.jpg",
            "/KL-trip/assets/images/activities/songket-restaurant/2.jpg",
            "/KL-trip/assets/images/activities/songket-restaurant/3.jpg"
        ],
        "added_date": "2025-10-19",
        "source": "proactive_research"
    },
    {
        "id": 61,
        "name": "Damascus Bukit Bintang",
        "category": "Food & Dining",
        "subcategory": "Middle Eastern Cuisine",
        "description": "Syrian-inspired restaurant offering authentic Middle Eastern BBQ, shawarma, and grilled specialties. Known for delicious grilled meats, friendly service, and authentic ingredients. Popular spot in Bukit Bintang area with consistently good quality and value.",
        "location": "126 Jalan Bukit Bintang (beside Wolo Hotel), Kuala Lumpur",
        "cost_rm": 28,
        "cost_usd": 6.2,
        "duration_hours": 1,
        "best_time": "Lunch or dinner, expect queues during peak",
        "tips": "Try the mixed grill platter for sharing. Expect lines during peak hours - sign of quality! Good value for money. Great for groups. Halal certified.",
        "photos": [
            "/KL-trip/assets/images/activities/damascus-bukit-bintang/1.jpg",
            "/KL-trip/assets/images/activities/damascus-bukit-bintang/2.jpg",
            "/KL-trip/assets/images/activities/damascus-bukit-bintang/3.jpg"
        ],
        "added_date": "2025-10-19",
        "source": "proactive_research"
    },
    {
        "id": 62,
        "name": "Restoran Yut Kee",
        "category": "Food & Dining",
        "subcategory": "Hainanese Coffee Shop",
        "description": "KL's oldest surviving Hainanese kopitiam since 1928, now run by the third generation. Famous for classic Hainanese dishes like chicken chop, pork chop, charcoal-toasted bread, and traditional Hainanese coffee. A living piece of KL's culinary heritage in Chow Kit area.",
        "location": "1 Jalan Kamunting, Chow Kit, Kuala Lumpur",
        "cost_rm": 16,
        "cost_usd": 3.5,
        "duration_hours": 1,
        "best_time": "Breakfast or lunch (closes at 5pm)",
        "tips": "Try the signature pork chop and Hailam mee. Arrive early as it gets crowded. Cash only. Closed Mondays. Historic atmosphere worth experiencing. May need to share tables.",
        "photos": [
            "/KL-trip/assets/images/activities/yut-kee-restaurant/1.jpg",
            "/KL-trip/assets/images/activities/yut-kee-restaurant/2.jpg"
        ],
        "added_date": "2025-10-19",
        "source": "proactive_research"
    },
    {
        "id": 63,
        "name": "Din Tai Fung (Pavilion KL)",
        "category": "Food & Dining",
        "subcategory": "Taiwanese Dumplings",
        "description": "World-renowned Taiwanese restaurant chain famous for its meticulously crafted xiao long bao (soup dumplings) with 18 precise folds each. Offers consistent quality Taiwanese specialties including fried rice, noodles, and other dumplings. Excellent service and group-friendly.",
        "location": "Pavilion Kuala Lumpur, Level 6, 168 Jalan Bukit Bintang",
        "cost_rm": 35,
        "cost_usd": 7.8,
        "duration_hours": 1.5,
        "best_time": "Lunch or dinner, expect queues",
        "tips": "Must try the pork xiao long bao - their signature dish. Book ahead or expect wait times during peak. Great for groups. Located in convenient Pavilion mall. Order a variety to share.",
        "photos": [
            "/KL-trip/assets/images/activities/din-tai-fung-pavilion/1.jpg",
            "/KL-trip/assets/images/activities/din-tai-fung-pavilion/2.jpg",
            "/KL-trip/assets/images/activities/din-tai-fung-pavilion/3.jpg"
        ],
        "added_date": "2025-10-19",
        "source": "proactive_research"
    }
]

# Add new activities to the list
activities.extend(new_activities)

# Write back to file
with open('assets/js/activities-data.json', 'w') as f:
    json.dump(activities, f, indent=2)

print(f"Successfully added {len(new_activities)} new food activities!")
print(f"Total activities now: {len(activities)}")
