# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meter.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='meter.proto',
  package='data_app',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0bmeter.proto\x12\x08\x64\x61ta_app\x1a\x1fgoogle/protobuf/timestamp.proto\"\\\n\rSearchRequest\x12)\n\x05start\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05limit\x18\x02 \x01(\x05\x12\x11\n\tprecision\x18\x03 \x01(\t\"Z\n\x0eSearchResponse\x12(\n\x04time\x18\x01 \x03(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05usage\x18\x02 \x03(\x01\x12\x0f\n\x07message\x18\x03 \x01(\t2L\n\rSearchService\x12;\n\x06Search\x12\x17.data_app.SearchRequest\x1a\x18.data_app.SearchResponseb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_SEARCHREQUEST = _descriptor.Descriptor(
  name='SearchRequest',
  full_name='data_app.SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='data_app.SearchRequest.start', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='data_app.SearchRequest.limit', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='precision', full_name='data_app.SearchRequest.precision', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=58,
  serialized_end=150,
)


_SEARCHRESPONSE = _descriptor.Descriptor(
  name='SearchResponse',
  full_name='data_app.SearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='data_app.SearchResponse.time', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usage', full_name='data_app.SearchResponse.usage', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='data_app.SearchResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=152,
  serialized_end=242,
)

_SEARCHREQUEST.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SEARCHRESPONSE.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['SearchResponse'] = _SEARCHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREQUEST,
  '__module__' : 'meter_pb2'
  # @@protoc_insertion_point(class_scope:data_app.SearchRequest)
  })
_sym_db.RegisterMessage(SearchRequest)

SearchResponse = _reflection.GeneratedProtocolMessageType('SearchResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHRESPONSE,
  '__module__' : 'meter_pb2'
  # @@protoc_insertion_point(class_scope:data_app.SearchResponse)
  })
_sym_db.RegisterMessage(SearchResponse)



_SEARCHSERVICE = _descriptor.ServiceDescriptor(
  name='SearchService',
  full_name='data_app.SearchService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=244,
  serialized_end=320,
  methods=[
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='data_app.SearchService.Search',
    index=0,
    containing_service=None,
    input_type=_SEARCHREQUEST,
    output_type=_SEARCHRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SEARCHSERVICE)

DESCRIPTOR.services_by_name['SearchService'] = _SEARCHSERVICE

# @@protoc_insertion_point(module_scope)
