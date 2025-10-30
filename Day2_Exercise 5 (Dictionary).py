employees=[
    {"id":1,"name":"Jane","dept":"HR"},
    {"id":2,"name":"Mark","dept":"IT"},
    {"id":3,"name":"Sue","dept":"HR"}
]

for person in employees:
    if person["dept"]=="HR":
        print(person["name"])