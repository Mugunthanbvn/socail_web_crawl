from scraplib.drivers.driver_types import EGender, FriendFilter
from scraplib.drivers.y99.y99_driver import Y99Driver
# from naampy import in_rolls_fn_gender
# from naampy import predict_fn_gender
import pandas as pd
# import pandas as pd

if __name__ == "__main__":
    driver = Y99Driver()
    driver.authenticate()
    driver.findFriends(FriendFilter(gender= EGender.female))
    # names = [{'name': 'mugunthan'},
    #          {'name': 'nabha'},
    #          {'name': 'yasmin'},
    #          {'name': 'deepti'},
    #          {'name': 'hrithik'},
    #          {'name': 'vivek'}]
    # df = pd.DataFrame(names)
    # # print("***",predict_fn_gender( 'deepti'))
    # print("hello")
