
f = open("myfile.txt", "a")
amin = [1,2,3]
#f.write(amin)
#f.truncate(0)
#f.close()

for x in amin:
    f = open("myfile.txt", "a")
    f.write(str(x))
    f.write(",")
    f.close()

f = open("myfile.txt", "r")
#print(f.read())
hi = f.read()
#print(list(hi))
hey = list(hi)
for x in hey:
    if x == ",":
        hey.remove(x)

string_list = ["1", "2", "3"]
integer_map = map(int, hey)
integer_list = list(integer_map)
print(integer_list)




