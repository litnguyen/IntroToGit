print('hello world')
xh = input("Enter hours: ")
xr = input("Enter rate: ")
pay = float(xh)*float(xr);
print("Pay:", pay)

if pay > 100 and pay <150:
    print("More money")
elif pay > 50:
    print("normal")
else: print("Little")

x = 'banana'
y = max(x)
print(y)

zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)
