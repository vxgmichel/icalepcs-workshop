import asyncio

import time


async def handle_echo(reader, writer):
    data = await reader.readline()
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print("Received %r from %r" % (message, addr))
    if "Hello World" in message:
        return_message = "You are lazy!"
    else:
        return_message = "HELLO! " + message.upper()

    # await loop.run_in_executor(None, time.sleep, 3)
    time.sleep(3)

    print("Send: %r" % return_message)
    writer.write(return_message.encode())
    await writer.drain()

    print("Close the client socket")
    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, '', 4567, loop=loop)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
