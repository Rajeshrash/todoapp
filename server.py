import grpc
from concurrent import futures
import time

import todo_pb2_grpc
import todo_pb2

class TodoServicer(todo_pb2_grpc.TodoServiceServicer):

    todoList = []
    def AddTodo(self, request, context):
        response = todo_pb2.OperationResponse()
        if len(self.todoList)>0:
            self.todoList.append({"id":self.todoList[len(self.todoList)-1]["id"]+1, "task":request.task})
        else:
            self.todoList.append({"id":len(self.todoList)+1, "task":request.task})
        response.status = todo_pb2.OperationResponse.CREATED
        response.todo.id = len(self.todoList)
        response.todo.task = request.task
        return response

    def DeleteTodo(self, request, context):
        response = todo_pb2.OperationResponse()
        if(len(self.todoList)>=request.id):
            response.todo.id = self.todoList[request.id]['id']
            response.todo.task = self.todoList[request.id]['task']
            self.todoList.remove(self.todoList[request.id])
            response.status = todo_pb2.OperationResponse.DELETED
        else:
            response.error = "Task with id doesn't exist" 
        return response
    
    def GetAllTodos(self, request, context):
        response = todo_pb2.TodoList()
        todos =[]
        for todo in self.todoList:
            todoObject = todo_pb2.Todo()
            todoObject.id = todo["id"]
            todoObject.task = todo["task"]
            todos.append(todoObject)
        response.data.extend(todos)
        return response

    def UpdateTodo(self, request, context):
        response = todo_pb2.OperationResponse()
        for todo in self.todoList:
            if todo["id"] == request.id:
                todo["task"] = request.task
                response.todo.id = request.id
                response.todo.task = request.task
                response.status = todo_pb2.OperationResponse.UPDATED 
                break
            else:
                response.error = "Task with id doesn't exist" 
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

todo_pb2_grpc.add_TodoServiceServicer_to_server(TodoServicer(),server)

print("server starting. Listening on port 50051")
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)



