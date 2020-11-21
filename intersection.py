def intersection(L):
    L_sets = []
    for l in L: #  [ [[], []], [[], []] ]  ---->  [ {(), ()}, {(), ()} ],  где {} это set "множество"
        l_tuples = [tuple(x) for x in l]  # Списки в списке привожу к таплам
        L_sets.append(set(tuple(l_tuples)))
    return set.intersection(*L_sets)

if __name__ == "__main__":
    L1 = [[0, 1], [2, 6, 9], [3, 5], [4,8], [7]]
    L2 = [[0, 1], [2, 6, 9], [3, 4, 7], [5, 8]]
    L3 = [[2, 6, 9]]
    L = [L1, L2, L3]
    print(intersection(L))