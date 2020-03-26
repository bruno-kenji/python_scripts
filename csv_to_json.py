import csv
import json

from format_cpf_or_cnpj import format_cpf_or_cnpj


def _build_key_value(body, row):
    try:
        document_number = format_cpf_or_cnpj(row["CPF do proprietário"])
        emails = row["Confirme o email do PP"].split(',')

        if not any(item["document-number"] == document_number for item in body["document_numbers_and_emails"]):
            return {
                "document-number": document_number,
                "emails": emails
            }

    except Exception as e:
        print(f'Ignoring wrong doc number: {row["CPF do proprietário"]}')
        pass


def _write_json_payload(body):
    with open('simba_cpf_emails_payload.json', mode='w') as payload_json:
        payload_json.write(json.dumps(body))
        payload_json.close()


def csv_to_json():
    body = {"document_numbers_and_emails": []}

    with open('/mnt/sda/downloads/cpfs_emails.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1

            key_value = _build_key_value(body, row)
            if key_value:
                body["document_numbers_and_emails"].append(key_value)

            line_count += 1

        print(f'Processed {line_count} lines.')
        csv_file.close()

    print(f'body: {body}')
    _write_json_payload(body)


if __name__ == "__main__":
    csv_to_json()
