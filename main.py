import serial
import keyboard
import time

# 创建一个串口对象
ser = serial.Serial()

# 配置串口参数，这里可以根据你的需求进行配置
ser.port = 'COM2'  # 设置串口的端口号，可以根据实际情况修改
ser.baudrate = 9600  # 波特率
ser.bytesize = serial.EIGHTBITS  # 数据位
ser.parity = serial.PARITY_NONE  # 校验位
ser.stopbits = serial.STOPBITS_ONE  # 停止位

# 打开串口
ser.open()

wsad_sent = False  # 用于跟踪是否已经发送了WSAD字符

try:
    while True:
        # 检测键盘按键
        if keyboard.is_pressed('w') and not wsad_sent:
            data_to_send = 'Forward'
            ser.write(data_to_send.encode('utf-8'))
            wsad_sent = True  # 标记已发送W
        elif keyboard.is_pressed('s') and not wsad_sent:
            data_to_send = 'Back'
            ser.write(data_to_send.encode('utf-8'))
            wsad_sent = True  # 标记已发送S
        elif keyboard.is_pressed('a') and not wsad_sent:
            data_to_send = 'Left'
            ser.write(data_to_send.encode('utf-8'))
            wsad_sent = True  # 标记已发送A
        elif keyboard.is_pressed('d') and not wsad_sent:
            data_to_send = 'Right'
            ser.write(data_to_send.encode('utf-8'))
            wsad_sent = True  # 标记已发送D
        elif keyboard.is_pressed('x') and not wsad_sent:
            data_to_send = 'Stop'
            ser.write(data_to_send.encode('utf-8'))
            wsad_sent = True
        elif not keyboard.is_pressed('w') and not keyboard.is_pressed('s') and not keyboard.is_pressed('a') and not keyboard.is_pressed('d') and not keyboard.is_pressed('x'):
            wsad_sent = False  # 重置标记

        # 模拟从串口接收数据，一次性接收所有可用的数据
        received_data = ser.read(ser.in_waiting)
        if received_data:
            decoded_data = received_data.decode('utf-8')  # 使用适当的字符编码解码数据
            current_time = time.strftime('%H:%M:%S')  # 获取当前时间
            print(f"接收: {decoded_data} 时间: {current_time}")  # 将接收到的数据和时间显示在控制台
except KeyboardInterrupt:
    pass

# 关闭串口
ser.close()
