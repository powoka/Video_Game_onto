# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 01:51:55 2021

@author: Chongyang
"""

import rdflib as rdf

graph = rdf.Graph()

# N'oublier pas changer le lien ici
result = graph.parse(r"Video_Game_ontology")

for sub, pred, obj in graph:
    if (sub, pred, obj) not in graph:
        raise Exception("Il n'y pas information dans ce .rdf")
print("Il y a {} déclaration dans ce .rdf".format(len(graph)))


#print(graph.serialize(format="turtle").decode("utf-8"))

query = graph.query("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX simon: <http://www.semanticweb.org/chongyang/ontologies/2021/1/untitled-ontology-9#>
SELECT ?game
 WHERE { ?game simon:isProducedBy simon:Ustwo }
 """)

query_1 = graph.query("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX simon: <http://www.semanticweb.org/chongyang/ontologies/2021/1/untitled-ontology-9#>
SELECT ?game_is_multiplayer
WHERE { ?game_is_multiplayer simon:isProducedBy simon:Activision}
 """)

query_2 = graph.query("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX simon: <http://www.semanticweb.org/chongyang/ontologies/2021/1/untitled-ontology-9#>
SELECT ?game_is_multiplayer
WHERE { ?game_is_multiplayer simon:isProducedBy simon:Blizzard}
 """)

print(query_2)
for result in query_2:
    print(result[0])
