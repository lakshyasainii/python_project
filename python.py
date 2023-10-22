import tkinter as tk
import paho.mqtt.client as mqtt

# Define the MQTT broker settings
broker_address = "broker.hivemq.com"
broker_port = 1883

# Define the functions to send MQTT messages
def send_message(topic, message):
    client.publish(topic, message)

def function1():
    print("Button 1 was pressed!")
    send_message("traffic-light-1", "RED")

def function2():
    print("Button 2 was pressed!")
    send_message("traffic-light-1", "YELLOW")

def function3():
    print("Button 3 was pressed!")
    send_message("traffic-light-1", "GREEN")

def function4():
    print("Button 4 was pressed!")
    send_message("traffic-light-2", "RED")

def function5():
    print("Button 5 was pressed!")
    send_message("traffic-light-2", "YELLOW")

def function6():
    print("Button 6 was pressed!")
    send_message("traffic-light-2", "GREEN")

# Create the main application window
root = tk.Tk()
root.title("Traffic Control")

# Create and configure the buttons with different colors
button1 = tk.Button(root, text="RED", command=function1, bg="red")
button2 = tk.Button(root, text="YELLOW", command=function2, bg="yellow")
button3 = tk.Button(root, text="GREEN", command=function3, bg="green")
button4 = tk.Button(root, text="RED", command=function4, bg="red")
button5 = tk.Button(root, text="YELLOW", command=function5, bg="yellow")
button6 = tk.Button(root, text="GREEN", command=function6, bg="green")

# Use the grid geometry manager to position the buttons
button1.grid(row=3, column=0, columnspan=2, sticky="nsew")
button2.grid(row=4, column=0, columnspan=2, sticky="nsew")
button3.grid(row=5, column=0, columnspan=2, sticky="nsew")
button4.grid(row=8, column=0, columnspan=2, sticky="nsew")
button5.grid(row=9, column=0, columnspan=2, sticky="nsew")
button6.grid(row=10, column=0, columnspan=2, sticky="nsew")

# Add the "Traffic Control" heading
heading_label = tk.Label(root, text="Traffic Control", font=("Helvetica", 24))
heading_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

# Start the MQTT client
client = mqtt.Client()
client.connect(broker_address, broker_port)
client.loop_start()

# Start the main loop
root.mainloop()