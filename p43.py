import itertools

if __name__ == "__main__":
    answer = []
    for combi in itertools.permutations('0123456789', 10):
        if int(combi[1]+combi[2]+combi[3]) % 2 == 0:
            if int(combi[2]+combi[3]+combi[4]) % 3 == 0:
                if int(combi[3]+combi[4]+combi[5]) % 5 == 0:
                    if int(combi[4]+combi[5]+combi[6]) % 7 == 0:
                        if int(combi[5]+combi[6]+combi[7]) % 11 == 0:
                            if int(combi[6]+combi[7]+combi[8]) % 13 == 0:
                                if int(combi[7]+combi[8]+combi[9]) % 17 == 0:
                                    answer.append(int(''.join(combi)))
    print(sum(answer))  