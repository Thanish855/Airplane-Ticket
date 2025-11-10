# Copyright (c) 2025, thanisha and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	a = frappe.get_all("Airplane Ticket",fields=["SUM(total_amount) AS revenue","flight.airplane"],group_by="flight")

	data = frappe.get_all("Airline")
 
	for i in range(len(data)):

		data[i]['revenue'] = 0
 
	total_revenue = 0

	for i in range(len(a)) :

		t = frappe.get_doc("Airplane",a[i]['airplane'])

		for j in range(len(data)):

			if data[j]['name'] == t.airline :

				data[j]['revenue'] += a[i]['revenue']

				total_revenue += a[i]['revenue']

 
	chart = {

		"data" : {

			"labels" : [x.name for x in data],

			"datasets" : [{ "values" : [x.revenue for x in data]}],

		},

	}

	chart['type'] = 'donut'

 
	columns = [
		{
			"fieldname": "name",
			"fieldtype": "Link",
			"options":"Airline",
			"label": "Airline",
		},
		{
			"fieldname": "revenue",
			"fieldtype": "Currency",
			"label": "Total Revenue",
		},
	]
	
	summary = [{"label": "Total Revenue", "value": frappe.format_value(total_revenue, {"fieldtype": "Currency"}), "indicator": "Green"}]
	return columns, data, None, chart, summary
