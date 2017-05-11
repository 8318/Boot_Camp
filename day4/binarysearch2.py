def BinarySearch(the_list, item_to_search):
    start_position=0 #initiate the position the binary search will start
    last_position=len(the_list)-1 #initiate the last position of the binary search
    found=False #initialize the status to know if the item has been found or not
    while start_position<=last_position and notfound: #check the status and ensure there are items 
        midpoint=(start_position+last)//2 #divide the search load into half
        if the_list[midpoint]==item_to_search: 
            found=True
        else:
            if item_to_search<the_list[midpoint]:#check lower half
                last_position=midpoint-1
            else:
                start_position=midpoint+1 #check upper half
        return found
