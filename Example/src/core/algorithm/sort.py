from operator import itemgetter, attrgetter
from ExampleObject import student_tuples, student_objects

'''
sorted(iterator, cmp = None, key = None, reverse = False)
cmp : a function that takes two arguments, romove in Python3, like binary Predicate in C++ STL
key : a function that takes a single argument, like unary Predicate in C++ STL

if multiple records have same order in sort, the original order is showed
'''

def base():
    print sorted((5, 2, 3, 1, 4))
    #[1, 2, 3, 4, 5], sort tuple get a list
    
    print sorted([5, 2, 3, 1, 4])
    #[1, 2, 3, 4, 5]
    
    print sorted({3: 'D', 2: 'B', 1: 'B', 5: 'E', 4: 'A'})
    #[1, 2, 3, 4, 5], the sorted key set
    
def useKey():
    #raw type
    print 1, sorted("This is a test string from Andrew".split(), key = str.lower)
    #['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
    
    #tuple, list
    print 2, sorted(student_tuples, key = lambda student: student[2])   # sort by age
    #[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
    
    #object
    print 3, sorted(student_objects, key = lambda student: student.age)   # sort by age
    #[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
    print 4, sorted(student_objects, key = lambda student: student.age, reverse = True)
    #[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    
    #itemgetter
    print 5, sorted(student_tuples, key = itemgetter(1))   # sort by grade
    #[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    
    #itemgetter
    print 6, sorted(student_tuples, key = itemgetter(1, 2))   # sort by grade and age
    #[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
    
    #itemgetter
    print 7, sorted(student_objects, key = attrgetter('grade'))   # sort by grade
    #[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    
    #itemgetter
    print 8, sorted(student_objects, key = attrgetter('grade', 'age'))   # sort by grade and age
    #[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
    



base()
#useKey()

