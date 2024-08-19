from scraplib.drivers.driver_types import EGender, FriendFilter
from scraplib.drivers.y99.y99_driver import Y99Driver

if __name__ == "__main__":
    driver = Y99Driver()
    driver.authenticate()
    driver.findFriends(FriendFilter(gender= EGender.female))