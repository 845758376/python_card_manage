def cards_dis():
   """显示菜单"""
   print("*" *20)
   print("\t欢迎使用【名片管理系统 V1.0】\n"
      "\t\t\t1. 新建名片\n" "\t\t\t2. 显示全部\n" "\t\t\t3. 查询名片\n\n" "\t\t\t0. 退出系统")
   print("*" *20)
cards_list = []
def cards_add ():
   """新增名片"""
   print("-" * 20 )
   print("新增名片")
   """输入-整理成字典-将字典存储到列表中-提示输入成功"""
   name_str = input("请输入姓名：")
   gender_str = input("请输入QQ：")
   tel_int = input("请输入电话：")
   add_str = input("请输入邮件：")
   cards_dict = {"name" : name_str,
              "gender" : gender_str,
              "telephone" : tel_int,
              "address" : add_str}
   cards_list.append(cards_dict)
   print(cards_list)
   print("%s 的名片新增成功！" % name_str)


def cards_show_all ():
   """显示全部名片"""
   print("- " *20)
   print("显示所有名片")
   if len(cards_list) == 0:
      print("当前系统中没有名片，请新增名片！")
   else:
      print("=" *40)
      #print("姓名\t\t" "QQ\t\t" "电话\t\t" "邮件")
      for name in ("姓名","QQ","电话","邮件"):
         print(name, end="\t\t")
      print(" ")
      for cards_dict in cards_list:
         print("%s\t\t%s\t\t%s\t\t%s" % (cards_dict["name"],
                                 cards_dict["gender"],
                                 cards_dict["telephone"],
                                 cards_dict["address"]))
        #  print(cards_dict)
      print("=" * 40)
def cards_requ ():
   """查询名片"""
   print("- " *20)
   print("查询名片")
   find_name = input("请输入要搜索的姓名:")
   if len(cards_list) == 0:
      print("抱歉！没找到用户 %s 的信息, 请新增！" % find_name)
   else:
      for search_name in cards_list:
         if search_name["name"] == find_name:
            print("找到 %s 的信息了。" % find_name)
            print("=" *40)
            for name in ("姓名", "QQ", "电话", "邮件"):
               print(name, end="\t\t")
            print(" ")
            print("%s\t\t%s\t\t%s\t\t%s" % (search_name["name"],
                                    search_name["gender"],
                                    search_name["telephone"],
                                    search_name["address"]))
            print("=" * 40)
            cards_deal(search_name)
            break
         else:
            print("抱歉！没找到用户 %s 的信息。" % find_name)
def cards_deal(find_dict):
   """修改和删除名片"""
   deal_cards = input("请选择要进行的操作: [1] 删除\t\t[2] 修改\t\t[3] 返回主菜单\n")
   if deal_cards in ["1","2","3"]:
      if deal_cards == "1":
         cards_list.remove(find_dict)
         print("删除用户 %s 名片成功！" % (find_dict["name"]))
      if deal_cards == "2":
         find_dict["name"] = cards_mod(find_dict["name"], "请输入修改后的姓名：")
         find_dict["gender"] = cards_mod(find_dict["gender"], "请输入修改后的QQ：")
         find_dict["telephone"] = cards_mod(find_dict["telephone"], "请输入修改后的电话：")
         find_dict["address"] = cards_mod(find_dict["address"], "请输入修改后的邮件：")
         print("用户 %s 的名片修改成功！" % find_dict["name"])
   else:
         print("输入错误，请重新输入!")
def cards_mod(cards_value, cards_new):
   result = input(cards_new)
   if len(result) > 0:
      return result
   else:
      return cards_value