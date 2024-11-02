#
# file = open(r'C:\Users\OWNER\Downloads\FLASK\leet\text.txt', encoding='utf-8')
# # print(file.read())
# file.close()
#
#
# with open(r'C:\Users\OWNER\Downloads\FLASK\leet\text.txt', encoding='utf-8') as file:
#     print(file.readline())
#
#
# # with open(r'C:\Users\OWNER\Downloads\FLASK\leet\text.txt', encoding='utf-8') as file:
# #     for line in file:
# #         print(line.strip().upper())
#
#
# # with open("lyric") as file:
# #     lines = file.readlines()
# #     lines.sort()
# #     print(lines)
# #
# #
# # with open("new file", "w") as file:
# #     file.write("KANYEEE")
#
#
# with open("new file", 'a') as file:
#     file.write("\n is good")

#
# guests = open("guests.txt", "w")
# initial_guests = ["tom","Riri","dandan","octavious"]
#
# for guest in initial_guests:
#     guests.write(guest + "\n")
# guests.close()
#
# with open("guests.txt") as file:
#     print(file.read())
#
# new_guests = ["King", "king", "diane", "meliodas"]
# with open("guests.txt", "a") as file:
#     for guest in new_guests:
#         file.write(guest + '\n')
#
# with open("guests.txt") as file:
#     print(file.read())
#
# checked_out = ["King", "tom", "king"]
# temp_list = []
#
# with open("guests.txt", "r") as guests:
#     for guest in guests:
#         temp_list.append(guest.strip())
#
# with open("guests.txt", "w") as guests:
#     for name in temp_list:
#         if name not in checked_out:
#             guests.write(name + "\n")
#
# with open("guests.txt") as guests:
#     print(guests.read())


guests_to_check = ["Riri", "tom"]
checked_in = []
with open("guests.txt") as guests:
    for name in guests:
        checked_in.append(name.strip())
    for name in guests_to_check:
        if name in checked_in:
            print("{} is checked in".format(name))
        else:
            print("{} is not checked in".format(name))




