specializations = {i: [] for i in range(1, 21)}

def add_patient():
    spec = int(input("Enter specialization (1-20): "))
    if spec not in specializations:
        print("Invalid specialization.")
        return
    if len(specializations[spec]) == 10:
        print("Sorry, no more spots available for this specialization.")
        return
    name = input("Enter patient name: ")
    status = int(input("Enter patient status (0=normal, 1=urgent, 2=super urgent): "))
    if status not in [0, 1, 2]:
        print("Invalid status.")
        return
    if status == 0:
        specializations[spec].append((name, "normal"))
    else:
        for i, (n, s) in enumerate(specializations[spec]):
            if s == "normal":
                specializations[spec].insert(i+1, (name, "urgent" if status == 1 else "super urgent"))
                break
        else:
            specializations[spec].append((name, "urgent" if status == 1 else "super urgent"))
    with open("C:/Users/Blu-Ray/Desktop/Hospital.txt", "a") as f:
        f.write(f"{spec},{name},{status}\n")
    print("Patient added successfully.")

def print_patients():
    for spec, patients in specializations.items():
        print(f"Specialization {spec}:")
        for i, (name, status) in enumerate(patients):
            print(f"{i+1}. {name} ({status})")
        print()

def get_next_patient():
    spec = int(input("Enter specialization (1-20): "))
    if spec not in specializations:
        print("Invalid specialization.")
        return
    with open("C:/Users/Blu-Ray/Desktop/Hospital.txt", "r") as file:
        data = file.readlines()
        line_number = (spec - 1) * 11
        patients = data[line_number:line_number+10]
        if not patients:
            print("No patients in queue.")
            return
        next_patient = patients[0].strip().split(",")
        name, status = next_patient[0], next_patient[1]
        data[line_number:line_number+10] = patients[1:]
    with open("C:/Users/Blu-Ray/Desktop/Hospital.txt", "w") as file:
        file.writelines(data)
    print(f"Next patient: {name} ({status})")

def remove_patient():
    spec = int(input("Enter specialization (1-20): "))
    if spec not in specializations:
        print("Invalid specialization.")
        return
    name = input("Enter patient name: ")
    for i, (n, s) in enumerate(specializations[spec]):
        if n == name:
            specializations[spec].pop(i)
            with open("C:/Users/Blu-Ray/Desktop/Hospital.txt", "r") as f:
                lines = f.readlines()
            with open("C:/Users/Blu-Ray/Desktop/Hospital.txt", "w") as f:
                for line in lines:
                    if not line.startswith(f"{spec},{name},"):
                        f.write(line)
            print("Patient removed successfully.")
            break
    else:
        print("No such patient found in queue.")

def add_dummy_data():
    from random import choice, randint
    with open("C:/Users/Blu-Ray/Desktop/Hospital.txt", "w") as f:
        for spec in specializations:
            for i in range(randint(0, 10)):
                status = choice(["normal", "urgent", "super urgent"])
                name = f"dummy {i+1}"
                specializations[spec].append((name, status))
                f.write(f"{spec},{name},{status}\n")
    print("Dummy data added successfully.")
    
while True:
    print("Please choose an option:")
    print("1. Add new patient")
    print("2. Print all patients")
    print("3. Get next patient")
    print("4. Remove a leaving patient")
    print("5. Add dummy data")
    print("6. End the program")
    choice = input(": ")
    if choice == "1":
        add_patient()
    elif choice == "2":
        print_patients()
    elif choice == "3":
        get_next_patient()
    elif choice == "4":
        remove_patient()
    elif choice == "5":
        add_dummy_data()
    elif choice == "6":
        break
    else:
        print("Invalid option.")
