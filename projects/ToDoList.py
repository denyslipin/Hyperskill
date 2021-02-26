from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class ToDoList:
    def __init__(self):
        self.week = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday",
                     4: "Friday", 5: "Saturday", 6: "Sunday"}
        self.main()

    def main(self):
        while True:
            print("1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Missed tasks")
            print("5) Add task\n6) Delete task\n0) Exit")
            user_input = input()
            print()
            if user_input == "1":
                self.show_todays_tasks()
            elif user_input == "2":
                self.show_weeks_tasks()
            elif user_input == "3":
                self.show_all_tasks()
            elif user_input == "4":
                self.show_missed_tasks()
            elif user_input == "5":
                self.add_task()
            elif user_input == "6":
                self.delete_task()
            elif user_input == "0":
                print("Bye!")
                break
            else:
                print("Invalid input")

    def show_todays_tasks(self):
        today = datetime.today()
        print(f"Today {today.day} {today.strftime('%b')}:")
        rows = session.query(Table).filter(Table.deadline == today.date()).all()
        if rows:
            for row in rows:
                print(str(row.id) + ". " + row.task)
            print()
        else:
            print("Nothing to do!\n")

    def show_weeks_tasks(self):
        today = datetime.today()
        for i in range(7):
            day = today + timedelta(days=i)
            print(f"{self.week[day.weekday()]} {day.day} {day.strftime('%b')}:")
            rows = session.query(Table).filter(Table.deadline == day.date()).all()
            if rows:
                for row in rows:
                    print(str(row.id) + ". " + row.task)
                print()
            else:
                print("Nothing to do!\n")

    def show_all_tasks(self):
        print("All tasks:")
        rows = session.query(Table).order_by(Table.deadline).all()
        if rows:
            for row in rows:
                day = str(row.deadline.day)
                month = row.deadline.strftime('%b')
                print(str(row.id) + ". " + row.task + ". " + day + " " + month)
            print()
        else:
            print("Nothing to do!\n")

    def show_missed_tasks(self):
        print("Missed tasks:")
        rows = session.query(Table).filter(Table.deadline < datetime.today().date()).order_by(Table.deadline).all()
        if rows:
            for row in rows:
                day = str(row.deadline.day)
                month = row.deadline.strftime('%b')
                print(str(row.id) + ". " + row.task + ". " + day + " " + month)
            print()
        else:
            print("Nothing to do!\n")

    def add_task(self):
        user_task = input("Enter task\n")
        user_date = input("Enter deadline\n")
        new_row = Table(task=user_task, deadline=datetime.strptime(user_date, '%Y-%m-%d').date())
        session.add(new_row)
        session.commit()
        print("The task has been added!\n")

    def delete_task(self):
        print("Choose the number of the task you want to delete:")
        rows = session.query(Table).order_by(Table.deadline).all()
        if rows:
            for row in rows:
                day = str(row.deadline.day)
                month = row.deadline.strftime('%b')
                print(str(row.id) + ". " + row.task + ". " + day + " " + month)
            print()
        else:
            print("Nothing to delete\n")
        del_task = int(input())
        specific_row = rows[del_task - 1]  # in case rows is not empty
        session.delete(specific_row)
        session.commit()
        print("The task has been deleted!")


if __name__ == '__main__':
    program = ToDoList()
