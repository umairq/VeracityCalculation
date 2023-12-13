# import np

from algorithms.query.httpquery import get_neighbors


def adamic_adar(s, p, o, linkpred=True):
    """
    Returns Adamic/Adar (AA) score computed based on common neighbors of s and o.

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
        A score >= 0.
    """
    _, s_nbrs = get_neighbors(s)
    _, o_nbrs = get_neighbors(o)
    s_nbrs, o_nbrs = set(s_nbrs), set(o_nbrs)
    common = s_nbrs & o_nbrs
    # TODO query these in deg vectors
    # z = np.asarray([G.indeg_vec[node] for node in common])
    # score = np.sum(1. / np.log(z))
    # return score
