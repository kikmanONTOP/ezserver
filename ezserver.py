import http.server
import threading




print('''

                         ______                     
 _________        .---"""      """---.              
:______.-':      :  .--------------.  :             
| ______  |      | :                : |             
|:______B:|      | |coded by kikman | |             
|:______B:|      | |                | |             
|:______B:|      | |  coded with ❤️  | |             
|         |      | |  fast and easy | |             
|:_____:  |      | |                | |             
|    ==   |      | :                : |             
|       O |      :  '--------------'  :             
|       o |      :'---...______...---'              
|       o |-._.-i___/'             \._              
|'-.____o_|   '-.   '-...______...-'  `-._          
:_________:      `.____________________   `-.___.-. 
                 .'.eeeeeeeeeeeeeeeeee.'.      :___:
               .'.eeeeeeeeeeeeeeeeeeeeee.'.         
              :____________________________:
''')
print("write stop to stop the server")





PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=None, **kwargs)

def start_server(server):
    print(f"Serving at port {PORT} view your website at http://localhost:8000")
    server.serve_forever()

def stop_server(server):
    print("Stopping the server...")
    server.shutdown()

web_folder = input("write the name of the folder to be run on your server (so you can test your web applications, php and sql etc without hosting: ")
Handler = MyHandler
Handler.directory = web_folder

server = http.server.HTTPServer(("localhost", PORT), Handler)
server_thread = threading.Thread(target=start_server, args=(server,))
server_thread.start()

try:
    while True:
        command = input()
        if command.strip().lower() == "stop":
            stop_server(server)
            break
except KeyboardInterrupt:
    stop_server(server)
