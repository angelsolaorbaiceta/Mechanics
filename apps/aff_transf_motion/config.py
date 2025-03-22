import json

import pkg_resources as res


def read_config():
    config = res.resource_string(__name__, "config.json")
    return json.loads(config)
