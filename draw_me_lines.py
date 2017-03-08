import simplegui

start_point = [0,0]
end_point = [0,0]

def draw(canvas):
    canvas.draw_line(
        start_point, end_point, 12, 'blue'
    )
    
def start_point_handler(start_point):
    pass

def end_point_handler(start_point):
    pass
    
    
frame = simplegui.create_frame("Home", 500, 500)
start_input_box = frame.add_input("start_point", start_point_handler, 60)
end_input_box = frame.add_input("end_point", end_point_handler, 60)
frame.set_draw_handler(draw)

def split_string_to_list(end_point):
    no_parens_start_point = end_point.replace("(","").replace(")", "")
    split_start_point = no_parens_start_point.split(',')
    
    end_point = []
    for el in split_start_point:
        end_point.append(int(el))

    return end_point
    
def draw_the_line():
    global start_point, end_point
    start_point = split_string_to_list(start_input_box.get_text())
    end_point = split_string_to_list(end_input_box.get_text())
    #print start_input_box.get_text(), end_input_box.get_text()
    #start_point = (1,3)
    #end_point = (100,200)
frame.add_button("draw the line", draw_the_line, 100)

# Start the frame animation
frame.start()
