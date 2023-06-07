from __future__ import print_function

import grpc
import sys
sys.path.append('/home/ajay/My_Projects/python/m_s_django/src/user/user')

import users_pb2
import users_pb2_grpc



def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = users_pb2_grpc.UsersStub(channel)
        response = stub.GetUsers(users_pb2.GetUsersRequest())
    print(response)


if __name__ == '__main__':
    run()
