import base64
from os.path import join

import jinja2
import yaml


def render_template(path: str, data: dict) -> str:
    """
    Renders a template with given data.

    Parameters
    ----------
    path: str
        Path to the template
    data:
        The provided data for rendering

    Returns
    -------
    template: str
        Rendered template
    """
    with open(path, 'r+') as f:
        template = f.read()
    template = jinja2.Template(source=template)
    return template.render(data=data)


def read_data(name: str) -> dict:
    """
    Reads the data from disk.

    Parameters
    ----------
    name: str
        Name of data

    Returns
    -------
    data: dict
        The data
    """
    with open(join('header', 'data', f'{name}.yaml'), 'r+') as f:
        data = yaml.safe_load(f)

    return data


def write_svg(name: str, path: str) -> None:
    """
    Write the SVG to disk.

    Parameters
    ----------
    name: str
        Name of the HTML

    path: str
        Path to write HTML to
    """
    data = read_data(name)
    for image, filename in data.items():
        encoded = base64.b64encode(open(join('header',
                                             'images',
                                             filename),
                                        'rb').read()).decode('ascii')
        data[image] = f'data:image/png;base64,{encoded}'

    svg = render_template(join('header', 'templates', f'{name}.svg'), data)
    with open(join(path, f'{name}.svg'), 'w+') as f:
        f.write(svg)
