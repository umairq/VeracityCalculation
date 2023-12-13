import requests


def get_neighbors_2(subject):

    # Endpoint URL for your SPARQL service
    wikidata_endpoint = 'http://localhost:9080/sparql'

    # SPARQL query you want to execute
    sparql_query = f"""
           SELECT ?predicate ?object WHERE {{
             {{
               <http://www.wikidata.org/entity/{subject}> ?predicate ?object.
             }}
             UNION
             {{
               ?object ?predicate <http://www.wikidata.org/entity/{subject}>.
             }}

           }}
           """
    print(sparql_query)

    # Constructing the request headers and body
    headers = {
        "Accept": "application/sparql-results+json"
    }

    # Sending the POST request
    response = requests.post(wikidata_endpoint, headers=headers, data={"query": sparql_query})

    # Checking the response status and content
    if response.status_code == 200:
        # Process the response content (results)
        results = response.json()
        neighbor_pred = []
        neighbor_obj = []
        # print(results)
        for result in results["results"]["bindings"]:
            # Extract predicate and object from the query results
            predicate = result["predicate"]["value"].split("/")[-1]
            obj = result["object"]["value"].split("/")[-1]
            neighbor_pred.append((predicate))
            neighbor_obj.append(obj)

        return neighbor_pred, neighbor_obj
        
    else:
        print(f"Failed with status code {response.status_code}: {response.text}")
        return 0,0
