import frappe

def before_tests():
    frappe.logger("practice_app").info("Preparing test data...")