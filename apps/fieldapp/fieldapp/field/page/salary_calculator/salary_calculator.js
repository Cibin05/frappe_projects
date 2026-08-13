frappe.pages['salary-calculator'].on_page_load=function(wrapper){
	var page=frappe.ui.make_app_page({
		parent:wrapper,
		title:"Salary calculator",
		single_column: true
	})
	page.body.html(`
		<div>
			<h3>basic salary:</h3>
			<input type="number" class="bs">
			<h3>Bonus</h3>
			<input type="number" class="bbs">
			<button class="btn">calculate the salary</button>
			<h2 class="result"></h2>
		</div>
		`);
	$(".btn").click(function(){
		var bs=Number(document.querySelector(".bs").value)
		var bbs=Number(document.querySelector(".bbs").value)
		var total=bs+bbs
		$(".result").text("The total salary is: $"+ total)
	})
}