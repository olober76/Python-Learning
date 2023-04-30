# Latihan kalkulator sederhana

print(20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")

angka_1 = float(input("masukkan bilangan pertama \t: "))
operator = input("Operator (+,-,x,/) \t\t: ")
angka_2 = float(input("masukkan bilangan kedua \t: "))

# Using If Else Statement
if operator == "+":
    hasil = angka_1 + angka_2
    print(f"\nhasilnya adalah \t: {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"\nhasilnya adalah \t: {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"\nhasilnya adalah \t: {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"\nhasilnya adalah \t: {hasil}")
else:
    print("\nTidak ada dalam program")

print("\n\nTerima kasih")


# Using Switch statement

print(20*"=")
print("Kalkulator Sederhana Yang Pake Switch")
print(20*"=" + "\n")

num1 = float(input("masukkan bilangan pertama \t: "))
operator = input("Operator (+,-,x,/,//,%) \t: ")
num2 = float(input("masukkan bilangan kedua \t: "))

match operator:
        case "+":
            print(f"\nHasil dari {num1:.0f} {operator} {num2:.0f} = {(num1 + num2):.0f}")
        case "-":
            print(f"\nHasil dari {num1:.0f} {operator} {num2:.0f} = {(num1 - num2):.0f}")
        case "x":
            print(f"\nHasil dari {num1:.0f} {operator} {num2:.0f} = {(num1 * num2):.0f}")
        case "*":
            print(f"\nHasil dari {num1:.0f} {operator} {num2:.0f} = {(num1 * num2):.0f}")
        case "/":
            print(f"\nHasil dari {num1:.0f} {operator} {num2:.0f} = {(num1 / num2):.0f}")
        case ":":
            print(f"\nHasil dari {num1:.0f} {operator} {num2:.0f} = {(num1 / num2):.0f}")
        case "//":
            print(f"\nHasil dari {num1:.0f} {operator} {num2:.0f} = {(num1 // num2):.0f}")
        case "%":
            print(f"\nHasil dari {num1:.0f} {operator} {num2:.0f} = {(num1 % num2):.0f}")
        case default:
            print("Tidak ada dalam Fitur kami")

print("\nTerima kasih")

