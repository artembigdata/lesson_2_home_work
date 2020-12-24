month = int(input("введите интересующий вас месяц года от 1 до 12: "))

month_dict = {1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june", 7: "july",
              8: "august", 9: "september", 10: "october", 11: "november", 12: "december"}

month_list = ["january", "february", "march", "april", "may", "june", "july",
              "august", "september", "october", "november", "december"]
if month in month_dict:
    print(f"{month}-й месяц года - это {month_dict[month]}")
    print(f"{month}-й месяц года - это {month_list[month - 1]}")

else:
    print("wrong number")
    