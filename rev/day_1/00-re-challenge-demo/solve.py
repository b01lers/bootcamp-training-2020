import gdb
import shlex

GUESSES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_{}"
GOOD = 0x00000000004012ec # replace me with the address of `call scream_abuse`

gdb.execute("file demo00")
gdb.execute("set print inferior-events off")
gdb.execute("set print thread-events off")

class NoStopBP(gdb.Breakpoint):
    def stop(self):
        return False

bp = NoStopBP("*{0}".format(GOOD))
bp.ignore_count = 1000000

flag = ""
while not flag.endswith("}"):
    for cur in GUESSES:
        test = flag + cur
        bp.hit_count = 0
        with open('flagfile', 'w') as f:
            f.write(test)
            f.write('\n')
        gdb.execute('''run < flagfile > /dev/null''')
        print(flag)
        if bp.hit_count >= len(test):
            flag = test
            flag = flag[:bp.hit_count]
            break
print("Got: ", flag)
