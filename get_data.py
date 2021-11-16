import json

import requests

query_ids = {
    "ps5_games": "4cbf39e2-5749-4970-ba81-93a489e4570c",
    "ps4_games": "44d8bb20-653e-431e-8ad0-c0a365f68d2f",
    "ps_vr_games": "95239ca7-2dcf-43d9-8d4b-b7672ee9304a",
}
if __name__ == '__main__':
    r = requests.get(
        'https://web.np.playstation.com/api/graphql/v1//op?operationName=categoryGridRetrieve&variables={%22id%22:%2244d8bb20-653e-431e-8ad0-c0a365f68d2f%22,%22pageArgs%22:{%22size%22:500,%22offset%22:0},%22sortBy%22:null,%22filterBy%22:[],%22facetOptions%22:[]}&extensions={%22persistedQuery%22:{%22version%22:1,%22sha256Hash%22:%224ce7d410a4db2c8b635a48c1dcec375906ff63b19dadd87e073f8fd0c0481d35%22}}',
        headers={
            "X-PSN-Store-Locale-Override": "ru-RU"
        })
    with open("data/example_data.json", "w", encoding="utf-8") as f:
        json.dump(r.json(), f, indent=2, ensure_ascii=False)
