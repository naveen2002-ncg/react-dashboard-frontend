import json
import psycopg2

# Load JSON Data
with open('jsondata.json', 'r') as file:
    data = json.load(file)

# Connect to PostgreSQL
conn = psycopg2.connect(database="dashboard", user="postgres", password="password", host="localhost", port="5432")
cur = conn.cursor()

# Insert Data
for item in data:
    cur.execute("INSERT INTO insights (intensity, likelihood, relevance, year, country, topics, region, city) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                (item.get('intensity'), item.get('likelihood'), item.get('relevance'), item.get('year'),
                 item.get('country'), item.get('topics'), item.get('region'), item.get('city')))

conn.commit()
conn.close()

print("✅ Data inserted successfully!")
