# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import chat_pb2 as chat__pb2


class ChatAdminStub(object):
  """Comando para generar clases
  py -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. .\chat.proto

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SendMessage = channel.unary_unary(
        '/ChatAdmin/SendMessage',
        request_serializer=chat__pb2.MessageRequest.SerializeToString,
        response_deserializer=chat__pb2.SendMesageResponse.FromString,
        )
    self.GetMesseges = channel.stream_stream(
        '/ChatAdmin/GetMesseges',
        request_serializer=chat__pb2.GetMessagesRequest.SerializeToString,
        response_deserializer=chat__pb2.MessagesResponse.FromString,
        )
    self.CreateChat = channel.unary_unary(
        '/ChatAdmin/CreateChat',
        request_serializer=chat__pb2.CreateChatRequest.SerializeToString,
        response_deserializer=chat__pb2.CreateChatResponse.FromString,
        )
    self.GetChats = channel.unary_stream(
        '/ChatAdmin/GetChats',
        request_serializer=chat__pb2.GetChatsRequest.SerializeToString,
        response_deserializer=chat__pb2.GetChatsResponse.FromString,
        )
    self.UpdateMensage = channel.unary_unary(
        '/ChatAdmin/UpdateMensage',
        request_serializer=chat__pb2.MessageRequest.SerializeToString,
        response_deserializer=chat__pb2.MessagesResponse.FromString,
        )
    self.DeleteMesage = channel.unary_unary(
        '/ChatAdmin/DeleteMesage',
        request_serializer=chat__pb2.MessageRequest.SerializeToString,
        response_deserializer=chat__pb2.MessagesResponse.FromString,
        )


class ChatAdminServicer(object):
  """Comando para generar clases
  py -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. .\chat.proto

  """

  def SendMessage(self, request, context):
    """ENvia multiples mensjes al servidor
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMesseges(self, request_iterator, context):
    """Recupera múltipes mensajes del servidor _a partir de una fecha_
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateChat(self, request, context):
    """crea un chat
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetChats(self, request, context):
    """recupera los chats en los que está incluido un usuairo
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateMensage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteMesage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChatAdminServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SendMessage': grpc.unary_unary_rpc_method_handler(
          servicer.SendMessage,
          request_deserializer=chat__pb2.MessageRequest.FromString,
          response_serializer=chat__pb2.SendMesageResponse.SerializeToString,
      ),
      'GetMesseges': grpc.stream_stream_rpc_method_handler(
          servicer.GetMesseges,
          request_deserializer=chat__pb2.GetMessagesRequest.FromString,
          response_serializer=chat__pb2.MessagesResponse.SerializeToString,
      ),
      'CreateChat': grpc.unary_unary_rpc_method_handler(
          servicer.CreateChat,
          request_deserializer=chat__pb2.CreateChatRequest.FromString,
          response_serializer=chat__pb2.CreateChatResponse.SerializeToString,
      ),
      'GetChats': grpc.unary_stream_rpc_method_handler(
          servicer.GetChats,
          request_deserializer=chat__pb2.GetChatsRequest.FromString,
          response_serializer=chat__pb2.GetChatsResponse.SerializeToString,
      ),
      'UpdateMensage': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateMensage,
          request_deserializer=chat__pb2.MessageRequest.FromString,
          response_serializer=chat__pb2.MessagesResponse.SerializeToString,
      ),
      'DeleteMesage': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteMesage,
          request_deserializer=chat__pb2.MessageRequest.FromString,
          response_serializer=chat__pb2.MessagesResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ChatAdmin', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
