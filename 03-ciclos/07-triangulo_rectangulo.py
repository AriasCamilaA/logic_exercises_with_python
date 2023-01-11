# Escriba un programa para mostrar el patrón como un triángulo rectángulo con un número. El patrón como:
# 1
# 12
# 123
# 1234
# 12345

# a = [1,2,3,4,5]
# for i in range(1,6):
#     print(a[:i])

for i in range(5):
    st = ""
    for j in range(i+1):
        st +=str(j+1)
    print(st)