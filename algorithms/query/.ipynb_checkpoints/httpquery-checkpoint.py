from SPARQLWrapper import SPARQLWrapper, JSON


def get_neighbors(subject):
    sparql = SPARQLWrapper("http://query.wikidata.org/sparql")

    # Define the SPARQL query to get neighbors of the subject
    # query = f"""
    # SELECT ?predicate ?object WHERE {{
    #   wd:{subject} ?predicate ?object.
    #
    # }}
    # """
    query = f"""
       SELECT ?predicate ?object WHERE {{
         {{
           wd:{subject} ?predicate ?object.
           FILTER ( STRSTARTS(str(?object), "http://www.wikidata.org/entity/Q"))
         }}
         UNION
         {{
           ?object ?predicate wd:{subject}.
             FILTER ( STRSTARTS(str(?object), "http://www.wikidata.org/entity/Q"))
         }}

       }}
       """

    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    try:
        # Execute the SPARQL query
        results = sparql.query().convert()
        neighbor_pred = []
        neighbor_obj = []

        for result in results["results"]["bindings"]:
            # Extract predicate and object from the query results
            predicate = result["predicate"]["value"].split("/")[-1]
            obj = result["object"]["value"].split("/")[-1]
            neighbor_pred.append((predicate))
            neighbor_obj.append(obj)

        return neighbor_pred, neighbor_obj

    except Exception as e:
        print("Error occurred:", str(e))
        return 0,0
