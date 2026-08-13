frappe.call({
    method: "create_employee",
    callback: function(r) {
        frappe.msgprint(r.message);
    }
});