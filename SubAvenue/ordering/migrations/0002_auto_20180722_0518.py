# Generated by Django 2.0.5 on 2018-07-21 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0001_initial'),
    ]

    operations = [
    	migrations.RunSQL("INSERT INTO Restaurant (RestaurantID, Address ) \
    		VALUES ('R100', '123 Toasted Street, Vancouver BC'), ('R101', '67A Whole Wheat Place, Vancouver BC'), \
    		('R102', '500 Mayo Drive, Burnaby BC'), ('R103', '32G Lettuce Street, Vancouver BC'), \
    		('R104', '13 Ketchup Court, Delta BC');"),

    	migrations.RunSQL("INSERT INTO Employee (EmployeeID, EmployeeName, EmployeePosition ) \
    		VALUES ('E100', 'Brittney Hewitson', 'Delivery Person'), \
    		('E101', 'Ananth Prabhu', 'Sandwich Maker'), ('E102', 'Philip Leblanc', 'Sandwich Maker'), \
    		('E103',  'Jason Fevang', 'Cashier'), ('E104', 'Hazra Imran', 'CEO');"),

    	migrations.RunSQL("INSERT INTO  WorksAt (RestaurantID, EmployeeID ) VALUES  ('R100', 'E100'), ('R101', 'E101'), ('R102', 'E102'), ('R103', 'E103'), ('R104', 'E104');"),

    	migrations.RunSQL("INSERT INTO Customer (CustomerID , Name , Email , CardNumber , Address , Password ) \
    		VALUES  ('C100', 'John Fry', 'jf@live.ca', '1245676', '12 Awe St', 'sandw1ch'), \
    		('C101', 'Jim Su', 'js@live.ca', '1235576', '35 Has Plc', 'c0okies'), \
    		('C102', 'Frank Man', 'fm@live.ca', '1235908', '6 Tech Ave', 'ch1ips'), \
    		('C103', 'Rachel Boo', 'rb@live.ca', '2348969', '3A Grand St', 'spr1t3'), \
    		('C104', 'Carly Ben', 'cb@live.ca', '4768043', 'F4 Past Ave', 'ch33se');"),

    	migrations.RunSQL("INSERT INTO  Orders (`OrderID`, `RestaurantID`, `CustomerID`, `DeliverySuccess`, `Cost` , `DeliveryInstructions`, `OrderPlacementTime`, `OrderCompletionTime`, `DeliveryOrPickup`) \
    		VALUES ('O100', 'R100', 'C100', True, 5.50, 'Garage', '2018-06-14 12:17:17', '2018-06-14 12:35:01', 'D'), \
    		('O101', 'R101', 'C101', False, 2.00, 'Behind park', '2018-06-15 12:17:17', '2018-06-15 12:42:17', 'D'), \
    		('O102', 'R102', 'C102', True, 8.75, 'N/A', '2018-06-18 12:17:17', '2018-06-18 12:38:17', 'P'), \
    		('O103', 'R103', 'C103', False, 10.50, 'Downstairs', '2018-06-20 12:17:17', '2018-06-20 12:44:17', 'D'), \
    		('O104', 'R104', 'C104', True, 5.50, 'N/A', '2018-06-21 12:17:17', '2018-06-21 12:51:17', 'P'),\
			('O105', 'R102', 'C101', True, 1.00, 'Front door', '2018-06-22 12:17:17', '2018-06-22 12:32:17', 'D'),\
			('O106', 'R103', 'C101', True, 5.50, 'N/A', '2018-06-22 12:17:17', '2018-06-22 12:24:17', 'P'),\
			('O107', 'R104', 'C101', True, 8.75, 'Back door', '2018-06-23 12:17:17', '2018-06-23 12:46:17', 'D'),\
			('O108', 'R100', 'C101', True, 4.50, 'N/A', '2018-06-24 12:17:17', '2018-06-24 12:37:17', 'P'),\
			('O109', 'R102', 'C101', True, 10.75, 'N/A', '2018-06-24 12:17:17', '2018-06-24 12:48:17', 'P');"),


    	migrations.RunSQL("INSERT INTO MenuItem (MenuItemID, ItemName, Price) VALUES \
    		('M100', '6inch Chicken Sandwich', 5.00), ('M101', 'Small Pepsi Drink', 1.00), \
    		('M102', 'Chocolate Chip Cookie', 0.80), ('M103', 'Regular Chips', 1.00), \
    		('M104', '6inch Tuna Sandwich', 5.00),  ('M105', '6inch Steak Sandwich', 5.00), \
    		('M106', '6inch Turkey Sandwich', 5.00), ('M107', 'Foot-long Ham and Cheese Sandwich', 8.50), \
    		('M108', 'Foot-long Egg Salad Sandwich', 8.50), ('M109', 'Large Lemonade Drink', 3.50), \
    		('M110', 'Medium IcedTea Drink', 2.00), ('M111', 'Medium Sprite Drink', 2.00), \
    		('M112', 'Small Coca-Cola Drink', 1.00), ('M113', 'Oatmeal Raisin Cookie', 0.80), \
    		('M114', 'All Dressed Chips', 1.00), ('M115', 'Double Chocolate Cookie', 0.80);"),

    	migrations.RunSQL("INSERT INTO Contain (OrderID, MenuItemID, Quantity) \
    		VALUES  ('O100', 'M100', 1), ('O101', 'M101', 2), ('O102', 'M100', 3), ('O103', 'M102', 1), \
    		('O104', 'M103', 3), ('O105', 'M102', '1'), ('O106', 'M100', '1'), ('O107', 'M108', '1'), ('O108', 'M110', '2'), ('O109', 'M104', '2');"),

    	migrations.RunSQL("INSERT INTO Sandwich (MenuItemID, SandwichName, SandwichSize ) \
    		VALUES ('M100', 'Chicken Sandwich', 'H'), ('M107', 'Ham and Cheese', 'F'), \
    		('M108', 'Egg Salad Sandwich', 'F'), ('M105', 'Turkey Sandwich', 'H'), \
    		('M104', 'Tuna Sandwich', 'H');"),

    	migrations.RunSQL("INSERT INTO Drinks (MenuItemID, DrinkName, DrinkSize ) VALUES \
    		('M101', 'Pepsi', 'S'), ('M109', 'Lemonade', 'L'), ('M110', 'IcedTea', 'M'), \
    		('M111', 'Sprite', 'M'), ('M112', 'Coca-Cola', 'S');"),

    	migrations.RunSQL("INSERT INTO Snacks (MenuItemID, SnackName ) VALUES \
    		('M102', 'Chocolate Chip Cookie'), ('M103', 'Regular Chips'), ('M113', 'Oatmeal Raisin Cookie'), \
    		('M114', 'All Dressed Chips'), ('M115', 'Double Chocolate Cookie');"),

    	migrations.RunSQL("INSERT INTO Ingredients (IngredientID, IngredientName ) VALUES \
    		('I100', 'Tomato'), ('I101', 'Lettuce'), ('I102', 'Turkey'), ('I103', 'Whole Grain Bread'), \
    		('I104', 'Mayonnaise');"),

    	migrations.RunSQL("INSERT INTO MadeWith (MenuItemID, IngredientID ) VALUES \
    		('M105', 'I100'), ('M105', 'I101'), ('M105', 'I102'), ('M105', 'I103'), \
    		('M105', 'I104');")

    ]

