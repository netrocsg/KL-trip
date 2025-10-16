import json

# Read existing activities
with open('assets/js/activities-data.json', 'r') as f:
    activities = json.load(f)

# Get the next ID
next_id = max([a['id'] for a in activities]) + 1

# Define the 7 new activities
new_activities = [
    {
        "id": next_id,
        "name": "Camp5 Jumpa Climbing Gym",
        "category": "Adventure & Sports",
        "subcategory": "Climbing & Active Park",
        "description": "Located in the heart of Bukit Bintang at Sungei Wang Plaza, Camp5 Jumpa features 15-meter high lead walls, bouldering areas, and 9-11m top roping. The facility also includes Beastpark, an active park with ninja courses and suspended netting challenges suitable for all ages.",
        "location": "3rd Floor Jumpa Mall, Sungei Wang Plaza, Jalan Sultan Ismail, Bukit Bintang KL 59200",
        "cost_rm": {
            "weekday_active": 31.50,
            "weekend_active": 42,
            "combo_deal": 85
        },
        "cost_usd": {
            "weekday_active": 7,
            "weekend_active": 9.50,
            "combo_deal": 19
        },
        "duration_hours": 2.5,
        "best_time": "Weekdays before 4pm for off-peak pricing and fewer crowds.",
        "suitable_for": "Groups of all skill levels, ages 7+",
        "booking_required": True,
        "contact": {
            "whatsapp": "+60126673571",
            "email": "jumpa@camp5.com"
        },
        "opening_hours": "Mon-Fri 12PM-10PM, Weekends 10AM-8PM",
        "tips": "Book online to avoid queues. Wear comfortable athletic clothing. Off-peak rates apply before 4pm on weekdays. Combo deal includes both climbing and Beastpark activities.",
        "images": [],
        "tags": ["climbing", "bouldering", "ninja course", "indoor", "central location", "group friendly"]
    },
    {
        "id": next_id + 1,
        "name": "WINDLAB Indoor Skydiving",
        "category": "Adventure & Sports",
        "subcategory": "Indoor Skydiving",
        "description": "Malaysia's only indoor skydiving facility featuring a vertical wind tunnel that simulates free-fall in a safe and controlled environment. Experience the thrill of skydiving without jumping from a plane. Suitable for ages 3 to 100+ years old.",
        "location": "Level 2, 1Utama Shopping Centre, Petaling Jaya (about 30 min from Bukit Bintang)",
        "cost_rm": {
            "2_flights_offpeak": 108,
            "2_flights_peak": 138,
            "4_flights_offpeak": 168,
            "4_flights_peak": 198
        },
        "cost_usd": {
            "2_flights_offpeak": 24,
            "2_flights_peak": 31,
            "4_flights_offpeak": 38,
            "4_flights_peak": 44
        },
        "duration_hours": 1.25,
        "best_time": "Weekdays for off-peak pricing (excludes public holidays and Jan/Jul/Aug/Dec).",
        "suitable_for": "All ages 3-100+, suitable for people with disabilities",
        "booking_required": True,
        "contact": {
            "phone": "+60377285588",
            "mobile": "+60122244342"
        },
        "opening_hours": "Check website for session times",
        "tips": "Arrive 1 hour before scheduled flight time. Wear comfortable clothes and closed-toe laced shoes. All gear provided. Free viewing gallery for spectators.",
        "images": [],
        "tags": ["indoor skydiving", "wind tunnel", "unique experience", "all ages", "group friendly"]
    },
    {
        "id": next_id + 2,
        "name": "Jump Street Trampoline Park",
        "category": "Adventure & Sports",
        "subcategory": "Trampoline Park",
        "description": "Malaysia's first and biggest indoor trampoline park featuring wall-to-wall trampolines, foam pits, slam dunk zones, dodgeball courts, zipline, and high-performance areas. Over 9,000 square feet of bouncing space with various attractions suitable for all ages.",
        "location": "Petaling Jaya (near 1Utama area, about 25-30 min from Bukit Bintang)",
        "cost_rm": {
            "3hrs_night": 29,
            "3hrs_weekday": 45,
            "3hrs_public_holiday": 50,
            "whole_day": 65,
            "whole_day_public_holiday": 70
        },
        "cost_usd": {
            "3hrs_night": 6.50,
            "3hrs_weekday": 10,
            "3hrs_public_holiday": 11,
            "whole_day": 14.50,
            "whole_day_public_holiday": 15.75
        },
        "duration_hours": 3,
        "best_time": "Weekday night sessions for best pricing, weekdays generally less crowded.",
        "suitable_for": "All ages and fitness levels",
        "booking_required": True,
        "contact": {
            "website": "jumpstreetasia.com"
        },
        "opening_hours": "Check website for current hours",
        "tips": "Book tickets online in advance. Grip socks required (available for purchase). Multiple attractions including dodgeball, basketball, foam pit, zipline.",
        "images": [],
        "tags": ["trampoline", "indoor", "dodgeball", "foam pit", "zipline", "group activities"]
    },
    {
        "id": next_id + 3,
        "name": "Arena 51 Archery Tag",
        "category": "Adventure & Sports",
        "subcategory": "Combat Sport",
        "description": "Malaysia's largest Archery Tag provider offering a unique combat sport that combines elements of paintball, dodgeball, and traditional archery. Uses specially designed foam-tipped arrows making it virtually painless and mess-free. Safe for ages 10 and above.",
        "location": "Various locations in Klang Valley (mobile service, can set up at venues)",
        "cost_rm": {
            "45min_10pax": 420,
            "1hr_20pax": 720,
            "2hrs_40pax": 1250,
            "per_person_min": 31.25,
            "per_person_max": 42
        },
        "cost_usd": {
            "45min_10pax": 94,
            "1hr_20pax": 161,
            "2hrs_40pax": 280
        },
        "duration_hours": 1,
        "best_time": "Can be arranged anytime, anywhere - mobile service available.",
        "suitable_for": "Ages 10+, great for corporate team building",
        "booking_required": True,
        "contact": {
            "website": "arena51.my"
        },
        "opening_hours": "By appointment",
        "tips": "Requires 50% deposit at least 5 working days prior. All equipment and masks provided. Minimum 10 players required. Can be played indoors or outdoors.",
        "images": [],
        "tags": ["archery tag", "combat sport", "team building", "mobile service", "group activity"]
    },
    {
        "id": next_id + 4,
        "name": "Sunway Lagoon Theme Park",
        "category": "Adventure & Sports",
        "subcategory": "Theme Park",
        "description": "Malaysia's premier multi-park theme park featuring 7 different experiences: Water Park, Amusement Park, Wildlife Park, Extreme Park, Scream Park, Nickelodeon Lost Lagoon, and Lynton V Harris' Scream Park. Over 90 attractions including water slides, thrill rides, and animal encounters.",
        "location": "Sunway City, Petaling Jaya (about 30 min from Bukit Bintang)",
        "cost_rm": {
            "malaysian_min": 145,
            "malaysian_max": 180,
            "international_min": 195,
            "international_max": 245
        },
        "cost_usd": {
            "malaysian_min": 32,
            "malaysian_max": 40,
            "international_min": 44,
            "international_max": 55
        },
        "duration_hours": 9,
        "best_time": "Weekdays for fewer crowds, arrive early to maximize time.",
        "suitable_for": "All ages, families, groups",
        "booking_required": True,
        "contact": {
            "website": "sunwaylagoon.com"
        },
        "opening_hours": "Typically 10am-6pm, check website for current hours",
        "tips": "Buy tickets online to skip queues. Includes ALL 7 parks and most attractions. Bring swimwear, towels, and change of clothes. Lockers and cabana rentals available.",
        "images": [],
        "tags": ["theme park", "water park", "wildlife", "full day", "family friendly", "90+ attractions"]
    },
    {
        "id": next_id + 5,
        "name": "Skytrex Adventure Shah Alam",
        "category": "Adventure & Sports",
        "subcategory": "High Rope Course",
        "description": "Malaysia's first forest adventure park featuring high-rope obstacle courses set in a natural forest environment. Multiple circuits with varying difficulty levels from beginner to advanced, including ziplines, rope bridges, and aerial challenges.",
        "location": "Taman Botani Negara Shah Alam (about 35-40 min from Bukit Bintang)",
        "cost_rm": {
            "beginner_online": 45,
            "intermediate_online": 55,
            "advanced_online": 65,
            "park_entrance": 3
        },
        "cost_usd": {
            "beginner_online": 10,
            "intermediate_online": 12,
            "advanced_online": 14.50
        },
        "duration_hours": 2.5,
        "best_time": "Morning or late afternoon to avoid midday heat, weekdays less crowded.",
        "suitable_for": "Ages 7+, minimum height 110cm-140cm depending on circuit",
        "booking_required": True,
        "contact": {
            "website": "skytrex-adventure.com"
        },
        "opening_hours": "Check website for current hours",
        "tips": "Book tickets online in advance for better pricing. Wear comfortable athletic clothing and closed-toe shoes. Bring water and insect repellent. Safety briefing and equipment provided.",
        "images": [],
        "tags": ["high rope course", "zipline", "forest", "outdoor", "team building", "multiple difficulty levels"]
    },
    {
        "id": next_id + 6,
        "name": "VAR LIVE VR Theme Park",
        "category": "Adventure & Sports",
        "subcategory": "Virtual Reality",
        "description": "Malaysia's largest virtual reality theme park featuring 13 exciting in-house VR attractions including Zombie Jail, Crazy Rush, Super Ninja, Viking Craft, and Horror Hospital. Experience cutting-edge VR technology with somatosensory feedback and immersive multi-sensory experiences.",
        "location": "MyTOWN Shopping Centre, Kuala Lumpur (about 20-25 min from Bukit Bintang)",
        "cost_rm": {
            "single_game": 46,
            "triple_combo": 120,
            "one_day_pass": 150
        },
        "cost_usd": {
            "single_game": 10.29,
            "triple_combo": 27,
            "one_day_pass": 33.50
        },
        "duration_hours": 2,
        "best_time": "Weekdays for shorter wait times, indoor activity suitable anytime.",
        "suitable_for": "Ages with minimum height 110cm",
        "booking_required": True,
        "contact": {
            "website": "klook.com",
            "location": "MyTOWN Shopping Centre"
        },
        "opening_hours": "Check shopping mall hours",
        "tips": "Book online through Klook for better pricing. 13 different VR experiences to choose from. Includes horror, racing, shooting, and adventure games. Highly rated (4.6/5 from 418 reviews).",
        "images": [],
        "tags": ["virtual reality", "VR", "indoor", "13 experiences", "technology", "group friendly"]
    }
]

# Add new activities to the list
activities.extend(new_activities)

# Write back to file
with open('assets/js/activities-data.json', 'w') as f:
    json.dump(activities, f, indent=2)

print(f"Successfully added {len(new_activities)} new activities!")
print(f"Total activities now: {len(activities)}")
print(f"New IDs: {next_id} to {next_id + len(new_activities) - 1}")
