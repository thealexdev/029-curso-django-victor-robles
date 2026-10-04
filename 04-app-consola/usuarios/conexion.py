import mysql.connector


def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="app_consola",
        # revisar tema de puertos
    )

    print(database)

    cursor = database.cursor(buffered=True)

    return [database, cursor]
