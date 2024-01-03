import pandas as pd
import matplotlib.pyplot as plt

df_mig = pd.read_csv('migrants.csv', low_memory=False)

c = df_mig['Child\'s Country of Origin'].value_counts()
c = c.sort_values(ascending=False).head(10)
plt.figure(figsize=(9, 6))
c.plot(kind='bar')
plt.tight_layout()
plt.savefig('origin.pdf')

c = df_mig['Relationship of Sponsor'].value_counts()
c = c.sort_values(ascending=False).head(10)
plt.figure(figsize=(9, 6))
c.plot(kind='bar')
plt.tight_layout()
plt.savefig('sponsor.pdf')

c = df_mig['Child\'s Gender'].value_counts()
plt.figure(figsize=(9, 6))
c.plot(kind='pie')
plt.tight_layout()
plt.savefig('gender.pdf')

# Zipcode logic.
df_zips = pd.read_csv('simplemaps_uszips_basicv1_83.csv', low_memory=False, dtype=object)
df_mig = df_mig.merge(df_zips[['zip', 'state_name']],
                            left_on='Sponsor Zipcode', right_on='zip')

c = df_mig['state_name'].value_counts()
c = c.sort_values(ascending=False).head(10)
plt.figure(figsize=(9, 6))
c.plot(kind='bar')
plt.tight_layout()
plt.savefig('states.pdf')
