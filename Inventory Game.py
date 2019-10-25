def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k , v in inventory.items():
        print(str(v) +" " + k)
        item_total = v + item_total
    print("Total number of items: "+ str(item_total))


if __name__ == "__main__":
    input_rope = int(input("rope you have:"))
    input_torch = int(input("torch you have:"))
    input_goldCoin = int(input("gold coin you have:"))
    input_dagger = int(input("dagger you have:"))
    input_arrow = int(input("arrow you have:"))
    staff = {'rope': input_rope,'torch':input_torch,'gold':input_goldCoin,'dagger':input_dagger,'arrow':input_arrow}
    display_inventory(staff)

