class DrinkMaker:
    def instruction (self, input_drink, input_sugar):
        if input_drink == "Tea":
            input_drink = "T"
        elif input_drink == "Coffee":
            input_drink = "C"
        elif input_drink == "Chocolate":
            input_drink = "H"

        input_stick = ""
        if input_sugar == "1" or input_sugar == "2":
            input_stick = "0"

        return (str(input_drink)+":"+str(input_sugar)+":"+str(input_stick))