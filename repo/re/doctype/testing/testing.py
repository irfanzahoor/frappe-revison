# Copyright (c) 2023, nextash and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

from repo.events.employee import book_data

class Testing(Document):
	@frappe.whitelist()
	def frm_call(self):
		# full_name = name
		frappe.msgprint(f"{self.full_name}")
	def validate(self):
		doc = frappe.get_list('Employee' ,'*')
		frappe.msgprint(f"{doc}") 
   
