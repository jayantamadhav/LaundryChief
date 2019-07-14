from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomerForm
from .models import Customer, Items, CustomerItems, SalesMetrics
import json
from datetime import date

def dashboard(request):																				#Dashboard view
	items = Items.objects.all()
	orders = CustomerItems.objects.all().order_by('id').reverse()
	customers = Customer.objects.all()
	submitbutton = request.POST.get("submit")
	data = ''
	cust_name=''
	cust_email=''
	cust_phone=''
	cust_address=''
	form = CustomerForm(request.POST or None)
	if form.is_valid():
		cust_name= form.cleaned_data.get("cust_name")
		cust_email= form.cleaned_data.get("cust_email")
		cust_phone = form.cleaned_data.get("cust_phone")
		cust_address = form.cleaned_data.get("cust_address")
		form.save()
	context = {
		'orders' : orders,
		'data' : data,
    	'form': form, 
    	'cust_name': cust_name, 
    	'cust_phone':cust_phone,
    	'cust_email': cust_email,
    	'cust_address' : cust_address,
        'submitbutton': submitbutton,
        'items' : items, 
        'customers' : customers,
    }

	return render(request, 'dashboard/dashboard.html', context)

@csrf_exempt
def orderStatus(request):
	if request.method == 'POST':
		data = request.POST
		item = CustomerItems.objects.get(id = int(data['id']))
		sendData = {}
		if data['status'] == "orderProcessing":
			item.status = "Cleaned"
			item.save()
		else:
			item.status = "Paid"
			item.save()

			total = 0																				#count total for the order
			items = item.item_ids.split('-')
			qtys = item.item_qtys.split('-')
			itemsDict = dict(zip(items[:-1], qtys[:-1]))
			for item, qty in itemsDict.items():
				total += Items.objects.get(item_id = int(item)).item_price * int(qty)
			
			try:																					#add total to total revenue
				a = SalesMetrics.objects.get(user_id = request.user.id)
				a.revenue_total += total
				a.save()
			except SalesMetrics.DoesNotExist:
				SalesMetrics.objects.create(user_id = request.user.id, revenue_total = total)
		item = CustomerItems.objects.get(id = int(data['id']))
		sendData['id'] = item.id
		sendData['customer_name'] = item.customer_name
		sendData['status'] = item.status
	return HttpResponse(json.dumps(sendData), content_type="application/json")

@csrf_exempt
def getData(request):																				#getting the submitted order
	product_list = []
	product_qty_list = []
	total = 0
	if request.method == 'POST':
		params = request.POST
		data = json.loads(params['cart_list'][:-1])
		for i in data:
			product_list.append(str(i['product_id'])+'-')
			product_qty_list.append(str(i['product_quantity'])+'-')
			total += int(i['product_price'])
		CustomerItems.objects.create(customer_name = params["\"customer"], item_ids = "".join(product_list), item_qtys = "".join(product_qty_list))
		
		return HttpResponse( json.dumps({"status" : 1}), content_type="application/json")


def customers(request):																				#Customer page view
	customerList = Customer.objects.all()
	return render(request, 'dashboard/customers.html', {'customerList' : customerList})

def getOrderHistory(request):																		#Customer page / get order history
	if request.method == 'GET':
		listdata = []
		data = {}
		cust_name = request.GET['customer_name']
		customers = CustomerItems.objects.filter(customer_name__exact=cust_name)
		for customer_items in customers:
			item_ids = customer_items.item_ids.split('-')
			item_qtys = customer_items.item_qtys.split('-')
			ordered_at = customer_items.orderedAt.date()
			items = dict(zip(item_ids[:-1], item_qtys[:-1]))
			for item, qty in items.items():
				item_details = Items.objects.get(item_id = int(item))
				data = { 'item_name' : item_details.item_name, 'item_qty' : qty, 'ordered_at' : str(ordered_at) }
				listdata.append(data)
		listdata = sorted(listdata, key = lambda i: i['ordered_at'],reverse=True) 
		return HttpResponse(json.dumps(listdata),content_type='application/json')
	else:
		return HttpResponse("Request method is not a GET")


def salesMetrics(request):
	today = date.today().strftime('%Y-%m-%d')
	processing = CustomerItems.objects.filter(status__exact = "Not Cleaned", orderedAt__date = today)
	cleaned = CustomerItems.objects.filter(status__exact = "Cleaned", orderedAt__date = today)
	paid = CustomerItems.objects.filter(status__exact = "Paid", orderedAt__date = today)
	cust_nos = []
	orders_served = []
	for month in range(1, 13):
		a = Customer.objects.filter(added_on__month = month)
		b = CustomerItems.objects.filter(orderedAt__month = month)
		cust_nos.append(a.count())
		orders_served.append(b.count())
	todayOrders = 0
	try:
		total_revenue = SalesMetrics.objects.get(user_id = request.user.id).revenue_total
	except:
		total_revenue = 0
	today_revenue = 0
	for i in paid:
		items = i.item_ids.split('-')
		qtys = i.item_qtys.split('-')
		itemsDict = dict(zip(items[:-1], qtys[:-1]))
		for item, qty in itemsDict.items():
			today_revenue += Items.objects.get(item_id = int(item)).item_price * int(qty)
		items = []
		qtys = []
	
	if processing.count() == 0:
		todayOrders += 0
		processing = 0
	else:
		todayOrders += processing.count()
		processing = processing.count()
	if cleaned.count() == 0:
		todayOrders += 0
		cleaned = 0
	else:
		todayOrders += cleaned.count()
		cleaned = cleaned.count()
	if paid.count() == 0:
		todayOrders += 0
		paid = 0
	else:
		todayOrders += paid.count()
		paid = paid.count()
	data = {
		"processing" : processing,
		"cleaned" : cleaned,
		"paid" : paid,
		"todayOrders" : todayOrders,
		"total_revenue" : total_revenue,
		"today_revenue" : today_revenue,
		"cust_nos" : cust_nos,
		"orders_served" : orders_served
	}
	return render(request, 'dashboard/salesMetrics.html', data)