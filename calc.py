from tkinter import *
import math

light_grey='#F5F5F5'
lable_colore='#25265E'
off_white='#F8FAFF'
small_font_style=('Arial',16)
large_font_style=('Arial',40)
default_font_style=('Arial',20)
digit_font_style=('Arial',24,'bold')
light_blue='#CCEDFF'

class Calculator:
    def __init__(self):
        self.window=Tk()
        self.window.title('Calculator')
        self.window.geometry('375x600+50+10')
        self.window.resizable(False,False)

        self.display_frame=self.create_display_frame()
        self.button_frame=self.create_button_frame()

        self.top_label_result=''
        self.ground_label_result=''
        self.top_label,self.ground_label=self.create_label()

        self.digit={7:(1,1),8:(1,2),9:(1,3),
                    4:(2,1),5:(2,2),6:(2,3),
                    1:(3,1),2:(3,2),3:(3,3),
                    '.':(4,1),0:(4,2)
                    }
        self.operation={'/':"\u00F7",'*':'\u00D7','-':'-','+':'+'}

        self.digit_button=self.create_digit_button()
        self.opetation_button=self.create_operation_button()
        self.create_all_clear_button()
        self.button_frame.rowconfigure(0, weight=1)
        self.spcial_button()
    def spcial_button(self):
        self.create_equal_button()
        self.create_all_clear_button()
        # self.create_clear_button()
        self.create_sqare_button()
        self.create_sqrt_button()
        self.create_pi_button()
        self.bind_key()




        for x in range(1, 5):
            self.button_frame.rowconfigure(x,weight=1)
            self.button_frame.columnconfigure(x,weight=1)



    def create_display_frame(self):
        frame=Frame(self.window,height=221,bg=lable_colore)
        frame.pack(expand=True,fill='both')
        return frame
    def create_button_frame(self):
        frame=Frame(self.window,bg=lable_colore)
        frame.pack(expand=True,fill='both')
        return frame
    def create_label(self):
        top_label=Label(self.display_frame,text=self.top_label_result,padx=24,anchor=E,font=small_font_style)
        top_label.pack(expand=True,fill='both')


        ground_label = Label(self.display_frame, text=self.top_label_result, padx=24, anchor=E,
                             font=large_font_style)
        ground_label.pack(expand=True, fill='both')
        return top_label,ground_label


    def create_digit_button(self):
        for digit,row_valu in self.digit.items():
            button=Button(self.button_frame,text=str(digit),bd=0,bg='white',fg=lable_colore,
                          font=default_font_style,command=lambda x=digit:self.show_valu(x))
            button.grid(row=row_valu[0],column=row_valu[1],sticky=NSEW)

    def create_operation_button(self):
        i=0
        for operator ,symbol in self.operation.items():
            operation_button=Button(self.button_frame,text=symbol,bd=0,fg=lable_colore,bg=off_white,
                                    font=default_font_style,
                                    command=lambda x=operator:self.operation_button_valu(x))
            operation_button.grid(row=i,column=4,sticky=NSEW)
            i+=1
    def create_all_clear_button(self):
        button = Button(self.button_frame, text='AC', bd=0, bg=off_white,fg=lable_colore,
                        font=small_font_style,command=lambda :self.all_clear_button_operation())
        button.grid(row=0, column=1, sticky=NSEW)
    def create_clear_button(self):
        button = Button(self.button_frame, text='C', bd=0, bg=off_white, fg=lable_colore,
                        font=small_font_style)
        button.grid(row=0, column=3, sticky=NSEW, columnspan=1)

    def create_equal_button(self):
        equal_button=Button(self.button_frame,text='=',bd=0,bg=light_blue,fg=lable_colore,
                            font=digit_font_style,command=lambda :self.equal_button_operation())
        equal_button.grid(row=4,column=3,sticky=NSEW)

    def create_sqare_button(self):
        button = Button(self.button_frame, text='x\u00b2', bd=0, bg=off_white, fg=lable_colore,
                        font=small_font_style,command=lambda :self.square_button_operation())
        button.grid(row=0, column=2, sticky=NSEW)
    def create_sqrt_button(self):
        button = Button(self.button_frame, text='\u221ax', bd=0, bg=off_white, fg=lable_colore,
                        font=small_font_style, command=lambda: self.sqrt_operation())
        button.grid(row=0, column=3, sticky=NSEW)

    def sqrt_operation(self):
        self.ground_label_result=str(eval(self.ground_label_result)**0.5)
        self.update_ground_label()
    def square_button_operation(self):
        self.ground_label_result=str(eval(self.ground_label_result)**2)
        self.update_ground_label()

    def create_pi_button(self):
        pi = Button(self.button_frame, text='pi', bd=0, bg=off_white, fg=lable_colore,
                              font=small_font_style, command=lambda: self.pi_operation())
        pi.grid(row=4, column=4, sticky=NSEW)
    def pi_operation(self):
        self.ground_label_result=str(math.pi)
        self.ground_label.config(text=self.ground_label_result[:12])





    def show_valu(self,valu):
        self.ground_label_result+=str(valu)
        self.update_ground_label()

    def operation_button_valu(self,operator):
        self.ground_label_result+=str(operator)
        self.top_label_result+=self.ground_label_result
        self.update_top_label()
        self.ground_label_result=''
        self.update_ground_label()
    def all_clear_button_operation(self):
        self.top_label_result=''
        self.ground_label_result=''
        self.update_ground_label()
        self.update_top_label()
    def equal_button_operation(self):

        self.top_label_result+=self.ground_label_result
        self.update_top_label()
        try:
            self.ground_label_result=str(eval(self.top_label_result))

            self.update_ground_label()
            self.top_label_result = ''
        except Exception as e:
            self.ground_label_result='Error'

        finally:

            self.update_ground_label()
    def bind_key(self):
        self.window.bind('<Return>',lambda event:self.equal_button_operation())
        for key in self.digit:
            self.window.bind(str(key),lambda event,digit=key:self.show_valu(digit))
        for key in self.operation:
            self.window.bind(key,lambda event,oparator=key:self.operation_button_valu(oparator))













    def update_top_label(self):
        self.top_label.config(text=self.top_label_result[:28])
    def update_ground_label(self):
        self.ground_label.config(text=self.ground_label_result[:12])



    def run(self):
        self.window.mainloop()
if __name__=='__main__':
    calc=Calculator()
    calc.run()

