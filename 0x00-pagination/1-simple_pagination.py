import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Check for index range of items in pages. """
    total = page_size * page
    return total - page_size, total


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "0x00-pagination/Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.dataset()

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
        assert isinstance(page_size, int) and isinstance(page, int)
        assert page_size > 0 and page > 0

        if self.__dataset:
            start, stop = index_range(page, page_size)
            if stop > len(self.__dataset):
                return []
            return self.__dataset[start:stop]
        return []
