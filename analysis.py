import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("applications.csv")

print("===== GENERAL INFORMATION =====")
print(f"Total Applications: {len(df)}")

df["date_applied"] = pd.to_datetime(df["date_applied"])


print("\n===== STATUS DISTRIBUTION =====")
status_counts = df["application_status"].value_counts()
print(status_counts)

# Salary Analysis
# -----------------------------
print("\n===== SALARY ANALYSIS =====")
print(f"Mean Salary: {df['salary'].mean():.2f}")
print(f"Median Salary: {df['salary'].median():.2f}")
print(f"Std Deviation: {df['salary'].std():.2f}")

print("\nMean Salary by Status:")
print(df.groupby("application_status")["salary"].mean())


# Acceptance Rate by Salary Bucket
# -----------------------------
print("\n===== ACCEPTANCE RATE BY SALARY RANGE =====")

df["salary_bucket"] = pd.cut(df["salary"], bins=5)

bucket_analysis = bucket_analysis = (
    df.groupby("salary_bucket", observed=False)["application_status"]
      .value_counts(normalize=True)
      .unstack()
)
print(bucket_analysis)

# Visualization Section
#-------------------------

# Status Bar Chart
plt.figure()
status_counts.plot(kind="bar")
plt.title("Application Status Distribution")
plt.tight_layout()
plt.show()

# Salary Histogram
plt.figure()
df["salary"].plot(kind="hist", bins=10)
plt.title("Salary Distribution")
plt.tight_layout()
plt.show()

# Salary Boxplot (Outlier Detection)
df.boxplot(column="salary", by="application_status")
plt.title("Salary Distribution by Status")
plt.suptitle("")
plt.tight_layout()
plt.show()
