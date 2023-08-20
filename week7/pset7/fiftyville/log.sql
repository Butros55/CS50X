-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports WHERE day = 28 AND year = 2021 AND month = 7 AND street = 'Humphrey Street';

-- Drei Zeugen NR. 161,162,163
SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;

-- Muss amount vom ATM herausfinden
SELECT * FROM atm_transactions WHERE year = 2021 AND day = 28 AND month = 7 AND atm_location = 'Leggett Street';

-- nix gefunden bisher brauche genauere ZEIT
SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10;

-- id = 8, abbreviation = CSF, full_name = Fiftyville Regional Airport
SELECT * FROM airports WHERE city = 'Fiftyville';

-- destination_airport(id 6,11,4,1,9) oder genaue Zeit herausfinden(frühster Flug 8:20 destination 4)
SELECT * FROM flights WHERE origin_airport_id = 8 AND year = 2021 AND day = 29 AND month = 7;

-- Nummer oder genaue duration herausfinden
SELECT * FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;

-- city New York City LaGuardia Airport abbreviation LGA id 4
SELECT * FROM airports WHERE id = 4;

-- Flug id 36
SELECT * FROM flights WHERE year = 2021 AND day = 29 AND month = 7 AND origin_airport_id = 8 AND destination_airport_id = 4 ORDER BY hour, minute;

-- seat herausfinden
SELECT * FROM passengers WHERE flight_id = 36;


airport sus:
SELECT name, passengers.passport_number FROM passengers, people WHERE flight_id = 36 AND passengers.passport_number = people.passport_number;
+--------+-----------------+
|  name  | passport_number |
+--------+-----------------+
| Doris  | 7214083635      |
| Sofia  | 1695452385      |
| Bruce  | 5773159633      |
| Edward | 1540955065      |
| Kelsey | 8294398571      |
| Taylor | 1988161715      |
| Kenny  | 9878712108      |
| Luca   | 8496433585      |
+--------+-----------------+


phone sus:
SELECT name, receiver, caller FROM phone_calls, people WHERE phone_calls.year = 2021 AND phone_calls.month = 7 AND phone_calls.day = 28 AND phone_calls.duration <= 60 AND people.phone_number = phone_calls.caller;
+---------+----------------+----------------+
|  name   |    receiver    |     caller     |
+---------+----------------+----------------+
| Sofia   | (996) 555-8899 | (130) 555-0289 |
| Kelsey  | (892) 555-8872 | (499) 555-9472 |
| Bruce   | (375) 555-8161 | (367) 555-5533 |
| Kathryn | (389) 555-5198 | (609) 555-5876 |
| Kelsey  | (717) 555-1342 | (499) 555-9472 |
| Taylor  | (676) 555-6554 | (286) 555-6063 |
| Diana   | (725) 555-3243 | (770) 555-1861 |
| Carina  | (910) 555-3251 | (031) 555-6622 |
| Kenny   | (066) 555-9701 | (826) 555-1652 |
| Benista | (704) 555-2131 | (338) 555-6650 |
+---------+----------------+----------------+

ATM sus:
SELECT name, bank_accounts.account_number FROM people, bank_accounts, atm_transactions WHERE atm_transactions.atm_location = 'Leggett Street' AND atm_transactions.transaction_type = 'withdraw' AND atm_transactions.year = 2021 AND atm_transactions.month = 7 AND atm_transactions.day = 28 AND bank_accounts.account_number = atm_transactions.account_number AND people.id = bank_accounts.person_id;
+---------+----------------+
|  name   | account_number |
+---------+----------------+
| Bruce   | 49610011       |
| Diana   | 26013199       |
| Brooke  | 16153065       |
| Kenny   | 28296815       |
| Iman    | 25506511       |
| Luca    | 28500762       |
| Taylor  | 76054385       |
| Benista | 81061156       |
+---------+----------------+


Sus bakery:
SELECT name, bakery_security_logs.hour, bakery_security_logs.minute FROM people, bakery_security_logs WHERE bakery_security_logs.license_plate = people.license_plate AND bakery_security_logs.hour = 10 AND bakery_security_logs.minute >= 15 AND bakery_security_logs.minute <= 25;
+-----------+------+--------+
|   name    | hour | minute |
+-----------+------+--------+
| Brenda    | 10   | 17     |
| Emily     | 10   | 20     |
| Vanessa   | 10   | 16     |
| Bruce     | 10   | 18     |
| Barry     | 10   | 18     |
| Luca      | 10   | 19     |
| Sofia     | 10   | 20     |
| Iman      | 10   | 21     |
| Diana     | 10   | 23     |
| Kelsey    | 10   | 23     |
| Carolyn   | 10   | 19     |
| Alice     | 10   | 19     |
| Noah      | 10   | 15     |
| Kathleen  | 10   | 16     |
| Alice     | 10   | 20     |
| Christine | 10   | 21     |
| Karen     | 10   | 24     |
| Alexander | 10   | 25     |
+-----------+------+--------+

-- END Result
-- Bruce is the Thief
SELECT name FROM people, bank_accounts, atm_transactions, bakery_security_logs, phone_calls, passengers WHERE atm_transactions.atm_location = 'Leggett Street' AND atm_transactions.transaction_type = 'withdraw' AND atm_transactions.year = 2021 AND atm_transactions.month = 7 AND atm_transactions.day = 28 AND bank_accounts.account_number = atm_transactions.account_number AND people.id = bank_accounts.person_id AND bakery_security_logs.license_plate = people.license_plate AND bakery_security_logs.hour = 10 AND bakery_security_logs.minute >= 15 AND bakery_security_logs.minute <= 25 AND flight_id = 36 AND passengers.passport_number = people.passport_number AND phone_calls.year = 2021 AND phone_calls.month = 7 AND phone_calls.day = 28 AND phone_calls.duration <= 60 AND people.phone_number = phone_calls.caller;
+-------+
| name  |
+-------+
| Bruce |
+-------+

-- The ACCOMPLICE is Robin bc. Bruce called him on that Day with a duration under 60 sec
SELECT name FROM people WHERE phone_number = (SELECT receiver FROM phone_calls, people WHERE phone_calls.year = 2021 AND phone_calls.month = 7 AND phone_calls.day = 28 AND phone_calls.duration <= 60 AND people.phone_number = phone_calls.caller AND people.name = 'Bruce');
+-------+
| name  |
+-------+
| Robin |
+-------+