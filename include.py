# -*- coding: utf-8 -*-
"""
Plugin for Pelican to include external files
=================================================
Author: Toni Heittola (toni.heittola@gmail.com)

"""

import re
import copy
from past.builtins import long
import os.path
import shutil
import logging
from pelican import signals, contents

logger = logging.getLogger(__name__)
__version__ = '0.0.1'

# Default parameter values
include_default_settings = {}

include_settings = copy.deepcopy(include_default_settings)


def parse_tags(instance):
    global include_settings

    regex = r"{include::(.*?)}"
    from datetime import datetime
    if instance._content is not None:
        content = instance._content
        if '{include::' in content:
            matches = re.finditer(regex, content, re.MULTILINE | re.IGNORECASE)
            map = {}

            for match_id, match in enumerate(matches):
                filename = match.group(1)

                if os.path.exists(filename):
                    # Read file content
                    file = open(filename, mode='r')
                    file_content = file.read()
                    file.close()

                    map[match.group()] = file_content

            for map_item in map:
                content = content.replace(map_item, map[map_item])

            instance._content = content


def init_default_config(pelican):
    global include_default_settings


def register():
    signals.initialized.connect(init_default_config)
    signals.content_object_init.connect(parse_tags)
