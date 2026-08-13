# Copyright (c) 2026, cibin and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Project_name(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from fieldapp.field.doctype.member.member import member
		from frappe.types import DF

		membe: DF.Table[member]
		project_name: DF.Link
	# end: auto-generated types

	pass
