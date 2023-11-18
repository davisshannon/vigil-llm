"""Top-level package for Vigil"""

from importlib import metadata

from vigil.core.config import Config

from vigil.common import uuid4_str
from vigil.common import timestamp_str

from vigil.dispatch import Manager
from vigil.dispatch import Scanner

from vigil.schema import BaseScanner
from vigil.schema import ScanModel
from vigil.schema import VectorMatch
from vigil.schema import YaraMatch
from vigil.schema import ModelMatch
from vigil.schema import SimilarityMatch

from vigil.core.embedding import Embedder
from vigil.core.embedding import cosine_similarity

from vigil.core.vectordb import VectorDB

__version__ = "0.9.7-alpha"
__app__ = "vigil"
__description__ = "LLM security scanner"


__all__ = [
    'Config',
    'uuid4_str',
    'timestamp_str',
    'Manager',
    'Scanner',
    'BaseScanner',
    'ScanModel',
    'VectorMatch',
    'YaraMatch',
    'ModelMatch'
    'SimilarityMatch',
    'Embedder',
    'cosine_similarity',
    'VectorDB'
]
