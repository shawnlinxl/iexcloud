# Versioneer automatic version
from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

from iexcloud.config import get_token, set_token, set_test_token, set_mode
