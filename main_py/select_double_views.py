
import tkinter as tk
import os
import shutil
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox

def bt1_hit():
    """
    打开空中视角类别原路径
    """

    global source_path_aerial,source_path_street, target_path, aerial_pic_list, \
    street_pic_list,together_list, now_num, all_together_nums, now_img, now_img_name

    now_num = 0

    aerial_pic_list = []

    # 这里返回一个目录名 文件选择对话框,    askdirectory	选择目录，并返回目录名
    source_path_aerial = filedialog.askdirectory()
    source_path_Text1.delete(1.0, "end")
    source_path_Text1.insert(1.0, source_path_aerial)

    for pic_name in sorted(os.listdir(source_path_aerial)):
        aerial_pic_list.append(pic_name)



def bt2_hit():
    """
    打开地面视角类别原路径
    """
    global source_path_aerial,source_path_street, target_path, aerial_pic_list, \
    street_pic_list,together_list, now_num, all_together_nums, now_img, now_img_name

    now_num = 0
    street_pic_list = []
    together_list = []

    # 这里返回一个目录名 文件选择对话框,    askdirectory	选择目录，并返回目录名
    source_path_street = filedialog.askdirectory()
    now_class = source_path_street.split('/')[-1:]
    source_path_Text2.delete(1.0, "end")
    source_path_Text2.insert(1.0, source_path_street)

    for pic_name in sorted(os.listdir(source_path_street)):
        street_pic_list.append(pic_name)

    for i in aerial_pic_list:
        for j in street_pic_list:
            if i.split('/')[-1:][0].split('.')[0] == j.split('/')[-1:][0].split('.')[0]:
                together_list.append(i.split('/')[-1:][0].split('.')[0]) #这个list存的只是图片名,而且没有后缀png或jpg

    now_img_name = together_list[now_num]
    all_together_nums = len(together_list)

    # 显示内容
    var1 = f'已排序，当前{now_class}下,空图总数: {len(aerial_pic_list)}，地图总数: {len(street_pic_list)},共存数量：{len(together_list)}'
    show_text(var1, 10, 148)

    var2 = f'记住当前共有的图片索引(0~{len(together_list)-1}): {now_num}'
    show_text(var2, 10, 168)

    var3 = f'当前共有的图片名字: {together_list[now_num]} '
    show_text(var3, 10, 188)


    #显示共有图片 空中视角

    img = Image.open(source_path_aerial+'/'+together_list[now_num]+'.png')
    img = img.resize((250, 250))
    img_ph = ImageTk.PhotoImage(img)

    img_open = Image.open(source_path_street+'/'+together_list[now_num]+'.jpg')
    img_open = img_open.resize((250, 250))
    img_pho = ImageTk.PhotoImage(img_open)


    img_show = tk.Label(root_window, image=img_ph)
    img_show.place(x=20, y=280, anchor='nw')

    img_show = tk.Label(root_window, image=img_pho)
    img_show.place(x=300, y=280, anchor='nw')

    root_window.mainloop() #原来这句话才是重点，就是需要这个东西，才能保证显示图像



def bt3_hit():
    """
    打开目标输出路径,将自动输出找到aerial和street的类别
    """
    global source_path_aerial,source_path_street, target_path, aerial_pic_list, \
    street_pic_list,together_list, now_num, all_together_nums, now_img, now_img_name

    target_path = filedialog.askdirectory()  # 这里返回一个目录名，即good_double_views
    target_path_Text.delete(1.0, "end")
    target_path_Text.insert(1.0, target_path)


def bt4_hit():
    """
    上一张
    """
    global source_path_aerial,source_path_street, target_path, aerial_pic_list, \
    street_pic_list,together_list, now_num, all_together_nums, now_img, now_img_name

    now_num = now_num - 1
    if now_num >= 0 and now_num < all_together_nums:
        now_img_name = together_list[now_num]

        var = f'记住当前的图片索引(0~{all_together_nums-1}): {now_num}'
        show_text(var, 10, 170)

        var2 = f'当前图片名字: {now_img_name} '
        show_text(var2, 10, 190)

        # 显示图片
        img = Image.open(source_path_aerial+'/'+together_list[now_num]+'.png')
        img = img.resize((250, 250))
        img_ph = ImageTk.PhotoImage(img)

        img_open = Image.open(source_path_street+'/'+together_list[now_num]+'.jpg')
        img_open = img_open.resize((250, 250))
        img_pho = ImageTk.PhotoImage(img_open)

        img_show = tk.Label(root_window, image=img_ph)
        img_show.place(x=20, y=280, anchor='nw')

        img_show = tk.Label(root_window, image=img_pho)
        img_show.place(x=300, y=280, anchor='nw')

        root_window.mainloop()

    else:
        now_num = 0


def bt5_hit():
    """
    下一张
    """
    global source_path_aerial,source_path_street, target_path, aerial_pic_list, \
    street_pic_list,together_list, now_num, all_together_nums, now_img, now_img_name

    now_num = now_num + 1
    if now_num >= 0 and now_num < all_together_nums:
        now_img_name = together_list[now_num]

        var = f'记住当前的图片索引(0~{all_together_nums-1}): {now_num}'
        show_text(var, 10, 170)

        var2 = f'当前图片名字: {now_img_name} '
        show_text(var2, 10, 190)

        # 显示图片
        img = Image.open(source_path_aerial+'/'+together_list[now_num]+'.png')
        img = img.resize((250, 250))
        img_ph = ImageTk.PhotoImage(img)

        img_open = Image.open(source_path_street+'/'+together_list[now_num]+'.jpg')
        img_open = img_open.resize((250, 250))
        img_pho = ImageTk.PhotoImage(img_open)

        img_show = tk.Label(root_window, image=img_ph)
        img_show.place(x=20, y=280, anchor='nw')

        img_show = tk.Label(root_window, image=img_pho)
        img_show.place(x=300, y=280, anchor='nw')

        root_window.mainloop()
    else:
        now_num = all_together_nums - 1


def bt6_hit():
    """
    复制移动到目标目录，自动去输出到哪个视角下的哪个类别，只需要给到一个文件夹即可
    """

    global source_path_aerial,source_path_street, target_path, aerial_pic_list, \
    street_pic_list,together_list, now_num, all_together_nums, now_img, now_img_name

    aerial_view_class = source_path_aerial.split('/')[-2:]
    street_view_class = source_path_street.split('/')[-2:]

    shutil.copy(source_path_aerial+'/'+together_list[now_num]+'.png',
    target_path +'/'+aerial_view_class[0]+'/'+aerial_view_class[1]+'/'+together_list[now_num]+'.png')

    shutil.copy(source_path_street+'/'+together_list[now_num]+'.jpg',
    target_path +'/'+street_view_class[0]+'/'+street_view_class[1]+'/'+together_list[now_num]+'.jpg')


def show_text(var, p_x, p_y):
    """
    展示文字的show函数
    """

    now_text_show = tk.Text(
        root_window, font=('Arial', 10), height=1, width=80)
    now_text_show.delete(1.0, "end")
    now_text_show.insert(1.0, var)
    now_text_show.place(x=p_x, y=p_y, anchor='nw')


def bt_to_hit(input_index):
    """
    跳转到指定的index图片
    """
    global source_path_aerial,source_path_street, target_path, aerial_pic_list, \
    street_pic_list,together_list, now_num, all_together_nums, now_img, now_img_name

    now_num = input_index

    var = f'记住当前的图片索引(0~{all_together_nums-1}): {now_num}'
    show_text(var, 10, 170)

    var2 = f'当前图片名字: {together_list[now_num]} '
    show_text(var2, 10, 190)

    # 显示图片
    img = Image.open(source_path_aerial+'/'+together_list[now_num]+'.png')
    img = img.resize((250, 250))
    img_ph = ImageTk.PhotoImage(img)

    img_open = Image.open(source_path_street+'/'+together_list[now_num]+'.jpg')
    img_open = img_open.resize((250, 250))
    img_pho = ImageTk.PhotoImage(img_open)

    img_show = tk.Label(root_window, image=img_ph)
    img_show.place(x=20, y=280, anchor='nw')

    img_show = tk.Label(root_window, image=img_pho)
    img_show.place(x=300, y=280, anchor='nw')

    root_window.mainloop()

def close_all():
    """
    关闭一切按钮
    """
    reslut = messagebox.askokcancel("提示", " 你确定要关闭窗口吗? ")
    if reslut:
        #root_window.quit
        root_window.destroy()


if __name__ == '__main__':
    global root_window, source_path, target_path, pic_list, now_num, all_nums, now_img, now_img_name
    # all_nums = 10
    # now_num = 0
    root_window = tk.Tk()
    root_window.title('Select good pair pictures from two single views')
    root_window.geometry('1100x750')
    tip1 = tk.Label(root_window, text='空中视角类别的输入原路径：',font=('Arial', 10))
    tip1.place(x=20, y=30, anchor='nw')
    source_path_Text1 = tk.Text(root_window, font=('Arial', 10), height=2)
    source_path_Text1.place(x=230, y=30, anchor='nw')

    tip2 = tk.Label(root_window, text='地面视角相同类别的输入原路径：',font=('Arial', 10))
    tip2.place(x=20, y=70, anchor='nw')
    source_path_Text2 = tk.Text(root_window, font=('Arial', 10), height=2)
    source_path_Text2.place(x=230, y=70, anchor='nw')

    tip3 = tk.Label(root_window, text='目标输出路径(自动找到aerial和street):',font=('Arial', 10))
    tip3.place(x=10, y=110, anchor='nw')
    target_path_Text = tk.Text(root_window, font=('Arial', 10),  height=2)
    target_path_Text.place(x=240, y=110, anchor='nw')

    bt1 = tk.Button(root_window, text='1.打开空视类别原路径',
                    font=(15), command=bt1_hit)
    bt1.place(x=620, y=180, anchor='nw')

    bt2 = tk.Button(root_window, text='2.打开地视类别原路径',
                    font=(15), command=bt2_hit)
    bt2.place(x=850, y=180, anchor='nw')

    bt3 = tk.Button(root_window, text='3.打开目标输出路径',
                    font=(15), command=bt3_hit)
    bt3.place(x=720, y=220, anchor='nw')


    bt4 = tk.Button(root_window, text='上一张',
                    font=(15), command=bt4_hit)
    bt4.place(x=760, y=260, anchor='nw')

    bt5 = tk.Button(root_window, text='下一张',
                    font=(15), command=bt5_hit)
    bt5.place(x=920, y=260, anchor='nw')

    bt6 = tk.Button(root_window, text='这对空地质量均达标(复制移动到目标目录)',
                    font=(15), command=bt6_hit)
    bt6.place(x=650, y=320, anchor='nw')

    input_index = tk.Entry(root_window, )
    input_index.place(x=750, y=400, anchor='nw')

    bt_to = tk.Button(root_window, text='跳转到指定index的图片',
                      font=(15), command=lambda: bt_to_hit(int(input_index.get())))  # 这里注意带参数的函数调用 需要加个lambda
    bt_to.place(x=700, y=440, anchor='nw')

    bt_close = tk.Button(root_window, text="关闭",command=close_all, font=(15))
    bt_close.place(x=700, y=500, anchor='nw')

    tip_last = tk.Label(root_window, text='提示：完成一个类别的挑选后，请关闭后再重新启动',font=('Arial', 11))
    tip_last.place(x=650, y=620, anchor='nw')

    root_window.mainloop()
