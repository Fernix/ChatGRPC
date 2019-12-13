import grpc;
import chat_pb2 as chat
import chat_pb2_grpc as chat_grpc
from concurrent import futures
import peewee
database = peewee.MySQLDatabase("instawhat", host= "localhost", port = 3306, user = "root", password = "IriNando2403.")

class Chat(peewee.Model):
    idchat = peewee.AutoField(primary_key = True)
    nombre = peewee.CharField()

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
    usuario_correo = peewee.CharField()
    chat_idchat = peewee.ForeignKeyField(Chat)
    idchatprocedencia = peewee.IntegerField()
    idusuariochat = peewee.AutoField(primary_key = True)

    class Meta:
        database = database
        db_table = "usuario_en_chat"


class ChatService(chat_grpc.ChatAdminServicer):
    
    def __init__(self):
        super().__init__()
        
    def CreateChat(self, request, context):

        requestChat = request.chat
        newChat = Chat.create(nombre = requestChat.nombre)
        newChat.save()
        print("paso 1")
        for usuario in request.usuariosenchat:
            query = Usuario.select().where( Usuario.correo == usuario.usuario)
            print(query)
            if query.count() == 0:
                us = Usuario.create(correo = usuario.usuario.correo, username = usuario.usuario.username)
                us.save()
            else:
                print("existe")
            print("paso 2")
            query2 = UsuarioEnChat.select()
            print(query2)
            uec = UsuarioEnChat.create(usuario_correo = usuario.usuario.correo, chat_idchat = newChat.idchat, idchatprocedencia = usuario.idchatprocedencia)
            uec.save()
            print("paso 3")
        response = chat.CreateChatResponse(idchatServer = newChat.idchat)
        return response
 
 
    def GetMesseges(self, request_iterator, context):
        for request in request_iterator:
            self.mensajes = request
            response = chat.GetChatsResponse
            yield response

    def SendMessage(self, request, context):
       return 
    
    def GetChats(self, request, context):
        return super().GetChats(request, context)
    



server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))

chat_grpc.add_ChatAdminServicer_to_server(ChatService(),server)

server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()

