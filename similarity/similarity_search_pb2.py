# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: similarity_search.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17similarity_search.proto\x12\x10similaritysearch\"1\n\x0e\x41\x64\x64ItemRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"2\n\x0f\x41\x64\x64ItemResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"#\n\x12SearchItemsRequest\x12\r\n\x05query\x18\x01 \x01(\t\"(\n\x13SearchItemsResponse\x12\x11\n\tsearch_id\x18\x01 \x01(\t\",\n\x17GetSearchResultsRequest\x12\x11\n\tsearch_id\x18\x01 \x01(\t\"K\n\x18GetSearchResultsResponse\x12/\n\x07results\x18\x01 \x03(\x0b\x32\x1e.similaritysearch.SearchResult\"/\n\x0cSearchResult\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t2\xb6\x02\n\x17SimilaritySearchService\x12P\n\x07\x41\x64\x64Item\x12 .similaritysearch.AddItemRequest\x1a!.similaritysearch.AddItemResponse\"\x00\x12\\\n\x0bSearchItems\x12$.similaritysearch.SearchItemsRequest\x1a%.similaritysearch.SearchItemsResponse\"\x00\x12k\n\x10GetSearchResults\x12).similaritysearch.GetSearchResultsRequest\x1a*.similaritysearch.GetSearchResultsResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'similarity_search_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ADDITEMREQUEST']._serialized_start=45
  _globals['_ADDITEMREQUEST']._serialized_end=94
  _globals['_ADDITEMRESPONSE']._serialized_start=96
  _globals['_ADDITEMRESPONSE']._serialized_end=146
  _globals['_SEARCHITEMSREQUEST']._serialized_start=148
  _globals['_SEARCHITEMSREQUEST']._serialized_end=183
  _globals['_SEARCHITEMSRESPONSE']._serialized_start=185
  _globals['_SEARCHITEMSRESPONSE']._serialized_end=225
  _globals['_GETSEARCHRESULTSREQUEST']._serialized_start=227
  _globals['_GETSEARCHRESULTSREQUEST']._serialized_end=271
  _globals['_GETSEARCHRESULTSRESPONSE']._serialized_start=273
  _globals['_GETSEARCHRESULTSRESPONSE']._serialized_end=348
  _globals['_SEARCHRESULT']._serialized_start=350
  _globals['_SEARCHRESULT']._serialized_end=397
  _globals['_SIMILARITYSEARCHSERVICE']._serialized_start=400
  _globals['_SIMILARITYSEARCHSERVICE']._serialized_end=710
# @@protoc_insertion_point(module_scope)
