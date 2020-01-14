# Q should be an ordered dict with coord and tool key and minutes (steps) value
# hmmmm, maybe not, lets Q up a list of objects, then sort them by minute (steps)



# HOW TO SORT OBJECTS
customObjects = [obj1, obj2, obj3, obj4, obj5]
 
# One line sort function method using an inline lambda function lambda x: x.date
# The value for the key param needs to be a value that identifies the sorting property on the object
customObjects.sort(key=lambda x: x.date, reverse=True)
 
for obj in customObjects:
	print("Sorted Date from obj: " +str(obj.date) + " with title: " +obj.title)





# BFS
BFS (G, s)                   //Where G is the graph and s is the source node
      let Q be queue.
      Q.enqueue( s ) //Inserting s in queue until all its neighbour vertices are marked.

      mark s as visited.
      while ( Q is not empty)
           //Removing that vertex from queue,whose neighbour will be visited now
           v  =  Q.dequeue( )

          //processing all the neighbours of v  
          for all neighbours w of v in Graph G
               if w is not visited 
                        Q.enqueue( w )             //Stores w in Q to further visit its neighbour
                        mark w as visited.