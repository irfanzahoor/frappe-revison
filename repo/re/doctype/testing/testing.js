// Copyright (c) 2023, nextash and contributors
// For license information, please see license.txt

frappe.ui.form.on('Testing', {
	full_name: function (frm) {
		frm.call("frm_call", {
			name: "hello this is from ",

			// disable the button until the request is completed
			// btn: $('.primary-action'),
			// // freeze the screen until the request is completed
			// freeze: true,
			callback: (name) => {
				name: "this is from"
			},

		});
		

		// frappe.call({
		// 	method: 'repo.events.employee.book_data',
		// 	// args: {
		// 	// 	first_name, date_of_join, qualification
		// 	// },
		// 	callback: function (r) {
		// 		// Handle the response here
		// 		if (r.message) {
		// 			// You can do something with the response data if needed
		// 			console.log(r.message);
		// 		}
		// 	},
		// 	error: function (err) {
		// 		// Handle errors here
		// 		console.error(err);
		// 	}
		// });

		//if we want to set a field by other fields data we use this
		frm.set_value("full_name", frm.doc.first_name + " " + frm.doc.last_name);
		// //in case of form refresh we use frm.refresh() 
		// frm.refresh()
		// //if we want to save automaticcally we use frm.savr
		// frm.save();

		// //we use this in submitable doctype  submit form 
		// frm.save('Submit');

		// // cancel form
		// frm.save('Cancel');

		// // update form (after submit)
		// frm.save('Update');

		// if (frappe.user_roles.includes('Administrator')) {
		// 	frm.enable_save();
		// } else {
		// 	frm.disable_save();
		// }
		// frm.reload_doc();

		// frm.refresh_field('first_name');

		// if (frm.is_dirty()) {
		// 	frappe.show_alert('Please save form before attaching a file')
		// }
		// frm.doc.browser_data = navigator.appVersion;
		// frm.dirty();
		// frm.save();

		// if (!frm.is_new()) {
		// 	frm.add_custom_button('Click me', () => {
		// 		frappe.msgprint('Clicked custom button')
		// 		// change type of ungrouped button
		// 		// change type of a button in a group
		// 		// frm.change_custom_button_type('Closed', 'Set Status', 'danger');
		// 	})
		// 	frm.change_custom_button_type('Open Reference form', null, 'primary');
		// 	frm.clear_custom_buttons();
		// }

		// change the fieldtype of description field to Text
		frm.set_df_property('full_name', 'hidden', 1);

		// // set the options of the status field to only be [Open, Closed]
		// frm.set_df_property('status', 'options', ['Open', 'Closed'])

		// // set a field as mandatory
		// frm.set_df_property('title', 'reqd', 1)

		// // set a field as read only
		// frm.set_df_property('status', 'read_only', 1)


	}
});
