# List তৈরি করা
fruits = ["apple", "banana", "mango"]
print("Initial list:", fruits)

# Item যোগ করা
fruits.append("orange")
print("After append:", fruits)

# নির্দিষ্ট অবস্থানে item যোগ করা
fruits.insert(1, "grape")
print("After insert:", fruits)

# Item সরানো
fruits.remove("banana")
print("After remove:", fruits)

# ইনডেক্স দিয়ে অ্যাক্সেস
print("First fruit:", fruits[0])

# লুপ চালানো
for fruit in fruits:
    print("Fruit:", fruit)

# লিস্টের দৈর্ঘ্য
print("Total fruits:", len(fruits))
