# 数据结构(Python语言描述) 阅读记录

## 二叉树

binary_tree.py

```python
from binary_tree import Tree
from binary_tree import pre_order_recursive, post_order_recursive, in_order_recursive

t = Tree()

# 顺序生成一个二叉树，
t.p_add([1,2,3,4,5,6,7,8,9,10])

# 先序
x = pre_order_recursive(t)

# 中序
y = in_order_recursive(t)

# 后序
z = post_order_recursive(t)
```
