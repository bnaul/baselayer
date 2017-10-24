#!/usr/bin/env python

import re
import os

from baselayer.app.env import load_env


def fill_config_file_values(
        template_paths=['baselayer/conf/nginx.conf.template',
                        'baselayer/conf/supervisor/supervisor.conf.template']):
    env, cfg = load_env()
    for template_path in template_paths:
        with open(template_path) as f:
            data = f.read()
        data_compiled = re.sub('\$\$\{\{([a-zA-Z_]+)?\}\}', '{\\1}',
                               data.replace('{', '{{').replace('}', '}}'))
        with open(os.path.splitext(template_path)[0], 'w') as f:
            f.write(data_compiled.format(**cfg['ports']))


if __name__ == '__main__':
    fill_config_file_values()
