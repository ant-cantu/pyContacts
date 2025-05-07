contacts = []

print("*** Contact List ***\n");

while True:
    try:
        print("1. Add contact");
        print("2. Search contacts");
        print("3. View contacts");
        print("4. Exit\n");

        choice_str = input("Select an option (1-4): ");
        choice = int(choice_str);

        if choice == 1:
            #adding contacts
            name = input("Enter name: ");
            phone = input("Enter phone number: ");
            email = input("Enter email address: ");
            new_contact = {"name": name, "phone": phone, "email": email}
            contacts.append(new_contact);
            print("\nContact was added.\n");
        elif choice == 2:
            #searching contacts
            if len(contacts) == 0:
                print("\nThere are no contacts saved.\n");
                continue;
            
            search_str = input("Enter the name you would like to search: ");
            found_contact = False;
            for contact in contacts:
                if contact["name"] == search_str:
                    print(f"\nContact found:");
                    print(f"   Name: {contact['name']}");
                    print(f"   Phone: {contact['phone']}");
                    print(f"   Email: {contact['email']}\n");
                    found_contact = True;
                    break;
            if not found_contact:
                print("\nContact not found.\n");
        elif choice == 3:
            #display all contacts
            if len(contacts) == 0:
                print("\nThere are no contacts saved.\n");
                continue;
            
            print("\n**** All Contacts ***");
            for contact in contacts:
                print("   ************************");
                print(f"   Name: {contact['name']}");
                print(f"   Phone: {contact['phone']}");
                print(f"   Email: {contact['email']}");
                print("   ************************\n");
        elif choice == 4:
            #exit application
            print("Exiting application");
            break;
        else:
            print("\nError: Please select a valid option.\n");
    except ValueError:
        print("\nError: Please select a valid option.\n");
