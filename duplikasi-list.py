# Teknik duplikasi pada list

x = ["obin", "riski", "sadik"]
print(f"x : {x}")

y = x
print(f"y : {y}")

x[0] = "habibi"
y.sort()
print(f"x diubah : {x}")
print(f"y setelah x diubah : \n{y}")

print(f" alamat memory x : {hex(id(x))}")
print(f" alamat memory y : {hex(id(y))}")

z = x.copy()
x[1] = "dadan"
print(f"x : {x}")
print(f"z : {z}")

print(f" alamat memory x : {hex(id(x))}")
print(f" alamat memory y : {hex(id(y))}")
print(f" alamat memory z : {hex(id(z))}")