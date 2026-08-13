frappe.ui.form.on("Project_name", {
    refresh(frm) {
        frm.set_query("project_lead","membe", function () {
            return {
                filters: {
                    name1: "sanjusanju"
                }
            };
        });
        frm.add_custom_button("add fied",()=>{
            frm.add_child("membe",{
                project_lead:"cibin",
                role:"HR"

            })
            frm.refresh_field('membe');
        });
        frm.add_custom_button("Show Selected", function () {

            let selected = frm.get_selected();

            console.log(selected);

        });
        
    }
    
});
frappe.ui.form.on("member", {

    membe_add(frm) {
        frappe.msgprint("New member row added");
    },

    before_membe_remove(frm) {
        frappe.msgprint("Member row is about to be deleted");
    },

    membe_remove(frm, cdt, cdn) {
        frappe.msgprint("Member row deleted");
    },

    membe_move(frm, cdt, cdn) {
        frappe.msgprint("Member row order changed");
    },

    form_render(frm, cdt, cdn) {
        frappe.msgprint("Member row opened as a form");
    }

});