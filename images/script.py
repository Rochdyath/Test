import sys

def requirement_c():
    try:
        with open("Makefile", 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def requirement_python():
    try:
        with open("requirements.txt", 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def requirement_javascript():
    try:
        with open("package.json", 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def requirement_java():
    try:
        with open("app/pom.xml", 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def requirement_befunge():
    try:
        with open("app/main.bf", 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def check_requirement():
    mylst = []
    if requirement_c() == True:
        mylst.append("c")
    if requirement_python() == True:
        mylst.append("python")
    if requirement_javascript() == True:
        mylst.append("javascript")
    if requirement_java() == True:
        mylst.append("java")
    if requirement_befunge() == True:
        mylst.append("befunge")

    if len(mylst) == 0 or len(mylst) > 1:
        return "Error"
    else:
        return mylst[0]

check_requirement()
