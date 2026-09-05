frappe.ui.form.on("details", {
    refresh(frm){
        frappe.msgprint("my_custom_code");
    }
});