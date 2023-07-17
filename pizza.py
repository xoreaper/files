def take_order():
    customer_name = input("Enter your name: ")
    print("Pizza Menu:")
    print("1. Cheese")
    print("2. Pepperoni")
    print("3. Margherita")
    print("4. Hawaiian")
    print("5. Veggie")
    choice = int(input("Enter your choice (1-5): "))

    pizzas = ["Cheese", "Pepperoni", "Margherita", "Hawaiian", "Veggie"]
    pizza = pizzas[choice - 1]

    toppings = select_toppings()

    print(f"You ordered: {pizza}")
    bill = calculate_bill(customer_name, pizza, toppings)
    save_order(customer_name, pizza, toppings, bill)


def select_toppings():
    print("Available toppings:")
    print("1. Mushrooms")
    print("2. Onions")
    print("3. Bell Peppers")
    print("4. Olives")
    print("5. Spinach")

    num_toppings = int(input("How many toppings do you want? "))
    toppings = []

    for _ in range(num_toppings):
        while True:
            topping_choice = int(input("Enter topping choice (1-5): "))
            if 1 <= topping_choice <= 5:
                toppings.append(get_topping_name(topping_choice))
                break

    return toppings


def get_topping_name(topping_choice):
    toppings = {
        1: "Mushrooms",
        2: "Onions",
        3: "Bell Peppers",
        4: "Olives",
        5: "Spinach"
    }
    return toppings[topping_choice]


def calculate_bill(customer_name, pizza, toppings):
    prices = {
        "Cheese": 399,
        "Pepperoni": 450,
        "Margherita": 500,
        "Hawaiian": 480,
        "Veggie": 350
    }
    topping_price = 100
    toppings_count = len(toppings)

    bill = prices[pizza] + (topping_price * toppings_count)
    print(f"Customer Name: {customer_name}")
    print(f"Pizza: {pizza}")
    print(f"Toppings: {', '.join(toppings)}")
    print(f"Total Bill: Rs{bill}")
    return bill


def save_order(customer_name, pizza, toppings, bill):
    order = f"Customer Name: {customer_name}\nPizza: {pizza}\nToppings: {', '.join(toppings)}\nTotal Bill: Rs{bill}\n"

    with open("orders.txt", "a") as file:
        file.write(order)

    print("Order saved!")


def main():
    print("Welcome to the Pizza Shop")
    take_order()


if __name__ == "__main__":
    main()
