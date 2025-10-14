import json
from datetime import datetime

# Read existing activities
with open('/home/ubuntu/KL-trip/assets/activities.json', 'r') as f:
    activities = json.load(f)

# Get the next ID
next_id = max([a['id'] for a in activities]) + 1

# New nightlife activities
new_activities = [
    {
        "id": next_id,
        "name": "Sky51 at EQ Hotel",
        "category": "Nightlife & Entertainment",
        "subcategory": "Rooftop Bar & Restaurant",
        "description": "Asia's Top 5 Rooftop Bar features fine dining at Sabayon restaurant, a speakeasy bar, and an alfresco terrace with spectacular views of Petronas Twin Towers and KL Tower. The 'Go Lokal' cocktail menu uses ethnic Malaysian flavours and locally-derived distillates for a unique drinking experience. Also features Blue lounge with live music performances and VIP upper deck with live DJs on weekends.",
        "location": "51st Floor, EQ Hotel, Equatorial Plaza, Jalan Sultan Ismail, 50450 Kuala Lumpur",
        "cost_rm": 60,
        "cost_usd": 13,
        "duration_hours": 2.5,
        "best_time": "Sunset hours or weekends for live DJ performances",
        "tips": "Book in advance for weekends. VIP upper deck has live DJs. Also visit Blue lounge for live music. Smart casual dress code after 9pm. Try the signature 'Go Lokal' cocktails featuring Malaysian ingredients.",
        "photos": [
            "/KL-trip/assets/images/activities/sky51-eq-hotel/1.jpg",
            "/KL-trip/assets/images/activities/sky51-eq-hotel/2.jpg",
            "/KL-trip/assets/images/activities/sky51-eq-hotel/3.jpg"
        ],
        "added_date": "2025-10-14",
        "source": "proactive_research"
    },
    {
        "id": next_id + 1,
        "name": "Heli Lounge Bar",
        "category": "Nightlife & Entertainment",
        "subcategory": "Helipad Rooftop Bar",
        "description": "A functioning helipad that transforms into an upscale rooftop bar at night, offering one of KL's most unique drinking experiences. Sunset views at golden hour are spectacular, with panoramic city skyline vistas from this open-air venue on the 34th floor of Menara KH.",
        "location": "34th Floor, Menara KH, Jalan Sultan Ismail, 50450 Kuala Lumpur",
        "cost_rm": 50,
        "cost_usd": 11,
        "duration_hours": 1.5,
        "best_time": "Sunset/golden hour (6-7pm)",
        "tips": "Arrive before sunset for best views. Smart casual dress code after 9pm (no slippers, flip-flops, sandals, bermudas). Limited capacity so arrive early on weekends. Entry fee includes one drink.",
        "photos": [
            "/KL-trip/assets/images/activities/heli-lounge-bar/1.jpg",
            "/KL-trip/assets/images/activities/heli-lounge-bar/2.jpg",
            "/KL-trip/assets/images/activities/heli-lounge-bar/3.jpg"
        ],
        "added_date": "2025-10-14",
        "source": "proactive_research"
    },
    {
        "id": next_id + 2,
        "name": "Marini's on 57",
        "category": "Nightlife & Entertainment",
        "subcategory": "Rooftop Bar & Italian Restaurant",
        "description": "Luxurious rooftop bar, upscale Italian restaurant, and whiskey lounge with magical panoramic views and up-close vistas of the famous Petronas Towers from the 57th floor. Award-winning mixologists create signature cocktails served alongside Italian bar bites and pizzas in a trendy, festive atmosphere.",
        "location": "57th Floor, Petronas Tower 3, KLCC, Kuala Lumpur",
        "cost_rm": 85,
        "cost_usd": 19,
        "duration_hours": 2.5,
        "best_time": "Sunset hour (5-9pm) for favorable drink prices",
        "tips": "Happy hour offers better prices. Book ahead for window seats with Petronas views. Dress smart casual. Try the Italian pizzas and bar bites. Whiskey lounge has extensive selection.",
        "photos": [
            "/KL-trip/assets/images/activities/marinis-on-57/1.jpg",
            "/KL-trip/assets/images/activities/marinis-on-57/2.jpg",
            "/KL-trip/assets/images/activities/marinis-on-57/3.jpg"
        ],
        "added_date": "2025-10-14",
        "source": "proactive_research"
    },
    {
        "id": next_id + 3,
        "name": "PS150 Speakeasy",
        "category": "Nightlife & Entertainment",
        "subcategory": "Speakeasy Bar",
        "description": "A hidden speakeasy bar disguised as a vintage toy shop in Chinatown, featuring three distinct areas: the Red Opium Den with intimate booths, an airy outdoor courtyard, and the Main Bar with pre-war character. The extensive cocktail menu covers five distinct eras of mixology in a cosy, dimly lit, intimate setting.",
        "location": "Jalan Petaling (Petaling Street), Chinatown, Kuala Lumpur (entrance through 'Cheng And Huang Toys and Co' toy shop)",
        "cost_rm": 52,
        "cost_usd": 11,
        "duration_hours": 2.5,
        "best_time": "Weekday evenings for relaxed vibe, weekends for buzzing atmosphere",
        "tips": "Book ahead for weekend seating, otherwise can stand at bar. Look for the toy shop facade and bouncer at door. Try their classic negronis or era-themed cocktails. No flip-flops allowed.",
        "photos": [
            "/KL-trip/assets/images/activities/ps150-speakeasy/1.jpg",
            "/KL-trip/assets/images/activities/ps150-speakeasy/2.jpg",
            "/KL-trip/assets/images/activities/ps150-speakeasy/3.jpg"
        ],
        "added_date": "2025-10-14",
        "source": "proactive_research"
    },
    {
        "id": next_id + 4,
        "name": "Zouk Club KL",
        "category": "Nightlife & Entertainment",
        "subcategory": "Nightclub",
        "description": "Malaysia's premier nightlife destination offering a dynamic clubbing experience with world-class international DJs, multiple rooms with different music genres, and a vibrant party ambiance. One of Southeast Asia's most famous nightclubs with state-of-the-art sound and lighting systems.",
        "location": "436 Jalan Tun Razak, Kelab Golf di Raja Selangor, 50400 Kuala Lumpur",
        "cost_rm": 75,
        "cost_usd": 16,
        "duration_hours": 4,
        "best_time": "Friday and Saturday nights (open until 5am)",
        "tips": "Arrive after midnight for peak atmosphere. Check DJ lineup in advance on their website. Dress code enforced (smart casual, no slippers/shorts). Can get very crowded on weekends. Multiple rooms offer different music styles.",
        "photos": [
            "/KL-trip/assets/images/activities/zouk-club-kl/1.jpg",
            "/KL-trip/assets/images/activities/zouk-club-kl/2.jpg",
            "/KL-trip/assets/images/activities/zouk-club-kl/3.jpg"
        ],
        "added_date": "2025-10-14",
        "source": "proactive_research"
    },
    {
        "id": next_id + 5,
        "name": "Jao Tim Jazz Bar",
        "category": "Nightlife & Entertainment",
        "subcategory": "Live Music Venue (Jazz)",
        "description": "Housed in a century-old heritage building (built 1910) with exposed brick walls and high ceilings, Jao Tim has become KL's premier jazz venue. Featuring live jazz acts, jam sessions, and even swing dance classes in a stylish, intimate setting that accommodates up to 100 people. Full food and drinks menu available.",
        "location": "Top floor, heritage shophouse, Chinatown, Kuala Lumpur",
        "cost_rm": 40,
        "cost_usd": 9,
        "duration_hours": 2.5,
        "best_time": "Check schedule for featured artists, typically evenings",
        "tips": "Admission ticket required (varies by performer). Full food and drinks menu available including cocktails, wines, and beer. Arrive early for good seats as capacity is limited. Beautiful heritage architecture.",
        "photos": [
            "/KL-trip/assets/images/activities/jao-tim-jazz/1.jpg",
            "/KL-trip/assets/images/activities/jao-tim-jazz/2.jpg",
            "/KL-trip/assets/images/activities/jao-tim-jazz/3.jpg"
        ],
        "added_date": "2025-10-14",
        "source": "proactive_research"
    },
    {
        "id": next_id + 6,
        "name": "Pisco Bar & Restaurant",
        "category": "Nightlife & Entertainment",
        "subcategory": "Live Music Bar & Restaurant",
        "description": "A casual restobar in the heart of Changkat Bukit Bintang serving great tapas, tacos, and cocktails with live bands on Thursdays and DJs on weekends. The upstairs area features the main bar and dance floor, creating a lively party atmosphere after dinner service with happy hour specials.",
        "location": "Jalan Mesui, Changkat Bukit Bintang, Kuala Lumpur",
        "cost_rm": 45,
        "cost_usd": 10,
        "duration_hours": 3,
        "best_time": "Thursday for live music, weekends for DJ parties",
        "tips": "Happy hour available. Strong Long Island iced teas. Great tapas and tacos for dinner before dancing. Upstairs gets packed on weekends. Located in the heart of Changkat nightlife area so easy to bar hop.",
        "photos": [
            "/KL-trip/assets/images/activities/pisco-bar/1.jpg",
            "/KL-trip/assets/images/activities/pisco-bar/2.jpg",
            "/KL-trip/assets/images/activities/pisco-bar/3.jpg"
        ],
        "added_date": "2025-10-14",
        "source": "proactive_research"
    }
]

# Add new activities
activities.extend(new_activities)

# Write updated activities
with open('/home/ubuntu/KL-trip/assets/activities.json', 'w') as f:
    json.dump(activities, f, indent=2)

print(f"Successfully added {len(new_activities)} new activities!")
print(f"Total activities now: {len(activities)}")
print(f"New IDs: {next_id} to {next_id + len(new_activities) - 1}")
