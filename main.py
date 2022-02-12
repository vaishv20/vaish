celsius = int(input("enter temperature in celsius"))
farenheit = (celsius*1.8) + 32
print("%0.1f degrees celcius is = %0.1f farenheit" %(celsius,farenheit))
if (farenheit>= 104) :
    print("the temperatre is too hot")
elif (farenheit<= 50):
    print("the temperature is cold")
else :
    print("the temperature is nice")