import tkinter as tk
from datetime import datetime
import json
import time
import data
import hashlib


windows=tk.Tk()
windows.geometry('1000x700')
windows.title('Trafficware - Cabinets')
windows.iconbitmap('flame.ico')
#windows.attributes("-topmost",True)
##frame=tk.Frame(master=windows, width=650, height=600)
Label_technitian_value=None

#background color yellow
def background_yellow():
    Frame_technitian.configure(bg="gold")
    Frame_spot.configure(bg="gold")
    Frame_CabinetType.configure(bg="gold")
    Frame_customer.configure(bg="gold")
    Frame_cabinet.configure(bg="gold")
    Frame_SN.configure(bg="gold")
    Frame_Message1.configure(bg="gold")
    Frame_Message2.configure(bg="gold")
    Frame_button.configure(bg="gold")

#background color green
def background_green():
    Frame_technitian.configure(bg="SpringGreen3")
    Frame_spot.configure(bg="SpringGreen3")
    Frame_CabinetType.configure(bg="SpringGreen3")
    Frame_customer.configure(bg="SpringGreen3")
    Frame_cabinet.configure(bg="SpringGreen3")
    Frame_SN.configure(bg="SpringGreen3")
    Frame_Message1.configure(bg="SpringGreen3")
    Frame_Message2.configure(bg="SpringGreen3")
    Frame_button.configure(bg="SpringGreen3")

#background color red
def background_red():
    Frame_technitian.configure(bg="firebrick")
    Frame_spot.configure(bg="firebrick")
    Frame_CabinetType.configure(bg="firebrick")
    Frame_customer.configure(bg="firebrick")
    Frame_cabinet.configure(bg="firebrick")
    Frame_SN.configure(bg="firebrick")
    Frame_Message1.configure(bg="firebrick")
    Frame_Message2.configure(bg="firebrick")
    Frame_button.configure(bg="firebrick")

    

##------------------------------------Check technitian------------------------##
        #--------------------------------------------------------------#
def CheckandMove(event):
    global technitian_index
    start_time=time.time()
    end_time=0
    lapsed_time=0
    #data.Technitian_validate=True
    try:
        i=0
        find=False
        while(i<len(List_technitians_data) and find==False):
            if List_technitians_data[i]["id"]==Data_input.get():
                find=True
                technitian_index=i
                Data_Spot.focus()
                dt = datetime.now()
                #Frame_technitian.configure(bg="gold")
                background_yellow()
                data.Technitian_validate=True
                Label_message.configure(text="--Escanear Gabinete--")
                Label_message_2.configure(text=List_technitians_data[technitian_index]["firstName"]+" " +List_technitians_data[technitian_index]["lastName"]+" : "+List_technitians_data[technitian_index]["process"])
                #Validate_technitian=Technitian_id.index(Data_input.get())
            i=i+1
        if find==False:
            Frame_technitian.configure(bg="firebrick1")
            Frame_technitian.pack() 
            Data_input.delete(0,'end')
            Data_input_name.delete(0,'end')
            Data_input.focus()
            Label_message.configure(text="--Tecnico no registrado--")
            Label_message_2.configure(text="No found")
    except:
        Frame_technitian.configure(bg="firebrick1")
        Frame_technitian.pack()
        #print(-1) 
        Data_input.delete(0,'end')
        Data_input_name.delete(0,'end')
        Data_input.focus()
        Label_message.configure(text="--Tecnico no registrado--")
        Label_message_2.configure(text="Error")
  
#Open json tracking cabinets
file_tracking=open('Tracking_Cabinets.json')
Cabinets_in_production=json.load(file_tracking)
list_cabinets_in_floor=Cabinets_in_production['cabinets']
file_tracking.close()

#open json cabinets history
file_tracking_done=open('Cabinets_History.json')
Cabinets_done=json.load(file_tracking_done)
list_cabinets_done=Cabinets_done['cabinets']
file_tracking_done.close()

technitian_index=-1
f=open('Technitians.json')
Technitians_data=json.load(f)
List_technitians_data=Technitians_data['Technitians']
print(List_technitians_data)
Technitian_id=[]
for i in List_technitians_data:
    row_Technitians=i['id']
    Technitian_id.append(row_Technitians)
Cabinets_list={}
f.close()

def update_list_cabinets_in_floor():
    global list_cabinets_in_floor
    file_tracking=open('Tracking_Cabinets.json')
    Cabinets_in_production=json.load(file_tracking)
    list_cabinets_in_floor=Cabinets_in_production['cabinets']
    file_tracking.close()

def update_list_cabinets_history():
    global list_cabinets_done
    file_tracking_done=open('Cabinets_History.json')
    Cabinets_done=json.load(file_tracking_done)
    list_cabinets_done=Cabinets_done['cabinets']
    file_tracking_done.close()
    
#print(Technitian_id)
Cabinet_Type=''
Cabinet_Customer=''
Cabinet=''
Serial_number=''
Spot_cabinet=''

def Place_Entry():
    global Label_technitian_value
    global Label_Spot_value
    global Label_type_value
    global Label_customer_value
    global Label_cabinet_value
    global Label_sn_value

    #Technitian
    Label_technitian_value.pack_forget()
    Data_input.pack(side='left',fill=tk.X,padx=30)
    Data_input.delete(0,'end')
    Data_input.focus()

    #Spot
    Label_Spot_value.pack_forget()
    Data_Spot.pack(side=tk.LEFT,fill=tk.X,padx=10)
    Data_Spot.delete(0,'end')

    #Type
    Label_type_value.pack_forget()
    Data_input_name.pack(side=tk.LEFT,fill=tk.X,padx=10)
    Data_input_name.delete(0,'end')

    #Customer
    Data_input_customer.pack(side=tk.LEFT,fill=tk.X,padx=45)
    Data_input_customer.delete(0,'end')
    Label_customer_value.pack_forget()

    #Cabinet
    Data_input_cabinet.pack(side=tk.LEFT,fill=tk.X,padx=30)
    Data_input_cabinet.delete(0,'end')
    Label_cabinet_value.pack_forget()

    #Serial number
    Data_input_SerialNumber.pack(side=tk.LEFT,fill=tk.X)
    Data_input_SerialNumber.delete(0,'end')
    Label_sn_value.pack_forget()

    Data_done.delete(0,'end')
    Data_done.pack_forget()
    Done_button.pack_forget()

    
def Place_labels():
    global Label_technitian_value
    global Label_Spot_value
    global Label_type_value
    global Label_customer_value
    global Label_cabinet_value
    global Label_sn_value

    #Technitian
    Data_input.pack_forget()
    Label_technitian_value=tk.Label(Frame_technitian,font=("arial",30),text=Data_input.get())
    Label_technitian_value.pack(padx=10,side='left')

    #Spot
    Data_Spot.pack_forget()
    Label_Spot_value=tk.Label(Frame_spot,font=("arial",30),text=Data_Spot.get())
    Label_Spot_value.pack(padx=10,side='left')

    #Type
    Data_input_name.pack_forget()
    Label_type_value=tk.Label(Frame_CabinetType,font=("arial",30),text=Data_input_name.get())
    Label_type_value.pack(padx=10,side='left')

    #customer
    Data_input_customer.pack_forget()
    Label_customer_value=tk.Label(Frame_customer,font=("arial",30),text=Data_input_customer.get())
    Label_customer_value.pack(padx=10,side='left')

    #Cabinet
    Data_input_cabinet.pack_forget()
    Label_cabinet_value=tk.Label(Frame_cabinet,font=("arial",30),text=Data_input_cabinet.get())
    Label_cabinet_value.pack(padx=10,side='left')

    #Serial number
    Data_input_SerialNumber.pack_forget()
    Label_sn_value=tk.Label(Frame_SN,font=("arial",30),text=Data_input_SerialNumber.get())
    Label_sn_value.pack(padx=10,side='left')

    Data_done.pack(side='left')
    Data_done.focus()

    
    
#Spot
def Spot(event):
    global Spot_cabinet
    Spot_value=Data_Spot.get()
    Spot_cabinet=Data_Spot.get()
    print(Spot_value)
    print(Spot_cabinet[0:4])
    if ("Spot"==Spot_cabinet[0:4]):
        Data_input_name.focus()
    else:
        Label_message.configure(bg="firebrick1")
        Frame_technitian.pack()
        Data_input.delete(0,'end')
        Data_input_name.delete(0,'end')
        Data_Spot.delete(0,'end')
        Data_input.focus()
        Label_message.configure(text="--Lugar no registrado--")
        Label_message_2.configure(text="No found")
    
    

def write_json(new_data):
    with open('Tracking_Cabinets.json','r+') as fi:
        file_data=json.load(fi)
        #print('exists')
        #print(file_data)
        file_data['cabinets'].append(new_data)
        fi.seek(0)
        json.dump(file_data,fi,indent=4)
    #Open json tracking cabinets
    file_tracking=open('Tracking_Cabinets.json')
    Cabinets_in_production=json.load(file_tracking)
    list_cabinets_in_floor=Cabinets_in_production['cabinets']
    file_tracking.close()
    print(list_cabinets_in_floor)
    
#----------------------------------Check cabinet--------------------------------------#
        #----------------------------------------------------------------------#
def Done_mechanical_assembly(index):
    global Data_done
    global Done_button
    global list_cabinets_in_floor
    with open('Tracking_Cabinets.json','r+') as fi:
        Cabinets_data=json.load(fi)
        Cabinets_data['cabinets'][index]['Stamp_time_mechanical_assembly']=Cabinets_data['cabinets'][index]['Stamp_time']
        Cabinets_data['cabinets'][index]['Current_place']="Waiting electrical assembly"
        Cabinets_data['cabinets'][index]['Stamp_time']=str(datetime.now())
        Cabinets_data['cabinets'][index]['Technitian_Mechanical']=Cabinets_data['cabinets'][index]['Technitian']
        fi.seek(0)
        json.dump(Cabinets_data,fi,indent=4)
        list_cabinets_in_floor=Cabinets_data['cabinets']
    Label_message.configure(text="--Mechanical assembly complete--")
    Label_message_2.configure(text="--Now is waiting to electrical assembly--")
    #print(list_cabinets_in_floor)
    Done_button.pack_forget()
    Place_Entry()
    Data_done.pack_forget()
    windows.geometry('1000x700')
    background_green()
    

    #Done_electrical_assembly
def Done_electrical_assembly(index):
    with open('Tracking_Cabinets.json','r+') as fi:
        Cabinets_data=json.load(fi)
        Cabinets_data['cabinets'][index]['Stamp_time_electrical_assembly']=Cabinets_data['cabinets'][index]['Stamp_time']
        Cabinets_data['cabinets'][index]['Stamp_time']=str(datetime.now())
        Cabinets_data['cabinets'][index]['Technitian_Electrical_Assembly']=Cabinets_data['cabinets'][index]['Technitian']
        Cabinets_data['cabinets'][index]['Current_place']="Waiting electrical test"
        fi.seek(0)
        json.dump(Cabinets_data,fi,indent=4)
    Label_message.configure(text="--Electrical assembly complete--")
    Label_message_2.configure(text="--Now is waiting to electrical test--")
    windows.geometry('1000x700')
    Done_button.pack_forget()
    Place_Entry()
    background_green()

    #Done_electrical_test
def remove_Done_electrical_test(index):
    with open('Tracking_Cabinets.json','r+') as fi:
        Cabinets_data=json.load(fi)
        Cabinets_data['cabinets'][index]['Stamp_time_electrical_test']=Cabinets_data['cabinets'][index]['Stamp_time']
        Cabinets_data['cabinets'][index]['Stamp_time']=str(datetime.now())
        Cabinets_data['cabinets'][index]['Technitian_Electrical_Test']=Cabinets_data['cabinets'][index]['Technitian']
        Cabinets_data['cabinets'][index]['Current_place']="Waiting Packing"
        fi.seek(0)
        json.dump(Cabinets_data,fi,indent=4)
    Place_Entry()
    Label_message.configure(text="--Electrical test complete--")
    Label_message_2.configure(text="--Now is waiting for Packing--")
    windows.geometry('1000x700')
    Done_button.pack_forget()
    background_green()

    #Done_packing
def Done_packing(index):
    global Done_button
    update_list_cabinets_in_floor()
    with open('Tracking_Cabinets.json','r') as readCabinets:
        Cabinets_data=json.load(readCabinets)
        Cabinets_data['cabinets'][index]['Current_place']="Waiting Quality inspection"
        Cabinets_data['cabinets'][index]['Stamp_time_packing']=Cabinets_data['cabinets'][index]['Stamp_time']
        Cabinets_data['cabinets'][index]['Stamp_time']=str(datetime.now())
        Cabinets_data['cabinets'][index]['Technitian_Packing']=Cabinets_data['cabinets'][index]['Technitian']
    with open('Tracking_Cabinets.json','w') as writeCabinets:
        json.dump(Cabinets_data,writeCabinets,indent=4)
    Place_Entry()
    Label_message.configure(text="--Packing complete--")
    Label_message_2.configure(text="--Now is waiting for Quality inspection--")
    windows.geometry('1000x700')
    Done_button.pack_forget()
    background_green()

    #Done_quality_inspection
def Done_electrical_test(index):
    global Done_button
    #Add cabinet to the list of the history list
    with open('Tracking_Cabinets.json','r') as readCabinets:
        Cabinets_data=json.load(readCabinets)
        Cabinets_data['cabinets'][index]['Stamp_time_end']=str(datetime.now())
    with open('Tracking_Cabinets.json','w') as writeCabinets:
        json.dump(Cabinets_data,writeCabinets,indent=4)
    update_list_cabinets_in_floor()
    print(list_cabinets_in_floor[index])
    with open('Cabinets_History.json','r') as readCabinets_history:
        Cabinets_data_history=json.load(readCabinets_history)
        Cabinets_data_history['cabinets'].append(list_cabinets_in_floor[index])
    with open('Cabinets_History.json','w') as writeCabinets_history:
        json.dump(Cabinets_data_history,writeCabinets_history,indent=1)
    #Remove cabinet for the list of the floor production
    with open('Tracking_Cabinets.json','r') as readCabinets:
        print("delete")
        Cabinets_data=json.load(readCabinets)
        print(Cabinets_data['cabinets'][index])
        del Cabinets_data['cabinets'][index]
    with open('Tracking_Cabinets.json','w') as writeCabinets:
        json.dump(Cabinets_data,writeCabinets,indent=4)
    Place_Entry()
    Label_message.configure(text="--Cabinet complete--")
    Label_message_2.configure(text="--Scan new cabinet--")
    windows.geometry('1000x700')
    update_list_cabinets_history()
    Done_button.pack_forget()
    background_green()
    

def update_index_cabinet():
    global checksum_value
    update_list_cabinets_in_floor()
    i_cabinet=0
    index_find=False
    while(i_cabinet<len(list_cabinets_in_floor) and index_find==False):    
        if(checksum_value==list_cabinets_in_floor[i_cabinet]['Checksum']):
            index_find=True
        else:
            i_cabinet=i_cabinet+1
    print("i_cabinet: ",i_cabinet)
    print("lenght: ",len(list_cabinets_in_floor))
    print("checksum cabinet",checksum_value)
    try:
        print("checksum index",list_cabinets_in_floor[i_cabinet]['Checksum'])
    except:
        print("out of index")
    return i_cabinet
    
def Check_cabinet(event):
    global list_cabinets_in_floor
    global checksum_value
    global Data_done
    global Done_button
    global Label_technitian_value
    #global list_cabinets_in_floor
    Data_input.focus()
    #print(Data_input_name.get())
    #print(data.Technitian_validate)
    #Open json tracking cabinets
    file_tracking=open('Tracking_Cabinets.json')
    Cabinets_in_production=json.load(file_tracking)
    list_cabinets_in_floor=Cabinets_in_production['cabinets']
    file_tracking.close()
    
    if(data.Technitian_validate==True):

        ##Get data from the widgets##
        Cabinet_Type=Data_input_name.get()
        Cabinet_Customer=Data_input_customer.get()
        Cabinet=Data_input_cabinet.get()
        Serial_number=Data_input_SerialNumber.get()
        Cabinet_split=Cabinet.split()
        order=Cabinet_split[0]
        PartNumber=Cabinet_split[1]
        ##Get Checksum##
        Cabinet_header=Cabinet_Type+Cabinet_Customer+order+PartNumber+Serial_number
        Cabinet_MD5=hashlib.md5(Cabinet_header.encode())
        print(technitian_index)
        checksum_value=Cabinet_MD5.hexdigest()

        #--------------------check if cabinet is on production---------------------#
        #--------------------------------------------------------------------------#
        #--------------------------------------------------------------------------#
        i_cabinet=0
        index_find=False
        while(i_cabinet<len(list_cabinets_in_floor) and index_find==False):    
            #print("i_cabinet= "+str(i_cabinet))
            #print("MD5: "+str(list_cabinets_in_floor[i_cabinet]['Checksum']))
            if(Cabinet_MD5.hexdigest()==list_cabinets_in_floor[i_cabinet]['Checksum']):
                index_find=True
            else:
                i_cabinet=i_cabinet+1
        print("i_cabinet: ",i_cabinet)
        print("lenght: ",len(list_cabinets_in_floor))
        print("checksum cabinet",Cabinet_MD5.hexdigest())
        try:
            print("checksum index",list_cabinets_in_floor[i_cabinet]['Checksum'])
        except:
            print("out of index")
        #print(list_cabinets_in_floor)


        #-------------Cabinet is in production-------------------#
                    #-------------------------------#
        if(i_cabinet<len(list_cabinets_in_floor)):
            if(Cabinet_MD5.hexdigest()==list_cabinets_in_floor[i_cabinet]['Checksum']):
                print('cabinet is in production line')
                        
            #mechanical assembly scan cabinet
                if(list_cabinets_in_floor[i_cabinet]['Current_place']=='Mechanical assembly'):
                    if(List_technitians_data[technitian_index]["process"]=="Mechanical assembly" or List_technitians_data[technitian_index]["process"]=="Assembly"):
                        windows.geometry('1000x700')
                        Done_button = tk.Button(Frame_button,text="Done",width='10',command=lambda: Done_mechanical_assembly(i_cabinet))
                        Done_button.pack(padx=10,side='left')
                        background_yellow()
                        #Frame_cabinet.configure(bg="SpringGreen3")
                        Place_labels()
                        Label_message.configure(text="--Current place: Mechanical assembly--")
                        Label_message_2.configure(text="--In process--")
                    else:
                        Frame_cabinet.configure(bg="firebrick")
                        Data_input.delete(0,'end')
                        Data_input_name.delete(0,'end')
                        Data_input_customer.delete(0,'end')
                        Data_input_cabinet.delete(0,'end')
                        Data_input_SerialNumber.delete(0,'end')
                        Data_Spot.delete(0,'end')
                        Label_message.configure(text="--Current place: Mechanical assembly--")
                        Label_message_2.configure(text=List_technitians_data[technitian_index]["process"]+" denied access.")

            
                #Waiting electrical assembly
                elif(list_cabinets_in_floor[i_cabinet]['Current_place']=='Waiting electrical assembly'):
                    if(List_technitians_data[technitian_index]["process"]=="Electrical assembly" or List_technitians_data[technitian_index]["process"]=="Assembly"):
                        print("Enter electrical assembly in waiting electrical assembly")
                        with open('Tracking_Cabinets.json','r') as readCabinets:
                            Cabinets_data=json.load(readCabinets)
                            Cabinets_data['cabinets'][i_cabinet]['Technitian_Mechanical']=Cabinets_data['cabinets'][i_cabinet]['Technitian']
                            Cabinets_data['cabinets'][i_cabinet]['Stamp_time_Waiting_electrical_assembly']=Cabinets_data['cabinets'][i_cabinet]['Stamp_time']
                            Cabinets_data['cabinets'][i_cabinet]['Stamp_time']=str(datetime.now())
                            Cabinets_data['cabinets'][i_cabinet]['Technitian']=Data_input.get()
                            Cabinets_data['cabinets'][i_cabinet]['Current_place']="Electrical assembly"
                        with open('Tracking_Cabinets.json','w') as writeCabinets: 
                            json.dump(Cabinets_data,writeCabinets,indent=4)
                        list_cabinets_in_floor=Cabinets_data['cabinets']
                        Done_button = tk.Button(Frame_button,text="Done",width='10',command=lambda: Done_electrical_assembly(i_cabinet))
                        Done_button.pack(padx=10,side='left')
                        Place_labels()
                        windows.geometry('1000x700')
                        #Label_message.configure(text="--Current place: Electrical assembly--")
                        #Label_message_2.configure(text="--"+List_technitians_data[technitian_index]["process"]+"--")
                        #print(list_cabinets_in_floor)
                        #Label_technitian_value=tk.Label(Frame_technitian,font=("arial",16),text=List_technitians_data[technitian_index]["id"])
                        #Label_technitian_value.pack(side='left',fill=tk.X,padx=10)
                        background_yellow()
                        
                    else:
                        print("not an electrical assembly")
                        Frame_cabinet.configure(bg="firebrick1")
                        Data_input.delete(0,'end')
                        Data_input_name.delete(0,'end')
                        Data_input_customer.delete(0,'end')
                        Data_input_cabinet.delete(0,'end')
                        Data_input_SerialNumber.delete(0,'end')
                        Data_Spot.delete(0,'end')
                        Label_message.configure(text="--Waiting Electrical assembly--")
                        Label_message_2.configure(text=List_technitians_data[technitian_index]["process"]+" denied access.")
                

            #Electrical assembly
                elif(list_cabinets_in_floor[i_cabinet]['Current_place']=='Electrical assembly'):
                    if(List_technitians_data[technitian_index]["process"]=="Electrical assembly" or List_technitians_data[technitian_index]["process"]=="Assembly"):
                        windows.geometry('1000x700')
                        Done_button = tk.Button(text="Done",width='10',command=lambda: Done_electrical_assembly(i_cabinet))
                        Done_button.pack(padx=10,side='left')
                        Frame_cabinet.configure(bg="SpringGreen3")
                        Place_labels()
                        Label_message.configure(text="--Current place: Electrical assembly--")
                        Label_message_2.configure(text="--In process--")
                        background_yellow()
                    else:
                        Frame_cabinet.configure(bg="firebrick1")
                        Data_input.delete(0,'end')
                        Data_input_name.delete(0,'end')
                        Data_input_customer.delete(0,'end')
                        Data_input_cabinet.delete(0,'end')
                        Data_input_SerialNumber.delete(0,'end')
                        Data_Spot.delete(0,'end')
                        Label_message.configure(text="--Current place: Electrical assembly--")
                        Label_message_2.configure(text=List_technitians_data[technitian_index]["process"]+" denied access.")


            #Waiting electrical test
                elif(list_cabinets_in_floor[i_cabinet]['Current_place']=='Waiting electrical test'):
                    if(List_technitians_data[technitian_index]["process"]=="Electrical test"):
                        print("Enter electrical test in waiting electrical test")
                        with open('Tracking_Cabinets.json','r') as readCabinets:
                            Cabinets_data=json.load(readCabinets)    
                            Cabinets_data['cabinets'][i_cabinet]['Current_place']="Electrical test"
                            Cabinets_data['cabinets'][i_cabinet]['Stamp_time_Waiting_electrical_test']=Cabinets_data['cabinets'][i_cabinet]['Stamp_time']
                            Cabinets_data['cabinets'][i_cabinet]['Stamp_time']=str(datetime.now())
                            Cabinets_data['cabinets'][i_cabinet]['Technitian']=Data_input.get()
                        with open('Tracking_Cabinets.json','w') as writeCabinets:
                            json.dump(Cabinets_data,writeCabinets,indent=4)
                        list_cabinets_in_floor=Cabinets_data['cabinets']
                        Done_button = tk.Button(Frame_button,text="Done",width='10',command=lambda: Done_electrical_test(i_cabinet))
                        Done_button.pack(padx=10,side='left')
                        windows.geometry('1000x700')
                        #Label_message.configure(text="--Current place: Electrical assembly--")
                        #Label_message_2.configure(text="--"+List_technitians_data[technitian_index]["process"]+"--")
                        #print(list_cabinets_in_floor)
                        Place_labels()
                        Data_input.delete(0,'end')
                        Data_input_name.delete(0,'end')
                        Data_input_customer.delete(0,'end')
                        Data_input_cabinet.delete(0,'end')
                        Data_input_SerialNumber.delete(0,'end')
                        Data_Spot.delete(0,'end')
                        background_yellow()
                    else:
                        Frame_cabinet.configure(bg="firebrick1")
                        Data_input.delete(0,'end')
                        Data_input_name.delete(0,'end')
                        Data_input_customer.delete(0,'end')
                        Data_input_cabinet.delete(0,'end')
                        Data_input_SerialNumber.delete(0,'end')
                        Data_Spot.delete(0,'end')
                        Label_message.configure(text="--Waiting Electrical test--")
                        Label_message_2.configure(text=List_technitians_data[technitian_index]["process"]+" denied access.")

            #Electrical Test

                elif(list_cabinets_in_floor[i_cabinet]['Current_place']=='Electrical test'):
                    if(List_technitians_data[technitian_index]["process"]=="Electrical test"):
                        Done_button = tk.Button(master=Frame_button,text="Done",width='10',command=lambda: Done_electrical_test(i_cabinet))
                        Done_button.pack(padx=10,side='left')
                        windows.geometry('1000x700')
                        #Frame_cabinet.configure(bg="SpringGreen3")
                        Place_labels()
                        Label_message.configure(text="--Current place: Electrical test--")
                        Label_message_2.configure(text="--In process--")
                        background_yellow()
                        
                    else:
                        Frame_cabinet.configure(bg="firebrick1")
                        Data_input.delete(0,'end')
                        Data_input_name.delete(0,'end')
                        Data_input_customer.delete(0,'end')
                        Data_input_cabinet.delete(0,'end')
                        Data_input_SerialNumber.delete(0,'end')
                        Data_Spot.delete(0,'end')
                        Label_message.configure(text="--Current place: Electrical test--")
                        Label_message_2.configure(text=List_technitians_data[technitian_index]["process"]+" denied access.")

            #Waiting Quality inspection
               

            #Waiting Packing
                elif(list_cabinets_in_floor[i_cabinet]['Current_place']=='Waiting Packing'):
                    if(List_technitians_data[technitian_index]["process"]=="Packing"):
                        print("Enter Quality inspector in waiting quality inspection")
                        with open('Tracking_Cabinets.json','r') as readCabinets:
                            Cabinets_data=json.load(readCabinets)    
                            Cabinets_data['cabinets'][i_cabinet]['Current_place']="Packing"
                            #Cabinets_data['cabinets'][i_cabinet]['Technitian_Packing']=Cabinets_data['cabinets'][i_cabinet]['Technitian']
                            Cabinets_data['cabinets'][i_cabinet]['Stamp_Waiting_packing']=Cabinets_data['cabinets'][i_cabinet]['Stamp_time']
                            Cabinets_data['cabinets'][i_cabinet]['Stamp_time']=str(datetime.now())
                            Cabinets_data['cabinets'][i_cabinet]['Technitian']=Data_input.get()
                        with open('Tracking_Cabinets.json','w') as writeCabinets:
                            json.dump(Cabinets_data,writeCabinets,indent=4)
                        list_cabinets_in_floor=Cabinets_data['cabinets']
                        Done_button = tk.Button(Frame_button,text="Done",width='10',command=lambda: Done_packing(i_cabinet))
                        Done_button.pack(padx=10,side='left')
                        windows.geometry('1000x700')
                        #Label_message.configure(text="--Current place: Electrical assembly--")
                        #Label_message_2.configure(text="--"+List_technitians_data[technitian_index]["process"]+"--")
                        #print(list_cabinets_in_floor)
                        Place_labels()
                        Data_input.delete(0,'end')
                        Data_input_name.delete(0,'end')
                        Data_input_customer.delete(0,'end')
                        Data_input_cabinet.delete(0,'end')
                        Data_Spot.delete(0,'end')
                        Data_input_SerialNumber.delete(0,'end')
                        background_yellow()
                    else:
                        Frame_cabinet.configure(bg="firebrick1")
                        Data_input.delete(0,'end')
                        Data_input_name.delete(0,'end')
                        Data_input_customer.delete(0,'end')
                        Data_input_cabinet.delete(0,'end')
                        Data_input_SerialNumber.delete(0,'end')
                        Data_Spot.delete(0,'end')
                        Label_message.configure(text="--Waiting Packing--")
                        Label_message_2.configure(text=List_technitians_data[technitian_index]["process"]+" access denied.")

            #Packing

                elif(list_cabinets_in_floor[i_cabinet]['Current_place']=='Packing'):
                    if(List_technitians_data[technitian_index]["process"]=="Packing"):
                        Done_button = tk.Button(master=Frame_button,text="Done",width='10',command=lambda: Done_packing(i_cabinet))
                        Done_button.pack(padx=10,side='left')
                        windows.geometry('1000x700')
                        Frame_cabinet.configure(bg="SpringGreen3")
                        Place_labels()
                        Label_message.configure(text="--Current place: Packing--")
                        Label_message_2.configure(text="--In process--")
                        background_yellow()
                    else:
                        Frame_cabinet.configure(bg="firebrick1")
                        Data_input.delete(0,'end')
                        Data_input_name.delete(0,'end')
                        Data_input_customer.delete(0,'end')
                        Data_input_cabinet.delete(0,'end')
                        Data_input_SerialNumber.delete(0,'end')
                        Data_Spot.delete(0,'end')
                        Label_message.configure(text="--Current place: Packing--")
                        Label_message_2.configure(text=List_technitians_data[technitian_index]["process"]+" denied access.")

        


        ##Write Cabinet info to Json##
        #jsonString=json.dumps(Cabinet_info)
        #jsonFile=open("Tracking_Cabinets.json","w")
        #jsonFile.write(jsonString)
        #jsonFile.close()
        #with open("Tracking_Cabinets.json","w") as write_file:
         #   json.dump(Cabinet_info,write_file)
        #print(Cabinet_info)
        
                
                #Cabinet is not in production, now will be check if is in History
         #------------------------------------------------------------------------------------#
        elif(i_cabinet==len(list_cabinets_in_floor)):
            print(str(i_cabinet)+" "+str(len(list_cabinets_in_floor)))
            i_cabinet_done=0
            #looking up for the cabinet in the history file json
            while(i_cabinet_done<len(list_cabinets_done) and Cabinet_MD5.hexdigest()!=list_cabinets_done[i_cabinet_done]['Checksum']):
                #print(list_cabinets_done[i_cabinet_done]['Checksum'])
                i_cabinet_done=i_cabinet_done+1
            print("i_cabinet_done: "+str(i_cabinet_done))

            #Cabinet is in History file
            if(i_cabinet_done<len(list_cabinets_done)):
                if(Cabinet_MD5.hexdigest()==list_cabinets_done[i_cabinet_done]['Checksum']):
                    #Frame_cabinet.configure(bg="SpringGreen3")
                    Data_input.delete(0,'end')
                    Data_input_name.delete(0,'end')
                    Data_input_customer.delete(0,'end')
                    Data_input_cabinet.delete(0,'end')
                    Data_input_SerialNumber.delete(0,'end')
                    Data_Spot.delete(0,'end')
                    data.Technitian_validate=False
                    Label_message.configure(text="--Cabinet is in History file--")
                    Label_message_2.configure(text="--Finished cabinet--")
                    background_red()

             #Cabinet doesn't exist, recording new cabinet
            elif(i_cabinet_done==len(list_cabinets_done) and i_cabinet==len(list_cabinets_in_floor)):
                if(List_technitians_data[technitian_index]["process"]=="Electrical test"):
                    Cabinet_info={"Technitian":Data_input.get(),"Checksum":Cabinet_MD5.hexdigest(),"Cabinet_type":Cabinet_Type,"Spot":Spot_cabinet,"Customer":Cabinet_Customer,"Sales Order":order,"Cabinet_Part_Number":PartNumber,"Cabinet_SN":Serial_number,"Stamp_time":str(datetime.now()),"Current_place":"Electrical test"}
                    write_json(Cabinet_info)
                    windows.geometry('650x600')
                    Done_button = tk.Button(Frame_button,text="Done",width='10',command=lambda: Done_electrical_test(i_cabinet))
                    Done_button.pack(padx=10,side='left')
                    Data_done=tk.Entry(Frame_button,font=("arial",16))
                    Data_done.bind('<Return>',lambda event: Scanner_done(event, Scanner_index=i_cabinet))
                    Data_done.pack(side='left',fill=tk.X,padx=30)
                    Data_done.focus()
                    #Frame_cabinet.configure(bg="SpringGreen3")
                    

                    #Frame_technitian=tk.Frame(windows,width=200,height=50)
                    #Frame_technitian.pack(fill=tk.BOTH,expand=True)
                    #Label_technitian_value=tk.Label(Frame_technitian,font=("arial",16),text="Technician:")

                    Place_labels()

                    data.Technitian_validate=False
                    background_yellow()
                    

                #Cabinet doesn't exist, The technitian is diferent to a mechanical assembly, can't record a new cabinet.
                elif(List_technitians_data[technitian_index]["process"]!="Mechanical assembly"):
                    Frame_cabinet.configure(bg="firebrick1")
                    Data_input.delete(0,'end')
                    Data_input_name.delete(0,'end')
                    Data_input_customer.delete(0,'end')
                    Data_input_cabinet.delete(0,'end')
                    Data_input_SerialNumber.delete(0,'end')
                    Data_Spot.delete(0,'end')
                    data.Technitian_validate=False
                    Label_message.configure(text="--Technitian is not Mechanical assembly--")
                    Label_message_2.configure(text="--Can't record new cabinet--")
                
def Scanner_done(event, Scanner_index):
    global list_cabinets_in_floor
    global Data_done
    i=0
    find=False
    index_cabinet=update_index_cabinet()
    print(Data_done.get())
    while(i<len(List_technitians_data) and find==False):
        if List_technitians_data[i]["id"]==Data_done.get():
            find=True
        i=i+1
    if(find==True):
        Place_Entry()
        print("is a technitian")
    elif(Data_done.get()=="Done_electrical_test"):
        if(list_cabinets_in_floor[index_cabinet]['Current_place']=='Electrical test'):
            Done_electrical_test(index_cabinet)
            print('Done')
        else:
            print('is no electrical test')

def focusToCustomer(event):
    Data_input_customer.focus()

def focusToCabinet(event):
    Data_input_cabinet.focus()

def focusToSN(event):
    Data_input_SerialNumber.focus()

#-----------------------------------Widgets---------------------------------------#
    #--------------------------------------------------------------------------#

##Technitian    
Frame_technitian=tk.Frame(windows,width=200,height=50)
Frame_technitian.pack(fill=tk.BOTH,expand=True)
Label_technitian=tk.Label(Frame_technitian,font=("arial",30),text="Technician:")
Label_technitian.pack(side='left',fill=tk.X,padx=10)
Data_input=tk.Entry(Frame_technitian,font=("arial",30))
Data_input.bind('<Return>',CheckandMove)
Data_input.pack(side='left',fill=tk.X,padx=30)
Data_input.focus()
#Label_technitians=tk.Label(windows,font=("arial",12),text="Technician:")
#Label_technitians.pack(expand=True,fill=tk.X,side=tk.LEFT)


##Spot
Frame_spot=tk.Frame(windows,width=200,height=50)
Frame_spot.pack(fill=tk.BOTH,expand=True)
Label_Spot=tk.Label(Frame_spot,font=("arial",30),text="Spot:")
Label_Spot.pack(side=tk.LEFT,fill=tk.X,padx=10)
Data_Spot=tk.Entry(Frame_spot,font=("arial",30),width=12)
Data_Spot.pack(side=tk.LEFT,fill=tk.X,padx=90)
#Data_Spot.focus()
Data_Spot.bind('<Return>',Spot)


##Type
Frame_CabinetType=tk.Frame(windows,width=200,height=50)
Frame_CabinetType.pack(fill=tk.BOTH,expand=True)
Label_tester=tk.Label(Frame_CabinetType,font=("arial",30),text="Cabinet Type:")
Label_tester.pack(side=tk.LEFT,fill=tk.X,padx=10)
Data_input_name=tk.Entry(Frame_CabinetType,font=("arial",30),width=30)
Data_input_name.pack(side=tk.LEFT,fill=tk.X,padx=10)
#Data_input_name.focus()
Data_input_name.bind('<Return>',focusToCustomer)

##customer
Frame_customer=tk.Frame(windows,width=200,height=50)
Frame_customer.pack(fill=tk.BOTH,expand=True)
Label_tester=tk.Label(Frame_customer,font=("arial",30),text="Customer:")
Label_tester.pack(side=tk.LEFT,fill=tk.X,padx=10)
Data_input_customer=tk.Entry(Frame_customer,font=("arial",30),width=30)
Data_input_customer.pack(side=tk.LEFT,fill=tk.X,padx=45)
Data_input_customer.bind('<Return>',focusToCabinet)


##Cabinet
Frame_cabinet=tk.Frame(windows,width=200,height=50)
Frame_cabinet.pack(fill=tk.BOTH,expand=True)
Label_tester=tk.Label(Frame_cabinet,font=("arial",30),text="Cabinet PN:")
Label_tester.pack(side=tk.LEFT,fill=tk.X,padx=10)
Data_input_cabinet=tk.Entry(Frame_cabinet,font=("arial",30),width=30)
Data_input_cabinet.pack(side=tk.LEFT,fill=tk.X,padx=30)
#Data_input_cabinet.focus()
Data_input_cabinet.bind('<Return>',focusToSN)

##Serial number
Frame_SN=tk.Frame(windows,width=200,height=50)
Frame_SN.pack(fill=tk.BOTH,expand=True)
Label_tester=tk.Label(Frame_SN,font=("arial",30),text="Serial Number:")
Label_tester.pack(side=tk.LEFT,fill=tk.X,padx=10)
Data_input_SerialNumber=tk.Entry(Frame_SN,font=("arial",30),width=30)
Data_input_SerialNumber.pack(side=tk.LEFT,fill=tk.X)
Data_input_SerialNumber.bind('<Return>',Check_cabinet)

##Message
Frame_Message1=tk.Frame(windows,width=200,height=50)
Frame_Message1.pack(fill=tk.BOTH,expand=True)
Label_message=tk.Label(Frame_Message1,font=("arial",24),text="--Escanear credencial del Tecnico--")
Label_message.pack(side=tk.LEFT,fill=tk.X,padx=10)

##Message_2
Frame_Message2=tk.Frame(windows,width=200,height=50)
Frame_Message2.pack(fill=tk.BOTH,expand=True)
Label_message_2=tk.Label(Frame_Message2,font=("arial",24),text="--")
Label_message_2.pack(side=tk.LEFT,fill=tk.X,padx=10)

Frame_button=tk.Frame(windows,width=200,height=50)
Frame_button.pack(fill=tk.BOTH,expand=True)


windows.mainloop()   

