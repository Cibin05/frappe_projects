frappe.pages["employee-dashboard"].on_page_load = function (wrapper) {

    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: "Employee Dashboard",
        single_column: true
    }); 

    page.add_button("Click Me", function () {
        frappe.msgprint("Button clicked!");
    });

};  