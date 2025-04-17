def write_names(filename = "names.txt"):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            line_number = 1
            while True:
                first_name = input("Enter your first name (or 'stop' to finish)")
                if first_name.lower() == "stop":
                       break
                last_name = input("Enter your last name:")
                file.write(f"{line_number}. {first_name} {last_name}\n")
                line_number += 1
        print (f"First name and last name was uploaded into the file: {filename}")
    except Exception as e:
        print(f"This is error: {e}")
write_names()
