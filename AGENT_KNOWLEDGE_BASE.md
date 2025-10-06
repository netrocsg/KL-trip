# KL Trip 2025 - Daily Agent Knowledge Base

## 🎯 CRITICAL: Read This First Every Time

This document contains ALL the information the daily agent needs to successfully execute the KL Trip review task.

**GitHub Token**: The token is provided in your scheduled task environment. Use it to authenticate with GitHub.

## 📋 Daily Tasks

### Task 1: Check for New Suggestions

**Location**: GitHub Issues with label "suggestion" and "pending"

**Steps**:
1. Fetch issues from GitHub API: `https://api.github.com/repos/netrocsg/KL-trip/issues?labels=suggestion,pending`
2. For each unprocessed issue:
   - Read the suggestion details from issue body
   - Research thoroughly using search tools
   - Add complete activity details to `/assets/js/activities-data.json`
   - Close the issue with comment: "✅ Processed and added to website"
   - Remove "pending" label, add "processed" label

### Task 2: Analyze Voting Data

Users can export votes via browser console: `exportVotes()`
Check `/votes/` directory for exported vote files.

### Task 3: Generate Daily Report

Create report in `/reports/YYYY-MM-DD-daily-report.md`

### Task 4: Update Website

Update activities database and commit changes.

### Task 5: Verify Deployment

Check that GitHub Pages reflects changes.

## 🔧 Technical Details

All technical details are in the repository README and code comments.

**Remember**: Your goal is to help the team plan an amazing KL trip!
