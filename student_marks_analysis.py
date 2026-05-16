import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("students.csv")
print(data)
#average 
data["Average"] = (
    data["Python"] +
    data["SQL"] +
    data["AI"]
) / 3

print("\nData With Average Marks:\n")
print(data)
#top student with highest avg marks
top_student = data.loc[data["Average"].idxmax()]

print("\nTop Student:\n")
print(top_student)
#lowest student with lowest avg marks
lowest_student = data.loc[data["Average"].idxmin()]

print("\nLowest Student:\n")
print(lowest_student)
#avg  for each subject
avg_python = data["Python"].mean()
avg_sql = data["SQL"].mean()
avg_ai = data["AI"].mean()
print("\nSubject Average Marks:")
print("Python Average:", avg_python)
print("SQL Average:", avg_sql)
print("AI Average:", avg_ai)
#bar chart for avg marks
plt.bar(data["Name"], data["Average"])

plt.title("Student Average Marks")
plt.xlabel("Student Names")
plt.ylabel("Average Marks")

plt.xticks(rotation=45)

plt.show()
#percentage of avg marks
data["Percentage"] = (
    data["Average"] / 100
) * 100
#rank students based on avg marks
data["Rank"] = data["Average"].rank(
    ascending=False
)

print("\nStudent Rankings:\n")
print(data[["Name", "Average", "Rank"]])
#seaborn heatmap 
sns.barplot(
    x="Name",
    y="Average",
    data=data
)

plt.title("Student Average Marks")
plt.xlabel("Student Names")
plt.ylabel("Average Marks")

plt.xticks(rotation=45)

plt.show()
#pie chart 
top5 = data.head(5)

plt.figure(figsize=(7,7))

plt.pie(
    top5["Average"],
    labels=top5["Name"],
    autopct="%1.1f%%"
)

plt.title("Top 5 Students Average Distribution")

plt.show()
#export results to csv
data.to_csv(
    "student_results.csv",
    index=False
)

print("\nResults exported successfully!")