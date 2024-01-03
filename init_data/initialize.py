import pandas as pd
import os
from os.path import dirname, abspath
import json
from NeuraGraphAPIs.HugeGraphAPIs import hugegraphClient
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
            counter = 0
            total = len(json.load(f))
            for data in json.load(f):
                res = self.graph_db.create_property_key(data['name'], data['data_type'], data['cardinality'])
                if res.status_code == 202:
                    print(f"Success import {data['name']}!")
                    counter += 1
            print(f"Success import {counter}/{total} of propertykey.")

    def init_edge(self):
        path_file = self.get_file_path('edge')
        with open(path_file, 'r') as f:
            counter = 0
            total = len(json.load(f))
            for data in json.load(f):
                self.graph_db.create_vertex_label(data)
                if res.status_code == 202:
                    print(f"Success import {data['name']}!")
                    counter += 1
            print(f"Success import {counter}/{total} of EdgeLabel.")

    def init_vertex(self):
        path_file = self.get_file_path('vertex')
        try:
            with open(path_file, encoding="utf-8") as f:
                data = json.load(f)
                counter = 0
                total = len(json.load(f))
                for data in json.load(f):
                    res = self.graph_db.create_edge_label(data)
                    if res.status_code == 202:
                        print(f"Success import {data['name']}!")
                        counter += 1
                print(f"Success import {counter}/{total} of VertexLabel.")
        except json.JSONDecodeError as e:
            print("JSONDecodeError: ", e)
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred: ", e)
            

    def run(self):
        # self.init_property_key()
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
