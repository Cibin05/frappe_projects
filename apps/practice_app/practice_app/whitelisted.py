import frappe
@frappe.whitelist()
def custom_get_count(doctype, filters=None, debug=False, cache=False):
    print("My custom get_count is running")

    count = frappe.db.count(doctype, filters)

    return count