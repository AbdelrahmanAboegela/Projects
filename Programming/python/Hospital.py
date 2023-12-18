import pandas as pd

# Function to load data from Excel file
def load_data():
    try:
        df = pd.read_excel('Hospital.xlsx')
        # Convert 'Specialization' column to integer type
        df['Specialization'] = df['Specialization'].astype(int)
        # Convert 'Patients' column to a list of tuples
        df['Patients'] = df['Patients'].apply(eval)
        # Convert 'Status' column to string type
        df['Patients'] = df['Patients'].apply(lambda x: [(name, str(status)) for name, status in x])
        # Convert 'Total' column to integer type
        df['Total'] = df['Total'].astype(int)
        return df
    except FileNotFoundError:
        # If the file doesn't exist, create a new dataframe
        df = pd.DataFrame({'Specialization': range(1, 21),
                           'Patients': [[] for _ in range(1, 21)],
                           'Total': [0 for _ in range(1, 21)]})
        return df

# Function to save data to Excel file
def save_data(df):
    # Convert 'Patients' column back to original format
    df['Patients'] = df['Patients'].apply(str)
    # Save dataframe to Excel file
    df.to_excel('Hospital.xlsx', index=False)

specializations_df = load_data()

def add_patient():
    spec = input("Enter specialization (1-20): ")
    if not spec.isdigit():
        print("Invalid specialization. Please enter a valid integer between 1 and 20.")
        return
    spec = int(spec)
    if spec not in range(1, 21):
        print("Invalid specialization.")
        return
    if specializations_df.at[spec - 1, 'Total'] == 10:
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
        specializations_df.at[spec - 1, 'Patients'].append((name, "normal"))
    else:
        patients = specializations_df.at[spec - 1, 'Patients']
        for i, (n, s) in enumerate(patients):
            if s == "normal":
                patients.insert(i+1, (name, "urgent" if status == "1" or status == "urgent" else "super urgent"))
                break
        else:
            patients.append((name, "urgent" if status == "1" or status == "urgent" else "super urgent"))
    specializations_df.at[spec - 1, 'Total'] += 1
    print("Patient added successfully.")
    save_data(specializations_df)

def print_patients():
    for _, row in specializations_df.iterrows():
        spec = row['Specialization']
        patients = row['Patients']
        count = len(patients)
        print(f"Specialization {spec}:")
        for i, (name, status) in enumerate(patients):
            print(f"{i+1}. {name} ({status})")
        print(f"Total patients in this specialization: {count}\n")

def get_next_patient():
    spec = input("Enter specialization (1-20): ")
    if not spec.isdigit():
        print("Invalid specialization. Please enter a valid integer between 1 and 20.")
        return
    spec = int(spec)
    if spec not in range(1, 21):
        print("Invalid specialization.")
        return
    patients = specializations_df.at[spec - 1, 'Patients']
    if not patients:
        print("No patients in queue.")
        return
    name, status = patients.pop(0)
    specializations_df.at[spec - 1, 'Total'] -= 1
    print(f"Next patient: {name} ({status})")
    save_data(specializations_df)

def remove_patient():
    spec = input("Enter specialization (1-20): ")
    if not spec.isdigit():
        print("Invalid specialization. Please enter a valid integer between 1 and 20.")
        return
    spec = int(spec)
    if spec not in range(1, 21):
        print("Invalid specialization.")
        return
    name = input("Enter patient name: ")
    patients = specializations_df.at[spec - 1, 'Patients']
    for i, (n, s) in enumerate(patients):
        if n == name:
            patients.pop(i)
            specializations_df.at[spec - 1, 'Total'] -= 1
            print("Patient removed successfully.")
            save_data(specializations_df)
            break
    else:
        print("No such patient found in queue.")

def add_dummy_data():
    from random import choice, randint
    for spec in range(1, 21):
        num_patients = specializations_df.at[spec - 1, 'Total']
        if num_patients >= 10:
            continue
        max_additional_patients = 10 - num_patients
        for i in range(randint(0, max_additional_patients)):
            status = choice(["normal", "urgent", "super urgent"])
            specializations_df.at[spec - 1, 'Patients'].append((f"dummy {i+1}", status))
            specializations_df.at[spec - 1, 'Total'] += 1
    print("Dummy data added successfully.")
    save_data(specializations_df)

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
