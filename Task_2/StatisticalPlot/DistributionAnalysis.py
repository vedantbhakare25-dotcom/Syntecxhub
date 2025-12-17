import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")


region_a = df[df["Region"] == "A"]["Sales"]
region_b = df[df["Region"] == "B"]["Sales"]

plt.figure()
plt.hist(region_a, alpha=0.6, label="Region A")
plt.hist(region_b, alpha=0.6, label="Region B")
plt.title("Histogram of Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig("histogram.png")
plt.close()

plt.figure()
sns.kdeplot(region_a, label="Region A")
sns.kdeplot(region_b, label="Region B")
plt.title("KDE of Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Density")
plt.legend()
plt.tight_layout()
plt.savefig("kde_plot.png")
plt.close()

plt.figure()
sns.boxplot(x="Region", y="Sales", data=df)
plt.title("Boxplot of Sales by Region")
plt.tight_layout()
plt.savefig("boxplot.png")
plt.close()

with open("interpretation.txt", "w") as f:
    f.write(
        "The sales distribution for Region B shows higher variability and "
        "positive skewness due to the presence of extreme high values. "
        "Region A has a more compact distribution with fewer outliers. "
        "Boxplots highlight outliers clearly, while KDE and histograms "
        "provide insights into distribution shape and spread."
    )

print("Plots and interpretation exported successfully!")
