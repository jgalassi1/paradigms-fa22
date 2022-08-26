def tree_to_text(tree, root_node):
    # text to keep track of in order notation
    text = ""
    # push root_node to stack
    stack = [root_node]
    # run until stack is empty
    while stack:
        # peek into stack
        current_node = stack[len(stack)-1]
        if tree[current_node]:
            # peek
            current_node = tree[current_node][0]
            # push onto stack
            stack.append(current_node)
        else:
            # add to final string
            text += stack.pop(len(stack)-1).split("_",1)[1]
            # check to make sure stack isn't empty
            if stack:
                # peek
                current_node = stack.pop(len(stack)-1)
                #add to string
                text += current_node.split("_",1)[1]
                # peek
                current_node = tree[current_node][1]
                # push
                stack.append(current_node)
    return text
