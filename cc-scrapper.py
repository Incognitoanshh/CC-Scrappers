import os
import time
from telethon.sync import TelegramClient

os.system('cls')
session = input('Enter your session: ')
client = TelegramClient(session, 'API_ID', 'API_HASH')

client.start()

txt_file = input('Enter the name and extension of the file to be scanned: ')

if os.path.exists(txt_file):
    entity_input = input('Do you want to send messages through a username (1) or a chat_id (2): ')

    try:
        entity_type = int(entity_input)
        
        if entity_type == 1 or entity_type == 2:
            if entity_type == 1:
                entity = input('Enter username: ')
            else:
                entity = int(input('Enter chat_id: '))   
            
            command_to_use = input('Enter the command to use (in lowercase): ')
            antispam = int(input('Enter the antispam that will be between checks (in seconds): '))

            with open(txt_file, 'r') as file_:
                for line in file_:
                    client.send_message(entity, f"/{command_to_use} {line}")
                    time.sleep(antispam + 3)

            client.send_message(entity, 'Automatic check process completed')
        else:
            print('Invalid option. Please choose between 1 and 2.')
    except ValueError:
        print('Invalid entry. Please enter a number.')
else:
    print(f'The File {txt_file} does not exist.')

client.disconnect()




