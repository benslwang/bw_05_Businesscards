import bw_02_cards_tools

# 无限循环，由用户主动决定什么时候退出循环！
while True:

    # 显示功能菜单
    bw_02_cards_tools.show_menu()

    """
    在#后面跟上TODO，用于标记需要去做的事情
    # TODO（作者/邮件） 需要去做的事情备注
    """
    action_str = input("请输入希望执行的操作：")
    print("您选择的操作是 【%s】" % action_str)

    # 1,2,3是针对名片的操作
    if action_str in ["1", "2", "3"]:

        # 新增名片
        if action_str == "1":
            bw_02_cards_tools.new_card()

        # 显示全部
        elif action_str == "2":
            bw_02_cards_tools.show_all()

        # 查询名片
        elif action_str == "3":
            bw_02_cards_tools.search_card()

    # 0是退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break
    # 其他内容：输入错误，需要提醒用户
    else:
        print('您输入的内容不正确，请重新输入')

"""
如果在开发程序时，不希望立刻编写分支内部的代码
可以使用pass关键字，表示一个占位符，能够保证程序的代码结构正确
程序运行时，pass关键字不会执行任何操作
"""