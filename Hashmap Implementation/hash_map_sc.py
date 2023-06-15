# Name: Lamar Petty
# OSU Email: pettyla@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6
# Due Date: 17 MAR 2023
# Description: Hashmap implementation


from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self,
                 capacity: int = 11,
                 function: callable = hash_function_1) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

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
        Increment from given number and the find the closest prime number
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
        if self.table_load() >= 1.0:
            new_capacity = 2 * self._capacity
            self.resize_table(new_capacity)

        # determine hash and index
        hashed_key = self._hash_function(key)
        index = hashed_key % self._capacity


        #search for duplicates keys
        found = False

        for node in self._buckets[index]:
            if key == node.key:
                node.value = value
                found = True
                break

        if found == True:
            return

        #insert
        self._size += 1
        self._buckets[index].insert(key, value)

    def empty_buckets(self) -> int:
        """
        Calculates the number of empty buckets.

        :return: number of empty buckets (integer)
        """

        counter = 0
        #loop through and count non-empty buckets
        for i in range(0, self._capacity, 1):
            if self._buckets[i].length() != 0:
                counter += 1

        numEmpty = self._capacity - counter

        return numEmpty


    def table_load(self) -> float:
        """
        Calculates the load factor based on
        the size and capacity of the hashmap.

        :return: load factor (float)
        """

        load = self._size / self._capacity

        return load

    def clear(self) -> None:
        """
        Clear the contents of the hash map.

        :return: NONE
        """

        #preserve the capacity
        current_cap = self._capacity

        #preserve the hash function
        function = self._hash_function

        #add linked List to each bucket
        for i in range(0, self._capacity, 1):
            if self._buckets[i].length() != 0:
                self._buckets[i] = LinkedList()

        #reset self
        self._size = 0
        self = HashMap(current_cap, function)
        self._capacity = current_cap

    def resize_table(self, new_capacity: int) -> None:
        """
        Resizes the hash table with the given input param.

        :param new_capacity: (integer)
        :return: None
        """
        # ensure valid new capacity
        if new_capacity < 1:
            return

        #preserve old capacity
        old_capacity = self._capacity

        right_cap = self._is_prime(new_capacity)
        #if capacity is already prime, move on
        if right_cap:
            self._capacity = new_capacity

        #else, loop until capacity is prime
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
            self._buckets.append(LinkedList())

        #rehash
        daLength = new_da.length()
        for i in range(0, daLength, 1):
            if new_da[i].length() != 0:
                for node in new_da[i]:
                    key = node.key
                    value = node.value
                    self.put(key, value)
                    node = node.next

    def get(self, key: str) -> object:
        """
        Get the value associated with a given key.

        :param key: string
        :return: value (object)
        """
        #hash the key to get index
        hashed_key = self._hash_function(key)
        index = hashed_key % self._capacity

        found = None
        #iterate and if key is found, return the node value
        for node in self._buckets[index]:
            if key == node.key:
                found = node.value
                break


        return found

    def contains_key(self, key: str) -> bool:
        """
        Determine if a given key is in the hash map.

        :param key: (string)
        :return: TRUE if found, otherwise FALSE
        """

        # hash the key to get index
        hashed_key = self._hash_function(key)
        index = hashed_key % self._capacity

        found = False
        # iterate and if key is found, return boolean
        for node in self._buckets[index]:
            if key == node.key:
                found = True
                break


        return found

    def remove(self, key: str) -> None:
        """
        Remove a given key and associated value
        pair from the hash map.

        :param key: (string)
        :return: NONE
        """
        # hash the key to get index
        hashed_key = self._hash_function(key)
        index = hashed_key % self._capacity

        removed = False
        #iterate and if key is found, remove it
        for node in self._buckets[index]:
            if key == node.key:
                removed = self._buckets[index].remove(key)
                break

        if removed:
            self._size -= 1

    def get_keys_and_values(self) -> DynamicArray:
        """
        Gets the key/value pairs from the hashmap.

        :return: key/value pair (Dynamic Array)
        """

        #initialize new array and tuple
        new_da = DynamicArray()

        #load tuple w/ key value and add to new_da
        for i in range(0, self._capacity, 1):
            if self._buckets[i].length() != 0:
                for node in self._buckets[i]:
                    keyVal_tuple = (node.key, node.value)
                    new_da.append(keyVal_tuple)
                    node = node.next

        return new_da



def find_mode(da: DynamicArray) -> (DynamicArray, int):
    """
    Find the mode of a given input array. Returns a tuple
    containing a key(s) and the associated mode.

    :param da: input array
    :return: Dynamic array, mode (int)
    """

    #initialize map
    map = HashMap()
    new_da = DynamicArray()

    #Put elements into hasmap (similar to put method)
    for i in range(0, da.length(), 1):
        # check to see if table needs resizing
        if map.table_load() >= 1.0:
            map.resize_table(2 * map.get_capacity())

        # determine hash and index
        hashed_key = map._hash_function(da[i])
        index = hashed_key % map._capacity

        #load the map
        #if empty bucket, insert with count of 1
        if map._buckets[index].length() == 0:
            map._size += 1
            map._buckets[index].insert(da[i], 1)
        else:
        #if not empty
            counter = 0
            for node in map._buckets[index]:
                counter += 1
                #if initial node, increment freq if same
                if da[i] == node.key:
                    node.value += 1
                    break
                #increment next bucket if not initial bucket
                if counter == map._buckets[index].length():
                    map._buckets[index].insert(da[i], 1)
                node = node.next

    #Build a array of tuples
    count_arr = map.get_keys_and_values()

    #find max and append
    max = 0
    arrLength = count_arr.length()
    for i in range(0, arrLength, 1):
        if count_arr[i][1] == max:
            new_da.append(count_arr[i][0])
        if count_arr[i][1] > max:
            #if new max, clear the array, re-append
            new_da = DynamicArray()
            max = count_arr[i][1]
            new_da.append(count_arr[i][0])


    return (new_da, max)
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
    m = HashMap(53, hash_function_1)
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

    print("\nPDF - get_keys_and_values example 1")
    print("------------------------")
    m = HashMap(11, hash_function_2)
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(2)
    print(m.get_keys_and_values())

    print("\nPDF - find_mode example 1")
    print("-----------------------------")
    da = DynamicArray(["apple", "apple", "grape", "melon", "peach"])
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")

    print("\nPDF - find_mode example 2")
    print("-----------------------------")
    test_cases = (
        ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu"],
        ["one", "two", "three", "four", "five"],
        ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}\n")


"""
#=============Student Testing Block ================#
print("\nPDF - put example 1")
print("-------------------")
m = HashMap(53, hash_function_1)
for i in range(150):
    m.put('str' + str(i), i * 100)
    if i % 25 == 24:
        print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

print("\nPDF - find_mode example 1 w/ gradescope example")
print("-----------------------------")
da = DynamicArray(['914', '987', '689', '-917', '-213', '41', '2', '-983', '-983', '-983', '-370', '-548', '-548', '-548'])
mode, frequency = find_mode(da)
print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")


print("\nPDF - find_mode example 2")
print("-----------------------------")
test_cases = (
    ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu"],
    ["one", "two", "three", "four", "five"],
    ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"])

for case in test_cases:
    da = DynamicArray(case)
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}\n")"""