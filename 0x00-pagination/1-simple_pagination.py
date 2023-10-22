#!/usr/bin/env python3
"""
Defines class Server that paginates a database of popular baby names
"""
import csv
import math
from typing import List, Tuple


def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
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
    data_length = len(dataset)
    try:
        index = index_range(page, page_size)
        return dataset[index[0]:index[1]]
    except IndexError:
        return []
         