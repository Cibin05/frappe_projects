# Copyright (c) 2026, cibin and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LeaveRequest(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		email: DF.Data | None
		from_date: DF.Date | None
		leave_type: DF.Literal["Sick", "casaul", "Earned"]
		mobile_number: DF.Data | None
		name1: DF.Link
		status: DF.Literal["Pending", "Approved", "Rejected"]
		to_date: DF.Date | None
		total_days: DF.Int
	# end: auto-generated types

	pass
