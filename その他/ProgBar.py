import sys, time
 
def prog_bar(t):
    length=100
    for i in range(length):
        sys.stdout.write('#'*i +' '*(100-i) + str(i) + "%  " + '\r')
        sys.stdout.flush()
        time.sleep(t)
    sys.stdout.write('#'*i +' '*(100-i) +"100% " +  '\n')
 
for i in range(4):
    prog_bar((4-i) * 0.02)