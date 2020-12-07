import numpy as np


def getVirtualEdgesToJamFactors(edgeKernel, numberOfEdge, numberOfJamFactor):
    IFREdgesToJamFactors = np.array([((0.8, 0.1), (0.6, 0.1), (0.2, 0.8), (0.6, 0.1)),
                                     ((0.0, 0.8), (0.4, 0.4), (0.6, 0.1), (0.1, 0.7)),
                                     ((0.8, 0.1), (0.8, 0.1), (0.0, 0.6), (0.2, 0.7)),
                                     ((0.6, 0.1), (0.5, 0.4), (0.3, 0.4), (0.7, 0.2)),
                                     ((0.8, 0.1), (0.8, 0.1), (0.0, 0.6), (0.2, 0.7)),
                                     ((0.0, 0.8), (0.4, 0.4), (0.6, 0.1), (0.1, 0.7)),
                                     ((0.1, 0.6), (0.5, 0.4), (0.4, 0.1), (0.5, 0.7))],
                                    dtype=edgeKernel)
    return IFREdgesToJamFactors
