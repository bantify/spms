// Copyright (c) 2023, nbanik and contributors
// For license information, please see license.txt

// frappe.ui.form.on("case", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('case', {
  vendor(frm) {
      frm.set_query('assignee', function() {
       return {
		filters: {
	         'vendor': frm.doc.vendor
				}
		};
	});
	},

   validate(frm) {
         if (frm.doc.status == "Closed")
            {
             frm.set_df_property('resolve_date', 'reqd', 1);
             frm.set_df_property('replace_hardware_serial', 'reqd', 1);
            }
        }
})
