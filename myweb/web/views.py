from django.shortcuts import render
from django.db import connection

def table(request):

    cursor=connection.cursor()
    cursor.execute("SELECT * FROM web_movie")
    all=cursor.fetchall()
    return render(request,'table.html',{'all':all})