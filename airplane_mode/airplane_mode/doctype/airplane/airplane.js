// Copyright (c) 2025, thanisha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane", {
 	refresh(frm) {
        const hasRole = frappe.user.has_role("Airport Authority Personnel");

        if (!hasRole) {
            // Hide the field for everyone else
            frm.set_df_property('initial_audit_completed', 'hidden', 1);
        } else {
            // Show and make it editable for authorized users
            frm.set_df_property('initial_audit_completed', 'hidden', 0);
            frm.set_df_property('initial_audit_completed', 'read_only', 0);
        }
    }
});

