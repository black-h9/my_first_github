#建立一个空列表
list = []

# 建立一个函数 界面
def student_inter():

    print("-" * 75)
    print("【欢迎使用学生管理系统】")
    print("")
    print("1.【新建学生信息】")
    print("2.【显示全部信息】")
    print("3.【查询学生信息】")
    print("4.【删除学生信息】")
    print("5.【修改学生信息】")
    print("0.【退出学生管理系统】")
    print("")
    print("-" * 75)

# 建立一个函数   新建学生信息
def student_new():
    # print("1.学生基本信息 2.学生成绩 0.返回上一级")
    # str_new = input("请你执行的操作：")
    # print("你将要执行的操作是【%s】" % str_new)
    new_name = input("请输入名字：")
    new_age = input("请输入年龄：")
    new_date = input("请输入出生日期：")
    new_phone = input("请输入电话号码：")
    new_email = input("请输入邮箱：")
    new_majir = input("请输入专业：")
    new_china = input("请输入语文成绩：")
    new_math = input("请输入数学成绩：")
    new_English = input("请输入英语成绩：")

    student_dict = {"name": new_name,
                     "age": new_age,
                     "date": new_date,
                     "phone": new_phone,
                    "email":new_email,
                     "majir": new_majir,
                    "china": new_china,
                    "math": new_math,
                    "English": new_English
                    }

    list.append(student_dict)
    print('添加 %s 的信息成功' % new_name)







# 建立一个函数 显示全部学生信息
def student_all():


    if len(list) == 0:

        print("*" * 75)
        print("当前没有学生信息，请添加学生信息")


        return

    print("*" * 75)
    for student in ["姓名", "年龄", "出生日期", "电话号码", "邮箱"]:


        print(student, end="\t\t\t")
    print("")

    for student_dict in list:
        print("%s\t\t\t%s\t\t\t%s\t\t\t\t%s\t\t\t\t%s" %(student_dict["name"],
                                                     student_dict["age"],
                                                     student_dict["date"],
                                                     student_dict["phone"],
                                                     student_dict["email"]))

    pass
    #     1.学生基本信息
    #     2.学生成绩
    #     3.返回上一级



# 建立一个函数  查询学生信息
def student_query():

    print("*" * 75)
    name_query = input("请输入你查找的名字：")
    print("你将查找的是%s的学生"%name_query)
    print("*" * 75)
    for student_dict in list:
        if student_dict["name"] == name_query:
            print("姓名\t\t\t年龄\t\t\t出生日期\t\t\t\t电话号码\t\t\t\t邮箱")
            print("%s\t\t\t%s\t\t\t%s\t\t\t\t\t%s\t\t\t\t\t%s" %(student_dict["name"],
                                             student_dict["age"],
                                             student_dict["date"],
                                             student_dict["phone"],
                                             student_dict["email"] ))
    pass
    #     1.学生基本信息
    #     2.学生成绩
    #     3.返回上一级





# 建立一个函数  删除学生信息
def student_remove(name_query):


    print(name_query)
    str_remove = input("请你输入你要执行的:1.删除 2.修改")

    if str_remove == "1":
        name_query["name"] = input_remove(name_query["name"], "名字：")
        name_query["age"] = input_remove(name_query["age"], "年龄：")
        name_query["date"] = input_remove(name_query["date", "出生日期："])
        name_query["phone"] = input_remove(name_query["phone"], "电话号码：")
        name_query["email"] = input_remove(name_query["email", "邮箱："])

        print('修改成功！')

    elif str_remove == "2":
        list.remove(name_query)
        print('删除成功！')

    else:
        print("你输入有误")


    pass
    # 添加
    # 修改
    # 删除



#建立一个函数  修改学生信息
def student_amend():
    pass
    #     1.学生基本信息
    #     2.学生成绩
    #     3.返回上一级

def input_remove(num, mun):
    input_str = input(mun)
    if len(input_str) > 0:
        return input_str
    else:
        return  num


