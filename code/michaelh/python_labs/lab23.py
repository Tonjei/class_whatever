'''
# Lab 23: Contact List


Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. Headers might consist of `name`, `favorite fruit`, `favorite color`. Open the CSV, convert the lines of text into a **list of dictionaries**, one dictionary for each user. The text in the header represents the **keys**, the text in the other lines represent the **values**.

```python
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)
```

Once you've processed the file, your list of contacts will look something like this...
```python
contacts = [
    {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
    {'name':'sam', 'favorite fruit':'pineapple' ...}
]
```

*Note: There is a `csv` library in Python that will do much of this for you. It is what you would use normally in a project, but for this lab you need to write all the logic yourself.*

## Version 2

Implement a CRUD REPL

- **C**reate a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
- **R**etrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
- **U**pdate a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
- **D**elete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.

## Version 3

When REPL loop finishes, write the updated contact info to the CSV file to be saved. I highly recommend saving a backup `contacts.csv` because you likely won't write it correctly the first time.
'''
def create_initial_list(attributes, contacts):
    contact_list = []
    num_attributes = len(attributes.split(','))
    for contact in contacts:
        cur_contact = {}
        for j in range(num_attributes):
            cur_contact[attributes.split(',')[j]] = contact.split(',')[j]
        contact_list.append(cur_contact)
    return contact_list

def create(contact_list, attributes):
    cur_contact = {}
    for attribute in attributes:
        cur_contact[attribute] = input(f'What is the contact\'s {attribute}? ')
    contact_list.append(cur_contact)

def retrieve(contact_list, attributes):
    first_name = input(f'What is the contact\'s {attributes[0]}? ')
    for contact in contact_list:
        if contact[attributes[0]] == first_name:
            for i in range(1, len(attributes)):
                print(f'{contact[attributes[0]]}\'s {attributes[i]} is {contact[attributes[i]]}')

def update(contact_list, attributes):
    first_name = input(f'What is the contact\'s {attributes[0]}? ')
    attribute_to_update = input(f'What would you like to update? ')
    for contact in contact_list:
        if contact[attributes[0]] == first_name and attribute_to_update in attributes:
            contact[attribute_to_update] = input(f'Enter the new {attribute_to_update}: ')

def delete(contact_list, attributes):
    first_name = input(f'What is the contact\'s {attributes[0]}? ')
    for i, contact in enumerate(contact_list):
        if contact[attributes[0]] == first_name:
            contact_list.pop(i)

filename = 'contacts.csv'
with open('/home/michael/Desktop/'+filename, 'r') as f:
    contents = f.read()
attributes = contents.split('\n')[0]
contacts = contents.split('\n')[1:len(contents)]
contact_list = create_initial_list(attributes, contacts)

attributes = attributes.split(',')
while True:
    REPL_function = input('How would you like to alter your contact list? ')
    REPL_function = REPL_function.lower()
    if REPL_function == 'done':
        break
    elif REPL_function == 'create':
        create(contact_list, attributes)
    elif REPL_function == 'retrieve':
        retrieve(contact_list, attributes)
    elif REPL_function == 'update':
        update(contact_list, attributes)
    elif REPL_function == 'delete':
        delete(contact_list, attributes)
    else:
        print('Enter \"create\", \"retrieve\", \"update\", \"delete\" or \"done\".')

save_str = ','.join(attributes)
print(contact_list)
for contact in contact_list:
    save_str += '\n'
    for i, attribute in enumerate(attributes):
        if i != len(attributes) - 1:
            save_str += contact[attribute] + ','
        else:
            save_str += contact[attribute]

filename = 'contacts.csv'
with open('/home/michael/Desktop/'+filename, 'w') as f:
    f.write(save_str)