import frappe

@frappe.whitelist()
def ping():
    return 'pong'
