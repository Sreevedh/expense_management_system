students_list = [{"name": "Tom", "country": "india"}, {"name": "Tom", "country": "austrailia"}]

for student in students_list:
       if student["country"]=="india":
           continue
       print(student["name"])
                     
