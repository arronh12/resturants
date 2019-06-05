class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return self.name + " Menu is Avalable from {}:00 to {}:00".format(self.start_time, self.end_time)

    def calculate_bill(self, purchased_items):
        calc_bill = 0
        for i in purchased_items:
            calc_bill += self.items[i]
        return calc_bill

        # -------------------------------------------------


# ---------------------------------------------------
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50,
                'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
                }
brunch = Menu("Brunch", brunch_items, 11, 16)

early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu("Early Bird", early_bird_items, 15, 18)

dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
                'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00, }
dinner = Menu("Dinner", dinner_items, 17, 23)

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu("Kids", kids_items, 11, 21)
# -----------------------------------------------
# -----------------------------------------------
print(brunch)

break_items = ['pancakes', 'home fries', 'coffee']
print(brunch.calculate_bill(break_items))

early_bird_order = ['salumeria plate', 'mushroom ravioli (vegan)']
print(early_bird.calculate_bill(early_bird_order))


# -------------------------------------------------
# -----------------------------------------------

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return "This store is located at {}".format(self.address)

    def available_menus(self, time):
        for i in menus:
            if (time >= i.start_time) and (time < i.end_time):
                print(i.name + " is available")


# -------------------------------------------------
# -------------------------------------------------

menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

flagship_store.available_menus(17)

franchise_list = [flagship_store, new_installment]


# ------------------------------------------------
# ------------------------------------------------

class Business:
    def __init__(self, name, Franchises):
        self.name = name
        self.Franchises = Franchises


# ----------------------------------------------

basta_fazoolin = Business("'Basta Fazoolin' with my Heart", franchise_list)

arepas_menu = Menu('Take a Arepa',
                   {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
                    }, 10, 20)

arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

take_a_arepa = Business("Take a' Arepa", arepas_place)









