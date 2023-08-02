from .cmaps import Cmaps
from .utils import concat, show_cmaps_all, show_cmaps_collection
import sys

sys.modules[__name__] = Cmaps()
