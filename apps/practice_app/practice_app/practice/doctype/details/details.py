import frappe
from frappe.model.document import Document
from frappe.utils import formatdate
class details(Document):

    # @frappe.whitelist()
    # def get_message(self):
    #     return self.name1

    # @frappe.whitelist()
    # def create_new(self):
    #     doc = frappe.new_doc("details")
    #     doc.name1 = "preethi"
    #     doc.name2 = "sasikumar"
    #     doc.insert()

    # @frappe.whitelist()
    # def last_doc(self):
    #     doc = frappe.get_last_doc("details")
    #     return doc.name1

    # @frappe.whitelist()
    # def last_doc_order(self):
    #     doc = frappe.get_last_doc("details", filters={"check": 1})
    #     return doc.name1

    # @frappe.whitelist()
    # def delete(self):
    #     frappe.only_for("Administrator")
    #     frappe.delete_doc("details", self.name)

    # @frappe.whitelist()
    # def rename(self):
    #     frappe.rename_doc("details", self.name, self.name + self.name)

    # @frappe.whitelist()
    # def details(self):
    #     meta = frappe.get_meta("details")
    #     return meta.has_field("name1")

    # @frappe.whitelist()
    # def check_all(self):
    #     records = frappe.get_all("details", pluck="name")

    #     for name in records:
    #         doc = frappe.get_doc("details", name)
    #         doc.check = 1
    #         doc.save()

    # @frappe.whitelist()
    # def uncheck_all(self):
    #     records = frappe.get_all("details", pluck="name")

    #     for name in records:
    #         doc = frappe.get_doc("details", name)
    #         doc.check = 0
    #         doc.save()
    # today
    # @frappe.whitelist()
    # def before_save(self):
    #     old_doc=self.get_doc_before_save()
    #     if not old_doc:
    #         return
    #     if(old_doc.phone==self.phone):
    #         frappe.throw("new phone number can be same as old number")
    #     name1=self.has_value_changed("name1")
    #     if name1:
    #         frappe.msgprint("name has been changed")
    # @frappe.whitelist()
    # def default_save(self):
    # 	self.db_set("name1", "cibin")

    # @frappe.whitelist()
    # def get_titlee(self):
    # 	return self.get_title()
    # @frappe.whitelist()
    # def timeline(self):
    # 	self.add_comment("Edit"," what are you sure? details  are changed?")
    # @frappe.whitelist()
    # def view(self):
    # 	ge=frappe.get_all("View Log",
    # 			   filters={"reference_doctype": "Details",
    # 	"reference_name": self.name
    # 			   },fields=["*"])
    # 	return ge
    # @frappe.whitelist()
    # def add_users(self):
    # 	self.add_viewed()
    # @frappe.whitelist()
    # def add_tags(self):
    # 	self.add_tag("developer")
    # 	self.add_tag("front")
    # @frappe.whitelist()
    # def ge_tags(self):
    # 	self.get_tags()
    # @frappe.whitelist()
    # def date_format(self):
    #     return formatdate(self.date,"MMM d, yyyy")
    # @frappe.whitelist()
    # def date_format(self):
    #     return formatdate(self.date,"yyyy/MM/dd")
    # @frappe.whitelist()
    # def date_format(self):
    #     return formatdate(self.date,"dd/MM/yyyy")
    @frappe.whitelist()
    def email_send(self):
        frappe.sendmail(
            recipients=["cibinshanmugasundaram05@gmail.com"],
            subject="Test Email",
            message="Hello from Frappe!"
        )
