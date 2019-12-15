limit = 100
count = 0

single = [0,1,2,3,4,5,6,7,8,9,10]
singletwo = [0,1,2,3,4,5,6,7,8,9,10]
bdouble = [0,1,2,3,4,5,6,7,8,9,10]
extra = [0,1,2,3,4,5,6,7,8,9,10]

total_combinations = []

spallet = 0
stwopallet = 0
bpallet = 0
epallet = 0
tpallet = 0

for s in single:
    spallet = s*22
    tpallet += spallet
    firstround = tpallet
    if tpallet < limit:
        for stwo in singletwo:
            if stwo != 0:
                stwopallet = 24
            tpallet += stwopallet
            secondround = tpallet
            if tpallet < limit:
                for b in bdouble:
                    if b != 0:
                        bpallet = 36
                    tpallet += bpallet
                    thirdround = tpallet
                    if tpallet < limit:
                        for e in extra:
                            if e != 0:
                                epallet = 1
                            tpallet += epallet
                            if tpallet < limit:
                                total_combinations.append([s,stwo,b,e,tpallet])
                                print([s,stwo,b,e])
                                print(tpallet)
                            else:
                                print("BREAK Extra")
                                tpallet = thirdround
                                stwopallet = 0
                                bpallet = 0
                                epallet = 0
                                break
                    else:
                        print("BREAK b")
                        tpallet = secondround
                        stwopallet = 0
                        bpallet = 0
                        epallet = 0
                        break
                tpallet = secondround
                epallet = 0
            else:
                print("BREAK s2")
                tpallet = firstround
                stwopallet = 0
                bpallet = 0
                epallet = 0
                break

print(total_combinations)

print(len(total_combinations))


#for s in single:
#    tpalletcount = 0
#    spalletcount = 0
#    bpalletcount = 0
#    combination = []
#    spalletcount += s * 24
#    tpalletcount += spalletcount
#    print(tpalletcount)
#    if tpalletcount < limit:
#        combination.append(s)
#        for b in bdouble:
#            bpalletcount += b * 36
#            if bpalletcount + tpalletcount < limit:
#                print(str(bpalletcount)+"text")
#                combination.append(b)
#                total_combinations.append(combination)
#                combination = []
#            else:
#                break
#        print(combination)
#        total_combinations.append(combination)
#        print(total_combinations)
#    else:
#        break
