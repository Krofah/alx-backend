#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Cache a key-value pair
        Args:
            key: The key to cache
            item: The value associated with the key
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value associated with a key
        Args:
            key: The key to retrieve the value for
        Returns:
            The value associated with the key, or None if the key doesn't exist
        """
        return self.cache_data.get(key, None)
