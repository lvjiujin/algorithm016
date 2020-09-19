学习笔记

## 1. 问题解答篇：

#### 1. 关于 HashMap 的小总结



#### 2. 树的面试题解法一般都是递归，为什么？

因为树的结构是非线性的，也不是环，也就是说树的各个节点单独来看都是一颗树：左子树，右子树，父节点，也就是最小的重复单元，递归三要素：1. 终止条件，2.返回值，3.最小重复单元(也就是每个重复单元干的事情) 中非常关键的一点就是重复性。树的结构决定了它满足这种重复性，所以树的面试题目一般都是递归。

树的实例代码，要滚瓜烂熟。

Linked List是特殊化的 Tree（线性树），Tree是特殊化的 Graph(没有环)。

```python
# python code
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

```c++
struct TreeNode{
    int val;
    TreeNode * left;
    TreeeNode * right;
    // construct function
    TreeNode(int x): val(x), left(NULL), right(NULL) {}
}
`
```

```java
//java code
public class TreeNode{
    public int val;
    public TreeNode left, right;
    public TreeNode(int val){
        this.val = val;
        this.left = null;
        this.right = null;
    }
}
```

二叉树遍历 Pre order/In order/Post order (关键术语的英文名称一定要懂，否则面试的时候可能蒙圈)

1. 前序(pre order) 根-左-右

2. 中序(in order) 左-根-右

3. 后序(post order) 左-右-根

   注意：上述三种情况 都是先左后右的相对顺序。

```python
# 实例代码:
def preorder(self, root):
    if root:
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
def inorder(self, root):
    if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)
def preorder(self,root):
    if root:
        self.preorder(root.left)
        self.preorder(root.right)
        self.traverse_path.append(root.val)
```

