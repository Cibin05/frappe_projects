# def clear_website_cache(path=None):
#     if path:
#         print("successfull")
#     else:
#         print("not successfull")
import frappe
def successful_login(login_manager):
    frappe.msgprint("User logged in")

def clear_user_cache(login_manager):
    print("Thank you never come back")