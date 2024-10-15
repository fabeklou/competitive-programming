import sys, threading
def main():
    pass

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()

# https://codeforces.com/gym/532332/problem/C