import os
import time

def main():
    # Export GPIO18 as an output pin
    with open('/sys/class/gpio/export', 'w') as f:
        f.write('18')

    # Set GPIO18 as output
    with open('/sys/class/gpio/gpio18/direction', 'w') as f:
        f.write('out')

    while True:
        # Set GPIO18 high
        with open('/sys/class/gpio/gpio18/value', 'w') as f:
            f.write('1')
        time.sleep(0.2)

        # Set GPIO18 low
        with open('/sys/class/gpio/gpio18/value', 'w') as f:
            f.write('0')
        time.sleep(0.2)

if __name__ == '__main__':
    main()