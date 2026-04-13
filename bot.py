from telethon import TelegramClient
import asyncio
import time
from telethon import events

api_id = 'API ID'
api_hash = 'API HASH'



client = TelegramClient('BOT USERNAME', api_id, api_hash)
message_default = 'Message'


def main():
    # Create the client and connect

    client = TelegramClient('telehandler_session', api_id, api_hash)
    client.start()
    
    entity=client.get_entity(destination_user_username)
    @client.on(events.NewMessage(incoming=True))
    async def handler(event):
        print(time.asctime(), '-', event.message)
        time.sleep(2)
        await event.reply(message_default)
    print(time.asctime(), '-', 'Waiting for incoming messages...')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')


if __name__ == '__main__':
    main()
