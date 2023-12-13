"""
Similarity by Jaccard's coefficient, using neighbors of a node in graph as features.

Source: 'The Link-Prediction Problem for Social Networks' by D. Liben-Nowell & J.Kleinberg.
"""
import os
import sys
from algorithms.query.httprequest import get_neighbors_2
# Example usage
# subject_entity = "Q76"  # Example entity identifier for Barack Obama in Wikidata
# neighbors = get_neighbors(subject_entity)
# print(neighbors)


def jaccard_coeff(s, p, o, linkpred=True):
    """
    Returns Jaccard's coefficient score computed based on neighbors of s and o.

    Parameters:
    -----------
    G: rgraph
        Knowledge graph.
    s, p, o: int
        Subject, Predicate and Object identifiers.
    linkpred: bool
        Whether or not to perform link prediction.

    Returns:
    --------
    score: float
        A score in [0, 1].
    """
    # # link prediction: second condition is to avoid unnecessary introduction
    # # of a zero in the if clause
    # if linkpred and G[s, o, p] != 0:
    #     G[s, o, p] = 0
    _, s_nbrs = get_neighbors_2(s)
    _, o_nbrs = get_neighbors_2(o)
    if s_nbrs==0 or o_nbrs == 0:
        return "N/A"
    s_nbrs, o_nbrs = set(s_nbrs), set(o_nbrs)
    common = s_nbrs & o_nbrs
    allnbrs = s_nbrs | o_nbrs
    if float(len(allnbrs)) == 0:
        return "N/A"
    score = len(common) / float(len(allnbrs))
    return score
