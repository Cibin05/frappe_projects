import frappe

def send_hourly_email():
    frappe.sendmail(
        recipients=["cibiking007@gmail.com"],
        subject="Hourly Email",
        message="This email was sent automatically by Frappe."
    )

def printt():
   frappe.msgprint("hi from scheduler")
   