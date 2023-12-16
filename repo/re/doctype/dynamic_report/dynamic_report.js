// Copyright (c) 2023, nextash and contributors
// For license information, please see license.txt

frappe.ui.form.on('Dynamic report', {
	validate: function (frm) {
		frm.add_custom_button('Open Report', () => {
			// frappe.set_route('Form', frm.doc.report, frm.doc.reference_name);
			// frappe.query_reports["'Dynamic report"] = {

			// 		// Add more filters as needed

			// 	// "onload": function (report) {
			// 	// 	// Add any additional onload behavior if needed
			// 	// },
			// };

		})
	}
});