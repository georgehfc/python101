# THIS SCRIPT EVALUATES LUGGAGE WEIGHTS
# "INTEGRAL DE LIVRO NÃO É RESUMO" @ErickMuller
print("### ⚖️ WELCOME ⚖️ ###")
premium_client = input("Are you a Premium client? Y-YES or N-NO: ")
luggage = int(input("Inform the weight of the luggage in kgs: "))
if premium_client == 'N' or premium_client == 'n':
    if luggage > 28:
        print("⛔️ Overweight! Please discard some items.")
    else:
        print("✅ Permitted weight. Go on!")
elif premium_client == 'Y' or premium_client == 'y':
    if luggage > 33:
        print("⛔️ Overweight! Please discard some items.")
    else:
        print("✅ Permitted weight. Go on!")
else:
    print("Bye! 🛫")
print("Premium client? {}".format(premium_client))
print("Luggage weight: {}kg".format(luggage))
