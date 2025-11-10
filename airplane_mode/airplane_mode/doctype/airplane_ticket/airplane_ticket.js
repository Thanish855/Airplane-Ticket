// Copyright (c) 2025, thanisha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
        frm.add_custom_button("Assign seat",()=>{
            let dialog = new frappe.ui.Dialog({
                    title: __('Seat Number'),
                    fields: [
                        {
                            label: __('Seat Number'),
                            fieldname: 'seat_number',
                            fieldtype: 'Data',
                            reqd: 1
                        }
                    ],
                    primary_action_label: __("Assign Seat"),
                    primary_action: function(values) {
                        frm.set_value('seat', values.seat_number);
                        dialog.hide();
                    }
                });
                dialog.show();
            },"Actions");
        }
    });