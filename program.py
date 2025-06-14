from tkinter import messagebox
from tkinter import *
from tkinter import ttk
def read_elements_from_file(filename):
    elements_masses={}
    with open(filename,'r') as file:
        for line in file:
            element, mass = line.strip().split(':')
            elements_masses[element]=float(mass)
    return elements_masses
def save_element_to_file(filename, element, mass):
    with open(filename,'a') as file:
        file.write(f"{element}:{mass}\n")
def add_element():
    selected_element=comboboxelem.get()
    selected_count=comboboxcount.get()
    if selected_count=="":
        formula=f"{selected_element}"
        entry.insert(40,formula)
    else:
        formula=f"{selected_element}{selected_count}"
        entry.insert(40, formula)
# Функция для очистки полей ввода
def clear_entrys():
    entry.delete(0,END)
    labeloutput.config(text="")
# Расчёт массы
def calculate_mass():
    formula=entry.get()
    if formula=="":
        labeloutput.config(text="Строка пуста")
    else:
        total_mass=0.0
        i=0
        while i<len(formula):
            if i+1<len(formula) and formula[i:i+2] in elements_masses:
                element=formula[i:i+2]
                i+=2
            elif formula[i] in elements_masses:
                element=formula[i]
                i+=1
            else:
                labeloutput.config(text="Неверно введён элемент")
                return
            count=""
            while i<len(formula) and formula[i].isdigit():
                count+=formula[i]
                i+=1
            if count=="":
                count="1"
            if int(count)==0:
                labeloutput.config(text="Количество атомов не может быть равно 0")
                return
            total_mass+=elements_masses[element]*int(count)
        labeloutput.config(text=str(total_mass))
#Инструкции
def instructions():
    global inst
    try:
        if 'inst' in globals() and inst.winfo_exists():
            inst.lift()
            return
    except:
        pass
    inst=Tk()
    text = """В основном окне программы присутствуют поля со списком. В левом поле со списком вы можете выбрать элемент, в правом- количество атомов элемента. После выбора элемента и количества его атомов при нажатии ни кнопку добавить в строку ввода формулы добавится название элемента и количество атомов. Также можно ввести формулу вручную. При введении формулы вручную вводится название элемента из периодической таблицы Менделеева. Первая буква в названии элемента-заглавная, вторая- строчная. После ввода формулы необходимо нажать на кнопку Рассчитать и вам выведется атомная масса элемента. Инструкции по применению откроется окно, в котором вы и читаете этот текст. При нажатии на кнопку Добавить новый элемент откроется окно добавления нового элемента, в котором вы можете добавить элемент. В верхнюю строку ввода вводится название элемента, в нижнюю- атомная масса этого элемента. Название элемента может состоять не более чем из 2 букв латинского алфавита, первая буква-заглавная, вторая- строчная. Масса нового элемента не может быть отрицательной, нулевой. Для разделения числа на целую и действительную часть используетя точка. После ввода данных необходимо нажать кнопку Сохранить, в нижней строке программа выведет вам результат добавления. Если элемент успешно добавлен, его можно использовать в дальнейших вычислениях. Чтобы завершить работу программы, необходимо нажать кнопку Закрыть в основном окне."""
    inst.resizable(False, False)
    inst.iconbitmap('image.ico')
    inst.geometry('550x600')
    inst.title('Инструкции по применению')
    text_widget = Text(inst, wrap=WORD, font=('Arial', 12))
    text_widget.configure(bg=window.cget('bg'))
    text_widget.pack(side=LEFT, fill=BOTH, expand=1)
    text_widget.insert(END, text)
    text_widget.config(state=DISABLED)
    closebutt = Button(inst, text='Закрыть окно', width=12, height=1, font=10, command=inst.destroy)
    closebutt.place(x=400, y=500)
#Окно добавления элемента
def add_new_element():
    global addwindow
    try:
        if 'addwindow' in globals() and addwindow.winfo_exists():
            addwindow.lift()
            return
    except:
        pass
    addwindow = Tk()
    addwindow.geometry('550x600')
    addwindow.title('Добавление нового элемента')
    addwindow.iconbitmap('image.ico')
    addwindow.resizable(False, False)
    text_add = Label(addwindow, text='Введите название элемента', bg=window.cget('bg'), fg='black', width=40,font=12)
    text_add.place(x=50, y=5)
    entryelem = ttk.Entry(addwindow, font=10, width=40, state="normal", justify="center")
    entryelem.place(x=50, y=55)
    massadd = Label(addwindow, text='Введите массу элемента', bg=window.cget('bg'), fg='black', width=40, font=12)
    massadd.place(x=50, y=105)
    entrymass = ttk.Entry(addwindow, font=10, width=40, state="normal", justify="center")
    entrymass.place(x=50, y=155)
    vivodstring = Label(addwindow, bg=window.cget('bg'), fg='black', width=40, font=12)
    vivodstring.place(x=50, y=205)
    buttonclosing = Button(addwindow, text='Закрыть окно', width=12, height=1, font=10, command=addwindow.destroy)
    buttonclosing.place(x=400, y=500)
    def save_new_element():
        new_elem = entryelem.get()
        new_mass = entrymass.get()
        if new_elem == "" or new_mass == "":
            vivodstring.config(text="Строка ввода пуста")
            return
        if len(new_elem) > 2:
            vivodstring.config(text="Неверный ввод элемента")
            return
        if not new_elem.isalpha() and not new_elem.isascii():
            vivodstring.config(text="Неверный ввод элемента")
            return
        if not new_elem[0].isupper():
            vivodstring.config(text="Неверный ввод элемента")
            return
        if not new_elem[1].islower():
            vivodstring.config(text="Неверный ввод элемента")
            return
        try:
            new_mass = float(new_mass)
            if new_mass <= 0:
                vivodstring.config(text="Неверный ввод массы")
                return
        except ValueError:
            vivodstring.config(text="Неверный ввод массы")
            return
        if new_elem in elements_masses:
            vivodstring.config(text="Элемент с таким названием уже есть")
            return
        elements_masses.update({new_elem: new_mass})
        save_element_to_file("elements_masses.txt", new_elem, new_mass)
        comboboxelem['values'] = list(elements_masses.keys())
        vivodstring.config(text="Элемент успешно добавлен")
    buttons = Button(addwindow, text='Сохранить', width=12, height=1, font=10, command=save_new_element)
    buttons.place(x=50, y=500)
#Закрытие
def close_krest():
    if messagebox.askokcancel("Выход", "Выйти из программы?"):
        window.destroy()
        try:
            if 'inst' in globals() and inst.winfo_exists():
                inst.destroy()
        except:
            pass
        try:
            if 'addwindow' in globals() and addwindow.winfo_exists():
                addwindow.destroy()
        except:
            pass
window = Tk()
window.geometry('550x600')
window.title('Калькулятор молекулярных масс')
window.iconbitmap('image.ico')
window.resizable(False,False)
window.protocol("WM_DELETE_WINDOW", close_krest)
elements_masses = read_elements_from_file('elements_masses.txt')
label = Label(window, text='Калькулятор молекулярных масс', bg=window.cget('bg'), fg='black', width=40, font=12)
label.place(x=50, y=50)
button1 = Button(text='Добавить', width=12, height=1, font=10, command=add_element)
button1.place(x=50, y=200)
elements = list(elements_masses.keys())
comboboxelem = ttk.Combobox(values=elements, state="readonly")
comboboxelem.pack(anchor=NW, padx=6, pady=6)
comboboxelem.place(x=50, y=120)
labelelem = Label(window, text='Выберите элемент', bg=window.cget('bg'), fg='black', width=16, font=("Arial", 11 ))
labelelem.place(x=50,y=90)
labelcount = Label(window, text='Выберите количество атомов', bg=window.cget('bg'), fg='black', width=23, font=("Arial", 11 ))
labelcount.place(x=285,y=90)
comboboxcount = ttk.Combobox(values = list(range(1, 51)), state="readonly")
comboboxcount.pack(anchor=NW, padx=6, pady=6)
comboboxcount.place(x=350, y=120)
entry = ttk.Entry(font=10, width=40, state="normal", justify="center")
entry.place(x=50, y=150)
button2 = Button(text='Рассчитать', width=12, height=1, font=10, command=calculate_mass)
button2.place(x=200, y=200)
labeloutput = Label(bg='white', fg='black', width=40, font=12)
labeloutput.place(x=50, y=250)
buttonclose = Button(text='Закрыть', width=12, height=1, font=10, command=close_krest)
buttonclose.place(x=350, y=500)
buttonclear = Button(text='Очистить', width=12, height=1, font=10, command=clear_entrys)
buttonclear.place(x=350, y=200)
buttoninst = Button(text='Инструкции по применению', width=25, height=1, font=10, command=instructions)
buttoninst.place(x=210, y=400)
addbutt = Button(text='Добавить новый элемент', width=25, height=1, font=10, command=add_new_element)
addbutt.place(x=210, y=350)
window.mainloop()