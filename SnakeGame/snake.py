

class Snake:
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    for seg_num in range(len(segments)-1,0,-1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x,new_y)   
