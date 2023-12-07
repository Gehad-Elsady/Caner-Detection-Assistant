# Caner-Detection-Assistant 
It is a computer system that enables lab technician to upload a microscopic blood 
smear of a patient to detect if they have ALL and categorize the subtype (pre, pro, 
early, benign) or if the cell is normal using YOLOv5. Alongside this, The model 
is used to detect melanoma skin cancer using images of the patient skin.
The system has two users:

● The lab technician: Uploads the patient’s blood smear or skin image so 
the model can do its prediction. Furthermore, they can add patients, and 
delete patients. Lab technicians can save reports and print reports.

● The admin: Can update, delete, and add lab technicians


## The main supported functions to be coded in this system are: : 

● Sign up

● Login

● Add new patient

● Add new lab technician

● Show report by patient ID

● Edit patient

● Delete patient

● Delete doctor

● Show patient details

● Upload image

● Log out

● Print report

● Save report

-  Constraints:

● Doctor username must be unique

● Password and confirm password fields must be identical

● Password must be mix of letters and number and 6 characters long

● Gender is in dropdown list to ensure consistency

● Mobile number must begin with 011, 012, 010, or 015

● Mobile number must be 11 numbers

● Ensure that the username and password are correct before logging in
  
 


## Objectives: 

 ● The system detects ALL subtypes accurately and fast using an object 
detection model called YOLOv5 which is the main goal of the project.

● A generated report of the patient’s case will be generated and it can be 
printed so the patient can take it to their physicians.

● The patient can have more than one image on the database.

● Each lab technician has their patients and can’t access the patients of other 
technicians.

● The system shows the predicted class of the ALL and shows the bounding 
boxes with the confidence level of the prediction.

## Data Description  

   This study evaluates object detection model to be specific on ALL image dataset. 
The bone marrow laboratory at Taleqani Hospital provided the images for this 
dataset (Tehran, Iran). This dataset included 3256 PBS pictures from 89 
individuals who were thought to be ALL and whose blood samples were properly 
processed and stained by professional laboratory personnel. This dataset is 
separated into the benign and malignant classes. Hematogenes make up the first 
group, whereas the ALL group, which includes the three malignant lymphoblast 
subtypes Early Pre-B, Pre-B, and Pro-B ALL, makes up the latter. All of the 
photos were taken with a Zeiss camera at a 100x magnification in a microscope, 
and they were all saved as JPG files. The specific types and subtypes of these 
cells were identified by a professional using the flow cytometry instrument. 
Segmented photos following colour thresholding-based segmentation in the HSV 
colour space are offered. However, segmentation made a lot of details to be lost 
leading to inaccuracies, therefore, the original images were used .
((((((((add images)) pg 25 

  - Melanoma Skin Cancer Dataset
    
1) Dataset from Kaggle
10000 pictures are included in the Melanoma Skin Cancer Dataset.. 9600 images 
make up the dataset, whereas 1000 images are used to evaluate the model. It is 
subdivided into two classes: malignant and bening. The dataset is found in Kaggle 
with no bounding boxes. Figure 2 displays samples of data from Kaggle.
(((images )))

  -  Dataset from Roboflow
The same exact dataset is found in Roboflow but only 4300 pictures are found 
with the bounding boxes automatically assigned to the objects. Figure 3 illustrates 
samples of the same Melanoma Skin Cancer dataset but with bounding boxes 
from Roboflow ( images)

## Functional/ Non-functional Requirement
 - Functional requirements
1. Login
Actor: User (Doctor)
Precondition: Open application and have active internet connection.
38
Description: The Doctor will start entering his information such as username and 
password.
Postcondition: Access his personal account & other services.


2. Add Patient
Actor: User (Doctor)
Precondition: The Doctor must be logged in.
Description: The doctor should enter the patient name, gender, phone number, 
date of birth of the patient to be created.
Postcondition: New patient information will be displayed in the table and saved 
in the firebase.


3. Update Patient
Actor: User (Doctor)
Precondition: The Doctor must be logged in and know the name or id of the user 
that he wants to update.
Description: The doctor should enter patient id and the updated patient fields of 
the patient to be updated.
39
Postcondition: Patient information will be updated in the firebase and displayed 
in the table on screen.


5. Delete Patient
Actor: User (Doctor)
Precondition: The Doctor must be logged in and know the name or id of the user 
that he wants to delete.
Description: The doctor should enter the id of the patient to be deleted.
Postcondition: Patient information will be deleted in the firebase and removed 
from the table on screen.


6. Search Patient
Actor: User (Doctor)
Precondition: The Doctor must be logged in and patient data exists.
Description: The doctor should enter the id of the patient and search patient data.
Postcondition: Patient information will be displayed in a table.


7. Browse Image
Actor: User (Doctor)
Precondition: The Doctor must be logged in.
Description: The doctor should enter the patient id and patient name and browse 
blood smear image from pc.
Postcondition: The system detects the cancer type and location of cancer cells in 
a blood smear image.


8. Generate Report
Actor: User (Doctor)
Precondition: The Doctor must be logged in and a blood smear image is uploaded.
Description: When the doctor presses the “Generate Report” button, the system 
redirects him to the Examination Report window to view the generated report.
Postcondition: Detailed report of the patient’s blood smear will be displayed in 
the Examination Report window.


9. Save Report
Actor: User (Doctor)
Precondition: The Doctor must be logged in and a report is generated.
Description: When the doctor presses the “Save Report” button, the report is 
saved in the firebase.
Postcondition: The generated report and patient information are saved in the 
firebase.


10. View report numbers
Actor: User (Doctor)
Precondition: The Doctor must be logged in and patient exits.
Description: The doctor is redirected to show a report window and all the reports 
numbers of the patient will be displayed in the table.
Postcondition: The report numbers of reports of the patient will be displayed in 
the table.


11. View report
Actor: User (Doctor)
Precondition: The Doctor must be logged in and patient exits.
Description: The doctor is redirected to the Examination Report window and the 
patient report is displayed on screen.
Postcondition: The patient report will be displayed on screen.


12.Save report as pdf
Actor: User (Doctor)
Precondition: The Doctor must be logged in and the patient and report number 
exists.
Description: The doctor will choose the folder to which the report file will be 
saved as pdf on pc and the report file will be saved. 
Postcondition: Report is saved as pdf and doctor views report file of patient as 
pdf file.


13.Logout
Actor: User (Doctor)
Precondition: The Doctor must be logged in.
Description: When the doctor presses the “Logout” button, he will be directed to 
the login window.
Postcondition: Doctor will log out successfully & won’t use the app without login 
again.


14.Add Doctor
Actor: User (Admin)
Precondition: Must be logged in.
Description: The admin should enter new doctor id, password and confirm 
password then create doctor.
Postcondition: New doctor information is saved in the firebase.


15.Delete Doctor
Actor: User (Admin)
Precondition: Must be logged in, doctor exists.
Description: The doctor should enter id, password and confirm password of the 
doctor to be deleted.
Postcondition: Doctor information will be deleted in the firebase.


16.Update Doctor
Actor: User (Doctor)
Precondition: Must be logged in and the doctor exists.
Description: The doctor should enter his old password, new password and 
confirm password to update his information.
Postcondition: Doctor information will be updated in the firebase and the system 
outputs “Password updated” message on screen.

-  Non-functional requirements
● Performance: The response time for the system is few milliseconds 
depending on the device it is working on.

● Maintainability: It is easy to maintain and update the system anytime 
because of the high system integrity.

● Portability and compatibility: The system can work on any RAM capacity 
equals or higher that 8 gigabyte. Moreover, it can be opened using any type 
of pc and any type of operating system.

● Usability: Due to the user-friendly design of the system and the utilization 
of the graphical user interface it is extremely easy for the users to use our 
system.

● Capacity: unlimited users can concurrently use it.

● Security: Only authorized users can access the system, and only authorized 
users for a specific patient can access the patient information.

## User Requirements

● The user shall be able to login to the system

● The user shall be able to add, delete, view and update patient information.

● The user shall be able to browse a blood smear image and examine the 
image for skin or leukemia cancer detection.

● The user shall be able to generate a report of the biopsy image.

● The user shall be able to save the generated report as pdf on pc.

● The user shall be able to view the reports numbers of the patient and 
choose which report to view.

● The user shall be able to update his password. 

● The user shall be able to logout of the system.

## System Requirements
● PC: The application works on pc that runs any operating system such as 
windows, linux ,mac os.

● Internet connection: This app uses a firebase to store data so you need to 
be connected to the internet to fetch, view and modify it.

## Domain Requirements
● The role between the responsible lab technician for a specific patient and 
other different types of users must be defined.

● RAM must be at least 8 gigabyte for the system to work.

## GUI 
-  Add Doctor with incorrect password OR password and confirm 
password are not identical

This allows the admin to add and delete doctors by providing the username, 
password and confirm password of the doctor. 
The password should be less than 6 characters and contain letters and numbers. 
If the admin doesn’t follow these constraints, the system outputs the message 
“Password should be at least character long and contain letters and numbers” on 
the screen. The fields of Password and Confirm Password must be identical

![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/d069636f-6870-4654-b375-868cb8ef0b01)

![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/25678214-5d1c-4753-947b-4b8ee05acd4b)


-   Add Doctor Successfully  
This allows the admin to add and delete doctor by providing the username, password and confirm password of the doctor. 
If the admin provides username, password and confirms password following password constraints, doctor is added successfully in the firebase and system outputs  “Doctor is added Successfully” message on screen.


![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/0e89a95c-aab9-4ba7-846b-199a1a5a492b)

-  Add Doctor with incomplete data
![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/4758633c-ebf6-42ec-8bd9-9295fc60f2a5)

-  Add Doctor that already exists
  This allows the admin to add and delete doctor by providing the username, password and confirm password of the doctor. 
If the admin provides the username of the doctor that already exists when adding a new doctor, the system outputs the “User already exists” message on screen.


![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/43cc41ba-761e-42ba-9f81-5fb03b8bca69)


-  Update Doctor with incorrect old password
  This screen allows the doctor to update his password by providing his old password, new password and confirm password. If the Doctor provides an incorrect old password, the system outputs a “No such doctor” message on screen.


![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/1e8d7066-f8d4-435c-8779-8b74cc2dae6e)

-  Update Doctor with incorrect password
  This screen allows the doctor to update his password by providing his old password, new password and confirm password.
The password should be less than 6 characters and contain letters and numbers. If the doctor doesn’t follow these constraints, the system outputs the message “Password should be at least character long and contain letters and numbers”  on the screen.

![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/fdbce25f-3cf9-4015-8e9c-a5afe0aae974) 

-  Update Doctor with unmatched new and confirm password

  This screen allows the doctor to update his password by providing his old password, new password and confirm password.
If the new and confirm password are unmatched, System outputs “New password and confirm password are not matched” message on screen. 


  ![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/cb94a6ea-217d-4cb7-b38d-582f9065ee5c) 


  -  Update doctor with incomplete data

    This screen allows the doctor to update his password by providing his old password, new password and confirm password.
If the doctor provides incomplete data, the system outputs a “Please complete the data” message on screen.


 ![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/723c8e14-f209-4850-8292-7f7acea6c7db) 

 -  Update Doctor successfully

This screen allows the doctor to update his password by providing old password, new password and confirm password. If the doctor provides the old, new and confirm password following password constraints, the doctor's password is updated successfully in the firebase and the system outputs  “Password updated” message on screen. 


![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/0af9f148-662a-4733-8594-46c63eb52e79) 

-  Add Patient

This screen allows doctor to add by providing name, gender, phone number and date of birth of patient, update by providing id and the new and old data of patient, delete by providing id of patient, search by providing id of patient, show reports numbers of patient, show data of all patients in the table and logout.   
If the doctor provides name, gender, phone number and Date of birth following constraints and presses the create patient button, a new patient is created successfully in the firebase and the system displays new patient data on the table.

![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/db465a9d-f2a3-45de-9b44-5284a26eb276)


-  Add patient with incorrect date of birth 

This screen allows doctor to add by providing name, gender, phone number and date of birth of patient, update by providing id and the new and old data of patient, delete by providing id of patient, search by providing id of patient, show reports numbers of patient, show data of all patients in the table and logout.   
The date of birth should be in dd/mm/yyyy format. If the doctor doesn’t follow these constraints, the system outputs the message “Enter date in dd/mm/yyyy” format  on the screen.


 ![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/fcc6bc5a-39f3-4c89-8568-0313aa0037c9) 

 -  Add Patient with incorrect phone number
   This screen allows doctor to add by providing name, gender, phone number and date of birth of patient, update by providing id and the new and old data of patient, delete by providing id of patient, search by providing id of patient, show reports numbers of patient, show data of all patients in the table and logout.   
If the doctor doesn’t follow phone number constraints, the system outputs the message “Invalid phone number” on the screen.


![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/4a092613-6ef4-4aa6-b096-2ba6c1a090bf) 

-  Incomplete data
  If data is incompleted show error message “Please complete the data”


![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/03cb620e-88fd-4f3d-834f-905e0fa19841) 

-  Update Patient  
This screen allows doctor to add by providing name, gender, phone number and date of birth of patient, update by providing id and the new and old data of patient, delete by providing id of patient, search by providing id of patient, show reports numbers of patient, show data of all patients in table and logout. Doctor provides the data to be modified in patient and id of patient to be updated, patient data will be updated from firebase and the row containing patient data will be updated with the modified patient data in the table.


![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/954b0f88-ea64-458c-a501-4afb65d5c8c8)



![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/e1860e07-65bd-4fa9-bfde-3c9a1dafebf2)


-  Choose Section
  This screen allows the doctor to choose whether to go to the patient management section of the system to create new patients and access data and report of existing patients or to go to the sample examination section to examine biopsy images.

![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/43ac68d0-2608-4939-8d42-a2195f5e1a3b)

-  Choose Cancer Section
  This screen allows doctors to choose whether to go to the leukemia cancer detection section or to the skin cancer detection section.


![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/fe4b5def-cd4c-4bbd-9b13-ac9abcf9b67e)


-  peripheral blood smear examination

  This screen allows doctor to perform examination on blood smear image by providing patient id and name and upload image of blood smear from device by pressing button browse then the system will perform detection on image and identify the location of cancer cells. When the doctor presses the generate report button, the system generates a report of the case.


  ![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/9ccc9e43-3747-4ff3-9742-95ff70afb0c9) 


-  Examination Report of Skin Cancer
  This screen allows the doctor to view report of the examined skin biopsy, save report to firebase along with patient data and save data as pdf in the desired location in pc. 

  ![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/ae0d65ae-6972-4004-a842-16a2036c8737) 

  -  Examination Report of Leukemia
    This screen allows the doctor to view the report of the examined peripheral blood smear, save the report to firebase along with patient data and save data as pdf in the desired location on the PC.


![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/da96eebd-5af2-4ab7-be26-1993e15a7f55)


-  The Generated Report as pdf
  The screen shows the generated report of blood smear image as pdf on pc. 


  ![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/aa028154-b9a5-4015-ae68-4bcb0a3ec6ea) 

  -  Skin biopsy examination   
  This screen allows the doctor to perform an examination on skin biopsy image by providing patient id and name and upload image of blood smear from device by pressing browse button then the system will perform detection on image and identify the location of cancer cells. When the doctor presses the generate report button, the system generates a report of the case.

![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/e127a992-ca6f-44e1-8901-3a38fe79be10)

-  Login 

This screen allows the doctor and admin to login to the system by providing an id and password. The user must enter the correct id and password to access the system otherwise a message will be shown saying “Wrong doctor password or ID 


![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/4285e285-7d67-429f-99b9-58ef06671671)


-  View saved report
  This screen allows the doctor to view the reports numbers of the saved reports of the patient and to view and save the report as pdf by providing patient id and report number and press the show report button. After pressing the show report button , the doctor will be redirected to the Examination Report window and the report will be displayed on screen.


![image](https://github.com/Maha-emad/Caner-Detection-Assistant/assets/71048834/2fc78024-647a-4f46-9575-768711d41b16)




 
 

## Demo
 
https://drive.google.com/file/d/1OWJ9XI6PzgfKCVEKYYGiJ4wlAkK6yql0/view?usp=sharing

 
