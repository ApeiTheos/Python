while True:
    print("================================")
    print("         BMI CALCULATOR")
    print("================================")
    print("1. Calculate BMI\n2. View BMI Categories\n3. Exit")
    print("================================")   

    while True:
        choices = input("Enter your choices: ")
        if choices in['1', '2', '3']:
            break
        else:
            print("Invalid choices. Please choose 1, 2, or 3.\n")

    if(choices == "1"):
        input_name = input("Enter your name: ")
        input_weight = float(input("Enter your weight in kilogram: "))
        input_height = float(input("Enter your height in meters: "))

        if input_weight and input_height <= 0:
            print("Invalid input. Weight and height must be greater than zero.")

        bmi_calc = input_weight / (input_height * input_height)

        print("\n================================")
        print("          BMI RESULT")
        print("================================")
        print(f"Name: {input_name}")
        print(f"Weight: {input_weight}")
        print(f"Height: {input_height}")
        print(f"BMI: {bmi_calc:.2f}")
        print(f"Category: ", end="")

        if bmi_calc < 18.5:
            print("Underweight")
        elif 18.5 <= bmi_calc < 25:
            print("Normal weight")
        elif 25  <= bmi_calc < 30:
            print("Overweight")
        else:
            print("Obesity")

        print("Thank you for using the BMI Calculator!\n")

    elif choices == "2":
        print("\n===== BMI Categories =====")
        print("Below 18.5 - Underweight")
        print("18.5 to below 25- Underweight")
        print("25 to below 30- Underweight")
        print("30 and above- Underweight")

    elif choices == "3":
        print("Thank you for using the BMI Calculator!")
        print(exit(0))

