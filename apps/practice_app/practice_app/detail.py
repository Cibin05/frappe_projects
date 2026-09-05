import frappe
def employee_query(user):
    if not user:
        user=frappe.session.user
    return "`tabdetails`.name2='sasi'"