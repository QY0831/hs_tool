import tkinter as tk

def on_submit():
    # key cards cost
    cost = {
        'tourist': 5,
        'call_mgr': 2, 
        'drink': 1,
        'stick': 4,
        'weapon': 6,
    }

    cnt = {
        "tourist": entry1.get(),
        "call_mgr": entry2.get(),
        "drink": entry3.get(),
        "stick": entry4.get(),
        "weapon": entry5.get(),
    } 
    
    for k in cnt:
        try:
            cnt[k] = int(cnt[k])
        except:
            cnt[k] = 0
    
    print(cnt)
    save_power = int(entry6.get())
    tr_on_board = bool_var_0.get()
    weapon_on_board = bool_var_1.get()
    print('tr_on_board: ', tr_on_board)
    print('weapon_on_board: ', weapon_on_board)
    print('save_power: ', save_power)

    total_cost = 0
    

    if not weapon_on_board and cnt['weapon'] > 0:
        weapon_on_board = True 
        total_cost += cost['weapon']
        
    if not tr_on_board and cnt['tourist'] > 0:
        tr_on_board = True
        total_cost += cost['tourist']

    damege = 6 if weapon_on_board else 0
    times = 2 if tr_on_board else 1
    print('damege: ', damege)
    print('times: ', times)

    if cnt['call_mgr'] > 0:
        total_cost += cost['call_mgr'] * cnt['call_mgr'] - cnt['call_mgr'] * times
        mgr_dmg = times * 2 * cnt['call_mgr']
        print("mgr_dmg: ", mgr_dmg)
        damege += mgr_dmg

    if cnt['drink'] > 0:
        total_cost += cost['drink'] * cnt['drink']
        drink_dmg = cnt['drink'] * times - 1
        if weapon_on_board:
            drink_dmg *= 2
        print('drink_dmg: ', drink_dmg)
        damege += drink_dmg

    if cnt['stick'] > 0:
        if cnt['drink'] > 0:
            cost['stick'] = 2 
        stk_dmg = cnt['stick'] * 4 * times
        print('stk_dmg: ', stk_dmg)
        total_cost += cost['stick'] * cnt['stick']
        damege += stk_dmg
        
    total_cost -= save_power

    # 弹出信息框显示结果
    # messagebox.showinfo("Max damage: ", damege, "\nTotal cost: ", total_cost)
    res = f"最高伤害: {damege} 花费: {total_cost}"
    result_label.config(text=res)

root = tk.Tk()
root.title("TK")

tk.Label(root, text="游客").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)
entry1.insert(0, "0")

tk.Label(root, text="叫经理").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)
entry2.insert(0, "0")

tk.Label(root, text="佳酿").grid(row=2, column=0, padx=10, pady=10)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1, padx=10, pady=10)
entry3.insert(0, "0")

tk.Label(root, text="荧光棒").grid(row=3, column=0, padx=10, pady=10)
entry4 = tk.Entry(root)
entry4.grid(row=3, column=1, padx=10, pady=10)
entry4.insert(0, "0")

tk.Label(root, text="风怒刀").grid(row=4, column=0, padx=10, pady=10)
entry5 = tk.Entry(root)
entry5.grid(row=4, column=1, padx=10, pady=10)
entry5.insert(0, "0")

tk.Label(root, text="额外减费").grid(row=5, column=0, padx=10, pady=10)
entry6 = tk.Entry(root)
entry6.grid(row=5, column=1, padx=10, pady=10)
entry6.insert(0, "0")

# 布尔变量
bool_var_0 = tk.BooleanVar()
check_button = tk.Checkbutton(root, text="游客在场", variable=bool_var_0)
check_button.grid(row=6, column=0, padx=10, pady=10)

bool_var_1 = tk.BooleanVar()
check_button = tk.Checkbutton(root, text="刀在手", variable=bool_var_1)
check_button.grid(row=7, column=0, padx=10, pady=10)

# 提交按钮
submit_button = tk.Button(root, text="计算", command=on_submit)
submit_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# 显示结果的标签
result_label = tk.Label(root, text="")
result_label.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# 运行主循环
root.mainloop()
