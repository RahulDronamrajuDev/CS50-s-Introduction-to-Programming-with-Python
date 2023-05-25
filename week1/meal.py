def main():
    time=input("What time is it? ")
    is_pm=time.endswith("pm")
    time=time.replace("a.m","").replace("p.m","").strip()

    new_time=convert(time)
    if is_pm and new_time<12:
        new_time+=12
    if  7<= new_time <=8:
        print("breakfast time")
    elif 12<= new_time <=13:
        print("lunch time")
    elif 18<= new_time <=19:
        print("dinner time")








def convert(time):
    hours, minutes=time.split(":")
    hours=float(hours)
    minutes=float(minutes)/60
    new_time=float(hours+minutes)
    return new_time



if __name__ == "__main__":
    main()
