import turtle
import pandas
import random
screen=turtle.Screen()

screen.title('Name the Countries')
image='world_map.gif'
correct=0

screen.setup(width=800,height=500)
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("country_names.csv")
countries= data.country.to_list()
guess=0
color = ['red','green','brown','orange','blue']
random_color= random.randint(0,4)
guessed=[]
while True:
    if correct==196:
        country_turtle.hideturtle()
        country_turtle.goto(0, 0)
        country_turtle.color('black')
        country_turtle.write("ALL CORRECT GUESSES", align="center", font=("Courrier", 35, "bold"))
    else:
        answer=screen.textinput(str(correct)+"/196 Correct Guesses", "Name the Country:").lower()
        guess += 1

        if answer in guessed:
            print(guessed)
        else:
            country_turtle=turtle.Turtle()
            for i in range(0,len(countries)):
                country_name=countries[i]
                if answer==country_name.lower():
                    print(country_name)
                    guessed.append(answer)
                    x_list = data['x'].to_list()
                    y_list = data['y'].to_list()
                    xcor= int(float(x_list[i]))
                    ycor = int(float(y_list[i]))
                    country_turtle.hideturtle()
                    country_turtle.penup()
                    random_color = random.randint(0, 4)
                    country_turtle.color(color[random_color])
                    country_turtle.goto(xcor, ycor)
                    country_turtle.write(country_name, align="center", font=("Arial",7, "bold"))
                    correct+=1



turtle.exitonclick()