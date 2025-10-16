import json
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

# Read voting data
with open('data/voting_data.json', 'r') as f:
    voting_data = json.load(f)

# Read activities data
with open('assets/js/activities-data.json', 'r') as f:
    activities = json.load(f)

votes = voting_data['votes']

# Create activity lookup
activity_lookup = {act['id']: act for act in activities}

# Analyze votes
vote_counts = Counter([v['activity_id'] for v in votes])
user_counts = Counter([v['user_id'] for v in votes])

# Create DataFrame for analysis
vote_df = pd.DataFrame([
    {
        'activity_id': aid,
        'votes': count,
        'activity_name': activity_lookup.get(aid, {}).get('name', f'Activity {aid}'),
        'category': activity_lookup.get(aid, {}).get('category', 'Unknown')
    }
    for aid, count in vote_counts.items()
]).sort_values('votes', ascending=False)

# Statistics
total_votes = len(votes)
unique_users = len(set([v['user_id'] for v in votes]))
unique_activities_voted = len(vote_counts)
total_activities = len(activities)

print(f"=== Voting Data Analysis ===")
print(f"Total votes: {total_votes}")
print(f"Unique users: {unique_users}")
print(f"Activities with votes: {unique_activities_voted}/{total_activities}")
print(f"Average votes per user: {total_votes/unique_users:.2f}")
print(f"Average votes per activity: {total_votes/unique_activities_voted:.2f}")
print()
print("Top 10 Most Voted Activities:")
print(vote_df.head(10).to_string(index=False))
print()
print("Votes by Category:")
category_votes = vote_df.groupby('category')['votes'].sum().sort_values(ascending=False)
print(category_votes.to_string())

# Save detailed analysis
with open('voting_analysis_2025-10-16.json', 'w') as f:
    json.dump({
        'date': '2025-10-16',
        'total_votes': total_votes,
        'unique_users': unique_users,
        'unique_activities_voted': unique_activities_voted,
        'total_activities': total_activities,
        'avg_votes_per_user': round(total_votes/unique_users, 2),
        'avg_votes_per_activity': round(total_votes/unique_activities_voted, 2),
        'top_activities': vote_df.head(10).to_dict('records'),
        'category_breakdown': category_votes.to_dict()
    }, f, indent=2)

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('KL Trip 2025 - Voting Analysis Dashboard', fontsize=16, fontweight='bold')

# Top 10 activities
ax1 = axes[0, 0]
top10 = vote_df.head(10)
ax1.barh(range(len(top10)), top10['votes'], color='#3498db')
ax1.set_yticks(range(len(top10)))
ax1.set_yticklabels([name[:30] + '...' if len(name) > 30 else name for name in top10['activity_name']], fontsize=9)
ax1.set_xlabel('Number of Votes')
ax1.set_title('Top 10 Most Voted Activities')
ax1.invert_yaxis()
for i, v in enumerate(top10['votes']):
    ax1.text(v + 0.1, i, str(v), va='center')

# Votes by category
ax2 = axes[0, 1]
category_votes_sorted = category_votes.sort_values(ascending=True)
colors = plt.cm.Set3(range(len(category_votes_sorted)))
ax2.barh(range(len(category_votes_sorted)), category_votes_sorted.values, color=colors)
ax2.set_yticks(range(len(category_votes_sorted)))
ax2.set_yticklabels(category_votes_sorted.index, fontsize=9)
ax2.set_xlabel('Number of Votes')
ax2.set_title('Votes by Category')
for i, v in enumerate(category_votes_sorted.values):
    ax2.text(v + 0.1, i, str(v), va='center')

# User engagement
ax3 = axes[1, 0]
user_vote_counts = list(user_counts.values())
ax3.hist(user_vote_counts, bins=range(1, max(user_vote_counts)+2), color='#2ecc71', edgecolor='black', alpha=0.7)
ax3.set_xlabel('Votes per User')
ax3.set_ylabel('Number of Users')
ax3.set_title('User Engagement Distribution')
ax3.grid(axis='y', alpha=0.3)

# Vote distribution
ax4 = axes[1, 1]
vote_distribution = list(vote_counts.values())
ax4.hist(vote_distribution, bins=range(1, max(vote_distribution)+2), color='#e74c3c', edgecolor='black', alpha=0.7)
ax4.set_xlabel('Votes Received')
ax4.set_ylabel('Number of Activities')
ax4.set_title('Activity Vote Distribution')
ax4.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('voting_analysis_2025-10-16.png', dpi=300, bbox_inches='tight')
print("\nVisualization saved to voting_analysis_2025-10-16.png")
