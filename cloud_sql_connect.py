import psycopg2
import google.auth
import google.auth.transport.requests

# Obtain the default credentials
credentials, project_id = google.auth.default()

# Request an IAM token
request = google.auth.transport.requests.Request()
credentials.refresh(request)

# Connect to the PostgreSQL database via the Cloud SQL proxy
conn = psycopg2.connect(
    host='127.0.0.1',
    port='5432',
    user='your_db_user',
    password=credentials.token,
    dbname='your_db_name',
    sslmode='disable'  # Disable SSL since it's localhost and already secure
)

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM your_table")

# Fetch all results
results = cursor.fetchall()

# Iterate through the results and print them
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
