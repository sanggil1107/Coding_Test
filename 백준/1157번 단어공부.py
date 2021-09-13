alphabet = [0] * 26
s = input()
s = s.upper()

for i in s:
    alphabet[ord(i)-65] += 1

m = max(alphabet)
result = list(filter(lambda e:alphabet[e] == m, range(len(alphabet))))

if len(result) > 1:
    print('?')
else:
    print(chr(result[0] + 65))