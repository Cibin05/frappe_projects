# Copyright (c) 2026, frappe and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class task(Document):

	pass

@frappe.whitelist()
def create_task(task_subject):
    doc = frappe.new_doc("task")
    doc.subject = task_subject
    doc.save()

    return doc.name
		
