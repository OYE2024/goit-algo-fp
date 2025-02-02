import turtle
import math


def draw_tree(t, length, angle, level):
    if level == 0:
        return

    # Малюємо гілку
    t.forward(length)

    # Малюємо праву гілку
    t.left(angle)
    draw_tree(t, length * 0.7, angle, level - 1)  # Зменшуємо довжину гілки

    # Повертаємося назад
    t.right(2 * angle)
    draw_tree(t, length * 0.7, angle, level - 1)  # Зменшуємо довжину гілки

    # Повертаємось до початкової позиції
    t.left(angle)
    t.backward(length)


# Налаштування вікна
screen = turtle.Screen()
screen.bgcolor("white")

# Створюємо об'єкт "черепашки"
t = turtle.Turtle()
t.speed(0)  # Режим малювання
t.left(90)  # Ориєнтуємо черепаху вверх

# Параметри
length = 100  # Початкова довжина гілки
angle = 30  # Кут розбіжності гілок
level = 7  # Глибина рекурсії

draw_tree(t, length, angle, level)
t.hideturtle()
screen.mainloop()
