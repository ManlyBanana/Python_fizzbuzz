import csv

maxFor = 1000000

counter = 0

f = open(str(os.getcwd()) + "\\bigOutput.csv", "w")

for counter in range(0,maxFor+1):
    output = ""
    if counter % 3 == 0:
        output = output + "Fizz"
    if counter % 5 == 0:
        output = output + "Buzz"
    if counter % 7 == 0:
        output = output + "Bonk"
    if counter % 7 != 0 and counter % 5 != 0 and counter % 3 != 0:
        output = str(counter)
    print(output)
    writer = csv.writer(f)
    writer.writerow(output)

f.close()