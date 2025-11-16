def get_rocket_frames():
    
    with open("src/rocket/rocket_frame_1.txt", 'r') as file_1:
        rocket_1 = file_1.read()
            
    with open("src/rocket/rocket_frame_2.txt", 'r') as file_2:
        rocket_2 = file_2.read()
    return rocket_1, rocket_2