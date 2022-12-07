import os
import pandas as pd
import csv
import sys

def check_if_exist():
    if os.path.isfile('data.csv') == False:
        starting_data = []
        df = pd.DataFrame(starting_data, columns = ['folder', 'file', 'path', 'data'])
        df.to_csv("data.csv", index = False)

check_if_exist()

def main():

    folders = []
    files = []

    path = "root/"

    print("Hello. Welcome to the data logger.")
    print("If you want information on the commands you can use, please read the commands.txt file.")

    command_input = input(f"Hello. you are at: {path}: ")
    while True:

        cmd_input_list = command_input.split(" ")
        command = cmd_input_list[0]

        if command == 'mkdata':
            folder = cmd_input_list[1]
            file = cmd_input_list[2]
            folders.append(folder)
            files.append(file)
            path_ = path+folder+'/'+file+'.txt'
            path = path+folder+'/'

            data = input("Please enter the data you want to store: ")

            data_sect = [folder, file, path_, data]

            with open('data.csv', 'a') as f:

                writer = csv.writer(f)

                writer.writerow(data_sect)

        elif command == 'getdata':
            arg_path = path+cmd_input_list[1]
            data_lines = []
            with open("data.csv","r") as f:
                for i in f:
                    boom = i.strip().split(",")
                    data_lines.append(boom)
                data_lines.pop(0)
                paths = []
                for i in data_lines:
                    paths.append(i[2])
                for i in paths:
                    if arg_path == i:
                        for j in data_lines:
                            if arg_path == j[2]:
                                data_thing = j[3]
                                print(data_thing)
                                break
        
        elif command == "home":
            path = "root/"
        elif command == "wipe":
            descision = input("WIPE ALL DATA? [Y/N]: ")
            if descision.lower() == "y":
                print("Killing file...")
                data_sect = ["folder","file","path","data"]
                with open("data.csv", "w") as f:
                    f.close()
                with open("data.csv", "w") as f:
                    writer = csv.writer(f)

                    writer.writerow(data_sect)
                    
            elif descision.lower() == "n":
                print("Returning to root...")
                path = "root/"
        
        elif command == "exit":
            print("Exiting program.")
            sys.exit()
        elif command == "list":
            data_lines = []
            print("Listing all data paths...")
            with open("data.csv","r") as f:
                for i in f:
                    boom = i.strip().split(",")
                    data_lines.append(boom)
                data_lines.pop(0)
                paths = []
                for i in data_lines:
                    paths.append(i[2])
                for i in paths:
                    print(f"\n{i}")
        else:
            print(f"command '{command}' does not exist.")

        command_input = input(f"Hello. you are at {path}: ")
                
main()