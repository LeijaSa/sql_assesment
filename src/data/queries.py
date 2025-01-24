import json
import psycopg2 as psycopg2
from psycopg2.extras import RealDictCursor
from config import config

def get_flights():
    command = (
        """
        SELECT * FROM flights
        ORDER BY departure_time
        """
    ) 
    try:
        with psycopg2.connect(**config()) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(command)
                flights = cur.fetchall()
                if not flights:  # Check if the list is empty
                    return json.dumps({"message": "No flights found"})
                # The function includes printing because the task specifically requires it
                for flight in flights:
                    print(f"Flight number: {flight['flight_number']} Departure: {flight['departure_time']} Arrival: {flight['arrival_time']} From: {flight['departure_airport']} To: {flight['destination_airport']}")
                return json.dumps(flights)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def get_flights_by_airline():

    # The INNER JOIN only returns rows where the join condition (a.flight_id = f.id) is met in both table
    command = (
        """
        SELECT a.name, f.*
        FROM airline a
        JOIN flights f ON a.flight_id = f.id
        ORDER BY a.name;
        """
    )
    try:
        with psycopg2.connect(**config()) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(command)
                flights = cur.fetchall()
                if not flights:  # Check if the list is empty
                    return json.dumps({"message": "No flights found"})
                # The function includes printing because the task specifically requires it
                for flight in flights:
                    print(f"Airline:{flight ['name']} Flight number: {flight['flight_number']} Departure: {flight['departure_time']} Arrival: {flight['arrival_time']} From: {flight['departure_airport']} To: {flight['destination_airport']}")
                return json.dumps(flights)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def delete_a_flight(flight_number:str):
    command = (
        """
        DELETE FROM flights
        WHERE flight_number = %s;
        """
        )
    try:
        with psycopg2.connect(**config()) as conn:
            with conn.cursor() as cur:
                cur.execute(command,(flight_number,))
                if cur.rowcount == 0:  # Check if any rows were affected
                    return json.dumps({"error": "Flight not found"})
            conn.commit()
            return json.dumps({"success": f"Flight number {flight_number} deleted successfully."})
    except psycopg2.Error as error: 
        return json.dumps({"error": str(error)}) # Return error as JSON

"""
If airline foreign key does not have on delete cascade constraint

def delete_a_flight(flight_number: str):
    try:
        with psycopg2.connect(*config()) as conn:
            with conn.cursor() as cur:
                1. Check if the flight exists:
                command = ("SELECT id FROM flights WHERE id = %s")
                cur.execute(command, (flight_number,))
                flight_id = cur.fetchone()
                if not flight_id:
                    return json.dumps({"error": "Flight not found"})

                # 2. Delete related airline:
                delete_command = ("DELETE FROM airline WHERE flight_id = %s")
                cur.execute(delete_command, (fligh_number,))

                # 3. Delete the flight:
                delete_flight_command = ("DELETE FROM flights WHERE id = %s")
                cur.execute(command_flight_command, (flight_number,))

            conn.commit()
            return json.dumps({"success": f"Flight number {flight_number} deleted successfully."})

    except psycopg2.Error as error:
        return json.dumps({"error": str(error)})
"""


if __name__ == '__main__':

    # Print out the flights here if required or the error message
    flights = get_flights()
    flights_by_airline = get_flights_by_airline()
    #print(delete_a_flight('7890'))
    