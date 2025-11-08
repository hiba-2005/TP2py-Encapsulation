from compte_bancaire import CompteBancaire

if __name__ == "__main__":
    compte = CompteBancaire("Ali", 1000)
    compte.deposer(200)
    compte.retirer(150)
    print(compte)
    print("Solde accessible (lecture) :", compte.solde)

    print("\nHistorique des opérations :")
    compte.afficher_operations()

    # Tentative de modification directe
    try:
        compte.solde = 500
    except AttributeError as e:
        print("\nErreur capturee :", e)
