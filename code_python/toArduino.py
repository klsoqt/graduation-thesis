# Importing Libraries
import serial
import time
ser = serial.Serial(port='COM4', baudrate=9600)

def write_read(data):
    try:
        while True:
            if (ser.in_waiting > 0):
                data1 = ser.readline()
                data2 = data1.decode()
                recei_data = data2.rstrip()
                # print(recei_data)
                if recei_data == "done":
                    print("Robot đã thực hiện nước đi!")
                    print("==============================")
                    break
                time.sleep(1)
            else:
                # send_data = "AABBF"
                data_Python = str(data) + '\r'
                ser.write(data_Python.encode())
    except KeyboardInterrupt:
        ser.close()
