
import serial
import time
import threading
import pytool


class SerialPort:
    message = ''

    def __init__(self, port, buand):
        super(SerialPort, self).__init__()
        self.port = serial.Serial(port, buand)
        self.port.close()
        if not self.port.isOpen():
            self.port.open()

    def port_open(self):
        if not self.port.isOpen():
            self.port.open()

    def port_close(self):
        self.port.close()

    def send_data(self):
        data = input(u"请输入要发送的数据（非中文）并同时接收数据: ")
        n = self.port.write((data + '\n').encode())
        return n

    def read_data(self):
        while True:
            # self.message = self.port.readline()
            # self.message = self.port.read(1024)
            self.message = self.port.read_all()

            # pytool.radar_display(self.message, dtype=None, SOF=None, EOF=None)
            pytool.display_mtd(self.message, dtype=None, SOF=None, EOF=None)
            # print(self.message)
            print(len(self.message))


if __name__ == '__main__':

    serialPort = "COM7"  # 串口
    baudRate = 1050000  # 波特率
    mSerial = SerialPort(serialPort, baudRate)
    t1 = threading.Thread(target=mSerial.read_data)

    t1.start()
    while True:
        time.sleep(1)
        # mSerial.send_data()
    mSerial.port_close()
