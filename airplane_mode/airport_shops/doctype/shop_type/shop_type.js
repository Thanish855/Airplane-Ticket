// Copyright (c) 2025, thanisha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Shop Type", {
    refresh(frm) {
        frm.set_query('shop_type', function() {
            return {
                filters: {
                    enabled: 1
                }
            };
        });
	},
});
