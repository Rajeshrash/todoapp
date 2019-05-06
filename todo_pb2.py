# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='todo.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ntodo.proto\"\x0e\n\x0c\x45mptyRequest\" \n\x04Todo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04task\x18\x02 \x01(\t\"\x1f\n\x08TodoList\x12\x13\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x05.Todo\"\xc5\x01\n\x11OperationResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\t\x12\x33\n\x06status\x18\x02 \x01(\x0e\x32#.OperationResponse.OPERATION_STATUS\x12\x13\n\x04todo\x18\x03 \x01(\x0b\x32\x05.Todo\"W\n\x10OPERATION_STATUS\x12\x1c\n\x18UNKNOWN_OPERATION_STATUS\x10\x00\x12\x0b\n\x07\x43REATED\x10\x01\x12\x0b\n\x07\x44\x45LETED\x10\x02\x12\x0b\n\x07UPDATED\x10\x03\x32\xb6\x01\n\x0bTodoService\x12)\n\x0bGetAllTodos\x12\r.EmptyRequest\x1a\t.TodoList\"\x00\x12&\n\x07\x41\x64\x64Todo\x12\x05.Todo\x1a\x12.OperationResponse\"\x00\x12)\n\nUpdateTodo\x12\x05.Todo\x1a\x12.OperationResponse\"\x00\x12)\n\nDeleteTodo\x12\x05.Todo\x1a\x12.OperationResponse\"\x00\x62\x06proto3')
)



_OPERATIONRESPONSE_OPERATION_STATUS = _descriptor.EnumDescriptor(
  name='OPERATION_STATUS',
  full_name='OperationResponse.OPERATION_STATUS',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_OPERATION_STATUS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=208,
  serialized_end=295,
)
_sym_db.RegisterEnumDescriptor(_OPERATIONRESPONSE_OPERATION_STATUS)


_EMPTYREQUEST = _descriptor.Descriptor(
  name='EmptyRequest',
  full_name='EmptyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=28,
)


_TODO = _descriptor.Descriptor(
  name='Todo',
  full_name='Todo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Todo.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task', full_name='Todo.task', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=62,
)


_TODOLIST = _descriptor.Descriptor(
  name='TodoList',
  full_name='TodoList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='TodoList.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=95,
)


_OPERATIONRESPONSE = _descriptor.Descriptor(
  name='OperationResponse',
  full_name='OperationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='OperationResponse.error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='OperationResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='todo', full_name='OperationResponse.todo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OPERATIONRESPONSE_OPERATION_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=295,
)

_TODOLIST.fields_by_name['data'].message_type = _TODO
_OPERATIONRESPONSE.fields_by_name['status'].enum_type = _OPERATIONRESPONSE_OPERATION_STATUS
_OPERATIONRESPONSE.fields_by_name['todo'].message_type = _TODO
_OPERATIONRESPONSE_OPERATION_STATUS.containing_type = _OPERATIONRESPONSE
DESCRIPTOR.message_types_by_name['EmptyRequest'] = _EMPTYREQUEST
DESCRIPTOR.message_types_by_name['Todo'] = _TODO
DESCRIPTOR.message_types_by_name['TodoList'] = _TODOLIST
DESCRIPTOR.message_types_by_name['OperationResponse'] = _OPERATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmptyRequest = _reflection.GeneratedProtocolMessageType('EmptyRequest', (_message.Message,), dict(
  DESCRIPTOR = _EMPTYREQUEST,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:EmptyRequest)
  ))
_sym_db.RegisterMessage(EmptyRequest)

Todo = _reflection.GeneratedProtocolMessageType('Todo', (_message.Message,), dict(
  DESCRIPTOR = _TODO,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:Todo)
  ))
_sym_db.RegisterMessage(Todo)

TodoList = _reflection.GeneratedProtocolMessageType('TodoList', (_message.Message,), dict(
  DESCRIPTOR = _TODOLIST,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:TodoList)
  ))
_sym_db.RegisterMessage(TodoList)

OperationResponse = _reflection.GeneratedProtocolMessageType('OperationResponse', (_message.Message,), dict(
  DESCRIPTOR = _OPERATIONRESPONSE,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:OperationResponse)
  ))
_sym_db.RegisterMessage(OperationResponse)



_TODOSERVICE = _descriptor.ServiceDescriptor(
  name='TodoService',
  full_name='TodoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=298,
  serialized_end=480,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAllTodos',
    full_name='TodoService.GetAllTodos',
    index=0,
    containing_service=None,
    input_type=_EMPTYREQUEST,
    output_type=_TODOLIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddTodo',
    full_name='TodoService.AddTodo',
    index=1,
    containing_service=None,
    input_type=_TODO,
    output_type=_OPERATIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateTodo',
    full_name='TodoService.UpdateTodo',
    index=2,
    containing_service=None,
    input_type=_TODO,
    output_type=_OPERATIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteTodo',
    full_name='TodoService.DeleteTodo',
    index=3,
    containing_service=None,
    input_type=_TODO,
    output_type=_OPERATIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TODOSERVICE)

DESCRIPTOR.services_by_name['TodoService'] = _TODOSERVICE

# @@protoc_insertion_point(module_scope)
