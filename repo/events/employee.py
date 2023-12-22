import frappe

@frappe.whitelist()
def book_data():
    doc = frappe.new_doc("Employee")
    # doc.user_name = emp_name
    # doc.address = date_of_join
    # doc.city = qualification
    doc.insert()
    # doc.save()
    frappe.msgprint("Complete")