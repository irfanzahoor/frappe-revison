# Copyright (c) 2023, nextash and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class EmployeeRecords(Document):
    def validate(self):
        frappe.msgprint("hello this is a frappe ")
        
        # Fetching a single document of 'Employee Data' doctype
        doc = frappe.get_doc("Employee Data" ,self.employee_id)

        # Set the attributes of EmployeeRecords with values from the fetched document
        self.employee_name = doc.employee_name
        # self.employee_id = doc.employee_id
        self.employee_number = doc.employee_number
        self.dob = doc.dob
        self.gender = doc.gender
        self.email = doc.email
        self.country = doc.country
        self.date_of_joining = doc.date_of_joining
        self.designation = doc.designation
        self.employee_role = doc.employee_role
        self.employee_status = doc.employee_status
        self.termination_date = doc.termination_date
        self.basic_salary = doc.basic_salary
        self.address = doc.address

        frappe.msgprint(f"{doc}")
