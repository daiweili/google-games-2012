from fp_util import *

def all_splits(n, cands, ls1, ls2):
    if len(ls1) * 2 == n:
        return [(ls1, ls2 + cands)]
    elif len(ls2) * 2 == n:
        return [(ls1 + cands, ls2)]
    else:
        cand = [cands[0]]
        rest = cands[1:]
        return all_splits(n, rest, ls1 + cand, ls2) + \
            all_splits(n, rest, ls1, ls2 + cand)

def best_split(splits):
    best = min(splits, key=lambda split: abs(sum(split[0]) - sum(split[1])))
    return abs(sum(best[0]) - sum(best[1]))

if __name__ == '__main__':
    num_cases = read_int()
    for i in range(1, num_cases+1):
        line = read_list(int, False)
        num_players = line[0]
        players = line[1:]
        splits = all_splits(len(players), players, [], [])
        print "Case #{0}: {1}".format(i, best_split(splits))
        
