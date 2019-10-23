# trymeter.py
# test program to try out the meter class
# written by Roger Woollett

from sys import version_info
import time
import threading
import random
if version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
import meter as m


def initialize(meters):

    class Meterframe(tk.Frame):
        def __init__(self, master, id, text='', scale=(0, 300), *args, **kwargs):
            tk.Frame.__init__(self, master, *args, **kwargs)

            width = kwargs.get('width', 100)
            height = kwargs.get('height', 100)
            self.meter = m.Meter(self, width=width, height=height)
            meters[id]['meter'] = self.meter
            self.meter.setrange(scale[0], scale[1])
            self.meter.pack()

    class Mainframe(tk.Frame):
        def __init__(self, master, *args, **kwargs):
            tk.Frame.__init__(self, master, *args, **kwargs)
            index = 0
            for m in meters.keys():
                Meterframe(self, id=m, text=meters[m].get('text'), width=meters[m].get('width'), height=meters[m].get('height')).grid(row=0, column=index)
                index += 1
            tk.Button(self, text='Quit', width=15, command=master.destroy) \
                .grid(row=1, column=0)

    class App(tk.Tk):
        def __init__(self):
            tk.Tk.__init__(self)

            self.title('Try Meter.py')

            Mainframe(self).pack()

    class Application(threading.Thread):
        def __init__(self):
            super(Application, self).__init__()
            self.start()

        def callback(self):
            self.root.quit()

        def run(self):
            self.root = App()
            self.root.mainloop()

    app = Application()

    return meters, app
