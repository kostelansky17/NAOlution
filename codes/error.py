def check_errors(errors,fce_name):
    if errors != 0:
        print(fce_name + " returned code " + str(errors))
        return False
    return True   