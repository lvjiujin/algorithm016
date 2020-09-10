## 学习总结

基本思想：不要死磕，敢于承认自己不会，第二遍第三遍做不出来正常，说明之前自己认为懂了，可能没有真的懂了。不追求自己一遍理解。

https://www.zhihu.com/question/387295413/answer/1154369980

成年人学习算法有两大常见的误区，1是只看书不动手，2是什么都要追求“理解”。抱着这两种心态的人前赴后继同样的话说多少遍也没有用。
我们每个人都是从小婴儿长大的。想想小婴儿是怎么学习说话的。是从“模仿”开始的。如果每个词每句话都要追求”理解“，那就永远都学不会讲话。
当然，婴儿没有意识，不知道追求理解。但是成年人有意识，学什么都要先理解，只可惜这有时候反而会成为学习的障碍。
对于初学编程的人来说，无论年龄多大、智商多高，在编程语言相关的知识面前，其实依然是婴儿。放低身段，用鹦鹉学舌的姿势，不“理解”别强求，只要能够依葫芦画瓢地去解题、考试，就够了。
至于“理解”，交给时间。

## 一、算法的几个原则：

1. 以空间换时间。
2. 升维（将一维问题转化为二维为题，有点类似SVM 做核映射，将低维的非线性转化为高维的线性问题，又如同多层神经网络能够模拟（无限逼近）任意函数，但是单个感知机就不行，连异或问题就解决不了）
3. 找最近重复子问题（泛化）
4. 一切算法不过是if-else, for/while, recursion
5. 不要人肉递归。从递归的模板上去思考问题。
6. 递归可以加缓存，加快速度@lru_cache, 需要导入包：from functools import lru_cache



### 二、五毒神掌

> 1. 5-10 分钟读题和思考，如果没有思路，看题解，默写背诵代码，熟练掌握代码。
> 2. 马上自己写，提交LeetCode，多种解法，体会优化
> 3. 24 小时之后，再重复做题
> 4. 一周后重复做题
> 5. 面试前一周恢复性训练
>
> ### 切题四件套
>
> 1. 理清题意，确定题目的要求
> 2. 想尽可能多的解法，对比几种写法的时空复杂度，找到比较好的解法
> 3. 尽可能多地动手写
> 4. 测试用例
>
> #### 一维数据结构
>
> 1. 数组 array，查询速度快，时间复杂度O(1)，删除、添加的速度慢，时间复杂度O(n)。
> 2. 链表 linked list，查询速度慢，时间复杂度O(n)；删除、添加的速度快，时间复杂度O(1)。
> 3. 栈 stack, 先进后出 FILO，查询速度为O(n)；删除、添加的速度快，时间复杂度O(1)。
> 4. 队列 queue，先进先出，FIFO，查询速度为O(n)；删除、添加的速度快，时间复杂度O(1)。
> 5. 双端队列 deque, queue 和 stack 的结合体，头和尾都可以进行元素的push和pop，查询速度为O(n)，删除、添加速度为O(1)。
> 6. 集合 set,
> 7. hash表 map, python中对应为dict. 
>
> #### 二维数据结构
>
> 1. 树 tree,
> 2. 图 graph,
> 3. 二叉搜索树 binary search tree,
> 4. 堆 heap,
> 5. 并查集 disjoint set,
> 6. 字典树
>
> #### 特殊数据结构
>
> 1. 位运算 Bitwise,
> 2. 布隆过滤器 Bloom Fiilter,
> 3. LruChache
>
> ## 数组和链表时间复杂度
>
> | 操作    | 数组 | 链表 |
> | ------- | ---- | ---- |
> | prepend | o(1) | o(1) |
> | append  | o(1) | o(1) |
> | lookup  | o(1) | o(n) |
> | insert  | o(n) | o(1) |
> | delete  | o(n) | o(1) |
>
> ##### 1.1 数组
>
> 连续内存块，在插入，删除过程中需要移动对应位置的后面所有元素，具有o(n)复杂度。在对应位置查找中具有o(1)复杂度。
>
> 在高级语言中的数组，一般至少含有原始数组及size及cap三个成员变量，当size==cap后继续append，需要分配更大的连续内存存放数据 以及复制原有数据到新的内存空间中再继续后续的append操作，意味着数组初始化容量太小，会有多次扩容复制以及内存垃圾的产生，因此 尽量在使用的过程中确定数组的size范围来初始化数组
>
> 数组相较链表，内存位置连续，这样更有可能利用上cpu cache，例如同样从0->n的遍历，数组要比链表快
>
> 虽然数组具有高速访问数据的特性，但是删除上的性能过低，无法直接用于当做队列结构，可以封装成环来充当队列
>
> #### 1.2 链表
>
> 链表的处理尽量加上哑结点来简化操作。
>
> 主要用到双指针加逼性,链表的递归比较少见，要知道。
>
> #### 1.3 跳表
>
> 跳表主要麻烦在插入，删除节点的处理，处理不好会导致导致高层节点间的元素不均衡，会导致查询时间复杂度退化到o(n)
>
> ### 一些思想
>
> - 写代码要采用自顶向下的编程方式，即先写主干逻辑，再写具体实现；
> - 双指针的算法一般要先进行排序；
> - 一维数据要加速可以通过升维度，如 有序的链表升为跳表；
>
> 
>
> ##  相关题目
>
> ## 简单：
>
> - 用 add first 或 add last 这套新的 API 改写 Deque 的代码
> - 分析 Queue 和 Priority Queue 的源码
>
> - [删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)（Facebook、字节跳动、微软在半年内面试中考过）
> - [旋转数组](https://leetcode-cn.com/problems/rotate-array/)（微软、亚马逊、PayPal 在半年内面试中考过）
> - [合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)（亚马逊、字节跳动在半年内面试常考）
> - [合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)（Facebook 在半年内面试常考）
> - [两数之和](https://leetcode-cn.com/problems/two-sum/)（亚马逊、字节跳动、谷歌、Facebook、苹果、微软在半年内面试中高频常考）
> - [移动零](https://leetcode-cn.com/problems/move-zeroes/)（Facebook、亚马逊、苹果在半年内面试中考过）
> - [加一](https://leetcode-cn.com/problems/plus-one/)（谷歌、字节跳动、Facebook 在半年内面试中考过）
>
> ### 中等：
>
> - [设计循环双端队列](https://leetcode.com/problems/design-circular-deque)（Facebook 在 1 年内面试中考过）
>
> ### 困难：
>
> - [接雨水](https://leetcode.com/problems/trapping-rain-water/)（亚马逊、字节跳动、高盛集团、Facebook 在半年内面试常考）
>
> ## Reference
>
> https://github.com/orcswang-lang/algorithm016/tree/master/Week_01
>
> ## 强烈推荐的一个github 链接
>
> https://github.com/labuladong/fucking-algorithm

