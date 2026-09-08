x = eval(input('Distance in meters: '))

print('The measure of {} meters is {}km {}hm {}dam {:.0f}dm {:.0f}cm {:.0f}mm'.format(x, x / 1000, x / 100, x / 10, x * 10, x * 100, x * 1000))