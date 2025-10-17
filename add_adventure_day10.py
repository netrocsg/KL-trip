#!/usr/bin/env python3.11
import json
from datetime import datetime

# Read existing activities
with open('assets/activities.json', 'r') as f:
    activities = json.load(f)

# Get the next ID
next_id = max([a['id'] for a in activities]) + 1

# New activities to add (Day 10 - Adventure & Sports)
new_activities = [
    {
        "id": next_id,
        "name": "Lalaspeed E Kart Raceway",
        "category": "Adventure & Sports",
        "subcategory": "Go-Karting",
        "description": "An outdoor electric go-kart track located on the rooftop of Lalaport BBCC, offering high-speed racing fun with four different speed modes. The 12-minute sessions cater to both casual racers and thrill-seekers, with a unique rooftop setting providing breezy racing vibes, especially during sunset.",
        "location": "Lot L5-AP-01b, Level 5 Lalaport, Bukit Bintang, 55200 Kuala Lumpur",
        "cost_rm": 62,
        "cost_usd": 14,
        "duration_hours": 0.5,
        "best_time": "Weekdays for 20% student discount and less crowded track. Sunset hours for best ambiance.",
        "tips": "Choose speed mode based on experience level. Book ahead on weekends. Located in heart of Bukit Bintang shopping district.",
        "photos": [
            "/KL-trip/assets/images/activities/lalaspeed-ekart/1.webp",
            "/KL-trip/assets/images/activities/lalaspeed-ekart/2.jpeg"
        ],
        "added_date": "2025-10-17",
        "source": "proactive_research",
        "difficulty": "Easy to Moderate"
    },
    {
        "id": next_id + 1,
        "name": "Camp5 Climbing Gym - KL Eco City",
        "category": "Adventure & Sports",
        "subcategory": "Rock Climbing",
        "description": "Southeast Asia's largest bouldering facility spread across 3000sqm, offering almost 1000sqm of bouldering, 33 top-ropes, autobelays, 2 lead lanes, dedicated kids area, fitness studio, and training walls. Features an on-site barista café with healthy meals.",
        "location": "4th Floor, KL Eco City Mall, No 3 Jalan Bangsar, Kuala Lumpur 59200",
        "cost_rm": 42,
        "cost_usd": 9,
        "duration_hours": 3,
        "best_time": "Off-peak hours before 4pm on weekdays for lower rates. Weekends 10am-8pm.",
        "tips": "Gear rental available (shoes RM5, harness RM7). First-timers welcome with orientation. Multi-gym membership allows access to all 6 Camp5 locations.",
        "photos": [
            "/KL-trip/assets/images/activities/camp5-eco-city/1.jpg",
            "/KL-trip/assets/images/activities/camp5-eco-city/2.jpg"
        ],
        "added_date": "2025-10-17",
        "source": "proactive_research",
        "difficulty": "Easy to Challenging"
    },
    {
        "id": next_id + 2,
        "name": "Jump Street Trampoline Park",
        "category": "Adventure & Sports",
        "subcategory": "Trampoline Park",
        "description": "Malaysia's first trampoline park featuring over 9,000 square feet of interconnected trampolines extending up the walls. Includes 17 different attractions: Main Court, Foam Pit, Big Airbag, High Performance area, trampoline basketball, dodgeball, and Velcro Fly Wall.",
        "location": "8A, Jalan 13/6, Seksyen 13, 46200 Petaling Jaya, Selangor",
        "cost_rm": 50,
        "cost_usd": 11,
        "duration_hours": 3,
        "best_time": "Weekday sessions for fewer crowds. Multiple 3-hour sessions available from 10am-7pm.",
        "tips": "Grip socks required (available for purchase). Great for all ages and fitness levels. Multi-visit pass offers 15% discount.",
        "photos": [
            "/KL-trip/assets/images/activities/jump-street/1.jpg",
            "/KL-trip/assets/images/activities/jump-street/2.jpg"
        ],
        "added_date": "2025-10-17",
        "source": "proactive_research",
        "difficulty": "Easy to Moderate"
    },
    {
        "id": next_id + 3,
        "name": "Windlab Indoor Skydiving Experience",
        "category": "Adventure & Sports",
        "subcategory": "Indoor Skydiving",
        "description": "Experience the thrill of skydiving without jumping from a plane. This indoor wind tunnel facility allows you to float and fly in a safe, controlled environment with professional instructors. Perfect for first-timers and experienced flyers alike.",
        "location": "Kuala Lumpur (check website for exact location)",
        "cost_rm": 118,
        "cost_usd": 26,
        "duration_hours": 2,
        "best_time": "Book in advance, especially on weekends. Sessions available throughout the day.",
        "tips": "Wear comfortable clothing. Full safety briefing provided. Great for overcoming fear of heights. Suitable for ages 7 and above.",
        "photos": [
            "/KL-trip/assets/images/activities/windlab-skydiving/1.jpg",
            "/KL-trip/assets/images/activities/windlab-skydiving/2.jpg"
        ],
        "added_date": "2025-10-17",
        "source": "proactive_research",
        "difficulty": "Easy"
    },
    {
        "id": next_id + 4,
        "name": "SKYTREX Adventure Sungai Congkak",
        "category": "Adventure & Sports",
        "subcategory": "Outdoor Adventure Park",
        "description": "An outdoor adventure park set in the rainforest featuring high-rope courses, zip lines, and obstacle courses through the treetops. Multiple difficulty levels available from beginner to advanced, offering a unique way to experience Malaysia's natural beauty.",
        "location": "Sungai Congkak, Kuala Lumpur (approximately 45 minutes from city center)",
        "cost_rm": 74,
        "cost_usd": 17,
        "duration_hours": 3,
        "best_time": "Morning sessions to avoid afternoon heat. Weekdays for fewer crowds.",
        "tips": "Wear comfortable athletic clothing and closed-toe shoes. Bring insect repellent. Full safety equipment provided. Not suitable for those afraid of heights.",
        "photos": [
            "/KL-trip/assets/images/activities/skytrex-congkak/1.jpg",
            "/KL-trip/assets/images/activities/skytrex-congkak/2.jpg"
        ],
        "added_date": "2025-10-17",
        "source": "proactive_research",
        "difficulty": "Moderate to Challenging"
    },
    {
        "id": next_id + 5,
        "name": "Berjaya Times Square Theme Park",
        "category": "Adventure & Sports",
        "subcategory": "Indoor Theme Park",
        "description": "Malaysia's largest indoor theme park covering 133,000 square feet with two exciting zones: Galaxy Station for thrill-seekers and Fantasy Garden for families. Features rides like Supersonic Odyssey roller coaster, Fantasy Labyrinth for kids, and various carnival games.",
        "location": "Berjaya Times Square, 1 Jalan Imbi, 55100 Kuala Lumpur",
        "cost_rm": 82,
        "cost_usd": 18,
        "duration_hours": 4,
        "best_time": "Weekdays for shorter queues. Open 10am-10pm daily.",
        "tips": "Located in city center mall with shopping and dining. Air-conditioned comfort. Perfect for rainy days. Height restrictions apply for some rides.",
        "photos": [
            "/KL-trip/assets/images/activities/berjaya-theme-park/1.jpg",
            "/KL-trip/assets/images/activities/berjaya-theme-park/2.jpg"
        ],
        "added_date": "2025-10-17",
        "source": "proactive_research",
        "difficulty": "Easy to Moderate"
    },
    {
        "id": next_id + 6,
        "name": "Guided Rock Climbing at Batu Caves",
        "category": "Adventure & Sports",
        "subcategory": "Rock Climbing",
        "description": "Experience outdoor rock climbing on the limestone cliffs of Batu Caves with professional guides. Suitable for first-timers and experienced climbers, this half-day adventure includes equipment, instruction, and a visit to the famous Batu Caves temple complex.",
        "location": "Batu Caves, Gombak, Selangor (approximately 30 minutes from KL city center)",
        "cost_rm": 175,
        "cost_usd": 39,
        "duration_hours": 3,
        "best_time": "Morning sessions to avoid afternoon heat. Best during dry season.",
        "tips": "All equipment provided. No experience necessary. Wear comfortable athletic clothing. Transportation to Batu Caves included in some packages. Combine with temple visit.",
        "photos": [
            "/KL-trip/assets/images/activities/batu-caves-climbing/1.jpg",
            "/KL-trip/assets/images/activities/batu-caves-climbing/2.jpg"
        ],
        "added_date": "2025-10-17",
        "source": "proactive_research",
        "difficulty": "Moderate"
    }
]

# Add new activities
activities.extend(new_activities)

# Write back to file
with open('assets/activities.json', 'w') as f:
    json.dump(activities, f, indent=2, ensure_ascii=False)

print(f"✅ Successfully added {len(new_activities)} new Adventure & Sports activities!")
print(f"📊 Total activities in database: {len(activities)}")
print(f"🆔 New activity IDs: {next_id} to {next_id + len(new_activities) - 1}")
print("\nNew activities added:")
for i, activity in enumerate(new_activities, 1):
    print(f"{i}. {activity['name']} (ID: {activity['id']}) - RM{activity['cost_rm']}")

