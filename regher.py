max_value = 795028841
step = 360287471
previous_serial = 0
for i in range(0, max_value):
    previous_serial += step
    previous_serial %= max_value
    print("Serial: %09i" % previous_serial)
    
s = set()


with open("test.txt", "w+") as f:
    previous_serial = 0
    for i in range(0, 2711):
        previous_serial += 1811
        previous_serial %= 2711
        assert previous_serial not in s
        s.add(previous_serial)