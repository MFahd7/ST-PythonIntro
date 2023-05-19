package coffeshop;
/**
// * @author Mohammed Fahd
*/

import java.util.ArrayList;

class MenuItem {
    private String items;
    private String item_type;
    private double price;

    public MenuItem(String item, String item_type, double price) {
        this.items = item;
        this.item_type = item_type;
        this.price = price;
    }

    public String get_Item() {
        return items;
    }

    public String get_ItemType() {
        return item_type;
    }

    public double get_Price() {
        return price;
    }
}

class CoffeeShop {
    private String name;
    private ArrayList<MenuItem> menu;
    private ArrayList<String> orders;

   public CoffeeShop(String name, ArrayList<MenuItem> menu) {
        this.name = name;
        this.menu = menu;
        this.orders = new ArrayList<>();
   }

   public void addOrder(String item) {
        for (MenuItem menu_item : menu) {
            if (menu_item.get_Item().equals(item)) {
                orders.add(item);
                return;
            }
        }
        System.out.println("This item is currently unavailable!");
   }

   public void fulfillOrder() {
        if (orders.isEmpty()) {
            System.out.println("All orders have been fulfilled!");
        } else {
            String item = orders.remove(0);
            System.out.println("The " + item + " is ready!");
        }
   }

   public ArrayList<String> listOrders() {
        return orders;
   }

   public double dueAmount() {
        double total = 0;
        for (String order : orders) {
            for (MenuItem menu_item : menu) {
                if (menu_item.get_Item().equals(order)) {
                    total += menu_item.get_Price();
                    break;
                }
            }
        }
        return total;
    }

   public String cheapestItem() {
        MenuItem cheapest = null;
        for (MenuItem menu_item : menu) {
            if (cheapest == null || menu_item.get_Price() < cheapest.get_Price()) {
                cheapest = menu_item;
            }
        }
        return cheapest.get_Item();
    }

   public ArrayList<String> drinksOnly() {
        ArrayList<String> drinks = new ArrayList<>();
        for (MenuItem menu_item : menu) {
            if (menu_item.get_ItemType().equals("drink")) {
                drinks.add(menu_item.get_Item());
            }
        }
        return drinks;
    }

   public ArrayList<String> foodOnly() {
        ArrayList<String> food = new ArrayList<>();
        for (MenuItem menu_item : menu) {
            if (menu_item.get_ItemType().equals("food")) {
                food.add(menu_item.get_Item());
            }
        }
        return food;
    }
}

public class CoffeShop {
    public static void main(String[] args) {
        ArrayList<MenuItem> menu = new ArrayList<>();
        menu.add(new MenuItem("Coffee", "drink", 2.5));
        menu.add(new MenuItem("Sandwich", "food", 5));
        menu.add(new MenuItem("Tea", "drink", 2));

        CoffeeShop coffeeShop = new CoffeeShop("My Coffee Shop", menu);

        coffeeShop.addOrder("Coffee");    // adds "Coffee" to the orders
        coffeeShop.addOrder("Smoothie");  // prints "This item is currently unavailable!"
        coffeeShop.fulfillOrder();        // prints "The Coffee is ready!"
        coffeeShop.fulfillOrder();        // prints "All orders have been fulfilled!"
        System.out.println(coffeeShop.listOrders());  // returns []
        coffeeShop.addOrder("Tea");       // adds "Tea" to the orders
        coffeeShop.addOrder("Sandwich");  // adds "Sandwich" to the orders
        System.out.println(coffeeShop.dueAmount());
    }
}
