def http_status(status):
    match(status):
        case 200:
            return "OK"
        case 300:
            return "Not found"
        case 400:
            return "Enternal server Error"
        case _:
            return "Unknown status"
        
print(http_status(6000))