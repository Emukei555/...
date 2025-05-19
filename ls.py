inventory = {
    "りんご": 30,
    "バナナ": 45,
    "オレンジ": 20
}

# 在庫の確認関数
def check_inventory():
    print("在庫の確認")
    for fruit, quantity in inventory.items():
        print(f"{fruit}の在庫は{quantity}個です。")

# 在庫の追加関数
def add_inventory():
    print("在庫の追加")
    item = input("追加する果物の名前を入力してください: ")
    quantity = int(input("追加する数量を入力してください: "))
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"{item}の在庫は{inventory[item]}個です。")

# 在庫の削除関数
def remove_inventory():
    print("在庫の削除")
    item = input("削除する果物の名前を入力してください: ")
    if item in inventory:
        del inventory[item]
        print(f"{item}を削除しました。")
    else:
        print(f"{item}は在庫にありません。")

# メイン処理
while True:
    print("\n1: 在庫の確認\n2: 在庫の追加\n3: 在庫の削除\n4: 終了")
    choice = input("操作を選んでください (1-4): ")
    if choice == "1":
        check_inventory()
    elif choice == "2":
        add_inventory()
    elif choice == "3":
        remove_inventory()
    elif choice == "4":
        print("終了します。")
        break
    else:
        print("無効な選択です。もう一度入力してください。")
