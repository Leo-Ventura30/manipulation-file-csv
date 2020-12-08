import csv

with open("data_users.csv", "w") as file:
    content = csv.writer(file)
    content.writerow(('Nome', 'Sobrenome', 'Turno'))
    content.writerow(('James', 'Vieira', 'T1'))
    content.writerow(('Victor', 'Souza', 'T2'))
    content.writerow(('Tales', 'Sousa', 'T3'))


with open("data_users.csv", "r", encoding="utf8", newline="\r\n") as file:
    read_file = csv.reader(file)
    dados = list(read_file)

for lines in dados:
    print(lines)
