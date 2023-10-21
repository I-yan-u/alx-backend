#!/usr/bin/env python3
"""
index_range
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Check for index range of items in pages. """
    total = page_size * page
    return total - page_size, total
