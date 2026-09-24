import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()

while True:
    print("\n1 for CREATE TABLE")
    print("2 for INSERT")
    print("3 for UPDATE")
    print("4 for DELETE")
    print("5 for DISPLAY")
    print("6 for EXIT")

    val_get = int(input("Pick Choice: "))

    match val_get:
        case 1:
            c.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    roll_no INTEGER PRIMARY KEY,
                    username VARCHAR(50) NOT NULL UNIQUE,
                    email VARCHAR(100) NOT NULL
                )
            """)
            conn.commit()
            print("Table Created.")

        case 2:
            roll_get = int(input("Roll Number: "))
            username_get = input("Username: ")
            email_get = input("Email: ")

            c.execute("""
                INSERT INTO users (roll_no, username, email)
                VALUES (?, ?, ?)
            """, (roll_get, username_get, email_get))

            conn.commit()
            print("Record Inserted.")

        case 3:
            roll_get = int(input("Roll Number: "))
            email_get = input("New Email: ")

            c.execute("""
                UPDATE users
                SET email = ?
                WHERE roll_no = ?
            """, (email_get, roll_get))

            conn.commit()
            print("Record Updated.")

        case 4:
            roll_get = int(input("Roll Number: "))

            c.execute("""
                DELETE FROM users
                WHERE roll_no = ?
            """, (roll_get,))

            conn.commit()
            print("Record Deleted.")

        case 5:
            c.execute("SELECT * FROM users")

            for row in c.fetchall():
                print(row)

        case 6:
            print("Exiting...")
            break

        case _:
            print("Invalid Choice.")

conn.close()