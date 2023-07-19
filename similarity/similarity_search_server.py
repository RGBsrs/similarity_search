from concurrent import futures
from typing import List
import uuid

import grpc
from sqlalchemy.orm import sessionmaker
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


from models import create_all, drop_all, engine, Document, Search
import similarity_search_pb2
import similarity_search_pb2_grpc

THRESHOLD = 0.6


class SimilaritySearchServicer(
    similarity_search_pb2_grpc.SimilaritySearchServiceServicer
):
    def __init__(self):
        self.engine = engine
        self.Session = sessionmaker(bind=engine)

    def AddItem(self, request, context):
        id_ = request.id
        description = request.description
        session = self.Session()
        try:
            document = Document(id=id_, description=description)
            session.add(document)
            session.commit()
            status = 201
            message = "Created"
        except Exception as e:
            status = 500
            message = str(e)
        finally:
            session.close()
        item = similarity_search_pb2.AddItemResponse(status=status, message=message)
        return item

    def SearchItems(self, request, context):
        session = self.Session()
        search_id = str(uuid.uuid4())
        query = request.query
        documents_data = session.query(Document.id, Document.description).all()
        documents = [document[1] for document in documents_data]
        if documents:
            # Cosine similarity method
            vectorizer = TfidfVectorizer()
            tfidf_matrix = vectorizer.fit_transform(documents + [query])
            query_vector = tfidf_matrix[-1]
            similarities = cosine_similarity(query_vector, tfidf_matrix[:-1])

            for similarity, record in zip(similarities[0], documents_data):
                if similarity > THRESHOLD:
                    search_result = Search(search_id=search_id, document_id=record[0])
                    session.add(search_result)
            session.commit()
        search_item = similarity_search_pb2.SearchItemsResponse(search_id=search_id)
        session.close()
        return search_item

    def GetSearchResults(self, request, context):
        session = self.Session()
        search_id = request.search_id
        document_ids = (
            session.query(Search.document_id).where(Search.search_id == search_id).all()
        )
        document_ids = [record[0] for record in document_ids]
        documents = session.query(Document).filter(Document.id.in_(document_ids))
        session.close()
        response = similarity_search_pb2.GetSearchResultsResponse(results=[])
        for document in documents:
            response.results.append(
                similarity_search_pb2.SearchResult(
                    id=document.id, description=document.description
                )
            )
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    similarity_search_pb2_grpc.add_SimilaritySearchServiceServicer_to_server(
        SimilaritySearchServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    drop_all()
    create_all()
    serve()
