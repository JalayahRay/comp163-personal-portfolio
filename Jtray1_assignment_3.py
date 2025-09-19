"""
COMP 163 — Assignment 3: Personal Data Portfolio (Part 1)
Author: jtray1 (Jalayah Ray)
AI Usage: Limited Use — AI assisted; reviewed and edited by the student.

This program demonstrates Chapter 3 data types (strings, lists, tuples, sets, dicts),
required indexing operations, and the required calculations with round() where appropriate.
No functions, loops, or conditionals are used.
"""

# Personal Info
full_name = "Jalayah Ray"
student_email = "jtray1@aggies.ncat.edu"
hometown = "Charleston, SC"
graduation_semester = "Spring 2028"
major = "Accounting"

# Academic Data
current_courses = ["COMP 163", "MATH 131", "ENGL 101", "HIST 207", "MGMT 110"]
completed_courses = ["Biology", "English", "Math", "History", "Speech"]
credit_hours_list = [3,4,3,3,3]
gpa_history = [3.2, 3.3, 3.0, 3.3]

# Contact Info
emergency_contact = ("Mom", "Kalielah Ray", "704-621-2922")
home_address = ("816 Province Spring Circle", "Greensboro, NC", "27403")
instagram_info = ("Instagram", "@0fficial_.laya", 684)
twitter_info = ("Twitter", "@JalayahRay13", 33)
birthday = ("Birthday", 3, 9, 2006)

# Interest Tracking
current_skills = {"Problem solving", "Quick learner", "Time management"}
skills_to_learn = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_interests = {"Software development", "Web development", "Game development"}
hobbies = {"Basketball", "Music", "Reading"}
entertainment_backlog = {"Grey's Anatomy", "S.W.A.T", "Blind Spot"}

# Organizational Mapping
course_credits = {"COMP 163": 3, "MATH 131": 4, "ENGL 101": 3, "HIST 207": 3, "MGMT 110": 3}
course_professors = {"COMP 163": "Prof. Rhodes", "MATH 131": "Prof. Evans", "ENGL 101": "Prof. Gunthrop", "HIST 207": "Prof. Wood", "MGMT 110": "Prof. Worthy"}
course_rooms = {"COMP 163": "Gibbs 337", "MATH 131": "Online", "ENGL 101": "Online", "HIST 207": "Online", "MGMT 110": "Online"}
monthly_budget = {"Food": 400, "Entertainment": 300, "Books": 120, "Transportation": 60}
study_hours_per_subject = {"Programming": 15, "Math": 5, "ENGL": 3, "HIST": 2, "MGMT": 1}
contact_directory = {"Mom": "704-621-6922", "Roommate": "302-290-3336", "Academic Advisor": "336-285-4098"}

# Required Calculations
first_current_course = current_courses[0]
food_budget_amount = monthly_budget["Food"]
birthday_month = birthday[1]

total_current_credits = sum(credit_hours_list)
cumulative_gpa = round(sum(gpa_history) / len(gpa_history), 2)
completed_courses_count = len(completed_courses)
total_weekly_study_hours = sum(study_hours_per_subject.values())
academic_load = total_current_credits + total_weekly_study_hours
monthly_budget_total = sum(monthly_budget.values())
daily_food_budget = round(food_budget_amount / 30, 2)
annual_budget_projection = monthly_budget_total * 12
study_cost_per_hour = round(monthly_budget["Books"] / total_weekly_study_hours, 2)

# Analytics Calculations
total_social_followers = instagram_info[2] + twitter_info[2]
current_skills_count = len(current_skills)
skills_to_learn_count = len(skills_to_learn)
skills_difference = current_skills_count - skills_to_learn_count
contact_directory_size = len(contact_directory)
entertainment_backlog_count = len(entertainment_backlog)
study_hours_per_credit = round(total_weekly_study_hours / total_current_credits, 2)

# Output
print("=" * 60)
print(f"Graduation Semester: {graduation_semester}")
print()


print("-- Academic Overview --")
print(f"Current Courses: {current_courses}")
print(f"Credit Hours (current): {credit_hours_list}")
print(f"GPA History: {gpa_history}")
print(f"Completed Courses ({completed_courses_count}): {completed_courses}")
print(f"Sample (List Indexing): First current course -> {first_current_course}")
print()


print("-- Contacts & Key Info --")
print(f"Emergency Contact: {emergency_contact}")
print(f"Home Address: {home_address}")
print(f"Instagram Info: {instagram_info}")
print(f"Twitter Info: {twitter_info}")
print(f"Sample (Tuple Indexing): Birthday month -> {birthday_month}")
print()


print("-- Interests & Activities --")
print(f"Current Skills ({current_skills_count}): {current_skills}")
print(f"Skills to Learn ({skills_to_learn_count}): {skills_to_learn}")
print(f"Career Interests: {career_interests}")
print(f"Hobbies: {hobbies}")
print(f"Entertainment Backlog ({entertainment_backlog_count}): {entertainment_backlog}")
print()


print("-- Course Logistics --")
print(f"Course Credits Map: {course_credits}")
print(f"Course Professors: {course_professors}")
print(f"Course Rooms: {course_rooms}")
print(f"Sample (Dictionary Key Access): Food budget -> ${monthly_budget['Food']}")
print()


print("-- Study Plan --")
print(f"Study Hours per Subject: {study_hours_per_subject}")
print(f"Total Weekly Study Hours: {total_weekly_study_hours} hrs")
print(f"Study Hours per Credit: {study_hours_per_credit} hrs/credit")
print()


print("-- Budget --")
print(f"Monthly Budget: {monthly_budget}")
print(f"Monthly Total: ${monthly_budget_total}")
print(f"Daily Food Budget: ${daily_food_budget}")
print(f"Annual Budget Projection: ${annual_budget_projection}")
print(f"Study Cost per Hour (Books ÷ study hours): ${study_cost_per_hour}")
print()


print("-- Summary Metrics --")
print(f"Total Current Credits: {total_current_credits}")
print(f"Cumulative GPA: {cumulative_gpa}")
print(f"Academic Load (credits + study hours): {academic_load}")
print(f"Total Social Followers (Instagram + Twitter): {total_social_followers}")
print(f"Skills Difference (current - to learn): {skills_difference}")
print(f"Contact Directory Size: {contact_directory_size}")