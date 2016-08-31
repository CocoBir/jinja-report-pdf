# -*- coding: utf-8 -*-

"""

    use jinja2 to create html stream
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    load template from template dir and render to 
    html stream

    :Created: 2016/8/31
    :Copyright: (c) 2016<smileboywtu@gmail.com>

"""


import yaml
import logging
from pprint import pprint
from jinja2 import (
        Environment,
        FileSystemLoader,
)

# get the logger by module name
logger = logging.getLogger(__file__)

# load the config file
config = {}
with open("config.yaml", "r") as fp:
    config = yaml.safe_load(fp)


# create environment
env = Environment(loader=FileSystemLoader(config.get("TEMPLATE_DIRS", "./")))


# test the template
def main():
    """run main for test
    """
    logger.info(config)
    pprint(config)

    wvss_pattern = env.get_template("wvss/report.html")
    pprint(wvss_pattern.render())


if __name__ == "__main__":
    main()


