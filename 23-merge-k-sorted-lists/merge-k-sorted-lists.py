class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None

        def mergeTwo(list1, list2):
            dummy = ListNode(0)
            current = dummy

            while list1 and list2:
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next

                current = current.next

            if list1:
                current.next = list1
            else:
                current.next = list2

            return dummy.next

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None

                merged.append(mergeTwo(list1, list2))

            lists = merged

        return lists[0]