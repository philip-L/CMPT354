from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import json


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
# Create your views here.
@csrf_exempt
def index(request):

	if request.method == "POST":
		json_obj = json.loads(request.body)
		query = json_obj['query']

		if(query == 'projection'):
			attr = json_obj['attr']
			sql = "SELECT %s FROM MenuItem;" % (attr)
			
			with connection.cursor() as cursor:
				cursor.execute(sql)
				row = dictfetchall(cursor)
			
				print(row)

		if(query == 'selection'):
			attr = json_obj['attr']
			num = json_obj['num']
			sql = "SELECT %s FROM MenuItem WHERE Price > %f;" % (attr, num)

			with connection.cursor() as cursor:
				cursor.execute(sql)
				row = dictfetchall(cursor)
				print(row)	

		if(query == 'join'):
			attr = json_obj['attr']
			sql = "SELECT e.EmployeeID FROM Employee e, WorksAt w, Restaurant r \
					WHERE r.RestaurantID = w.RestaurantID AND w.EmployeeID = e.EmployeeID AND r.Address = '%s';" % (attr)

			with connection.cursor() as cursor:
				cursor.execute(sql)
				row = dictfetchall(cursor)
				print(row)

		if(query == 'aggregation'):
			attr = json_obj['attr']
			s = 'm.'+attr
			sql = "SELECT %s FROM MenuItem m, Sandwich s \
					WHERE m.Price = (SELECT MAX(m.Price) FROM MenuItem m) AND m.MenuItemID = s.MenuItemID;" % (s)

			with connection.cursor() as cursor:
				cursor.execute(sql)
				row = dictfetchall(cursor)
				print(row)

		if(query == 'nested_aggregation'):
			
			with connection.cursor() as cursor:
				cursor.execute("SELECT c.CustomerID, AVG(o.Cost) FROM Customer c, Orders o \
					WHERE c.CustomerID = o.CustomerID AND c.CustomerID IN	\
					(SELECT CustomerID FROM Orders GROUP BY CustomerID HAVING COUNT(*) > 2) GROUP BY c.CustomerID;")
				row = dictfetchall(cursor)

				for rows in row:
					rows['Cost'] = str(rows['AVG(o.Cost)'])
					if 'AVG(o.Cost)' in rows:
						del rows['AVG(o.Cost)']
					

		if(query == 'update'):
			attr = json_obj['attr']
			sql = "UPDATE MenuItem SET Price=Price+%f WHERE MenuItemID IN \
					(SELECT MenuItemID FROM Snacks);" % (attr)
			with connection.cursor() as cursor:
				cursor.execute(sql)
				cursor.execute("SELECT * FROM MenuItem WHERE MenuItemID IN (SELECT MenuItemID FROM Snacks);")
				row = dictfetchall(cursor)
				print(row)
		
		if(query == 'viewSandwiches'):
			
			with connection.cursor() as cursor:
				cursor.execute("SELECT * FROM Sandwich;")
				row = dictfetchall(cursor)
				print(row)

		if(query == 'delete'):
			attr = json_obj['attr']
			sql = "DELETE FROM Sandwich WHERE SandwichSize = '%s';" % (attr)

			with connection.cursor() as cursor:
				cursor.execute(sql)
				cursor.execute("SELECT * FROM Sandwich;")
				row = dictfetchall(cursor)
				print(row)

		if(query == 'insert'):
			with connection.cursor() as cursor:
				cursor.execute("INSERT INTO Sandwich (MenuItemID, SandwichName, SandwichSize ) \
					VALUES ('M100', 'Chicken Sandwich', 'H'), \
					('M105', 'Turkey Sandwich', 'H'), \
					('M104', 'Tuna Sandwich', 'H');")
				cursor.execute("SELECT * FROM Sandwich;")
				row = dictfetchall(cursor)
				print(row)

		if(query == 'division'):
			attr = json_obj['attr']
			sql = "SELECT c.%s FROM Customer c \
					WHERE NOT EXISTS (SELECT * FROM Restaurant r \
					WHERE NOT EXISTS (SELECT o.CustomerID FROM Orders o \
					WHERE c.CustomerID = o.CustomerID AND r.RestaurantID = o.RestaurantID));" % (attr)

			with connection.cursor() as cursor:
				cursor.execute(sql)
				row = dictfetchall(cursor)
				print(row)

		return HttpResponse(json.dumps(row))
