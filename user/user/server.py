from concurrent import futures

import grpc

import sys
sys.path.append('/home/ajay/My_Projects/python/m_s_django/src/user/user')

import users_pb2
import users_pb2_grpc


from user.models import User

class Users(users_pb2_grpc.UsersServicer):

    def GetUsers(self, request, context):
        u = list(User.objects.all()) 
        print("l18", u)
        response = users_pb2.GetUsersResponse(
            users=u
        )
        return response


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UsersServicer_to_server(Users(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()


