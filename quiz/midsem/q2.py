import math
import operator

def sort_dict(student_data):
    return sorted(student_data.items, key=student_data.get,
            reverse=True)

def compute_derivative(f, h):
    return lambda x: (f(x+h)-f(x))/h

def compute_integral(f, a, b, n):
    delta = (b-a)*1.0/n
    sum = 0
    for i in range(0, n):
        sum += f(a + i * delta)
    sum *= delta
    return sum

def word_frequency(s,n):
    words = s.split(' ')
    lst = {}
    for word in words:
        if word in lst:
            lst[word] += 1
        else:
            lst[word] = 1
    sorted_list = sorted(lst, key=lst.get, reverse=True)
    sorted_dict = [(key, lst[key]) for key in sorted_list]
    cmp = lambda x,y: 1 if x[1] > y[1] else 1 if x[1] == y[1] and x[0] < y[0]  else -1
    sorted_dict.sort(cmp, reverse = True)
    counter = 1
    for i in range(1, len(sorted_dict)):
        if sorted_dict[i][1] != sorted_dict[i-1][1]:
            counter += 1
        if counter > n:
            i -= 1
            break
    return sorted_dict[:i+1]

student_data = [{"name": "a", "rollno": 3}, {"name": "b", "rollno":
    2}, {"name": "c", "rollno": 1}]

# print(student_data)

# print(compute_derivative(lambda x: x**2, .05)(1))

# print(compute_integral(lambda x: 3*x**2, 0, 1, 100))

s = "the the the quick quick brown brown brown brown fox jumps jumps over"
# print(word_frequency(s, 1), [("brown", 4)])
# print(word_frequency(s, 2), [("brown", 4), ("the",3)])
print(word_frequency(s, 4), [("brown", 4), ("the", 3), ("jumps", 2), ("quick", 2), ("fox", 1), ("over", 1)])
