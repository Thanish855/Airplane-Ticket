# Copyright (c) 2025, thanisha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Airplane(Document):
	def validate(self):
		if self.has_value_changed("initial_audit_completed"):
			if not frappe.session.user == "Administrator" and not frappe.has_role("Airport Authority Personnel"):
				frappe.throw("You are not allowed to modify the 'Initial Audit Completed' field.")