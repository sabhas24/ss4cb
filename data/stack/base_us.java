class Stack {
    private int[] elementArray;
    private int topIndex;
    private int stackCapacity;

    /** Initializes a stack with the given capacity */
    public Stack(int stackCapacity) {
        this.stackCapacity = stackCapacity;
        this.elementArray = new int[stackCapacity];
        this.topIndex = -1;
    }

    /** Returns true if the stack has no elements */
    public boolean isEmpty() {
        return topIndex == -1;
    }

    /** Returns true if the stack has reached its capacity */
    public boolean isFull() {
        return topIndex == stackCapacity - 1;
    }

    /** Adds a new element on top of the stack */
    public void push(int newElement) {
        if (isFull()) {
            System.out.println("Stack overflow: cannot push " + newElement);
            return;
        }
        elementArray[++topIndex] = newElement;
    }

    /** Removes and returns the top element of the stack */
    public int pop() {
        if (isEmpty()) {
            System.out.println("Stack underflow: stack is empty");
            return -1;
        }
        return elementArray[topIndex--];
    }

    /** Returns the top element without removing it */
    public int peek() {
        if (isEmpty()) {
            System.out.println("Stack is empty");
            return -1;
        }
        return elementArray[topIndex];
    }
}
