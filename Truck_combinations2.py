import csv

limit = 500
count = 0

single = [0,1,2,3,4,5,6,7,8,9,10]
singletwo = [0,1,2,3,4,5,6,7,8,9,10]
bdouble = [0,1,2,3,4,5,6,7,8,9,10]
extra = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

total_combinations = [["single_a","single_b","bdouble_a","standalone","total_pallets"]]

spallet = 0
stwopallet = 0
bpallet = 0
epallet = 0
tpallet = 0

for s in single:
    if s != 0:
        spallet += 22
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
                        epallet = 0
                        tpallet = thirdround
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
        tpallet = firstround
    else:
        print("BREAK s1")
        tpallet = 0
        spallet = 0
        stwopallet = 0
        bpallet = 0
        epallet = 0
        break
    tpallet = 0

print(total_combinations)

print(len(total_combinations))

def save_to_csv(total_combinations):
    with open('test.csv', 'w', errors='replace', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(total_combinations)
    csvFile.close()

save_to_csv(total_combinations)
