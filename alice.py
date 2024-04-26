import time
import sssr
import random

my_ip = "127.0.0.1"
my_port = 16065
dest_ip = "127.0.0.1"
dest_port = 16066

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
    print("Alice".center(78), end="")
    print("*")
    print("*" + "-" * 78 + "*")

    print("\nGoal - calculate z where z = x + y.  Alice (me) has X, Bob has Y.", flush=True)

    # step 0 - get x
    alice_x = int(input("\nEnter Alice's x value: "))
    time.sleep(sleep_delay)

    # step 1 - generate random r1
    alice_r1 = random.randint(1, random_max)
    print("\n")
    print("(Calculated random r1 : " + str(alice_r1) + ")")
    time.sleep(sleep_delay)

    # step 2 - calculate X0 and X1
    alice_x0 = alice_x - alice_r1
    print("(Calculated x0 = x - r1 : " + str(alice_x0) + ")")
    time.sleep(1)
    alice_x1 = alice_r1
    print("(Calculated x1 = r1 : " + str(alice_x1) + ")")
    time.sleep(sleep_delay)

    # step 3 - send x1 to Bob
    print("\n")
    print("Sending x1 data to Bob... ", end = "", flush = True)
    time.sleep(sleep_delay * 2)
    sssr.send_socket_data(dest_ip, dest_port, alice_x1)
    print("(Sent to Bob x1 : " + str(alice_x1) + ")")
    time.sleep(sleep_delay)

    # ...and obtain y0 from Bob
    print("\n")
    print("Receive y0 data from Bob... ", end = "")
    bob_y0 = sssr.get_socket_data(my_ip, my_port)
    bob_y0 = int(bob_y0)
    print("(Received Bob's y0 : " + str(bob_y0) + ")")
    time.sleep(sleep_delay)

    # step 4 - calculate z0
    alice_z0 = alice_x0 + bob_y0
    print("\nAlice's z0 value (x0 + Bob's y0) is : " + str(alice_z0))
    time.sleep(sleep_delay)

    # step 5 - send z0 to Bob
    print("\n")
    print("Sending z0 data to Bob... ", end = "", flush = True)
    time.sleep(sleep_delay * 2)
    sssr.send_socket_data(dest_ip, dest_port, alice_z0)
    print("(Sent to Bob z0 : " + str(alice_z0) + ")")
    time.sleep(sleep_delay)

    # ...and obtain z1 from Bob
    print("\n")
    print("Receive z1 data from Bob... ", end = "")
    bob_z1 = sssr.get_socket_data(my_ip, my_port)
    bob_z1 = int(bob_z1)
    print("(Received Bob's z1 : " + str(bob_z1) + ")")
    time.sleep(sleep_delay)

    # final step - calculate z
    alice_z = alice_z0 + bob_z1
    print("\nAlice's z value (z0 + z1) is : " + str(alice_z))
    print("(z0 = Alice's x0 + Bob's y0, z1 from Bob)\n")
    time.sleep(sleep_delay)

if __name__ == "__main__":
    run_as_test()