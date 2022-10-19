# Age-Calculator-Class
This Class will get a data contain a pair of name and date of birth, and will return more data for each person like age, day of birth and you can add or delete spacific person data
The usage of the class is as below,
```
>>> obj= AgeCalculator([("a","12-1-2000"),("b","1-1-1999"),("c","24-12-1985")])
>>> obj.print_report()
c is 37 years old, and born on 24/12/1985 and it was Tuesday
b is 23 years old, and born on 01/01/1999 and it was Friday
a is 22 years old, and born on 12/01/2000 and it was Wednesday

The oldest one is c
The smallest one a
```

### To delete the data in object
```
>>> del obj.generate_person_data
```
### To delete spacific person data
```
>>> obj.delete_person_data("a")
'a Data Deleted!!!'
```
### To set new person data it will append with the existed one
```
>>> obj2 = AgeCalculator()
>>> obj2.generate_person_data = ("Ahmed","1-5-2000")
>>> obj2.all_persons_data
[{'name': 'Ahmed',
  'date_of_birth': datetime.datetime(2000, 5, 1, 0, 0),
  'day_of_birth': 'Monday',
  'age': 22}]

