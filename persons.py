def write_person(input_filename ="persons.txt", young_filename = "young_persons.txt", old_filename="old_persons.txt"):
    try:
        with open(input_filename, "r", encoding="utf-8") as infile, \
                 open(young_filename,"w", encoding="utf-8") as youngfile, \
                 open (old_filename, "w", encoding="utf-8") as oldfile:
            for line in infile:
                name_city, age_str, city = line.strip().rsplit(',', 2)
                age = int(age_str.strip())
                if age < 50:
                   youngfile.write(f"{name_city.strip()}, {age}, {city.strip()}\n")
                else:
                   oldfile.write(f"{name_city.strip()}, {age}, {city.strip()}\n")
        print(f"Successfuly sorted and uploaded into the file: {young_filename}, {old_filename}")
    except FileNotFoundError:
        print(f"Warning: File '{input_filename}' was not found")
    except ValueError:
        print(f"Warning: Wrong Age format")
    except Exception as e:
        print(f"Unexpected Error: {e}")
write_person()
