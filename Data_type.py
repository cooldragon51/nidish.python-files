name = input("Enter your name: ")
gadget = input("Enter your favorite gadget: ")

agent_number = 9
speed_rating = 15.5
mission_count = 15
height = 1.45
is_active = True
print("Name:",name, "Data type of name is",type(name))
print("Gadget:",name,"Data type of gadget is",type(gadget))
print("Agent number:",agent_number,"Data type of agent_number is",type(agent_number))
print("Speed rating:",speed_rating,"Data type of speed_rating is",type(speed_rating))
print("Mission count:",mission_count,"Data type of mission_count is",type(mission_count))
print("Height:",height,"Data type of height is",type(height))
print("Is active:",is_active,"Data type of is_active",type(is_active))
agent_number_text = float(agent_number)
speed_rating_text = int(speed_rating)
mission_count_text = bool(mission_count)
height_text = str(height)
print("Agent number:",agent_number_text,"Data type of agent_number_text is",type(agent_number_text))
print("Speed rating:",speed_rating_text,"Data type of speed_rating_text is",type(speed_rating_text))
print("Mission count:",mission_count_text,"Data type of mission_count_text is",type(mission_count_text))
print("Height:",height_text,"Data type of height_text is",type(height_text))
a = "hello"
print(a[::-3])