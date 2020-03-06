# Code Listing #11

"""

Example of using namedtuple
A namedtuple is much more memory-efficient when compared to a class which has the same fields.
 Hence a namedtuple is very useful in the following scenarios:
*A large amount of data needs to be loaded as read-only with keys and values from a store.
Examples are loading columns and values via a DB query or loading data from a large CSV file.
*When a lot of instances of a class need to be created but not many write or set operations need to be done
on the attributes. Instead of creating class instances, namedtuple instances can be created to save on memory.
The _make method can be used to load an existing iterable that supplies fields in the same order to
return a namedtuple instance. For example, if there is an employees.csv file with the columns name, age, gender, title,
and department in that order, we can load them all into a container of namedtuples using the following command line:
employees = map(Employee._make, csv.reader(open('employees.csv'))
"""

from collections import namedtuple

Employee = namedtuple('Employee', 'name, age, gender, title, department')
print(Employee)
# Create an employee
jack = Employee('Jack', 25, 'M', 'Programmer', 'Engineering')
print(jack)

for field in jack:
    print(field)

# This will raise an error
# jack.age=32

# This works fine
print(jack._replace(age=32))
