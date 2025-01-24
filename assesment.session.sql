
    
CREATE TABLE IF NOT EXISTS flights (
            id SERIAL PRIMARY KEY,
            flight_number VARCHAR(50) NOT NULL,
            departure_time TIMESTAMP NOT NULL,
            arrival_time TIMESTAMP NOT NULL,
            departure_airport VARCHAR(50) NOT NULL,
            destination_airport VARCHAR(50) NOT NULL
        );

INSERT INTO flights (flight_number, departure_time, arrival_time, departure_airport, destination_airport) 
VALUES ('1234', '2025-03-05 03:40:00', '2025-03-05 09:40:00', 'Helsinki', 'Berlin');

INSERT INTO flights (flight_number, departure_time, arrival_time, departure_airport, destination_airport) 
VALUES ('5678', '2025-03-01 08:00:00', '2025-03-01 12:30:00', 'London', 'Paris');

INSERT INTO flights (flight_number, departure_time, arrival_time, departure_airport, destination_airport) 
VALUES ('9012', '2025-03-02 14:15:00', '2025-03-02 18:45:00', 'New York', 'Los Angeles');


CREATE TABLE IF NOT EXISTS airline (
       id SERIAL PRIMARY KEY,
       name VARCHAR(50) UNIQUE NOT NULL,
       flight_id INTEGER NOT NULL,
       FOREIGN KEY (flight_id) REFERENCES flights(id) ON DELETE CASCADE
   );

INSERT INTO airline (name, flight_id) 
VALUES ('Air Berlin', 1);

INSERT INTO airline (name, flight_id) 
VALUES ('Lufthansa', 2);

INSERT INTO airline (name, flight_id) 
VALUES ('Emirates', 3);

INSERT INTO airline (name, flight_id) 
VALUES ('Delta Airlines', 4);

INSERT INTO airline (name, flight_id) 
VALUES ('Vancouver Airlines', 5);

INSERT INTO airline (name, flight_id) 
VALUES ('Singapore Airlines', 6);