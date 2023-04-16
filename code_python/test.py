# # Importing Libraries
# import serial
# import time
# arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
# res = "AA CD False"
# def write_read(data):
#     arduino.write(bytes(data, 'utf-8'))
#     time.sleep(0.5)
#     data = arduino.readline()
#     return data
#
# for i in range(0, 3):
#     data1 = write_read(res)
#     print(data1)
#
#
for val in "quantrimang":
    if val == "m":
        if True:
            break

    else:
        print(val)

print("Kết thúc!")