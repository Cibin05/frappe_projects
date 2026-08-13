frappe.query_reports["school"] = {
    filters: [
        {
            fieldname: "department",
            label: "Department",
            fieldtype: "Select",
            options: "\nIT\nCSE\nECE\nCivil\nMechanical"
        },
        {
            fieldname: "year",
            label: "Year",
            fieldtype: "Select",
            options: "\n1\n2\n3\n4"
        },
        {
            fieldname: "status",
            label: "Status",
            fieldtype: "Select",
            options: "\nActive\nInactive"
        }
    ]
};