import time

c = "RUNNING COMMAND"
b = "THINKING THOUGHTS"
a = "RUNNING ACTIONS"

def p.command(runner):
    print(a)
    time.sleep(0.2)
    print(c)
    print(runner)
    return runner
