import json

# JSON to Python
'''
x = '{"name":"adity","age":"23","city":"toranto"}'

y = json.loads(x)

print(y['age'])
'''
# Python to JSON
'''
x = {
    'name':'saheb',
    'age':18,
    'city':'toranto'
}

y = json.dumps(x)

print(y)
'''
# Python to JSON
'''
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
'''