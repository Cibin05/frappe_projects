frappe.pages['page1'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'practice',
		single_column: true
	});

	 page.set_primary_action("Create Job", function () {
        frappe.msgprint("Primary Action Clicked");
    });

    page.set_secondary_action("Refresh", function () {
        frappe.msgprint("Refresh Clicked");
    });
	
	page.add_menu_item("Send Email", function () {
        frappe.msgprint("Email Menu Clicked");
    });

	page.add_menu_item("gmail", function () {
        frappe.msgprint("gmail Menu Clicked");
    });

}
   