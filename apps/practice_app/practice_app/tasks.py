import frappe
@frappe.whitelist()
def daily_maintenance():
    frappe.log_error("something went wrong")