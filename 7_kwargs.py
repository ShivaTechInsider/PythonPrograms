def person_info(**kwargs):             # it will accept it as a dictionary kwargs={name:"shiva",age:20,roll:16}
    for key,value in kwargs.items():
        print(key,value)
        


person_info(name="shiva",age=22,roll=16)        