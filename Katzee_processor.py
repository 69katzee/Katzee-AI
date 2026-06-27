class Katzee_input:
    
    def __init__(self, user_input):
        self.user_input = user_input
        
    def check_command(self):
        print("checking command. . .")
        
        if self.user_input.startswith("!"):
            command_found = True
            print("Command found.")
            return command_found
        else:
            command_found = False
            print("No command found.")
            return command_found

    
