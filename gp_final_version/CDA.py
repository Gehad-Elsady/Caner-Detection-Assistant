# C:\Users\user\Desktop\figmas\build\build\assets\all_Pics
# firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json
import os
from datetime import datetime
from fpdf import FPDF
from tkinter import filedialog
from pathlib import Path
from tkinter import *
import json
import re
from tkinter import ttk, filedialog
from tkinter.ttk import Treeview, Combobox
from roboflow import Roboflow 
import firebase_admin
from PIL.ImageDraw import ImageDraw
from PIL.ImageFont import ImageFont
from firebase_admin import credentials
from firebase_admin import firestore
from PIL import ImageTk, Image, ImageDraw, ImageFont
import textwrap
import torch 
import aspose.pdf as ap



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\user\Desktop\figmas\build\build\assets\all_Pics")

cred = credentials.Certificate(
    r"firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json")

 

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
db = firestore.client()



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class AdminFrame:
    def create_frame(self, window):
        self.window = window
        self.admin_frame = Frame(window, width=1530, height=790)
        self.admin_canvas = Canvas(self.admin_frame, bg="#051747", height=790, width=1530, bd=0, highlightthickness=0,
                                   relief="ridge")
        self.admin_canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(file=relative_to_assets("ad_image_1.png"))
        self.image_1 = self.admin_canvas.create_image(765.0, 395.0, image=self.image_image_1)
        self.entry_image_1 = PhotoImage(file=relative_to_assets("ad_entry_1.png"))
        self.entry_bg_1 = self.admin_canvas.create_image(470.0, 245.0, image=self.entry_image_1)
        self.entry_1 = Entry(self.admin_canvas, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=316.0, y=221.0, width=308.0, height=46.0)
        self.entry_image_2 = PhotoImage(file=relative_to_assets("ad_entry_2.png"))
        self.entry_bg_2 = self.admin_canvas.create_image(470.0, 328.0, image=self.entry_image_2)
        self.entry_2 = Entry(self.admin_canvas, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, show="*")
        self.entry_2.place(x=317.0, y=303.0, width=306.0, height=48.0)
        self.entry_image_3 = PhotoImage(file=relative_to_assets("ad_entry_3.png"))
        self.entry_bg_3 = self.admin_canvas.create_image(470.0, 407.0, image=self.entry_image_3)
        self.entry_3 = Entry(self.admin_canvas, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, show="*")
        self.entry_3.place(x=317.0, y=382.0, width=306.0, height=48.0)
        self.button_image_3 = PhotoImage(file=relative_to_assets("ad_button_3.png"))
        self.button_3 = Button(self.admin_canvas, image=self.button_image_3, borderwidth=0, highlightthickness=0,
                               command=self.logout, relief="flat")
        self.button_3.place(x=1329.0, y=41.0, width=140.0, height=48.0)
        self.button_image_1 = PhotoImage(file=relative_to_assets("ad_button_1.png"))
        self.button_1 = Button(self.admin_canvas, image=self.button_image_1, borderwidth=0, highlightthickness=0,
                               command=self.save_data, relief="flat")
        self.button_1.place(x=200.0, y=455.0, width=246.0, height=63.0)
        self.button_image_2 = PhotoImage(file=relative_to_assets("ad_button_2.png"))
        self.button_2 = Button(self.admin_canvas, image=self.button_image_2, borderwidth=0, highlightthickness=0,
                               command=self.delete_selected_row, relief="flat")
        self.button_2.place(x=1250.0, y=130.0, width=246.0, height=63.0)
        self.image_image_2 = PhotoImage(file=relative_to_assets("ad_image_2.png"))
        self.image_2 = self.admin_canvas.create_image(1098.0, 481.0, image=self.image_image_2)
        self.message_label_1 = self.admin_canvas.create_text(250.0, 600.0, anchor="w", text="", fill="#FFFFFF",
                                                             font=("Arial", 14))
        self.message_label_2 = self.admin_canvas.create_text(100.0, 600.0, anchor="w", text="", fill="#FFFFFF",
                                                             font=("Arial", 10))

    def __init__(self, window):
        # callbacks ##############################
        self.al7aga_aly_almafrood_a3mlha = {}
        # UI ##############################
        self.window = {}
        self.admin_frame = {}
        self.admin_canvas = {}
        self.image_image_1 = {}
        self.image_1 = {}
        self.entry_image_1 = {}
        self.entry_bg_1 = {}
        self.entry_1 = {}
        self.entry_image_2 = {}
        self.entry_bg_2 = {}
        self.entry_2 = {}
        self.entry_image_3 = {}
        self.entry_bg_3 = {}
        self.entry_3 = {}
        self.button_image_3 = {}
        self.button_3 = {}
        self.button_image_1 = {}
        self.button_1 = {}
        self.button_image_2 = {}
        self.button_2 = {}
        self.image_image_2 = {}
        self.image_2 = {}
        self.message_label_1 = {}
        self.message_label_2 = {}
        self.tree = {}
        self.dr_id_var={}
        # UI ##############################
        self.create_frame(window)

    def edeeny_al7aga_aly_almafrood_a3mlha(self, hya_de_al7aga):
        self.al7aga_aly_almafrood_a3mlha = hya_de_al7aga

    def logout(self):
        # logic
        self.al7aga_aly_almafrood_a3mlha()

    def save_data(self):
        entry1_value = self.entry_1.get()
        entry2_value = self.entry_2.get()
        self.admin_canvas.itemconfig(self.message_label_1, text="")
        self.admin_canvas.itemconfig(self.message_label_2, text="")
        cred = credentials.Certificate(
            r"firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json")

        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        doctors_ref = db.collection('doctors')
        query = doctors_ref.where('username', '==', entry1_value).limit(1)
        doctors = query.get()
        self.admin_canvas.itemconfig(self.message_label_1, text="")
        self.admin_canvas.itemconfig(self.message_label_2, text="")
        if not entry1_value or not entry2_value:
            self.admin_canvas.itemconfig(self.message_label_1, text="Please complete the data")
            return
        if len(doctors) > 0:
            self.admin_canvas.itemconfig(self.message_label_1, text="User already exists")

        elif len(entry2_value) < 6 or not re.search(r"\d", entry2_value) or not re.search(r"[a-zA-Z]", entry2_value):
            self.admin_canvas.itemconfig(self.message_label_2,
                                         text="Password should be at least 6 characters long and contain a mix of letters and numbers")
            return
        else:
            entry3_value = self.entry_3.get()
            self.admin_canvas.itemconfig(self.message_label_1, text="Doctor added successfully")
            if entry2_value == entry3_value:
                max_dr = db.collection('doctors').order_by('id', direction=firestore.Query.DESCENDING).limit(1).get()
                new_dr = 1
                if max_dr:
                    for doc in max_dr:
                        new_dr = doc.get('id') + 1
                data = {'username': entry1_value, 'password': entry2_value, 'id': new_dr, 'dr': 1}
                db.collection('doctors').add(data)
                self.tree.insert("", "end", values=(new_dr, entry1_value))
            else:
                self.admin_canvas.itemconfig(self.message_label_1, text="Password is not identical")

    def populate_treeview(self):
        # Clear existing items in the Treeview
        self.tree.delete(*self.tree.get_children())
        # Fetch updated data from Firestore
        cred = credentials.Certificate(
            r"firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json")

        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        doctors_ref = db.collection('doctors').order_by('id', direction=firestore.Query.ASCENDING)
        doctors_data = doctors_ref.get()
        # Populate the Treeview with the updated data
        for doctor in doctors_data:
            doc_data = doctor.to_dict()
            self.tree.insert("", "end", values=(doc_data["id"], doc_data["username"]))

    def delete_selected_row(self):
        self.admin_canvas.itemconfig(self.message_label_1, text="")
        self.admin_canvas.itemconfig(self.message_label_2, text="")

        selected_item = self.tree.focus()
        if selected_item:
            values = self.tree.item(selected_item, "values")
            id_value = int(values[0])
            # Delete the selected doctor from Firestore
            cred = credentials.Certificate(
                r"firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json")

            if not firebase_admin._apps:
                firebase_admin.initialize_app(cred)
            db = firestore.client()
            doctor_ref = db.collection('doctors').where('id', '==', id_value)
            for doc in doctor_ref.stream():
                doc.reference.delete()
            # Update the IDs of doctors higher than the deleted one
            doctors_ref = db.collection('doctors').where('id', '>', id_value)
            for doc in doctors_ref.stream():
                doc.reference.update({'id': doc.get('id') - 1})
            # Delete the selected item from the Treeview
            self.tree.delete(selected_item)

            self.admin_canvas.itemconfig(self.message_label_1, text="")
            self.admin_canvas.itemconfig(self.message_label_1, text="Doctor deleted")
            # Repopulate the Treeview with updated data
            self.populate_treeview()

    def show_tree(self):
        self.tree = ttk.Treeview(columns=("id", "Username"), show="headings")
        self.tree.place(x=690, y=198, width=810, height=567)
        self.tree.heading("id", text="id")
        self.tree.heading("Username", text="Username")
        cred = credentials.Certificate(
            r"firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json")

        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        doctors_ref = db.collection('doctors').order_by('id', direction=firestore.Query.ASCENDING)
        doctors_data = doctors_ref.get()
        for doctor in doctors_data:
            doc_data = doctor.to_dict()
            self.tree.insert("", "end", values=(doc_data["id"], doc_data["username"]))

    def show(self):
        self.show_tree()
        self.admin_canvas.pack()
        self.admin_frame.pack()
        

    def hide(self):
        self.tree.place(x=0, y=0, width=0, height=0)
        self.tree.grid_remove()
        self.tree.pack_forget()
        self.admin_canvas.pack_forget()
        self.admin_frame.pack_forget()

#600.0, 200.0
class SettingsFrame:
    def create_frame(self, window ):
        self.settings_frame = Frame(window, width=1530, height=790)
        self.settings_canvas = Canvas(self.settings_frame, bg="#051747", height=790, width=1530, bd=0,
                                      highlightthickness=0, relief="ridge")
        self.settings_canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(file=relative_to_assets("st_image_1.png"))
        self.image_1 = self.settings_canvas.create_image(773.0, 395.0, image=self.image_image_1)
         
            
        self.dr_id_var = IntVar()
        self.entry_image_1 = PhotoImage(file=relative_to_assets("st_entry_2.png"))
        self.entry_bg_1 = self.settings_canvas.create_image(709.0, 200.0, image=self.entry_image_1)
        self.entry_1 = Entry(self.settings_canvas, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0,
                             textvariable=self.dr_id_var)
        self.entry_1.place(x=555.0, y=176.0, width=306.0, height=48.0)
        
        
        
        self.old_pass_var = StringVar()
        self.entry_image_2 = PhotoImage(file=relative_to_assets("st_entry_2.png"))
        self.entry_bg_2 = self.settings_canvas.create_image(709.0, 294.0, image=self.entry_image_2)
        self.entry_2 = Entry(self.settings_canvas, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0,
                             textvariable=self.old_pass_var)
        self.entry_2.place(x=556.0, y=269.0, width=306.0, height=48.0)
        self.nw_pass_var = StringVar()
        self.entry_image_3 = PhotoImage(file=relative_to_assets("st_entry_3.png"))
        self.entry_bg_3 = self.settings_canvas.create_image(709.0, 490.0, image=self.entry_image_3)
        self.entry_3 = Entry(self.settings_canvas, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0,
                             textvariable=self.nw_pass_var)
        self.entry_3.place(x=556.0, y=465.0, width=306.0, height=48.0)
        self.cnf_pass_var = StringVar()
        self.entry_image_4 = PhotoImage(file=relative_to_assets("st_entry_4.png"))
        self.entry_bg_4 = self.settings_canvas.create_image(709.0, 392.0, image=self.entry_image_4)
        self.entry_4 = Entry(self.settings_canvas, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0,
                             textvariable=self.cnf_pass_var)
        self.entry_4.place(x=556.0, y=367.0, width=306.0, height=48.0)
        self.back_button_image = PhotoImage(file=relative_to_assets("st_button_2.png"))
        self.back_button = Button(self.settings_canvas, image=self.back_button_image, borderwidth=0,
                                  highlightthickness=0,
                                  command=lambda: self.go_to_home_frame(), relief="flat")
        self.back_button.place(x=1260.0, y=48.0, width=140.0, height=48.0)
        self.button_image_1 = PhotoImage(file=relative_to_assets("st_button_1.png"))
        self.button_1 = Button(self.settings_canvas, image=self.button_image_1, borderwidth=0, highlightthickness=0,
                               command=lambda: self.update_pass(), relief="flat")
        self.button_1.place(x=621.0, y=534.0, width=136.0, height=80.0)
        self.message_label_1 = self.settings_canvas.create_text(615.0, 625.0, anchor="w", text="", fill="#FFFFFF",
                                                                font=("Arial", 12, "bold"), )
        self.message_label_2 = self.settings_canvas.create_text(900.0, 367.0, anchor="w", text="", fill="#FFFFFF",
                                                                font=("Arial", 12, "bold"), )

    def __init__(self, window , json_name):
        # fields variables
        self.json_name = json_name
        self.dr_id_var ={}
        self.dr_id_var = {}
        self.nw_pass_var = {}
        self.cnf_pass_var = {}
        self.old_pass_var = {}
        
        # callbacks ##############################
        self.go_to_home_callback = {}
        # UI ##############################
        self.settings_frame = {}
        self.settings_canvas = {}
        self.image_image_1 = {}
        self.image_1 = {}
        self.message_label_1 = {}
        self.entry_image_2 = {}
        self.entry_bg_2 = {}
        self.entry_2 = {}
        self.entry_image_3 = {}
        self.entry_bg_3 = {}
        self.entry_3 = {}
        self.entry_image_4 = {}
        self.entry_bg_4 = {}
        self.entry_4 = {}
        self.back_button_image = {}
        self.back_button = {}
        self.button_image_1 = {}
        self.button_1 = {}
        self.message_label_1 = {}
        self.message_label_2 = {}
        # UI ##############################
        self.create_frame(window)

    def set_go_to_home_callback(self, callback):
        self.go_to_home_callback = callback

    def go_to_home_frame(self):
        self.go_to_home_callback()

    def update_pass(self):
        old_pass = self.old_pass_var.get()
        nw_pass = self.nw_pass_var.get()
        conf_pass = self.cnf_pass_var.get()
        s = self.cnf_pass_var.get()
        self.settings_canvas.itemconfig(self.message_label_1, text="")
        self.settings_canvas.itemconfig(self.message_label_2, text="")
        s = self.old_pass_var.get()
        cred = credentials.Certificate(
            r"firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json")

        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        dr_ref = db.collection('doctors')
        query = dr_ref.where('id', '==', self.dr_id_var.get()).where('password', '==', old_pass).limit(1).get()
        documents = [doc for doc in query]
        if not self.dr_id_var or not old_pass or not nw_pass or not conf_pass:
            # lbl=Label(text = "Please complete the data", fg="white", font=("Arial", 12, "bold"),bg='red' )
            self.settings_canvas.itemconfig(self.message_label_1, text="Please complete the data")
            # lbl.place(x = 615 , y = 620)
            return
        if len(query) != 0:
            if len(nw_pass) < 6 or not re.search(r"\d", nw_pass) or not re.search(r"[a-zA-Z]", nw_pass):
                self.settings_canvas.itemconfig(self.message_label_2,
                                                text="Password should be at least 6 characters long\n and contain a mix of letters and numbers")
                return
            else:
                if nw_pass == conf_pass:
                    document_ref = documents[0].reference
                    document_ref.update({'password': nw_pass})
                    self.settings_canvas.itemconfig(self.message_label_1, text="Password updated")
                else:
                    self.settings_canvas.itemconfig(self.message_label_2,
                                                    text="New password and confirmed password not matched")
        else:
            self.settings_canvas.itemconfig(self.message_label_1, text="No such doctor")

    def show(self):
        self.settings_canvas.pack()
        self.settings_frame.pack()
        

    def hide(self):
        self.settings_canvas.pack_forget()
        self.settings_frame.pack_forget()


class LoginFrame:
    def create_frame(self, window):
        self.login_frame = Frame(window, width=1530, height=790)
        self.login_canvas = Canvas(self.login_frame, bg="#051747", height=790, width=1530, bd=0, highlightthickness=0,
                                   relief="ridge")
        self.login_canvas.place(x=0, y=0)

        self.tk_login_image = ImageTk.PhotoImage(Image.open(relative_to_assets("lg_image_1.png")))
        self.login_image = self.login_canvas.create_image(768.0, 395.0, image=self.tk_login_image)
        self.tk_id_entry_image = ImageTk.PhotoImage(Image.open(relative_to_assets("lg_entry_1.png")))
        self.id_entry_image = self.login_canvas.create_image(757.0, 349.0, image=self.tk_id_entry_image)
        self.id_entry = Entry(self.login_canvas, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0,
                              textvariable=self.doctor_id_var)
        self.id_entry.place(x=603.0, y=325.0, width=308.0, height=46.0)
        self.tk_pass_entry_image = ImageTk.PhotoImage(Image.open(relative_to_assets("lg_entry_2.png")))
        self.pass_entry_bg = self.login_canvas.create_image(757.0, 466.0, image=self.tk_pass_entry_image)
        self.pass_entry = Entry(self.login_canvas, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, show='*',
                                textvariable=self.doctor_pass_var)
        self.pass_entry.place(x=604.0, y=441.0, width=306.0, height=48.0)
        self.login_button_image = ImageTk.PhotoImage(Image.open(relative_to_assets("lg_button_1.png")))
        self.login_button = Button(self.login_canvas, image=self.login_button_image, borderwidth=0,
                                   highlightthickness=0,
                                   command=lambda: self.login_and_open_file(), relief="flat")
        self.login_button.place(x=651.0, y=512.0, width=184.0, height=74.0)

    def __init__(self, window, json_name):
        # fields variables
        self.json_name = json_name
        self.doctor_id_var = IntVar()
        self.doctor_id_var.set("")
        self.doctor_pass_var = StringVar()
        # callbacks ##############################
        self.login_callback = {}
        # UI ##############################
        self.login_frame = {}
        self.login_canvas = {}
        self.tk_login_image = {}
        self.login_image = {}
        self.tk_id_entry_image = {}
        self.id_entry_image = {}
        self.id_entry = {}
        self.tk_pass_entry_image = {}
        self.pass_entry_bg = {}
        self.pass_entry = {}
        self.login_button_image = {}
        self.login_button = {}
        self.no_lbl = {}
        # UI ##############################
        self.create_frame(window)

    def set_login_callback(self, callback):
        self.login_callback = callback

    def login_and_open_file(self):
        self.login_canvas.itemconfig(self.no_lbl, text="")
        cred = credentials.Certificate(
            r"firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json")

        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        data = {'dr_id': self.doctor_id_var.get()}
        with open(self.json_name, 'w') as file:
            json.dump(data, file)
            print("set",self.doctor_id_var.get() )
             
        doc_ref = db.collection('doctors').where('id', '==', self.doctor_id_var.get()).where('password', '==',
                                                                                             self.doctor_pass_var.get()).limit(
            1).stream()
        documents = [doc for doc in doc_ref]

        if documents:
            doc = documents[0]
            role = doc.get('dr')
            self.login_callback(role)
        else:
            print("Wrong doctor password or ID")
            self.no_lbl = self.login_canvas.create_text(651.0, 630.0, anchor="w", text="", fill="#FFFFFF",
                                                        font=("Arial", 14))
            self.login_canvas.itemconfig(self.no_lbl, text="Wrong doctor password or ID")
            
    def loged(self) : 
        lg = 1 
   
    def show(self):
        self.login_canvas.pack()
        self.login_frame.pack()
        

    def hide(self):
        self.login_canvas.pack_forget()
        self.login_frame.pack_forget()
    

class HomeFrame:
    def create_frame(self, window):
        self.home_frame = Frame(window, width=1530, height=790)
        self.home_canvas = Canvas(self.home_frame, bg="#051747", height=790, width=1530, bd=0, highlightthickness=0,
                                  relief="ridge")
        self.home_canvas.place(x=0, y=0)
        self.tk_home_image = ImageTk.PhotoImage(Image.open(relative_to_assets("hf_image_1.png")))
        self.home_image = self.home_canvas.create_image(765.0, 395.0, image=self.tk_home_image)

        self.tk_home_button_1_image = ImageTk.PhotoImage(Image.open(relative_to_assets("hf_button_1.png")))
        self.tk_home_button_2_image = ImageTk.PhotoImage(Image.open(relative_to_assets("hf_button_2.png")))
        self.tk_home_button_3_image = ImageTk.PhotoImage(Image.open(relative_to_assets("hf_button_3.png")))
        self.tk_home_button_4_image = ImageTk.PhotoImage(Image.open(relative_to_assets("hf_button_4.png")))

        self.home_button_1 = Button(self.home_canvas, image=self.tk_home_button_1_image, borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: self.pt_callback(), relief="flat")
        self.home_button_2 = Button(self.home_canvas, image=self.tk_home_button_2_image, borderwidth=0,
                                    highlightthickness=0, command=lambda: self.login_callback(), relief="flat")
        self.home_button_3 = Button(self.home_canvas, image=self.tk_home_button_3_image, borderwidth=0,
                                    highlightthickness=0, command=lambda: self.ex_opts_callback(), relief="flat")
        self.home_button_4 = Button(self.home_canvas, image=self.tk_home_button_4_image, borderwidth=0,
                                    highlightthickness=0, command=lambda: self.settings_callback(), relief="flat")

        self.home_button_1.place(x=84.0, y=94.0, width=413.0, height=376.0)
        self.home_button_2.place(x=1329.0, y=41.0, width=140.0, height=48.0)
        self.home_button_3.place(x=567.0, y=375.0, width=402.0, height=365.0)
        self.home_button_4.place(x=1209.0, y=42.0, width=65.0, height=51.0)

    def __init__(self, window):
        # callbacks
        self.login_callback = {}
        self.ex_opts_callback = {}
        self.settings_callback = {}
        self.pt_callback = {}
        # UI ##############################
        self.home_frame = {}
        self.home_canvas = {}
        self.tk_home_image = {}
        self.home_image = {}
        self.tk_home_button_1_image = {}
        self.tk_home_button_2_image = {}
        self.tk_home_button_3_image = {}
        self.tk_home_button_4_image = {}
        self.home_button_1 = {}
        self.home_button_2 = {}
        self.home_button_3 = {}
        self.home_button_4 = {}
        # UI ##############################
        self.create_frame(window)

    def login_callback(self):
        print("we are in login_callback")
        self.login_callback()

    def set_login_callback(self, callback):
        self.login_callback = callback

    def login_callback(self):
        print("we are in login_callback")
        self.login_callback()

    def set_login_callback(self, callback):
        self.login_callback = callback

    def ex_opts_callback(self):
        print("we are in ex_opts_callback")
        self.ex_opts_callback()

    def set_ex_opts_callback(self, callback):
        self.ex_opts_callback = callback

    def settings_callback(self):
        print("we are in settings_callback")
        self.settings_callback()

    def set_settings_callback(self, callback):
        self.settings_callback = callback

    def set_pt_callback(self, callback):
        self.pt_callback = callback

    def show(self):
        self.home_canvas.pack()
        self.home_frame.pack()
        

    def hide(self):
        self.home_canvas.pack_forget()
        self.home_frame.pack_forget()


class ExamineOptionsFrame:
    def create_frame(self, window):
        self.ex_opt_frame = Frame(window, width=1530, height=790)
        self.ex_opt_canvas = Canvas(self.ex_opt_frame, bg="#051747", height=790, width=1530, bd=0, highlightthickness=0,
                                    relief="ridge")
        self.ex_opt_canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(file=relative_to_assets("ex_opt_image_1.png"))
        self.button_image_1 = PhotoImage(file=relative_to_assets("ex_opt_button_1.png"))
        self.image_1 = self.ex_opt_canvas.create_image(765.0, 395.0, image=self.image_image_1)
        self.button_1 = Button(self.ex_opt_canvas, image=self.button_image_1, borderwidth=0, highlightthickness=0,
                               command=lambda: self.exm_skin(),
                               relief="flat")
        self.button_1.place(x=563.0, y=368.0, width=422.0, height=369.0)
        self.button_image_2 = PhotoImage(file=relative_to_assets("ex_opt_button_2.png"))
        self.button_2 = Button(self.ex_opt_canvas, image=self.button_image_2, borderwidth=0, highlightthickness=0,
                               command=lambda: self.logout(),
                               relief="flat")
        self.button_2.place(x=1313.0, y=52.0, width=140.0, height=48.0)
        self.button_image_3 = PhotoImage(file=relative_to_assets("ex_opt_button_3.png"))
        self.button_3 = Button(self.ex_opt_canvas, image=self.button_image_3, borderwidth=0, highlightthickness=0,
                               command=lambda: self.home(),
                               relief="flat")
        self.button_3.place(x=1313.0, y=130.0, width=140.0, height=48.0)
        self.button_image_4 = PhotoImage(file=relative_to_assets("ex_opt_button_4.png"))
        self.button_4 = Button(self.ex_opt_canvas, image=self.button_image_4, borderwidth=0, highlightthickness=0,
                               command=lambda: self.exm_pbs(),
                               relief="flat")
        self.button_4.place(x=94.0, y=100.0, width=413.0, height=376.0)

    def __init__(self, window):
        # callbacks ##############################
        self.home_callback = {}
        self.logout_callback = {}
        self.exm_pbs_callback = {}
        self.exm_skin_callback = {}
        # UI ##############################
        self.ex_opt_frame = {}
        self.ex_opt_canvas = {}
        self.image_image_1 = {}
        self.image_1 = {}
        self.button_image_1 = {}
        self.button_1 = {}
        self.button_image_2 = {}
        self.button_2 = {}
        self.button_image_3 = {}
        self.button_3 = {}
        self.button_image_4 = {}
        self.button_4 = {}
        # UI ##############################
        self.create_frame(window)

    def logout(self):
        self.logout_callback()

    def set_logout_callback(self, callback):
        self.logout_callback = callback

    def home(self):
        self.home_callback()

    def set_home_callback(self, callback):
        self.home_callback = callback

    def exm_skin(self):
        self.exm_skin_callback()

    def exm_pbs(self):
        self.exm_pbs_callback()

    def set_exm_pbs_callback(self, callback):
        self.exm_pbs_callback = callback

    def set_exm_skin_callback_callback(self, callback):
        self.exm_skin_callback = callback

    def show(self):
        self.ex_opt_canvas.pack()
        self.ex_opt_frame.pack()
        

    def hide(self):
        self.ex_opt_canvas.pack_forget()
        self.ex_opt_frame.pack_forget()


class PatientFrame:
    def create_frame(self, window):
        self.pt_frame = Frame(window, width=1530, height=790)
        self.pt_canvas = Canvas(self.pt_frame, bg="#051747", height=790, width=1530, bd=0, highlightthickness=0,
                                relief="ridge")
        self.pt_canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("pt_image_1.png"))
        self.image_1 = self.pt_canvas.create_image(
            765.0,
            395.0,
            image=self.image_image_1
        )

        self.name_entry_image = PhotoImage(
            file=relative_to_assets("pt_entry_1.png"))
        self.name_entry_bg = self.pt_canvas.create_image(
            371.0,
            244.5,
            image=self.name_entry_image
        )
        self.name_entry = Entry(self.pt_canvas,
                                bd=0,
                                bg="#D9D9D9",
                                fg="#000716",
                                highlightthickness=0
                                )
        self.name_entry.place(
            x=254.5,
            y=220.0,
            width=233.0,
            height=47.0
        )

        self.search_entry_image = PhotoImage(
            file=relative_to_assets("pt_entry_2.png"))
        self.search_entry_bg = self.pt_canvas.create_image(
            796.0,
            234.5,
            image=self.search_entry_image
        )
        self.search_entry = Entry(self.pt_canvas,
                                  bd=0,
                                  bg="#D9D9D9",
                                  fg="#000716",
                                  highlightthickness=0
                                  )
        self.search_entry.place(
            x=679.5,
            y=210.0,
            width=233.0,
            height=47.0
        )

        self.phone_entry_image = PhotoImage(
            file=relative_to_assets("pt_entry_3.png"))
        self.phone_entry_bg = self.pt_canvas.create_image(
            371.0,
            428.5,
            image=self.phone_entry_image
        )
        self.phone_entry = Entry(self.pt_canvas,
                                 bd=0,
                                 bg="#D9D9D9",
                                 fg="#000716",
                                 highlightthickness=0
                                 )
        self.phone_entry.place(
            x=254.5,
            y=404.0,
            width=233.0,
            height=47.0
        )

        self.dob_entry_image = PhotoImage(
            file=relative_to_assets("pt_entry_4.png"))
        self.dob_entry_bg = self.pt_canvas.create_image(
            371.0,
            532.5,
            image=self.dob_entry_image
        )
        self.dob_entry = Entry(self.pt_canvas,
                               bd=0,
                               bg="#D9D9D9",
                               fg="#000716",
                               highlightthickness=0
                               )
        self.dob_entry.place(
            x=254.5,
            y=508.0,
            width=233.0,
            height=47.0
        )

        self.gender_entry_image = PhotoImage(
            file=relative_to_assets("pt_entry_5.png"))
        self.gender_entry_bg = self.pt_canvas.create_image(
            371.0,
            336.5,
            image=self.gender_entry_image
        )
        self.gender_entry = Entry(self.pt_canvas,
                                  bd=0,
                                  bg="#D9D9D9",
                                  fg="#000716",
                                  highlightthickness=0
                                  )
        self.gender_entry.place(
            x=254.5,
            y=312.0,
            width=233.0,
            height=47.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("pt_button_1.png"))
        self.button_1 = Button(self.pt_canvas,
                               image=self.button_image_1,
                               borderwidth=0,
                               highlightthickness=0,
                               command=lambda: self.login(),
                               relief="flat"
                               )
        self.button_1.place(
            x=1278.0,
            y=48.0,
            width=140.0,
            height=48.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("pt_button_2.png"))
        self.button_2 = Button(self.pt_canvas,
                               image=self.button_image_2,
                               borderwidth=0,
                               highlightthickness=0,
                               command=lambda: self.home(),
                               relief="flat"
                               )
        self.button_2.place(
            x=1278.0,
            y=131.0,
            width=140.0,
            height=48.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("pt_button_3.png"))
        self.button_3 = Button(self.pt_canvas,
                               image=self.button_image_3,
                               borderwidth=0,
                               highlightthickness=0,
                               command=lambda: self.add_patient(),
                               relief="flat"
                               )
        self.button_3.place(
            x=286.0,
            y=657.0,
            width=169.0,
            height=53.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("pt_button_4.png"))
        self.button_4 = Button(self.pt_canvas,
                               image=self.button_image_4,
                               borderwidth=0,
                               highlightthickness=0,
                               command=lambda: self.delete_patient(),
                               relief="flat"
                               )
        self.button_4.place(
            x=796.0,
            y=663.0,
            width=191.0,
            height=53.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("pt_button_5.png"))
        self.button_5 = Button(self.pt_canvas,
                               image=self.button_image_5,
                               borderwidth=0,
                               highlightthickness=0,
                               command=lambda: self.update_patient(),
                               relief="flat"
                               )
        self.button_5.place(
            x=1025.0,
            y=664.0,
            width=229.0,
            height=49.84619140625
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("pt_button_6.png"))
        self.button_6 = Button(self.pt_canvas,
                               image=self.button_image_6,
                               borderwidth=0,
                               highlightthickness=0,
                               command=lambda: self.show_reports(),
                               relief="flat"
                               )
        self.button_6.place(
            x=1278.0,
            y=657.0,
            width=169.0,
            height=53.0
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("pt_button_7.png"))
        self.button_7 = Button(self.pt_canvas,
                               image=self.button_image_7,
                               borderwidth=0,
                               highlightthickness=0,
                               command=lambda: self.search_patient(),
                               relief="flat"
                               )
        self.button_7.place(
            x=987.0,
            y=203.31982421875,
            width=169.0,
            height=49.2900390625
        )

        self.pt_canvas.create_rectangle(
            599.0,
            269.0,
            1475.0,
            630.0,
            fill="#F1F1F3",
            outline="")

        self.gender_var = StringVar()
        self.gender_entry = Combobox(self.pt_canvas,
                                     values=["Female", "Male"],
                                     textvariable=self.gender_var,
                                     state="readonly",
                                     width=22,
                                     )
        self.gender_entry.place(
            x=254.5,
            y=312.0,
            width=233.0,
            height=47.0
        )

        self.table = Text(self.pt_canvas,
                          bd=0,
                          bg="#F1F1F3",
                          fg="#000716",
                          highlightthickness=0,
                          font=("Arial", 12),
                          )

        self.table = Treeview(self.pt_canvas,
                              columns=('ID', 'Name', 'Gender', 'Date Of Birth', 'Phone Number', 'Number Of Reports'),
                              show='headings')
        self.table.place(x=604, y=274, width=870, height=356)

        self.table.column("ID", stretch=NO, width=110)
        self.table.heading('ID', text='ID')
        self.table.column("Name", stretch=NO, width=160)
        self.table.heading('Name', text='Name')
        self.table.column("Gender", stretch=NO, width=150)
        self.table.heading('Gender', text='Gender')
        self.table.column("Date Of Birth", stretch=NO, width=150)
        self.table.heading('Date Of Birth', text='Date Of Birth')
        self.table.column("Phone Number", stretch=NO, width=150)
        self.table.heading('Phone Number', text='Phone Number')
        self.table.column("Number Of Reports", stretch=NO, width=150)
        self.table.heading('Number Of Reports', text='Number of Reports')
        # table.grid(row=0, column=0, sticky='nsew')
        self.error_label = self.pt_canvas.create_text(
            200,
            600,
            text="",
            fill="red",
            font=("Arial", 12)
        )
        self.show_all()

    def __init__(self, window):
        ###callbacks##
        self.logout_callback = {}
        self.home_callback = {}
        self.settings_callback = {}
        self.pt_callback = {}
        self.show_reports_call_back = {}
        ###########
        self.pt_frame = {}
        self.pt_canvas = {}
        self.image_image_1 = {}
        self.image_1 = {}

        self.name_entry_image = {}
        self.name_entry_bg = {}
        self.name_entry = {}
        self.search_entry_image = {}
        self.search_entry_bg = {}
        self.search_entry = {}
        self.phone_entry_image = {}
        self.phone_entry_bg = {}
        self.phone_entry = {}
        self.dob_entry_image = {}
        self.dob_entry_bg = {}
        self.dob_entry = {}
        self.gender_entry_image = {}
        self.gender_entry_bg = {}
        self.gender_entry = {}
        self.button_image_1 = {}
        self.button_1 = {}
        self.button_image_2 = {}
        self.button_2 = {}
        self.button_image_3 = {}
        self.button_3 = {}
        self.button_image_4 = {}
        self.button_4 = {}
        self.button_image_5 = {}
        self.button_5 = {}
        self.button_image_6 = {}
        self.button_6 = {}
        self.button_image_7 = {}
        self.button_7 = {}
        self.gender_var = {}
        self.gender_entry = {}
        self.table = {}
        self.error_label = {}
        self.create_frame(window)

    def show_all(self):
        cred = credentials.Certificate(
            r"firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json")

        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        patients_ref = db.collection('patients')
        query = patients_ref.order_by('id').get()  # Order the data by ID

        self.table.delete(*self.table.get_children())  # Clear existing table rows

        for doc in query:
            reports_ref = db.collection('reports')
            report_query = reports_ref.where('patient_id', '==', doc.id).get()

            data = doc.to_dict()
            self.table.insert('', 'end',
                              values=(
                                  data['id'], data['name'], data['gender'], data['DOB'], data['phone'],
                                  len(report_query)))

    def set_go_to_home_callback(self, callback):
        self.home_callback = callback

    def set_go_to_login_callback(self, callback):
        self.logout_callback = callback

    def go_to_login_frame(self):
        self.logout_callback()

    def login(self):
        self.logout_callback()

    def home(self):
        self.home_callback()

    def add_patient(self):
        name = self.name_entry.get()
        gender = self.gender_var.get()
        phone_number = self.phone_entry.get()
        dob = self.dob_entry.get()

        entry1_value = self.name_entry.get()
        entry3_value = self.gender_var.get()
        entry4_value = self.phone_entry.get()
        entry5_value = self.dob_entry.get()

        if not name or not gender or not phone_number or not dob:
            self.pt_canvas.itemconfig(self.error_label, text="Please complete the data")
            return
        # Check if phone number is valid
        if not (phone_number.isdigit() and len(phone_number) == 11 and phone_number.startswith(
                ("010", "011", "012", "015"))):
            self.pt_canvas.itemconfigure(self.error_label, text="Invalid phone number")
            return

        try:
            dob_date = datetime.strptime(dob, "%d/%m/%Y")
        except ValueError:
            self.pt_canvas.itemconfigure(self.error_label, text="Enter date in dd/mm/yyyy format")
            return

        try:
            dob_date = datetime.strptime(dob, "%d/%m/%Y")
        except ValueError:
            self.pt_canvas.itemconfigure(self.error_label, text="Enter date in dd/mm/yyyy format")
            return
        cred = credentials.Certificate(
            r"firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json")

        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        patients_ref = db.collection('patients')
        maxRef = patients_ref.order_by("id").limit_to_last(1).get()
        dataRef = maxRef[0] if len(maxRef) != 0 else 1
        id = dataRef.get('id')
        id = int(id) + 1

        new_patient_data = {
            'name': name,
            'gender': gender,
            'phone': phone_number,
            'id': id,
            'DOB': dob,
        }
        patients_ref.add(new_patient_data)

        # Update the table with the new patient
        self.table.insert('', 'end', values=(id, name, gender, dob, phone_number, 0))
        self.pt_canvas.itemconfigure(self.error_label, text="")

    def delete_patient(self):
        selection = self.table.selection()
        if selection:
            item_data = self.table.item(selection)
            patient_id = item_data['values'][0]
            cred = credentials.Certificate(
                r"firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json")

            if not firebase_admin._apps:
                firebase_admin.initialize_app(cred)
            db = firestore.client()
            patients_ref = db.collection('patients')
            query = patients_ref.where('id', '==', patient_id).limit(1).get()
            if len(query):
                for doc in query:
                    doc.reference.delete()
                decrement_ref = patients_ref.where('id', '>', patient_id).get()
                for doc in decrement_ref:
                    doc.reference.update({'id': doc.get('id') - 1})
                reports_ref = db.collection('reports')
                query = reports_ref.where('patient_id', '==', patient_id).get()
                for doc in query:
                    doc_id = doc.id
                    reports_ref.document(doc_id).delete()
                self.show_all()

    def update_patient(self):
        patient_id = int(self.search_entry.get())
        cred = credentials.Certificate(
            r"firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json")

        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        patients_ref = db.collection('patients')
        query = patients_ref.where('id', '==', patient_id).limit(1).get()
        if len(query) != 0:
            for doc in query:
                data = doc.to_dict()
                name = self.name_entry.get() if self.name_entry.get() else data['name']
                gender = self.gender_var.get() if self.gender_var.get() else data['gender']
                phone_number = self.phone_entry.get() if self.phone_entry.get() else data['phone']
                dob = self.dob_entry.get() if self.dob_entry.get() else data['DOB']
                updated_patient_data = {
                    'name': name,
                    'gender': gender,
                    'phone': phone_number,
                    'DOB': dob,
                }
                key = doc.id
                patients_ref.document(key).update(updated_patient_data)
            self.show_all()
        else:
            self.delete(*self.table.get_children())
            self.table.insert('', 'end', values=("Patient Not Found.", "", ""))

    def search_patient(self):
        patient_id = int(self.search_entry.get())
        cred = credentials.Certificate(
            r"firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json")

        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        patients_ref = db.collection('patients')
        query = patients_ref.where('id', '==', patient_id).get()
        if len(query) != 0:
            self.table.delete(*self.table.get_children())
            for doc in query:
                reports_ref = db.collection('reports')
                report_query = reports_ref.where('patient_id', '==', patient_id).get()
                data = doc.to_dict()
                self.table.insert('', 'end', values=(
                    data['id'], data['name'], data['gender'], data['DOB'], data['phone'], len(report_query)))
        else:
            self.table.delete(*self.table.get_children())
            self.table.insert('', 'end', values=("Patient Not Found.", "", ""))

    def show(self):
        self.pt_canvas.itemconfigure(self.error_label, text="")
        self.pt_frame.pack()
        self.pt_canvas.pack()
        

    def hide(self):
        self.pt_frame.pack_forget()
        self.pt_canvas.pack_forget()

    def show_reports(self):
        p_id = self.search_entry.get()
        data = {'patient_id': p_id}
        if (not p_id):
            self.pt_canvas.itemconfigure(self.error_label, text="Add id to the search field")
            return
        with open('patient_id.json', 'w') as file:
            json.dump(data, file)
        self.show_reports_call_back()

    def set_show_reports_call_back(self, callback):
        self.show_reports_call_back = callback


class ReportFrame:
    def __init__(self, window):
        self.open_view_callback = {}
        self.back_callback = {}
        self.logout_callback = {}
        self.report_frame = Frame(window, width=1530, height=790)
        self.report_canvas = Canvas(
            self.report_frame,
            bg="#051747",
            height=790,
            width=1530,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.report_canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("pt_rep_image_1.png"))
        self.image_1 = self.report_canvas.create_image(
            765.0,
            395.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("pt_rep_image_2.png"))
        self.image_2 = self.report_canvas.create_image(
            930.0,
            473.0,
            image=self.image_image_2
        )

        self.rep_no_entry_image = PhotoImage(file=relative_to_assets("pt_rep_entry_1.png"))
        self.rep_no_entry_bg = self.report_canvas.create_image(
            197.0,
            231.5,
            image=self.rep_no_entry_image
        )
        self.rep_no_entry = Entry(self.report_canvas,
                                  bd=0,
                                  bg="#D9D9D9",
                                  fg="#000716",
                                  highlightthickness=0
                                  )
        self.rep_no_entry.place(
            x=80.5,
            y=207.0,
            width=233.0,
            height=47.0
        )

        self.patient_id_entry_image = PhotoImage(
            file=relative_to_assets("pt_rep_entry_2.png"))
        self.patient_id_entry_bg = self.report_canvas.create_image(
            197.0,
            370.5,
            image=self.patient_id_entry_image
        )
        self.patient_id_entry = Entry(self.report_canvas,
                                      bd=0,
                                      bg="#D9D9D9",
                                      fg="#000716",
                                      highlightthickness=0
                                      )
        self.patient_id_entry.place(
            x=80.5,
            y=346.0,
            width=233.0,
            height=47.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("pt_rep_button_1.png"))
        self.button_1 = Button(self.report_canvas,
                               image=self.button_image_1,
                               borderwidth=0,
                               highlightthickness=0,
                               command=lambda: self.logout(),
                               relief="flat"
                               )
        self.button_1.place(
            x=1278.0,
            y=48.0,
            width=140.0,
            height=48.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("pt_rep_button_2.png"))
        self.button_2 = Button(self.report_canvas,
                               image=self.button_image_2,
                               borderwidth=0,
                               highlightthickness=0,
                               command=lambda: self.back(),
                               relief="flat"
                               )
        self.button_2.place(
            x=1278.0,
            y=114.0,
            width=140.0,
            height=48.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("pt_rep_button_3.png"))
        self.button_3 = Button(self.report_canvas,
                               image=self.button_image_3,
                               borderwidth=0,
                               highlightthickness=0,
                               command=lambda: self.show_report(),
                               relief="flat"
                               )
        self.button_3.place(
            x=97.0,
            y=453.0,
            width=169.0,
            height=53.0
        )

        self.table = Treeview(self.report_canvas, columns=('Number'), show='headings')
        self.table.place(x=604, y=274, width=870, height=356)

        self.table.heading('Number', text='Number')

    def show(self):
        self.report_canvas.pack()
        self.report_frame.pack()
        self.fetch_report()
        

    def hide(self):
        self.report_canvas.pack_forget()
        self.report_frame.pack_forget()

    def back(self):
        self.back_callback()

    def logout(self):
        self.logout_callback()

    def set_back_callback(self, callback):
        self.back_callback = callback

    def set_logout_callback(self, callback):
        self.logout_callback = callback

    def fetch_report(self):
        with open('patient_id.json', 'r') as file:
            data = json.load(file)
        cred = credentials.Certificate(
            r"firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json")

        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        reports_ref = db.collection('reports')
        query = reports_ref.where('P_id', '==', int(data['patient_id'])).get()

        if len(query) != 0:
            self.table.delete(*self.table.get_children())  # Clear existing table rows

            for doc in query:
                report_data = doc.to_dict()
                self.table.insert('', 'end', values=(report_data['rep_no']))
        else:
            self.table.delete(*self.table.get_children())
            self.table.insert('', 'end', values=("No report found.", "", ""))

    def set_open_view_callback(self, callback):
        self.open_view_callback = callback

    def show_report(self):
        patient_id = self.patient_id_entry.get()
        report_no = self.rep_no_entry.get()

        data = {'patient_id': patient_id,
                'report_number': report_no}

        with open('report.json', 'w') as file:
            json.dump(data, file)

        self.open_view_callback()


class ViewFrame:
    def __init__(self, window):
        self.back_callback = {}
        self.back_callback = {}
        self.view_frame = Frame(window, width=1530, height=790)
        self.view_canvas = Canvas(
            self.view_frame,
            bg="#051747",
            height=790,
            width=1530,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.view_canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("ex_rep_image_1.png"))
        self.image_1 = self.view_canvas.create_image(
            765.0,
            395.0,
            image=self.image_image_1
        )

        self.logout_button_image = PhotoImage(
            file=relative_to_assets("ex_rep_button_1.png"))
        self.logout_button = Button(self.view_canvas,
                                    image=self.logout_button_image,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: self.logout(),
                                    relief="flat"
                                    )
        self.logout_button.place(
            x=1278.0,
            y=48.0,
            width=140.0,
            height=48.0
        )

        self.back_button_image = PhotoImage(
            file=relative_to_assets("ex_rep_button_2.png"))
        self.back_button = Button(self.view_canvas,
                                  image=self.back_button_image,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  command=lambda: self.back(),
                                  relief="flat"
                                  )
        self.back_button.place(
            x=1097.0,
            y=48.0,
            width=140.0,
            height=48.0
        )

        self.print_button_image = PhotoImage(
            file=relative_to_assets("ex_rep_button_4.png"))
        self.print_button = Button(self.view_canvas,
                                   image=self.print_button_image,
                                   borderwidth=0,
                                   highlightthickness=0,
                                   command=lambda: self.save_labels_to_pdf(),
                                   relief="flat"
                                   )
        self.print_button.place(
            x=650.0,
            y=709.0,
            width=191.0,
            height=71.0
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("ex_rep_image_2.png"))
        self.image_2 = self.view_canvas.create_image(
            737.0,
            470.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("ex_rep_image_3.png"))
        image_3 = self.view_canvas.create_image(
            732.0,
            204.0,
            image=self.image_image_3
        )

    def back(self):
        self.back_callback()

    def set_back_callback(self, callback):
        self.back_callback = callback

    def save_labels_to_pdf(self):
        cred = credentials.Certificate(
            r"firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json")

        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        reports_ref = db.collection('reports')   
        with open('report.json','r') as file:
            data = json.load(file)
        query = reports_ref.where('P_id', '==', int(data['patient_id'])).where('rep_no', '==', int(data['report_number'])).get()

        if len(query) != 0:
            for doc in query:
                r_data = doc.to_dict()
                p_id = r_data['P_id']
                p_name = r_data['Name']
                p_gender = r_data['Gender']
                p_phone = r_data['Phone']
                report = r_data['report']

                document = ap.Document()

                # Add page
                page = document.pages.add()

                # Initialize textfragment object
                text_fragment = ap.text.TextFragment(f"Name: {p_name}\nID: {p_id}\n\nGender: {p_gender}\nphone: {p_phone}\n")
                # Add text fragment to new page
                page.paragraphs.add(text_fragment)

                text_fragment = ap.text.TextFragment(report)

                page.paragraphs.add(text_fragment)

                default_filename = "patient_id_" + str(p_id)

                file_path = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF Files", "*.pdf")],
                title="Save PDF",
                initialfile=default_filename)

                # Save updated PDF
                document.save(file_path)
        else:
            table.delete(*table.get_children())
            table.insert('', 'end', values=("No report with the given ID found.", "", ""))

    def set_logout_callback(self, callback):
        self.logout_callback = callback

    def logout(self):
        self.logout_callback()

    def set_logout_callback(self, callback):
        self.logout_callback = callback

    def show(self):
        self.view_canvas.pack()
        self.view_frame.pack()
        self.view_report()
        

    def hide(self):
        self.view_canvas.pack_forget()
        self.view_frame.pack_forget()

    def view_report(self):
        cred = credentials.Certificate(
            r"firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json")

        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        db = firestore.client()
        reports_ref = db.collection('reports')
        with open('report.json', 'r') as file:
            data = json.load(file)
        query = reports_ref.where('P_id', '==', int(data['patient_id'])).where('rep_no', '==',
                                                                               int(data['report_number'])).get()
        xx = 97
        if len(query) != 0:
            for doc in query:
                r_data = doc.to_dict()
                p_id = r_data['P_id']
                p_name = r_data['Name']
                p_gender = r_data['Gender']
                p_phone = r_data['Phone']
                report = r_data['report']
            self.nm_lbl = Label(self.view_canvas, text="Name:", font=("times new roman", 12, "bold"), bg='#BABDC5')
            self.nm_lbl.place(x=xx, y=191)
            xx += 65
            self.nm_val_lbl = Label(self.view_canvas, text=p_name, font=("times new roman", 12, "bold"), bg='#BABDC5')
            self.nm_val_lbl.place(x=xx, y=191)
            xx += 90
            self.id_lbl = Label(self.view_canvas, text="ID:", font=("times new roman", 12, "bold"), bg='#BABDC5')
            self.id_lbl.place(x=xx, y=191)
            xx += 65
            self.id_val_lbl = Label(self.view_canvas, text=p_id, font=("times new roman", 12, "bold"), bg='#BABDC5')
            self.id_val_lbl.place(x=xx, y=191)
            xx += 90
            self.gen_lbl = Label(self.view_canvas, text="Gender:", font=("times new roman", 12, "bold"), bg='#BABDC5')
            self.gen_lbl.place(x=xx, y=191)
            xx += 65
            self.gen_val_lbl = Label(self.view_canvas, text=p_gender, font=("times new roman", 12, "bold"),
                                     bg='#BABDC5')
            self.gen_val_lbl.place(x=xx, y=191)
            xx += 90
            self.phn_lbl = Label(self.view_canvas, text="Phone:", font=("times new roman", 12, "bold"), bg='#BABDC5')
            self.phn_lbl.place(x=xx, y=191)
            xx += 65
            self.phn_val_lbl = Label(self.view_canvas, text=p_phone, font=("times new roman", 12, "bold"), bg='#BABDC5')
            self.phn_val_lbl.place(x=xx, y=191)
            xx += 90
            nw_x = 95
            nw_y = 265
            self.b_lbl = Label(self.view_canvas, text=report, font=("times new roman", 12, "bold"), bg='#BABDC5',
                               justify='left', anchor='w')
            self.b_lbl.place(x=nw_x, y=nw_y)
            nw_y += 100
        else:
            self.nm_lbl = Label(self.view_canvas, text="Patient not found", font=("times new roman", 12, "bold"),
                                bg='#BABDC5')
            self.nm_lbl.place(x=xx, y=184)


class ExPbsFrame:
    def create_frame(self, window):
        self.ex_pbs_frame = Frame(window, width=1530, height=790)
        self.ex_pbs_canvas = Canvas(self.ex_pbs_frame, bg="#051747", height=790, width=1530, bd=0, highlightthickness=0)

        self.ex_pbs_canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets(self.image_name))
        self.image_1 = self.ex_pbs_canvas.create_image(
            765.0,
            395.0,
            image=self.image_image_1
        )

        self.logout_button_image = PhotoImage(
            file=relative_to_assets("ex_pbs_button_1.png"))
        self.logout_button = Button(self.ex_pbs_canvas,
                                    image=self.logout_button_image,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: self.logout(),
                                    relief="flat"
                                    )
        self.logout_button.place(
            x=1278.0,
            y=48.0,
            width=140.0,
            height=48.0
        )

        self.back_button_image = PhotoImage(
            file=relative_to_assets("ex_pbs_button_2.png"))
        self.back_button = Button(self.ex_pbs_canvas,
                                  image=self.back_button_image,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  command=lambda: self.ex_opts(),
                                  relief="flat"
                                  )
        self.back_button.place(
            x=1097.0,
            y=48.0,
            width=140.0,
            height=48.0
        )

        self.gen_rep_button_image = PhotoImage(
            file=relative_to_assets("ex_pbs_button_3.png"))
        self.gen_rep_button = Button(self.ex_pbs_canvas,
                                     image=self.gen_rep_button_image,
                                     borderwidth=0,
                                     highlightthickness=0,
                                     command=lambda: self.gen_rep(),
                                     relief="flat"
                                     )
        self.gen_rep_button.place(
            x=120.0,
            y=482.0,
            width=235.0,
            height=56.0
        )

        self.browse_button_image = PhotoImage(
            file=relative_to_assets("ex_pbs_button_4.png"))
        self.browse_button = Button(self.ex_pbs_canvas,
                                    image=self.browse_button_image,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: self.browse_file(),
                                    relief="flat"
                                    )
        self.browse_button.place(
            x=905.0,
            y=715.0,
            width=174.0,
            height=55.0
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("ex_pbs_image_2.png"))
        self.image_2 = self.ex_pbs_canvas.create_image(
            972.0,
            431.0,
            image=self.image_image_2
        )

        self.pnm_var = StringVar()
        self.pnm_entry_image = PhotoImage(
            file=relative_to_assets("ex_pbs_entry_2.png"))
        self.entry_bg_2 = self.ex_pbs_canvas.create_image(
            238.0,
            321.5,
            image=self.pnm_entry_image

        )
        self.pnm_entry = Entry(self.ex_pbs_canvas,
                               bd=0,
                               bg="#D9D9D9",
                               fg="#000716",
                               highlightthickness=0,
                               textvariable=self.pnm_var
                               )
        self.pnm_entry.place(
            x=121.5,
            y=297.0,
            width=233.0,
            height=47.0
        )

        self.pid_var = IntVar()
        self.pid_var.set("")
        self.id_entry_image = PhotoImage(
            file=relative_to_assets("ex_pbs_entry_1.png"))
        self.entry_bg_1 = self.ex_pbs_canvas.create_image(
            238.0,
            419.5,
            image=self.id_entry_image
        )
        self.id_entry = Entry(self.ex_pbs_canvas,
                              bd=0,
                              bg="#D9D9D9",
                              fg="#000716",
                              highlightthickness=0,
                              textvariable=self.pid_var
                              )
        self.id_entry.place(
            x=121.5,
            y=395.0,
            width=233.0,
            height=47.0
        )

        # (x=600,y=723.0)   , (x=120, y=561)
        self.message_label_1 = self.ex_pbs_canvas.create_text(600, 723.0, anchor="w",
                                                              text="",
                                                              fill="#FFFFFF",
                                                              font=("Arial", 12, "bold"),
                                                              )

        self.message_label_2 = self.ex_pbs_canvas.create_text(
            120, 561,
            anchor="w",
            text="",
            fill="#FFFFFF",
            font=("Arial", 12, "bold"),
        )

        self.message_label_3 = self.ex_pbs_canvas.create_text(
            800.0,
            400.0,
            anchor="w",
            text="",
            fill="white",
            font=("Arial", 12, "bold"),
        )

    def __init__(self, window, json_name, image_name, model_path):
        ###callbacks##
        self.logout_callback = {}
        self.ex_opt_callback = {}
        self.image_name = image_name
        self.model_path = model_path
        self.gen_pbs_rep_callback = {}
        self.json_name = json_name
        ###########
        self.pid_var = ""
        self.pt_frame = {}
        self.ex_pbs_canvas = {}
        self.image_image_1 = {}
        self.image_1 = {}
        self.logout_button_image = {}
        self.logout_button = {}
        self.back_button_image = {}
        self.back_button = {}
        self.gen_rep_button_image = {}
        self.gen_rep_button = {}
        self.browse_button_image = {}
        self.browse_button = {}
        self.image_image_2 = {}
        self.image_2 = {}
        self.pnm_var = {}
        self.pnm_entry_image = {}
        self.entry_bg_2 = {}
        self.pnm_entry = {}
        self.pid_var = {}
        self.id_entry_image = {}
        self.entry_bg_1 = {}
        self.id_entry = {}
        self.message_label_1 = {}
        self.message_label_2 = {}
        self.message_label_3 = {}
        self.create_frame(window)

    def set_go_to_ex_opt_callback(self, callback):
        self.ex_opt_callback = callback

    def set_go_to_login_callback(self, callback):
        self.logout_callback = callback

    def set_go_to_gen_pbs_rep_callback(self, callback):
        self.gen_pbs_rep_callback = callback

    def show_delay(self):
        self.ex_pbs_canvas.itemconfig(self.message_label_3, text="Please wait for the examination process!")

    def browse_file(self):
        self.ex_pbs_canvas.itemconfig(self.message_label_1, text="")
        self.ex_pbs_canvas.itemconfig(self.message_label_2, text="")

        pt_nm = self.pnm_var.get()

        if pt_nm == "":
            self.ex_pbs_canvas.itemconfig(self.message_label_1, text="Enter patient data!")
        else:
            self.show_delay()
            image_path =filedialog.askopenfilename()
            img = Image.open(image_path)
            self.predict_image(image_path)

    def predict_image(self, image_path):
        model_path = self.model_path
#         model_path = "D:/best.pt"
#     model_path = "D:/best_skin.pt"
        if not os.path.exists(model_path):
            print(f"Model file '{model_path}' not found.")
            return
        model = torch.hub.load("ultralytics/yolov5", "custom", path=model_path, force_reload=True)
    
        image = Image.open(image_path)
        image = image.resize((452, 452))
        predictions = model(image)

        pred = predictions.pandas().xyxy[0]
        if len(pred) > 0:
            class_counts = pred["name"].value_counts()
            most_repeated_class = class_counts.idxmax()

            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype("arial.ttf", size=12)

            pred_set=set() 
            for index, row in pred.iterrows():
                x1, y1, x2, y2, conf, class_id = row[:6]
                predicted_class = model.names[int(class_id)]
                pred_set.add(predicted_class)

                confidence = "{:.2f}".format(float(conf))

                original_image_size = image.size
                x1 = int(x1 * original_image_size[0] / 452)
                y1 = int(y1 * original_image_size[1] / 452)
                x2 = int(x2 * original_image_size[0] / 452)
                y2 = int(y2 * original_image_size[1] / 452)

                draw.rectangle([(x1, y1), (x2, y2)], outline="red", width=1)
                draw.text((x1, y1 - 10), f"{predicted_class} ({confidence})", fill="red", font=font)


            pred_list = list(pred_set)    

            data = {
              'p_id':self.pid_var.get() ,
              'p_nm': self.pnm_var.get(),
              'pred_set': pred_list
                   }

                # Write the dictionary to the file in JSON format
            with open(self.json_name, 'w') as file:
                json.dump(data, file)

            rendered_image = ImageTk.PhotoImage(image)
            output_lbl = Label(self.ex_pbs_canvas,width=452, height=452, bg='#F1F2F4')
            output_lbl.place(x=700, y=190)
            label = Label(output_lbl, width=452, height=452)
            label.image = rendered_image
            label.configure(image=rendered_image)
            label.pack()
            self.ex_pbs_canvas.itemconfig(message_label_3, text="") 

    def logout(self):
        self.logout_callback()

    def ex_opts(self):
        self.ex_opt_callback()

    def gen_rep(self):
        self.ex_pbs_canvas.itemconfig(self.message_label_1, text="")
        self.ex_pbs_canvas.itemconfig(self.message_label_2, text="")
        cred = credentials.Certificate(
            r"firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json")

        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        db = firestore.client()
        doc_ref = db.collection('patients').where('id', '==', self.pid_var.get()).where('name', '==',
                                                                                        self.pnm_var.get()).limit(
            1).stream()
        documents = [doc for doc in doc_ref]
        if documents:
            self.gen_pbs_rep_callback()
        else:
            self.no_p_lbl = Label(self.ex_pbs_canvas, text="No such patient", fg="white", font=("Arial", 12, "bold"),
                                  bg='#3E4B66', height=2,
                                  width=20)
            self.no_p_lbl.place(x=120, y=561)
            print("no patient")

        firebase_admin.delete_app(firebase_admin.get_app())

    def show(self):
        self.ex_pbs_canvas.pack()
        self.ex_pbs_frame.pack()
        

    def hide(self):
        self.ex_pbs_canvas.pack_forget()
        self.ex_pbs_frame.pack_forget()


class ExSkinFrame:
    def create_frame(self, window):
        self.gen_pbs_rep_frame = Frame(window, width=1530, height=790)
        self.gen_pbs_rep_canvas = Canvas(
            self.gen_pbs_rep_frame,
            bg="#051747",
            height=790,
            width=1530,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.gen_pbs_rep_canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("ex_rep_image_1.png"))
        self.image_1 = self.gen_pbs_rep_canvas.create_image(
            765.0,
            395.0,
            image=self.image_image_1
        )

        self.logout_button_image = PhotoImage(
            file=relative_to_assets("ex_rep_button_1.png"))
        self.logout_button = Button(self.gen_pbs_rep_canvas,
                                    image=self.logout_button_image,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: self.login(),
                                    relief="flat"
                                    )
        self.logout_button.place(
            x=1278.0,
            y=48.0,
            width=140.0,
            height=48.0
        )

        self.back_button_image = PhotoImage(
            file=relative_to_assets("ex_rep_button_2.png"))
        self.back_button = Button(self.gen_pbs_rep_canvas,
                                  image=self.back_button_image,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  command=lambda: self.ex_pbs(),
                                  relief="flat"
                                  )
        self.back_button.place(
            x=1097.0,
            y=48.0,
            width=140.0,
            height=48.0
        )

        self.sv_button_image = PhotoImage(
            file=relative_to_assets("ex_rep_button_3.png"))
        self.sv_button = Button(self.gen_pbs_rep_canvas,
                                image=self.sv_button_image,
                                borderwidth=0,
                                highlightthickness=0,
                                command=self.save_labels_to_online,
                                relief="flat"
                                )
        self.sv_button.place(
            x=567.0,
            y=709.0,
            width=182.0,
            height=71.0
        )

        self.print_button_image = PhotoImage(
            file=relative_to_assets("ex_rep_button_4.png"))
        self.print_button = Button(self.gen_pbs_rep_canvas,
                                   image=self.print_button_image,
                                   borderwidth=0,
                                   highlightthickness=0,
                                   command=self.save_labels_to_pdf,
                                   relief="flat"
                                   )
        self.print_button.place(
            x=777.0,
            y=709.0,
            width=191.0,
            height=71.0
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("ex_rep_image_2.png"))
        self.image_2 = self.gen_pbs_rep_canvas.create_image(
            737.0,
            470.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("ex_rep_image_3.png"))
        self.image_3 = self.gen_pbs_rep_canvas.create_image(
            732.0,
            204.0,
            image=self.image_image_3
        )

    def __init__(self, window, json_name):
        ###callbacks##
        self.json_name = json_name
        self.logout_callback = {}
        self.ex_pbs_callback = {}
        ###########
        self.pred_set={}
        self.pt_id = {}
        self.pt_nm = {}
        self.gen_pbs_rep_frame = {}
        self.gen_pbs_rep_canvas = {}
        self.image_image_1 = {}
        self.image_1 = {}
        self.logout_button_image = {}
        self.logout_button = {}
        self.back_button_image = {}
        self.back_button = {}
        self.sv_button_image = {}
        self.sv_button = {}
        self.print_button_image = {}
        self.print_button = {}
        self.image_image_2 = {}
        self.image_2 = {}
        self.image_image_3 = {}
        self.image_3 = {}
        self.create_frame(window)

    def do_things(self):
        
        with open(self.json_name, 'r') as file:
            data = json.load(file)
        self.pt_id = data['p_id']
        self.pt_nm = data['p_nm']
        self.prd_set = data['pred_set']
        cred = credentials.Certificate(
            r"firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json")

        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        db = firestore.client()
        p_ref = db.collection('patients')
        p_docs = p_ref.where('id', '==', self.pt_id).limit(1).get()
        found = 0
        if len(p_docs) > 0:
            print("hey")
            p_doc = p_docs[0]
            print('found')
            found = 1
            p_data = p_doc.to_dict()
            print(p_data)
            p_name = p_data['name']
            p_id = p_data['id']
            p_phone = p_data['phone']
            p_gender = p_data['gender']
        else:
            print("patient not found")
        xx = 97
        if found == 1:
            self.nm_lbl = Label(self.gen_pbs_rep_canvas, text="Name:", font=("times new roman", 12, "bold"),
                                bg='#BABDC5')
            self.nm_lbl.place(x=xx, y=191)
            xx += 65
            self.nm_val_lbl = Label(self.gen_pbs_rep_canvas, text=p_name, font=("times new roman", 12, "bold"),
                                    bg='#BABDC5')
            self.nm_val_lbl.place(x=xx, y=191)
            xx += 90

            self.id_lbl = Label(self.gen_pbs_rep_canvas, text="ID:", font=("times new roman", 12, "bold"), bg='#BABDC5')
            self.id_lbl.place(x=xx, y=191)
            xx += 65
            self.id_val_lbl = Label(self.gen_pbs_rep_canvas, text=p_id, font=("times new roman", 12, "bold"),
                                    bg='#BABDC5')
            self.id_val_lbl.place(x=xx, y=191)
            xx += 90

            self.gen_lbl = Label(self.gen_pbs_rep_canvas, text="Gender:", font=("times new roman", 12, "bold"),
                                 bg='#BABDC5')
            self.gen_lbl.place(x=xx, y=191)
            xx += 65

            self.gen_val_lbl = Label(self.gen_pbs_rep_canvas, text=p_gender, font=("times new roman", 12, "bold"),
                                     bg='#BABDC5')
            self.gen_val_lbl.place(x=xx, y=191)
            xx += 90

            self.phn_lbl = Label(self.gen_pbs_rep_canvas, text="Phone:", font=("times new roman", 12, "bold"),
                                 bg='#BABDC5')
            self.phn_lbl.place(x=xx, y=191)
            xx += 65

            self.phn_val_lbl = Label(self.gen_pbs_rep_canvas, text=p_phone, font=("times new roman", 12, "bold"),
                                     bg='#BABDC5')
            self.phn_val_lbl.place(x=xx, y=191)
            xx += 90

        else:
            self.nm_lbl = Label(self.gen_pbs_rep_canvas, text="Patient not found", font=("times new roman", 12, "bold"),
                                bg='#BABDC5')
            self.nm_lbl.place(x=xx, y=184)

        Heading_txt = " Microscopic Examination and Diagnosis"
        Early_txt = "Early-ALL cells  :  Found\nThe examination shows irregular cell shapes and an abnormal nuclear-to-cytoplasmic ratio. In addition, there is an increased number of immature and abnormal cells and decreased numbers\nof normal blood cells. Also,cells tend to form clusters or aggregates in the peripheral blood, indicating their tendency to associate with each other and potentially leading to the obstruction of\nblood vessels.\n"
        pre_txt = "Pre-ALL cells  :  Found\nSome nuclei appear to be round and others are slightly irregular.The chromatin pattern is coarse. In addition, there is an abnormal proliferation of immature B-cell progenitors,as well as a significant\nnumber of blast cells (lymphoblasts), leading to a reduction in the number of normal blood cells.This reduction can cause anemia, thrombocytopenia, and decreased mature white blood cells.\n"
        pro_txt = "Pro-ALL cells  :  Found\nHere, immature cellular features are observed, including large nuclei, fine chromatin pattern, prominent nucleoli, and scant cytoplasm.The nuclear shape is rounded and irregular, with a fine\ngranular chromatin pattern and dispersed chromatin clumps.There is a lack of cytoplasmic granules, as well as an increased number of blasts and a high nucleocytoplasmic ratio, indicating\nthe presence of immature cells and the presence of ribosomes and other protein synthesis machinery in the cytoplasm.\n"
        benign_txt = "Benign-Cancer cells:  Found\nThe cellular composition appears normal with small, round lymphocytes, including more fragile cells known as 'smudge cells.'There is also an increased number of platelets; however, the platelets\nthemselves may appear normal in morphology. Additionally, there is an increased number of red blood cells.\n"
        rec_txt = "Recommendations:\nIt is recommended to start following up with a hematologist in order to manage the treatment plan and coordinate care. In addition, it is important to start chemotherapy as soon as possible\nto avoid any progression in the proposed case. Also, supportive care measures must be implemented to manage and minimize treatment-related side effects.Emotional support and counseling\n should be provided to facilitate the treatment process.\n\nRemember,\n\"You never know how strong you are until being strong is your only choice.\""
        nw_x = 95
        nw_y = 265
        self.hd1_lbl = Label(self.gen_pbs_rep_canvas, text=Heading_txt, font=("times new roman", 12, "bold"),
                             bg='#BABDC5', justify='left',
                             anchor='w')
        self.hd1_lbl.place(x=nw_x, y=nw_y)
        nw_y += 40
        if 'Early' in self.prd_set:
            self.e_lbl = Label(self.gen_pbs_rep_canvas, text=Early_txt, font=("times new roman", 12, "bold"),
                               bg='#BABDC5', justify='left',
                               anchor='w')
            self.e_lbl.place(x=nw_x, y=nw_y)
            nw_y += 100
        if 'Pre' in self.prd_set:
            self.pre_lbl = Label(self.gen_pbs_rep_canvas, text=pre_txt, font=("times new roman", 12, "bold"),
                                 bg='#BABDC5', justify='left',
                                 anchor='w')
            self.pre_lbl.place(x=nw_x, y=nw_y)
            nw_y += 100

        if 'Pro' in self.prd_set:
            self.pro_lbl = Label(self.gen_pbs_rep_canvas, text=pro_txt, font=("times new roman", 12, "bold"),
                                 bg='#BABDC5', justify='left',
                                 anchor='w')
            self.pro_lbl.place(x=nw_x, y=nw_y)
            nw_y += 100

        if 'Benign' in self.prd_set:
            self.b_lbl = Label(self.gen_pbs_rep_canvas, text=benign_txt, font=("times new roman", 12, "bold"),
                               bg='#BABDC5', justify='left',
                               anchor='w')
            self.b_lbl.place(x=nw_x, y=nw_y)
            nw_y += 100

        self.rec_lbl = Label(self.gen_pbs_rep_canvas, text=rec_txt, font=("times new roman", 12, "bold"), bg='#BABDC5',
                             justify='left', anchor='w')
        self.rec_lbl.place(x=nw_x, y=nw_y)

    def set_go_to_ex_pbs_callback(self, callback):
        self.ex_pbs_callback = callback

    def ex_pbs(self):
        self.ex_pbs_callback()

    def set_go_to_login_callback(self, callback):
        self.logout_callback = callback

    def login(self):
        self.logout_callback()

    def save_labels_to_pdf(self):
        content = []
        content.append("Name: " + self.nm_val_lbl["text"] + "\n")
        content.append("ID: " + str(self.id_val_lbl["text"]) + "\n")
        content.append("Gender: " + self.gen_val_lbl["text"] + "\n")
        content.append("Phone: " + self.phn_val_lbl["text"] + "\n")
        content.append("\nExamination Results:\n")
        content.append(self.hd1_lbl["text"] + "\n")
        if 'Early' in self.prd_set:
            content.append(self.e_lbl["text"] + "\n")
        if 'Pre' in self.prd_set:
            content.append(self.pre_lbl["text"] + "\n")
        if 'Pro' in self.prd_set:
            content.append(self.pro_lbl["text"] + "\n")
        if 'Benign' in self.prd_set:
            content.append(self.b_lbl["text"] + "\n")
        content.append(self.rec_lbl["text"] + "\n")

        # Apply line wrapping to the content
        wrapped_content = []
        for line in content:
            wrapped_lines = textwrap.wrap(line, width=90)
            wrapped_content.extend(wrapped_lines)
            
          
        default_filename = "patient_id_" + str(self.id_val_lbl["text"])
        # Open file dialog to choose save location
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            title="Save PDF",
            initialfile=default_filename 
        )
        
        # Save content to a PDF file
        if file_path:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for line in wrapped_content:
                pdf.cell(0, 10, txt=line, ln=True)
            pdf.output(file_path)

            print("Labels saved to PDF:", file_path)


    def save_labels_to_online(self):
        Name = []
        Name.append(self.nm_val_lbl["text"] + "\n")

        P_id = []
        P_id.append(int(self.id_val_lbl["text"]))  # Convert P_id to an integer

        Gender = []
        Gender.append(self.gen_val_lbl["text"] + "\n")

        Phone = []
        Phone.append(int(self.phn_val_lbl["text"]))

        report = []

        report.append(self.hd1_lbl["text"] + "\n")
        if 'Early' in self.prd_set:
            report.append(self.e_lbl["text"] + "\n")
        if 'Pre' in self.prd_set:
            report.append(self.pre_lbl["text"] + "\n")
        if 'Pro' in self.prd_set:
            report.append(self.pro_lbl["text"] + "\n")
        if 'Benign' in self.prd_set:
            report.append(self.b_lbl["text"] + "\n")
        report.append(self.rec_lbl["text"] + "\n")

        wrapped_Name = []
        for line in Name:
            wrapped_lines = textwrap.wrap(line, width=90)
            wrapped_Name.extend(wrapped_lines)

        # Convert the content to a single string
        pdf_Name = '\n'.join(Name)
        pdf_P_id = P_id[0]  # Store P_id as an integer
        pdf_Gender = '\n'.join(Gender)
        pdf_Phone = Phone[0]
        pdf_report = '\n'.join(report)

        # Get a Firestore collection reference
        pdf_collection = db.collection('reports')
        p_docs = pdf_collection.where('P_id', '==', pdf_P_id).limit(1).get()
        if len(p_docs) > 0:
            # Patient exists, retrieve rep_no
            max_rep_no = 0
            for p_doc in p_docs:
                p_data = p_doc.to_dict()
                rep_no = int(p_data.get('rep_no', '0'))   
                max_rep_no = max(max_rep_no, rep_no)
            new_rep_no = max_rep_no + 1
        else:
            new_rep_no = 1

        new_doc = pdf_collection.document()
        new_doc.set({
            'Name': pdf_Name,
            'P_id': pdf_P_id,
            'Gender': pdf_Gender,
            'Phone': pdf_Phone,
            'report': pdf_report,
            'rep_no': new_rep_no
        })

        print("PDF saved to Firestore:", new_doc.id)
        self.lbl = Label(self.gen_pbs_rep_canvas, text="Report saved", fg="white", font=("Arial", 12, "bold"),
                         bg='#ADD8E6', height=2, width=20)
        self.lbl.place(x=300.0, y=709.0, )

    def show(self):
        self.gen_pbs_rep_frame.pack()
        self.gen_pbs_rep_canvas.pack()
        self.do_things()

    def hide(self):
        self.gen_pbs_rep_frame.pack_forget()
        self.gen_pbs_rep_canvas.pack_forget()


class ModifiedExSkinFrame:
    def create_frame(self, window):
        self.gen_pbs_rep_frame = Frame(window, width=1530, height=790)
        self.gen_pbs_rep_canvas = Canvas(
            self.gen_pbs_rep_frame,
            bg="#051747",
            height=790,
            width=1530,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.gen_pbs_rep_canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("ex_rep_image_1.png"))
        self.image_1 = self.gen_pbs_rep_canvas.create_image(
            765.0,
            395.0,
            image=self.image_image_1
        )

        self.logout_button_image = PhotoImage(
            file=relative_to_assets("ex_rep_button_1.png"))
        self.logout_button = Button(self.gen_pbs_rep_canvas,
                                    image=self.logout_button_image,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: self.login(),
                                    relief="flat"
                                    )
        self.logout_button.place(
            x=1278.0,
            y=48.0,
            width=140.0,
            height=48.0
        )

        self.back_button_image = PhotoImage(
            file=relative_to_assets("ex_rep_button_2.png"))
        self.back_button = Button(self.gen_pbs_rep_canvas,
                                  image=self.back_button_image,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  command=lambda: self.ex_pbs(),
                                  relief="flat"
                                  )
        self.back_button.place(
            x=1097.0,
            y=48.0,
            width=140.0,
            height=48.0
        )

        self.sv_button_image = PhotoImage(
            file=relative_to_assets("ex_rep_button_3.png"))
        self.sv_button = Button(self.gen_pbs_rep_canvas,
                                image=self.sv_button_image,
                                borderwidth=0,
                                highlightthickness=0,
                                command=self.save_labels_to_online,
                                relief="flat"
                                )
        self.sv_button.place(
            x=567.0,
            y=709.0,
            width=182.0,
            height=71.0
        )

        self.print_button_image = PhotoImage(
            file=relative_to_assets("ex_rep_button_4.png"))
        self.print_button = Button(self.gen_pbs_rep_canvas,
                                   image=self.print_button_image,
                                   borderwidth=0,
                                   highlightthickness=0,
                                   command=self.save_labels_to_pdf,
                                   relief="flat"
                                   )
        self.print_button.place(
            x=777.0,
            y=709.0,
            width=191.0,
            height=71.0
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("ex_rep_image_2.png"))
        self.image_2 = self.gen_pbs_rep_canvas.create_image(
            737.0,
            470.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("ex_rep_image_3.png"))
        self.image_3 = self.gen_pbs_rep_canvas.create_image(
            732.0,
            204.0,
            image=self.image_image_3
        )

    def __init__(self, window, json_name):
        ###callbacks##
        self.json_name = json_name
        self.logout_callback = {}
        self.ex_pbs_callback = {}
        ###########
        self.pt_id = {} 
        self.pt_nm = {} 
        self.prd_set={} 
        self.gen_pbs_rep_frame = {}
        self.gen_pbs_rep_canvas = {}
        self.image_image_1 = {}
        self.image_1 = {}
        self.logout_button_image = {}
        self.logout_button = {}
        self.back_button_image = {}
        self.back_button = {}
        self.sv_button_image = {}
        self.sv_button = {}
        self.print_button_image = {}
        self.print_button = {}
        self.image_image_2 = {}
        self.image_2 = {}
        self.image_image_3 = {}
        self.image_3 = {}
        self.create_frame(window)

    def do_things(self):
        with open(self.json_name, 'r') as file:
            data = json.load(file)
        self.pt_id = data['p_id']
        self.pt_nm = data['p_nm']
        self.prd_set = data['pred_set']
        cred = credentials.Certificate(
            r"firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json")

        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        
        p_ref = db.collection('patients')
        p_docs = p_ref.where('id', '==', self.pt_id).limit(1).get()
        found = 0
        if len(p_docs) > 0:
            print("hey")
            p_doc = p_docs[0]
            print('found')
            found = 1
            p_data = p_doc.to_dict()
            print(p_data)
            p_name = p_data['name']
            p_id = p_data['id']
            p_phone = p_data['phone']
            p_gender = p_data['gender']
        else:
            print("patient not found")
        xx = 97
        if found == 1:
            self.nm_lbl = Label(self.gen_pbs_rep_canvas, text="Name:", font=("times new roman", 12, "bold"),
                                bg='#BABDC5')
            self.nm_lbl.place(x=xx, y=191)
            xx += 65
            self.nm_val_lbl = Label(self.gen_pbs_rep_canvas, text=p_name, font=("times new roman", 12, "bold"),
                                    bg='#BABDC5')
            self.nm_val_lbl.place(x=xx, y=191)
            xx += 90

            self.id_lbl = Label(self.gen_pbs_rep_canvas, text="ID:", font=("times new roman", 12, "bold"), bg='#BABDC5')
            self.id_lbl.place(x=xx, y=191)
            xx += 65
            self.id_val_lbl = Label(self.gen_pbs_rep_canvas, text=p_id, font=("times new roman", 12, "bold"),
                                    bg='#BABDC5')
            self.id_val_lbl.place(x=xx, y=191)
            xx += 90

            self.gen_lbl = Label(self.gen_pbs_rep_canvas, text="Gender:", font=("times new roman", 12, "bold"),
                                 bg='#BABDC5')
            self.gen_lbl.place(x=xx, y=191)
            xx += 65

            self.gen_val_lbl = Label(self.gen_pbs_rep_canvas, text=p_gender, font=("times new roman", 12, "bold"),
                                     bg='#BABDC5')
            self.gen_val_lbl.place(x=xx, y=191)
            xx += 90

            self.phn_lbl = Label(self.gen_pbs_rep_canvas, text="Phone:", font=("times new roman", 12, "bold"),
                                 bg='#BABDC5')
            self.phn_lbl.place(x=xx, y=191)
            xx += 65

            self.phn_val_lbl = Label(self.gen_pbs_rep_canvas, text=p_phone, font=("times new roman", 12, "bold"),
                                     bg='#BABDC5')
            self.phn_val_lbl.place(x=xx, y=191)
            xx += 90

        else:
            self.nm_lbl = Label(self.gen_pbs_rep_canvas, text="Patient not found", font=("times new roman", 12, "bold"),
                                bg='#BABDC5')
            self.nm_lbl.place(x=xx, y=184)

        Heading_txt = " Microscopic Examination and Diagnosis"
        malig_txt = "The purpose of this lab report is to present the findings of the examined microscopic skin cell biopsy, which indicate the presence of malignant cells. The biopsy was performed as part of the\ninvestigation into suspected skin malignancy. Malignant cells possess abnormal characteristics compared to normal cells, including cellular atypia, altered nuclear-to-cytoplasmic ratio,\nenlarged nuclei, irregular nuclear membranes, prominent nucleoli, increased nuclear staining, increased rates of mitotic activity, invasion into surrounding connective tissue and blood vessels,\nlack of resemblance to normal skin tissue, and growth of fibrous or connective tissue in response to the tumor.\n"
        begnin_txt = "The examination reveals a normal cellular architecture, with consistent size, shape, and nuclear-to-cytoplasmic ratio. The nuclei display uniformity, with regular contours and mild staining\nintensity. Furthermore, normal nuclear features are observed, such as uniform size and shape, regular nuclear membranes, inconspicuous nucleoli,and moderate nuclear staining.\nThe cells maintain their differentiation and closely resemble the normal cells from their origin. All these characteristics indicate that the lesion is benign.\n"
        rec_txt = "Recommendations:\nThe diagnosed patient must consult with a dermatologist to receive personalized advice. Additionally, he should prioritize sun protection to prevent further skin damage and reduce the risk of\ndeveloping new skin cancers. This entails avoiding excessive sun exposure, particularly during peak hours (10 am to 4 pm), wearing protective clothing, using a broad-spectrum sunscreen with\n a high SPF, and seeking shade when outdoors.Performing regular self-examinations of the skin and closely monitoring any new or changing moles, growths, or lesions is crucial.The diagnosed\npatient should adopt a healthy lifestyle, as it can support overall well-being and potentially have a positive impact on cancer management. Seeking emotional support from loved ones, support\ngroups, or mental health professionals is also vital, as they can offer guidance and coping strategies. \n\nRemember,\n\"You never know how strong you are until being strong is your only choice.\""
        nw_x = 95
        nw_y = 265
        self.hd1_lbl = Label(self.gen_pbs_rep_canvas, text=Heading_txt, font=("times new roman", 12, "bold"),
                             bg='#BABDC5', justify='left',
                             anchor='w')
        self.hd1_lbl.place(x=nw_x, y=nw_y)
        nw_y += 40
        if 'Malignant' in self.prd_set:
            self.m_lbl = Label(self.gen_pbs_rep_canvas, text=malig_txt, font=("times new roman", 12, "bold"),
                               bg='#BABDC5', justify='left',
                               anchor='w')
            self.m_lbl.place(x=nw_x, y=nw_y)
            nw_y += 100
        if 'Benign' in self.prd_set:
            self.b_lbl = Label(self.gen_pbs_rep_canvas, text=begnin_txt, font=("times new roman", 12, "bold"),
                               bg='#BABDC5', justify='left',
                               anchor='w')
            self.b_lbl.place(x=nw_x, y=nw_y)
            nw_y += 100

        self.rec_lbl = Label(self.gen_pbs_rep_canvas, text=rec_txt, font=("times new roman", 12, "bold"), bg='#BABDC5',
                             justify='left', anchor='w')
        self.rec_lbl.place(x=nw_x, y=nw_y)

    def set_go_to_ex_pbs_callback(self, callback):
        self.ex_pbs_callback = callback

    def ex_pbs(self):
        self.ex_pbs_callback()

    def set_go_to_login_callback(self, callback):
        self.logout_callback = callback

    def login(self):
        self.logout_callback()

    def save_labels_to_pdf(self):
        content = []
        content.append("Name: " + self.nm_val_lbl["text"] + "\n")
        content.append("ID: " + str(self.id_val_lbl["text"]) + "\n")
        content.append("Gender: " + self.gen_val_lbl["text"] + "\n")
        content.append("Phone: " + self.phn_val_lbl["text"] + "\n")
        content.append("\nExamination Results:\n")
        content.append(self.hd1_lbl["text"] + "\n")
        if 'Malignant' in self.prd_set:
            content.append(self.m_lbl["text"] + "\n")
        if 'Benign' in self.prd_set:
            content.append(self.b_lbl["text"] + "\n")
        content.append(self.rec_lbl["text"] + "\n")

        # Apply line wrapping to the content
        wrapped_content = []
        for line in content:
            wrapped_lines = textwrap.wrap(line, width=90)
            wrapped_content.extend(wrapped_lines)

        # Set the default filename
        default_filename = "patient_id_" + str(self.id_val_lbl["text"])

        # Open file dialog to choose save location
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            title="Save PDF",
            initialfile=default_filename  # Set the default filename
        )

        # Save content to a PDF file
        if file_path:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for line in wrapped_content:
                pdf.cell(0, 10, txt=line, ln=True)
            pdf.output(file_path)

            print("Labels saved to PDF:", file_path)


    def save_labels_to_online(self):
        Name = []
        Name.append(self.nm_val_lbl["text"] + "\n")

        P_id = []
        P_id.append(int(self.id_val_lbl["text"]))  # Convert P_id to an integer

        Gender = []
        Gender.append(self.gen_val_lbl["text"] + "\n")

        Phone = []
        Phone.append(int(self.phn_val_lbl["text"]))

        report = []

        report.append(self.hd1_lbl["text"] + "\n")
        if 'Malignant' in self.prd_set:
            report.append(self.m_lbl["text"] + "\n")
        if 'Benign' in self.prd_set:
            report.append(self.b_lbl["text"] + "\n")
        report.append(self.rec_lbl["text"] + "\n")

        wrapped_Name = []
        for line in Name:
            wrapped_lines = textwrap.wrap(line, width=90)
            wrapped_Name.extend(wrapped_lines)

        # Convert the content to a single string
        pdf_Name = '\n'.join(Name)
        pdf_P_id = P_id[0]  # Store P_id as an integer
        pdf_Gender = '\n'.join(Gender)
        pdf_Phone = Phone[0]
        pdf_report = '\n'.join(report)

        # Get a Firestore collection reference
        pdf_collection = db.collection('reports')

        # Check if patient_id exists
        p_docs = pdf_collection.where('P_id', '==', pdf_P_id).limit(1).get()
        if len(p_docs) > 0:
            # Patient exists, retrieve rep_no
            max_rep_no = 0
            for p_doc in p_docs:
                p_data = p_doc.to_dict()
                rep_no = int(p_data.get('rep_no', '0'))  # Convert to integer and default to 0 if not found
                max_rep_no = max(max_rep_no, rep_no)
            new_rep_no = max_rep_no + 1
        else:
            # Patient doesn't exist, set rep_no to 1
            new_rep_no = 1

            # Create a new document and set the PDF content
        new_doc = pdf_collection.document()
        new_doc.set({
            'Name': pdf_Name,
            'P_id': pdf_P_id,
            'Gender': pdf_Gender,
            'Phone': pdf_Phone,
            'report': pdf_report,
            'rep_no': new_rep_no
            # Add more content fields as needed
        })

        print("PDF saved to Firestore:", new_doc.id)

        self.lbl = Label(self.gen_pbs_rep_canvas, text="Report saved", fg="white", font=("Arial", 12, "bold"),
                         bg='#ADD8E6', height=2, width=20)
        self.lbl.place(x=300.0, y=709.0, )

    def show(self):
        self.gen_pbs_rep_frame.pack()
        self.gen_pbs_rep_canvas.pack()
        self.do_things()
        

    def hide(self):
        self.gen_pbs_rep_frame.pack_forget()
        self.gen_pbs_rep_canvas.pack_forget()


if __name__ == '__main__':
    window = Tk()
    window.geometry("1530x790")
    window.configure(bg="#051747")
    window.title("Cancer Detection Assistant")

    login_frame = LoginFrame(window , "login_data.json")
    home_frame = HomeFrame(window)
    admin_frame = AdminFrame(window)
    settings_frame = SettingsFrame(window , "login_data.json")
    examine_frame = ExamineOptionsFrame(window)
    patient_frame = PatientFrame(window)
    reports_frame = ReportFrame(window)
    view_frame = ViewFrame(window)
    
    modified_ex_skin_frame = ModifiedExSkinFrame(window, "shared_data_skin.json")
    ex_skin_frame = ExSkinFrame(window, "shared_data.json")
    
    #examin_pbs_frame
    ex_pts_frame = ExPbsFrame(window, "shared_data.json", "ex_pbs_image_1.png", r"D:\best.pt")
    #examin_skin_frame
    modified_ex_pts_frame = ExPbsFrame(window, "shared_data_skin.json", "ex_skin_image_1.png", r"D:\best_skin.pt")
    
    


    def what_should_happen_when_we_click_on_login_bt_in_login_frame(role):
        login_frame.hide()
        if role == 0:
            admin_frame.show()
        else:
            home_frame.show()


    def what_should_happen_when_we_click_on_login_bt_in_home_frame():
        home_frame.hide()
        login_frame.show()


    def da_aly_almafrood_t3mlo_lama_ytdaas_3ala_logout():
        admin_frame.hide()
        login_frame.show()


    def go_to_homr_from_setting():
        settings_frame.hide()
        home_frame.show()


    def go_to_settings_from_home():
        home_frame.hide()
        settings_frame.show()


    def go_to_pt_from_home():
        home_frame.hide()
        patient_frame.show()


    def go_to_home_from_examine_frame():
        examine_frame.hide()
        home_frame.show()


    def logout_from_examine_frame():
        examine_frame.hide()
        login_frame.show()


    def go_to_examine_op_frame_from_home():
        home_frame.hide()
        examine_frame.show()


    def go_to_home_from_patient():
        patient_frame.hide()
        home_frame.show()


    def logout_from_patient_frame():
        patient_frame.hide()
        login_frame.show()


    def show_reports_from_patient_frame():
        patient_frame.hide()
        reports_frame.show()


    def logout_from_report_frame():
        reports_frame.hide()
        login_frame.show()


    def logout_from_view_frame():
        view_frame.hide()
        login_frame.show()


    def back_from_report_frame():
        reports_frame.hide()
        patient_frame.show()


    def open_view_from_reports_frame():
        reports_frame.hide()
        view_frame.show()


    def back_from_view_frame():
        view_frame.hide()
        reports_frame.show()


    def logout_from_ex_pts_frame():
        ex_pts_frame.hide()
        login_frame.show()


    def examine_from_ex_pts_frame():
        ex_pts_frame.hide()
        examine_frame.show()


    def go_to_ex_pts_frame():
        examine_frame.hide()
        ex_pts_frame.show()


    def logout_from_skin_frame():
        ex_skin_frame.hide()
        login_frame.show()


    def go_to_login_skin_frame():
        ex_skin_frame.hide()
        ex_pts_frame.show()


    def go_to_new_from_old():
        ex_pts_frame.hide()
        ex_skin_frame.show()


    def go_to_modified():
        examine_frame.hide()
        modified_ex_pts_frame.show()


    def logout_from_mdified_ex_pts_frame():
        modified_ex_pts_frame.hide()
        login_frame.show()


    def examine_from_mdified_ex_pts_frame():
        modified_ex_pts_frame.hide()
        examine_frame.show()


    def go_to_new_from_modified_old():
        modified_ex_pts_frame.hide()
        modified_ex_skin_frame.show()


    def logout_from_modified_skin_frame():
        modified_ex_skin_frame.hide()
        login_frame.show()


    def go_to_login_modified_skin_frame():
        modified_ex_skin_frame.hide()
        ex_pts_frame.show()


    login_frame.set_login_callback(what_should_happen_when_we_click_on_login_bt_in_login_frame)
    home_frame.set_login_callback(what_should_happen_when_we_click_on_login_bt_in_home_frame)
    admin_frame.edeeny_al7aga_aly_almafrood_a3mlha(da_aly_almafrood_t3mlo_lama_ytdaas_3ala_logout)
    settings_frame.set_go_to_home_callback(go_to_homr_from_setting)
    home_frame.set_settings_callback(go_to_settings_from_home)
    examine_frame.set_home_callback(go_to_home_from_examine_frame)
    examine_frame.set_logout_callback(logout_from_examine_frame)
    home_frame.set_ex_opts_callback(go_to_examine_op_frame_from_home)
    patient_frame.set_go_to_home_callback(go_to_home_from_patient)
    patient_frame.set_go_to_login_callback(logout_from_patient_frame)
    home_frame.set_pt_callback(go_to_pt_from_home)
    patient_frame.set_show_reports_call_back(show_reports_from_patient_frame)
    reports_frame.set_logout_callback(logout_from_report_frame)
    reports_frame.set_back_callback(back_from_report_frame)
    view_frame.set_logout_callback(logout_from_view_frame)
    reports_frame.set_open_view_callback(open_view_from_reports_frame)
    view_frame.set_back_callback(back_from_view_frame)
    examine_frame.set_exm_pbs_callback(go_to_ex_pts_frame)
    examine_frame.set_exm_skin_callback_callback(go_to_modified)

    ex_pts_frame.set_go_to_login_callback(logout_from_ex_pts_frame)
    ex_pts_frame.set_go_to_ex_opt_callback(examine_from_ex_pts_frame)
    ex_pts_frame.set_go_to_gen_pbs_rep_callback(go_to_new_from_old)
    ex_skin_frame.set_go_to_login_callback(logout_from_skin_frame)
    ex_skin_frame.set_go_to_ex_pbs_callback(go_to_login_skin_frame)

    modified_ex_pts_frame.set_go_to_login_callback(logout_from_mdified_ex_pts_frame)
    modified_ex_pts_frame.set_go_to_ex_opt_callback(examine_from_mdified_ex_pts_frame)
    modified_ex_pts_frame.set_go_to_gen_pbs_rep_callback(go_to_new_from_modified_old)
    modified_ex_skin_frame.set_go_to_login_callback(logout_from_modified_skin_frame)
    modified_ex_skin_frame.set_go_to_ex_pbs_callback(go_to_login_modified_skin_frame)

    login_frame.show()

    window.mainloop()
