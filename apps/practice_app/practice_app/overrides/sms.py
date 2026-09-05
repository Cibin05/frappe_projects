import frappe
from frappe import _


def send_sms(receiver_list, msg, sender=None, success_msg=True):

    print("Receiver:", receiver_list)
    print("Message:", msg)
    print("Sender:", sender)

    # For now, just simulate SMS sending
    frappe.msgprint(_("SMS sent successfully"))

    return True