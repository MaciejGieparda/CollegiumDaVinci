import pandas as pd
import typer
import csv
import pandas

app = typer.Typer()

def main():

    choice = 0
    while choice < 3:
        print("*** Welcome to Titanic Passengers Dataset! Choose Your option ***")
        print("1) Print whole dataset")
        print("2) Filter Dataset")
        print("3) Quit")
        choice = int(input())

        if choice == 1:
            data = pd.read_csv('final_results.csv')
            print(data)

        elif choice == 2:
            data = pd.read_csv('final_results.csv')
            data = data.astype(str)
            traits = ['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
            print("Type one of traits that You want to filter: " + str(traits))
            trait = str(input("Enter Trait: "))
            if trait in traits:
                filtered_trait = str(input('Type desired parameter: '))
                print(data[data[trait] == filtered_trait])
            else:
                print('Wrong Trait typped!')

if __name__ == "__main__":
    main()