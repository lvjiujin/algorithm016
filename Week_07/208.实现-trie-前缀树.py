#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
from collections import defaultdict
class TrieNode:
    def __init__(self):
        # dict的value是TireNode对象而不是字符 是关键!
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for s in word:
            node = node.children[s]
        node.is_word = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for s in word:
            if s in node.children:
                node = node.children[s]
            else:
                return False
        return node.is_word


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for s in prefix:
            if s in node.children:
                node = node.children[s]
            else:
                return False
        return True

class Trie2:
    # 这种方法效率比较高
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            
            t = t[c]
        
        t['word'] = word


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.trie
        for c in word:
            if c not in t:
                return False
            
            t = t[c]
        
        return 'word' in t
            

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.trie
        for c in prefix:
            if c not in t:
                return False
            else:
                t = t[c]
        
        return True
# Your Trie object will be instantiated and called as such:
def main():
    obj = Trie()
    words = ['hello', 'height', 'her', 'henan']
    for word in words:
        obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)
    print("obj = ", obj.root.children)

if __name__ == '__main__':
    main()
# @lc code=end

