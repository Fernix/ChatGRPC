import grpc;
import chat_pb2 as chat
import chat_pb2_grpc as chat_grpc
from concurrent import futures
import MiddleWare.Chat


class ChatService(chat_grpc.ChatAdminServicer):
    
    def __init__(self):
        super().__init__()

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

newChat = User.create(nombre = "prueba")
newChat.save()