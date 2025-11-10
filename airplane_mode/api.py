import frappe
from frappe.utils import today, add_days, nowdate

def send_rent_due_reminders():
    enabled = frappe.db.get_single_value("single doc", "enable_rent_reminders")
    if not enabled:
        return
    tenants = frappe.get_all(
        "Shop Details",
        fields=["shop_tenant_name", "email", "rent_amount"],
        filters={"shop_status":"Occupied"}
    )
    for tenant in tenants:
        if tenant.email:
            subject = "Rent Payment Reminder"
            message = f"""
                Dear {tenant.name},

                This is a reminder that your rent for Shop {tenant.shop} is due.
                Please make your payment by the due date to avoid any penalties.

                View your shop details here: {get_url('/app/shop/' + tenant.shop)}

                Thank you,
                Airport Leasing Team
            """

            frappe.sendmail(
                recipients=[tenant.email],
                subject=subject,
                message=message
            )