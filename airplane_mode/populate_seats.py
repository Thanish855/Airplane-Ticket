import frappe
import random
def execute():
    tickets = frappe.get_all("Airplane Ticket", fields=["name", "seat"])
    for ticket in tickets:
        seat_num = f"{random.randint(1, 99)}{random.choice('ABCDEF')}"
        frappe.db.set_value("Airplane Ticket", ticket["name"], "seat", seat_num)
        print(seat_num)
    frappe.db.commit()