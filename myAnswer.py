
def add_time(start, duration, day=""):

    Hour_of_Start = start.split(":")[0]
    Minutes_AMPM = start.split(":")[1]
    Minutes_of_Start = Minutes_AMPM.split(" ")[0]
    AMPM = Minutes_AMPM.split(" ")[1]

    Hour_of_duration = duration.split(":")[0]
    Minutes_of_duration = duration.split(":")[1]
    
    #print(type(Hour_of_duration))

    the_day= ""
    
    find_index=0
    
    count = int(Hour_of_duration) //24
    
    if int(Hour_of_duration) //24 == 1 :
        the_day = " (next day)"
        
        Hour_of_duration = 0
        find_index+=1
    elif int(Hour_of_duration) //24 >1 :
        count +=1
        the_day = " ("+str(count)+" days later)"
    
        
    Hour = int(Hour_of_Start) + int(Hour_of_duration)
    
    Minutes = int(Minutes_of_Start) + int(Minutes_of_duration)
    
    if Minutes >=60:
        Hour+=1
        Minutes-=60
        if Hour == 12 and count == 1:
             the_day = " ("+str(count + 1)+" days later)"
            

    if Hour > 12 and AMPM == "PM":
        AMPM = "AM"
        Hour = Hour - 24 * count
        if count == 0:
            Hour-=12
            the_day = " (next day)"
        #the_day = " (next day)" #changed
    elif Hour > 12 and AMPM == "AM":
        AMPM = "PM"
        Hour-= 12 * count
        if count == 0:
            Hour-=12
    elif Hour == 12:
        if AMPM =="AM":
            AMPM="PM"
        else:
            AMPM="AM"
            
            #the_day = " (next day)" #changed
    
    Day_of_The_Week = ["Monday","Tuesday","Wednesday",
                       "Thursday","Friday","Saturday","Sunday"]

    if the_day == " (next day)":
        find_index -=1
    if len(day) >=1:
        day = day.capitalize()
        find_index += Day_of_The_Week.index(day)
        if count > 1:
            if count >7:
                count%=7
                total_index = find_index+count
                if total_index >6:
                    total_index-=7
            day = Day_of_The_Week[total_index]
            day = ", "+ day 
        elif count == 1:
            total_index = find_index+count
            if total_index >6:
                    total_index-=7
            day = Day_of_The_Week[total_index]
            day = ", "+ day 
        else: 
            day = ", "+ day 

    Minutes = str(Minutes)
    
    if len(Minutes) == 1:
        Minutes = Minutes.zfill(2)
        
        
    Hour = abs(Hour)
    clock = str(Hour) + ":" + (Minutes) + " " + AMPM + day + the_day
    return clock
    
print(add_time("5:30 PM", "242:30"))
      
      
#add_time("11:59 PM", "24:05", "Wednesday")