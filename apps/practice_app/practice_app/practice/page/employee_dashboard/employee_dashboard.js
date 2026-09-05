frappe.pages["employee-dashboard"].on_page_load = function (wrapper) {

    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: "Employee Dashboard",
        single_column: true
    });
    page.set_title('My Page')
    page.set_title('My Page')
    page.set_indicator('Pending', 'orange')
    page.set_primary_action("add",function(){
        frappe.msgprint("primary button is pressed")
    })
    // page.clear_primary_action()

    page.add_menu_item('Send Email', () => open_email_dialog(), true)
    page.add_action_item("action", function(){
        frappe.msgprint("action")
    });
    page.add_inner_button('Update Posts', () => update_posts())

    let field = page.add_field({
    label: 'Status',
    fieldtype: 'Select',
    fieldname: 'status',
    options: [
        'Open',
        'Closed',
        'Cancelled'
    ]
});
console.log(field.status);
};
