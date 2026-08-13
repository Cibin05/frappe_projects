import frappe

def execute():

    employees = frappe.get_all(
        "details",
        fields=["name"]
    )

    updates = {}

    for emp in employees:
        updates[emp.name] = {
            "phone": "9876543210"
        }

    frappe.db.bulk_update(
        "details",
        updates
    )

    print(f"{len(updates)} employees updated.")