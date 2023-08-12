#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4.pyc
    
    names = dir(hidden_4.pyc).sort()
    for name in names:
        if not name.startswith("__"):
            print(name)