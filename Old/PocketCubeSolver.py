# 2x2x2 Rubik's Cube Solver
import Queue
import timeit

start = timeit.default_timer()

# groups of 4, white F, blue U, red R, green D, orange L, yellow B (IGNORE THIS LINE)
cube = range(0,24)

#cube = ['r','r','r','r','w','w','w','w','b','b','b','b','y','y','y','y','g','g','g','g','o','o','o','o']

sollength = 10

R = (0, 13, 2, 15, 4, 1, 6, 3, 10, 8, 11, 9, 12, 22, 14, 20, 16, 17, 18, 19, 7, 21, 5, 23)
Ri = (0, 5, 2, 7, 4, 22, 6, 20, 9, 11, 8, 10, 12, 1, 14, 3, 16, 17, 18, 19, 15, 21, 13, 23)
R2 = (0, 22, 2, 20, 4, 13, 6, 15, 11, 10, 9, 8, 12, 5, 14, 7, 16, 17, 18, 19, 3, 21, 1, 23)

U = (8, 9, 2, 3, 6, 4, 7, 5, 20, 21, 10, 11, 12, 13, 14, 15, 0, 1, 18, 19, 16, 17, 22, 23)
Ui = (16, 17, 2, 3, 5, 7, 4, 6, 0, 1, 10, 11, 12, 13, 14, 15, 20, 21, 18, 19, 8, 9, 22, 23)
U2 = (20, 21, 2, 3, 7, 6, 5, 4, 16, 17, 10, 11, 12, 13, 14, 15, 8, 9, 18, 19, 0, 1, 22, 23)

F = (2, 0, 3, 1, 4, 5, 19, 17, 6, 9, 7, 11, 10, 8, 14, 15, 16, 12, 18, 13, 20, 21, 22, 23)
Fi = (1, 3, 0, 2, 4, 5, 8, 10, 13, 9, 12, 11, 17, 19, 14, 15, 16, 7, 18, 6, 20, 21, 22, 23)
F2 = (3, 2, 1, 0, 4, 5, 13, 12, 19, 9, 17, 11, 7, 6, 14, 15, 16, 10, 18, 8, 20, 21, 22, 23)

RSet = (R, Ri, R2)
USet = (U, Ui, U2)
FSet = (F, Fi, F2)

NotRSet = USet + FSet
NotUSet = RSet + FSet
NotFSet = RSet + USet

RMoves = ('R', 'Ri', 'R2')
FMoves = ('F', 'Fi', 'F2')
UMoves = ('U', 'Ui', 'U2')
'''
RMoves = map(str,RSet)
UMoves = map(str,USet)
FMoves = map(str,FSet)

NotRMoves = map(str,NotRSet)
NotUMoves = map(str,NotUSet)
NotFMoves = map(str,NotFSet)
'''

Move = {R:'R', Ri:'Ri', R2:'R2', U:'U', Ui:'Ui', U2:'U2', F:'F', Fi:'Fi', F2:'F2'}

InverseMove = {'R':'Ri','F':'Fi','U':'Ui','Ui':'U','Ri':'R','Fi':'F','R2':'R2','F2':'F2','U2':'U2'}

q = Queue.Queue(maxsize = 0)

Solutions = {}


def NextStates(statestr):
    state = statestr.split(',')
    sol = Solutions[statestr]
    steps = sol.split(',')
    lastmove = steps[0]
    nextstate = [None]*24
    
    if lastmove in RMoves : nextmoves = NotRSet
    elif lastmove in UMoves : nextmoves = NotUSet
    else : nextmoves = NotFSet
    
    for move in nextmoves:
        for i in range(0,24):
            nextstate[i] = state[move[i]]
        nextstatestr = ','.join(str(x) for x in nextstate)
        if nextstatestr not in Solutions:
            Solutions[nextstatestr] = InverseMove[Move[move]] + ',' + sol
            if len(steps) < sollength:
                q.put(nextstatestr)
                
for fm in Move.keys():
    s = ",".join(str(x) for x in fm)
    q.put(s)
    Solutions[s] = InverseMove[Move[fm]]

while not (q.empty()):
    NextStates(q.get())

ColorMap = {'0':'r', '1':'r','2':'r','3':'r', '4':'w', '5':'w', '6':'w', '7':'w', '8':'b', '9':'b', '10':'b', '11':'b', '12':'y', '13':'y', '14':'y', '15':'y', '16':'g', '17':'g', '18':'g', '19':'g', '20':'o',  '21':'o', '22':'o', '23':'o'}

def Translate(numbers):
    s = numbers.split(",")
    ns = ""
    for i in range(0,24):
        ns += ColorMap[s[i]]
    return ns


f = open('Pocket Cube - God\'s Lookup Table','w')
for key,value in Solutions.items():
    f.write('%s : %s\n' % (Translate(key),value))
f.close()

stop = timeit.default_timer()
print "Run Time: " + str(stop - start) + " seconds"
