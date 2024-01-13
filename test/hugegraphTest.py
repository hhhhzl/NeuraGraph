from NeuraGraphAPIs.HugeGraphAPIs import hugegraphClient
from configs.hugegraph import (
    HOST,
    PORT,
    GRAPH_NAME
)

if __name__ == '__main__':
    hg = hugegraphClient.HugeGraphClient(
        host=f"{HOST}",
        port=PORT,
        graph_name=f"{GRAPH_NAME}"
    )
    print(hg.get_all_graphs().response)
    print(hg.get_version().response)