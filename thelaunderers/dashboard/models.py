# dashboard/models.py

from django.db import models


class Items(models.Model):
	item_img_path = models.CharField(max_length=255, null=True)
	item_id = models.IntegerField(null=True)
	item_name = models.CharField(max_length=50, null=True)
	item_qty = models.PositiveIntegerField(null=True)
	item_price = models.PositiveIntegerField(null=True)

	def __str__(self):
		return self.item_name

class Customer(models.Model):
	cust_name = models.CharField(max_length = 120)
	cust_email = models.EmailField(max_length = 120)
	cust_phone = models.CharField(max_length=10)
	cust_address = models.CharField(max_length = 250)
	added_on = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.cust_name


class CustomerItems(models.Model):
	customer_name = models.CharField(max_length = 120)
	item_ids = models.CharField(max_length = 200)
	item_qtys = models.CharField(max_length = 200)
	orderedAt = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=30, default="Not Cleaned", null=True)
	total = models.PositiveIntegerField(default=0)
	
	def __str__(self):
		return self.customer_name

class SalesMetrics(models.Model):
	user_id = models.CharField(max_length = 100)
	revenue_total = models.PositiveIntegerField(null=True)

	def __str__(self):
		return str(revenue_total)

	