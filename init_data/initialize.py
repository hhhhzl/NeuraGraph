import pandas as pd
import os
from os.path import dirname, abspath
import json
from GraphDbAPIs.HugeGraphAPIs import hugegraphClient
from configs.hugegraph import (
    HOST,
    PORT,
    GRAPH_NAME
)


class init_graph:
    def __init__(self, graph_connector):
        self.graph_db = graph_connector(
            host=f"{HOST}",
            port=PORT,
            graph_name=f"{GRAPH_NAME}"
        )

    def get_file_path(self, type):
        # function to get the file or json
        path_file = os.path.join(dirname(abspath(__file__)), 'json', f'init_{type}.json')
        print(path_file)
        if not os.path.isfile(path_file):
            return
        return path_file

    def init_property_key(self):
        path_file = self.get_file_path('propertykey')
        with open(path_file, encoding="utf-8") as f:
            for data in json.load(f):
                res = self.graph_db.create_property_key(data['name'], data['data_type'], data['cardinality'])
                print(res.status_code)
                if res.status_code == 201:
                    print('success!')

    def init_edge(self):
        path_file = self.get_file_path('edge')
        with open(path_file, encoding="utf-8") as f:
            for data in json.load(f):
                self.graph_db.create_vertex_label(data)

    def init_vertex(self):
        path_file = self.get_file_path('vertex')
        with open(path_file, encoding="utf-8") as f:
            for data in json.load(f):
                res = self.graph_db.create_edge_label(data)
                if res.status_code == 201:
                    print('success!')

    def run(self):
        self.init_property_key()
        self.init_vertex()
        self.init_edge()


class build_graph:
    def build_vertex(self):
        pass

    def build_relations(self):
        pass

    def run(self):
        self.build_vertex()
        self.build_relations()


if __name__ == "__main__":
    Init = init_graph(hugegraphClient.HugeGraphClient)
    Init.run()
