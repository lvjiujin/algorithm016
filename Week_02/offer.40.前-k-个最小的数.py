class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        最小的k个数
        """
        
        # 方法一: 排序法
        # arr.sort()
        # return arr[:k]
        # 方法二：大根堆（大顶堆）
        import heapq
        return heapq.nsmallest(k, arr)
        # if k == 0:
        #     return list()

        # hp = [-x for x in arr[:k]]
        # heapq.heapify(hp)
        # for i in range(k, len(arr)):
        #     if -hp[0] > arr[i]:
        #         heapq.heappop(hp)
        #         heapq.heappush(hp, -arr[i])
        # ans = [-x for x in hp]
        # return ans
        """
        求前k个最小用最大堆，前k个最大用最小堆，这是因为最大堆堆顶值最大，维护一个k大小的最大堆，向堆中添加剩余元素时，比堆顶值小就弹出堆顶，
        并向堆中插入该元素，这样，就保证维护了比堆顶小的k-1 个最小值。反之亦然。时间复杂度O(nlogk)，因为只需维护k大小的堆
        https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/nei-zhi-sort-kuai-pai-si-xiang-zui-da-dui-san-chon/

        """
        # if k == 0:
        #     return []
        # heaplist = HeapList()
        # heaplist.buildHeap(arr[:k])
        # for i in arr[k:]:
        #     if i < heaplist.heaplist[1]:
        #         heaplist.delMax()
        #         heaplist.insert(i)
        # return heaplist.heaplist[1:]

        # 快排的思想:
        """
        若第k小的值出现在左侧(当中值pos - l + 1 > k)，向左递归，出现在右侧(当中值pos - l + 1 < k)，向右递归。
		时间复杂度 最好O(n)，最坏会退化到O(n^2)
        """
        def partition(arr, l, r):
            #选定中值
            pivotvalue = arr[l]
            lmark = l + 1
            rmark = r
            done = False

            while not done:
                while lmark <= rmark and arr[lmark] <= pivotvalue:
                    lmark += 1
                while rmark >= lmark and arr[rmark] >= pivotvalue:
                    rmark -= 1
                if rmark < lmark:
                    done = True
                else:
                    arr[lmark], arr[rmark] = arr[rmark], arr[lmark]

            arr[l], arr[rmark] = arr[rmark], arr[l]
            return rmark
        
        def quicksort(arr, l, r, k):
            if l > r:
                return 
            pos = partition(arr, l, r)
            num = pos - l + 1
            if k == num:
                return
            if k < num:
                quicksort(arr, l, pos - 1, k)
            else:
                quicksort(arr, pos+1, r, k - num)

        if k == 0:
            return []
        quicksort(arr, 0, len(arr) - 1, k)
        return arr[:k]

        

class HeapList():
    """
    大顶堆
    """
    def __init__(self):
        self.heaplist = [0]
        self.size = 0

    def buildHeap(self, alist):
         i = len(alist) // 2
         self.size = len(alist)
         self.heaplist += alist[:]
         while i > 0:
             self.percDown(i)
             i -= 1

    def delMax(self):
        """删除堆顶最大元素"""
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.size]
        self.size -= 1
        self.heaplist.pop()
        self.percDown(1)
        return retval

    def insert(self, k):
        self.heaplist.append(k)
        self.size += 1
        self.percUP(self.size)

    def percUP(self, i):
        while i // 2 > 0:
            if self.heaplist[i] > self.heaplist[i // 2]:
                self.heaplist[i], self.heaplist[i // 2] = self.heaplist[i // 2], self.heaplist[i]
            i //= 2

    def percDown(self, i):
        while i * 2 <= self.size:
            mc = self.maxChild(i)
            if self.heaplist[i] < self.heaplist[mc]:
                self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]
            i = mc

    def maxChild(self, i):
        if 2 * i + 1 > self.size:
            return 2 * i
        else:
            if self.heaplist[2 * i] > self.heaplist[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1

def main():
	solu = Solution()
	arr = [3,2,1]
	k = 2
	res = solu.getLeastNumbers(arr,k)
	print("res = ", res)

if __name__ == '__main__':
	main()