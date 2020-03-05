# 调用文本
import car_two
# 无限循环体
while True:

    #  (李明)  显示功能菜单
    car_two.kanp_car()

    # 设计功能菜单栏
    my_str = input('请选择希望执行的操作：')
    print('你选择的操作是【 %s 】'% my_str )
    if my_str in ['1', '2', '3']:

        if my_str == '1':
            car_two.new_car()

        elif my_str == '2':
            car_two.all_car()

        elif my_str == '3':
            car_two.cha_car()

    elif my_str == '0' :

        print('欢迎再次使用【名片管理系统】')

        break

    else:
        print('你输入的不正确，请重新选择')