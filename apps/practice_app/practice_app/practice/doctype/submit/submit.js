// Copyright (c) 2026, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("submit", {
	after_discard(frm) {
    frappe.msgprint("data is deleted");
},
timeline_refresh(frm) {
    console.log("Timeline Refreshed");
}
});
