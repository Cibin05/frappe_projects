// frappe.listview_settings["details"] = {
//     onload(listview) {
//         listview.filter_area.add([
//             ["details", "name1", "=", 0]
//         ]);
//     }
// };
// frappe.listview_settings["details"] = {
//     get_indicator(doc) {
//         if (doc.status === "Active") {
//             return ["Active", "green", "status,=,Active"];
//         }

//         return ["Inactive", "red", "status,=,Inactive"];
//     }
// };
// frappe.listview_settings['details']={
//     primary_action() {
//         frappe.msgprint("Primary button clicked");
//     },


// }
// frappe.listview_settings["details"] = {
//     button: {
//         show(doc) {
//             if(doc.status==="Active"){
//                 return true;
//             }
//             else{
//                 return false
//             }
            
//         },

//         get_label() {
//             return "msg";
//         },

//         get_description(doc) {
//             return `View ${doc.name1}`;
//         },

//         action(doc) {
//             frappe.set_route("form","details",doc.name)
//         }
//     }
// };

// frappe.listview_settings["details"] = {
//     add_fields: ["name1"],

//     get_form_link(doc) {
//         return ["Form", "Employee_work", doc.name1];
//     }
// };
// frappe.listview_settings["details"] = {
//     formatters: {
//         name(value) {
//             return `<i>${value}</i>`;
//         }
//     }
// };
// frappe.listview_settings["details"] = {
//     dropdown_button: {
//         get_label() {
//             return "Actions";
//         },
//         buttons: [
//             {
//                 get_label() {
//                     return "Button 1";
//                 },

//                 show(doc) {
//                     return true;
//                 },

//                 get_description(doc) {
//                     return `Open ${doc.name}`;
//                 },

//                 action(doc) {
//                     frappe.msgprint(`Button 1 clicked: ${doc.name}`);
//                 }
//             },

//             {
//                 get_label() {
//                     return "Button 2";
//                 },

//                 show(doc) {
//                     return doc.check == 0;
//                 },

//                 get_description(doc) {
//                     return `Button 2 for ${doc.name}`;
//                 },

//                 action(doc) {
//                     frappe.set_route("Form", "details", doc.name);
//                 }
//             },

//             {
//                 get_label() {
//                     return "Button 3";
//                 },

//                 show(doc) {
//                     return true;
//                 },

//                 get_description(doc) {
//                     return `Button 3 for ${doc.name}`;
//                 },

//                 action(doc) {
//                     frappe.msgprint("Hello from Button 3");
//                 }
//             }
//         ]
//     }
// };
frappe.listview_settings["details"] = {
    onload(listview) {
        listview.page.add_inner_button("Search Employee", () => {

            let d = new frappe.ui.Dialog({
                title: "Search Employee",
                fields: [
                    {
                        fieldtype: "Data",
                        fieldname: "name1",
                        label: "Employee Name"
                    }
                ],
                primary_action_label: "Search",
                primary_action(values) {

                    listview.filter_area.add([
                        ["details", "name1", "like", "%" + values.name1 + "%"]
                    ]);

                    d.hide();
                }
            });

            d.show();
        });
    }
};