with open('example.txt', 'r') as file:
    content = file.read()

    word_count = len(content.split())

    line_count = content.count('\n') + 1  # Adding 1 to account for the last line

    print(f"Number of words: {word_count}")
    print(f"Number of lines: {line_count}")# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

