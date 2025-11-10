# Copyright (c) 2025, thanisha and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class ShopDetails(WebsiteGenerator):
	def before_save(self):
		if not self.rent_amount:
			self.rent_amount = frappe.db.get_single_value("single doc", "rent_amount")

