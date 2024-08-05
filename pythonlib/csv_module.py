# csv_module.py
import csv

def ler_csv(nome_arquivo):
    with open(nome_arquivo, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [row for row in reader]
