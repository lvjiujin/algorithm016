##  高级动态规划、字符串算法

[不同路径ii](https://leetcode-cn.com/problems/unique-paths-ii/)的状态转移方程如下：


$$
d p[i][j]=\left\{\begin{array}{ll}
d p[i-1, j]+d p[i, j-1] & (i, j) \text { 上无障碍物 } \\
0 & (i, j) \text { 上有障碍物 }
\end{array}\right.
$$
后续待补充：







### reference

1. https://www.mathsisfun.com/pascals-triangle.html