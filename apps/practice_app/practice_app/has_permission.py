import frappe
def permission(doc,user=None,permission_type=None):
    if permission_type=="read" and doc.status=="Active":
        return True;