# Example: Using iter() with a list
my_list = ["hey", "hello", "zero", "one", "two"]
my_iterator = iter(my_list)

# Now, we can iterate through the list using the iterator
for i in my_list:
    print(next(my_iterator))  # Outputs: 1

# The next call would raise a StopIteration exception since there are no more elements
#print(next(my_iterator))