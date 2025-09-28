# 1. nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
#a. What was the average temperature in first week of Jan
#b. What was the maximum temperature in first 10 days of Jan


arr = []

with open("nyc_weather.csv", "r") as f:
    for line in f:
        tokens = line.strip().split(",")
        
        if tokens[0] == "date":
            continue
        
        try:
            temperature = int(tokens[1])  # extract temperature
            arr.append(temperature)
        except ValueError:
            print("Invalid temperature. Ignoring this row.")

# (a) Average temperature in first week of Jan (first 7 days)
if len(arr) >= 7:
    avg_temp_week1 = sum(arr[0:7]) / len(arr[0:7])
    print(f"Average temperature in first week of Jan: {avg_temp_week1:.2f}")
else:
    print("Not enough data for first week.")

# (b) Maximum temperature in first 10 days of Jan
if len(arr) >= 10:
    max_temp_10days = max(arr[0:10])
    print(f"Maximum temperature in first 10 days of Jan: {max_temp_10days}")
else:
    print("Not enough data for first 10 days.")


#(2) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
#   (a) What was the temperature on Jan 9?
#   (b) What was the temperature on Jan 4?


weather_dict = {}

with open("nyc_weather.csv", "r") as f:
    for line in f:
        tokens = line.strip().split(",")
        
        if tokens[0] == "date":
            continue
        
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except ValueError:
            print("Invalid temperature. Ignore the row")

# (a) Temperature on Jan 9
print("Temperature on Jan 9:", weather_dict.get("Jan 9", "Data not available"))

# (b) Temperature on Jan 4
print("Temperature on Jan 4:", weather_dict.get("Jan 4", "Data not available"))



#3. poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.
word_count = {}  
with open("poem.txt", "r") as f:
    for line in f:
        tokens = line.split()
        for token in tokens:
            token = token.strip()
            
            if token in word_count:
                word_count[token] += 1
            else:
                word_count[token] = 1

for word, count in word_count.items():
    print(f"'{word}': {count},")


#4 Implement hash table where collisions are handled using linear probing. We learnt about linear probing in the video tutorial. Take the hash table implementation that uses chaining and modify methods to use linear probing. Keep MAX size of arr in hashtable as 10.
# hashtable_linear_probing.py

class HashTable:
    def __init__(self):
        self.MAX = 10  
        self.arr = [None for _ in range(self.MAX)]
        
    def get_hash(self, key):
        """Simple hash function based on sum of ASCII values."""
        hash_val = 0
        for char in key:
            hash_val += ord(char)
        return hash_val % self.MAX
    
    def get_prob_range(self, index):
        """Generate probing sequence starting from index, wrapping around."""
        return [*range(index, len(self.arr))] + [*range(0, index)]
    
    def find_slot(self, key, index):
        """Find an available slot using linear probing."""
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:   
                return prob_index
            if self.arr[prob_index][0] == key: 
                return prob_index
        raise Exception("Hashmap full")
    
    def __setitem__(self, key, val):
        """Insert or update key-value pair."""
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, val)
        print(self.arr)  
    
    def __getitem__(self, key):
        """Retrieve value for given key."""
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:   
                return None
            if element[0] == key:
                return element[1]
        return None
    
    def __delitem__(self, key):
        """Delete key-value pair."""
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return   # item not found
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
                break
        print(self.arr)  
t = HashTable()
t["march 6"] = 20
t["march 17"] = 88
t["march 17"] = 29
t["nov 1"] = 1
t["march 33"] = 234
print(t["march 33"])  
t["march 33"] = 999
print(t["march 33"])  
t["april 1"] = 87
t["april 2"] = 123
t["april 3"] = 234234
t["april 4"] = 91
t["May 22"] = 4
t["May 7"] = 47
del t["april 2"]
t["Jan 1"] = 0
