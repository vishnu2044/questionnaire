import csv 
#data collection
class The_Questionnaire():
    List_Personal_Details = []
    List_Answers = []   
    str_ans1 = " "
    str_personal = " "
    List_full_details = []
    def questionnaire_1(qstns):
        i = 1
        while 1:  
            i+=1

            #collecting personal data and store into a list(List_Personal_Details)
            name = input("enter your name : ")
            occupation = input("enter your occupation : ")
            company = input("enter your company name : ")
            contact = input("enter your contact number : ")

            The_Questionnaire.List_Personal_Details.append(name)
            The_Questionnaire.List_Personal_Details.append(occupation)
            The_Questionnaire.List_Personal_Details.append(company)
            The_Questionnaire.List_Personal_Details.append(contact)

            

            #QUESTIONNAIRE
            print("\n\n")
            questionnaire = "QUESTIONNAIRE"
            x = questionnaire.center(40," ")
            print(x)
            print("\n")

            #MANAGEMENT
            print("\n")
            management = "MANAGEMENT"
            y = management.center(20,"_")
            print(y)
            print("\n")

            #Collecting answers into a list (List_Answers)
            print("1. Does the management are providing awareness class regarding operation ?")
            print(" a) Daily\n b) Weakly\n c) Monthly\n d) No")
            a1 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a1)


            print("\n2. Does the management  provide adequate rest period? ") 
            print(" a) Properly\n b) Partly\n c) Depends on the work\n d) No")
            a2 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a2)

            print("\n3. How the management gives promotion according to the employees?")
            print(" a) experience\n b) Skill level\n c) Qualification\n d) Recommendation")
            a3 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a3)

            print("\n4.Does the management take proper investigation about previous accident reasons for safety measurements ?")
            print(" a) Proper investigation \n b) Partial investigation\n c) Improper investigation\n d) No investigation process")
            a4 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a4)

            print("\n5.Does the management forcing to complete production target in a limited period ?")
            print(" a) Yes\n b) Based on the profit margin\n c) No")
            a5 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a5)

            print("\n6.Does any employees work with incompatible physical conditions ?")
            print(" a) In office works\n b) In field works\n c) No")
            a6 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a6)

            print("\n7.Does the management  provide proper training ?")
            print(" a) Yes\n b) According to skills\n c) According to their experience\n d) According to their qualification\n e)No")
            a7 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a7)

            print("\n8.Does the management provide orientation classes about mental health ?")
            print(" a) Yes\n b) Some times\n c) No")
            a8 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a8)

            print("\n9.Does the management provide safety  equipments and precuations ?")
            print(" a) Yes\n b) Depends on the hazards\n c) Depends on the equipment health\n d) No")
            a9 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a9)

            print("\n10.Did the excessive  workload given  by the  management ?")
            print(" a) Yes\n b) Sometimes\n c) No")
            a10 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a10)

            print("\n11.Did the organization maintain proper schedule ?")
            print(" a) Yes\n b) Depends on the work\n c) No\n d) ")
            a11 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a11)

            #MANAGEMENT
            print("\n")
            supervisor = "SUPERVISOR"
            z = supervisor.center(20,"_")
            print(z)

            print("\n12.Does the supervisor failed to take proper overview ?")
            print(" a) Yes\n b) Sometimes\n c) No")
            a12 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a12)

            print("\n13.Does the supervisor coordinating the activities of the workers ?")
            print(" a) Yes\n b) In a proper manner\n c) Sometimes\n d) No")
            a13 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a13)

            print("\n14.Does the supervisor providing proper reports and other information to mine management about all aspects of mining or quarrying operations ?")
            print(" a) yes\n b) Depends on the work\n c) No")
            a14 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a14)

            print("\n15.The supervisor failed to report of any safety hazard ?")
            print(" a) Yes\n b) Depends on the hazard\n c) No")
            a15 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a15)

            print("\n16.Does the supervisor failed to ensure rules and regulations  in the workplace")
            print(" a) Yes\n b) Maybe\n c) No")
            a16 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a16)

            print("\n17.Did the supervisor failed to report unsafe  tendencies ?")
            print(" a) Yes\n b) No")
            a17 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a17)

            #WORKERS
            print("\n\n")
            workers = "WORKERS"
            a = workers.center(20,"_")
            print(a)

            print("\n18.Does the workers are showing over confidence ?")
            print(" a) Low confident\n b) Confident\n c) Over confident")
            a18 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a18)

            print("\n19.Does the workers are aware about the safety hazards in workplace ?")
            print(" a) Yes\n b) No")
            a19 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a19)

            print("\n20.While doing operation does the workers feel stress ?")
            print(" a) Yes\n b) Depends on the work\n c) Depends on the health\n c) No")
            a20 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a20)

            print("\n21.Does the workers are aware about all the operations in the mine ?")
            print(" a) Low \n b) Medium\n c) High")
            a21 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a21)

            print("\n22.Does the supervisor  provide adequate rest period?")
            print(" a) )Yes\n b) Depends on the work \n c) )No")
            a22 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a22)

            print("\n23.Did every workers are following safety rules ?")
            print(" a) Yes\n b) Maybe\n c) No")
            a23 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a23)

            print("\n24.Does the workers are able to concentrate during the work ?")
            print(" a) Yes\n b) Depends on the mental health\n c) Depends on the physical health\n d) )Depends on the work pressure\n e)No")
            a24 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a24)

            print("\n25.Did any workers use any type of  smoking/drinking habits during the work?")
            print(" a) Yes\n b) Moderately\n c) No")
            a25 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a25)

            print("\n26.Did you have any problems with your co-workers ?")
            print(" a) Yes\n b) partially\n c) )No")
            a26 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a26)

            print("\n27.Are you comfortable with your work atmosphere ?")
            print(" a) Comfortable\n b) Partially comfortable\n c) Dis comfortable")
            a27 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a27)

            print("\n28.Does any workers overexertion while off duty ?")
            print(" a) Yes\n b) Moderately \n c) No")
            a28 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a28)

            print("\n29.Does any workers work with incompatible physical conditions or illness ?")
            print(" a) Yes\n b) sometimes\n c) No")
            a29 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a29)

            print("\n30.Does the workers feel excessive task or work ?")
            print(" a) Yes\n b) Sometimes\n c) No")
            a30 = input("enter your answer : ")
            The_Questionnaire.List_Answers.append(a30)

            print(The_Questionnaire.List_Personal_Details)
            print(The_Questionnaire.List_Answers)

            #converting list  into string List_Answers => str_ans1
            for a in The_Questionnaire.List_Answers:
                The_Questionnaire.str_ans1 += a + ","

            #converting list into string List_personal_details => str_personal
            for b in The_Questionnaire.List_Personal_Details:
                The_Questionnaire.str_personal += b + ","

            print(The_Questionnaire.str_personal)
            print(The_Questionnaire.str_ans1)

            #write the data to "dat" file "data_collection"
            personal_details_and_answers = open("data_collection.txt", "a")
            personal_details_and_answers.write("\n" + The_Questionnaire.str_personal + The_Questionnaire.str_ans1)
            personal_details_and_answers.close()

            #to continue or not
            ans = input("Do you want to continue ? \n\nPress 'Y' to continue \nPress 'N' to stop ")
            if ans == "N":
                break

#writing the data into csv format
class Convertion_into_CSV(The_Questionnaire):

    def Questionnaire_into_CSV(csvfile):
        The_Questionnaire.List_full_details = (The_Questionnaire.List_Personal_Details + The_Questionnaire.List_Answers)
        List_headings = ["Name", "Occupation", "Company", "Contact", 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

        #name of csv file
        filename = "Questionnaire_records.csv"
        
        #writing to csv file
        with open (filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(List_headings)  #writing the headings
            csvwriter.writerows(The_Questionnaire.List_full_details)  #writing the answers


answers_1 = The_Questionnaire()
answers_1.questionnaire_1()
result = Convertion_into_CSV()
result.Questionnaire_into_CSV()
