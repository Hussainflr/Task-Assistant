import chromadb

class LongTermMemory:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection("memory")

    def add(self, text, metadata=None):
        self.collection.add(
            documents=[text],
            metadatas=[metadata or {}],
            ids=[str(hash(text))]
        )

    def query(self, query, k=3):
        results = self.collection.query(
            query_texts=[query],
            n_results=k
        )
        return results["documents"][0] if results["documents"] else []