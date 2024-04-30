import pandas as pd

# Load the messy dataset
url = 'https://example.com/messy_data.csv'  # Replace with the actual URL
df = pd.read_csv(url)

# Data cleaning and transformation
# E.g., handling missing values, data normalization, renaming columns, etc.

# Data analysis and visualization (if needed)
# E.g., generating summary statistics, creating plots, etc.

# Save the cleaned dataset to a new file
cleaned_file_path = 'cleaned_data.csv'
df.to_csv(cleaned_file_path, index=False)