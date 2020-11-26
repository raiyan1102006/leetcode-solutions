# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/


class DLinkedList(object):
        def __init__(self,key=0,val=0,prev_=None,next_=None):
            self.key = key
            self.val = val
            self.prev_ = prev_
            self.next_ = next_
            
class LRUCache:

    def addNode(self, node):
        tempNode = self.head.next_
        self.head.next_ = node
        node.next_ = tempNode
        tempNode.prev_ = node
        node.prev_ = self.head
        
    def move_to_head(self, node):
        #remove first
        p = node.prev_
        x = node.next_ 
        p.next_ = x
        x.prev_ = p
        self.addNode(node)
        
    def removetail(self):
        
        tempNode = self.tail.prev_.prev_
        del self.LRUCache[self.tail.prev_.key]
        self.tail.prev_ = tempNode
        tempNode.next_ = self.tail      
        
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head, self.tail = DLinkedList(),DLinkedList()
        self.head.next_ = self.tail 
        self.tail.prev_ = self.head 
        
        self.LRUCache = {}  
        
    def get(self, key: int) -> int:
        if key in self.LRUCache:
            self.move_to_head(self.LRUCache[key])
            return self.LRUCache[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.LRUCache:
            self.LRUCache[key].val = value
            self.move_to_head(self.LRUCache[key])
        else: #key doesnt exist, add it
            node = DLinkedList(key=key,val=value)
            self.addNode(node)
            self.LRUCache[key] = node
            self.move_to_head(node)
            
            if len(self.LRUCache) > self.capacity:
                self.removetail()
            
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
