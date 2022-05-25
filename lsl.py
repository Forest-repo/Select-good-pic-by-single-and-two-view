
import tkinter as tk
import os
import shutil
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox


def bt1_hit():
    global source_path, target_path, pic_list, now_num, all_nums, now_img, now_img_name

    now_num = 0

    pic_list = []
    # 这里返回一个目录名 文件选择对话框,    askdirectory	选择目录，并返回目录名
    source_path = filedialog.askdirectory()
    now_class = source_path.split('/')[-1:]
    source_path_Text.delete(1.0, "end")
    source_path_Text.insert(1.0, source_path)
    for pic_name in sorted(os.listdir(source_path)):
        pic_list.append(pic_name)
    all_nums = len(pic_list)
    now_img_name = pic_list[now_num]

    # 显示图片
    img_open = Image.open(source_path+'/'+pic_list[now_num])
    img_open = img_open.resize((350, 350))
    now_img = ImageTk.PhotoImage(img_open)
    img_show = tk.Label(root_window, image=now_img)
    img_show.place(x=40, y=220, anchor='nw')

    # 显示内容
    var1 = f'已排序，当前 {now_class} 类别下图片总数: {all_nums} '
    show_text(var1, 10, 140)

    new_all_nums = all_nums - 1
    var2 = f'记住当前的图片索引(0~{new_all_nums}): {now_num} '
    show_text(var2, 10, 170)

    var3 = f'当前图片名字: {now_img_name} '
    show_text(var3, 10, 190)


def bt2_hit():
    global source_path, target_path, pic_list, now_num, all_nums, now_img, now_img_name
    target_path = filedialog.askdirectory()  # 这里返回一个目录名
    target_path_Text.delete(1.0, "end")
    target_path_Text.insert(1.0, target_path)


def bt3_hit():
    global source_path, target_path, pic_list, now_num, all_nums, now_img, now_img_name
    now_num = now_num - 1
    if now_num >= 0 and now_num < all_nums:
        now_img_name = pic_list[now_num]
        new_all_nums = all_nums - 1
        var = f'记住当前的图片索引(0~{new_all_nums}): {now_num}'
        show_text(var, 10, 170)

        var2 = f'当前图片名字: {now_img_name} '
        show_text(var2, 10, 190)

        # 显示图片
        img_open = Image.open(source_path+'/'+pic_list[now_num])
        img_open = img_open.resize((350, 350))
        now_img = ImageTk.PhotoImage(img_open)
        img_show = tk.Label(root_window, image=now_img)
        img_show.place(x=40, y=220, anchor='nw')
    else:
        now_num = 0


def bt4_hit():
    global source_path, target_path, pic_list, now_num, all_nums, now_img, now_img_name
    now_num = now_num + 1
    if now_num >= 0 and now_num < all_nums:
        now_img_name = pic_list[now_num]
        new_all_nums = all_nums - 1
        var = f'记住当前的图片索引(0~{new_all_nums}): {now_num}'
        show_text(var, 10, 170)

        var2 = f'当前图片名字: {now_img_name} '
        show_text(var2, 10, 190)

        # 显示图片
        img_open = Image.open(source_path+'/'+pic_list[now_num])
        img_open = img_open.resize((350, 350))
        now_img = ImageTk.PhotoImage(img_open)
        img_show = tk.Label(root_window, image=now_img)
        img_show.place(x=40, y=220, anchor='nw')
    else:
        now_num = all_nums - 1


def bt5_hit():
    global source_path, target_path, pic_list, now_num, all_nums, now_img, now_img_name
    shutil.copy(source_path+'/'+now_img_name,
                target_path + '/'+now_img_name)


def show_text(var, p_x, p_y):
    #var = f'记住当前的图片索引:{now_num}'
    now_text_show = tk.Text(
        root_window, font=('Arial', 10), height=1, width=60)
    now_text_show.delete(1.0, "end")
    now_text_show.insert(1.0, var)
    now_text_show.place(x=p_x, y=p_y, anchor='nw')


def bt_to_hit(input_index):
    global source_path, target_path, pic_list, now_num, all_nums, now_img, now_img_name
    now_num = input_index
    now_img_name = pic_list[now_num]
    # all_nums = 1
    new_all_nums = all_nums - 1
    var = f'记住当前的图片索引(0~{new_all_nums}): {now_num}'
    show_text(var, 10, 170)

    var2 = f'当前图片名字: {now_img_name} '
    show_text(var2, 10, 190)

    # 显示图片
    img_open = Image.open(source_path+'/'+pic_list[now_num])
    img_open = img_open.resize((350, 350))
    now_img = ImageTk.PhotoImage(img_open)
    img_show = tk.Label(root_window, image=now_img)
    img_show.place(x=40, y=220, anchor='nw')


def close_all():
    reslut = messagebox.askokcancel("提示", " 你确定要关闭窗口吗? ")
    if reslut:
        root_window.quit()


if __name__ == '__main__':
    global source_path, target_path, pic_list, now_num, all_nums, now_img, now_img_name
    # all_nums = 10
    # now_num = 0
    root_window = tk.Tk()
    root_window.title('Select good pictures for single view')
    root_window.geometry('800x650')
    tip1 = tk.Label(root_window, text='输入具体到类别的原路径：',
                    font=('Arial', 10))
    tip1.place(x=30, y=30, anchor='nw')
    source_path_Text = tk.Text(root_window, font=('Arial', 10), height=2)
    source_path_Text.place(x=200, y=30, anchor='nw')
    tip2 = tk.Label(root_window, text='输入具体到类别的目标路径：',
                    font=('Arial', 10))
    tip2.place(x=30, y=80, anchor='nw')
    target_path_Text = tk.Text(root_window, font=('Arial', 10),  height=2)
    target_path_Text.place(x=220, y=80, anchor='nw')

    bt1 = tk.Button(root_window, text='1.打开类别原路径',
                    font=(15), command=bt1_hit)
    bt1.place(x=450, y=180, anchor='nw')

    bt2 = tk.Button(root_window, text='2.打开类别目标路径',
                    font=(15), command=bt2_hit)
    bt2.place(x=610, y=180, anchor='nw')

    bt3 = tk.Button(root_window, text='上一张',
                    font=(15), command=bt3_hit)
    bt3.place(x=450, y=220, anchor='nw')

    bt4 = tk.Button(root_window, text='下一张',
                    font=(15), command=bt4_hit)
    bt4.place(x=550, y=220, anchor='nw')

    bt5 = tk.Button(root_window, text='本张有可学习的特征（复制移动到目标目录）',
                    font=(15), command=bt5_hit)
    bt5.place(x=450, y=280, anchor='nw')

    input_index = tk.Entry(root_window, )
    input_index.place(x=450, y=400, anchor='nw')

    bt_to = tk.Button(root_window, text='跳转到指定index的图片',
                      font=(15), command=lambda: bt_to_hit(int(input_index.get())))  # 这里注意带参数的函数调用 需要加个lambda
    bt_to.place(x=450, y=440, anchor='nw')

    bt_close = tk.Button(root_window, text="关闭",
                         command=close_all, font=(15))
    bt_close.place(x=650, y=500, anchor='nw')

    root_window.mainloop()
