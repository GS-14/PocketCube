import Queue
import timeit

start = timeit.default_timer()

#cube = ['r','r','r','r','w','w','w','w','b','b','b','b','y','y','y','y','g','g','g','g','o','o','o','o']
cube = 'rrrrwwwwbbbbyyyyggggoooo'

R = (0, 13, 2, 15, 4, 1, 6, 3, 10, 8, 11, 9, 12, 22, 14, 20, 16, 17, 18, 19, 7, 21, 5, 23)
U = (8, 9, 2, 3, 6, 4, 7, 5, 20, 21, 10, 11, 12, 13, 14, 15, 0, 1, 18, 19, 16, 17, 22, 23)
F = (2, 0, 3, 1, 4, 5, 19, 17, 6, 9, 7, 11, 10, 8, 14, 15, 16, 12, 18, 13, 20, 21, 22, 23)

Solutions = {}
q = Queue.Queue(maxsize = 0)

depth = 11

def NextStates(state):
    statesol = Solutions[state]
    enq = not (len(statesol.split(','))==depth-1)
    lastMove = (statesol.split(','))[-1][0]

    if lastMove == 'R':
        os = state
        for z in range(0,3):
            ns = ''
            for i in range (0,24):
                ns += os[F[i]]
            nsol = statesol+',F'
            if z == 0:
                nsol+='i'
            elif z==1:
                nsol+='2'
            if ns not in Solutions:
                Solutions[ns] = nsol
                if enq:
                    q.put(ns)
            os = ns

        os = state
        for z in range(0,3):
            ns = ''
            for i in range (0,24):
                ns += os[U[i]]
            nsol = statesol+',U'
            if z == 0:
                nsol+='i'
            elif z==1:
                nsol+='2'
            if ns not in Solutions:
                Solutions[ns] = nsol
                if enq:
                    q.put(ns)
            os = ns
                
    elif lastMove == 'F':
        os = state
        for z in range(0,3):
            ns = ''
            for i in range (0,24):
                ns += os[R[i]]
            nsol = statesol+',R'
            if z == 0:
                nsol+='i'
            elif z==1:
                nsol+='2'
            if ns not in Solutions:
                Solutions[ns] = nsol
                if enq:
                    q.put(ns)
            os = ns

        os = state
        for z in range(0,3):
            ns = ''
            for i in range (0,24):
                ns += os[U[i]]
            nsol = statesol+',U'
            if z == 0:
                nsol+='i'
            elif z==1:
                nsol+='2'
            if ns not in Solutions:
                Solutions[ns] = nsol
                if enq:
                    q.put(ns)
            os = ns
            
    else:
        os = state
        for z in range(0,3):
            ns = ''
            for i in range (0,24):
                ns += os[R[i]]
            nsol = statesol+',R'
            if z == 0:
                nsol+='i'
            elif z==1:
                nsol+='2'
            if ns not in Solutions:
                Solutions[ns] = nsol
                if enq:
                    q.put(ns)
            os = ns

        os = state
        for z in range(0,3):
            ns = ''
            for i in range (0,24):
                ns += os[F[i]]
            nsol = statesol+',F'
            if z == 0:
                nsol+='i'
            elif z==1:
                nsol+='2'
            if ns not in Solutions:
                Solutions[ns] = nsol
                if enq:
                    q.put(ns)
            os = ns

os = cube
for z in range(0,3):
    ns = ''
    nsol = 'F'
    for i in range (0,24):
        ns += os[F[i]]
    if z == 0:
        nsol+='i'
    elif z==1:
        nsol+='2'
    Solutions[ns] = nsol
    q.put(ns)
    os = ns

os = cube
for z in range(0,3):
    ns = ''
    nsol = 'U'
    for i in range (0,24):
        ns += os[U[i]]
    if z == 0:
        nsol+='i'
    elif z==1:
        nsol+='2'
    Solutions[ns] = nsol
    q.put(ns)
    os = ns
    
os = cube
for z in range(0,3):
    ns = ''
    nsol = 'R'
    for i in range (0,24):
        ns += os[R[i]]
    if z == 0:
        nsol+='i'
    elif z==1:
        nsol+='2'
    Solutions[ns] = nsol
    q.put(ns)
    os = ns


while not q.empty():
    NextStates(q.get())

stop = timeit.default_timer()
print "Run time: " + str(stop - start) + " seconds"   
    
f = open('PC BFS.txt','w')
for key,value in Solutions.items():
    f.write('%s : %s\n' % (key,value))
f.close()

stop2 = timeit.default_timer()
print "Write time: " + str(stop2 - stop) + " seconds"
    
        
    
    