def f(x):
    x=(x**3+8)
    return x

def main():
    x=9
    x=f(x)    
    print(x)
    
    if x>27:
        print("Yay!")
        
if __name__ == "__main__":
    main()