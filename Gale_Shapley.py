def Gale_Shapley(menPref, womenPref):
    engaged = {}
    freemen = list(menPref.keys())

    while freemen:
        man = freemen.pop(0)
        manPref = menPref[man]
        for woman in manPref:
            if(woman not in engaged):
                engaged[woman] = man
            else:
                currentMan = engaged[woman]
                womanPref = womenPref[woman]
                if(womanPref.index(man) < womanPref.index(currentMan)):
                    freemen.append(currentMan)
                    engaged[woman] = man
        
    return engaged


# #Generate test cases
# menPref = {
#     'A': ['X', 'Y', 'Z'],
#     'B': ['Z', 'X', 'Y'],
#     'C': ['X', 'Z', 'Y']
# }
# #Woman also
# womenPref = {
#     'X': ['A', 'B', 'C'],
#     'Y': ['C', 'A', 'B'],
#     'Z': ['B', 'C', 'A']
# }

menPref = {}
womenPref = {}
num = int(input("Enter the number of men/women: "))
print("\nEnter men preferences:")
for i in range(num):
    pref = input("Enter the man: followed by his preferences: ").split()
    menPref[pref[0]] = pref[1:]

print("\nEnter woman preferences:")
for i in range(num):
    pref = input("Enter the woman: followed by her preferences: ").split()
    womenPref[pref[0]] = pref[1:]

print(Gale_Shapley(menPref, womenPref))