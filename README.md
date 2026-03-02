# Job Application Tracker CLI

A command-line based job application tracking system built with Python and MySQL.

This project allows users to manage job applications, export data, and perform exploratory data analysis (EDA).

---

## Features

- Add, update, delete job applications
- List all applications
- Search by company or position
- Application statistics (total, applied, rejected, accepted)
- Response rate calculation
- CSV export functionality
- Exploratory Data Analysis (EDA) with visualization
- Salary distribution analysis
- Acceptance rate by salary range

---

## Status Values

The system supports the following application statuses:

- Applied
- Rejected
- Accepted

Response rate is calculated as:

(Accepted + Rejected) / Total Applications

---

## Tech Stack

- Python
- MySQL
- Pandas
- Matplotlib
- argparse
- mysql-connector-python

---

## Project Structure

job-application-tracker-cli/
│
├── cli.py
├── main.py
├── database.py
├── analysis.py
├── seed.py
├── requirements.txt

---

## Installation

Clone the repository:

```bash
git clone https://github.com/hakanbkm2/job-application-tracker-cli.git
cd job-application-tracker-cli
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure you have a MySQL database named:

```
job_tracker
```

And update your database credentials inside `database.py` if necessary.

---

## CLI Usage

Add a new application:

```bash
python cli.py add \
--company "Google" \
--position "Data Analyst" \
--status Applied \
--salary 25000 \
--date 2025-01-15 \
--link "https://careers.google.com" \
--notes "Referral"
```

List applications:

```bash
python cli.py list
```

Update application status:

```bash
python cli.py update --id 5 --status Accepted
```

Delete application:

```bash
python cli.py delete --id 5
```

Get statistics:

```bash
python cli.py get_stats
```

Search applications:

```bash
python cli.py search --q Google
```

Export to CSV:

```bash
python cli.py export --filename applications.csv
```

---

## Data Seeding

To generate 100 realistic job applications:

```bash
python seed.py
```

---

## Exploratory Data Analysis

After exporting data to CSV:

```bash
python analysis.py
```

This will generate:

- Status distribution bar chart
- Salary histogram
- Salary boxplot by status
- Acceptance rate by salary bucket

---

## Example Stats Output

```
Total Applications: 100
Applied : 60
Rejected : 30
Accepted : 10

Response Rate: %40.0
```

---

## Requirements

```
pandas
matplotlib
mysql-connector-python
```

