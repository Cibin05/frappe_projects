import frappe
# def cal(count):
#     return count*100

def execute(filters=None):

    columns = [
        {
            "label": "Username",
            "fieldname": "name1",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": "Status",
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": "Product",
            "fieldname": "product",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": "Count",
            "fieldname": "count",
            "fieldtype": "Int",
            "width": 100
        }#{
        #     "label":"Cibin",
        #     "fieldname":"final",
        #     "fieldtype":"Currency"
        # }
    ]

    data = frappe.db.sql("""
        SELECT
            u.name1,
            d.status,
            dc.product,
            dc.count,
            dc.count*100 AS final
            

        FROM `tabusers1` u

        LEFT JOIN `tabdetails` d
            ON u.name1 = d.name1

        LEFT JOIN `tabdetails_child` dc
            ON d.name = dc.parent

        WHERE d.status=%(status)s

    """, filters,as_dict=True)
    # for row in data:
    #     final_price= cal(row["count"])
    #     row["final"]=final_price
    return columns, data

