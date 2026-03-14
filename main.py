
#Importing the need libraries
import os
import json
import requests
import pandas as pd
from mysql import connector 
from dotenv import load_dotenv

#API Information
API_KEY = os.getenv("API_KEY")
API_HOST = os.getenv("API_HOST")
SEASON = 2024
LEAGUE_ID = 39

url = "https://v3.football.api-sports.io/standings"

headers = {
	"x-rapidapi-key": API_KEY,
	"x-rapidapi-host": API_HOST
}

querystring = {"league":LEAGUE_ID,
               "season":SEASON}


#Sending Request
response = requests.get(url, headers=headers, params=querystring)
payload = response.json()
payload 


#Formating Data Received 
formatted_response = json.dumps(payload, indent=4 )

standings_list = payload["response"][0]["league"]["standings"][0]
standings_list


#Creating Rows and Columns for Data received 

rows = []
column_names = ['season', 'position', 'team_id', 'team', 'played', 'won', 'draw', 'lost', 'goal_for', 'goal_against', 'goal_diff', 'points', 'form']

for club in standings_list:
    season          = 2024
    position        = club['rank']
    team_id         = club['team']['id']
    team            = club['team']['name']
    played          = club['all']['played']
    won             = club['all']['win']
    draw            = club['all']['draw']
    lost            = club['all']['lose']
    goals_for       = club['all']['goals']['for']
    goals_against   = club['all']['goals']['against']
    goal_diff       = club['goalsDiff']
    points          = club['points']
    form            = club['form']

    active_row = (season, position, team_id, team, played, won, draw, lost, goals_for, goals_against, goal_diff, points, form)
    rows.append(active_row)

print(rows)

#Creating DF Dataframe
df = pd.DataFrame(rows, columns=column_names)
df.head(20)


#Connecting to MYSQL Server
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

server_conn = connector.connect(
    host = MYSQL_HOST,
    port = MYSQL_PORT,
    user = MYSQL_USER,
    password = MYSQL_PASSWORD,
    connection_timeout=10,
    autocommit=False,
    raise_on_warnings=True
)

server_cur = server_conn.cursor()
print(f"[Success] -  Connected to MySQL Server")

server_cur.close()
server_conn.close()

#Connecting to MYSQL database
db_connection = connector.connect(
    host = MYSQL_HOST,
    port = MYSQL_PORT,
    user = MYSQL_USER,
    password = MYSQL_PASSWORD,
    database = MYSQL_DATABASE
)

cur = db_connection.cursor(buffered=True)
print(f"[Success] -  Connected to database")


#Confirming Standings Table exist
sql_table = "standings"
cur.execute("SHOW TABLES LIKE %s", (f"{sql_table}",))

if cur.fetchone is None:
    raise SystemExit(f"This table '{sql_table}' is NOT found....please create it")
else:
    print(f"[SUCCESS]- This table '{sql_table}' exists! Continue to the next phase!")

#Loading data to Standings table
table_col = ['season', 'position', 'team_id', 'team', 'played', 'won', 'draw', 'lost', 'goal_for', 'goal_against', 'goal_diff', 'points', 'form']

standings_df = df[table_col] 

standings_records_tuples = standings_df.itertuples(index=False, name=None)

list_of_standings_records_tuples = list(standings_records_tuples)

UPSERT_SQL = f"""
INSERT INTO {sql_table}
(season, position, team_id, team, played, won, draw, lost, goals_for, goals_against, goals_diff, points, form)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) AS src
ON DUPLICATE KEY UPDATE
position         = src.position,
team             = src.team,
played           = src.played,
won              = src.won,
draw             = src.draw,
lost             = src.lost,
goals_for        = src.goals_for,
goals_against    = src.goals_against,
goals_diff       = src.goals_diff,
points           = src.points,
form             = src.form;
"""

no_of_rows_uploaded_to_mysql = len(list_of_standings_records_tuples)

try:
    cur.executemany(UPSERT_SQL, list_of_standings_records_tuples)
    db_connection.commit()
    print(f"[SUCCESS] - Upsert attempted for  {no_of_rows_uploaded_to_mysql} rows!")
except Exception as e:
    db_connection.rollback()
    print (f"[ERROR] - Rolled back due to this ....{e}")
finally:
    cur.close()
    db_connection.close()
    print("All database connections now closed.\n\nClean up completed.")