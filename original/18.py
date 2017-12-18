# Disclaimer: some of the ugliest code I have ever written.
# This doesn't even get the right answer (it hangs infinitely).

def alpha(a,n):
    
    return a+str(n) if a in 'abcdefghijklmnopqrstuvwxyz' else a

for l in 'abcdefghijklmnopqrstuvwxyz':
    exec(l + '0=0')
    exec(l + '1=0')
p0 = 0
p1 = 1
last_played = 0
instructions = [line.rstrip() for line in sys.stdin]
q0 = []
q1 = []
ind0 = ind1 = 0
waiting0 = waiting1 = False
count = 0
while (not waiting0) or (not waiting1):
    if ind0 < len(instructions):
        line0, *args0 = instructions[ind0].split()
        x = alpha(args0[0],0)
        y = None
        if len(args0) > 1:
            y = alpha(args0[1],0)
        if line0 == 'snd':
            q1.append(eval(x))
        if line0 == 'set':
            exec(x + '=' + y) 
        if line0 == 'add':
            exec(x + '+=' + y) 
        if line0 == 'mul':
            exec(x + '*=' + y) 
        if line0 == 'mod':
            exec(x + '%=' + y) 
        if line0 == 'jgz':
            if eval(x + '>0'):
                ind0 += eval(y) 
                ind0 -= 1
        ind0 += 1
        if line0 == 'rcv':
            if q0: 
                exec(x + '=' + str(q0.pop()))
                waiting0 = False
            else:
                waiting0 = True
                ind0 -= 1
    if ind1 < len(instructions):
        line1, *args1 = instructions[ind1].split()
        x = alpha(args1[0], 1) 
        y = None
        if len(args1) > 1:
            y = alpha(args1[1],1)
        if line1 == 'snd':
            q0.append(eval(x))
            count += 1
        if line1 == 'set':
            exec(x + '=' + y) 
        if line1 == 'add':
            exec(x + '+=' + y) 
        if line1 == 'mul':
            exec(x + '*=' + y) 
        if line1 == 'mod':
            exec(x + '%=' + y) 
        if line1 == 'jgz':
            if eval(x + '>0'):
                ind1 += eval(y) 
                ind1 -= 1
        ind1 += 1
        if line1 == 'rcv':
            if q1: 
                exec(x + '=' + str(q1.pop()))
                waiting1 = False
            else:
                waiting1 = True
                ind1 -= 1
print(count)
