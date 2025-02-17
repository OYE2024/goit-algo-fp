class Node:
    def __init__(self, data: int = None):
        self.data = data  # Зберігає дані вузла
        self.next = None  # Посилання на наступний вузол


class LinkedList:
    def __init__(self):
        self.head = None  # Початок списку, спочатку пустий

    def insert_at_beginning(self, data):
        new_node = Node(data)  # Створює новий вузол з даними
        # Вказує, що новий вузол має посилатися на поточний головний вузол
        new_node.next = self.head
        self.head = new_node  # Робить новий вузол головним вузлом списку

    def insert_at_end(self, data):
        new_node = Node(data)  # Створює новий вузол з даними
        if self.head is None:  # Якщо список пустий
            self.head = new_node  # Робить новий вузол головним вузлом
        else:
            cur = self.head  # Починає з головного вузла
            while cur.next:  # Проходить до кінця списку
                cur = cur.next
            cur.next = new_node  # Додає новий вузол в кінці списку

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:  # Перевіряє, чи існує попередній вузол
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)  # Створює новий вузол з даними
        # Вказує, що новий вузол має посилатися на вузол після попереднього вузла
        new_node.next = prev_node.next
        prev_node.next = new_node  # Вставляє новий вузол після попереднього вузла

    def delete_node(self, key: int):
        cur = self.head  # Починає з головного вузла
        if cur and cur.data == key:  # Якщо головний вузол містить потрібні дані
            self.head = cur.next  # Робить наступний вузол головним
            cur = None  # Видаляє вузол
            return
        prev = None  # Змінна для зберігання попереднього вузла
        while cur and cur.data != key:  # Проходить список у пошуках потрібних даних
            prev = cur
            cur = cur.next
        if cur is None:  # Якщо вузол з потрібними даними не знайдено
            return
        prev.next = cur.next  # Видаляє вузол з потрібними даними
        cur = None  # Звільняє пам'ять, видаляючи вузол

    def search_element(self, data: int) -> Node | None:
        cur = self.head  # Починає з головного вузла
        while cur:  # Проходить список у пошуках потрібних даних
            if cur.data == data:  # Якщо знайдено потрібні дані
                return cur  # Повертає вузол з потрібними даними
            cur = cur.next
        return None  # Якщо вузол з потрібними даними не знайдено

    def print_list(self):
        current = self.head  # Починає з головного вузла
        while current:  # Проходить весь список
            print(current.data, end=" -> ")  # Виводить дані вузла
            current = current.next  # Переходить до наступного вузла
        print("None")  # Вказує на кінець списку

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        if not head or not head.next:
            return head
        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None
        left_sorted = self._merge_sort(head)
        right_sorted = self._merge_sort(next_to_middle)
        return self.sorted_merge(left_sorted, right_sorted)

    def get_middle(self, head):
        if not head:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def sorted_merge(left, right):
        if not left:
            return right
        if not right:
            return left
        if left.data <= right.data:
            result = left
            result.next = LinkedList.sorted_merge(left.next, right)
        else:
            result = right
            result.next = LinkedList.sorted_merge(left, right.next)
        return result


if __name__ == '__main__':
    llist = LinkedList()
    llist_1 = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(13)
    llist.insert_at_beginning(100)
    llist.insert_at_beginning(-10)
    llist.insert_at_beginning(15)
    llist.print_list()
    llist.reverse()
    llist.print_list()
    llist.merge_sort()
    llist.print_list()

    llist_1.insert_at_beginning(42)
    llist_1.insert_at_beginning(115)
    llist_1.insert_at_beginning(37)
    llist_1.print_list()

    merged_head = LinkedList.sorted_merge(llist.head, llist_1.head)
    merged_list = LinkedList()
    merged_list.head = merged_head
    merged_list.print_list()
