while True:
    try:
        print('让我们来算算2026被各种数除的结果吧！')
        user_input = input("请输入一个数用来除2026(输入esc退出):")
        if user_input.lower() == "esc":
            print("欢迎下次使用")
            break
        print(f"计算结果：{2026 / int(user_input)}")
    except ZeroDivisionError as e:
        print('不能用零除')
    except ValueError as e:
        print("你输入的不是数字")
    else:
        print("运行正常")
    finally:
        print("本次运行完毕")