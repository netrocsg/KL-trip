#!/usr/bin/env python3.11
import json

# Read existing activities from assets/activities.json
with open('assets/activities.json', 'r') as f:
    activities = json.load(f)

# New activities to add (IDs 8-14)
new_activities = [
    {
        "id": 8,
        "name": "Camp5 Climbing Gym (1Utama)",
        "category": "Adventure & Sports",
        "subcategory": "Rock Climbing",
        "description": "Malaysia's flagship climbing gym featuring the country's tallest indoor climbing wall at 20m. Offers both bouldering and roped climbing (top-rope and lead) with color-coded routes for all skill levels. Air-conditioned facility with cafe and pro shop on the 5th floor of 1Utama Shopping Centre.",
        "location": "EZ501, 5th Floor, 1 Utama Shopping Centre, Bandar Utama, Petaling Jaya 47800, Selangor, Malaysia",
        "cost_rm": 38,
        "cost_usd": 8.40,
        "duration_hours": 3.5,
        "best_time": "Weekdays before 4pm for off-peak rates and fewer crowds",
        "tips": "Wear comfortable athletic clothing. Grip socks recommended for bouldering. First-timers can register for RM35 including all equipment. Multiple Camp5 locations available across KL. Book online for convenience.",
        "photos": [
            "/KL-trip/assets/images/activities/camp5-1utama/1.jpg",
            "/KL-trip/assets/images/activities/camp5-1utama/2.jpg",
            "/KL-trip/assets/images/activities/camp5-1utama/3.jpg"
        ],
        "added_date": "2025-10-12",
        "source": "proactive_research",
        "difficulty": "Easy to Advanced"
    },
    {
        "id": 9,
        "name": "Breakout Escape Room",
        "category": "Adventure & Sports",
        "subcategory": "Escape Room",
        "description": "Malaysia's largest escape room operator with 16 different themed rooms featuring high-quality props, special effects, and unique storylines. Each room offers a 55-minute challenge where teams must solve puzzles to escape. Also offers immersive Spy Game experiences with live actors.",
        "location": "Multiple locations: NU Sentral KL, Avenue K KL, The Shore Melaka",
        "cost_rm": 38,
        "cost_usd": 8.40,
        "duration_hours": 1,
        "best_time": "Weekdays for better availability, book in advance",
        "tips": "Book online in advance. Perfect for groups of 4-8 people. 15% discount if you play again within 30 days. Suitable for all ages and skill levels. Can do multiple rooms back-to-back for extended fun.",
        "photos": [
            "/KL-trip/assets/images/activities/breakout-escape-room/1.jpg",
            "/KL-trip/assets/images/activities/breakout-escape-room/2.jpg"
        ],
        "added_date": "2025-10-12",
        "source": "proactive_research",
        "difficulty": "Moderate"
    },
    {
        "id": 10,
        "name": "Windlab Indoor Skydiving",
        "category": "Adventure & Sports",
        "subcategory": "Indoor Skydiving",
        "description": "Experience the thrill of skydiving in a safe indoor environment with a 10-meter vertical wind tunnel. Professional instructors guide you through the experience of floating on air. Optional High Ride session whizzes you to the top of the tunnel for extra excitement.",
        "location": "Sunway Pyramid, Petaling Jaya, Selangor, Malaysia",
        "cost_rm": 108,
        "cost_usd": 24.00,
        "duration_hours": 1,
        "best_time": "Off-peak hours for lower rates",
        "tips": "Wear comfortable clothes, no loose items allowed. Minimum age 7 years. Great for first-time flyers and experienced skydivers. Book the High Ride for maximum thrill. Located in popular shopping mall with many dining options nearby.",
        "photos": [
            "/KL-trip/assets/images/activities/windlab-indoor-skydiving/1.jpg",
            "/KL-trip/assets/images/activities/windlab-indoor-skydiving/2.jpg"
        ],
        "added_date": "2025-10-12",
        "source": "proactive_research",
        "difficulty": "Easy"
    },
    {
        "id": 11,
        "name": "White Water Rafting (Kuala Kubu Bharu)",
        "category": "Adventure & Sports",
        "subcategory": "Water Sports",
        "description": "Grade 3-4 rapids adventure on the Selangor River, recognized as one of the best half-day rafting trips in Southeast Asia. Navigate 7km of thrilling rapids through lush rainforest with professional guides and full safety equipment. Perfect combination of adrenaline and natural beauty.",
        "location": "Selangor River, Kuala Kubu Bharu, Selangor (approximately 1 hour from KL)",
        "cost_rm": 180,
        "cost_usd": 40.00,
        "duration_hours": 2.5,
        "best_time": "Morning departures, avoid rainy season (November-January)",
        "tips": "Bring change of clothes and waterproof bag for valuables. Minimum age usually 12 years. Transport can be arranged from KL. All safety equipment provided. Great team bonding activity. Shower facilities available on-site.",
        "photos": [
            "/KL-trip/assets/images/activities/white-water-rafting-kkb/1.jpg",
            "/KL-trip/assets/images/activities/white-water-rafting-kkb/2.jpg"
        ],
        "added_date": "2025-10-12",
        "source": "proactive_research",
        "difficulty": "Moderate to Challenging"
    },
    {
        "id": 12,
        "name": "ATV Adventure Ride (Kampung Kemensah)",
        "category": "Adventure & Sports",
        "subcategory": "Off-Road Adventure",
        "description": "Off-road ATV adventure through jungle trails, riverbeds, and scenic landscapes. Ride brand new quad bikes with packages tailored to different skill levels. Experience includes stops at hidden waterfalls and local villages. No prior experience needed with full safety briefing and equipment provided.",
        "location": "Kampung Kemensah, near Taman Zoo Negara (approximately 30 minutes from KL)",
        "cost_rm": 120,
        "cost_usd": 27.00,
        "duration_hours": 2,
        "best_time": "Morning for cooler weather and better trail conditions",
        "tips": "Wear clothes you don't mind getting dirty and closed-toe shoes. Door-to-door transport available. Helmets and safety gear provided. Great for adventure seekers. Combine with waterfall visit for full experience.",
        "photos": [
            "/KL-trip/assets/images/activities/atv-adventure-kemensah/1.jpg",
            "/KL-trip/assets/images/activities/atv-adventure-kemensah/2.jpg"
        ],
        "added_date": "2025-10-12",
        "source": "proactive_research",
        "difficulty": "Easy to Moderate"
    },
    {
        "id": 13,
        "name": "Laser Battle (Sunway)",
        "category": "Adventure & Sports",
        "subcategory": "Laser Tag",
        "description": "Malaysia's largest laser tag arena with 5000 square feet of tactical gameplay. State-of-the-art equipment with interactive game modes in a futuristic arena. Multiple game scenarios available including team battles, capture the flag, and free-for-all modes. Perfect for competitive team fun.",
        "location": "Sunway Big Box, Sunway City, Petaling Jaya, Selangor",
        "cost_rm": 35,
        "cost_usd": 8.00,
        "duration_hours": 1.5,
        "best_time": "Weekdays for less crowds and better group rates",
        "tips": "Wear comfortable athletic shoes. Book for groups online for better rates. Multiple game modes available. Great for team building and friendly competition. Located in Sunway entertainment district with many dining options.",
        "photos": [
            "/KL-trip/assets/images/activities/laser-battle-sunway/1.jpg",
            "/KL-trip/assets/images/activities/laser-battle-sunway/2.jpg"
        ],
        "added_date": "2025-10-12",
        "source": "proactive_research",
        "difficulty": "Easy"
    },
    {
        "id": 14,
        "name": "Mudtrekkerz Paintball Park",
        "category": "Adventure & Sports",
        "subcategory": "Paintball",
        "description": "Malaysia's largest paintball park featuring 2 speedball fields and 3 themed scenario fields including Camelot Castle and Wild West. Corporate and family friendly facility with professional equipment and comprehensive safety gear. Multiple game modes for different group sizes and skill levels.",
        "location": "Shah Alam, Selangor (approximately 30-40 minutes from KL)",
        "cost_rm": 100,
        "cost_usd": 22.00,
        "duration_hours": 2.5,
        "best_time": "Weekends for full group experience, weekdays for private sessions",
        "tips": "Wear old clothes and closed-toe shoes. Bring change of clothes. Safety briefing mandatory. All equipment and paintballs included in packages. Great for team building and corporate events. Shower facilities available.",
        "photos": [
            "/KL-trip/assets/images/activities/mudtrekkerz-paintball/1.jpg"
        ],
        "added_date": "2025-10-12",
        "source": "proactive_research",
        "difficulty": "Easy to Moderate"
    }
]

# Add new activities to the list
activities.extend(new_activities)

# Write to both files
with open('assets/activities.json', 'w') as f:
    json.dump(activities, f, indent=2, ensure_ascii=False)

with open('assets/js/activities-data.json', 'w') as f:
    json.dump(activities, f, indent=2, ensure_ascii=False)

print(f"Successfully added {len(new_activities)} new activities!")
print(f"Total activities in database: {len(activities)}")
print("\nNew activities added:")
for act in new_activities:
    print(f"  ID {act['id']}: {act['name']}")

