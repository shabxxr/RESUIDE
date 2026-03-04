s='q255eZh-AMESYYCjCxWyzJIKvCjn5GrpBQowaffpZVH"'.strip('"') 
m=len(s)//2
a=s[:m][::-1]
b=s[m:]
def rot13(x):
 return ''.join(
chr((ord(c)-65+13)%26+65) if c.isupper() else 
chr((ord(c)-97+13)%26+97) if c.islower() else c 
for c in x
)
print(a + rot13(b))
