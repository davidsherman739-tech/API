cisla = [5, -3, 18, 0, -11, 42, 9]
jmena = ["Karel", "Eva", "Martin", "Tereza", "Alice", "David"]
kody = ["abc000", "xy-12", "000test", "hello", "88AAA", "kod123"]

# 1
for hodnota in cisla:
    if hodnota < 0:
        continue

    print(hodnota)

print("-----")

# 2
index = 0

while index < len(jmena):

    if jmena[index] == "Alice":
        break

    print(jmena[index])
    index += 1

print("-----")

# 3
nova_data = [item for item in kody if "0" in item]

print(nova_data)

print("-----")

# dobrovolný úkol

for text in kody:

    for i in range(len(text) - 2):

        if text[i] == text[i + 1] == text[i + 2]:
            print(text)
            break
