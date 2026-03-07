class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # If the input node is null, return null
        if not node:
            return None
        
        # Hash map to store {old_node: new_node}
        old_to_new = {}
        
        def dfs(curr_node):
            # If we already cloned this node, return the clone
            if curr_node in old_to_new:
                return old_to_new[curr_node]
            
            # Create the clone (without neighbors for now)
            copy = Node(curr_node.val)
            old_to_new[curr_node] = copy
            
