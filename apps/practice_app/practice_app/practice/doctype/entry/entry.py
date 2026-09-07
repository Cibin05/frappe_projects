import frappe
from frappe.model.document import Document
from frappe.utils import time_diff


class Entry(Document):
    pass


@frappe.whitelist()
def time(name1, date, check_in, check_out):

    difference = time_diff(check_out, check_in)
    total_hours = difference.total_seconds() / 3600

    if total_hours >= 8:
        status = "Present"
    elif total_hours >=4:
        status = "Half day"

    emp_name = frappe.db.get_value(
        "EmpDetails",
        {"name1": name1},
        "name"
    )

    if not emp_name:
        frappe.throw("Employee not found in EmpDetails")

    emp = frappe.get_doc("EmpDetails", emp_name)

    emp.append("table_hwwl", {
        "status": status,
        "total_hour": total_hours,
        "date": date
    })

    emp.save()

    return "Attendance added successfully"