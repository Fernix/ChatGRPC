import grpc;
import chat_pb2 as chat
import chat_pb2_grpc as chat_grpc
from concurrent import futures
import peewee
database = peewee.MySQLDatabase("instawhat", host= "localhost", port = 3306, user = "root", password = "IriNando2403.")

class Chat(peewee.Model):
    idchat = peewee.AutoField(primary_key = True)
    nombre = peewee.CharField()
    idprocedencia = peewee.IntegerField()

    class Meta:
        database = database
        db_table = "chat"

class Usuario(peewee.Model):
    username = peewee.CharField()
    correo = peewee.CharField(primary_key = True)

    class Meta:
        database = database
        db_table = "usuario"

class UsuarioEnChat(peewee.Model):
    correo = peewee.CharField()
    idchat = peewee.IntegerField()
    idusuariochat = peewee.AutoField(primary_key = True)

    class Meta:
        database = database
        db_table = "usuario_en_chat"


class ChatService(chat_grpc.ChatAdminServicer):
    
    def __init__(self):
        super().__init__()

    def CreateChat(self, request, context):
        requestChat = request.chat
        newChat = Chat.create(nombre = requestChat.nombre, idprocedencia = requestChat.idchat)
        newChat.save()
        for usuario in request.usuariosenchat:
            query = Usuario.select().where( Usuario.correo == usuario.usuario.correo)
            if not query.exists():
                us = Usuario.create(correo = usuario.usuario.correo, username = usuario.usuario.username)
                us.save()
            else:
                print("existe")
            query2 = UsuarioEnChat.select()
            uec = UsuarioEnChat.create(correo = usuario.usuario.correo, idchat = newChat.idchat)
            uec.save()
        response = chat.CreateChatResponse(idchatServer = newChat.idchat)
        return response

    def GetChats(self, request, context):
        req = request.idusuario
        responseQuery = UsuarioEnChat.select().where(UsuarioEnChat.correo == req)
        #itera los usuariosEnChat
        for row in responseQuery:
            chatR = Chat.select().where(Chat.idchat == row.idchat)
            #itera los chats
            for rowChat in chatR:
                usuarios = []
                for user in UsuarioEnChat.select().where(UsuarioEnChat.idchat == rowChat.idchat):
                    usuarios.append(user.correo)
                response = chat.GetChatsResponse(chat = chat.Chat(idchat = rowChat.idchat, nombre = rowChat.nombre, idprocedencia = rowChat.idprocedencia), usuarios = usuarios)
                #regresa cada uno de los chats
                yield response
 
    def GetMesseges(self, request_iterator, context):
        for request in request_iterator:
            self.mensajes = request
            response = chat.GetChatsResponse
            yield response

    def SendMessage(self, request, context):
       return


server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))

chat_grpc.add_ChatAdminServicer_to_server(ChatService(),server)

server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()

