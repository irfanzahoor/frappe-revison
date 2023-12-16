// Copyright (c) 2023, nextash and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee', {
	validate: function (frm) {
		// Access the child table data
		var child_table_data = frm.doc.employees;

		// Add a row to the child table
		var new_row = frappe.model.add_child(frm.doc, 'Employee Child', 'employees');


		frappe.msgprint('A row has been added to the links table 🎉 ');

		// Assign values from the develop table to the child table row
		new_row.emp_name = frm.doc.emp_name;
		new_row.date_of_join = frm.doc.date_of_join;
		new_row.gender = frm.doc.gender;
		new_row.qualification = frm.doc.qualification;
		new_row.role = frm.doc.role;
		new_row.salary = frm.doc.salary;
		// ... assign other fields as needed

		// Refresh the child table to reflect the changes
		frm.fields_dict['employees'].grid.refresh();

		// Your existing code
	}
});

