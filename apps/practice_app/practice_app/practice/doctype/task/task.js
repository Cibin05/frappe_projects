// Copyright (c) 2026, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("task", {
    refresh(frm) {
        let dialog =new frappe.ui.Dialog({
            title: "Create Task",

            fields: [
                {
                    label: "Task Subject",
                    fieldname: "subject",
                    fieldtype: "Data",
                    reqd: 1
                }
            ],

            primary_action_label: "Create Task",

            primary_action(value) {
                frappe.call({
                    method: "practice_app.practice.doctype.task.task.create_task",

                    args: {
                        task_subject: value.subject
                    },

                    callback: function(r) {
                        dialog.hide();

                        frappe.msgprint({
                            title: "success",
                            message: "task created successfully: " + r.message,
                            indicator: "green"
                        });
                    }
                });
            }
        });

        dialog.show();
    }
});
