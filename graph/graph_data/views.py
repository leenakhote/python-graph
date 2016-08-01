from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from mysql.connector import MySQLConnection, Error
# Create your views here.

def query_with_fetchone(request):

    try:

        month_var = request.GET['month']
        year_var = request.GET['year']

        context_dict = {}
        context_dict['month'] = month_var
        context_dict['year'] = year_var
        dbconfig = {'password': 'root', 'host': 'localhost', 'user': 'root', 'database': 'stats'}
        conn = MySQLConnection(**dbconfig)
       # print month_var, year_var
        cursor = conn.cursor()
        cursor.execute("select COUNT(*) from clientBookings where MONTH(CheckInDate) =  " + str(month_var) + "  AND YEAR(CheckInDate) = " + str(year_var) + " AND status = 'A'")
        accept = cursor.fetchone()
       # print(accept)
        context_dict['accept'] = accept[0]

        cursor1 = conn.cursor()
        cursor1.execute("select COUNT(*) from clientBookings where MONTH(CheckInDate) =  " + str(month_var) + "  AND YEAR(CheckInDate) = " + str(year_var) + " AND status = 'X'")
        cancel = cursor1.fetchone()
       # print(cancel)
        context_dict['cancel'] = cancel[0]

        cursor2 = conn.cursor()
        cursor2.execute("select COUNT(*) from clientBookings where MONTH(CheckInDate) =  " + str(month_var) + "   AND YEAR(CheckInDate) =  " + str(year_var) + " AND status = 'p'")
        wait = cursor2.fetchone()
       # print(wait)
        context_dict['wait'] = wait[0]

        cursor3 = conn.cursor()
        cursor3.execute("select COUNT(*) from clientBookings where MONTH(CheckInDate) = " + str(month_var) + " AND YEAR(CheckInDate) = " + str(year_var) + "  AND status = 'R'")
        req = cursor3.fetchone()
      #  print(req)
        context_dict['req'] = req[0]

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

    return render_to_response('gchart.html'
                              , context_dict)


def statistics(request):
    return render_to_response(
    'stats.html',
    )

def submit(request):
    if 'choice' in request.GET:
        message = 'The choice is: %r' % request.GET['choice']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)