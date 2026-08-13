// Copyright (c) 2026, cibin and contributors
// For license information, please see license.txt

frappe.ui.form.on("Leave Request", {
	setup(frm){
        frm.set_query("name1", function () {
    return {
        filters: {
            name: "cibin"
        }
    };
});
    }
});
