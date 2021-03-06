# Copyright (c) 2007 Enough Project.
# See LICENSE for details.

from lib.observer import Observable

class List(object):
    def __init__(self, *args, **kw):
        self.obs_list = Observable()
        self._items = list(*args, **kw)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self._items)

    def insert(self, index, item):
        self._items.insert(index, item)
        self.obs_list.notify.insert(index, item)
    
    def pop(self, index=-1):
        value = self._items.pop(index)
        self.obs_list.notify.pop(index, value)

    def remove(self, item):
        self.pop(self.index(item))

    def append(self, item):
        self.insert(len(self), item)

    def __setitem__(self, index, new_value):
        old_value = self._items[index]
        self._items[index] = new_value
        self.obs_list.notify.replace(index, old_value, new_value)

    def __delitem__(self, index):
        self.pop(index)

from lib.proxyclass import proxy_class
List = proxy_class(List, '_items', methods=[
    '__getitem__',
    '__len__',
    '__iter__',
    'index',
])
