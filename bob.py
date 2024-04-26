import sssr
import random
import time

my_ip = "127.0.0.1"
my_port = 16066
dest_ip = "127.0.0.1"
dest_port = 16065

# time to sleep between steps
sleep_delay = 1

# random number maximum - can be anything, but small is more readable
random_max = 100

# -----------------------------------------------------------------------------
# Additive Sharing Test
# -----------------------------------------------------------------------------

def run_as_test():
    # heading
    print("\n")
    print("*" + "-" * 78 + "*")
    print("*", end = "")
    print("Bob".center(78), end="")
    print("*")
    print("*" + "-" * 78 + "*")

    print("\nGoal - calculate z where z = x + y.  Alice has X, Bob (me) has Y.", flush=True)

    # step 0 - get x
    bob_y = int(input("\nEnter Bob's y value: "))
    time.sleep(sleep_delay)

    # step 1 - generate random r2
    bob_r2 = random.randint(1, random_max)
    print("\n")
    print("(Calculated random r2 : " + str(bob_r2) + ")")
    time.sleep(sleep_delay)

    # step 2 - calculate y0 and y1
    bob_y0 = bob_y - bob_r2
    print("(Calculated y0 = y - r2 : " + str(bob_y0) + ")")
    time.sleep(1)
    bob_y1 = bob_r2
    print("(Calculated y1 = r2 : " + str(bob_y1) + ")")
    time.sleep(sleep_delay)

    # step 3 - obtain x1 from Alice
    print("\n")
    print("Receive x1 data from Alice... ", end = "", flush = True)
    alice_x1 = sssr.get_socket_data(my_ip, my_port)
    alice_x1 = int(alice_x1)
    print("(Received Alice's x1 : " + str(alice_x1) + ")")
    time.sleep(sleep_delay)

    # ...and send y0 to Alice
    print("\n")
    print("Sending y0 data to Alice... ", end = "")
    time.sleep(sleep_delay * 2)
    sssr.send_socket_data(dest_ip, dest_port, bob_y0)
    print("(Sent to Alice y0 : " + str(bob_y0) + ")")
    time.sleep(sleep_delay)

    # step 4 - calculate z0
    bob_z1 = alice_x1 + bob_y1
    print("\nBob's z1 value (Alice's x1 + y1) is : " + str(bob_z1))
    time.sleep(sleep_delay)

    # step 3 - obtain z0 from Alice
    print("\n")
    print("Receive z0 data from Alice... ", end = "")
    alice_z0 = sssr.get_socket_data(my_ip, my_port)
    alice_z0 = int(alice_z0)
    print("(Received Alice's z0 : " + str(alice_z0) + ")")
    time.sleep(sleep_delay)

    # ...and send z1 to Alice
    print("\n")
    print("Sending z1 data to Alice... ", end = "", flush = True)
    time.sleep(sleep_delay * 2)
    sssr.send_socket_data(dest_ip, dest_port, bob_z1)
    print("(Sent to Alice z1 : " + str(bob_z1) + ")")
    time.sleep(sleep_delay)

    # final step 4 - calculate z
    bob_z = alice_z0 + bob_z1
    print("\nBob's z value (z0 + z1) is : " + str(bob_z))
    print("(z0 from Alice, z1 = Bob's y1 + Alice's x1)\n")
    time.sleep(1)

if __name__ == "__main__":
    #run_test()
    run_as_test()