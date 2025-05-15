import pandas as pd

data_path = "98-401-X2021021_English_CSV_data.csv"

target_characteristic = "Average total income of household in 2020 ($)"

# Load data in chunks
chunk_size = 100000
chunks = []

for chunk in pd.read_csv(data_path, encoding='ISO-8859-1', chunksize=chunk_size, low_memory=False):
    # Clean up whitespace
    chunk['CHARACTERISTIC_NAME'] = chunk['CHARACTERISTIC_NAME'].astype(str).str.strip()
    chunk['GEO_NAME'] = chunk['GEO_NAME'].astype(str).str.strip()
    
    # Filter for Census Subdivisions and the income characteristic
    filtered = chunk[
        (chunk['GEO_LEVEL'] == 'Census subdivision') &
        (chunk['CHARACTERISTIC_NAME'] == target_characteristic)
    ][['GEO_NAME', 'C1_COUNT_TOTAL']]
    
    chunks.append(filtered)

# Combine results
df = pd.concat(chunks, ignore_index=True)

# Convert income to numeric and drop nulls
df['C1_COUNT_TOTAL'] = pd.to_numeric(df['C1_COUNT_TOTAL'], errors='coerce')
df = df.dropna(subset=['C1_COUNT_TOTAL'])

# Sort and select top 50
top_50 = df.sort_values(by='C1_COUNT_TOTAL', ascending=False).head(50)

# Save to CSV
top_50.to_csv("top_50_ontario_household_income.csv", index=False)

# Print summary
print("Top 50 Ontario municipalities by average total household income (2020):")
print(top_50)
