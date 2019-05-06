import grpc

import todo_pb2_grpc
import todo_pb2

channel = grpc.insecure_channel('localhost:50051')

stub = todo_pb2_grpc.TodoServiceStub(channel)

todo_request = todo_pb2.Todo(task="Task 1")
todo_response = stub.AddTodo(todo_request)
print(todo_response)
todo_request = todo_pb2.Todo(task="Task 2")
todo_response = stub.AddTodo(todo_request)
print(todo_response)
todo_request = todo_pb2.Todo(task="Task 3")
todo_response = stub.AddTodo(todo_request)
print(todo_response)

print("Printing all Todo's\n")
todos = stub.GetAllTodos(todo_pb2.EmptyRequest())
print(todos)

print("====================================================================================")
print("Deleting Todo")
todo_request = todo_pb2.Todo(id=0)
todo_response = stub.DeleteTodo(todo_request)
print(todo_response)

print("====================================================================================")
print("Printing all Todo's")
todos = stub.GetAllTodos(todo_pb2.EmptyRequest())
print(todos)

print("====================================================================================")
print("Updating Todo")
todo_request = todo_pb2.Todo(id=3, task="Updated Task")
todo_response = stub.UpdateTodo(todo_request)
print(todo_response)

print("Printing all Todo's\n")
todos = stub.GetAllTodos(todo_pb2.EmptyRequest())
print(todos)




