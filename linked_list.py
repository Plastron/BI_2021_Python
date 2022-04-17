import unittest


class LinkedListItem:
    def __init__(self, value):
        self.value = value
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, next_item):
        self.__next = next_item

    def has_next(self):
        return self.__next is not None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0

    def __getitem__(self, index):
        current = self.__head
        for _ in range(index):
            if (current is None) or (current.has_next() is None):
                raise IndexError
            current = current.get_next()
        return current.value

    def __len__(self):
        return self.__len

    def __contains__(self, value):
        current = self.__head
        while current:
            if current.value == value:
                return True
            current = current.get_next()
        return False

    def add(self, value, position=None):
        if position == None:
            if self.__len == 0:
                inner_position = 0
            else:
                inner_position = self.__len - 1
        else:
            inner_position = position
        if inner_position < 0:
            inner_position = self.__len + inner_position
        if (inner_position < 0) or (inner_position > self.__len):
            raise IndexError
        else:
            if (inner_position == self.__len-1) or (self.__len == 0):
                self.__len += 1
                new_item = LinkedListItem(value)
                if not self.__head:
                    self.__head = new_item
                else:
                    self.__tail.set_next(new_item)
                self.__tail = new_item
            elif inner_position == 0:
                self.__len += 1
                new_item = LinkedListItem(value)
                new_item.set_next(self.__head)
                self.__head = new_item
            else:
                inner_linked_list = LinkedList()
                for i in range(self.__len):
                    if i != inner_position:
                        inner_linked_list.add(self[i])
                    else:
                        inner_linked_list.add(value)
                        inner_linked_list.add(self[i])
                self.__len += 1
                self.__head = inner_linked_list.__head
                self.__tail = inner_linked_list.__tail

    def extend(self, iterable, position=None):
        if position == None:
            if self.__len == 0:
                inner_position = 0
            else:
                inner_position = self.__len - 1
        else:
            inner_position = position
        if inner_position < 0:
            inner_position = self.__len + inner_position
        if (inner_position < 0) or (inner_position > self.__len):
            raise IndexError
        else:
            if (inner_position == self.__len-1) or (self.__len == 0):
                for i in iterable:
                    self.__len += 1
                    new_item = LinkedListItem(i)
                    if not self.__head:
                        self.__head = new_item
                    else:
                        self.__tail.set_next(new_item)
                    self.__tail = new_item
            elif inner_position == 0:
                for i in range(len(iterable)-1, -1, -1):
                    self.__len += 1
                    new_item = LinkedListItem(iterable[i])
                    new_item.set_next(self.__head)
                    self.__head = new_item
            else:
                inner_linked_list = LinkedList()
                for i in range(self.__len):
                    if i != inner_position:
                        inner_linked_list.add(self[i])
                    else:
                        for j in iterable:
                            inner_linked_list.add(j)
                        inner_linked_list.add(self[i])
                self.__len += len(iterable)
                self.__head = inner_linked_list.__head
                self.__tail = inner_linked_list.__tail

    def remove_last_occurence(self, value):
        if value in self:
            position = None
            for i in range(self.__len - 1, -1, -1):
                print(i)
                if self[i] == value:
                    position = i
                    break
            current = self.__head
            if position == 0:
                self.__head = current.get_next()
            else:
                for _ in range(position - 1):
                    current = current.get_next()
            if position == self.__len - 1:
                current.set_next(None)
            else:
                current.set_next(current.get_next().get_next())
            self.__len -= 1

    def pop(self, position=-1):
        inner_position = position
        outer_position = None
        if inner_position < 0:
            inner_position = self.__len + inner_position
        if (inner_position < 0) or (inner_position > self.__len):
            raise IndexError
        else:
            current = self.__head
            if inner_position == 0:
                outer_position = self.__head
                self.__head = current.get_next()
            else:
                for _ in range(inner_position - 1):
                    current = current.get_next()
                if inner_position == self.__len - 1:
                    outer_position = current.get_next()
                    current.set_next(None)
                else:
                    outer_position = current.get_next()
                    current.set_next(current.get_next().get_next())
            self.__len -= 1
        return outer_position.value

    def first(self):
        return self.__head.value

    def last(self):
        return self.__tail.value


class TestLinkedList(unittest.TestCase):
    def test_init(self):
        self.linked_list = LinkedList()
        self.assertEqual(len(self.linked_list), 0, "Initial length should be zero")
        self.assertEqual(self.linked_list.__len__(), 0, "Initial length should be zero")

    def test_add(self):
        self.linked_list = LinkedList()
        self.assertEqual(self.linked_list.__len__(), 0, "Initial length should be zero")
        self.linked_list.add(1)
        self.assertEqual(self.linked_list.__len__(), 1, "Length after the first insertion should be 1")
        self.assertEqual(self.linked_list[0], 1, "First element after the first insertion should be 1")
        self.linked_list.add(2)
        self.assertEqual(self.linked_list.__len__(), 2, "Length after the second insertion should be 2")
        self.assertEqual(self.linked_list[0], 1, "First element after the second insertion should be 1")
        self.assertEqual(self.linked_list[1], 2, "Second element after the second insertion should be 2")
        self.linked_list.add(3, 0)
        self.assertEqual(self.linked_list.__len__(), 3, "Length after the sird insertion should be 3")
        self.assertEqual(self.linked_list[0], 3, "First element after the sird insertion should be 3")
        self.assertEqual(self.linked_list[1], 1, "Second element after the sird insertion should be 1")
        self.assertEqual(self.linked_list[2], 2, "Third element after the sird insertion should be 2")

    def test_extend(self):
        self.linked_list = LinkedList()
        self.assertEqual(self.linked_list.__len__(), 0, "Initial length should be zero")
        self.linked_list.extend([1, 2, 3])
        self.assertEqual(self.linked_list.__len__(), 3, "Length after the first extension should be 3")
        self.assertEqual(self.linked_list[0], 1, "First element after the first extension should be 1")
        self.assertEqual(self.linked_list[1], 2, "Second element after the first extension should be 2")
        self.assertEqual(self.linked_list[2], 3, "Third element after the first extension should be 3")
        self.linked_list.extend(['1', '2', '3'])
        self.assertEqual(self.linked_list.__len__(), 6, "Length after the second extension should be 6")
        self.assertEqual(self.linked_list[0], 1, "First element after the second extension should be 1")
        self.assertEqual(self.linked_list[1], 2, "Second element after the second extension should be 2")
        self.assertEqual(self.linked_list[2], 3, "Third element after the second extension should be 3")
        self.assertEqual(self.linked_list[3], '1', "Forth element after the second extension should be 1 as string")
        self.assertEqual(self.linked_list[4], '2', "Fifth element after the second extension should be 2 as string")
        self.assertEqual(self.linked_list[5], '3', "Sixth element after the second extension should be 3 as string")
        self.linked_list.extend([41, 42, 43], 3)
        self.assertEqual(self.linked_list.__len__(), 9, "Length after the third extension should be 9")
        self.assertEqual(self.linked_list[0], 1, "First element after the third extension should be 1")
        self.assertEqual(self.linked_list[1], 2, "Second element after the third extension should be 2")
        self.assertEqual(self.linked_list[2], 3, "Third element after the third extension should be 3")
        self.assertEqual(self.linked_list[3], 41, "Forth element after the third extension should be 41")
        self.assertEqual(self.linked_list[4], 42, "Fifth element after the third extension should be 42")
        self.assertEqual(self.linked_list[5], 43, "Sixth element after the third extension should be 43")
        self.assertEqual(self.linked_list[6], '1', "Seventh element after the third extension should be 1 as string")
        self.assertEqual(self.linked_list[7], '2', "Eighths element after the third extension should be 2 as string")
        self.assertEqual(self.linked_list[8], '3', "Ninth element after the third extension should be 3 as string")

    def test_contains(self):
        self.linked_list = LinkedList()
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.assertEqual(1 in self.linked_list, True,
                         "After inserting 1 into the list, we should be able to find it there")
        self.assertEqual(4 in self.linked_list, False,
                         "After inserting 1 into the list, we should be able to find it there")

    def test_remove_last_occurence(self):
        self.linked_list = LinkedList()
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.assertEqual(self.linked_list.__len__(), 3, "Length should be 3")
        self.assertEqual(1 in self.linked_list, True, "After inserting 1 into the list, we should be able to find it there")
        self.assertEqual(2 in self.linked_list, True, "After inserting 2 into the list, we should be able to find it there")
        self.assertEqual(3 in self.linked_list, True, "After inserting 3 into the list, we should be able to find it there")
        self.linked_list.remove_last_occurence(1)
        self.assertEqual(self.linked_list.__len__(), 2, "After the first removal the length should be 2")
        self.assertEqual(1 in self.linked_list, False, "After removing 1 we should not be able to find it in our list")
        self.linked_list.remove_last_occurence(2)
        self.assertEqual(self.linked_list.__len__(), 1, "After the second removal the length should be 1")
        self.assertEqual(2 in self.linked_list, False, "After removing 2 we should not be able to find it in our list")
        self.linked_list.remove_last_occurence(3)
        self.assertEqual(self.linked_list.__len__(), 0, "After the third removal the length should be 0")
        self.assertEqual(3 in self.linked_list, False, "After removing 3 we should not be able to find it in our list")

    def test_pop(self):
        self.linked_list = LinkedList()
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.assertEqual(self.linked_list.__len__(), 3, "Length should be 3")
        self.assertEqual(1 in self.linked_list, True, "After inserting 1 into the list, we should be able to find it there")
        self.assertEqual(2 in self.linked_list, True, "After inserting 2 into the list, we should be able to find it there")
        self.assertEqual(3 in self.linked_list, True, "After inserting 3 into the list, we should be able to find it there")
        self.assertEqual(self.linked_list.pop(0), 1, "If we pop the first element we should get 1")
        self.assertEqual(self.linked_list.__len__(), 2, "Length after the first pop should be 2")
        self.assertEqual(self.linked_list.pop(), 3, "If we pop by default we should get 3")
        self.assertEqual(self.linked_list.__len__(), 1, "Length after the second pop should be 1")
        self.assertEqual(self.linked_list.pop(), 2, "If we pop by default we should get 2")
        self.assertEqual(self.linked_list.__len__(), 0, "Length after the third pop should be 0")


if __name__ == '__main__':
    items = LinkedList()
    items.add(10)
    items.add(11)
    items.add(12)
    items.add(13)
    items.add(20)
    print(items[0])
    print(items[2])
    print(items.first())
    print(items.last())
    print(len(items))
    unittest.main()
