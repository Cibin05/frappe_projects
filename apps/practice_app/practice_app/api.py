# from apps.frappe.frappe.core import doctype
import frappe


# http://127.0.0.1:8000/api/method/practice_app.api.get_projects
@frappe.whitelist()
def get_projects():
    projects = frappe.db.get_list(
        "projects",
        filters={
        "description": ["like", "%important%"]
    },
        fields=["project_name", "description"]
    )

    return projects
# http://127.0.0.1:8000/api/method/practice_app.api.get_all_projects
@frappe.whitelist()
def get_all_projects():
    projects = frappe.db.get_all(
        "projects",
        fields=["project_name", "description"]
    )

    return projects


# http://127.0.0.1:8000/api/method/practice_app.api.get_task_subject
@frappe.whitelist()
def get_task_subject():
    projects = frappe.db.get_value(
        "projects",
        "specsmakers",
        ["project_name"],
    )

    return projects


# http://127.0.0.1:8000/api/method/practice_app.api.get_company_name
# @frappe.whitelist()
# def get_company_name():

#     company_name = frappe.db.get_single_value(
#         "Company Settings",
#         "company_name"
#     )

#     return company_name

# http://127.0.0.1:8000/api/method/practice_app.api.update_value
@frappe.whitelist()
def update_value():
    update=frappe.set_value('projects','specsmakers','description','Updated description')

    return update

@frappe.whitelist()
def db_exists():
    exist=frappe.db.exists('projects','specsmakers')
    cached=True
    return exist

@frappe.whitelist()
def db_count():
    count=frappe.db.count('projects', filters={'description': 'important glasses'})
    cached=True
    return count

@frappe.whitelist()
def db_delete():
    frappe.db.delete('projects', filters={'description': 'important glasses'})
    cached=True
    return "Project deleted successfully"

import frappe


# @frappe.whitelist()
# def test_savepoint():
#     project_a = frappe.get_doc({
#         "doctype": "projects",
#         "project_name": "Savepoint Test c",
#         "description": "Created before savepoint"
#     })
#     project_a.insert()

#     frappe.db.commit()
#     frappe.db.savepoint("project_checkpoint")

#     project_b = frappe.get_doc({
#         "doctype": "projects",
#         "project_name": "Savepoint Test D",
#         "description": "Created after savepoint"
#     })

#     project_b.insert()

#     before_rollback = frappe.get_all(
#         "projects",
#         filters={
#             "name": ["in", ["Savepoint Test c", "Savepoint Test D"]]
#         },
#         fields=["name", "project_name", "description"]
#     )

#     frappe.db.rollback(save_point="project_checkpoint")



#     after_rollback = frappe.get_all(
#         "projects",
#         filters={
#             "name": ["in", ["Savepoint Test c", "Savepoint Test D"]]
#         },
#         fields=["name", "project_name", "description"]
#     )


#     frappe.db.commit()


#     return {
#         "before_rollback": before_rollback,
#         "after_rollback": after_rollback
#     }






@frappe.whitelist()
def test_sql():

    data = frappe.db.sql("""
        SELECT
            project_name,
            description
        FROM `tabprojects`
    """, as_dict=True)

    return data




@frappe.whitelist()
def test_multisql():

    data = frappe.db.multisql({
        "mariadb": """
            SELECT
                project_name,
                description
            FROM `tabprojects`
        """,

        "postgres": """
            SELECT
                project_name,
                description
            FROM "tabprojects"
        """
    })

    return data


@frappe.whitelist()
def describe():
    a = frappe.db.describe("projects")
    return a





@frappe.whitelist()
def change_project_description_type():

    frappe.db.change_column_type(
        "Project",
        "description",
        "TEXT"
    )

    return "Project description column type changed successfully"


@frappe.whitelist()
def get_projects_qb():

    Project = frappe.qb.DocType("projects")

    result = (
        frappe.qb.from_(Project)
        .select(
            Project.project_name,
            Project.description
        )
    ).run(as_dict=True)

    return result



import frappe


@frappe.whitelist()
def test_walk():

    Project = frappe.qb.DocType("Project")

    query = (
        frappe.qb.from_(Project)
        .select(
            Project.project_name,
            Project.description
        )
        .where(Project.project_name == "Website")
    )

    query_string, values = query.walk()

    return {
        "query": query_string,
        "values": values
    }

from frappe.query_builder.functions import Count
@frappe.whitelist()
def count_projects():

    Project = frappe.qb.DocType("projects")

    total = Count("*").as_("total")

    result = (
        frappe.qb.from_(Project)
        .select(total)
    ).run(as_dict=True)

    return result


import frappe


@frappe.whitelist()
def library_book_join():

    Book = frappe.qb.DocType("LBook")
    Shelf = frappe.qb.DocType("Library Shelf")

    query = (
        frappe.qb.from_(Book)
        .inner_join(Shelf)
        .on(Book.shelf == Shelf.shelf_name)
        .select(
            Book.book_title,
            Book.author,
            Shelf.shelf_name,
            Shelf.location
        )
    )

    return query.run(as_dict=True)


import frappe
from frappe.query_builder.functions import JSONValue


@frappe.whitelist()
def get_customer_language():

    CustomerProfile = frappe.qb.DocType("Customer Profile")

    query = (
        frappe.qb.from_(CustomerProfile)
        .select(
            CustomerProfile.customer_name,
            JSONValue(
                CustomerProfile.preferences_json,
                "$.language"
            ).as_("language")
        )
    )

    return query.run(as_dict=True)




from pypika import CustomFunction


@frappe.whitelist()
def test_upper():

    CustomerProfile = frappe.qb.DocType("Customer Profile")

    UpperCase = CustomFunction(
        "UPPER",
        ["value"]
    )

    query = (
        frappe.qb.from_(CustomerProfile)
        .select(
            UpperCase(
                CustomerProfile.customer_name
            ).as_("uppercase_name")
        )
    )

    return str(query)
import frappe

@frappe.whitelist()
def get_projects():
    query = frappe.qb.get_query(
        "Project",
        fields=["name", "project_name", "description"]
    )

    projects = query.run(as_dict=True)

    return projects




import frappe

@frappe.whitelist()
def get_fields():
    query = frappe.qb.get_query(
        "projects",
        fields="*"
    )
    good=query.run(as_dict=True)
    return good

import frappe

@frappe.whitelist()
def get_as():
    query = frappe.qb.get_query(
        "projects",
        fields=["project_name as First","description as Describe"]

    )
    good=query.run(as_dict=True)
    return good


import frappe

@frappe.whitelist()
def get_payment_details():
    query = frappe.qb.get_query(
        "Payment",
        fields=[
            "name",
            "order",
            "order.customer",
            "order.amount",

        ]
    )

    return query.run(as_dict=True)

import frappe

@frappe.whitelist()
def get_order_items():

    query = frappe.qb.get_query(
        "purchase order",
        fields=[
            "name",
            "items.product",
            "items.quantity",
            "items.rate"
        ]
    )

    return query.run(as_dict=True)

import frappe


import frappe


@frappe.whitelist()
def get_purchase_orders():

    query = frappe.qb.get_query(
        "purchase order",
        fields=[
            "name",
            "supplier",
            {
                "items": ["product", "quantity", "rate"]
            }
        ],
        limit=5
    )

    results = query.run(as_dict=True)

    return results

@frappe.whitelist()
def get_filterss():
    query = frappe.qb.get_query(
        "projects",
        fields=["project_name","description"],
        filters={"project_name":["like", "ci%"]}

    )
    good=query.run(as_dict=True)
    return good

@frappe.whitelist()
def get_orders_with_item():

    query = frappe.qb.get_query(
        "purchase order",
        fields=[
            "name",
            "supplier"
        ],
        filters={
            "items.product": "mobile"
        },
        distinct=True
    )

    return query.run(as_dict=True)

@frappe.whitelist()
def get_employees():
    query = frappe.qb.get_query(
        "details",
        fields=[
            "name3",
            "last_name"
        ]
    )
    employees = []
    with frappe.db.unbuffered_cursor():
        employee_iterator=query.run(as_iterator=True,
                                    as_dict=True)
        for emp in employee_iterator:
            employees.append(emp)

    return employees

@frappe.whitelist()
def get_count():
    query=frappe.qb.get_query("details",
                              fields=["first_name",{"COUNT":"'*'",'as':"count"}],
                              filters={"docstatus":1},
                              group_by="first_name")
    results = query.run(as_dict=True)
    return results


@frappe.whitelist()
def get_locking():
    query = frappe.qb.get_query(
        "details",
        fields=[
            "first_name",
            "second_name",
            "name3",
            "status"
        ],
        filters={
            "status": "Active"
        },
        for_update=True
    )

    employees = query.run(as_dict=True)

    return employees


frappe.whitelist()
def get_order():
    query = frappe.qb.get_query(
    "Employee qb",
    fields=["name", "first_name", "department", "salary"],
    order_by="salary desc"
    )
    return query.run(as_dict=True)

import frappe

@frappe.whitelist()
def get_order():
    query = frappe.qb.get_query(
        "details",
        fields=[
            "status",
            "name3",
            "last_name"
        ],
        order_by="name3 asc"
    )

    return query.run(as_dict=True)


import frappe

@frappe.whitelist()
def get_employee_count():
    query = frappe.qb.get_query(
        "details",
        fields=[
            "status",
            {"COUNT": "'*'", "as": "details_count"}
        ],
        group_by="status"
    )

    return query.run(as_dict=True)


import frappe

@frappe.whitelist()
def get_employees():
    query = frappe.qb.get_query(
        "details",
        fields=[
            "name",
            "last_name",
        ],
        limit=2,
        offset=1,
        distinct=True
    )

    return query.run(as_dict=True)

import time

def test_job(number):
    
    print(f"JOB {number} STARTED")

    time.sleep(10)

    print(f"JOB {number} FINISHED")
    

    return f"Job {number} completed"

def custom_logic(doc, method=None):
    frappe.msgprint("Hook executed!")
