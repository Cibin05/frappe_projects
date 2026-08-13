# Copyright (c) 2026, cibin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Employee_details(Document):
	@frappe.whitelist()
	def get_domain(self):
		return self.domain
	