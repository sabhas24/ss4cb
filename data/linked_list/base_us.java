class LinkedList {

    private static class ListNode {
        int nodeValue;
        ListNode nextNode;

        ListNode(int nodeValue) {
            this.nodeValue = nodeValue;
            this.nextNode = null;
        }
    }

    private ListNode headNode;

    /** Inserts a new node with value at the end of the list */
    public void insertAtEnd(int newValue) {
        ListNode newNode = new ListNode(newValue);
        if (headNode == null) {
            headNode = newNode;
            return;
        }
        ListNode currentNode = headNode;
        while (currentNode.nextNode != null) {
            currentNode = currentNode.nextNode;
        }
        currentNode.nextNode = newNode;
    }

    /** Deletes the first node found with the given targetValue */
    public void deleteByValue(int targetValue) {
        if (headNode == null)
            return;
        if (headNode.nodeValue == targetValue) {
            headNode = headNode.nextNode;
            return;
        }
        ListNode currentNode = headNode;
        while (currentNode.nextNode != null) {
            if (currentNode.nextNode.nodeValue == targetValue) {
                currentNode.nextNode = currentNode.nextNode.nextNode;
                return;
            }
            currentNode = currentNode.nextNode;
        }
    }

    /** Prints all node values from head to tail */
    public void printList() {
        ListNode currentNode = headNode;
        while (currentNode != null) {
            System.out.print(currentNode.nodeValue + " -> ");
            currentNode = currentNode.nextNode;
        }
        System.out.println("null");
    }
}
