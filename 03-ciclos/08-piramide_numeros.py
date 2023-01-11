# Escriba un programa para hacer un patrón como una pirámide con números aumentados en 1
#    1
#   2 3
#  4 5 6
# 7 8 9 10

a = 0
for i in range(5):
    st = ""
    st += (5-i)*" "
    for j in range(i):
        a += 1
        st += " "+str(a)
    print(st)
