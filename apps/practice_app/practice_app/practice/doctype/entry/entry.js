
frappe.ui.form.on("Entry", {

    async before_save(frm) {

        if (frm.doc.check_inout != "Check out") {
            return;
        }

        let records = await frappe.db.get_list("Entry", {
            filters: {
                name1: frm.doc.name1,
                date: frm.doc.date,
                check_inout: "Check in"
            },
            fields: [
                "name",
                "check_in"
            ],
            limit: 1
        });

        if (records.length == 0) {

            frappe.msgprint({
                title: "Check In Not Found",
                message: "No Check In found for this employee on this date.",
                indicator: "red"
            });

            frappe.validated = false;
            return;
        }

        let check_in = records[0].check_in;

        let response = await frm.call({
            method: "time",
            args: {
                name1: frm.doc.name1,
                date: frm.doc.date,
                check_in: check_in,
                check_out: frm.doc.check_out
            }
        });

        console.log("Python response:", response.message);

        frappe.msgprint({
            title: "Success",
            message: response.message,
            indicator: "green"
        });
    }
});