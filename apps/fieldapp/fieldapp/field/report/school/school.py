import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)

    return columns, data


def get_columns():
    return [
        {
            "label": "Student",
            "fieldname": "student_name",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": "Department",
            "fieldname": "department",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": "Marks",
            "fieldname": "total_mark",
            "fieldtype": "Float",
            "width": 100
        },
        {
            "label": "Attendance",
            "fieldname": "attendace",
            "fieldtype": "Percent",
            "width": 120
        },
        {
            "label": "Fee",
            "fieldname": "fees_amount",
            "fieldtype": "Currency",
            "width": 120
        },
        {
            "label": "Status",
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 100
        }
    ]


def get_data(filters):
    filter_dict = {}

    if filters.get("department"):
        filter_dict["department"] = filters.get("department")

    if filters.get("year"):
        filter_dict["year"] = filters.get("year")

    if filters.get("status"):
        filter_dict["status"] = filters.get("status")

    return frappe.get_all(
        "School record",
        filters=filter_dict,
        fields=[
            "student_name",
            "department",
            "total_mark",
            "attendace",
            "fees_amount",
            "status"
        ]
    )