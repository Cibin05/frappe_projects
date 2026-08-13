import frappe

def execute(filters=None):

    columns = [
        {
            "label": "Employee Name",
            "fieldname": "emp_name",
            "fieldtype": "Data"
        },
        {
            "label": "Employee Phone Number",
            "fieldname": "phone_no",
            "fieldtype": "Data"
        }
    ]

    filter_dict = {}

    if filters and filters.get("emp_name"):
        filter_dict["emp_name"] = ["	like",f"{filters.get("emp_name")}%"]

    data = frappe.get_all(
        "Employee_work",
        fields=["emp_name", "phone_no"],
        filters=filter_dict
    )

    return columns, data