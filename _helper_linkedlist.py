
def createLinkedList(input_arr):
    if len(input_arr) < 1:
        return None
    first_node = ListNode(input_arr[0])
    other_node = first_node
    for k, v in enumerate(input_arr[1:]):
        other_node.next = ListNode(v)
        other_node = other_node.next

    return first_node

def convertFromLinkedList(head: Optional[ListNode]) -> List[str]:
    if not head:
        return []
    output = [head.val]
    while head.next != None:
        head = head.next
        output.append(head.val)

    return output