# Name: Lamar Petty
# OSU Email: pettyla@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6
# Due Date: 17 MAR 2023
# Description: Hashmap Implementation

from a6_include import (DynamicArray, DynamicArrayException, HashEntry,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        quadratic probing for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(None)

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number to find the closest prime number
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity % 2 == 0:
            capacity += 1

        while not self._is_prime(capacity):
            capacity += 2

        return capacity

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity == 2 or capacity == 3:
            return True

        if capacity == 1 or capacity % 2 == 0:
            return False

        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2

        return True

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        Add a key/value pair to hashmap.

        :param key: string value
        :param value: object
        :return: None
        """

        # check to see if table needs resizing
        if self.table_load() >= 0.5:
            new_capacity = 2 * self._capacity
            self.resize_table(new_capacity)

        #determine hash and index
        hashed_key = self._hash_function(key)
        index = hashed_key % self._capacity #change from size to capacity

        #create new tuple with key/value pair
        hash_object = HashEntry(key, value)

        #set value to index if index = None
        #else, advance to next None and add
        if self._buckets[index] == None or self._buckets[index].is_tombstone == True:
            self._size += 1
            self._buckets[index] = hash_object
            return
        else:
            #if the initial placement index is already beyond
            initial_index = index
            j = 1
            while self._buckets[index] is not None:
                if self._buckets[index].key == key:
                    if self._buckets[index].is_tombstone == True:
                        self._buckets[index] = hash_object
                        self._size += 1
                    else:
                        self._buckets[index] = hash_object
                    return
                index = (initial_index + (j*j)) % self._capacity
                j += 1


        self._size += 1
        self._buckets[index] = hash_object


    def table_load(self) -> float:
        """
        Calculates the load factor based on
        the size and capacity of the hashmap.

        :return: load factor (float)
        """
        # n/m = lambda
        # n = total # of elements stored
        # m is the number of buckets

        load = self._size / self._capacity

        return load

    def empty_buckets(self) -> int:
        """
        Calculates the number of empty buckets.

        :return: number of empty buckets (integer)
        """

        numEmpty = self._capacity - self._size

        return numEmpty


    def resize_table(self, new_capacity: int) -> None:
        """
        Resizes the hash table with the given input param.

        :param new_capacity: integer
        :return: None
        """

        # ensure valid new capacity
        if new_capacity < self._size:
            return

        #preserve old capacity
        old_capacity = self._capacity

        right_cap = self._is_prime(new_capacity)
        #if capacity is prime, move on
        if right_cap:
            self._capacity = new_capacity
        #else, go to next prime
        else:
            while right_cap is not True:
                right_cap = self._next_prime(new_capacity)
                if self._is_prime(right_cap):
                    self._capacity = right_cap
                    break

        #create new_da to copy hashmap
        new_da = DynamicArray()

        #for loop copying copy self to new
        j = 0
        for i in range(0, old_capacity, 1):
            new_da.append(self._buckets[i])
            j += 1

        #reset buckets, size, and set to None
        self._buckets = DynamicArray()
        self._size = 0

        for i in range(0, self._capacity, 1):
            self._buckets.append(None)

        #rehash
        daLength = new_da.length()
        for i in range(0, daLength, 1):
            hash_object = new_da[i]
            if hash_object is not None:
                key = hash_object.key
                value = hash_object.value
                self.put(key, value)



    def get(self, key: str) -> object:
        """
        Get the value associated with a given key.

        :param key: string
        :return: value (object)
        """
        value = None

        # hash the key to generate lookup index
        hashed_key = self._hash_function(key)
        index = hashed_key % self._capacity

        #quadratic probe and loop
        j = 1
        initial_index = index
        while j <= self._capacity - 1:

            hash_object = self._buckets[index]
            #if the index is occupied, check for correct key
            if hash_object is not None:
                search_key = hash_object.key
                if key == search_key:
                    if hash_object.is_tombstone == True:
                        value = None
                        break
                    else:
                        value = hash_object.value
                        break

            index = (initial_index + (j * j)) % self._capacity
            j += 1

        return value

    def contains_key(self, key: str) -> bool:
        """
        Determine if a given key is in the hash map.

        :param key: (string)
        :return: TRUE if found, otherwise FALSE
        """

        found = False
        #hash the key to generate lookup index
        hashed_key = self._hash_function(key)
        index = hashed_key % self._capacity

        #loop and quadratic probe
        j = 1
        initial_index = index
        while j <= self._capacity-1:

            hash_object = self._buckets[index]

            # if the index is occupied, check for correct key
            if hash_object is not None:
                search_key = hash_object.key
                if key == search_key:
                    if hash_object.is_tombstone == True:
                        found = False
                        break
                    else:
                        found = True
                        break
            #advance index with quadratic probing (removed modulo)
            index = (initial_index + (j * j)) % self._capacity
            j += 1

        return found

    def remove(self, key: str) -> None:
        """
        Remove a given key and associated value
        pair from the hash map.

        :param key: (string)
        :return: NONE
        """
        # hash the key to generate lookup index
        hashed_key = self._hash_function(key)
        index = hashed_key % self._capacity
        found = False
        j = 1
        initial_index = index
        while j <= self._capacity - 1:

            hash_object = self._buckets[index]
            # if the index is occupied, check for correct key
            if hash_object is not None:
                search_key = hash_object.key
                if key == search_key:
                    if hash_object.is_tombstone == True:
                        return
                    else:
                        hash_object.is_tombstone = True
                        found = True
                        break

            index = (initial_index + (j * j)) % self._capacity
            j += 1

        if found:
            self._size -= 1

    def clear(self) -> None:
        """
        Clear the contents of the hash map.

        :return: NONE
        """
        #preserve the current capacity
        current_cap = self._capacity

        #preserve the hash function
        function = self._hash_function

        #create none values
        for i in range(0, self._capacity, 1):
            if self._buckets[i] is not None:
                self._buckets[i] = None

        #reset self
        self._size = 0
        self = HashMap(current_cap, function)
        self._capacity = current_cap


    def get_keys_and_values(self) -> DynamicArray:
        """
        Gets the key/value pairs from the hashmap.

        :return: key/value pair (Dynamic Array)
        """
        #initialize new array and tuple
        new_da = DynamicArray()

        #load tuple w/ key value and add to new_da
        for i in range(0, self._capacity, 1):
            hash_object = self._buckets[i]
            if hash_object is not None and hash_object.is_tombstone == False:
                keyVal_tuple = (hash_object.key, hash_object.value)
                new_da.append(keyVal_tuple)

        return new_da


    def __iter__(self):
        """
        Initiolizes an index variable for interation.

        :return: self
        """

        self._index = 0

        return self

    def __next__(self):
        """
        Returns the next valid item in the hashmap

        :return: key/value pair (object)
        """

        try:
            hash_object = self._buckets[self._index]
        except DynamicArrayException:
            raise StopIteration

        #iterate over None and Tombstones (invalid items)
        while hash_object == None or hash_object.is_tombstone == True:
            self._index += 1
            try:
                hash_object = self._buckets[self._index]
            except DynamicArrayException:
                raise StopIteration

        #set the hash object
        hash_object = self._buckets[self._index]

        #increment the index
        self._index += 1
        return hash_object

# ------------------- BASIC TESTING ---------------------------------------- #


if __name__ == "__main__":

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(41, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(101, hash_function_1)
    print(round(m.table_load(), 2))
    m.put('key1', 10)
    print(round(m.table_load(), 2))
    m.put('key2', 20)
    print(round(m.table_load(), 2))
    m.put('key1', 30)
    print(round(m.table_load(), 2))

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(101, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(23, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        if m.table_load() > 0.5:
            print(f"Check that the load factor is acceptable after the call to resize_table().\n"
                  f"Your load factor is {round(m.table_load(), 2)} and should be less than or equal to 0.5")

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(31, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(151, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(11, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(53, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(101, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(53, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - get_keys_and_values example 1")
    print("------------------------")
    m = HashMap(11, hash_function_2)
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    print(m.get_keys_and_values())

    m.resize_table(2)
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(12)
    print(m.get_keys_and_values())

    print("\nPDF - __iter__(), __next__() example 1")
    print("---------------------")
    m = HashMap(10, hash_function_1)
    for i in range(5):
        m.put(str(i), str(i * 10))
    print(m)
    for item in m:
        print('K:', item.key, 'V:', item.value)

    print("\nPDF - __iter__(), __next__() example 2")
    print("---------------------")
    m = HashMap(10, hash_function_2)
    for i in range(5):
        m.put(str(i), str(i * 24))
    m.remove('0')
    m.remove('4')
    print(m)
    for item in m:
        print('K:', item.key, 'V:', item.value)
        

"""
#===============STUDENT TESTING ==========================#

print("\nPDF - put example 1")
print("-------------------")
m = HashMap(53, hash_function_1)
for i in range(150):
    m.put('str' + str(i), i * 100)
    if i % 25 == 24:
        print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())


print("\nPDF - put example 2")
print("-------------------")
m = HashMap(41, hash_function_2)
for i in range(50):
    m.put('str' + str(i // 3), i * 100)
    if i % 10 == 9:
        print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

print("\nPDF - contains_key example 1")
print("----------------------------")
m = HashMap(11, hash_function_1)
print(m.contains_key('key1'))
m.put('key1', 10)
m.put('key2', 20)
m.put('key3', 30)
print(m.contains_key('key1'))
print(m.contains_key('key4'))
print(m.contains_key('key2'))
print(m.contains_key('key3'))
m.remove('key3')
print(m.contains_key('key3'))

print("\nPDF - remove example 1")
print("----------------------")
m = HashMap(53, hash_function_1)
print(m.get('key1'))
m.put('key1', 10)
print(m.get('key1'))
m.remove('key1')
print(m.get('key1'))
m.remove('key4')

print("\nPDF - get_keys_and_values example 1")
print("------------------------")
m = HashMap(11, hash_function_2)
for i in range(1, 6):
    m.put(str(i), str(i * 10))
print(m.get_keys_and_values())

m.resize_table(2)
print(m.get_keys_and_values())

m.put('20', '200')
m.remove('1')
m.resize_table(12)
print(m.get_keys_and_values())
"""