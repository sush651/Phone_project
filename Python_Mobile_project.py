#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Phone:
    def _init_(self, name, models, variants, colors, specifications):
        self.name = name
        self.models = models
        self.variants = variants
        self.colors = colors
        self.specifications = specifications

    def get_user_choice(self, prompt, valid_choices):
        while True:
            user_input = input(prompt).lower()
            if user_input in valid_choices:
                return user_input
            else:
                print("Invalid choice. Please try again.")

    def select_model(self):
        print(f"Which {self.name} model do you need? ({', '.join(self.models.keys())}): ")
        return self.get_user_choice('', self.models.keys())

    def select_variant(self):
        print(f"Which variant do you need? (i) {self.variants[0]} (ii) {self.variants[1]}: ")
        return self.get_user_choice('', self.variants.keys())

    def select_color(self):
        print(f"Which color do you need? ({', '.join(self.colors.keys())}): ")
        return self.get_user_choice('', self.colors.keys())

    def display_specifications(self):
        print("\nYou have selected the following options:")
        print(f"Phone: {self.name} {self.models[self.select_model()]}")
        print(f"Variant: {self.variants[self.select_variant()]}")
        print(f"Color: {self.colors[self.select_color()]}")
        print("Specifications:")
        print(self.specifications)


class IPhone(Phone):
    def _init_(self):
        super()._init_("iPhone", {'a': 'iphone13', 'b': 'iphone14', 'c': 'iphone15'},
                         {'i': '64GB', 'ii': '128GB'},
                         {'a': 'black', 'b': 'white'},
                         "Battery = 5000mAh\nCamera = 12-megapixel\nProcessor = A15 Bionic chip\nPrice = $1,000")


class Samsung(Phone):
    def _init_(self):
        super()._init_("Samsung", {'a': 'SamsungA14', 'b': 'SamsungA15'},
                         {'i': '64GB', 'ii': '128GB'},
                         {'a': 'black', 'b': 'white', 'c': 'blue'},
                         "Battery = 5000mAh\nCamera = 12-megapixel\nProcessor = A15 Bionic chip\nPrice = $1,000")


def phone():
    while True:
        output = "Yes"
        choice1 = input("Do you need a phone? (Yes/No): ")

        if choice1.lower() == output.lower():
            choice2 = input("Which phone do you need? (i) iPhone (ii) Samsung: ").lower()

            if choice2 == 'iphone' or choice2 == 'i':
                iphone = IPhone()
                iphone.display_specifications()
                return
            elif choice2 == 'samsung' or choice2 == 'ii':
                samsung = Samsung()
                samsung.display_specifications()
                return
            else:
                print("Invalid choice. Please enter 'i' for iPhone or 'ii' for Samsung.")
        elif choice1.lower() == "no":
            print("Thank you for visiting.")
            return
        else:
            print("Invalid choice. Please enter 'Yes' or 'No.'")


phone()


# In[ ]:


phone()


# In[ ]:




