import base64
import io
from os.path import join

import jinja2
import yaml
from PIL import Image


def render_template(path: str, data: dict) -> str:
    """
    Renders a template with given data.

    Parameters
    ----------
    path:
        Path to the template
    data:
        The provided data for rendering

    Returns
    -------
    template:
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
    name:
        Name of data

    Returns
    -------
    data:
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
    name:
        Name of the HTML

    path:
        Path to write HTML to
    """
    data = read_data(name)
    for image_name, image_data in data.items():
        image = Image.open(join('header', 'images', image_data['filename']))
        width = image_data['thumbnail_width']
        image.thumbnail((width, width*image.height/image.width))
        buffer = io.BytesIO()
        image.save(buffer, image.format)
        encoded = base64.b64encode(buffer.getvalue()).decode('ascii')
        image_data['data'] = f'data:image/png;base64,{encoded}'

    svg = render_template(join('header', 'templates', f'{name}.svg'), data)
    with open(join(path, f'{name}.svg'), 'w+') as f:
        f.write(svg)
