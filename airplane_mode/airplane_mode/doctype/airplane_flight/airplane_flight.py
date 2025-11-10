# Copyright (c) 2025, thanisha and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
    def on_submit(self):
        self.status="Completed"
    def on_update(doc, method):
        if doc.has_value_changed("gate_number"):
            frappe.enqueue(
                "airplane_mode.airplane_flight.doctype.airplane_flight.airplane_flight.update_ticket_gates",
                flight=doc.name,
                new_gate=doc.gate_number
            )
    def update_ticket_gates(flight, new_gate):
        tickets = frappe.get_all("Airplane Ticket", filters={"flight": flight}, fields=["name"])
        for ticket in tickets:
            frappe.db.set_value("Airplane Ticket", ticket.name, "gate_number", new_gate)
            frappe.db.commit()