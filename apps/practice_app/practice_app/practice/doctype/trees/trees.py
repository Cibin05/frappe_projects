# Copyright (c) 2026, frappe and contributors
# For license information, please see license.txt

import frappe
from frappe.utils.nestedset import NestedSet


class trees(NestedSet):
	# @frappe.whitelist()
	# def get_parent(self):
	# 	doc = frappe.get_doc("trees", "3fffmdfl81")
	# 	return doc.parent_trees
	@frappe.whitelist()
	def get_child(self):
		doc=frappe.get_doc("trees","32ug9b57ad")
		list=[]
		for do in doc.get_children():
			list.append(do.name)
		return list
	pass
	
