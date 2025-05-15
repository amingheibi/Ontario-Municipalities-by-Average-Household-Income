# Top 50 Ontario Municipalities by Average Household Income (2020)

This repo analyzes data from the **2021 Canada Census** to identify the top 50 municipalities (Census Subdivisions) in Ontario ranked by **average total household income in 2020**.

## Data Source
**Dataset**: [Census Profile, 2021 Census of Population, Ontario](<https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/download-telecharger/comp/GetFile.cfm?Lang=E&FILETYPE=CSV&GEONO=021>)  
**File used**: `98-401-X2021021_English_CSV_data.csv`  
**Geographic level**: `Census Subdivision`  
**Region**: Ontario  
**Encoding**: ISO-8859-1

## Output

- Extract average total household income for all municipalities (Census Subdivisions) in Ontario
- Sort them in descending order
- Output the **top 50 municipalities** by average household income

Sample output (top 5):

| Rank | Municipality            | Avg Household Income (\$) |
| ---- | ----------------------- | ------------------------- |
| 1    | Puslinch, Township (TP) | 221,400                   |
| 2    | King, Township (TP)     | 193,000                   |
| 3    | Oakville, Town (T)      | 182,800                   |
| 4    | Mulmur, Township (TP)   | 177,800                   |
| 5    | Mono, Town (T)          | 173,400                   |

Note: This dataset does not include Dissemination Areas. Only Census Subdivisions are available, which represent full municipalities, not neighbourhoods or blocks.
If you need DA-level data, use the official StatsCan product.
