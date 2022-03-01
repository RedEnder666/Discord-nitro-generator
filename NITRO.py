import random, string, webbrowser

amount = int(input('Укажите количество кодов для генерации: '))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[GENERATED] {code}')
    webbrowser.open(code, new=0, autoraise=True)
    value += 1
