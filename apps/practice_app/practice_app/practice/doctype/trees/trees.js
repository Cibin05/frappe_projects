// Copyright (c) 2026, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("trees", {
	 refresh(frm) {
    //     frm.call("get_parent")
    //         .then(r=>{
    //             frappe.msgprint(r.message)
    //         })
    frm.call("get_child")
    .then(r => {
        frappe.msgprint(r.message.join("<br>"));
    });
}
});
