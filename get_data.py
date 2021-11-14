import requests

if __name__ == '__main__':
    r = requests.get(
        """https://web.np.playstation.com/api/graphql/v1//op?operationName=categoryGridRetrieve&variables={%22id%22:%2244d8bb20-653e-431e-8ad0-c0a365f68d2f%22,%22pageArgs%22:{%22size%22:500,%22offset%22:0},%22sortBy%22:null,%22filterBy%22:[],%22facetOptions%22:[]}&extensions={%22persistedQuery%22:{%22version%22:1,%22sha256Hash%22:%224ce7d410a4db2c8b635a48c1dcec375906ff63b19dadd87e073f8fd0c0481d35%22}}""",
        headers={
            "X-PSN-Store-Locale-Override": "ru-RU"
        })
    with open("data/example_data.json", "w") as f:
        f.write(r.text)
