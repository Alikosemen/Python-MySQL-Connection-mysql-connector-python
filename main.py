import mysql.connector

def main():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="library"
    )

    cursor = db.cursor()

    delete_sql = "DELETE FROM book WHERE bookTitle = 'Bütün Şiirleri' "
    execute_query(db, cursor, delete_sql)

    update_sql = "UPDATE department SET dept_name = 'İnşaat Müh.' WHERE dept_name = 'Bilgisayar Müh.' "
    execute_query(db, cursor, update_sql)

    cursor.close()
    db.close()

def execute_query(db, cursor, query):
    try:
        cursor.execute(query)
        db.commit()
        print(f"{cursor.rowcount} record processed")
    except mysql.connector.Error as err:
        print("Error", err)
        db.rollback()

main()
