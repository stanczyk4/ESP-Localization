import time
import scanner
import identify

test, distances = scanner.get_BSSI()
distances = sorted(distances)
for i in range(0,10):
    # Wait
    time.sleep(3)

    # Save old test and distances
    oldTest = test
    oldDistances = distances

    # Scan again
    test, distances = scanner.get_BSSI()

    # Sort the list of distances
    distances = sorted(distances)
    circles = identify.identify(distances)

    # PASS CIRCLES LIST HERE

input("Press enter to continue...")
