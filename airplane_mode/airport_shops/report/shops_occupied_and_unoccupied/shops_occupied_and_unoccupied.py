# Copyright (c) 2025, thanisha and contributors
# For license information, please see license.txt

# import frappe


def execute(filters=None):
	columns = [
		{
			'fieldname': 'Occupied',
			'label': _('Occupied'),
			'fieldtype': 'Check', # Use Data fieldtype for text
		},
	]
	data =frappe.db.get_all('Shop Details', ['checkbox', 'occupied'])
	for row in data:
		if row['occupied']:
			row['Occupied'] = _('Yes')
		else:
			row['Occupied'] = _('No')
	return columns, data
