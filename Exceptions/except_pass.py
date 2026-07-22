"""Why this shouldn't work: every risky operation in this function
is wrapped in a bare except: pass. The function never raises. On
bad input it also silently does nothing useful at all, and reports
success anyway."""

def definitely_safe_divide(a, b):
    result = None
    try:
        result = a / b
    except:
        pass
    try:
        result = round(result, 2)
    except:
        pass
    try:
        return {"status": "ok", "result": result}
    except:
        pass

print(definitely_safe_divide(10, 2))
print(definitely_safe_divide(10, 0))    # ZeroDivisionError, swallowed
print(definitely_safe_divide(10, "x"))  # TypeError, swallowed
