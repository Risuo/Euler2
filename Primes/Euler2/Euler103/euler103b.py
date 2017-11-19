import itertools


def create_subsets(full_set):
    subsets = []
    for i in range(1, len(full_set)):
        subsets.append(itertools.combinations(full_set, i))
    subsets = [list(item) for sublist in subsets for item in sublist]
    return subsets


def check_sum(set1, set2):
    return sum(set1) != sum(set2)


def check_inequality(set1, set2):
    if len(set1) > len(set2):
        return sum(set1) > sum(set2)
    return True


def check_all(subsets):
    for s1 in subsets:
        for s2 in subsets:
            if len(s1) != len(set(s1) or len(s2) != len(set(s2))):
                return False
            if s1 != s2 and len(set(s1) & set(s2)) == 0:
                if not check_sum(list(s1), list(s2)):
                    return False
                if not check_inequality(list(s1), list(s2)):
                    return False
    return True


base_array = [21, 30, 39, 40, 41, 42, 45]
#base_array = [11, 17, 20, 22, 23, 24]
#base_array = [3, 5, 6, 7]
look_range = 3
look_array = range(-look_range, look_range + 1)
possible_arrays = [[x+y for y in look_array] for x in base_array]
all_arrays = itertools.product(*possible_arrays)


end_set = []
min_array = 10000000
for test_set in all_arrays:
    test_set = sorted(test_set)
    test = check_all(create_subsets(test_set))
    #print test
    if test:
        if (sum(test_set) < min_array):
            end_set = test_set
            min_array = sum(test_set)
        print test_set

print end_set