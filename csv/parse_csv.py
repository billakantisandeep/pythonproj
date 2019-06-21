import csv  #CSV module makes easy than the string functions.

with open('C://Users/sbillakanti/pythonlearning/csv/new_names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)

# with open('C:\\Users\\sbillakanti\\pythonlearning\\csv\\names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     with open('C:\\Users\\sbillakanti\\pythonlearning\\csv\\new_names.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')

#         for line in csv_reader:
#             csv_writer.writerow(line)