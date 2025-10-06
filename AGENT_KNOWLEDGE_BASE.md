# KL Trip 2025 - Daily Agent Knowledge Base

## 🎯 CRITICAL: Read This First Every Time

This document contains ALL the information the daily agent needs to successfully execute the KL Trip review task.

**GitHub Token**: The token is provided in your scheduled task environment. Use it to authenticate with GitHub.

## 📋 Daily Tasks

### Task 1: Check for New Suggestions

**Location**: Users will export suggestions as JSON files and upload to `/suggestions/` directory

**Steps**:
1. Check `/suggestions/` directory for new `.json` files
2. Read unprocessed suggestion files
3. Research each suggestion thoroughly
4. Add to `/assets/js/activities-data.json`
5. Mark as processed

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
