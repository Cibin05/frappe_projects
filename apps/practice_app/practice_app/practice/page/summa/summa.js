frappe.pages['summa'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'None',
        single_column: true
    });

    page.set_title('My Page');
	page.set_title_sub("Subtitle");
	page.set_indicator("Pending", "orange");
	page.clear_indicator();
	page.set_primary_action("New Employee", () => {
    frappe.msgprint("Creating employee");
    page.add_menu_item('Send Email', () => open_email_dialog());
})
}