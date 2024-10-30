#!/usr/bin/env python3
"""
    class LRUCache that inherits from BaseCaching
    and is a caching system:
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """the least recently used caching"""
    def __int__(self):
        """ the initialization overiding base"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """put an item in lru cache"""
        if key and item:
            if key in self.cache_data:

            self.cache_data[key] = item
            self.order.append(key)
