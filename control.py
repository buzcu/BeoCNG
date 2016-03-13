import os


def main():

    alive = open("alive.txt","w+")
    server_array = []
    server_array = [
        "10.144.22.81",
        "10.144.22.51",
        "10.144.22.52"
        "10.144.22.66"
        "10.144.22.59"
    ]

    #response 0 is online, else is offline

    for server in server_array:
        response = os.system("ping -c 1 " + server)
        if not response:
            alive.write(server+"\n")
        else:
            alive.write("#"+server+"\n")

    alive.close()

if __name__ == '__main__':
    main()