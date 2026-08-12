def get_int_input(prompt):   #Reusable input validation function#

    while True:
        try: 
            return int(input(prompt))

        except ValueError:
            print("Please select a valid option")

