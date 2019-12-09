str = "supercalifragilisticexpialidotious"
sub = "rag"
rep = "ornia"

i = 0
while i <= len(str):
    l = len(sub)
    if sub == str[i:i + l]:
        str = str[:i] + rep + str[i + l:]
    i += 1

print(str)