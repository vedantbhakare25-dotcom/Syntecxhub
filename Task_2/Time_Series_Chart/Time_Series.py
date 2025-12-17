import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
df["Date"] = pd.to_datetime(df["Date"])

daily_sales = df.groupby("Date")["Sales"].sum()

plt.figure()
daily_sales.plot()
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("sales_over_time.png")
plt.close()

monthly_sales = df.resample("M",on="Date")["Sales"].sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.close()

quarterly_sales = df.resample("Q",on="Date")["Sales"].sum()

plt.figure()
quarterly_sales.plot()
plt.title("Quarterly Sales Trend")
plt.xlabel("Quarter")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("quarterly_sales.png")
plt.close()

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure()
category_sales.plot(kind="bar")
plt.title("Category-wise Sales Comparison")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("category_sales_bar.png")
plt.close()

plt.figure()
category_sales.plot(kind="pie",autopct="%1.1f%%")
plt.title("Sales Share by Category")
plt.ylabel("")
plt.tight_layout()
plt.savefig("category_sales_pie.png")
plt.close()

with open("summary.txt","w") as f:
    f.write("Sales Analysis Summary\n")
    f.write("----------------------\n")
    f.write(f"Total Sales: {df['Sales'].sum()}\n")
    f.write(f"Highest Category: {category_sales.idxmax()}\n")
    f.write(f"Best Month: {monthly_sales.idxmax().strftime('%B %Y')}\n")

print("Charts and summary generated successfully!")
