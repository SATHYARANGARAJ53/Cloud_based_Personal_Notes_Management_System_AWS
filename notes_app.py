# EC2 => brain where user interacts
# dynamodb => database
# Lambda => automated backup engine
# S3 => backup repository(cloud archival storage)


# in ubuntu terminal -> commands to execute

# sudo apt update
# sudo apt install python3-pip -y
# pip3 install boto3
# python3 --version
# pip3 show boto3

# then move to python,

# python3
# import boto3
# ddb = boto3.client('dynamodb', region_name='us-east-1')
# print(ddb.list_tables())

# to open/create : nano file_name 
# to save : ctrl+o enter then exit(ctrl+x)
# to list files : ls
# to execute : python3 file_name(python3 notes_app.py)
 

import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('notes_table')
def create_note():
    title = input("Enter Note Title: ")

    print("Enter Note Content (type END on new line to finish):")
    lines = []
    while True:
        line = input()
        if line.upper() == "END":
            break
        lines.append(line)

    content = "\n".join(lines)

    note_id = str(uuid.uuid4())[:8]
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    table.put_item(
        Item={
            'note_id': note_id,
            'title': title,
            'content': content,
            'created_at': created_at
        }
    )

    print(f"Note created successfully with ID: {note_id}")
def view_notes():
    response = table.scan()
    items = response['Items']

    if not items:
        print("No notes found.")
    else:
        print("\n------ STORED NOTES ------")
        for note in items:
            print("ID:", note['note_id'])
            print("Title:", note['title'])
            print("Content:", note['content'])
            print("Created At:", note['created_at'])
            print("--------------------------")
def update_note():
    response = table.scan()
    items = response['Items']

    if not items:
        print("No notes available to update.")
        return

    print("\nAvailable Notes:")
    for note in items:
        print(f"ID: {note['note_id']} | Title: {note['title']}")

    note_id = input("Enter Note ID to update: ")
    new_title = input("Enter New Title: ")

    print("Enter New Content (type END on new line to finish):")
    lines = []
    while True:
        line = input()
        if line.upper() == "END":
            break
        lines.append(line)

    new_content = "\n".join(lines)

    table.update_item(
        Key={'note_id': note_id},
        UpdateExpression="set title=:t, content=:c",
        ExpressionAttributeValues={
            ':t': new_title,
            ':c': new_content
        }
    )

    print("Note updated successfully.")
def delete_note():
    response = table.scan()
    items = response['Items']

    if not items:
        print("No notes available to delete.")
        return

    print("\nAvailable Notes:")
    for note in items:
        print(f"ID: {note['note_id']} | Title: {note['title']}")

    note_id = input("Enter Note ID to delete: ")

    table.delete_item(
        Key={'note_id': note_id}
    )

    print("Note deleted successfully.")
while True:
    print("\n===== PERSONAL NOTES MANAGEMENT SYSTEM =====")
    print("1. Create Note")
    print("2. View Notes")
    print("3. Update Note")
    print("4. Delete Note")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_note()
    elif choice == '2':
        view_notes()
    elif choice == '3':
        update_note()
    elif choice == '4':
        delete_note()
    elif choice == '5':
        print("Exiting Application...")
        break
    else:
        print("Invalid choice. Try again.")
