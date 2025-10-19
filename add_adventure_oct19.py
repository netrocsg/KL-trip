#!/usr/bin/env python3
"""
Add 7 new Adventure & Sports activities - Oct 19, 2025
Category rotation: Day 12 = Adventure & Sports
"""

import json
import os
from datetime import datetime

# Load existing activities
with open('assets/activities.json', 'r') as f:
    activities = json.load(f)

# Get the last ID
last_id = max(activity['id'] for activity in activities)

# New activities to add
new_activities = [
    {
        "id": last_id + 1,
        "name": "FlowRider 1 Utama Indoor Surfing",
        "category": "Adventure & Sports",
        "subcategory": "Indoor Surfing",
        "description": "Malaysia's first indoor surf park featuring a state-of-the-art FlowRider wave simulator. Experience the thrill of surfing without going to the beach, with professional instructors guiding you through bodyboarding and flowboarding techniques. Perfect for all skill levels from beginners to advanced surfers.",
        "location": "LG601, Lower Ground Floor, 1 Utama Shopping Centre E, Bandar Utama, Petaling Jaya, Selangor",
        "cost_rm": 70,
        "cost_usd": 15.5,
        "duration_hours": 1,
        "best_time": "Weekdays for lower rates (RM65/hour vs RM75 weekend). Operating hours 10:00 AM - 10:00 PM daily",
        "tips": "Wear swimwear or athletic clothing. All equipment and professional instruction included. Book online for guaranteed slots. 2-hour sessions available for RM120 weekdays, RM140 weekends. Great for groups with private session options.",
        "photos": [
            "/KL-trip/assets/images/activities/flowrider-1utama/1.jpg",
            "/KL-trip/assets/images/activities/flowrider-1utama/2.jpg",
            "/KL-trip/assets/images/activities/flowrider-1utama/3.jpg"
        ],
        "added_date": "2025-10-19",
        "source": "proactive_research",
        "difficulty": "Easy to Advanced"
    },
    {
        "id": last_id + 2,
        "name": "Bubble Sports Malaysia",
        "category": "Adventure & Sports",
        "subcategory": "Bubble Football",
        "description": "Experience the hilarious and action-packed sport of bubble football, where players are half-encased in giant inflatable zorb balls. Compete in bubble soccer, bubble rugby, and tower defense games while bouncing, bumping, and rolling across a dedicated futsal-sized field. Perfect for team building and group fun.",
        "location": "Bubble Sports MY, 2, Jalan 19/1, Seksyen 19, 46300 Petaling Jaya, Selangor",
        "cost_rm": 65,
        "cost_usd": 14.4,
        "duration_hours": 1,
        "best_time": "Weekdays 10:00 AM - 10:00 PM. Book in advance for groups of 10-20 people",
        "tips": "Wear sports attire, T-shirt, and long pants to avoid bruises. Closed-toe sports shoes required (no studs). Minimum 10 people per session. Includes warm-up, training, game time, and group photo. Great for birthdays and corporate events.",
        "photos": [
            "/KL-trip/assets/images/activities/bubble-sports/1.jpg",
            "/KL-trip/assets/images/activities/bubble-sports/2.jpg",
            "/KL-trip/assets/images/activities/bubble-sports/3.jpg"
        ],
        "added_date": "2025-10-19",
        "source": "proactive_research",
        "difficulty": "Easy to Moderate"
    },
    {
        "id": last_id + 3,
        "name": "Conquer Indoor Extreme Park",
        "category": "Adventure & Sports",
        "subcategory": "Indoor Adventure Park",
        "description": "KL's premier indoor extreme park featuring over 11 adrenaline-pumping attractions including a custom-designed Ninja Warrior course, 6 unique climbing walls with auto-belay systems, elevated high-rope course with 42 elements, Tower Jump free-fall, Air Bag Launch, and Human Gyroscope. Perfect for action movie enthusiasts and thrill-seekers.",
        "location": "Monkeys Canopy Resort, Lot 683, Jalan Persiaran Bukit Enggang Sg Long Hill, Sungai Long, 43200 Cheras, Selangor",
        "cost_rm": 110,
        "cost_usd": 24.5,
        "duration_hours": 3.5,
        "best_time": "12:00 PM - 8:00 PM daily. Weekdays for fewer crowds. Arrive early to maximize play time",
        "tips": "Grip socks and gloves mandatory for safety (available for purchase). Minimum height 130cm, weight 45-90kg for all attractions. Not recommended for pregnant women, seniors, or those with high blood pressure/epilepsy. Paying adult must accompany children under 17. No outside food allowed.",
        "photos": [
            "/KL-trip/assets/images/activities/conquer-extreme-park/1.jpg",
            "/KL-trip/assets/images/activities/conquer-extreme-park/2.jpg",
            "/KL-trip/assets/images/activities/conquer-extreme-park/3.jpg"
        ],
        "added_date": "2025-10-19",
        "source": "proactive_research",
        "difficulty": "Moderate to Challenging"
    },
    {
        "id": last_id + 4,
        "name": "X Park Sunway - Extreme Sports Theme Park",
        "category": "Adventure & Sports",
        "subcategory": "Outdoor Extreme Park",
        "description": "Malaysia's first theme park dedicated to motorized and non-motorized extreme sports. Features 24/7 pickleball courts, archery, ATV rides, badminton, bubbleball, bungee activities, dodgeball, flying fox zipline, go-karting, golf, high ropes course, paintball, and futsal. A complete outdoor adventure destination with diverse activities for all ages.",
        "location": "Jalan Tasik Selatan, Sunway South Quay, Bandar Sunway, 47500 Subang Jaya, Selangor",
        "cost_rm": 80,
        "cost_usd": 17.7,
        "duration_hours": 3,
        "best_time": "Evenings for cooler weather. Contact for specific activity pricing and availability. Multiple activities can be combined",
        "tips": "Wear comfortable outdoor clothing and closed-toe shoes. Book activities in advance. Great for groups wanting variety. Pickleball available 24/7 at Sunway South Quay location. Package deals available for multiple activities. Bring sunscreen and water.",
        "photos": [
            "/KL-trip/assets/images/activities/xpark-sunway/1.jpg",
            "/KL-trip/assets/images/activities/xpark-sunway/2.jpg",
            "/KL-trip/assets/images/activities/xpark-sunway/3.jpg"
        ],
        "added_date": "2025-10-19",
        "source": "proactive_research",
        "difficulty": "Varies by activity"
    },
    {
        "id": last_id + 5,
        "name": "Flyboard Malaysia Putrajaya",
        "category": "Adventure & Sports",
        "subcategory": "Water Sports",
        "description": "Experience the futuristic thrill of flyboarding on Putrajaya Lake. Using water jet propulsion, soar up to 15 meters above the water while performing tricks and maneuvers. Professional instructors provide comprehensive training and safety equipment. This unique water sport combines the excitement of jet skiing with the freedom of flying.",
        "location": "Putrajaya Lake, Putrajaya, Wilayah Persekutuan Putrajaya (approximately 30 minutes from KL)",
        "cost_rm": 350,
        "cost_usd": 77.5,
        "duration_hours": 0.5,
        "best_time": "Mornings or late afternoons for best weather conditions. Avoid midday heat. March to September is dry season",
        "tips": "Minimum age 15+. Wear swimwear and bring change of clothes. All safety equipment and professional instruction included. No prior experience needed. Book in advance. Great for adventure seekers and unique photo opportunities. Duo packages available for 2 people.",
        "photos": [
            "/KL-trip/assets/images/activities/flyboard-putrajaya/1.jpg",
            "/KL-trip/assets/images/activities/flyboard-putrajaya/2.jpg",
            "/KL-trip/assets/images/activities/flyboard-putrajaya/3.jpg"
        ],
        "added_date": "2025-10-19",
        "source": "proactive_research",
        "difficulty": "Moderate to Challenging"
    },
    {
        "id": last_id + 6,
        "name": "Axe Throwing at The Bomb Battle",
        "category": "Adventure & Sports",
        "subcategory": "Axe Throwing",
        "description": "Malaysia's first axe throwing arena located in Sunway Pyramid. Learn the ancient art of axe throwing in a safe, controlled environment with expert guidance. Perfect for stress relief, unique date nights, or group competitions. Multiple lanes available for competitive games and tournaments.",
        "location": "The Bomb Battle, Sunway Pyramid Shopping Mall, 3, Jalan PJS 11/15, Bandar Sunway, 47500 Petaling Jaya, Selangor",
        "cost_rm": 50,
        "cost_usd": 11.1,
        "duration_hours": 1,
        "best_time": "Weekdays for better availability. Book online in advance. Operating during mall hours",
        "tips": "Wear closed-toe shoes and comfortable clothing. All equipment and safety briefing provided. Minimum age requirements apply. Great for team building and competitive groups. Combine with other activities at Sunway Pyramid. No prior experience needed.",
        "photos": [
            "/KL-trip/assets/images/activities/axe-throwing-sunway/1.jpg",
            "/KL-trip/assets/images/activities/axe-throwing-sunway/2.jpg",
            "/KL-trip/assets/images/activities/axe-throwing-sunway/3.jpg"
        ],
        "added_date": "2025-10-19",
        "source": "proactive_research",
        "difficulty": "Easy to Moderate"
    },
    {
        "id": last_id + 7,
        "name": "Sunway Lagoon Bungee Jump",
        "category": "Adventure & Sports",
        "subcategory": "Bungee Jumping",
        "description": "Take the ultimate leap of faith with a 21-meter bungee jump from Malaysia's longest pedestrian suspension bridge at Sunway Lagoon. Experience the adrenaline rush of free-falling with spectacular views of the theme park. Professional staff ensure safety while you conquer your fears in this iconic extreme sport.",
        "location": "Sunway Lagoon Theme Park, 3, Jalan PJS 11/11, Bandar Sunway, 47500 Subang Jaya, Selangor",
        "cost_rm": 40,
        "cost_usd": 8.9,
        "duration_hours": 0.5,
        "best_time": "During Sunway Lagoon operating hours 11:00 AM - 5:00 PM. Weekdays for shorter queues",
        "tips": "Requires Sunway Lagoon admission ticket (RM202 adult). Weight and health restrictions apply. Sign waiver before jumping. Wear comfortable clothing. Combine with other Sunway Lagoon attractions for full day experience. Video recording available for purchase.",
        "photos": [
            "/KL-trip/assets/images/activities/sunway-bungee/1.jpg",
            "/KL-trip/assets/images/activities/sunway-bungee/2.jpg",
            "/KL-trip/assets/images/activities/sunway-bungee/3.jpg"
        ],
        "added_date": "2025-10-19",
        "source": "proactive_research",
        "difficulty": "Extreme"
    }
]

# Add new activities to the list
activities.extend(new_activities)

# Save updated activities
with open('assets/activities.json', 'w') as f:
    json.dump(activities, f, indent=2)

print(f"✅ Successfully added {len(new_activities)} new Adventure & Sports activities!")
print(f"📊 Total activities in database: {len(activities)}")
print(f"🆔 New activity IDs: {last_id + 1} to {last_id + len(new_activities)}")
print("\nNew activities added:")
for activity in new_activities:
    print(f"  - {activity['name']} (ID: {activity['id']})")

