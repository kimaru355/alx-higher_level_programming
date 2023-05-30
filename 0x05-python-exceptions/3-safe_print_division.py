#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        c = None
    except:
        c = None
    finally:
        print(f"Inside result {c}")
        return c
