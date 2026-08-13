frappe.pages["employee-dashboard"].on_page_load = function (wrapper) {

    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: "Employee Dashboard",
        single_column: true
    });

    $(page.body).html(`
        <div id="employee-chart" style="height:400px;"></div>
    `);

    create_chart();
};
function create_chart() {

    new frappe.Chart("#employee-chart", {
        title: "Employee Count",
        data: {
            labels: ["HR", "IT", "Sales", "Finance"],
            datasets: [
                {
                    values: [15, 30, 22, 18]
                }
            ]
        },
        type: "bar",
        height: 300,
        colors: ["#5e64ff"]
    });

}