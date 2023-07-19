import argparse
import uuid

import grpc

import similarity_search_pb2
import similarity_search_pb2_grpc


def add_item(
    stub: similarity_search_pb2_grpc.SimilaritySearchServiceStub, description: str
) -> similarity_search_pb2.AddItemRequest:
    id_ = str(uuid.uuid4())
    request = similarity_search_pb2.AddItemRequest(id=id_, description=description)
    response = stub.AddItem(request)
    return response


def search_items(
    stub: similarity_search_pb2_grpc.SimilaritySearchServiceStub, query: str
) -> similarity_search_pb2.SearchItemsResponse:
    request = similarity_search_pb2.SearchItemsRequest(query=query)
    response = stub.SearchItems(request)
    return response


def get_search_result(
    stub: similarity_search_pb2_grpc.SimilaritySearchServiceStub, search_id: str
) -> similarity_search_pb2.GetSearchResultsResponse:
    request = similarity_search_pb2.GetSearchResultsRequest(search_id=search_id)
    response = stub.GetSearchResults(request)
    return response


def run(config):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = similarity_search_pb2_grpc.SimilaritySearchServiceStub(channel)

        description = "I enjoy coding"
        response = add_item(stub, description)
        assert type(response) == similarity_search_pb2.AddItemResponse
        assert response.status == 201
        assert response.message == "Created"

        description = "I'm not enjoy coding"
        response = add_item(stub, description)

        response = search_items(stub, "enjoy")
        search_id = response.search_id
        assert type(response) == similarity_search_pb2.SearchItemsResponse

        response = get_search_result(stub, search_id)
        assert type(response) == similarity_search_pb2.GetSearchResultsResponse
        assert len(response.results) >= 1
        assert response.results[0].description == "I enjoy coding"

        if config["add"] is not None:
            add_item(stub, config["add"])
        if config["query"] is not None:
            response = search_items(stub, config["query"])
            print(response.search_id)
        if config["search_id"] is not None:
            response = get_search_result(stub, config["search_id"])
            print(response)


import argparse

parser = argparse.ArgumentParser(
    description="CLI for client example",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument("-a", "--add", help="description to add")
parser.add_argument("-q", "--query", help="get id for query search", nargs="+")
parser.add_argument(
    "-s",
    "--search_id",
    help="get results for search_id",
)
args = parser.parse_args()
config = vars(args)


if __name__ == "__main__":
    run(config)
