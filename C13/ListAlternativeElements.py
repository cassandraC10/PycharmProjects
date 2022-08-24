def alternative_combination(List1, List2):
    return [sub[item] for item in range(len(List2))
            for sub in [List1, List2]]


List1 = ["a", "b", "c"]
List2 = [1, 2, 3]
print(alternative_combination(List1, List2))
