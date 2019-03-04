def convert_ms(n):
    seconds = round(n/1000)
    minutes = round(seconds/60)
    hours = round(minutes/60)
    print("{}:{}:{}".format(hours,minutes,seconds))
    
convert_ms(int(input()))
