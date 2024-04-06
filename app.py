from rich.console import Console
from rich.table import Table

def show_contacts_table(contacts): 
        rows = []
        for index, contact in enumerate(contacts, start=1):
            rows.append([str(index), contact['name'], contact['phone'], contact['email'], '♥︎' if contact['favorite'] else ''])

        columns = ['Índice', 'Nome', 'Telefone', 'Email', '']

        table = Table()
        for column in columns:
            table.add_column(column)
        for row in rows:
            table.add_row(*row)

        console = Console()
        console.print(table)


def add_contact(contacts, name, phone, email):
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'favorite': False
    }

    contacts.append(contact)
    print('Contato adicionado com sucesso!')

def list_contacts(contacts):
    print('\nLista de contatos:')
    if len(contacts) == 0:
        print('Nenhum contato encontrado.')
    else:
        show_contacts_table(contacts)

def update_contact(contacts, index, name, phone, email):
    contact = contacts[int(index) - 1]
    if contact is not None:
        contact['name'] = name
        contact['phone'] = phone
        contact['email'] = email
        print('Contato atualizado com sucesso!')
    else:
        print('Contato não encontrado.')

def toggle_favorite(contacts, index):
    contact = contacts[int(index) - 1]
    if contact is not None:
        contact['favorite'] = not contact['favorite']
        print('Status de favorito alterado com sucesso!')
    else:
        print('Contato não encontrado.')

def list_favorite_contacts():
    print('\nLista de contatos favoritos:')
    favorites = list(filter(lambda contact: contact['favorite'] == True, contacts))
    if len(favorites) == 0:
        print('Nenhum contato favorito encontrado.')
    else:
        show_contacts_table(favorites)

def remove_contact(contacts, index):
    contact = contacts[int(index) - 1]
    if contact is not None:
        contacts.remove(contact)
        print('Contato removido com sucesso!')
    else:
        print('Contato não encontrado.')

# Lista de contatos com dados de exemplo
contacts = [ 
    { 'name': 'John Doe', 'phone': '99999-9999', 'email': 'john.doe@email.com', 'favorite': False },
    { 'name': 'Jane Doe', 'phone': '88888-8888', 'email': 'jane.doe@email.com', 'favorite': True }  
]
while True:
    print('\nMenu deo gerenciador de contatos:')
    print('1. Adicionar contato')
    print('2. Listar contatos')
    print('3. Atualizar contato')
    print('4. Marcar/Desmarcar Favorito')
    print('5. Listar Favoritos')
    print('6. Remover contato')
    print('7. Sair')

    choice = input('Escolha uma opção: ')

    if choice == '1':
        name = input('Nome: ')
        phone = input('Telefone: ')
        email = input('Email: ')
        add_contact(contacts, name, phone, email)

    elif choice == '2':
        list_contacts(contacts)
    elif choice == '3':
        list_contacts(contacts)
        index = input('Escolha o contato deseja atualizar: ')
        name = input('Nome: ')
        phone = input('Telefone: ')
        email = input('Email: ')
        update_contact(contacts, index, name, phone, email)
    elif choice == '4':
        list_contacts(contacts)
        index = input('Escolha o contato deseja marcar/desmarcar: ')
        toggle_favorite(contacts, index)
    elif choice == '5':
        list_favorite_contacts()
    elif choice == '6':
        list_contacts(contacts)
        index = input('Escolha o contato deseja marcar/desmarcar: ')
        remove_contact(contacts, index)
    elif choice == '7':
        print('Saindo...')
        break
    else:
        print('Opção inválida. Tente novamente.')

