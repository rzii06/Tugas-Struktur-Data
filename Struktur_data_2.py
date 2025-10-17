class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display(self):
        temp = self.head
        data_list = []
        while temp:
            data_list.append(temp.data)
            temp = temp.next
        print(data_list)

    def delete_before(self, key):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        if not temp or not temp.prev:
            print(f"Tidak ada data sebelum {key}")
            return
        node_to_delete = temp.prev
        if node_to_delete.prev:
            node_to_delete.prev.next = temp
            temp.prev = node_to_delete.prev
        else:
            self.head = temp
            temp.prev = None
        print(f"Hapus sebelum {key} → Data {node_to_delete.data} dihapus")

    def delete_after(self, key):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        if not temp or not temp.next:
            print(f"Tidak ada data setelah {key}")
            return
        node_to_delete = temp.next
        temp.next = node_to_delete.next
        if node_to_delete.next:
            node_to_delete.next.prev = temp
        print(f"Hapus setelah {key} → Data {node_to_delete.data} dihapus")

    def insert_at_middle(self, data):
        if not self.head:
            self.head = Node(data)
            return
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        new_node = Node(data)
        new_node.next = slow.next
        if slow.next:
            slow.next.prev = new_node
        slow.next = new_node
        new_node.prev = slow
        print(f"Tambah di tengah → Data {data} ditambahkan")


dll = DoubleLinkedList()

nim = [2, 4, 0, 7, 0, 5, 1, 1, 9]
for i in nim:
    dll.append(i)

print("Data awal:", end=" ")
dll.display()

dll.delete_before(7)
dll.display()

dll.delete_after(0)
dll.display()

dll.insert_at_middle(8)
dll.display()
