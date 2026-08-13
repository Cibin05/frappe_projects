import frappe
from frappe.model.document import Document

class Employeepractice(Document):
    pass


@frappe.whitelist()
def create_employee():
    doc = frappe.new_doc("Employee practice")
    doc.employee_name = "Cibin"
    doc.age = 22
    doc.salary = 30000
    doc.description = "Learning Document API"
    doc.insert()

    return "Success"