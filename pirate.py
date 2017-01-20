print("Arr, matey")
for i in range(100):
	print(str(i) + "bottles of rum")
with open('treasure.txt') as fh:
  for line in fh:
    print(line)

with open('map.txt', 'w') as fh:
  for i in range(10):
    fh.write("Walk " + str(i) + " paces left.")

