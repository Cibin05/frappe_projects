# Copyright (c) 2026, cibin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Employee_work(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		domain: DF.Literal["HR", "Frontend", "Backend", "UI"]
		email: DF.Data | None
		name1: DF.Data | None
		phone_no1: DF.Data | None
	# end: auto-generated types

	@frappe.whitelist()
	def get_domain(self):
		return self.domain
	pass
