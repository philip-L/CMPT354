from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import json

# Create your views here.
@csrf_exempt
def index(request):

	if request.method == "POST":
		json_obj = json.loads(request.body)
		query = json_obj['query']
		#attr = json_obj['attribute']

		if(query == 'projection'):
			with connection.cursor() as cursor:
				cursor.execute("SELECT Customer FROM Customer;")
				row = cursor.fetchall()
				print(row)

		if(query == 'selection'):
			with connection.cursor() as cursor:
				cursor.execute("SELECT MenuItem FROM MenuItem WHERE Price > 2;")
				row = cursor.fetchall()
				print(row)	

		if(query == 'join'):
			with connection.cursor() as cursor:
				cursor.execute("SELECT e.Employee FROM Employee e, WorksAt w \
					WHERE w.Restaurant = ‘R100’ AND w.Employee = e.Employee;")
				row = cursor.fetchall()
				print(row)

		if(query == 'aggregation'):
			with connection.cursor() as cursor:
				cursor.execute("SELECT MAX(MenuItem.Price) FROM MenuItem, Sandwich \
					WHERE MenuItem.MenuItem = Sandwich.MenuItem;")
				row = cursor.fetchall()
				print(row)

		if(query == 'nested_aggregation'):
			with connection.cursor() as cursor:
				cursor.execute("SELECT Customer.Customer, AVG(Order.Cost) FROM Customer, Order \
					WHERE Customer.Customer = Order.Customer AND Customer.Customer IN	\
					(SELECT Customer FROM Order HAVING COUNT(Customer) > 2) \
					GROUPBY Customer.Customer;")
				row = cursor.fetchall()
				print(row)

		if(query == 'update'):
			with connection.cursor() as cursor:
				cursor.execute("UPDATE MenuItem SET Price=Price+1 WHERE MenuItem IN \
					(SELECT MenuItem FROM Snacks, MenuItem WHERE Snacks.MenuItem = MenuItem.MenuItem);")
				row = cursor.fetchall()
				print(row)

		if(query == 'delete'):
			with connection.cursor() as cursor:
				cursor.execute("DELETE MenuItem FROM Sandwich WHERE SandwichSize = 'H';")
				row = cursor.fetchall()
				print(row)

		if(query == 'division'):
			with connection.cursor() as cursor:
				cursor.execute("SELECT Customer FROM Customer WHERE NOT EXISTS \
					(SELECT * FROM Orders WHERE NOT EXISTS (SELECT RestaurantID FROM Restaurant \
					WHERE Customer.Customer = Order.Customer AND Order.Restaurant = Restaurant.Restaurant)));")
				row = cursor.fetchall()
				print(row)

		return HttpResponse(json.dumps(row))
