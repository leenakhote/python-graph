from mysql.connector import MySQLConnection, Error


def connect():
    """ Connect to MySQL database """

    db_config =  {'password': 'root', 'host': 'localhost', 'user': 'root', 'database': 'stats'}

    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')

    except Error as error:
        print(error)

    finally:
        conn.close()
        print('Connection closed.')


def query_with_fetchone():
    try:
        dbconfig = {'password': 'root', 'host': 'localhost', 'user': 'root', 'database': 'stats'}
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("select COUNT(*) from clientBookings where MONTH(CheckInDate) = '2' AND YEAR(CheckInDate) = '2005' AND status = 'A'")
        accept = cursor.fetchone()
        x = accept[0]
        print(accept)
        print x

        cursor1 = conn.cursor()
        cursor1.execute("select COUNT(*) from clientBookings where MONTH(CheckInDate) = '2' AND YEAR(CheckInDate) = '2005' AND status = 'X'")
        cancel = cursor1.fetchone()
        print(cancel)

        cursor2 = conn.cursor()
        cursor2.execute("select COUNT(*) from clientBookings where MONTH(CheckInDate) = '2' AND YEAR(CheckInDate) = '2005' AND status = 'p'")
        wait = cursor2.fetchone()
        print(wait)

        cursor3 = conn.cursor()
        cursor3.execute("select COUNT(*) from clientBookings where MONTH(CheckInDate) = '2' AND YEAR(CheckInDate) = '2005' AND status = 'R'")
        request = cursor3.fetchone()
        print(request)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    query_with_fetchone()