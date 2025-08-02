import kagglehub
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

path = kagglehub.dataset_download("dataanalyst001/world-marriage-dataset")
df = pd.read_csv(f"{path}/World Marriage Dataset.csv")

print("Shape of dataset:", df.shape)
print("Columns:", df.columns.tolist())
print("Missing values:\n", df.isnull().sum())

df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower() 
print("\nCleaned Columns:", df.columns.tolist())

plt.figure(figsize=(10, 6))
sns.countplot(y='maritalstatus', data=df, order = df['maritalstatus'].value_counts().index)
plt.title('Distribution of Marital Status')
plt.xlabel('Count')
plt.ylabel('Marital Status')
plt.show()

# Marriage Rate by Country (Approximation)
# We can approximate a "marriage rate" by looking at the proportion of married individuals
married_df = df[df['maritalstatus'] == 'Married']
marriage_by_country = married_df.groupby('country').size().reset_index(name='married_count')
total_by_country = df.groupby('country').size().reset_index(name='total_count')

marriage_stats = pd.merge(marriage_by_country, total_by_country, on='country')
marriage_stats['marriage_proportion'] = marriage_stats['married_count'] / marriage_stats['total_count']

# Top 10 Countries by Marriage Proportion
top10_marriage_proportion = marriage_stats.sort_values('marriage_proportion', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x='country', y='marriage_proportion', data=top10_marriage_proportion)
plt.title('Top 10 Countries by Proportion of Married Population')
plt.xticks(rotation=45)
plt.ylabel('Proportion of Married Population')
plt.show()

print("\n💡 INSIGHT 1: The dataset contains various marital statuses, with 'Married' being one of the most frequent.")
print("💡 INSIGHT 2: We can approximate a marriage rate by calculating the proportion of the population that is married.")
print("💡 INSIGHT 3: Some countries have a significantly higher proportion of their population reported as married compared to others.")

df.to_csv("cleaned_world_marriage_data.csv", index=False)

print("\n✅ Analysis updated. The new plots and insights are based on the actual columns in your dataset.")