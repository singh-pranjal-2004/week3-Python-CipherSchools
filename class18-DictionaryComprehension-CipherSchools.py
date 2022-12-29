# dictionary comprehension
# square = {1:1, 2:4, 3:9}
square = {f"Square of {num} is":num**2 for num in range(1,11)}
for k,v in square.items():
    print(f"{k} : {v}")

string = "Pranjal"
# for i in string:
#     print(i)
word_count = {char:string.count(char) for char in string}
print(word_count)