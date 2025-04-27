import turtle
import colorsys

def create_turtle_art():
    try:
        # screen setup
        screen = turtle.Screen()
        screen.bgcolor("black")
        screen.title("Turtle Graphics")

        # create turtle
        pen = turtle.Turtle()
        pen.speed(0)
        pen.width(2)
        pen.hideturtle()

        # color settings
        colors = [] # empty list
        n = 36 # number of colors
        hue = 0

        for i in range(n):
            colors.append(
                colorsys.hsv_to_rgb(hue, 1, 1)
            )
            hue += 1/n
        
        # draw a colorful pattern
        for i in range(360):
            color = colors[i % n]
            pen.pencolor(color)
            pen.forward(i * 3 / n + i)
            pen.right(59)
            pen.forward(i * 3 / n + i)
            pen.right(59)
            pen.forward(i * 3 / n + i)
            pen.right(59)
            pen.right(1)

            if not turtle.isvisible():
                break
        turtle.done()
    
    except turtle.Terminator:
        print("Turtle window was closed.")
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
    finally:
        try:
            turtle.bye()
        except:
            pass
        print("Turtle graphics program has ended.")

if __name__ == "__main__":
    create_turtle_art()