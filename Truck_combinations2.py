import csv

limit = 500
count = 0

single_a = [0,1,2,3,4,5,6,7,8,9,10]
single_b = [0,1,2,3,4,5,6,7,8,9,10]
single_c = [0,1,2,3,4,5,6,7,8,9,10]
bdouble_a = [0,1,2,3,4,5,6,7,8,9,10]
bdouble_b = [0,1,2,3,4,5,6,7,8,9,10]
bdouble_c = [0,1,2,3,4,5,6,7,8,9,10]
rigid_a = [0,1,2,3,4,5,6,7,8,9,10]
extra = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

total_combinations = [["single_a","single_b","bdouble_a","standalone","total_pallets"]]

sapallet = 0
sbpallet = 0
bapallet = 0
epallet = 0
tpallet = 0

zeroround = 0

for sa in single_a:
    if sa != 0:
        sapallet = sa*22
    tpallet += sapallet
    firstround = tpallet
    if tpallet < limit:
        for sb in single_b:
            if sb != 0:
                sbpallet = 24
            tpallet += sbpallet
            secondround = tpallet
            if tpallet < limit:
                for ba in bdouble_a:
                    if ba != 0:
                        bapallet = 36
                    tpallet += bapallet
                    thirdround = tpallet
                    if tpallet < limit:
                        for e in extra:
                            if e != 0:
                                epallet = 1
                            tpallet += epallet
                            if tpallet < limit:
                                total_combinations.append([sa,sb,ba,e,tpallet])
                                print([sa,sb,ba,e])
                                print(tpallet)
                            else:
                                print("BREAK Extra")
                                tpallet = thirdround
                                sapallet = 0
                                sbpallet = 0
                                bapallet = 0
                                epallet = 0
                                break
                        epallet = 0
                        tpallet = thirdround
                    else:
                        print("BREAK b")
                        tpallet = secondround
                        sapallet = 0
                        sbpallet = 0
                        bapallet = 0
                        epallet = 0
                        break
                tpallet = secondround
                bapallet = 0
            else:
                print("BREAK s2")
                tpallet = firstround
                sapallet = 0
                sbpallet = 0
                bapallet = 0
                epallet = 0
                break
        tpallet = firstround
        sbpallet = 0
    else:
        print("BREAK s1")
        tpallet = 0
        sapallet = 0
        sbpallet = 0
        bapallet = 0
        epallet = 0
        break
    tpallet = zeroround
    sapallet = 0

print(total_combinations)

print(len(total_combinations))

def save_to_csv(total_combinations):
    with open('test.csv', 'w', errors='replace', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(total_combinations)
    csvFile.close()

save_to_csv(total_combinations)
