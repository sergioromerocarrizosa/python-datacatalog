# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/datacatalog_v1/proto/table_spec.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/datacatalog_v1/proto/table_spec.proto",
    package="google.cloud.datacatalog.v1",
    syntax="proto3",
    serialized_options=b"\n\037com.google.cloud.datacatalog.v1P\001ZFgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1;datacatalog\370\001\001\252\002\033Google.Cloud.DataCatalog.V1\312\002\033Google\\Cloud\\DataCatalog\\V1\352\002\036Google::Cloud::DataCatalog::V1",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n2google/cloud/datacatalog_v1/proto/table_spec.proto\x12\x1bgoogle.cloud.datacatalog.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xe8\x01\n\x11\x42igQueryTableSpec\x12L\n\x11table_source_type\x18\x01 \x01(\x0e\x32,.google.cloud.datacatalog.v1.TableSourceTypeB\x03\xe0\x41\x03\x12:\n\tview_spec\x18\x02 \x01(\x0b\x32%.google.cloud.datacatalog.v1.ViewSpecH\x00\x12<\n\ntable_spec\x18\x03 \x01(\x0b\x32&.google.cloud.datacatalog.v1.TableSpecH\x00\x42\x0b\n\ttype_spec"#\n\x08ViewSpec\x12\x17\n\nview_query\x18\x01 \x01(\tB\x03\xe0\x41\x03"L\n\tTableSpec\x12?\n\rgrouped_entry\x18\x01 \x01(\tB(\xe0\x41\x03\xfa\x41"\n datacatalog.googleapis.com/Entry"\x89\x01\n\x17\x42igQueryDateShardedSpec\x12\x39\n\x07\x64\x61taset\x18\x01 \x01(\tB(\xe0\x41\x03\xfa\x41"\n datacatalog.googleapis.com/Entry\x12\x19\n\x0ctable_prefix\x18\x02 \x01(\tB\x03\xe0\x41\x03\x12\x18\n\x0bshard_count\x18\x03 \x01(\x03\x42\x03\xe0\x41\x03*[\n\x0fTableSourceType\x12!\n\x1dTABLE_SOURCE_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rBIGQUERY_VIEW\x10\x02\x12\x12\n\x0e\x42IGQUERY_TABLE\x10\x05\x42\xcb\x01\n\x1f\x63om.google.cloud.datacatalog.v1P\x01ZFgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1;datacatalog\xf8\x01\x01\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1b\x06proto3',
    dependencies=[
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
    ],
)

_TABLESOURCETYPE = _descriptor.EnumDescriptor(
    name="TableSourceType",
    full_name="google.cloud.datacatalog.v1.TableSourceType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="TABLE_SOURCE_TYPE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="BIGQUERY_VIEW",
            index=1,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="BIGQUERY_TABLE",
            index=2,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=633,
    serialized_end=724,
)
_sym_db.RegisterEnumDescriptor(_TABLESOURCETYPE)

TableSourceType = enum_type_wrapper.EnumTypeWrapper(_TABLESOURCETYPE)
TABLE_SOURCE_TYPE_UNSPECIFIED = 0
BIGQUERY_VIEW = 2
BIGQUERY_TABLE = 5


_BIGQUERYTABLESPEC = _descriptor.Descriptor(
    name="BigQueryTableSpec",
    full_name="google.cloud.datacatalog.v1.BigQueryTableSpec",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="table_source_type",
            full_name="google.cloud.datacatalog.v1.BigQueryTableSpec.table_source_type",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\003",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="view_spec",
            full_name="google.cloud.datacatalog.v1.BigQueryTableSpec.view_spec",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="table_spec",
            full_name="google.cloud.datacatalog.v1.BigQueryTableSpec.table_spec",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="type_spec",
            full_name="google.cloud.datacatalog.v1.BigQueryTableSpec.type_spec",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        )
    ],
    serialized_start=144,
    serialized_end=376,
)


_VIEWSPEC = _descriptor.Descriptor(
    name="ViewSpec",
    full_name="google.cloud.datacatalog.v1.ViewSpec",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="view_query",
            full_name="google.cloud.datacatalog.v1.ViewSpec.view_query",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\003",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=378,
    serialized_end=413,
)


_TABLESPEC = _descriptor.Descriptor(
    name="TableSpec",
    full_name="google.cloud.datacatalog.v1.TableSpec",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="grouped_entry",
            full_name="google.cloud.datacatalog.v1.TableSpec.grouped_entry",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\340A\003\372A"\n datacatalog.googleapis.com/Entry',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=415,
    serialized_end=491,
)


_BIGQUERYDATESHARDEDSPEC = _descriptor.Descriptor(
    name="BigQueryDateShardedSpec",
    full_name="google.cloud.datacatalog.v1.BigQueryDateShardedSpec",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="dataset",
            full_name="google.cloud.datacatalog.v1.BigQueryDateShardedSpec.dataset",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\340A\003\372A"\n datacatalog.googleapis.com/Entry',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="table_prefix",
            full_name="google.cloud.datacatalog.v1.BigQueryDateShardedSpec.table_prefix",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\003",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="shard_count",
            full_name="google.cloud.datacatalog.v1.BigQueryDateShardedSpec.shard_count",
            index=2,
            number=3,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\003",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=494,
    serialized_end=631,
)

_BIGQUERYTABLESPEC.fields_by_name["table_source_type"].enum_type = _TABLESOURCETYPE
_BIGQUERYTABLESPEC.fields_by_name["view_spec"].message_type = _VIEWSPEC
_BIGQUERYTABLESPEC.fields_by_name["table_spec"].message_type = _TABLESPEC
_BIGQUERYTABLESPEC.oneofs_by_name["type_spec"].fields.append(
    _BIGQUERYTABLESPEC.fields_by_name["view_spec"]
)
_BIGQUERYTABLESPEC.fields_by_name[
    "view_spec"
].containing_oneof = _BIGQUERYTABLESPEC.oneofs_by_name["type_spec"]
_BIGQUERYTABLESPEC.oneofs_by_name["type_spec"].fields.append(
    _BIGQUERYTABLESPEC.fields_by_name["table_spec"]
)
_BIGQUERYTABLESPEC.fields_by_name[
    "table_spec"
].containing_oneof = _BIGQUERYTABLESPEC.oneofs_by_name["type_spec"]
DESCRIPTOR.message_types_by_name["BigQueryTableSpec"] = _BIGQUERYTABLESPEC
DESCRIPTOR.message_types_by_name["ViewSpec"] = _VIEWSPEC
DESCRIPTOR.message_types_by_name["TableSpec"] = _TABLESPEC
DESCRIPTOR.message_types_by_name["BigQueryDateShardedSpec"] = _BIGQUERYDATESHARDEDSPEC
DESCRIPTOR.enum_types_by_name["TableSourceType"] = _TABLESOURCETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BigQueryTableSpec = _reflection.GeneratedProtocolMessageType(
    "BigQueryTableSpec",
    (_message.Message,),
    {
        "DESCRIPTOR": _BIGQUERYTABLESPEC,
        "__module__": "google.cloud.datacatalog_v1.proto.table_spec_pb2",
        "__doc__": """Describes a BigQuery table.
  
  Attributes:
      table_source_type:
          Output only. The table source type.
      type_spec:
          Output only.
      view_spec:
          Table view specification. This field should only be populated
          if ``table_source_type`` is ``BIGQUERY_VIEW``.
      table_spec:
          Spec of a BigQuery table. This field should only be populated
          if ``table_source_type`` is ``BIGQUERY_TABLE``.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1.BigQueryTableSpec)
    },
)
_sym_db.RegisterMessage(BigQueryTableSpec)

ViewSpec = _reflection.GeneratedProtocolMessageType(
    "ViewSpec",
    (_message.Message,),
    {
        "DESCRIPTOR": _VIEWSPEC,
        "__module__": "google.cloud.datacatalog_v1.proto.table_spec_pb2",
        "__doc__": """Table view specification.
  
  Attributes:
      view_query:
          Output only. The query that defines the table view.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1.ViewSpec)
    },
)
_sym_db.RegisterMessage(ViewSpec)

TableSpec = _reflection.GeneratedProtocolMessageType(
    "TableSpec",
    (_message.Message,),
    {
        "DESCRIPTOR": _TABLESPEC,
        "__module__": "google.cloud.datacatalog_v1.proto.table_spec_pb2",
        "__doc__": """Normal BigQuery table spec.
  
  Attributes:
      grouped_entry:
          Output only. If the table is a dated shard, i.e., with name
          pattern ``[prefix]YYYYMMDD``, ``grouped_entry`` is the Data
          Catalog resource name of the date sharded grouped entry, for
          example, ``projects/{project_id}/locations/{location}/entrygro
          ups/{entry_group_id}/entries/{entry_id}``. Otherwise,
          ``grouped_entry`` is empty.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1.TableSpec)
    },
)
_sym_db.RegisterMessage(TableSpec)

BigQueryDateShardedSpec = _reflection.GeneratedProtocolMessageType(
    "BigQueryDateShardedSpec",
    (_message.Message,),
    {
        "DESCRIPTOR": _BIGQUERYDATESHARDEDSPEC,
        "__module__": "google.cloud.datacatalog_v1.proto.table_spec_pb2",
        "__doc__": """Spec for a group of BigQuery tables with name pattern
  ``[prefix]YYYYMMDD``. Context:
  https://cloud.google.com/bigquery/docs/partitioned-
  tables#partitioning_versus_sharding
  
  Attributes:
      dataset:
          Output only. The Data Catalog resource name of the dataset
          entry the current table belongs to, for example, ``projects/{p
          roject_id}/locations/{location}/entrygroups/{entry_group_id}/e
          ntries/{entry_id}``.
      table_prefix:
          Output only. The table name prefix of the shards. The name of
          any given shard is ``[table_prefix]YYYYMMDD``, for example,
          for shard ``MyTable20180101``, the ``table_prefix`` is
          ``MyTable``.
      shard_count:
          Output only. Total number of shards.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1.BigQueryDateShardedSpec)
    },
)
_sym_db.RegisterMessage(BigQueryDateShardedSpec)


DESCRIPTOR._options = None
_BIGQUERYTABLESPEC.fields_by_name["table_source_type"]._options = None
_VIEWSPEC.fields_by_name["view_query"]._options = None
_TABLESPEC.fields_by_name["grouped_entry"]._options = None
_BIGQUERYDATESHARDEDSPEC.fields_by_name["dataset"]._options = None
_BIGQUERYDATESHARDEDSPEC.fields_by_name["table_prefix"]._options = None
_BIGQUERYDATESHARDEDSPEC.fields_by_name["shard_count"]._options = None
# @@protoc_insertion_point(module_scope)
