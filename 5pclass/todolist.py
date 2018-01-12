#!/usr/bin/python3
import tkinter as ttk

List =[]

class Task:
   """This is the List class that was created for the object to-do-list, and includes the event, date, location, priority and other methods"""

   def __init__(self, initEvent, initLocation, initDate, initPriority ):
       """create a new to-do-list"""
       self.event = initEvent
       self.location = initLocation
       self.date = initDate
       self.priority = initPriority

   def __str__(self):
       return 'Task: '+self.get_add_text()+' Due: '+self.get_due_text()+' At: '+self.get_location_text()+' Priority: '+self.get_priority_text()


   def __le__(self, other):
       return self.priority <= other

   def __gt__(self, other):
       return self.priority > other


   def getEvent(self):
       return self.event

   def getPriority(self):
       return self.priority




class SlugToDoList(ttk.Frame):

  def __init__(self, master):
      ttk.Frame.__init__(self, master)

      # Creating main containers

      self.outer_left = ttk.Frame(self, width=200, height=100, bg='light blue')
      self.outer_left.pack(side=ttk.LEFT, fill=ttk.Y)  # This is where add task would be located / action buttons

      self.middle = ttk.Frame(self, width=200, height=500, bg='orange red')
      self.middle.pack(side=ttk.LEFT, expand=1, fill=ttk.BOTH)  # This is where a list of tasks at hand would be located

      self.right_side = ttk.Frame(self, width=200, height=500, bg='light green')
      self.right_side.pack(side=ttk.RIGHT, expand=1, fill=ttk.BOTH)  # This would contain completed tasks

      self.create_labels()
      self.create_listbox()
      self.create_buttons()

  def create_labels(self):
      list_label = ttk.Label(self.middle, text='Task List', bg='orange red')
      list_label.pack()

      com_label = ttk.Label(self.right_side, text='Completed Task', bg='light green')
      com_label.pack()

  def create_buttons(self):
      # Action Buttons = outer_left, same as above
      add_btn = ttk.Button(self.outer_left, text=' Add Task ', pady=5, highlightbackground='light blue', command=self.add_window)
      add_btn.pack()  # Creates button for adding new tasks

      done_btn = ttk.Button(self.outer_left, text=' Done Task ', pady=5, highlightbackground='light blue', command=self.completed_task)
      done_btn.pack()  # Creates button for adding new tasks

      delete_btn = ttk.Button(self.outer_left, text='Delete', pady=5, highlightbackground='light blue', command=self.delete_items)
      delete_btn.pack()  # Creates button for deleting a most recent task

      delete_all_btn = ttk.Button(self.outer_left, text='Delete All', pady=5, highlightbackground='light blue', command=self.delete_all)
      delete_all_btn.pack()  # Creates button for deleting all task

      sort_btn = ttk.Button(self.outer_left, text='Priority(ASC)', pady=5, highlightbackground='light blue')
      sort_btn.pack()  # Creates button that sorts task by priority (1 highest, 3 = lowest)

      sort_btn2 = ttk.Button(self.outer_left, text='Priority(DESC)', pady=5, highlightbackground='light blue')
      sort_btn2.pack()  # Creates button that sorts task by priority (1 highest, 3 = lowest)

      help_btn = ttk.Button(self.outer_left, text='Help', pady=5, highlightbackground='light blue', command=self.help_box)
      help_btn.pack()  # Creates button that opens new window to show instructions for application

      exit_btn = ttk.Button(self.outer_left, text='Exit', pady=5, highlightbackground='light blue', command=root.destroy)
      exit_btn.pack()  # Button for exiting application

  def create_listbox(self):
      self.com_txt = ttk.Listbox(self.right_side, width=27, height=28, borderwidth=1)
      self.com_txt.pack()

      self.list_txt = ttk.Listbox(self.middle, width=27, height=28, borderwidth=1,)
      self.list_txt.pack()


  # Creates inner window when pressing the Add task button
  def add_window(self):
      window = ttk.Tk()
      window.title('Add Your Task')

      add_window = ttk.Frame(window, width=300, height=300, bg='light blue')
      add_window.pack()

      add_lbl = ttk.Label(add_window, text='Add Task:', bg='light blue')
      add_lbl.pack()

      self.add_txt = ttk.Text(add_window, width=27, height=10)
      self.add_txt.pack()

      due_lbl = ttk.Label(add_window, text='Due Date (MM/DD):', bg='light blue')
      due_lbl.pack()

      self.due_entry = ttk.Entry(add_window, width=7, highlightbackground='light blue')
      self.due_entry.pack()

      location_label = ttk.Label(add_window, text='Location:', bg='light blue')
      location_label.pack()

      self.location_text = ttk.Text(add_window, width=15, height=1, highlightbackground='light blue')
      self.location_text.pack()

      priority_label = ttk.Label(add_window, text ='Priority Level\n 1 High\n 2 Normal\n 3 Least', bg ='light blue')
      priority_label.pack()

      self.priority_entry = ttk.Text(add_window, width=7, height=1, highlightbackground='light blue')
      self.priority_entry.pack()
      
      # Had to add a lambda function due to having to pass arguments to function (Button commands don't usually allow that)
      add_tsk_btn = ttk.Button(add_window, text='Add', pady=2, highlightbackground='light blue', command= lambda: self.add_item_helper(window))
      add_tsk_btn.pack()

      ext_btn = ttk.Button(add_window, text='Exit', pady=2, highlightbackground='light blue', command=window.destroy)
      ext_btn.pack()

  def add_item_helper(self, window):
      # This is just a helper function to make sure the window exits after the item is added
      print("item helper is called")
      self.add_item()
      window.destroy()
      print("item helped call is done")

  # Creates inner window when pressing help button to help user understand app
  def help_box(self):
      help_window = ttk.Tk()
      help_window.title('Help')
      help_window.geometry('200x200')
      help_message = '''Hello, To Use this program start by writing your task in this format, "#: Task". Example: 1: Buy Eggs. The # denotes priority with 1 being the highest and 5 the lowest.'''

      help_txt = ttk.Message(help_window, text=help_message)
      help_txt.pack()

      help_exit = ttk.Button(help_window, text='Exit', command=help_window.destroy)
      help_exit.pack()

  # This returns value from add textbox
  def get_add_text(self):
      return self.add_txt.get('1.0', 'end-1c')

  # This returns value from due date entry
  def get_due_text(self):
      return self.due_entry.get()

  # This returns value from location textbox
  def get_location_text(self):
      return self.location_text.get('1.0', 'end-1c')

  # This returns value from priority textbox
  def get_priority_text(self):
      return self.priority_entry.get('1.0', 'end-1c')

  # This returns text to make it appear in listbox
  def add_item(self):
      print("add item is called")
      P = Task(self.get_add_text(),self.get_location_text(),self.get_due_text(),self.get_priority_text())
      List.append(P)
      self.list_txt.insert(ttk.END, 'Task: '+self.get_add_text()+' Due: '+self.get_due_text()+' At: '+self.get_location_text()+' Priority: '+self.get_priority_text())

  # This deletes an item from the listbox
  def delete_items(self):
      selection = self.list_txt.curselection()
      for t in List:
          if t.getEvent() == self.list_txt.get(selection[0]):
              List.remove(t)
      self.list_txt.delete(selection[0])

  # This moves an item from task list to completed list
  def completed_task(self):
      if len(self.list_txt.curselection()) != 0:
          selection1 = self.list_txt.curselection()
          selection = self.list_txt.get(self.list_txt.curselection())
          self.com_txt.insert(ttk.END,selection)
          # Don't know why, but commenting this out makes the DONE button work on items in the list
          # for t in List:
          #     if str(t) == self.list_txt.get(selection1[0]):
          #         List.remove(t)
          self.list_txt.delete(selection1[0])

  def delete_all(self):
      for t in List:
          List.remove(t)
      self.list_txt.delete(0, 'end')

      




if __name__ == "__main__":
  root = ttk.Tk()
  root.title('Slug To Do List')
  todolist = SlugToDoList(root)
  todolist.pack()
  root.mainloop()

