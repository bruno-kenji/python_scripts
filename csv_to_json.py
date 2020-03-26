import csv
import json

body = {"document_numbers_and_emails": []}

with open('/mnt/sda/downloads/cpfs_emails.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1

        body["document_numbers_and_emails"].append({
            "document_number": row["CPF do proprietário"],
            "emails": [row["Confirme o email do PP"]]
        })
        line_count += 1

    print(f'Processed {line_count} lines.')
    csv_file.close()

print(f'body: {body}')

with open('simba_cpf_emails_payload.json', mode='w') as payload_json:
    payload_json.write(json.dumps(body))
    payload_json.close()
