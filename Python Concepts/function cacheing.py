import time
from functools import lru_cache

@lru_cache(maxsize=3)
def fetch_data(n):
    time.sleep(n)
    return n



if __name__=='__main__':
    print("Fetching data from backend.....")
    fetch_data(2)
    fetch_data(2)
    print("4 seconds ")
    fetch_data(1)
    print("Fetching data complete.")
    print("Fetching again.....")
    fetch_data(5)
    print("Process complete.")
    # finally clause use
    f1 = open("trythis.txt")
    try:
        # f1 = open("trythis.txt")
        f2 = open("mytry.txt")
    except Exception as e:
        print(e)
    else:
        print("this will run only if except dosen't run")
    finally:
        print("Executing finally")
        f1.close()
        print("Files closed..")
