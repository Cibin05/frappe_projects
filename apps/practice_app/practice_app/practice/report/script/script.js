// // Copyright (c) 2026, frappe and contributors
// // For license information, please see license.txt

frappe.query_reports["script"] = {
	filters: [
		{
			"fieldname": "status",
			"label": __("My Filter"),
			"fieldtype": "Data",
			"reqd": 1,
		},
	],
};
