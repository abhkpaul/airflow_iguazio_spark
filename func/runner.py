from modules import jobA

if __name__ == '__main__':
    print("This runs before the spark context!")
    
    jobA.main()

    print("This runs after the job call")