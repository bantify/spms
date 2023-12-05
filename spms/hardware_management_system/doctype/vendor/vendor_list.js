frappe.listview_settings['vendor'] = {
	hide_name_column: true,
    button: {
        show(doc) {
            return true;
        },
        get_label() {
            return 'View';
        },
        get_description(doc) {
            return __('View {0}', [`${doc.name}`])
        },
        action(doc) {
            console.log(doc)
        }
    }
}
	
