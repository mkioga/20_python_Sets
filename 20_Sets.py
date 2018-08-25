
# ===========
# 20_sets.py
# ===========

# A set in python is unordered and does not contain duplicates
# In that way, it is similar to a dictionary. but unlike a dictionary
# items are Not accessed by a key. And do not have a key
# A set is more similar to a collection of dictionary keys and the set members
# are hashed in the same way dictionary keys are.
# Elements in a set must be immutable objects (just like dictionary keys)
# Sets also support "union" and "intersection" operations that can be formed on sets.
# Sets can be very useful for cleaning up data

# There are two ways to create sets.

# ==========
# Method 1
# ==========

farmAnimals = {"sheep", "cow", "hen"}    # creating a set
print(farmAnimals)   # print the set

for animals in farmAnimals:
    print(animals)       # Iterate through farmAnimals and print each one

print("=" *20)   # This is a separator line


# ==========
# Method 2:
# ==========
# using set function

# Using inbuilt "set" function and pass the list of animals to the "set" function

wildAnimals = set(["lion", "tiger", "hyena"])   # create using "set" function
print(wildAnimals)

for animals in wildAnimals:
    print(animals)

print("=" *20)

# ===============
# "add" operator
# ===============

# you can add items to set using "add" operator

# We will add horse to both farmAnimals and wildAnimals
# Note that there is no order to where "horse" was added.
# If you run the code several times, order will change
# This is because "sets" are unordered

farmAnimals.add("horse")
wildAnimals.add("horse")
print(farmAnimals)
print(wildAnimals)
print("=" *40)


# ===================
# Creating Empty set
# ===================

# we use the set function to create empty set because if we use Method 1 and pass no items to it
# it will create a "dictionary" instead of a set.

# In this example, we create two empty sets using both methods

emptySet_1 = set()   # empty set created the right way
emptySet_2 = {}      # empty set created using method 1 (wrong way). this creates a dictionary instead of a set


# Now to test which is a set and which is not, we use the "add" function which we know
# is a "set" function but not a "dictionary" function
# So we see line for emptySet_2 gives error proving it is a "dictionary" and not a set.
# so we use "set" function to create an empty "set"

emptySet_1.add("man")
# emptySet_2.add("man")   # This will give an error saying 'dict" object has no attribute 'add"
print(emptySet_1)
print(emptySet_2)

print("="*40)

# ======================
# Pass "range" to sets
# ======================

# When we used set earlier, we passed it a list of parameters as shown
# wildAnimals = set(["lion", "tiger", "hyena"])
# but we can also use any "iterable object" such as "tuple" or "range" to pass as parameters to sets

# Here we create a set named "evenNumbers" and pass it a range(0, 40, 2)

evenNumbers = set(range(0, 40, 2))
print(evenNumbers)   # prints out the range. Note that it loops at 32. This is because sets are unordered and can appear in any order
print("="*20)

# Pass "tuples" to "sets"
# Note that a tuple is an ordered set of data that is immutable. enclosed in {}

squaresTuple = {4, 9, 16, 25, 36}
print(squaresTuple)   # prints out the tuple

squaresSet = set(squaresTuple)
print(squaresSet)   # prints out the set made by passing it a tuple. it is unordered
print("="*40)


# ============================
# "union" function of "sets"
# ============================

# "union" function combines elements but does not duplicate them.
# If there are elements that are duplicates in both sets, it counts only once

even = set(range(0, 15, 2))
print("Set = {}".format(even))   # This is the set
print("Set Length = {}".format(len(even)))   # This is the length of the set
print("=" *20)

squaresTuple = {4, 6, 9, 16, 25}   # Tuple with 5 elements
squaresSet = set(squaresTuple)   # create set with tuple above. Also has 5 elements
print("SquaresSet = {}".format(squaresSet))   # print the set
print("SquareSet Length = {}".format(len(squaresSet)))  # print length of set
print("=" *20)

# Now we use "union" function to combine sets "even" and "squaresSet"
# Note that "even" has 8 elements and "squaresSet" has 5 elements. Total is 13
# But union shows 11 elements
# This is because there is no duplication. Element nymber 2 and 4 are in both sets
# So the union counts them as one and will not duplicate them.

print(even.union(squaresSet))
print(len(even.union(squaresSet)))

# Note that results are same whether you combine even to squaresSet or vice versa

print(squaresSet.union(even))
print(len(squaresSet.union(even)))

print("="*40)

# ===================================
# "intersection" function in "sets"
# ===================================

# "intersection" function prints only the numbers that are present in common in both sets.

even = set(range(0, 15, 2))
print("Set = {}".format(even))   # This is the set
print("Set Length = {}".format(len(even)))   # This is the length of the set
print("=" *20)

squaresTuple = {4, 6, 9, 16, 25}   # Tuple with 5 elements
squaresSet = set(squaresTuple)   # create set with tuple above. Also has 5 elements
print("SquaresSet = {}".format(squaresSet))   # print the set
print("SquareSet Length = {}".format(len(squaresSet)))  # print length of set
print("=" *20)

# intersection gets the numbers that are common in both sets.
print("even.intersection(squaresSet)")
print(even.intersection(squaresSet))    # prints the values found intersecting
print(len(even.intersection(squaresSet)))   # prints the length of values found intersecting

# Note that results are same both ways
print("squaresSet.intersection(even)")
print(squaresSet.intersection(even))
print(len(squaresSet.intersection(even)))

print("="*40)



# ========================
# "subtraction" in sets
# ========================

# We do subtraction in set using "difference" function or "-" sign
# "difference" function is preferred because it makes you know you are dealing with sets
# because "difference" function is for sets only.


even = set(range(0, 15, 2))
print("Even (sorted) = {}".format(sorted(even)))   # print sorted "even"
print("Even Length = {}".format(len(even)))   # This is the length of "even" set
print("=" *20)

squaresTuple = {4, 6, 9, 16, 25}   # Tuple with 5 elements
squaresSet = set(squaresTuple)   # create set with tuple above. Also has 5 elements
print("SquaresSet (sorted) = {}".format(sorted(squaresSet)))   # print sorted "squaresSet"
print("SquareSet Length = {}".format(len(squaresSet)))  # print length of set
print("=" *20)

# Now we are going to do subtraction using both "difference" and "-" sign
# Even minus SquaresSet takes off any common elements existing in SquaresSet from Even
# In this case, common elements are 4 & 6
# So we take 4 & 6 away from Even and we remain with 6 elements

print("Even minus SquaresSet")
print(sorted(even.difference(squaresSet)))   # results are same for these two methods
print(len(even.difference(squaresSet)))      # length is 6
print(sorted(even - squaresSet))             # results are same for these two methods
print(len(even - squaresSet))                # Length is 6
print("=" *20)

# When we do SquareSet minus Even, the common elements are 4 and 6
# So we remove 4 and 6 from SquareSet and we remain with only 3 elements

print("SquareSet minus Even")
print(sorted(squaresSet.difference(even)))   # results are same for these two methods
print(len(squaresSet.difference(even)))      # length is 3
print(sorted(squaresSet - even))             # results are same for these two methods
print(len(squaresSet - even))                # Length is 3
print("=" *40)




# ====================================
# "update_difference" method in sets
# ====================================

# The "update_difference" method performs subtraction in place.
# i.e. it subtracts and updates the same set
# It does not return a new set, but it modifies the set from which it is called on.

even = set(range(0, 15, 2))
print("Even (sorted) = {}".format(sorted(even)))   # print sorted "even"
print("Even Length = {}".format(len(even)))   # This is the length of "even" set
print("=" *20)

squaresTuple = {4, 6, 9, 16, 25}   # Tuple with 5 elements
squaresSet = set(squaresTuple)   # create set with tuple above. Also has 5 elements
print("SquaresSet (sorted) = {}".format(sorted(squaresSet)))   # print sorted "squaresSet"
print("SquareSet Length = {}".format(len(squaresSet)))  # print length of set
print("=" *20)

# difference_update function does a subtraction on "even" and updates "even" with results
print("even.difference_update(squareSet)")
even.difference_update(squaresSet)
print("New Even (sorted) = {}".format(sorted(even)))   # New "even" is updated
print("SquaresSet (sorted) = {}".format(sorted(squaresSet)))   # "squaresSet" is unchanged
print("=" *40)



# =====================================
# "symmetric_difference" of two sets.
# =====================================

# "symmetric_difference" of two sets is all the members that are in one set or the other
# but not both. These are numbers that are not common in both sets.

# being symmetric means that it does not matter which way around you calculate the difference
# "symmetric_difference" can be thought of as the opposite of "intersection" that we covered above
# Because "intersection" gets numbers that are common in both sets.

even = set(range(0, 15, 2))
print("Even (sorted) = {}".format(sorted(even)))   # print sorted "even"
print("Even Length = {}".format(len(even)))   # This is the length of "even" set
print("=" *20)

squaresTuple = {4, 6, 9, 16, 25}   # Tuple with 5 elements
squaresSet = set(squaresTuple)   # create set with tuple above. Also has 5 elements
print("SquaresSet (sorted) = {}".format(sorted(squaresSet)))   # print sorted "squaresSet"
print("SquareSet Length = {}".format(len(squaresSet)))  # print length of set
print("=" *20)

# We will do "symmetric_difference" both ways to pull all members that are not common in both
# In this case, we see 4 & 6 are common. So they are removed.
# All the other members are not common in both sets and are shown.
# both commands get same results because they pull same numbers that are not common in both.
# Note that you don't need "sorted", but we just put it there for easier viewing of results.

print("Symmetric Even minus SquaresSet")
print(sorted(even.symmetric_difference(squaresSet)))
print()
print("Symmetric SquaresSet minus Even")
print(sorted(squaresSet.symmetric_difference(even)))

print("=" *40)


# ================================
# "symmetric_difference_update"
# ================================

# It does a "symmetric_difference" but updates the set
# that it is being called from rather than create a new set.


even = set(range(0, 15, 2))
print("Even (sorted) = {}".format(sorted(even)))   # print sorted "even"
print("Even Length = {}".format(len(even)))   # This is the length of "even" set
print("=" *20)

squaresTuple = {4, 6, 9, 16, 25}   # Tuple with 5 elements
squaresSet = set(squaresTuple)   # create set with tuple above. Also has 5 elements
print("SquaresSet (sorted) = {}".format(sorted(squaresSet)))   # print sorted "squaresSet"
print("SquareSet Length = {}".format(len(squaresSet)))  # print length of set
print("=" *20)

# "symmetric_difference_update" returns values that are not common in both sets.
# Then updates the set it was called from with the results

print("even.symmetric_difference_update(squareSet)")
even.symmetric_difference_update(squaresSet)
print("New Even (sorted) = {}".format(sorted(even)))   # New "even" is updated
print("New Even Length = {}".format(len(even)))
print("SquaresSet (sorted) = {}".format(sorted(squaresSet)))   # "squaresSet" is unchanged
print("SquareSet Length = {}".format(len(squaresSet)))   # "squareSet" length is unchanged
print("=" *40)



# =======================
# "discard" and "remove"
# =======================

# "discard" and "remove" are the two ways to remove an item from a set.
# The difference between them is that "remove" will raise an error if item to be removed
# does not exist, while "discard" will not raise an error in that scenario


even = set(range(0, 15, 2))
print("Even (sorted) = {}".format(sorted(even)))   # print sorted "even"
print("Even Length = {}".format(len(even)))   # This is the length of "even" set
print("=" *20)

squaresTuple = {4, 6, 9, 16, 25}   # Tuple with 5 elements
squaresSet = set(squaresTuple)   # create set with tuple above. Also has 5 elements
print("SquaresSet (sorted) = {}".format(sorted(squaresSet)))   # print sorted "squaresSet"
print("SquareSet Length = {}".format(len(squaresSet)))  # print length of set
print("=" *20)

# remove existing member using "discard"
print("Remove existing 0 from 'even' using 'discard")
even.discard(0)
print(sorted(even))

# remove non existent member using "discard".
# There is no error if you try to remove non-existing member from a set using "discard"

print("Remove non-existing 3 from 'even' using 'discard")
even.discard(3)
print(even)
print("=" *20)


# remove existing member using "remove"
print("Remove existing 4 from 'SquaresSet' using 'remove")
squaresSet.remove(4)
print(sorted(squaresSet))

print("=" *20)

# remove non existent member using "remove".
# "remove" gives an error if you try to remove non-existing member with it

# print("Remove non-existing 7 from 'squaresSet' using 'remove")
# squaresSet.remove(7)   # This one gives an error since 7 does not exist in squareSet
# print(squaresSet)
# print("=" *20)



# A solution to avoiding above error is to check if the number you want to remove exists
# in the set.

if 7 in squaresSet:
    squaresSet.remove(7)
    print(squaresSet)
else:
    print("Number 7 does not exist in squaresSet")

print("=" *40)


# ====================
# Why we use "remove"
# ====================

# we may want to use remove so that it creates an error so we are aware something is
# happening and it will let us take some action about the error

# Here is an example of using functions "try" and "except" to act on errors
# created by "remove"
# We will try to remove 7 from squareSet and it does not exist there

# this is the same concept as trying to retrieve values from dictionary using
# [] or using get(). If values don't exist, [] gives error but get() does not.

print()
print("Test if 7 exist in 'squaresSet' before using 'remove")
try:
    squaresSet.remove(7)
except KeyError:
    print("7 does not exist in SquareSet")

print("=" *40)



# ============================
# "subsets" and "supersets"
# ============================

# Set A is a subset of Set B if all the elements in Set A exists in Set B
# While Set B is a superset of Set A if it contains all of Set A's elements

# From the results, we know that "squareSet" is a subset of "even"

even = set(range(0, 15, 2))
print("Even (sorted) = {}".format(sorted(even)))   # print sorted "even"
print("Even Length = {}".format(len(even)))   # This is the length of "even" set
print("=" *20)

squaresTuple = {4, 6, 8, 10, 12}   # Tuple with 5 elements
squaresSet = set(squaresTuple)   # create set with tuple above. Also has 5 elements
print("SquaresSet (sorted) = {}".format(sorted(squaresSet)))   # print sorted "squaresSet"
print("SquareSet Length = {}".format(len(squaresSet)))  # print length of set
print("=" *20)

# We can now test to see if "squareSet" is a subset of "even"
# and also if "even" is a superset of "squareSet"
# if you change numbers on squareSet to make it not subset, results will not print.

print("Test for subset and superset")
print()
if squaresSet.issubset(even):
    print("SquareSet is a subset of Even")

if even.issuperset(squaresSet):
    print("Even is superset of squareSet")

print("=" *40)

# =============
# "frozen set"
# =============

# A "frozen set" is an immutable set i.e. it cannot be changed.
# Being immutable, we can use a "frozen set" as a "dictionary" key
# And we can also add a "frozen set" as a member of a set
# "add", "remove" and "discard" methods are not available in "frozen sets"
# Once you create a "frozen set", it cannot be changed.


# we create a frozen set called even.

even = frozenset(range(0, 10, 2))
print(even)

# if you try to add something to this set, you will get error,
# because frozen sets are immutable

# even.add(3)   # This code gives error

print("=" *40)

# Other than inability to add or remove members, frozen sets behave like regular sets
# and can be used to create "unions", "intersections" and can be "subtracted" from other sets


# 8.7.1. Set Objects
# Here is a link of the operations that can be used with sets
# https://docs.python.org/2/library/sets.html


# "Sets" are not used as often as "lists" and "dictionaries"
# but they are useful in some ways like modifying data.


# ==================
# Sets Challenge
# ==================

# Create a program that takes some texts and returns a list of all
# the characters in the text that are not vowels (a,e,i,o,u). sorted in alphabetical order
# You can enter the text from the keyboard or initialize a string variable with a string.

# ==================
# My solution 1
# ==================

print("My Solution 1")
letters = set(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"])
print("Letters:")
print(sorted(letters))
print()
print("vowels:")
vowels = set(["a", "e", "i", "o", "u"])
print(sorted(vowels))
print()
print("Letters minus Vowels")   # we use difference to subtract vowels from letters
print(sorted(letters.difference(vowels)))
print()
print("=" *40)
print()

# =====================
# Trainers Solution 2
# =====================

print("Trainers Solution 2")
sampleString = "abcdefghijk"
vowels = frozenset("aeiou")   # Note that frozen set is immutable

# Here we create a new set named "vowelsRemoved"
# this new set is assigned results of set from sampleString minus vowels

print("Set from sampleString is:")
print(sorted(set(sampleString)))  # we create a set by passing it a string.
vowelsRemoved = set(sampleString).difference(vowels)
print()
print("Set from sampleString minus vowels")
print(vowelsRemoved)
print()
print("=" *40)
print()



# ====================
# Trainers Solution 3
# ====================

# This is similar to solution 2 but we will create vowels with a "set" instead of "frozenset".


print("Trainers Solution 3")
sampleString = "abcdefghijk"
vowels = {"a", "e", "i", "o" "u"}

# Here we create a new set named "vowelsRemoved"
# this new set is assigned results of set from sampleString minus vowels

print("Set from sampleString is:")
print(sorted(set(sampleString)))  # we create a set by passing it a string.
vowelsRemoved = set(sampleString).difference(vowels)
print()
print("Set from sampleString minus vowels")
print(vowelsRemoved)
print()
print("=" *40)
print()


