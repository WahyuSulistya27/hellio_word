import pyodbc as pyodbc

conn = pyodbc.connect('DRIVER={MySQL ODBC 5.3 ANSI Driver};User ID=44;Password=;Server=127.0.0.1;Database=document;Port=3306;String Types=Unicode')
cursor = conn.cursor()