# Wi-Fi Diagnostic Tree.

print('Reboot the computer and try to connect.')
wifi_fixed = input('Did that fix the problem? ')

if wifi_fixed == 'no':
    print('\nReboot the computer and try to connect.')
    wifi_fixed = input('Did that fix the problem? ')

    if  wifi_fixed == 'no':
        print("\nMake sure the cables between the router and modem")
        print("are plugged in firmly.")
        wifi_fixed = input('Did that fix the problem? ')

        if wifi_fixed == 'no':
            print('\nMove the router to a new location')
            print('and try to connect.')
            wifi_fixed = input('Did that fix the problem? ')

            if wifi_fixed == 'no':
                print('\nGet a new router.')
