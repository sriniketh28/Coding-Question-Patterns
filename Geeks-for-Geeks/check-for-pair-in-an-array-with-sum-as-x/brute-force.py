def two_numbers_of_array(arr, x):
    ans = []
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==x:
                # temp to store two or three possiblities like in this case two_numbers_of_array([0, -1, 2, -3, 1,-4],-2) output is [[2, -4], [-3, 1]]
                temp = []
                temp.append(arr[i])
                temp.append(arr[j])
                ans.append(temp)
                break
    
    if len(ans)>0:
        print(ans)
    else:
        print(-1)    

              

