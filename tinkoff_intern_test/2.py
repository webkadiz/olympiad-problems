n = int(input())

membersMap = {}

for command in range(n):
    membersStr = input()
    members = membersStr.split()

    membersSet = set(members)
    membersHash = str(membersSet)

    membersMap.setdefault(membersHash, 0)
    membersMap[membersHash] += 1

print(max(membersMap.values()))
