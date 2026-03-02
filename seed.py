import random
from datetime import datetime, timedelta
from main import add_application

companies = [
    "Google", "Amazon", "Microsoft", "Meta", "Netflix",
    "Tesla", "Spotify", "Nvidia", "Intel", "Airbnb",
    "Uber", "LinkedIn", "SAP", "Oracle", "IBM"
]

positions = [
    "Data Analyst", "Backend Developer", "Frontend Developer",
    "ML Engineer", "Data Scientist", "Software Engineer",
    "Business Analyst", "DevOps Engineer", "Intern"
]

statuses = (
    ["Applied"] * 60 +
    ["Rejected"] * 30 +
    ["Accepted"] * 10
)

start_date = datetime(2025, 1, 1)

for _ in range(100):
    random_days = random.randint(0, 365)
    date_applied = (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

    add_application(
        company=random.choice(companies),
        position=random.choice(positions),
        salary=random.randint(15000, 45000),
        application_status=random.choice(statuses),
        date_applied=date_applied,
        job_link="https://careers.example.com",
        notes="Generated dataset"
    )

print("100 realistic applications inserted.")