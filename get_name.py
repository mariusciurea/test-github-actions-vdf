"""dummy function - github actions tutorial"""
import os


def get_my_name(var) -> str or False:
    """Get name from environment variables"""
    try:
        return os.environ[var]
    except KeyError:
        return False


print(get_my_name('USERNAME'))