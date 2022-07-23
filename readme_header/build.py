"""
Build script for portfolio.
"""
from pathlib import Path

from utils import write_svg

write_svg('header-image', Path(__file__).parent.parent / 'images')
