// Copyright (c) 2026, cibin and contributors
// For license information, please see license.txt

frappe.ui.form.on("Employee_work", {
    refresh(frm) {
        if (frm.is_new()) {
            return;
        }

        frm.call("get_domain")
            .then(r => {
                frappe.msgprint("Department: " + r.message);
            });
    }
});