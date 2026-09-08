def Check_Cpu_Print(usage):
    if usage > 80:
        print(f"alert! temp is high {usage}")
    else:
        print(f"good! temp is normal {usage}")

def  Check_Cpu_return(usage):
    if usage > 80:
        return f"alert! temp is high {usage}"
    else:
        return f"good! temp is normal {usage}"


res1 = Check_Cpu_Print(85)
print (f"value of res1: {res1}")

res2 = Check_Cpu_return(85)
print (f"value of res2: {res2} ")