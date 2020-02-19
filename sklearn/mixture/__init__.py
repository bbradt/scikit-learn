"""
The :mod:`sklearn.mixture` module implements mixture modeling algorithms.
"""

from ._gaussian_mixture import GaussianMixture
from ._bayesian_mixture import BayesianGaussianMixture
from ._ic_gaussian_mixture import ICGaussianMixture

__all__ = ['GaussianMixture',
           'ICGaussianMixture',
           'BayesianGaussianMixture']
