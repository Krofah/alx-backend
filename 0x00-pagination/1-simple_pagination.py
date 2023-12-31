#!/usr/bin/env python3
"""
Defines class Server that paginates a database of popular baby names
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes 2 integer arguments and returns a tuple of size two
    containing the start and end index corresponding to the range of
    indexes to return in a list for those pagination parameters
    Args:
        page (int): page number to return (pages are 1-indexed)
        page_size (int): number of items per page
    Return:
        tuple(start_index, end_index)
    """
    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Takes 2 integer arguments and returns requested page from the dataset
        Args:
            page (int): required page number. must be a positive integer
            page_size (int): number of records per page. must be a +ve integer
        Return:
            list of lists containing required data from the dataset
        """
        if not isinstance(page, int) or page <= 0:
            raise ValueError("Page number must be a positive integer")
        if not isinstance(page_size, int) or page_size <= 0:
            raise ValueError("Page size must be a positive integer")

        dataset = self.dataset()
        try:
            index = index_range(page, page_size)
            return dataset[index[0]:index[1]]
        except IndexError:
            return []
