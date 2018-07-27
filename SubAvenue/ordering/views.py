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
		attr = json_obj['attribute']
		ArrayOfDics = []

		if(query == 'projection'):
			sql = "SELECT %s FROM MenuItem;" % (attr)
			
			with connection.cursor() as cursor:
				cursor.execute(sql)
				row = dictfetchall(cursor)
			
				print(row)

		if(query == 'selection'):
			with connection.cursor() as cursor:
				cursor.execute("SELECT MenuItemID FROM MenuItem WHERE Price > 2;")
				row = dictfetchall(cursor)
				print(row)	

		if(query == 'join'):
			with connection.cursor() as cursor:
				cursor.execute("SELECT e.EmployeeID FROM Employee e, WorksAt w \
					WHERE w.RestaurantID = 'R100' AND w.EmployeeID = e.EmployeeID;")
				row = dictfetchall(cursor)
				print(row)

		if(query == 'aggregation'):
			with connection.cursor() as cursor:
				cursor.execute("SELECT MAX(MenuItem.Price) FROM MenuItem, Sandwich \
					WHERE MenuItem.MenuItemID = Sandwich.MenuItemID;")
				row = dictfetchall(cursor)
				print(row)

		if(query == 'nested_aggregation'):
			with connection.cursor() as cursor:
				cursor.execute("SELECT Customer.CustomerID, AVG(Orders.Cost) FROM Customer, Orders \
					WHERE Customer.CustomerID = Orders.CustomerID AND Customer.CustomerID IN	\
					(SELECT CustomerID FROM Orders HAVING COUNT(CustomerID) > 2);")
				row = dictfetchall(cursor)
				print(row)

		if(query == 'update'):
			with connection.cursor() as cursor:
				cursor.execute("UPDATE MenuItem SET Price=Price+1 WHERE MenuItemID IN \
					(SELECT MenuItemID FROM Snacks);")
				cursor.execute("SELECT * FROM MenuItem WHERE MenuItemID IN (SELECT MenuItemID FROM Snacks);")
				row = dictfetchall(cursor)
				print(row)
	

		if(query == 'delete'):
			with connection.cursor() as cursor:
				cursor.execute("DELETE FROM Sandwich WHERE SandwichSize = 'H';")
				cursor.execute("SELECT * FROM Sandwich;")
				row = dictfetchall(cursor)
				print(row)

		if(query == 'insert'):
			with connection.cursor() as cursor:
				cursor.execute("INSERT INTO Sandwich (MenuItemID, SandwichName, SandwichSize ) \
					VALUES ('M100', 'Chicken Sandwich', 'H'), \
					('M105', 'Turkey Sandwich', 'H'), \
					('M104', 'Tuna Sandwich', 'H');")
				row = dictfetchall(cursor)
				print(row)

		if(query == 'division'):
			with connection.cursor() as cursor:
				cursor.execute("SELECT CustomerID FROM Customer WHERE NOT EXISTS \
					(SELECT * FROM Orders WHERE NOT EXISTS (SELECT RestaurantID FROM Restaurant \
					WHERE Customer.CustomerID = Orders.CustomerID AND Orders.RestaurantID = Restaurant.RestaurantID));")
				row = dictfetchall(cursor)
				print(row)

		return HttpResponse(json.dumps(row))
