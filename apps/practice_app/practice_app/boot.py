import frappe

@frappe.whitelist()
def cibin():

    details = frappe.qb.DocType("details")

    name2 = frappe.qb.Field("name2")

    result = (
        frappe.qb
        .from_(details)
        .select(details.name2)
        .where(name2 == "cibin")
    ).run()

    return result