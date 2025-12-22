import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set_style("whitegrid")

df= sns.load_dataset("penguins")
print(df.head())
# histplot
sns.histplot(df ["body_mass_g"], bins=30, kde=True)
plt.title("Distribution of Penguin Body Mass")
plt.show()

# kdeplot
sns.kdeplot(df["body_mass_g"])
plt.title("Density of Body Mass")
plt.show()

# countplot
sns.countplot(x="species", data=df)
plt.title("Count of Penguin Species")
plt.show()

# barplot
sns.barplot (
    x="species",
    y="body_mass_g",
    data=df
)
plt.title ("Average Body Mass by Species")
plt.show()

#lineplot 
sns.lineplot(
    x="flipper_length_mm",
    y="body_mass_g",
    data=df
)
plt.title("Flipper Length vs Body Mass")
plt.show()


# scatterplot
sns.scatterplot(
    x="flipper_length_mm",
    y="body_mass_g",
    data=df
)
plt.title("Scatter: Flipper Length vs Body Mass")
plt.show()

# style+ size

sns.scatterplot(
    x="flipper_length_mm",
    y="body_mass_g",
    hue="species",
    style="sex",
    size="body_mass_g",
    data=df
)
plt.show()

# boxplot
sns.boxplot(
    x="species",
    y="body_mass_g",
    data=df
)
plt.title("Boxplot by Species")
plt.show()

# violinplot
sns.violinplot(
    x="species",
    y="body_mass_g",
    data=df
)
plt.title("Violin Plot")
plt.show()

# stripplot
sns.stripplot(
    x="species",
    y="body_mass_g",
    data=df
)
plt.show()

# swarmplot
sns.swarmplot(
    x="species",
    y="body_mass_g",
    data=df
)
plt.show()

# pairplot
sns.pairplot(
    df,
    hue="species"
)
plt.show()

# heatmap
corr = df.select_dtypes("number").corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
