import re
import random

#------------------------------------ Roll full
def rollf(rolling):
    try:
        string = " "
        dices = re.split(r'\s*[+-]\s*', rolling) 
        num = 0
        operation = []
        result = 0
        count = 0
        #------------------------------------ Operations verifications

        for item in rolling:

            if item == "+" or item == "-":    
                operation.append(item)
        
        #------------------------------------ Random functions
        for item in dices:
            
            if count <= len(operation): 

                #Positive
                if count== 0 or operation[count-1] == "+":
                    
                    dice = re.split(r'\s*[dD]\s*', item)
                    
                    if "D" in item or "d" in item:
                        
                        if dice[0]=="":
                            value= random.randint(1, int(dice[1]))
                            
                            string += ("( " + str(value) + " )")
                            result+=value

                        else:
                            for i in range (int(dice[0])):
                                value= random.randint(1, int(dice[1]))
                                
                                if i==0:
                                    string+= "( " + str(value)
                                    
                                else:
                                    string+=" + " + str(value) + " "
                                    
                                num+=value
                            string+=")"
                            result+=num
                    else:
                        string += ("( " + item + " )")
                        
                        result += int(item)
            
                #Negative
                elif count!= 0 and operation[count-1]=="-":                

                    dice = re.split(r'\s*[dD]\s*', item)
                    
                    if "D" in item or "d" in item:
                        
                        if dice[0]=="":
                            value= random.randint(1, int(dice[1]))
                            
                            string += ("( " + str(value) + " )")
                            result-=value

                        else:
                            for i in range (int(dice[0])):
                                value= random.randint(1, int(dice[1]))
                                
                                if i==0:
                                    string+= "( " + str(value)
                                    
                                else:
                                    string+=" + " + str(value) + " "
                                    
                                num+=value
                            string+=")"
                            result-=num
                    else:
                        string += ("( " + item + " )")
                        
                        result -= int(item)  
                
                if count < len(operation):
                    string +=" " + operation[count] + " "    
                    
                    count += 1        
            
            num=0
        string += " = " + str(result)
        return string, result
    except:
        print("Input Error: Data needs to be in string format and structured like 1d5 + 2d5 - 5")


#------------------------------------ Roll normal (just 1 return)
def roll(rolling):
    try:
        string = " "
        dices = re.split(r'\s*[+-]\s*', rolling) 
        num = 0
        operation = []
        result = 0
        count = 0
        #------------------------------------ Operations verifications

        for item in rolling:

            if item == "+" or item == "-":    
                operation.append(item)

        #------------------------------------ Random function
        for item in dices:
            
            if count <= len(operation): 

                if count== 0 or operation[count-1] == "+":
                    
                    dice = re.split(r'\s*[dD]\s*', item)
                    
                    if "D" in item or "d" in item:
                        
                        if dice[0]=="":
                            value= random.randint(1, int(dice[1]))
                            
                            string += ("( " + str(value) + " )")
                            result+=value

                        else:
                            for i in range (int(dice[0])):
                                value= random.randint(1, int(dice[1]))
                                
                                if i==0:
                                    string+= "( " + str(value)
                                    
                                else:
                                    string+=" + " + str(value) + " "
                                    
                                num+=value
                            string+=")"
                            result+=num
                    else:
                        string += ("( " + item + " )")
                        
                        result += int(item)
            

                elif count!= 0 and operation[count-1]=="-":
                    

                    dice = re.split(r'\s*[dD]\s*', item)
                    
                    if "D" in item or "d" in item:
                        
                        if dice[0]=="":
                            value= random.randint(1, int(dice[1]))
                            
                            string += ("( " + str(value) + " )")
                            result-=value

                        else:
                            for i in range (int(dice[0])):
                                value= random.randint(1, int(dice[1]))
                                
                                if i==0:
                                    string+= "( " + str(value)
                                    
                                else:
                                    string+=" + " + str(value) + " "
                                    
                                num+=value
                            string+=")"
                            result-=num
                    else:
                        string += ("( " + item + " )")
                        
                        result -= int(item)  
                
                if count < len(operation):
                    string +=" " + operation[count] + " "    
                    
                    count += 1
                
            
            num=0
        string += " = " + str(result)
        return result
    except:
        print("Input Error: Data needs to be in string format and structured like 1d5 + 2d5 - 5")


