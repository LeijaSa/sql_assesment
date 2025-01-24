import json
import psycopg2 as psycopg2
from psycopg2.extras import RealDictCursor
from config import config
from datetime import datetime

def db_create_flight(flight_number:str,departure_time:datetime,arrival_time:datetime,departure_airport:str,destination_airport:str):
    command = 'INSERT INTO flights (flight_number,departure_time,arrival_time,departure_airport,destination_airport) VALUES (%s, %s, %s, %s, %s);'
    try:
        with psycopg2.connect(**config()) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(command, (flight_number,departure_time,arrival_time,departure_airport,destination_airport))
                result = {"success": "created flight with number: %s " % flight_number}
                return json.dumps(result)  
            conn.commit()           
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
   

if __name__ == '__main__':
    print(db_create_flight(
        flight_number := '7890',
        departure_time := '2025-03-07 15:45:00',
        arrival_time := '2025-03-07 18:15:00',
        departure_airport := 'Toronto',
        destination_airport := 'Vancouver'
    ))

    print(db_create_flight(
        flight_number := '1123',
        departure_time := '2025-03-10 02:00:00',
        arrival_time := '2025-03-10 08:00:00',
        departure_airport := 'Dubai',
        destination_airport := 'Singapore'
    ))
    
    print(db_create_flight(
        flight_number := '3456',
        departure_time := '2025-03-05 22:00:00',
        arrival_time := '2025-03-06 06:30:00',
        departure_airport := 'Tokyo',
        destination_airport := 'Sydney'
    ))


      