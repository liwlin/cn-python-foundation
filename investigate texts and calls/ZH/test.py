import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


records = texts + calls 
def remove_duplicates(records):
    mix_records= []
    for i in records:
        mix_records += [i[0], i[1]]
    new_records = set(mix_records)
    return new_records
   

print("There are {} different telephone numbers in the records.".format(len(remove_duplicates(records))))