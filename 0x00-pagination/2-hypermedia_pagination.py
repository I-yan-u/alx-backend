#!/usr/bin/env python3
"""
Simple implementation of pagination
"""


import csv
import math
from typing import List, Tuple, Dict, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Check for index range of items in pages. """
    total = page_size * page
    return total - page_size, total


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get page by given page and page size. """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        data = self.dataset()

        start, stop = index_range(page, page_size)
        return [] if (start >= len(data) or
                      stop >= len(data)) else data[start:stop]

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, Union[str, List]]:
        """
        A hypermedia pagination method.
        Return HATEOAS format of get_page.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        data = self.dataset()

        data_store = {}
        got_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(data) / page_size)

        data_store['page_size'] = 0
        data_store['page'] = page
        data_store['data'] = []
        data_store['next_page'] = page + 1 if page + 1 < total_pages else None
        data_store['prev_page'] = page - 1 if page > 1 else None
        data_store['total_pages'] = total_pages
        if got_page == []:
            return data_store
        data_store['page_size'] = page_size
        data_store['data'] = got_page
        return data_store
