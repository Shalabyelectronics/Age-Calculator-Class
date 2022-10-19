from datetime import datetime

class AgeCalculator:
    def __init__(self,data:list=[]):
        self.data = data
        self.all_persons_data = None
        self.all_persons_data = []
        self.generate_person_data

    @property
    def generate_person_data(self):
        if len(self.data) > 0:
            temp = []
            for name, date in self.data:
                date = datetime.strptime(date,'%d-%m-%Y')
                person_data = {
                        'name':name,
                        'date_of_birth':date,
                        'day_of_birth':date.strftime('%A'),
                        'age':datetime.now().year - date.year 
                        }
                temp.append(person_data)

            self.all_persons_data = sorted(temp,key=self.sort_by_date)
            return self.all_persons_data
        
    @generate_person_data.setter
    def generate_person_data(self,data):
        name, date = data
        date = datetime.strptime(date,'%d-%m-%Y')
        person_data = {
                'name':name,
                'date_of_birth':date,
                'day_of_birth':date.strftime('%A'),
                'age':datetime.now().year - date.year 
                }
        self.all_persons_data.append(person_data)
        self.all_persons_data = sorted(self.all_persons_data,key=self.sort_by_date)

    @generate_person_data.deleter
    def generate_person_data(self):
        self.all_persons_data = []

    def delete_person_data(self,name):
        data_deleted =None
        if len(self.all_persons_data):
            for index,chunk in enumerate(self.all_persons_data):
                if chunk['name'] == name:
                    data_deleted = self.all_persons_data.pop(index)
            if data_deleted:
                return f"{name} Data Deleted!!!"
            return f"Sorry, can't find person name {name}"


    def sort_by_date(self, data):
        return data['date_of_birth']

    def print_report(self):
        oldest = self.all_persons_data[0]
        smallest = self.all_persons_data[-1]
        for person in self.all_persons_data:
            print(f"{person['name']} is {person['age']} years old, and born on {person['date_of_birth'].strftime('%d/%m/%Y')} and it was {person['day_of_birth']}")
        print(f"\nThe oldest one is {oldest['name']}",
                f"The smallest one {smallest['name']}",sep="\n")

