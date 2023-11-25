## python字典的添加与常用方法

1. #### 使用字典的`key`来添加元素，如果该`key`不存在，则会创建一个新的键值对；如果该`key`已经存在，则会更新该`key`对应的值。

   ```python
   # 添加元素
my_dict = {'name': 'Tom', 'age': 18}
my_dict['gender'] = 'male'  # 添加新元素
my_dict['age'] = 20  # 修改已有元素
print(my_dict)  # {'name': 'Tom', 'age': 20, 'gender': 'male'}
   ```

   

2. #### 使用`update()`方法：使用`update()`方法可以一次性添加多个元素，如果该`key`已经存在，则会更新该`key`对应的值。
```python
 
# 使用update()方法添加元素
my_dict = {'name': 'Tom', 'age': 18}
my_dict.update({'gender': 'male', 'age': 20})  # 添加新元素和修改已有元素
print(my_dict)  # {'name': 'Tom', 'age': 20, 'gender': 'male'}
```
3. #### 字典的其他使用方法

   1. ==clear()：清空字典中的所有元素。==
   2. copy()：返回一个字典的浅拷贝。
   3. fromkeys(seq[, value])：创建一个新字典，以序列seq中的元素作为字典的键，value为字典所有键对应的初始值。
   4. ==get(key[, default])：返回字典中key对应的值，如果key不存在，则返回default值。==
   5. ==items()：返回一个包含字典所有键值对的元组列表。==
   6. keys()：返回一个包含字典所有键的列表。
   7. ==pop(key[, default])：删除字典中key对应的键值对，并返回该键对应的值。如果key不存在，则返回default值。==
   8. popitem()：随机删除并返回字典中的一对键值对。
   9. setdefault(key[, default])：返回字典中key对应的值，如果key不存在，则将key和default值插入到字典中。
   10. update([other])：将其他字典或键值对更新到当前字典中。
   11. ==values()：返回一个包含字典所有值的列表。==