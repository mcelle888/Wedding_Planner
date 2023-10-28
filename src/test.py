# Calculates and prints scheduled to do list 

import datetime

user_details = [0, 100]
timestamps = [0.1, 0.25, 0.4, 0.6, 0.7, 0.8, 0.9, 1]

tasks = []
for i in timestamps:
    tasks.append(i * round(user_details[1]))

print(tasks)
today = datetime.date.today()

dates = [(today + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in tasks]
 

print(dates)


end_date_one = (today + datetime.timedelta(days=i)).strftime("%Y-%m-%d")
# end_date_two = (today + datetime.timedelta(days=task_two)).strftime("%Y-%m-%d")
# end_date_three = (today + datetime.timedelta(days=task_three)).strftime("%Y-%m-%d")
# end_date_four = (today + datetime.timedelta(days=task_four)).strftime("%Y-%m-%d")
# end_date_five = (today + datetime.timedelta(days=task_five)).strftime("%Y-%m-%d")
# end_date_six = (today + datetime.timedelta(days=task_six)).strftime("%Y-%m-%d")
# end_date_seven = (today + datetime.timedelta(days=task_seven)).strftime("%Y-%m-%d")
# end_date_eight = (today + datetime.timedelta(days = task_eight)).strftime("%Y-%m-%d")

# with open('test.txt', 'a') as f:
#     f.write("\n\n ~ PLANNING CHECKLIST ~\n\n")
#     f.write(end_date_one)
#     f.write("\n")
#     f.write("Start looking for vendors\n\n")
#     f.write(end_date_two)
#     f.write("\n")
#     f.write("Hire/Book all suppliers and vendors\n\n")
#     f.write(end_date_three)
#     f.write("\n")
#     f.write("Send out invitations\n\n")
#     f.write(end_date_four)
#     f.write("\n")
#     f.write("Food Tasting\n")
#     f.write("Call vendors to confirm\n\n")
#     f.write(end_date_five)
#     f.write("\n")
#     f.write("Hair and Makeup Trial\n")
#     f.write("Dress collection and last alterations\n\n")
#     f.write(end_date_six)
#     f.write("\n")
#     f.write("Organise Final payments for vendors\n")
#     f.write("Final guest count and plean table arrangements\n")
#     f.write("Plan accommadation and transport\n\n")
#     f.write(end_date_seven)
#     f.write("\n")
#     f.write("Ceremony and Reception rehearsals\n\n")
#     f.write(end_date_eight)
#     f.write("\n")
#     f.write("D-DAY: GET MARRIED!")
