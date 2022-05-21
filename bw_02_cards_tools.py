# 用列表记录所有的名片字典
card_list = []

def show_menu():

    """菜单显示"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】V 1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():

    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1.提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ号码：")
    email_str = input("请输入邮箱地址：")

    # 2.使用用户输入的名片信息建立一个字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    # print(card_list)
    # 4.提示用户添加成功
    print("%s 的名片已添加成功！" % name_str)

def show_all():

    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    # 判断是否有名片记录，如没有，提示用户并且返回
    if len(card_list) == 0:
        print("当前没有任何的名片记录，请使用新增功能添加名片！")
        # return可以返回一个函数的执行结果
        # 下方的代码不会被执行
        # 如果return后面没有任何的内容，表示会返回到调用函数的位置
        # 并且不返回任何的结果
        return

    # 打印表头(遍历列表，以不换行的形式输出，作为表头)
    for title in ["姓名", "电话", "qq", "邮箱"]:
        print(title, end="\t\t")

    print("")

    # 打印分割线
    print("=" * 50)
    # 遍历名片列表依次输出字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
              card_dict["phone"],
              card_dict["qq"],
              card_dict["email"]))
    # 打印分割线
    print("=" * 50)


def search_card():

    """搜索名片"""
    print("-" * 50)
    print("搜索名片")

    # 1.提示用户输入要搜索的姓名
    search_info = input("请输入您要查询的信息：")

    # 2.遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:
        if search_info == card_dict["name"] \
                or search_info == card_dict["phone"] \
                or search_info == card_dict["qq"] \
                or search_info == card_dict["email"]:
            print("姓名\t\t电话\t\tqq\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            # 针对找到的名片记录执行修改和删除的操作
            deal_card(card_dict)

            break
    else:
        print("抱歉，未查询到%s相关的名片信息，请重新输入！" % search_info)


def deal_card(find_dict):
    """对查找到的名片进行修改删除操作
    :param find_dict: 查找到的名片所属字典
    """
    # print(find_dict)
    action_str = input("请选择要执行的操作："
                       "[1] 修改 [2] 删除 [0] 返回上级菜单 ")

    if action_str == "1":
        # 修改名片
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "qq：")
        find_dict["email"] = input_card_info(find_dict["email"], "email：")
        print("修改名片成功！")

    elif action_str == "2":
        # 删除名片
        card_list.remove(find_dict)
        print("删除名片成功！")

    else:
        print("输入错误，请重新查询！")

def input_card_info(dict_value, tip_message):
    """修改名片时，根据用户是否输入内容判断是否更改名片信息
    :param dict_value: 字典中原有的值
    :param tip_message: 输入的提示文字
    :return:如果用户输入了内容，就返回内容，否则返回字典中原有的值
    """

    # 1.提示用户输入内容
    result_str = input(tip_message)

    # 2.针对用户的输入进行判断，如果用户输入内容，直接返回结果
    if len(result_str) > 0:
        return result_str

    # 3.如果用户没有输入内容，返回‘字典中原有的值’
    else:
        return dict_value
