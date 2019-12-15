import grpc;
import chat_pb2 as chat
import chat_pb2_grpc as chat_grpc
import datetime

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = chat_grpc.ChatAdminStub(channel)

# create a valid request message
#film = proto_pb2.GetFilmRequest(id="")

# make the call
#response = stub.GetFilm(film)



#response = stub.ListFilms(films)

# et voilà
#print(response)

usuario1 = chat.Usuario(correo = "test12111@hotmail.com", username ="fernix")
usuario2 = chat.Usuario(correo = "test21111@hotmail.com", username ="fernix3")
usuarioChat1 = chat.usuariosEnChat(usuario = usuario1, idChat = 0)
usuarioChat2 = chat.usuariosEnChat(usuario = usuario2, idChat = 0)
#users = [chat.Usuario(correo = "soy@hotmail.com", username ="fernix"),chat.Usuario(correo = "soy2@hotmail.com", username ="fernix2")]
c = chat.Chat(idchat = 1, nombre = "test121")
creatChat = chat.CreateChatRequest(chat = c, usuariosenchat = [usuarioChat1,usuarioChat2])
#resp = stub.CreateChat(creatChat)
#print(resp)


# for c in stub.GetChats(chat.GetChatsRequest(idusuario = "test12111@hotmail.com")):
#     print(c)
#for row in getC:
 #   print(row)
fecha = datetime.datetime.now()
x = datetime.datetime.now()
print(x.strftime("%X"))
print(x.strftime("%x"))
mensaje = chat.Mensaje(idmensaje = 0, mensaje = "hola", estado = "enviado", fecha = x.strftime("%x"), correoremitente = "test12111@hotmail.com",idmensajeprocedencia = 1, idchat = 10, hora = x.strftime("%X"))
#mr = stub.SendMessage(chat.MessageRequest(mensaje = mensaje))
#print(mr)
fecha = "2019-12-15"
hora = "02:36:42"

datei = datetime.datetime.strptime(fecha + " " + hora, '%Y-%m-%d %H:%M:%S')

mensajes = iter([chat.GetMessagesRequest(fecha = fecha, hora = hora, idchat = 10)])

for ms in stub.GetMesseges(mensajes):
    print("mmm....")
    print(ms)