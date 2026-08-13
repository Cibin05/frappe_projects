frappe.pages['click'].on_page_load = function(wrapper) {

    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: "Employee Dashboard",
        single_column: true
    });

    
    page.main.html(`
        <div class="dashboard"></div>
    `);

    // Dashboard container
    $(".dashboard").css({
        "padding":"20px",
        "font-family":"Arial"
    });

    // Title
    $("<h2>Employee Dashboard</h2>").appendTo(".dashboard");

    // Cards
    $("<div class='card total'></div>").appendTo(".dashboard");
    $("<div class='card approved'></div>").appendTo(".dashboard");
    $("<div class='card pending'></div>").appendTo(".dashboard");
    $("<div class='card rejected'></div>").appendTo(".dashboard");

    // Card content
    $(".total").html("<h3>Total Employees</h3><h1>150</h1>");

    $(".approved").html("<h3>Approved</h3><h1>95</h1>");

    $(".pending").html("<h3>Pending</h3><h1>35</h1>");

    $(".rejected").html("<h3>Rejected</h3><h1>20</h1>");

    // CSS using jQuery
    $(".card").css({
        "border":"1px solid #ccc",
        "padding":"20px",
        "margin":"15px 0",
        "border-radius":"10px",
        "background":"#f5f5f5",
        "text-align":"center"
    });

};