import frappe
from frappe.model.document import Document
# from frappe.utils import formatdate
# from frappe.utils import date_diff, now, pretty_date
# from frappe.utils import comma_and
from frappe.utils import get_filtered_list_url
class details(Document):
    pass
    # def validate(self):
    #     print(">>> DEFAULT CLASS")
    
    # @frappe.whitelist()
    # def creation(self):
    #     self.creatio = pretty_date(now())
    # pass
    # @frappe.whitelist()
    # def get_message(self):
    #     return self.name1

    # @frappe.whitelist()
    # def create_new(self):
    #     doc = frappe.new_doc("details")
    #     doc.name1 = "preethi"
    #     doc.name2 = "sasikumar"
    #     doc.insert()
    #     return "successful"
# @frappe.whitelist()
# def get_url():
#     return get_filtered_list_url("details","b3sbjgjjvcb3sbjgjjvc")
# @frappe.whitelist()
# def employee():
#     frappe.response.filename = "test.txt"
#     frappe.response.filecontent = b"Hello World"
#     frappe.response.type = "download"
# @frappe.whitelist()
# def detail():
#     doc=frappe.db.get_list("details")  
#     return frappe.get_doc("details",doc)
# http://127.0.0.1:8000/api/method/practice_app.practice.doctype.details.details.generate_pdf
# from frappe.utils.pdf import get_pdf
# @frappe.whitelist()
# def generate_pdf():

#     html = """
#     <h1>My Invoice</h1>
#     <p>Customer: Cibin</p>
#     <p>Amount: 500</p>
#     """

#     frappe.local.response.filename = "invoice.pdf"
#     frappe.local.response.filecontent = get_pdf(html)
#     frappe.local.response.type = "pdf"
# @frappe.whitelist()
# def last_doc(name2):
#     doc = frappe.get_doc("details", name2)
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
    # @frappe.whitelist()
    # def email_send(self):
    #     frappe.sendmail(
    #         recipients=["cibinshanmugasundaram05@gmail.com"],
    #         subject="Test Email",
    #         message="Hello from Frappe!"
    #     )
    # @frappe.whitelist()
    # def caldate(self):
    #     self.last=date_diff(self.end,self.start)

    # @frappe.whitelist()
    # def comma(self):
    #     self.list=comma_and([self.name1,self.name2,self.name3],add_quotes=False)
