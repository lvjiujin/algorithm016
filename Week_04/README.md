# DFS BFS 二分查找 贪心法

### 1. DFS 和BFS

#### 1. DFS (depth first search)

二叉树的前序（preorder），中序（inorder），后序（postorder）都是深度优先搜索。

图的DFS是二叉树前序遍历的推广。

DFS 的一个经典例子是 leetcode 200 [岛屿数量问题](https://leetcode-cn.com/problems/number-of-islands/description/) 通过递归一下子将一个岛屿完全解决，然后找下一个岛屿。

当然二叉树最大深度，最小深度，n-叉树的前序遍历，后续遍历等都是DFS的经典题目。

一个是掌握递归的模板，也就是经典做法，另一个掌握二叉树和n叉树遍历的非递归做法（借助栈）

经典代码看过来：https://shimo.im/docs/D68KxVpHjWGdJXk3

而且DFS的过程也体现了回溯的思想。

#### 2. BFS breadth first search

BFS 是层序遍历，很少有递归的，因为不太符合树的递归的条件。

BFS的解题思路是和队列和栈结合起来。

>  保证在循环中，一次循环，插入队列或栈中的node 都是同一层的。这样在获取队列或栈的长度的时候，就可以知道这一层有多少个节点。
>
> 经典的代码链接见石墨文档：https://shimo.im/docs/QH6XrR3hkKQ8Pr9y

### 2. 二分查找

二分查找，就是看起来简单，想起来简单，理解上简单，做起来，不容易做对，不容易做全对，尤其是test case 各种变化的时候。

* 重要的是要掌握各种边界条件，什么时候取等号。
* 二叉搜索树也是一种二分查找的数据结构
* 二叉搜索树和堆的区别与联系。

二分查找的几个经典例子：

[153.寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)

[154.寻找旋转排序数组中的最小值-ii （含重复元素）](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/)

[33.搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)

上述3个题目是有递进关系的，最基础的就是单纯找旋转数组的最小值，然后含有重复元素时，找旋转数组的最小值，最后旋转数组（有重复）中的某一个给定值的目标值。

先来看153.



### 3. 贪心法

### 4. 数学技巧



### 5. reference



最经典的代码就是二叉树和n-叉树的层序遍历。