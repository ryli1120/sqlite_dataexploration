import pandas as pd
import sqlite3

#1: connection to SQLite database
conn = sqlite3.connect('COD.db')

#2: Pandas Data frame
df = pd.read_csv('https://data.cdc.gov/api/views/bi63-dtpu/rows.csv')

df.to_sql('NCHS_Leading_Cause_Of_Deaths', conn, if_exists='replace', index=False)

#3: SQL Queries

#Query 1: Prints the first 10 rows in the DF by most recent year
query1 = """
SELECT * FROM NCHS_Leading_Cause_Of_Deaths
ORDER BY "Year" DESC
LIMIT 10;
"""

result1 = pd.read_sql(query1, conn)
print("\nLeading Cause of Deaths Sorted by Year:",result1)


#Query 2: Prints the count of heart disease related deaths
query2 = """
SELECT COUNT(*) AS Heart_Disease_Count
FROM NCHS_Leading_Cause_Of_Deaths
WHERE TRIM(LOWER("Cause Name")) = 'heart disease';
"""

result2 = pd.read_sql(query2, conn)
print("\n",result2)


#Query 3: Prints the total deaths from each state from highest to lowest
query3 = """
SELECT State, SUM(Deaths) AS total_deaths
FROM NCHS_Leading_Cause_Of_Deaths
GROUP BY State
ORDER BY "total_deaths" DESC;
"""

result3 = pd.read_sql(query3, conn)
print("\n",result3)


#Query 4: Prints the leading causes of deaths from highest to lowest
query4 = """
SELECT "Cause Name", SUM(Deaths) AS total_deaths
FROM NCHS_Leading_Cause_Of_Deaths
GROUP BY "Cause Name"
ORDER BY "total_deaths" DESC;
"""
result4 = pd.read_sql(query4, conn)
print("\n",result4)


conn.close()