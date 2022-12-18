import csv

def finalFormat(filename, finalfile):
    csvLines = []
    with open(filename, mode='r') as csvfile:
        csvFile = csv.reader(csvfile)
        for lines in csvFile:
            csvLines.append(lines)

            applines = csvLines[1:]
            update_lines = []
            for line in applines:

                wear = line[0][(line[0].rfind('(') + 1):-1]

                update_lines.append([line[0][:line[0].rfind('(')], wear, line[1], line[2]])

    with open(finalfile, mode='w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerow(
                ['hash_name', 'wear', 'steam_price', 'floatdb_price'])

            for line in update_lines:
                filewriter.writerow(line)
