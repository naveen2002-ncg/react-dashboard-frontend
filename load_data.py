import json
import psycopg2

# Load JSON Data with UTF-8 Encoding
with open('jsondata.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(
        database="dashboard",  
        user="postgres",       
        password="Naveen",  # 🔴 Replace with your actual PostgreSQL password
        host="localhost",      
        port="5432"            
    )
    cur = conn.cursor()
    print("✅ Connected to the database successfully!")

    # Insert Data (Handling Empty Strings)
    for item in data:
        cur.execute(
            "INSERT INTO insights (intensity, likelihood, relevance, year, country, topics, region, city) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (
                int(item['intensity']) if item.get('intensity') and item['intensity'] != "" else None,
                int(item['likelihood']) if item.get('likelihood') and item['likelihood'] != "" else None,
                int(item['relevance']) if item.get('relevance') and item['relevance'] != "" else None,
                int(item['year']) if item.get('year') and item['year'] != "" else None,
                item.get('country') if item.get('country') and item['country'] != "" else None,
                item.get('topics') if item.get('topics') and item['topics'] != "" else None,
                item.get('region') if item.get('region') and item['region'] != "" else None,
                item.get('city') if item.get('city') and item['city'] != "" else None
            )
        )

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Data inserted successfully!")

except Exception as e:
    print("❌ Error:", e)
