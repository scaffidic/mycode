#!/usr/bin/env python3

"""Working with lists in Python"""

def main():

    
    # Create a list
    my_list = [ "192.168.0.5", 5060, "UP" ]


    # access index 0 (first item)
    print("The first item in the list (IP): " + my_list[0] )


    # access index 1
    print("The second item in the list (port): " + str(my_list[1]) )


    # access index 2
    print("The last item in the list (state): " + my_list[2] )


    # create an IP list
    iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]


    # print only the IP addresses
    print(f"IP addresses: {iplist[3]} and {iplist[4]}")

if __name__ == "__main__":
    main()
