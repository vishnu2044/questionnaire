def questionnaire_1():
    
    i = 1
    while i<=2:  #collecting data upto 2 members
        i+=1
        name = input("enter your name : ")
        occupation = input("enter your occupation : ")
        company = input("enter your company name : ")
        contact = input("enter your contact number : ")

        personal_details = []
        personal_details.append(name)
        personal_details.append(occupation)
        personal_details.append(company)
        personal_details.append(contact)

        print(personal_details)
        answers = []

        print("\n\n")
        questionnaire = "QUESTIONNAIRE"
        x = questionnaire.center(40," ")
        print(x)
        print("\n")

        print("\n")
        management = "MANAGEMENT"
        y = management.center(20,"_")
        print(y)
        print("\n")


        print("1. Does the management are providing awareness class regarding operation ?")
        print(" a) Daily\n b) Weakly\n c) Monthly\n d) No")
        a1 = input("enter your answer : ")
        answers.append(a1)


        print("\n2. Does the management  provide adequate rest period? ") 
        print(" a) Properly\n b) Partly\n c) Depends on the work\n d) No")
        a2 = input("enter your answer : ")
        answers.append(a2)

        print("\n3. How the management gives promotion according to the employees?")
        print(" a) experience\n b) Skill level\n c) Qualification\n d) Recommendation")
        a3 = input("enter your answer : ")
        answers.append(a3)

        print("\n4.Does the management take proper investigation about previous accident reasons for safety measurements ?")
        print(" a) Proper investigation \n b) Partial investigation\n c) Improper investigation\n d) No investigation process")
        a4 = input("enter your answer : ")
        answers.append(a4)

        print("\n5.Does the management forcing to complete production target in a limited period ?")
        print(" a) Yes\n b) Based on the profit margin\n c) No")
        a5 = input("enter your answer : ")
        answers.append(a5)

        print("\n6.Does any employees work with incompatible physical conditions ?")
        print(" a) In office works\n b) In field works\n c) No")
        a6 = input("enter your answer : ")
        answers.append(a6)

        print("\n7.Does the management  provide proper training ?")
        print(" a) Yes\n b) According to skills\n c) According to their experience\n d) According to their qualification\n e)No")
        a7 = input("enter your answer : ")
        answers.append(a7)

        print("\n8.Does the management provide orientation classes about mental health ?")
        print(" a) Yes\n b) Some times\n c) No")
        a8 = input("enter your answer : ")
        answers.append(a8)

        print("\n9.Does the management provide safety  equipments and precuations ?")
        print(" a) Yes\n b) Depends on the hazards\n c) Depends on the equipment health\n d) No")
        a9 = input("enter your answer : ")
        answers.append(a9)

        print("\n10.Did the excessive  workload given  by the  management ?")
        print(" a) Yes\n b) Sometimes\n c) No")
        a10 = input("enter your answer : ")
        answers.append(a10)

        print("\n11.Did the organization maintain proper schedule ?")
        print(" a) Yes\n b) Depends on the work\n c) No\n d) ")
        a11 = input("enter your answer : ")
        answers.append(a11)

        print("\n")
        supervisor = "SUPERVISOR"
        z = supervisor.center(20,"_")
        print(z)

        print("\n12.Does the supervisor failed to take proper overview ?")
        print(" a) Yes\n b) Sometimes\n c) No")
        a12 = input("enter your answer : ")
        answers.append(a12)

        print("\n13.Does the supervisor coordinating the activities of the workers ?")
        print(" a) Yes\n b) In a proper manner\n c) Sometimes\n d) No")
        a13 = input("enter your answer : ")
        answers.append(a13)

        print("\n14.Does the supervisor providing proper reports and other information to mine management about all aspects of mining or quarrying operations ?")
        print(" a) yes\n b) Depends on the work\n c) No")
        a14 = input("enter your answer : ")
        answers.append(a14)

        print("\n15.The supervisor failed to report of any safety hazard ?")
        print(" a) Yes\n b) Depends on the hazard\n c) No")
        a15 = input("enter your answer : ")
        answers.append(a15)

        print("\n16.Does the supervisor failed to ensure rules and regulations  in the workplace")
        print(" a) Yes\n b) Maybe\n c) No")
        a16 = input("enter your answer : ")
        answers.append(a16)

        print("\n17.Did the supervisor failed to report unsafe  tendencies ?")
        print(" a) Yes\n b) No")
        a17 = input("enter your answer : ")
        answers.append(a17)

        print("\n\n")
        workers = "WORKERS"
        a = workers.center(20,"_")
        print(a)

        print("\n18.Does the workers are showing over confidence ?")
        print(" a) Low confident\n b) Confident\n c) Over confident")
        a18 = input("enter your answer : ")
        answers.append(a18)

        print("\n19.Does the workers are aware about the safety hazards in workplace ?")
        print(" a) Yes\n b) No")
        a19 = input("enter your answer : ")
        answers.append(a19)

        print("\n20.While doing operation does the workers feel stress ?")
        print(" a) Yes\n b) Depends on the work\n c) Depends on the health\n c) No")
        a20 = input("enter your answer : ")
        answers.append(a20)

        print("\n21.Does the workers are aware about all the operations in the mine ?")
        print(" a) Low \n b) Medium\n c) High")
        a21 = input("enter your answer : ")
        answers.append(a21)

        print("\n22.Does the supervisor  provide adequate rest period?")
        print(" a) )Yes\n b) Depends on the work \n c) )No")
        a22 = input("enter your answer : ")
        answers.append(a22)

        print("\n23.Did every workers are following safety rules ?")
        print(" a) Yes\n b) Maybe\n c) No")
        a23 = input("enter your answer : ")
        answers.append(a23)

        print("\n24.Does the workers are able to concentrate during the work ?")
        print(" a) Yes\n b) Depends on the mental health\n c) Depends on the physical health\n d) )Depends on the work pressure\n e)No")
        a24 = input("enter your answer : ")
        answers.append(a24)

        print("\n25.Did any workers use any type of  smoking/drinking habits during the work?")
        print(" a) Yes\n b) Moderately\n c) No")
        a25 = input("enter your answer : ")
        answers.append(a25)

        print("\n26.Did you have any problems with your co-workers ?")
        print(" a) Yes\n b) partially\n c) )No")
        a26 = input("enter your answer : ")
        answers.append(a26)

        print("\n27.Are you comfortable with your work atmosphere ?")
        print(" a) Comfortable\n b) Partially comfortable\n c) Dis comfortable")
        a27 = input("enter your answer : ")
        answers.append(a27)

        print("\n28.Does any workers overexertion while off duty ?")
        print(" a) Yes\n b) Moderately \n c) No")
        a28 = input("enter your answer : ")
        answers.append(a28)

        print("\n29.Does any workers work with incompatible physical conditions or illness ?")
        print(" a) Yes\n b) sometimes\n c) No")
        a29 = input("enter your answer : ")
        answers.append(a29)

        print("\n30.Does the workers feel excessive task or work ?")
        print(" a) Yes\n b) Sometimes\n c) No")
        a30 = input("enter your answer : ")
        answers.append(a30)

        print(answers)
        my_string = " "
        for x in answers:
            my_string += x + ","

        per = open("questionnaire_data", "w")
        per.write("\n" + name + ", " + occupation + ", " + contact + ", " + company + ", " + my_string )
        per.close()
        ans = input("Do you want to continue ? (YES/ NO) : ")
        if ans == "NO":
            break

questionnaire_1()