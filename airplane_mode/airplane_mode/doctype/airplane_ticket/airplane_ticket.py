# Copyright (c) 2025, thanisha and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe.model.document import Document


class AirplaneTicket(Document):	
	def validate(self):
		self.calculate_total_amount()
		self.remove_duplicate_add_ons()
		self.exceeding()

	def calculate_total_amount(self):
		total_add_ons=0
		for x in self.add_ons:
			total_add_ons=total_add_ons+x.amount
		self.total_amount=self.flight_price+total_add_ons


	def on_submit(self):
		if self.status != "Boarded":
			frappe.throw("You can only submit the Airplane Ticket if the status is 'Boarded'.")

	def remove_duplicate_add_ons(self):
		add_on=[]
		unique_rows = []
		for addon in self.add_ons:
			if addon.item not in add_on :
				add_on.append(addon.item)
				unique_rows.append(addon)
			
		self.add_ons = unique_rows

	def before_insert(self):
		self.random_seat()
		self.random_gate()

	def random_seat(self):
		random_number = random.randint(1, 99)
		random_letter = random.choice(['A', 'B', 'C', 'D', 'E'])
		self.seat = f"{random_number}{random_letter}"

	def random_gate(self):
		random_number=random.randint(1, 10)
		letters = string.ascii_uppercase
		random_letter = random.choice(letters)
		self.gate_number=f"{random_number}{random_letter}"
	

	def exceeding(self):
		if self.flight:
			# Get the Flight document
			flight = frappe.get_doc("Airplane Flight", self.flight)
			if flight and flight.airplane:
				# Get the Airplane document associated with the Flight
				airplane = frappe.get_doc("Airplane", flight.airplane)
				if airplane:
					# Count existing Airplane Tickets for this Flight
					existing_tickets = frappe.db.count("Airplane Ticket", {"flight": self.flight})
					# Check if adding a new ticket would exceed the airplane's capacity
					if existing_tickets >= airplane.capacity:
						frappe.throw(f"Cannot create Airplane Ticket. Flight {self.flight} is fully booked. ")
						


				
			

	
	
			