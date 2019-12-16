import csv

limit = 200
count = 0

single_a = [0,1,2,3,4,5,6,7,8,9,10]
single_b = [0,1,2,3,4,5,6,7,8,9,10]
single_c = [0,1,2,3,4,5,6,7,8,9,10]
bdouble_a = [0,1,2,3,4,5,6,7,8,9,10]
bdouble_b = [0,1,2,3,4,5,6,7,8,9,10]
bdouble_c = [0,1,2,3,4,5,6,7,8,9,10]
rigid_a = [0,1,2,3,4,5,6,7,8,9,10]
single_a_mezz = [0,1,2,3,4,5,6,7,8,9,10]
single_b_mezz = [0,1,2,3,4,5,6,7,8,9,10]
single_c_mezz = [0,1,2,3,4,5,6,7,8,9,10]
bdouble_a_mezz = [0,1,2,3,4,5,6,7,8,9,10]
bdouble_b_mezz = [0,1,2,3,4,5,6,7,8,9,10]
bdouble_c_mezz = [0,1,2,3,4,5,6,7,8,9,10]
extra = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

total_combinations = [["single_a","single_b","single_c","bdouble_a","bdouble_b","bdouble_c","rigid_a","single_b_mezz","bdouble_a_mezz","standalone","total_pallets"]]

sapallet = 0
sbpallet = 0
scpallet = 0
bapallet = 0
bbpallet = 0
bcpallet = 0
rapallet = 0
sbmpallet = 0
bampallet = 0
epallet = 0
tpallet = 0

sa_round = 0

for sa in single_a:
    if sa != 0:
        sapallet = sa*22
    tpallet += sapallet
    sb_round = tpallet
    if tpallet < limit:
        for sb in single_b:
            if sb != 0:
                sbpallet = 24
            tpallet += sbpallet
            sc_round = tpallet
            if tpallet < limit:
                for sc in single_c:
                    if sc != 0:
                        scpallet = 26
                    tpallet += scpallet
                    ba_round = tpallet
                    if tpallet < limit:
                        for ba in bdouble_a:
                            if ba != 0:
                                bapallet = 36
                            tpallet += bapallet
                            bb_round = tpallet
                            if tpallet < limit:
                                for bb in bdouble_b:
                                    if bb != 0:
                                        bbpallet = 34
                                    tpallet += bbpallet
                                    bc_round =tpallet
                                    if tpallet < limit:
                                        for bc in bdouble_c:
                                            if bc != 0:
                                                bcpallet = 32
                                            tpallet += bcpallet
                                            ra_round = tpallet
                                            if tpallet < limit:
                                                for ra in rigid_a:
                                                    if ra != 0:
                                                        rapallet = 8
                                                    tpallet += rapallet
                                                    sbm_round = tpallet
                                                    if tpallet < limit:
                                                        for sbm in single_b_mezz:
                                                            if sbm != 0:
                                                                sbmpallet = 48
                                                            tpallet += sbmpallet
                                                            bam_round = tpallet
                                                            if tpallet < limit:
                                                                for bam in bdouble_a_mezz:
                                                                    if bam != 0:
                                                                        bampallet = 72
                                                                    tpallet += bampallet
                                                                    e_round = tpallet
                                                                    if tpallet < limit:
                                                                        for e in extra:
                                                                            if e != 0:
                                                                                epallet = 1
                                                                            tpallet += epallet
                                                                            if tpallet < limit:
                                                                                total_combinations.append([sa,sb,sc,ba,bb,bc,ra,sbm,bam,e,tpallet])
                                                                                print([sa,sb,sc,ba,bb,bc,ra,sbm,bam,e])
                                                                                print(tpallet)
                                                                            else:
                                                                                print("BREAK Extra")
                                                                                tpallet = e_round
                                                                                sapallet = 0
                                                                                sbpallet = 0
                                                                                scpallet = 0
                                                                                bapallet = 0
                                                                                bbpallet = 0
                                                                                bcpallet = 0
                                                                                rapallet = 0
                                                                                sbmpallet = 0
                                                                                bampallet = 0
                                                                                epallet = 0
                                                                                break
                                                                        epallet = 0
                                                                        tpallet = e_round
                                                                    else:
                                                                        print("BREAK bam")
                                                                        tpallet = bam_round
                                                                        sapallet = 0
                                                                        sbpallet = 0
                                                                        scpallet = 0
                                                                        bapallet = 0
                                                                        bbpallet = 0
                                                                        bcpallet = 0
                                                                        rapallet = 0
                                                                        sbmpallet = 0
                                                                        bampallet = 0
                                                                        epallet = 0
                                                                        break
                                                                bampallet = 0
                                                                tpallet = bam_round
                                                            else:
                                                                print("BREAK sbm")
                                                                tpallet = sbm_round
                                                                sapallet = 0
                                                                sbpallet = 0
                                                                scpallet = 0
                                                                bapallet = 0
                                                                bbpallet = 0
                                                                bcpallet = 0
                                                                rapallet = 0
                                                                sbmpallet = 0
                                                                bampallet = 0
                                                                epallet = 0
                                                                break
                                                        tpallet = sbm_round
                                                        sbmpallet = 0
                                                    else:
                                                        print("BREAK ra")
                                                        tpallet = ra_round
                                                        sapallet = 0
                                                        sbpallet = 0
                                                        scpallet = 0
                                                        bapallet = 0
                                                        bbpallet = 0
                                                        bcpallet = 0
                                                        rapallet = 0
                                                        sbmpallet = 0
                                                        bampallet = 0
                                                        epallet = 0
                                                        break
                                                tpallet = ra_round
                                                rapallet = 0
                                            else:
                                                print("BREAK bc")
                                                tpallet = bc_round
                                                sapallet = 0
                                                sbpallet = 0
                                                scpallet = 0
                                                bapallet = 0
                                                bbpallet = 0
                                                bcpallet = 0
                                                rapallet = 0
                                                sbmpallet = 0
                                                bampallet = 0
                                                epallet = 0
                                                break
                                        tpallet = bc_round
                                        bcpallet = 0
                                    else:
                                        print("BREAK bb")
                                        tpallet = bb_round
                                        sapallet = 0
                                        sbpallet = 0
                                        scpallet = 0
                                        bapallet = 0
                                        bbpallet = 0
                                        bcpallet = 0
                                        rapallet = 0
                                        sbmpallet = 0
                                        bampallet = 0
                                        epallet = 0
                                        break
                                tpallet = bb_round
                                bbpallet = 0
                            else:
                                print("BREAK b")
                                tpallet = ba_round
                                sapallet = 0
                                sbpallet = 0
                                scpallet = 0
                                bapallet = 0
                                bbpallet = 0
                                bcpallet = 0
                                rapallet = 0
                                sbmpallet = 0
                                bampallet = 0
                                epallet = 0
                                break
                        tpallet = ba_round
                        bapallet = 0
                    else:
                        print("BREAK s3")
                        tpallet = sc_round
                        sapallet = 0
                        sbpallet = 0
                        scpallet = 0
                        bapallet = 0
                        bbpallet = 0
                        bcpallet = 0
                        rapallet = 0
                        sbmpallet = 0
                        bampallet = 0
                        epallet = 0
                        break
                tpallet = sc_round
                scpallet = 0
            else:
                print("BREAK s2")
                tpallet = sb_round
                sapallet = 0
                sbpallet = 0
                scpallet = 0
                bapallet = 0
                bbpallet = 0
                bcpallet = 0
                rapallet = 0
                sbmpallet = 0
                bampallet = 0
                epallet = 0
                break
        tpallet = sb_round
        sbpallet = 0
    else:
        print("BREAK s1")
        tpallet = 0
        sapallet = 0
        sbpallet = 0
        scpallet = 0
        bapallet = 0
        bbpallet = 0
        bcpallet = 0
        rapallet = 0
        sbmpallet = 0
        bampallet = 0
        epallet = 0
        break
    tpallet = sa_round
    sapallet = 0

print(total_combinations)

print(len(total_combinations))

def save_to_csv(total_combinations):
    with open('test.csv', 'w', errors='replace', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(total_combinations)
    csvFile.close()

save_to_csv(total_combinations)
