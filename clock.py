import time
from tkinter import *
from datetime import datetime
from tkinter import ttk


def time_now_update():
    pass
    lbl_time_now.configure(
        text=datetime.now().strftime('%H:%M:%S')
    )
    lbl_time_now.after(1000, time_now_update)


def update_timer():
    count = (
            int(hour_timer.get()) * 3600
            + int(minute_timer.get()) * 60
            + int(second_timer.get())
    )

    while count > -1:

        minute_ost, second_ost = divmod(count, 60)

        hour_ost = 0
        if minute_ost > 60:
            hour_ost, minute_ost = divmod(minute_ost, 60)

        frame_2.update()
        time.sleep(1)

        hour_timer.set("{0:2d}".format(hour_ost))
        minute_timer.set("{0:2d}".format(minute_ost))
        second_timer.set("{0:2d}".format(second_ost))

        count -= 1

        entry_timer_hour.configure(state='readonly')
        entry_timer_minute.configure(state='readonly')
        entry_timer_second.configure(state='readonly')

    entry_timer_hour.configure(state='normal')
    entry_timer_minute.configure(state='normal')
    entry_timer_second.configure(state='normal')


def update_stopwatch():
    def stop_watch():
        global vkl_otl
        vkl_otl = -1

    global vkl_otl
    vkl_otl = +1

    btn_stop_stopwatch = Button(frame_3,
                                text='Остановить',
                                command=stop_watch,
                                width=10
                                )
    btn_stop_stopwatch.grid(column=4, row=0)

    count = 0

    while vkl_otl == 1:
        minute_ost, second_ost = divmod(count, 60)

        hour_ost = 0
        if minute_ost > 60:
            hour_ost, minute_ost = divmod(minute_ost, 60)

        frame_2.update()
        time.sleep(1)

        hour_stopwatch.set("{0:2d}".format(hour_ost))
        minute_stopwatch.set("{0:2d}".format(minute_ost))
        second_stopwatch.set("{0:2d}".format(second_ost))

        count += 1


widow = Tk()
widow.geometry('600x100')
widow.title('Time')

notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

frame_1 = ttk.Frame(notebook)
frame_2 = ttk.Frame(notebook)
frame_3 = ttk.Frame(notebook)

vkl_otl = 0

notebook.add(frame_1, text="Время")

lbl_time_now = Label(frame_1,
                     text='',
                     font='Arial 50',
                     foreground="#293036",
                     background="#f73b6a",
                     )
lbl_time_now.pack(fill=BOTH, expand=True)
time_now_update()

notebook.add(frame_2, text="Таймер")

hour_timer = StringVar(frame_2)
minute_timer = StringVar(frame_2)
second_timer = StringVar(frame_2)

hour_timer.set('00')
minute_timer.set('00')
second_timer.set('00')

entry_timer_hour = Entry(frame_2, textvariable=hour_timer, width=10)
entry_timer_hour.grid(column=0, row=0)

entry_timer_minute = Entry(frame_2, textvariable=minute_timer, width=10)
entry_timer_minute.grid(column=1, row=0)

entry_timer_second = Entry(frame_2, textvariable=second_timer, width=10)
entry_timer_second.grid(column=2, row=0)

btn_timer = Button(frame_2, text='Запустить', command=update_timer, width=10)
btn_timer.grid(column=3, row=0)

notebook.add(frame_3, text="Секундомер")

hour_stopwatch = StringVar(frame_3)
minute_stopwatch = StringVar(frame_3)
second_stopwatch = StringVar(frame_3)

hour_stopwatch.set('00')
minute_stopwatch.set('00')
second_stopwatch.set('00')

entry_hour_stopwatch = Entry(frame_3,
                             textvariable=hour_stopwatch,
                             width=10,
                             state='readonly')
entry_hour_stopwatch.grid(column=0, row=0)

entry_minute_stopwatch = Entry(frame_3,
                               textvariable=minute_stopwatch,
                               width=10,
                               state='readonly'
                               )
entry_minute_stopwatch.grid(column=1, row=0)

entry_second_stopwatch = Entry(frame_3,
                               textvariable=second_stopwatch,
                               width=10,
                               state='readonly'
                               )
entry_second_stopwatch.grid(column=2, row=0)

btn_stopwatch = Button(frame_3,
                       text='Запустить',
                       command=update_stopwatch,
                       width=10
                       )
btn_stopwatch.grid(column=3, row=0)


widow.mainloop()
