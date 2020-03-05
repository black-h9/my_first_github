# 建立一个空的列表
car_list =[]
# 建立一个函数， 名为 菜单栏
def kanp_car():

    # 设计菜单栏
    """
    1.第一行为 50 个 * ；
    2.最后一行为 50 个 * ；
    3.菜单栏有
    【新增名片】 【显示名片】【搜索名片】 【退出系统】
    4.建立一个用户登录语
    5.建立一个用户退出语

    """

    print('*' * 50)
    print('欢迎使用【名片管理系统】')
    print('')
    print('1. 新增名片')
    print('2. 显示全部')
    print('3. 搜索名片')
    print('')
    print('0. 退出系统')
    print('*' * 50)

# 建立一个函数，名为 新增名片
def new_car():

    print('-' * 50)
    # 显示新增名片
    print('新增名片')
    # 建立名片信息项目  列如：个人的名字 电话号码  微信 QQ 邮箱 工作  兴趣
    name_str = input('请输入姓名： ')
    haoma_str = input('请输入电话号码： ')
    QQ_str = input('请输入QQ： ')
    youjie_str = input('请输入邮件： ')

    # 建立名片字典或集合
    car_key = { 'name' : name_str,
                'haoma': haoma_str,
                'QQ': QQ_str,
                'youjie': youjie_str
                }
    # 字典添加到空的列表中
    car_list.append(car_key)
    # 显示列表 并且添加成功
    print(car_list)
    print('添加 %s 的名片成功' % name_str)

# 建立一个函数，名为 显示所有名片
def all_car():

    print('-' * 50)
    # 显示所有名片
    print('显示所有名片')
    # 判断列表中是否有名片
    if len(car_list) == 0:
        # 如果没有名片  提示用户请添加名片
        print('当前没有任何名片，请添加名片')
        # 当return 后面没有内容时，不会执行下面的代码
        return
    # 设计表头
    for name in ['姓名', '电话', 'QQ', '邮件']:
        # 设计表头的空格 注意：print('')
        #                    print('') 的两个用法
        print(name, end='\t\t')
    print('')
    print('=' * 50)

    # 如果列表中有名片  请显示所有名片
    for car_key in car_list:
        print('%s\t\t%s\t\t%s\t\t%s' %(car_key['name'],
                                       car_key['haoma'],
                                       car_key['QQ'],
                                       car_key['youjie']))

# 建立一个函数，名为 搜索名片
def cha_car():

    print('-' * 50)
    # 显示搜索名片
    print('搜索名片')
    # 提示用户输入名片
    find_name = input('请输入用搜索的姓名：')

    # 判断用户输入的名片是否存在
    for car_key in car_list:
        # 如果用户输入的名片存在列表中
        if car_key['name'] == find_name:
            # 显示名片的表头
            print('姓名\t\t电话\t\tQQ\t\t邮件')
            print('= ' * 50)
            # 输出用户输入搜索的名片信息
            print('%s\t\t%s\t\t%s\t\t%s' % (car_key['name'],
                                            car_key['haoma'],
                                            car_key['QQ'],
                                            car_key['youjie']))

            #   修改 删除名片
            # 建立的修改 删除函数这这提取用户修改 删除的名片
            chu_car(car_key)
            # 如果用户输入的名片存在，则停止执行下面的代码
            break
    # 如果用户输入的名片不存在，则提示用户名片不存在
    else:
        print('抱歉，没有找到 %s '%find_name)

#建立一个函数， 名为 删除 修改名片
def chu_car(find_name):
    # 在搜索中找到用户修改 删除的名片 并且显示
    print(find_name)

    # 提示用户修改 删除 返回上级菜单做一个菜单栏
    xiu_car = input('请选择要执行的操作：'
                    '[1]修改  [2]删除  [0]返回上级菜单')

    # 当用户输入修改时
    if xiu_car == '1':

        # 显示用户输入的名片进行修改
        find_name['name'] = input_car(find_name['name'],'名字: ')
        find_name['haoma'] = input_car(find_name['haoma'] ,'电话号码: ')
        find_name['QQ'] = input_car(find_name['QQ'] ,'QQ: ')
        find_name['youjie'] = input_car(find_name['youjie'],'邮件: ')

        # 提示用户修改名片成功
        print('修改名片成功！')

    # 当用户输入删除时
    elif xiu_car == '2' :

        # 直接在列表中找到用户输入的名片 并且删除
        car_list.remove(find_name)
        # 提示用户删除成功
        print('删除名片成功！')


# 建立一个函数， 名为 在修改时，按回车键无修改效果
def input_car(num,mun):
    """
    输入名片信息


    :param num: 字典中原有的值
    :param mun:输入的提示文字
    :return:如果用户输入了内容，就返回内容，否则，就返回字典中原有的值
    """
    #
    result_str = input(mun)

    # 判断用户是否输入内容
    # 如果用户输入内容
    if len(result_str) > 0:

        # 则返回输入的内容
        return result_str

    # 如果用户没有输入内容
    else:

        # 则返回当前值
        return num





