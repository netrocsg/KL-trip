# KL Trip 2025 - Daily Agent Knowledge Base

## 🎯 CRITICAL: Read This First Every Time

This document contains ALL the information the daily agent needs to successfully execute the KL Trip review task.

**GitHub Token**: The token is provided in your scheduled task environment. Use it to authenticate with GitHub.

---

## 📋 Daily Tasks (Execute in Order)

### ⭐ Task 1: PROACTIVE RESEARCH - Add 7 New Activities Daily

**IMPORTANT**: This task runs EVERY DAY regardless of suggestions!

**Goal**: Research and add 7 new unique activities to keep the website fresh and exciting.

**Categories to Rotate Through**:
- Day 1-7: Food & Dining (restaurants, cafes, street food, food tours)
- Day 8-14: Adventure & Sports (go-karting, rock climbing, water sports, hiking)
- Day 15-21: Culture & Heritage (museums, temples, historical sites, art galleries)
- Day 22-28: Shopping & Markets (malls, night markets, boutiques, local markets)
- Day 29-35: Nature & Parks (gardens, waterfalls, eco-parks, wildlife)
- Day 36-42: Nightlife & Entertainment (bars, clubs, live music, rooftop venues)
- Day 43-49: Unique Experiences (workshops, classes, tours, hidden gems)
- Repeat cycle...

**Steps**:
1. **Determine today's category** based on day number (see rotation above)
2. **Research 7 activities** in that category:
   - Use search tools to find popular and hidden gem activities
   - Look for activities suitable for groups of 8 people
   - Focus on activities within 30-45 min of Bukit Bintang/KLCC
   - Check reviews, ratings, and current information
3. **For EACH activity, gather**:
   - Name and exact location
   - Description (2-3 sentences)
   - Cost per person (in RM and USD)
   - Duration/time needed
   - Best time to visit
   - Tips and recommendations
   - At least 2-3 high-quality photos
4. **Add to activities database**:
   - Update `/kl_activities_database.json`
   - Add photos to `/assets/images/activities/[activity-slug]/`
   - Ensure proper formatting and categories
5. **Update website**:
   - Regenerate activity pages if needed
   - Ensure photos display correctly
6. **Document in daily report**:
   - List all 7 new activities added
   - Include category and reasoning
   - Note any interesting findings

**Example Activities to Research**:
- **Food**: Village Park Restaurant (nasi lemak), Merchant's Lane (hipster cafe), Lot 10 Hutong (food court), Madam Kwan's, Old China Cafe
- **Adventure**: LYL Circuit (go-karting), Skytrex (adventure park), KL Forest Canopy Walk, rock climbing gyms
- **Culture**: National Museum, Islamic Arts Museum, Thean Hou Temple, Sri Mahamariamman Temple
- **Shopping**: Central Market, Sungei Wang Plaza, Pavilion KL, Petaling Street
- **Nature**: KL Bird Park, Butterfly Park, Perdana Botanical Garden, Titiwangsa Lake Gardens
- **Nightlife**: Heli Lounge Bar, Marini's on 57, Zouk Club, Changkat Bukit Bintang bars
- **Unique**: Batik painting workshop, cooking class, street art tour, bicycle tour

**Quality Standards**:
- ✅ Must be currently operating (check latest info)
- ✅ Suitable for international tourists
- ✅ Clear pricing information
- ✅ Accessible by public transport or Grab
- ✅ Good reviews/ratings
- ✅ Diverse mix (not all similar activities)

---

### Task 2: Check for User Suggestions

**Location**: GitHub Issues with label "suggestion" and "pending"

**Steps**:
1. Fetch issues from GitHub API: `https://api.github.com/repos/netrocsg/KL-trip/issues?labels=suggestion,pending`
2. For each unprocessed issue:
   - Read the suggestion details from issue body
   - Research thoroughly using search tools
   - Add complete activity details to `/kl_activities_database.json`
   - Save photos to `/assets/images/activities/[activity-slug]/`
   - Close the issue with comment: "✅ Processed and added to website on [date]"
   - Remove "pending" label, add "processed" label

**Note**: This is IN ADDITION to the 7 proactive activities. If users suggest activities, add them as well!

---

### Task 3: Analyze Voting Data

**Location**: `/votes/` directory

**Steps**:
1. Check for new vote export files (JSON format)
2. Aggregate voting data across all files
3. Identify trending activities and itineraries
4. Note any activities with 5+ votes for special attention
5. Include analysis in daily report

**Vote Export Format**:
```json
{
  "timestamp": "2025-10-08T09:00:00Z",
  "votes": {
    "itineraries": {
      "cultural": 5,
      "instagram": 3,
      "balanced": 2
    },
    "activities": {
      "1": 8,
      "2": 6,
      "3": 4
    }
  }
}
```

---

### Task 4: Generate Daily Report

**Location**: `/reports/YYYY-MM-DD-daily-report.md`

**Template**:
```markdown
# KL Trip Daily Report - YYYY-MM-DD

## Summary
Brief overview of today's agent run.

## ⭐ New Activities Added (Proactive Research)
**Category**: [Today's category]
**Count**: 7 activities

1. **[Activity Name]** - [Brief description] | Cost: [price] | [Why added]
2. **[Activity Name]** - [Brief description] | Cost: [price] | [Why added]
... (all 7)

**Photos Added**: [Number] new photos
**Total Activities in Database**: [Current count]

## User Suggestions Processed
- [List any GitHub Issues processed, or "None"]

## Voting Trends
- [Analysis of voting data, or "No new votes"]
- Top voted itinerary: [Name] with [X] votes
- Top voted activities: [List top 3]

## Recommendations
- [Any insights or recommendations based on votes/trends]

## Errors
- [List any errors, or "No errors encountered"]

## Next Run
Tomorrow's category: [Next category in rotation]
```

**Also update**: `/reports/latest.md` (symlink or copy)

---

### Task 5: Commit and Push Changes

**Steps**:
1. Stage all changes: `git add -A`
2. Commit with message: `Daily update YYYY-MM-DD: Added [X] new activities ([category])`
3. Push to GitHub: `git push origin main`

**Files to commit**:
- `/kl_activities_database.json` (updated activities)
- `/assets/images/activities/*/` (new photos)
- `/reports/YYYY-MM-DD-daily-report.md` (today's report)
- `/reports/latest.md` (updated latest)
- Any updated itinerary files

---

### Task 6: Verify Deployment

**Steps**:
1. Wait 2-3 minutes for GitHub Pages to build
2. Visit: `https://netrocsg.github.io/KL-trip/`
3. Verify new activities appear
4. Check that photos load correctly
5. Note in report if any issues

---

## 🔧 Technical Details

### GitHub Authentication
Use the token provided in environment: `GITHUB_TOKEN`

**Clone repository**:
```bash
git clone https://[TOKEN]@github.com/netrocsg/KL-trip.git
```

### Activity Database Format
Location: `/kl_activities_database.json`

```json
{
  "activities": [
    {
      "id": 21,
      "name": "Activity Name",
      "category": "Food & Dining",
      "subcategory": "Local Cuisine",
      "description": "Detailed description...",
      "location": "Exact address or area",
      "cost_rm": 50,
      "cost_usd": 11,
      "duration_hours": 2,
      "best_time": "Lunch or Dinner",
      "tips": "Arrive early, try the signature dish",
      "photos": [
        "/KL-trip/assets/images/activities/activity-slug/1.jpg",
        "/KL-trip/assets/images/activities/activity-slug/2.jpg"
      ],
      "added_date": "2025-10-08",
      "source": "proactive_research"
    }
  ]
}
```

### Photo Management
- Save photos to: `/assets/images/activities/[activity-slug]/`
- Use sequential numbering: `1.jpg`, `2.jpg`, `3.jpg`
- Optimize images (max 1920px width, 80% quality)
- Use descriptive slugs: `village-park-restaurant`, `lyl-circuit-karting`

---

## 📊 Success Metrics

**Daily Goals**:
- ✅ 7 new activities added (proactive)
- ✅ All user suggestions processed
- ✅ Voting data analyzed
- ✅ Daily report generated
- ✅ Changes committed and pushed
- ✅ Website deployment verified
- ✅ No errors

**Quality Checks**:
- All activities have complete information
- All photos display correctly
- No duplicate activities
- Diverse mix of activity types
- Accurate pricing and details

---

## 🚨 Error Handling

**If research fails**:
- Try alternative search queries
- Use backup activity list (see below)
- Document in report

**If GitHub push fails**:
- Check token validity
- Retry with fresh clone
- Document in report

**If photos fail to download**:
- Use placeholder images
- Note in activity entry
- Document in report

---

## 📝 Backup Activity Ideas

**If research is difficult, use these proven activities**:

**Food**: Nasi Kandar Pelita, Jalan Alor Wong Ah Wah, Lokl Coffee Co, Feeka Coffee, Merchant's Lane

**Adventure**: Batu Caves Dark Caves, Sunway Lagoon, Skytrex Adventure, KL Tower Sky Box

**Culture**: Bank Negara Museum, Kuala Lumpur City Gallery, Chan She Shu Yuen Clan Temple

**Shopping**: Suria KLCC, Mid Valley Megamall, Bangsar Shopping Centre, Publika

**Nature**: FRIM (Forest Research Institute), Taman Tugu, KL Eco Forest Park

**Nightlife**: Pisco Bar, Omakase + Appreciate, The Roof, Mantra Rooftop Bar

**Unique**: Sekeping Tenggiri (architecture), Kwai Chai Hong (street art), PS150 (speakeasy)

---

## 🎯 Remember

**Your mission**: Help this team of 8 colleagues plan the BEST KL trip possible!

- Be proactive - don't wait for suggestions
- Research thoroughly - quality over quantity
- Stay current - check if places are still open
- Think like a traveler - what would YOU want to do?
- Have fun with it - find hidden gems and unique experiences!

**The team is counting on you to discover amazing activities they wouldn't find on their own!** 🚀



# Deploying to GitHub Pages and Bypassing Caching Issues

This document outlines strategies and lessons learned for successfully deploying static websites to GitHub Pages, specifically addressing persistent caching issues that can prevent updates from appearing on the live site.

## Problem Description

GitHub Pages is known for its aggressive caching mechanisms. This can lead to situations where, even after pushing new code to the repository, the live website continues to serve older versions of HTML, CSS, or JavaScript files. This problem is particularly acute for `index.html` files within subdirectories (e.g., `activities/index.html`), where changes may not propagate reliably.

## Diagnosis

When encountering deployment issues on GitHub Pages where updates are not reflected:

1.  **Verify Repository State:** Ensure the GitHub repository (`main` branch) contains the latest, correct versions of all files.
2.  **Check Live File Content:** Directly access the problematic files on the live GitHub Pages URL (e.g., `https://<username>.github.io/<repo>/path/to/file.js`) to confirm if the deployed content matches the repository.
3.  **Browser Console Inspection:** Use browser developer tools to check the console for JavaScript errors and network requests. Pay attention to whether scripts are loading and executing, and if data files are being fetched correctly.
4.  **View Source:** Inspect the HTML source of the live page (e.g., `view-source:https://<username>.github.io/<repo>/path/to/page.html`) to see if the HTML structure, including script and stylesheet references, matches the latest committed version.

## Solutions and Strategies

### 1. Local Server Testing (Crucial First Step)

Before attempting any public deployment, always verify the website's functionality on a local HTTP server. This eliminates external hosting and caching variables, confirming that the code itself is working as expected.

*   **Command:** `python3.11 -m http.server 8000` (from the project root directory)
*   **Access:** `http://0.0.0.0:8000/` or `http://0.0.0.0:8000/path/to/page.html`

### 2. Cache Busting for JavaScript/CSS Files

If JavaScript or CSS files are not updating, force the browser to fetch a new version by adding a unique query parameter to their `script` or `link` tags. A timestamp is an effective method.

*   **Example:**
    ```html
    <script src="/KL-trip/assets/js/activities.js?v=1760273301"></script>
    ```
*   **Automation:** Use a `date +%s` command to generate a new timestamp for each deployment.

### 3. Inlining Critical JavaScript/Data

For critical JavaScript logic or small data sets that are prone to caching issues, consider inlining them directly into the HTML file. This ensures the code is always served with the HTML.

*   **Process:** Copy the content of the `.js` or `.json` file and paste it within `<script>` tags in the HTML.
*   **Caution:** This increases HTML file size and reduces cacheability of the script itself.

### 4. Renaming HTML Files (Limited Usefulness)

While renaming an HTML file (e.g., `index.html` to `index-v2.html`) can force GitHub Pages to treat it as new content, it often leads to 404 errors if not handled carefully. GitHub Pages expects `index.html` within directories to serve content automatically. This strategy is generally **not recommended** for primary content pages unless accompanied by careful redirection or link updates.

### 5. Force Redeployment (Manual Trigger)

Making a trivial change (e.g., adding a comment) to a file that is known to be served correctly (like the root `index.html`) and pushing it can sometimes trigger a full rebuild and cache refresh for the entire site.

### 6. Verify Build Logs (for CI/CD)

If using a Continuous Integration/Continuous Deployment (CI/CD) pipeline (e.g., Netlify, Vercel), always check the build logs for errors or warnings. These logs provide crucial information about what happened during the deployment process.

## Lessons Learned

*   **GitHub Pages Caching:** Be extremely wary of GitHub Pages caching, especially for HTML files in subdirectories. It can be very aggressive and unpredictable.
*   **Local Testing is Key:** Always perform local testing before public deployment to isolate code issues from deployment issues.
*   **Systematic Debugging:** When facing deployment problems, systematically verify each component: repository state, live file content, browser console, and HTML source.
*   **Alternative Platforms:** If GitHub Pages proves too problematic, consider alternative static site hosting platforms (e.g., Netlify, Vercel with Git integration) that offer more transparent deployment and caching controls.

This knowledge base entry will be updated as new insights and solutions are discovered.
