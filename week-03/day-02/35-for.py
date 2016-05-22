ah = ['kuty', 'macsk', 'cic']
# add to all elements an 'a' on the end

# ah elemei nem valtoynak
for a in ah:
    print(a + "a")

# ah elemei is valtoznak

for a in range(len(ah)):
    ah[a] += "a"
print(ah)
