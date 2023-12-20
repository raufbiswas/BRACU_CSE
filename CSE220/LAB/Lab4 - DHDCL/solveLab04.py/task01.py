class Patient:
    def __init__(self, id, name, age, bg):
        self.patientID, self.patientName, self.patientAge, self.patientBG = id, name, age, bg
        self.next, self.prev = None, None

class WRM:
    def __init__(self):
        self.head = Patient(None, None, None, None)
        self.head.next, self.head.prev = self.head, self.head
        self.temp = self.head

    def RegisterPatient(self, id, name, age, bg):
        newPatient = Patient(id, name, age, bg)
        self.temp.next = newPatient
        newPatient.prev = self.temp
        newPatient.next = self.head
        self.head.prev = newPatient
        self.temp = newPatient
        print("Patient registered successfully.")

    def ServePatient(self):
        patient = self.head.next
        if patient != self.head:
            print(f"Patient being served: {patient.patientName}")
            self.head.next = patient.next
            patient.next.prev = self.head
        else:
            print("No patient to be served.")

    def CancelAll(self):
        if self.head.next != self.head:
            self.__init__()
            print("All appoinments of the patients are cancelled. Now, doctor can go to lunch.")
        else:
            print("No patients are waiting. Doctor can go to lunch.")

    def CanDoctorGoHome(self):
        if self.head.next == self.head:
            return True
        return False

    def ShowAllPatient(self):
        patient = self.head.next
        if patient != self.head:
            print("Waiting list: ")
            while patient != self.head:
                print(patient.patientName, end = " ")
                patient = patient.next
            print()
        else:
            print("No patients are waiting.")

    def ReverseTheLine(self):
        if self.head.next != self.head:
            self.head.next = self.head.prev
            currentPatient = self.head.next

            while currentPatient != self.head:
                tempPrev = currentPatient.prev
                tempNext = currentPatient.next
                currentPatient.next = tempPrev
                currentPatient.prev = tempNext
                prevPatient = currentPatient
                currentPatient = tempPrev

                if currentPatient == self.head:
                    self.head.prev = prevPatient
                    prevPatient.next = self.head
            self.ShowAllPatient()
        else:
            print("No patient is available. So, no need to reverse the line.")

wrm = WRM()

print("Welcome to Waiting Room Management(WRM) System\nYou are requested to choose an option...")

while True:
    print("_"*20)
    print("Available options:\n1. RegisterPatient()\n2. ServePatient()\n3. ShowAllPatients()\n4. CanDoctorGoHome()\n5. CancelAll()\n6. ReverseTheLine()\n7. exit")
    print("_"*20, "\n")
    option = int(input("Please choose an option: "))
    if option == 1:
        id = int(input("Enter patient ID: "))
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        bg = input("Enter patient bloodgroup: ")
        print("Registering your patient...")
        wrm.RegisterPatient(id, name, age, bg)
    elif option == 2:
        print("Serving Patient...")
        wrm.ServePatient()
    elif option == 3:
        print("Checking any patients are waiting or not...")
        wrm.ShowAllPatient()
    elif option == 4:
        print("Checking Doctor can go home or not...")
        can = wrm.CanDoctorGoHome()
        if can == True:
            print("Yes, no patient to be served. Doctor can go home.")
        else:
            print("Sorry, doctor can't go home. Patients are waiting.")
    elif option == 5:
        print("Canceling all appointments of the patients...")
        wrm.CancelAll()
    elif option == 6:
        print("Reversing the patient line...")
        wrm.ReverseTheLine()
    elif option == 7:
        break
    else:
        print("Sorry! No such option available right now.\nYou are requested to enter available option.")
if option == 7:
    print("Thank you for using Waiting Room Management(WRM) System.\nExiting...\nExited.")