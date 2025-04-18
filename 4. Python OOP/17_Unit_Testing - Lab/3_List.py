class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class TestList(TestCase):
    def setUp(self):
        self.cl = IntegerList(1, 2, 3)

    def test_init_int_values(self):
        self.assertListEqual([1, 2, 3], self.cl._IntegerList__data)

    def test_init_non_integers_are_skipped(self):
        new_list = IntegerList("asd", 1.25, [1, 2, 3], 5)
        self.assertListEqual([5], new_list._IntegerList__data)

    def test_get_data_return_private_data(self):
        result = self.cl.get_data()

        self.assertListEqual([1, 2, 3], result)
        self.assertIs(self.cl._IntegerList__data, result)

    def test_add_non_integer_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cl.add("asd")
            self.cl.add(4.5)
            self.cl.add([1, 2, 3])

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_integer(self):
        self.assertListEqual([1, 2, 3], self.cl._IntegerList__data)

        result = self.cl.add(5)

        self.assertListEqual([1, 2, 3, 5], self.cl._IntegerList__data)
        self.assertIs(self.cl._IntegerList__data, result)

    def test_remove_index_invalid_index_raises(self):
        length_index = len(self.cl._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.cl.remove_index(length_index)
            length_index += 1
            self.cl.remove_index(length_index)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index(self):
        self.assertListEqual([1, 2, 3], self.cl._IntegerList__data)

        result = self.cl.remove_index(1)

        self.assertEqual(2, result)

        self.assertListEqual([1, 3], self.cl._IntegerList__data)
        self.assertNotIn(2, self.cl._IntegerList__data)

    def test_get_invalid_index_raises(self):
        length_index = len(self.cl._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.cl.get(length_index)
            length_index += 1
            self.cl.get(length_index)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_el_by_index(self):
        self.assertListEqual([1, 2, 3], self.cl._IntegerList__data)
        result = self.cl.get(1)

        self.assertEqual(2, result)
        self.assertListEqual([1, 2, 3], self.cl._IntegerList__data)

    def test_invalid_index_insert_raises(self):
        length_index = len(self.cl._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.cl.insert(length_index, 5)
            length_index += 1
            self.cl.insert(length_index, 5)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_invalid_element_raises(self):
        element = "asd"

        with self.assertRaises(ValueError) as ex:

            self.cl.insert(0, element)
            element = 3.5

            self.cl.insert(0, element)
            element = [1, 2, 3]

            self.cl.insert(0, element)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert(self):
        self.assertListEqual([1, 2, 3], self.cl._IntegerList__data)

        result = self.cl.insert(0, 5)
        self.assertIsNone(result)

        self.assertListEqual([5, 1, 2, 3], self.cl._IntegerList__data)

    def test_get_biggest(self):
        new_list = IntegerList(3, -2, 100, 8)

        result = new_list.get_biggest()

        self.assertEqual(100, result)

    def test_get_index(self):
        self.assertIn(1, self.cl._IntegerList__data)
        self.assertEqual(1, self.cl._IntegerList__data[0])

        result = self.cl.get_index(1)

        self.assertEqual(0, result)

if __name__ == "__main__":
    main()

