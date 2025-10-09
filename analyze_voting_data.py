import json

def analyze_voting_data(activities_file, voting_file):
    with open(activities_file, 'r') as f:
        activities_data = json.load(f)

    with open(voting_file, 'r') as f:
        voting_data = json.load(f)

    activity_votes = {activity['id']: 0 for activity in activities_data['activities']}

    for vote in voting_data['votes']:
        activity_id = vote['activity_id']
        if activity_id in activity_votes:
            activity_votes[activity_id] += 1

    # Sort activities by votes in descending order
    sorted_activities = sorted(
        activities_data['activities'],
        key=lambda x: activity_votes.get(x['id'], 0),
        reverse=True
    )

    # Prepare a report
    report = "## Voting Data Analysis Report\n\n"
    report += "### Activities Ranked by Votes\n\n"
    for activity in sorted_activities:
        votes = activity_votes.get(activity['id'], 0)
        report += f"- **{activity['name']}**: {votes} votes\n"

    return report

if __name__ == '__main__':
    report = analyze_voting_data('kl_activities_database.json', 'data/voting_data.json')
    with open('voting_analysis_report.md', 'w') as f:
        f.write(report)
    print("Voting analysis report generated: voting_analysis_report.md")

