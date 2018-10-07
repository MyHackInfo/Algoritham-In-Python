''' ######## Linked Lists #############
@Linked Lists@:-> Linked lists are composed of nodes and references/pointers pointing
                   form one node to the other!!!
                -> The last reference is pointing to a NULL!
                -> Each node is composed of a data and a reference/link to the
                     next node in the sequence
                -> Simple and very common data structure!!
                -> They can be used to implement several other common data
                    types: stacks,queues
                -> Simple linked lists by themselves do not allow random access to
                    the data // so we can not use indexes .. getltem(int index)!!!
                -> Many basic operations such as obtaining the last node of the list or
                    finding a node that contains a given data or locating the place where a
                    a new node should be inserted -- require sequential scanning of most or
                    all of the list emlememts!

@Advantages@:->
        <>Linked list are dynamic data strutures(arrays are not!!).
        <>It can allocate the needed memory in run-time.
        <>Very efficient if we want to manipulate the first elememets.
        <>Easy implementation.
        <>Can store items with different sizes: an array assumes every element
            to be exactly the same.
        <>It's easier for a linked list to grow organically.An array;s size needs to
            be known ahead of time,or re-created when it needs to grow.

@Disadvantages@:->
        <>Waste memory because of the references
        <>Nodes in a linked list must be read in order in order form the beginning as
            linked lists have sequential access.
        <>Difficulties arise in linked lists when it comes to reverse traversing.
            single lined lists are extremely difficult to navigate backwards.
        <>Solution: doubly lined lists-> easier to read,but memory is wasted in
            allocating space for a back pointer

@Single Node@:->
             @->contains data->integer,double or custom object
             @->contains a regerence pointing to the next node in the linked list

    class Node{

            data
            Node nextNode

            ...
        }









'''
