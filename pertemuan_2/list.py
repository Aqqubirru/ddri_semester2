makanan = ["bubur", "nasi goreng", "mie"]
minuman = ["jus jahe", "jus kucing", "jus oatmeal"]

print(makanan)
print(minuman)

print(minuman[0])
print(len(minuman))

minuman[1] = "kuku daffa"
del minuman[1]
print(minuman[1])
makanan.append("borgir")
print(makanan)