import output_printer

def Main_2_reader(usrin):

  command = ["//learn//, //newmem//, //recognize//, //forget//" ]

  useriput = usrin

  command_found = None

  for cmd in command:
      if cmd in command:
          command_found = cmd
          break
     
  if command_found is not Not:
      output_printer.p_command(command_found)
  else:
      print("No command detected")
