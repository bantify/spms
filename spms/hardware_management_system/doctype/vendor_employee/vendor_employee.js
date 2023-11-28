// Copyright (c) 2023, nbanik and contributors
// For license information, please see license.txt

 frappe.ui.form.on("vendor_employee", {
 	before_save(frm) {
	 frm.set_value("full_name", strip(frm.doc.first_name + " " + frm.doc.last_name));
 	},
 });
