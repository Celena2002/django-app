from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    import sqlite3
    conn =sqlite3.connect("books.db")
    cur = conn.cursor()
    datos= cur.execute("""select* from books limt 10""").fetchall()
    import json
    return HttpResponse(json.dumps(datos, ensure_ascii=False)) # con esto conecto a la base de datos books

    #conn2 = sqlite3.connect("db.sqlite3")
    #cur2 = conn2.cursor()
    #datos=cur2.execute("""SELECT name fROM sqlite_schema WHERE type = 'table' AND name NOT LIKE 'sqlite:%;""").fetchall()
    #return HttpResponse()   
    # con esta podemos concectar a la base de datos db.sqlite3

    #port pandas as pd
    #from sqlalchemy import create_engine

    #engine = create_engine(url)





    #dumps convierte un diccionario a string(serializar)

def man(request):
    return render("<h1>Maing Page</h1>")