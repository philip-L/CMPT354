from django.db import models

# Create your models here.
class Restaurant(models.Model):
    RestaurantID = models.CharField(max_length=4, primary_key=True)
    Address  = models.CharField(max_length=255)
    class Meta:
        db_table = 'Restaurant'

class Employee(models.Model):
    EmployeeID = models.CharField(max_length=4, primary_key=True)
    EmployeeName = models.CharField(max_length=255)
    EmployeePosition = models.CharField(max_length=255)
    class Meta:
        db_table = 'Employee'

class WorksAt(models.Model):
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, db_column="RestaurantID")
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column="EmployeeID" )
    class Meta:
        db_table = 'WorksAt'
        unique_together = (("Restaurant", "Employee"),)

class Customer(models.Model):
    CustomerID = models.CharField(max_length=4, primary_key=True)
    Name  = models.CharField(max_length=255)
    Email  = models.CharField(max_length=255)
    CardNumber  = models.IntegerField()
    Address  = models.CharField(max_length=255)
    Password = models.CharField(max_length=20)
    class Meta:
        db_table = 'Customer'

class Orders(models.Model):
    delivery_or_pickup = (
        ('D', 'Delivery'),
        ('P', 'Pickup'),
    )
    OrderID = models.CharField(max_length=4, primary_key=True)
    Restaurant  = models.ForeignKey(Restaurant, on_delete=models.CASCADE, db_column="RestaurantID")
    Customer  = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column="CustomerID")
    DeliverySuccess = models.BooleanField(default=False)
    DeliveryInstructions = models.CharField(max_length=255)
    OrderPlacementTime = models.DateTimeField()
    OrderCompletionTime = models.DateTimeField()
    DeliveryOrPickup = models.CharField(max_length=1, choices=delivery_or_pickup)
    class Meta:
        db_table = 'Orders'


class MenuItem(models.Model):
    MenuItemID = models.CharField(max_length=4, primary_key=True)
    ItemName  = models.CharField(max_length=255)
    Price  = models.FloatField()
    class Meta:
        db_table = 'MenuItem'


class Contain(models.Model):
    Order = models.ForeignKey(Orders, on_delete=models.CASCADE, db_column="OrderID")
    MenuItem = models.ForeignKey(MenuItem, on_delete=models.CASCADE, db_column="MenuItemID")
    Quantity  = models.IntegerField()
    class Meta:
        db_table = 'Contain'
        unique_together = (("Order", "MenuItem"),)


class Sandwich(models.Model):
    sizes = (
        ('H', '6-inch'),
        ('F', 'Foot-long'),
    )
    MenuItem = models.ForeignKey(MenuItem, on_delete=models.CASCADE, db_column="MenuItemID")
    SandwichName = models.CharField(max_length=255)
    SandwichSize = models.CharField(max_length=1, choices=sizes)
    class Meta:
        db_table = 'Sandwich'


class Drinks(models.Model):
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    MenuItem = models.ForeignKey(MenuItem, on_delete=models.CASCADE, db_column="MenuItemID")
    DrinkName = models.CharField(max_length=255)
    DrinkSize = models.CharField(max_length=1, choices=sizes)
    class Meta:
        db_table = 'Drinks'


class Snacks(models.Model):
    MenuItem = models.ForeignKey(MenuItem, on_delete=models.CASCADE, db_column="MenuItemID")
    SnackName = models.CharField(max_length=255)
    class Meta:
        db_table = 'Snacks'


class Ingredients(models.Model):
    IngredientID = models.CharField(max_length=4, primary_key=True)
    IngredientName = models.CharField(max_length=255)
    class Meta:
        db_table = 'Ingredients'


class MadeWith(models.Model):
    MenuItem = models.ForeignKey(MenuItem, on_delete=models.CASCADE, db_column="MenuItemID")
    Ingredient  = models.ForeignKey(Ingredients, on_delete=models.CASCADE, db_column="IngredientID")
    class Meta:
        db_table = 'MadeWith'
        unique_together = (("MenuItem", "Ingredient"),)











