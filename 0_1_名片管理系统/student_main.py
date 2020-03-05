#导入函数
import student_two
#做一个无限循环体
while True:


    student_two.student_inter()

    # 用户选择输入
    str_student = input("请输入你要执行的操作：")
    # 提醒用户你的选择是
    print("你要执行的操作是【%s】" %str_student)
    # 判断
    if str_student in ["1", "2", "3", "4", "5"]:

        # 如果用户选择1
        if str_student == "1":
            student_two.student_new()

        # 如果用户选择2
        elif str_student == "2":
            student_two.student_all()
        # 如果用户选择3
        elif str_student == "3":
            student_two.student_query()
        # 如果用户选择4
        elif str_student == "4":
            student_two.student_remove()
        # 如果用户选择5
        elif str_student == "5":
            student_two.student_amend()
    # 用户退出
    elif str_student == "0":
        print("欢迎再次使用【学生管理系统】")
        break
    # 用户输错
    else:
        print("对不起，你输入的操作有误，请重新核对，谢谢！")