class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path by '/' - this handles multiple slashes automatically
        parts = path.split("/")
        stack = []

        for part in parts:
            if part == "..":
                # Go up one level: pop from stack if it's not empty
                if stack:
                    stack.pop()
            elif part == "." or not part:
                # '.' means current directory, '' means extra slashes; skip both
                continue
            else:
                # It's a valid directory name
                stack.append(part)


        # Join the stack elements with '/' and add the leading '/'
        return "/" + "/".join(stack)