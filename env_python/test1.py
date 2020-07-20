
now = "703825146"

next = list(now)
tmp = next[zeroIdx]
next[zeroIdx] = next[nx*3+ny]
next[nx*3+ny] = tmp
next = "".join(next)
print("debug", next)
