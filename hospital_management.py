import datetime

class HospitalOPD:
    def __init__(self):
        # Define doctor and appointment data structures [cite: 32]
        self.doctors = {
            "Dr. Smith": {"dept": "General Medicine", "queue": []},
            "Dr. Jones": {"dept": "Pediatrics", "queue": []},
            "Dr. Brown": {"dept": "Orthopedics", "queue": []}
        }
        self.consulted_patients = [] # Consultation tracking 
        self.token_counter = 100

    def register_patient(self, name, age, doctor_name):
        """Add patients and auto-generate doctor-wise tokens."""
        if doctor_name not in self.doctors:
            print(f"Error: Doctor {doctor_name} not found.")
            return

        self.token_counter += 1
        token = f"TK-{self.token_counter}"
        
        # Auto-assign estimated consultation time 
        # Assuming 15 mins per patient in the current queue
        wait_time = len(self.doctors[doctor_name]["queue"]) * 15
        est_time = datetime.datetime.now() + datetime.timedelta(minutes=wait_time)

        patient_data = {
            "token": token,
            "name": name,
            "age": age,
            "doctor": doctor_name,
            "dept": self.doctors[doctor_name]["dept"],
            "time": est_time.strftime("%H:%M"),
            "status": "Waiting"
        }

        # Maintain separate queues for each doctor [cite: 28, 35]
        self.doctors[doctor_name]["queue"].append(patient_data)
        print(f"Registered: {name} | Token: {token} | Est. Time: {patient_data['time']}")

    def search_patient(self, query):
        """Search patients by name or token number[cite: 28, 36]."""
        print(f"\nSearching for: '{query}'...")
        found = False
        for doc, info in self.doctors.items():
            for p in info["queue"]:
                if query.lower() in p["name"].lower() or query == p["token"]:
                    print(f"Found in {doc}'s Queue: {p}")
                    found = True
        if not found:
            print("No matching patient found.")

    def complete_consultation(self, doctor_name):
        """Mark patients as 'Consulted' and remove from active queue."""
        if doctor_name in self.doctors and self.doctors[doctor_name]["queue"]:
            patient = self.doctors[doctor_name]["queue"].pop(0)
            patient["status"] = "Consulted"
            self.consulted_patients.append(patient)
            print(f"\nConsultation complete for {patient['name']} (Token: {patient['token']})")
        else:
            print(f"\nNo patients in queue for {doctor_name}.")

    def display_queues(self):
        """Display doctor-wise queue details[cite: 38]."""
        print("\n--- CURRENT DOCTOR QUEUES ---")
        for doc, info in self.doctors.items():
            count = len(info["queue"])
            print(f"{doc} ({info['dept']}): {count} patient(s) waiting")
            for p in info["queue"]:
                print(f"  > {p['token']} - {p['name']}")
        print("----------------------------")

# --- Development Testing ---
if __name__ == "__main__":
    opd = HospitalOPD()

    # Step 1: Patient Registration [cite: 33]
    opd.register_patient("Alice Walker", 29, "Dr. Smith")
    opd.register_patient("Bob Martin", 45, "Dr. Smith")
    opd.register_patient("Charlie Day", 10, "Dr. Jones")

    # Step 2: Show Queues [cite: 38]
    opd.display_queues()

    # Step 3: Search Functionality [cite: 36]
    opd.search_patient("Alice")

    # Step 4: Complete Consultation [cite: 37]
    opd.complete_consultation("Dr. Smith")
    
    # Final View
    opd.display_queues()