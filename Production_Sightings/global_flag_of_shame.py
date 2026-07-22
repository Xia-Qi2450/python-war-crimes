"""ANONYMIZED SIGHTING #2
Reported location: an internal admin dashboard, still running five
years after the intern who wrote it left the company."""

# global flag of shame -- controls whether the entire app is "in maintenance"
# nobody remembers who sets this to True, only that something breaks if you touch it
IS_BROKEN_DO_NOT_TOUCH = False

def handle_request(path):
    global IS_BROKEN_DO_NOT_TOUCH
    if path == "/admin/reset-everything":
        IS_BROKEN_DO_NOT_TOUCH = True  # nobody knows why this line exists
    if IS_BROKEN_DO_NOT_TOUCH:
        return "503: the flag is true, ask no further questions"
    return "200: OK"

print(handle_request("/home"))
print(handle_request("/admin/reset-everything"))
print(handle_request("/home"))  # now broken, forever, until restart
