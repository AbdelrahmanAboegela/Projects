specializations = {i: [] for i in range(1, 21)}

def add_patient():
    spec = input("Enter specialization (1-20): ")
    if not spec.isdigit():
        print("Invalid specialization. Please enter a valid integer between 1 and 20.")
        return
    spec = int(spec)
    if spec not in specializations:
        print("Invalid specialization.")
        return
    if len(specializations[spec]) == 10:
        print("Sorry, no more spots available for this specialization.")
        return
    name = input("Enter patient name: ")
    if not name.isalpha():
        print("Invalid name. Please enter a valid string.")
        return
    status = input("Enter patient status (0=normal, 1=urgent, 2=super urgent): ")
    if status not in ["0", "1", "2", "normal", "urgent", "super urgent"]:
        print("Invalid status.")
        return
    if status == "0" or status == "normal":
        specializations[spec].append((name, "normal"))
    else:
        for i, (n, s) in enumerate(specializations[spec]):
            if s == "normal":
                specializations[spec].insert(i+1, (name, "urgent" if status == "1" or status == "urgent" else "super urgent"))
                break
        else:
            specializations[spec].append((name, "urgent" if status == "1" or status == "urgent" else "super urgent"))
    print("Patient added successfully.")

def print_patients():
    for spec, patients in specializations.items():
        count = 0
        print(f"Specialization {spec}:")
        for i, (name, status) in enumerate(patients):
            count += 1
            print(f"{count}. {name} ({status})")
        print(f"Total patients in this specialization: {count}\n")

def get_next_patient():
    spec = input("Enter specialization (1-20): ")
    if not spec.isdigit():
        print("Invalid specialization. Please enter a valid integer between 1 and 20.")
        return
    spec = int(spec)
    if spec not in specializations:
        print("Invalid specialization.")
        return
    if not specializations[spec]:
        print("No patients in queue.")
        return
    name, status = specializations[spec].pop(0)
    print(f"Next patient: {name} ({status})")

def remove_patient():
    spec = input("Enter specialization (1-20): ")
    if not spec.isdigit():
        print("Invalid specialization. Please enter a valid integer between 1 and 20.")
        return
    spec = int(spec)
    if spec not in specializations:
        print("Invalid specialization.")
        return
    name = input("Enter patient name: ")
    for i, (n, s) in enumerate(specializations[spec]):
        if n == name:
            specializations[spec].pop(i)
            print("Patient removed successfully.")
            break
    else:
        print("No such patient found in queue.")

def add_dummy_data():
    from random import choice, randint
    for spec in specializations:
        num_patients = len(specializations[spec])
        if num_patients >= 10:
            continue
        max_additional_patients = 10 - num_patients
        for i in range(randint(0, max_additional_patients)):
            status = choice(["normal", "urgent", "super urgent"])
            specializations[spec].append((f"dummy {i+1}", status))
        specializations[spec].sort(key=lambda x: ("super urgent", "urgent", "normal").index(x[1]))
    print("Dummy data added successfully.")


while True:
    print("Please choose an option:")
    print("1. Add new patient")
    print("2. Print all patients")
    print("3. Get next patient")
    print("4. Remove a leaving patient")
    print("5. Add dummy data")
    print("6. End the program")
    choice = input("Enter Your Choice: ")
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
