from Katzee_processor import Katzee_input

print("WHAT I CAN HELP YOU TODAY?")
usrinput_origin = input(": ")

user_input = Katzee_input(usrinput_origin)
user_input.check_command()
