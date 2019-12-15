limit = 150
count = 0

single = [0,1,2,3,4,5]
bdouble = [0,1,2,3,4,5]
extra = [0,1,2,3,4,5]

total_combinations = []

spallet = 0
bpallet = 0
tpallet = 0

for s in single:
    spallet = s*24
    tpallet += spallet
    if tpallet < limit:
        for b in bdouble:
            if b != 0:
                bpallet = 36
            tpallet += bpallet
            if tpallet < limit:
                total_combinations.append([s,b,tpallet])
                print([s,b])
                print(tpallet)
            else:
                tpallet = 0
                bpallet = 0
                break
print(total_combinations)


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
