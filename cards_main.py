import cards_tools

while True:
   cards_tools.cards_dis()
   cards_input = input("请选择操作功能：")
   if cards_input in ["1", "2", "3"]:
      if cards_input == "1":
         print("- " *20)
         print("您选择输入的操作代码是: 1" )
         cards_tools.cards_add()
      elif cards_input == "2":
         print("- " *20)
         print("您选择输入的操作代码是: 2" )
         cards_tools.cards_show_all()
      elif cards_input == "3":
         print("- " *20)
         print("您选择输入的操作代码是: 3" )
         cards_tools.cards_requ()
   elif cards_input == "0":
      print("您选择输入的操作代码是: 0" )
      print("即将退出系统......\n" "已退出系统，欢迎您下次【名片管理系统】！")
      break
   else:
      cards_input = input("输入错误，请重新输入:")
      cards_tools.cards_dis()
      #cards_input = input("输入错误，请重新输入:")
      while True:
         cards_input = input("输入错误，请重新输入:")
         cards_tools.cards_dis()
         if cards_input in ["1", "2", "3", "0"]:
            if cards_input == "1":
               print("- " *20)
               print("您选择输入的操作代码是: 1")
               cards_tools.cards_add()
               break
            if cards_input == "2":
               print("- " *20)
               print("您选择输入的操作代码是: 2")
               cards_tools.cards_show_all()
               break
            if cards_input == "3":
               print("- " *20)
               print("您选择输入的操作代码是: 3")
               cards_tools.cards_requ()
               break
            else:
            # #print("返回主菜单")
               break
      break