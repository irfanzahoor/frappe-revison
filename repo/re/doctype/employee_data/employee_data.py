# Copyright (c) 2023, nextash and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class EmployeeData(Document):
	def validate(self):
  	#  if we wnat to check a dacument name through the specific field we use this
		doc = frappe.db.exists("Employee Records" ,{ "employee_name": self.employee_name})
		frappe.msgprint(f"{doc}")
 	 #  if we want to check our document exists or not we use this 
		# doc =  frappe.db.exists("Employee Records", "Emp-00022")
  	#  if we want to check all list of aur documents we use 
				# doc = frappe.get_list('Employee Records' ,'*')
				# frappe.msgprint(f"{doc}")
				# doc = frappe.get_list('Employee Records' ,'*' , filters = {'employee_name' : 'Tania Nawaz'})
				# doc.employee_name = 'Abdullah'
    # total number of Task records
		count = frappe.db.count('Employee Data')
		frappe.msgprint(f"Total Number of Documents ==> {count}")		
		# total number of Open tasks
		count = frappe.db.count('Employee Data', {'employee_status': self.employee_status})
		frappe.msgprint(f"Total Number of Status base Documents ==> {count}")	
  	
		# docs = frappe.db.truncate("Error Log")
		# frappe.msgprint(f"{docs}")
		# frappe.db.truncate("__Test Table")
		docs = frappe.db.describe("Employee Data")
		frappe.msgprint(f"{docs}")
	

