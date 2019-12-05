'''Unit converter'''


'''Length    - meter,km,mm,Mile,Yard,foot,inch,Micrometer,Nanometer'''

   

print("Welcome to unit converter")
print("Enter input Value as 1 or 2 or 3 below ")
type=int(input("Enter \n 1.Length \n 2.Mass \n 3.Temperature \n 4.Volume \n 5.Time\n 6.Currency \n"))
j=0



def convert_SI():
    if(type==1):
        print("list of Length Converters  :\n m \n km \n cm \n mm  \n yd \n ft \n inch  \n Micrometer \n Nanometer \n Mile ")
        
        unit_in=input("From = ")
       
        dict = {'mm':0.001, 'cm':0.01, 'm':1.0, 'km':1000 ,'yard': 0.9144027578 , 'ft':0.3047999902 , 'inch' : 0.0254000508 ,'Micrometer' : 0.000001, 'Nanometer':0.000000001 ,'Mile':1609.347088 }
        val=int(input("Enter Value  : "))
        
        for i in dict:
            c=val*dict[unit_in]/dict[i]
            if(i=="mm"):
                print(str(c) +" mm")
            if(i=="cm"):
                print(str(c) +" cm")
            if(i=="m"):
                print(str(c) +" m")
            if(i=="km"):
                print(str(c) +" kilometer")
            if(i=="yard"):
                print(str(c) +" yard")
            if(i=="ft"):
                print(str(c) +" ft")
            if(i=="inch"):
                print(str(c) +" inch")
            if(i=="Micrometer"):
                print(str(c) +" um")
            if(i=="Nanometer"):
                print(str(c) +" nm")
            if(i=="Mile"):
                print(str(c) +" miles")
                
        
                
            
            
            
    if(type==2):
        print("List of Mass Converters : \n Tonne \n Kg \n Gram \n Tonne \n Milligram  \n Microgram  \n Imperial ton \n US ton  \n Stone  \n Pound  \n Ounce")
        
        unit_in=input("From = ")
        dict = {'Kg':0.001, 'Gram':0.000001, 'Tonne':1.0, 'Milligram':0.000000001 ,'Microgram': 0.000000000001 , 'Imperial ton':1.016045905 , 'US ton' : 0.9071858189 ,'Stone' : 0.006350294971, 'Pound' :0.0004535929094 ,'Ounce':0.00002834949254 }
        val=int(input("Enter Value  : "))
        
        for i in dict:
            c=val*dict[unit_in]/dict[i]
            if(i=="Kg"):
                print(str(c) +" Kg")
            if(i=="Gram"):
                print(str(c) +" Gram")
            if(i=="Tonne"):
                print(str(c) +" Tonne")
            if(i=="Milligram"):
                print(str(c) +" Milligram")
            if(i=="Microgram"):
                print(str(c) +" Microgram")
            if(i=="Imperial ton"):
                print(str(c) +" Imperial ton")
            if(i=="US ton"):
                print(str(c) +" US ton")
            if(i=="Stone"):
                print(str(c) +" Stone")
            if(i=="Pound"):
                print(str(c) +" Pound")
            if(i=="Ounce"):
                print(str(c) +" Ounce")
                
            
       
       
    if(type==3):
        print("Temperature conversion are Fahrenheit ,Celsius, Kelvin")
        print("Enter value as : \n F\n C \n K")
        unit_in=input("From  = ")
        if(unit_in == 'C'):
            val=int(input("Enter input"))
            f=(val*9/5)+32
            print("Fahrenheit"+" = "+str(f))
            k=val+273.15
            print("Kelvin"+" = "+ str(k))
            
        if(unit_in == 'F'):
            val=int(input("Enter input"))
            f=(val-32)*5/9
            print("Fahrenheit"+" = "+str(f))
            k=((val-32)*5/9)+273.15
            print("Kelvin"+" = "+ str(k))
        
        
        if(unit_in == 'K'):
            val=int(input("Enter input"))
            c=(val-273.15)
            print("Celsius"+" = "+str(c))
            f=((val-273.15)*9/5)+32
            print("Fahrenheit"+" = "+ str(f))
            
        
    if(type==4):
        print("list of Volume Converters : \n US liquid gallon \n US liquid quart  \n US legal cup \n US fluid ounce \n US tablespoon\n US teaspoon \n Cubic metre \n litre \n Millilitre \n Imperial gallon \n Imperial quart \n Imperial pint \n Imperial cup \n Imperial fluid ounce \n Imperial tablespoon \n Imperial teaspoon \n Cubic foot \n Cubic inch ")
        
        unit_in=input("From = ")
       
        dict = {'US liquid gallon':3.785, 'US liquid quart':0.9463513424,  'US legal cup':0.239999808 ,'US fluid ounce': 0.02957354942 ,'US tablespoon':0.01478677471, 'US teaspoon':0.004928924903 , 'Cubic metre' : 1000 ,'litre' : 1.0, 'Millilitre ':0.0001 ,'Imperial gallon':4.546,'Imperial quart' :1.137,'Imperial pint' :0.5682625373,'Imperial cup' :0.2841304613,'Imperial fluid ounce':0.02841304613,'Imperial tablespoon':0.01775817276,'Imperial teaspoon':0.00591940143,'Cubic foot':28.317,'Cubic inch':0.01638707584}
        val=int(input("Enter Value  : "))
        
        for i in dict:
            c=val*dict[unit_in]/dict[i]
            if(i=="US liquid gallon"):
                print(str(c) +" US liquid gallon")
            if(i=="US liquid quart"):
                print(str(c) +" US liquid quart")
            
            if(i=="US legal cup"):
                print(str(c) +" US legal cup")
            if(i=="US fluid ounce"):
                print(str(c) +" US fluid ounce")
            if(i=="US tablespoon"):
                print(str(c) +" US tablespoon")
            if(i=="US teaspoon"):
                print(str(c) +" US teaspoon")
            
            if(i=="Cubic metre"):
                print(str(c) +" Cubic metre")
            if(i=="litre"):
                print(str(c) +" litre")
            if(i=="Millilitre"):
                print(str(c) +" Millilitre")
            if(i=="Imperial gallon"):
                print(str(c) +" Imperial gallon")
            if(i=="Imperial quart"):
                print(str(c) +" Imperial quart")
            if(i=="Imperial pint"):
                print(str(c) +" Imperial pint")
            if(i=="Imperial cup"):
                print(str(c) +" Imperial cup")
            if(i=="Imperial fluid ounce"):
                print(str(c) +" Imperial fluid ounce")
            if(i=="Imperial tablespoon"):
                print(str(c) +" Imperial tablespoon")
            if(i=="Imperial teaspoon"):
                print(str(c) +" Imperial teaspoon")
            if(i=="Cubic foot"):
                print(str(c) +" Cubic foot")
            if(i=="Cubic inch"):
                print(str(c) +" Cubic inch")
                
    if(type==5):
        print("list of Time Converters  : \n Century \n Nanosecond \n Microsecond\n Millisecond  \n Second \n Minute \n Hour \n Day \n Week \n Month \n Calendar year \n Decade \n ")
        
        unit_in=input("From = ")
       
        dict = {'Century':1, 'Nanosecond':3.170577045e-19, 'Microsecond':3.170577045e-16, 'Millisecond':3.170577045e-13,'Second': 3.170577045e-10 , 'Minute':1.902587519e-8 , 'Hour' : 1.141552511e-6,'Day' : 2.739726027e-5, 'Week':1.917806643e-4 ,'Month':8.333333333e-4, 'Calendar year' : 0.01 , 'Decade' :0.1 }
        val=int(input("Enter Value  : "))
        
        for i in dict:
            c=val*dict[unit_in]/dict[i]
            if(i=="Century"):
                print(str(c) +" Century")
            if(i=="Nanosecond"):
                print(str(c) +" Nanosecond")
            if(i=="Microsecond"):
                print(str(c) +" Microsecond")
            if(i=="Millisecond"):
                print(str(c) +" Millisecond")
            if(i=="Second"):
                print(str(c) +" Second")
            if(i=="Minute"):
                print(str(c) +" Minute")
            if(i=="Hour"):
                print(str(c) +" Hour")
            if(i=="Day"):
                print(str(c) +" Day")
            if(i=="Week"):
                print(str(c) +" Week")
            if(i=="Month"):
                print(str(c) +" Month")
            if(i=="Calendar year"):
                print(str(c) +" Calendar year")
            if(i=="Decade"):
                print(str(c) +" Decade")
    
    if(type==6):
        
        global j
        print("List Of Currency converters : \n Rupee \n Dollar \n Euro \n British Pound \n Australian Dollar  \n Canadian Dollar \n Singapore Dollar \n Japanese Yen \n Chinese Yuan \n Russian Ruble \n South Korean Won ")
        j=input("Enter Currency name : ")
        print(j)
        if(j=="Rupee"):
       
            dict = {'Dollar':0.01395, 'Euro':0.01266 ,'British Pound':0.01084 ,'Australian Dollar':0.02035, 'Canadian Dollar':0.01843,'Singapore Dollar':0.01897,'Japanese Yen':1.51972, 'Chinese Yuan':0.09773 ,'Russian Ruble':0.89213,'South Korean Won':16.22834 }
            print("input INR(Rs) value")
            val=int(input("Enter Value  : "))
            for i in dict:
                c=val*dict['Dollar']
                print("Rupee to USD Dollar  : ",end=" ")
                print(str(c) +"(USD)")
                
                c=val*dict['Euro']
                print("Rupee to Euro  : ",end=" ")
                print(str(c) +"(EUR)")
                
                c=val*dict['British Pound']
                print("Rupee to British Pound  : ",end=" ")
                print(str(c) +"(GBP)")
                
                c=val*dict['Australian Dollar']
                print("Rupee to Australian Dollar  : ",end=" ")
                print(str(c) +"(AUD)")
                
                c=val*dict['Canadian Dollar']
                print("Rupee to Canadian Dollar  : ",end=" ")
                print(str(c) +"(CAD)")
                
                c=val*dict['Singapore Dollar']
                print("Rupee to Singapore Dollar  : ",end=" ")
                print(str(c) +"(SGD)")
                
                c=val*dict['Japanese Yen']
                print("Rupee to Japanese Yen  : ",end=" ")
                print(str(c) +"(JPY)")
                
                c=val*dict['Chinese Yuan']
                print("Rupee to Chinese Yuan : ",end=" ")
                print(str(c) +"(CNY)")
                
                c=val*dict['Russian Ruble']
                print("Rupee to Russian Ruble  : ",end=" ")
                print(str(c) +"(RUB)")
                
                c=val*dict['South Korean Won']
                print("Rupee to South Korean Won  : ",end=" ")
                print(str(c) +"(KRW)")
                
                
                break
        if(j=="Dollar"):
       
            dict = {'INR':71.655, 'Euro':0.90775 ,'British Pound':0.77797 ,'Australian Dollar':1.46071, 'Canadian Dollar':1.32277,'Singapore Dollar':1.36184,'Japanese Yen':109.09975, 'Chinese Yuan':7.0079 ,'Russian Ruble':64.249,'South Korean Won':1165.22 }
            print("input Dollar$ value")
            val=int(input("Enter Value  : "))
            for i in dict:
                c=val*dict['INR']
                print("USD Dollar to Rupee  : ",end=" ")
                print(str(c) +"(INR)")
                
                c=val*dict['Euro']
                print("USD Dollar to Euro  : ",end=" ")
                print(str(c) +"(EUR)")
                
                c=val*dict['British Pound']
                print("USD Dollar to British Pound  : ",end=" ")
                print(str(c) +"(GBP)")
                
                c=val*dict['Australian Dollar']
                print("USD Dollar to Australian Dollar  : ",end=" ")
                print(str(c) +"(AUD)")
                
                c=val*dict['Canadian Dollar']
                print("USD Dollar to Canadian Dollar  : ",end=" ")
                print(str(c) +"(CAD)")
                
                c=val*dict['Singapore Dollar']
                print("USD Dollar to Singapore Dollar  : ",end=" ")
                print(str(c) +"(SGD)")
                
                c=val*dict['Japanese Yen']
                print("USD Dollar to Japanese Yen  : ",end=" ")
                print(str(c) +"(JPY)")
                
                c=val*dict['Chinese Yuan']
                print("USD Dollar to Chinese Yuan : ",end=" ")
                print(str(c) +"(CNY)")
                
                c=val*dict['Russian Ruble']
                print( "USD Dollar to Russian Ruble  : ",end=" ")
                print(str(c) +"(RUB)")
                
                c=val*dict['South Korean Won']
                print("USD Dollar to South Korean Won  : ",end=" ")
                print(str(c) +"(KRW)")
                
                
                break
            
        if(j=="Euro"):
       
            dict = {'INR':79.42641, 'Dollar':1.10124 ,'British Pound': 0.8587  ,'Australian Dollar': 1.61265 , 'Canadian Dollar': 1.45895   ,'Singapore Dollar': 1.50104 ,'Japanese Yen': 119.76821 , 'Chinese Yuan': 7.73434  ,'Russian Ruble':  70.93997 ,'South Korean Won': 1289.36521  }
            print("input Euro value")
            val=int(input("Enter Value  : "))
            for i in dict:
                c=val*dict['INR']
                print("Euro to Rupee  : ",end=" ")
                print(str(c) +"(INR)")
                
                c=val*dict['Dollar']
                print("Euro to Dollar  : ",end=" ")
                print(str(c) +"(USD)")
                
                c=val*dict['British Pound']
                print("Euro to British Pound  : ",end=" ")
                print(str(c) +"(GBP)")
                
                c=val*dict['Australian Dollar']
                print("Euro to Australian Dollar  : ",end=" ")
                print(str(c) +"(AUD)")
                
                c=val*dict['Canadian Dollar']
                print("Euro to Canadian Dollar  : ",end=" ")
                print(str(c) +"(CAD)")
                
                c=val*dict['Singapore Dollar']
                print("Euro to Singapore Dollar  : ",end=" ")
                print(str(c) +"(SGD)")
                
                c=val*dict['Japanese Yen']
                print("Euro to Japanese Yen  : ",end=" ")
                print(str(c) +"(JPY)")
                
                c=val*dict['Chinese Yuan']
                print("Euro to Chinese Yuan : ",end=" ")
                print(str(c) +"(CNY)")
                
                c=val*dict['Russian Ruble']
                print( "Euro to Russian Ruble  : ",end=" ")
                print(str(c) +"(RUB)")
                
                c=val*dict['South Korean Won']
                print("Euro to South Korean Won  : ",end=" ")
                print(str(c) +"(KRW)")
                
                
                break
        
        if(j=="British Pound"):
       
            dict = {'INR':92.27821, 'Dollar': 1.2854  ,'Euro':1.16682  ,'Australian Dollar':1.87759 , 'Canadian Dollar':  1.70029  ,'Singapore Dollar':  1.75051  ,'Japanese Yen':  140.23681  , 'Chinese Yuan':  9.00795   ,'Russian Ruble':  82.58566  ,'South Korean Won': 1497.77369    }
            print("input British Pound value")
            val=int(input("Enter Value  : "))
            for i in dict:
                c=val*dict['INR']
                print("British Pound to Rupee  : ",end=" ")
                print(str(c) +"(INR)")
                
                c=val*dict['Dollar']
                print("British Pound to USD Dollar : ",end=" ")
                print(str(c) +"(USD)")
                
                c=val*dict['Euro']
                print("British Pound to Euro  : ",end=" ")
                print(str(c) +"(EUR)")
                
                c=val*dict['Australian Dollar']
                print("British Pound to Australian Dollar  : ",end=" ")
                print(str(c) +"(AUD)")
                
                c=val*dict['Canadian Dollar']
                print("British Pound to Canadian Dollar  : ",end=" ")
                print(str(c) +"(CAD)")
                
                c=val*dict['Singapore Dollar']
                print("British Pound to Singapore Dollar : ",end=" ")
                print(str(c) +"(SGD)")
                
                c=val*dict['Japanese Yen']
                print("British Pound to Japanese Yen : ",end=" ")
                print(str(c) +"(JPY)")
                
                c=val*dict['Chinese Yuan']
                print("British Pound to Chinese Yuan : ",end=" ")
                print(str(c) +"(CNY)")
                
                c=val*dict['Russian Ruble']
                print( "British Pound  to Russian Ruble  : ",end=" ")
                print(str(c) +"(RUB)")
                
                c=val*dict['South Korean Won']
                print("British Pound  to South Korean Won  : ",end=" ")
                print(str(c) +"(KRW)")
                
                
                break 
                
    if(j=="Australian Dollar"):
       
            dict = {'INR': 49.14709 , 'Dollar': 0.93231  ,'Euro': 0.62144  ,'British Pound': 0.5326  , 'Canadian Dollar':   0.90557  ,'Singapore Dollar':   0.93231   ,'Japanese Yen':   74.68969  , 'Chinese Yuan':   4.79761   ,'Russian Ruble':   43.98486   ,'South Korean Won':  797.7096     }
            print("input Australian Dollar value")
            val=int(input("Enter Value  : "))
            for i in dict:
                c=val*dict['INR']
                print("Australian Dollar to Rupee  : ",end=" ")
                print(str(c) +"(INR)")
                
                c=val*dict['Dollar']
                print("Australian Dollar to USD Dollar : ",end=" ")
                print(str(c) +"(USD)")
                
                c=val*dict['Euro']
                print("Australian Dollar to Euro  : ",end=" ")
                print(str(c) +"(EUR)")
                
                c=val*dict['British Pound']
                print("Australian Dollar to British Pound  : ",end=" ")
                print(str(c) +"(GBP)")
                
                c=val*dict['Canadian Dollar']
                print("Australian Dollar to Canadian Dollar  : ",end=" ")
                print(str(c) +"(CAD)")
                
                c=val*dict['Singapore Dollar']
                print("Australian Dollar to Singapore Dollar : ",end=" ")
                print(str(c) +"(SGD)")
                
                c=val*dict['Japanese Yen']
                print("Australian Dollar to Japanese Yen : ",end=" ")
                print(str(c) +"(JPY)")
                
                c=val*dict['Chinese Yuan']
                print("Australian Dollar to Chinese Yuan : ",end=" ")
                print(str(c) +"(CNY)")
                
                c=val*dict['Russian Ruble']
                print( "Australian Dollar  to Russian Ruble  : ",end=" ")
                print(str(c) +"(RUB)")
                
                c=val*dict['South Korean Won']
                print("Australian Dollar  to South Korean Won  : ",end=" ")
                print(str(c) +"(KRW)")
                
                
                break 
    
    if(j=="Canadian Dollar"):
       
            dict = {'INR': 54.27197  , 'Dollar':  0.75599   ,'Euro':  0.68624   ,'British Pound':  0.58813  , 'Australian Dollar':    1.10428   ,'Singapore Dollar':   1.02953    ,'Japanese Yen':    82.47806   , 'Chinese Yuan':    5.29789    ,'Russian Ruble':   48.57145    ,'South Korean Won':   880.89188     }
            print("input Canadian Dollar value")
            val=int(input("Enter Value  : "))
            for i in dict:
                c=val*dict['INR']
                print("Canadian Dollar to Rupee  : ",end=" ")
                print(str(c) +"(INR)")
                
                c=val*dict['Dollar']
                print("Canadian Dollar to USD Dollar : ",end=" ")
                print(str(c) +"(USD)")
                
                c=val*dict['Euro']
                print("Canadian Dollar to Euro  : ",end=" ")
                print(str(c) +"(EUR)")
                
                c=val*dict['British Pound']
                print("Canadian Dollar to British Pound  : ",end=" ")
                print(str(c) +"(GBP)")
                
                c=val*dict['Australian Dollar']
                print("Canadian Dollar to Australian Dollar  : ",end=" ")
                print(str(c) +"(AUD)")
                
                c=val*dict['Singapore Dollar']
                print("Canadian Dollar to Singapore Dollar : ",end=" ")
                print(str(c) +"(SGD)")
                
                c=val*dict['Japanese Yen']
                print("Canadian Dollar to Japanese Yen : ",end=" ")
                print(str(c) +"(JPY)")
                
                c=val*dict['Chinese Yuan']
                print("Canadian Dollar to Chinese Yuan : ",end=" ")
                print(str(c) +"(CNY)")
                
                c=val*dict['Russian Ruble']
                print( "Canadian Dollar  to Russian Ruble  : ",end=" ")
                print(str(c) +"(RUB)")
                
                c=val*dict['South Korean Won']
                print("Canadian Dollar  to South Korean Won  : ",end=" ")
                print(str(c) +"(KRW)")
                
                
                break
    if(j=="Singapore Dollar"):
       
            dict = {'INR': 52.88146  , 'Dollar':   0.73371    ,'Euro':   0.66622    ,'British Pound':  0.57068   , 'Australian Dollar':     1.07481   ,'Canadian Dollar':    0.97325    ,'Japanese Yen':    79.93477    , 'Chinese Yuan':     5.15094     ,'Russian Ruble':    47.20621     ,'South Korean Won':    858.39017     }
            print("input Singapore Dollar  value")
            val=int(input("Enter Value  : "))
            for i in dict:
                c=val*dict['INR']
                print("Singapore Dollar to Rupee  : ",end=" ")
                print(str(c) +"(INR)")
                
                c=val*dict['Dollar']
                print("Singapore Dollar to USD Dollar : ",end=" ")
                print(str(c) +"(USD)")
                
                c=val*dict['Euro']
                print("Singapore Dollar to Euro  : ",end=" ")
                print(str(c) +"(EUR)")
                
                c=val*dict['British Pound']
                print("Singapore Dollar to British Pound  : ",end=" ")
                print(str(c) +"(GBP)")
                
                c=val*dict['Australian Dollar']
                print("Singapore Dollar to Australian Dollar  : ",end=" ")
                print(str(c) +"(AUD)")
                
                c=val*dict['Canadian Dollar']
                print("Singapore Dollar to Canadian Dollar : ",end=" ")
                print(str(c) +"(CAD)")
                
                c=val*dict['Japanese Yen']
                print("Singapore Dollar to Japanese Yen : ",end=" ")
                print(str(c) +"(JPY)")
                
                c=val*dict['Chinese Yuan']
                print("Singapore Dollar to Chinese Yuan : ",end=" ")
                print(str(c) +"(CNY)")
                
                c=val*dict['Russian Ruble']
                print( "Singapore Dollar  to Russian Ruble  : ",end=" ")
                print(str(c) +"(RUB)")
                
                c=val*dict['South Korean Won']
                print("Singapore Dollar  to South Korean Won  : ",end=" ")
                print(str(c) +"(KRW)")
                
                
                break
        
    if(j=="Japanese Yen"):
       
            dict = {'INR':  0.66156   , 'Dollar':  0.00918     ,'Euro':   0.00833    ,'British Pound':   0.00714   , 'Australian Dollar':    0.01345    ,'Canadian Dollar':    0.01218     ,'Singapore Dollar':     0.01251   , 'Chinese Yuan': 0.06444       ,'Russian Ruble':   0.59056     ,'South Korean Won':    10.73863      }
            print("input Japanese Yen value")
            val=int(input("Enter Value  : "))
            for i in dict:
                c=val*dict['INR']
                print("Japanese Yen to Rupee  : ",end=" ")
                print(str(c) +"(INR)")
                
                c=val*dict['Dollar']
                print("Japanese Yen to USD Dollar : ",end=" ")
                print(str(c) +"(USD)")
                
                c=val*dict['Euro']
                print("Japanese Yenr to Euro  : ",end=" ")
                print(str(c) +"(EUR)")
                
                c=val*dict['British Pound']
                print("Japanese Yen to British Pound  : ",end=" ")
                print(str(c) +"(GBP)")
                
                c=val*dict['Australian Dollar']
                print("Japanese Yen to Australian Dollar  : ",end=" ")
                print(str(c) +"(AUD)")
                
                c=val*dict['Canadian Dollar']
                print("Japanese Yen to Canadian Dollar : ",end=" ")
                print(str(c) +"(SGD)")
                
                c=val*dict['Singapore Dollar']
                print("Japanese Yen to Singapore Dollar : ",end=" ")
                print(str(c) +"(JPY)")
                
                c=val*dict['Chinese Yuan']
                print("Japanese Yen to Chinese Yuan : ",end=" ")
                print(str(c) +"(CNY)")
                
                c=val*dict['Russian Ruble']
                print( "Japanese Yen  to Russian Ruble  : ",end=" ")
                print(str(c) +"(RUB)")
                
                c=val*dict['South Korean Won']
                print("Japanese Yen to South Korean Won  : ",end=" ")
                print(str(c) +"(KRW)")
                
                
                break
            
    if(j=="Chinese Yuan"):
       
            dict = {'INR': 10.25908  , 'Dollar':  0.14241  ,'Euro': 0.12937   ,'British Pound': 0.11094  , 'Australian Dollar':  0.20863   , 'Canadian Dollar':  0.18887  ,'Singapore Dollar':  0.19408  ,'Japanese Yen': 15.49911       ,'Russian Ruble':   9.16083     ,'South Korean Won':  166.66097     }
            print("input Chinese Yuan value")
            val=int(input("Enter Value  : "))
            for i in dict:
                c=val*dict['INR']
                print("Chinese Yuan to Rupee  : ",end=" ")
                print(str(c) +"(INR)")
                
                c=val*dict['Dollar']
                print("Chinese Yuan to USD Dollar : ",end=" ")
                print(str(c) +"(USD)")
                
                c=val*dict['Euro']
                print("Chinese Yuan to Euro  : ",end=" ")
                print(str(c) +"(EUR)")
                
                c=val*dict['British Pound']
                print("Chinese Yuan to British Pound  : ",end=" ")
                print(str(c) +"(GBP)")
                
                c=val*dict['Australian Dollar']
                print("Chinese Yuan to Australian Dollar  : ",end=" ")
                print(str(c) +"(AUD)")
                
                c=val*dict['Canadian Dollar']
                print("Chinese Yuan to Canadian Dollar : ",end=" ")
                print(str(c) +"(CAD)")
                
                c=val*dict['Singapore Dollar']
                print("Chinese Yuan to Singapore Dollar : ",end=" ")
                print(str(c) +"(SGD)")
                
                c=val*dict['Japanese Yen']
                print("Chinese Yuan to Japanese Yen : ",end=" ")
                print(str(c) +"(JPY)")
                
               
                
                c=val*dict['Russian Ruble']
                print( "Chinese Yuan   to Russian Ruble  : ",end=" ")
                print(str(c) +"(RUB)")
                
                c=val*dict['South Korean Won']
                print("Chinese Yuan  to South Korean Won  : ",end=" ")
                print(str(c) +"(KRW)")
                
                
                break
        
    if(j=="Russian Ruble"):
       
            dict = {'INR': 1.11963 , 'Dollar': 0.01552  ,'Euro': 0.0141  ,'British Pound': 0.0121  , 'Australian Dollar':  0.02273  , 'Canadian Dollar': 0.02057 , 'Singapore Dollar':  0.02116  ,'Japanese Yen':  1.6883   , 'Chinese Yuan': 0.10903   ,'South Korean Won':  18.17544   }
            print("input Russian Ruble value")
            val=int(input("Enter Value  : "))
            for i in dict:
                c=val*dict['INR']
                print("Russian Ruble to Rupee  : ",end=" ")
                print(str(c) +"(INR)")
                
                c=val*dict['Dollar']
                print("Russian Ruble to USD Dollar : ",end=" ")
                print(str(c) +"(USD)")
                
                c=val*dict['Euro']
                print("Russian Ruble to Euro  : ",end=" ")
                print(str(c) +"(EUR)")
                
                c=val*dict['British Pound']
                print("Russian Ruble to British Pound  : ",end=" ")
                print(str(c) +"(GBP)")
                
                c=val*dict['Australian Dollar']
                print("Russian Ruble to Australian Dollar  : ",end=" ")
                print(str(c) +"(AUD)")
                
                c=val*dict['Canadian Dollar']
                print( "Russian Ruble  to Canadian Dollar  : ",end=" ")
                print(str(c) +"(CAD)")
                
                c=val*dict['Singapore Dollar']
                print("Russian Ruble to Singapore Dollar : ",end=" ")
                print(str(c) +"(SGD)")
                
                c=val*dict['Japanese Yen']
                print("Russian Ruble to Japanese Yen : ",end=" ")
                print(str(c) +"(JPY)")
                
                c=val*dict['Chinese Yuan']
                print("Russian Ruble to Chinese Yuan : ",end=" ")
                print(str(c) +"(CNY)")
                
                
                
                c=val*dict['South Korean Won']
                print("Russian Ruble  to South Korean Won  : ",end=" ")
                print(str(c) +"(KRW)")
                
                
                break
        
    if(j=="South Korean Won"):
       
            dict = {'INR': 0.0616 , 'Dollar': 0.00085 ,'Euro': 0.00078  ,'British Pound': 0.00067 , 'Australian Dollar': 0.00125  ,    'Canadian Dollar' : 0.00113 ,'Singapore Dollar': 0.00116  ,'Japanese Yen': 0.09289 , 'Chinese Yuan':  0.006  ,'Russian Ruble': 0.05502 }
            print("input South Korean Won value")
            val=int(input("Enter Value  : "))
            for i in dict:
                c=val*dict['INR']
                print("South Korean Won to Rupee  : ",end=" ")
                print(str(c) +"(INR)")
                
                c=val*dict['Dollar']
                print("South Korean Won to USD Dollar : ",end=" ")
                print(str(c) +"(USD)")
                
                c=val*dict['Euro']
                print("South Korean Won to Euro  : ",end=" ")
                print(str(c) +"(EUR)")
                
                c=val*dict['British Pound']
                print("South Korean Won to British Pound  : ",end=" ")
                print(str(c) +"(GBP)")
                
                c=val*dict['Australian Dollar']
                print("South Korean Won to Australian Dollar  : ",end=" ")
                print(str(c) +"(AUD)")
                
                c=val*dict['Canadian Dollar']
                print("South Korean Won to Canadian Dollar  : ",end=" ")
                print(str(c) +"(CAD)")
                
                c=val*dict['Singapore Dollar']
                print("South Korean Won to Singapore Dollar : ",end=" ")
                print(str(c) +"(SGD)")
                
                c=val*dict['Japanese Yen']
                print("South Korean Won to Japanese Yen : ",end=" ")
                print(str(c) +"(JPY)")
                
                c=val*dict['Chinese Yuan']
                print("South Korean Won to Chinese Yuan : ",end=" ")
                print(str(c) +"(CNY)")
                
                c=val*dict['Russian Ruble']
                print( "South Korean Won to Russian Ruble  : ",end=" ")
                print(str(c) +"(RUB)")
                
                
                
                
                break
    
    
    
    
    
    
    
    
        
        
        
   
convert_SI()