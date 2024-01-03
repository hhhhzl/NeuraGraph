from NeuraGraphAPIs.HugeGraphAPIs import hugegraphClient
from configs.hugegraph import (
    HOST,
    PORT,
    GRAPH_NAME
)

class GraphBuilder:
    def __init__(self):
        graph_db_connector = hugegraphClient.HugeGraphClient(
            host=f"{HOST}",
            port=PORT,
            graph_name=f"{GRAPH_NAME}"
        )
        mysql_connector = None

    def import_to_graph_db(self):
        pass
