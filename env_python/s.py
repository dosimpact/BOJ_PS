from copy import deepcopy

userG1 = {
    "name": "dodo"
}

userG2 = {
    "party": "amo"
}

copyed = deepcopy(userG1)
copyed.update(userG2)

print(userG1)
print(copyed)
