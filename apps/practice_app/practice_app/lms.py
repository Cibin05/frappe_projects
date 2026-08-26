import frappe


@frappe.whitelist()
def update_bulk():
    details = frappe.qb.DocType("details")
    employee = frappe.qb.DocType("Employee_work")
    queryy = (
        frappe.qb.from_(details)
        .join(employee)
        .on(details.first == employee.name1)
        .select(
            details.name,
            details.first,
            details.name3,
            details.status
        )
        .where(details.status == "Inactive")
    ).run(as_dict=True)
    if not queryy:
        return []
    doc = frappe.get_doc("details", queryy[0]["name"])
    doc.name3 = "cibin"
    doc.save()
    for q in queryy:
        frappe.db.set_value(
            "details",
            q["name"],
            "status",
            "Active"
        )
    return queryy