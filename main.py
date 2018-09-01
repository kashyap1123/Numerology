from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from Num_BasicTypes import numerologybase
from datetime import datetime
from cStringIO import StringIO
import sys

# fname   = "Vijaya Kumar"
# lname   = "Jataprolu"
# dob     = datetime(1956, 01, 17, 04, 40)
# num_object  = numerologybase(fname, lname, dob)

def printOutput(num_object):
    #Redirect o/p to string
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    print num_object.name_first, num_object.name_last
    print "Date of Birth is ", num_object.dob.date().strftime("%A %d. %B %Y")
    num_object.pop_dob_today_corr()
    num_object.pop_age()
    print 'Age is ', num_object.age
    num_object.pop_birthnumber()
    print 'Birth Number is ', num_object.birth_number
    num_object.pop_progress_number()
    print 'Progress Number is ', num_object.progress_no
    num_object.pop_bad_years()
    print 'Bad years are ', num_object.bad_years
    num_object.pop_imp_years()
    print 'Imp years are ', num_object.imp_years
    num_object.pop_radical_years()
    print 'Radical years are ', num_object.radical_years
    num_object.pop_zenith_years()
    print 'Zenith years are ', num_object.zenith_years
    num_object.pop_birth_lom()
    print 'Birth LoM is ', num_object.birth_lom
    num_object.pop_curr_lom()
    print 'Current LoM is ', num_object.curr_lom
    print num_object.print_chart()

    sys.stdout = old_stdout
    return(mystdout.getvalue())

class NumeroRun(FloatLayout):

    # Declare members
    fname = lname = ''
    yob = mob = dob = hob = minob = 0
    dtdob   = datetime.today()
    #Numerology base class
    numerobase = numerologybase(fname,lname,dtdob)

    label_wid = ObjectProperty()

    def set_fname(self, data):
        self.fname   = data

    def set_lname(self, data):
        self.lname   = data

    def set_yob(self, data):
        #Need to type cast for these ?
        self.yob   = int(float(data))

    def set_mob(self, data):
        self.mob   = int(float(data))

    def set_dob(self, data):
        self.dob   = int(float(data))

    def set_hob(self, data):
        self.hob   = int(float(data))

    def set_minob(self, data):
        self.minob   = int(float(data))

    # numeroinput = ObjectProperty(None)
    def calculate(self):
        # self.fname   = "Vijaya Kumar"
        # self.lname   = "Jataprolu"
        # self.dtdob   = datetime(1956, 01, 17, 04, 40)
        self.dtdob   = datetime(self.yob, self.mob, self.dob, self.hob, self.minob)
        self.numerobase = numerologybase(self.fname,self.lname,self.dtdob)
        printOut = printOutput(self.numerobase)
        self.label_wid.text = printOut
        self.label_wid.texture_update()
        return 0

class NumeroApp(App):

    def build(self):
        return NumeroRun()


if __name__ == '__main__':
    NumeroApp().run()
