a = {1: "a"}

b = {}

for el in a:
	b[el] = a[el]

a[1] = "ba"
print(b)

# model = {name:, user:, source:, source_link: }
first = ["first.png", "EricAlcaide", "Pexels", "pexels.com"]
second = ["second.png", "EricAlcaide", "Pexels", "pexels.com"]
third = ["third.png", "EricAlcaide", "Pexels", "pexels.com"]
fourth = ["fortuh.png", "EricAlcaide", "Pexels", "pexels.com"]

def linker(data):
	base = "/add_image/"
	for i in first:
		base += i+"/"
	return base

print(linker(first))
print(linker(second))


print(str(first))