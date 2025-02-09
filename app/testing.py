# ONLY FOR TESTING WITHOUT DOCKER
import utils

# species	island	bill_length_mm	bill_depth_mm	flipper_length_mm	body_mass_g	sex
# 0	Adelie	Torgersen	39.1	18.7	181.0	3750.0	Male
# 1	Adelie	Torgersen	39.5	17.4	186.0	3800.0	Female
# species	island	bill_length_mm	bill_depth_mm	flipper_length_mm	body_mass_g	sex
# 214	Gentoo	Biscoe	46.1	13.2	211.0	4500.0	Female
# 215	Gentoo	Biscoe	50.0	16.3	230.0	5700.0	Male
# species	island	bill_length_mm	bill_depth_mm	flipper_length_mm	body_mass_g	sex
# 146	Chinstrap	Dream	46.5	17.9	192.0	3500.0	Female
# 147	Chinstrap	Dream	50.0	19.5	196.0	3900.0	Male

print(utils.predict("Torgersen", 39.1, 18.7, 181.0, 3750.0, "Male"))
# print(utils.predict("Torgersen", 39.5, 17.4, 186.0, 3800.0, "Female"))
# print(utils.predict("Biscoe", 46.1, 13.2, 211.0, 4500.0, "Female"))
# print(utils.predict("Biscoe", 50.0, 16.3, 230.0, 5700.0, "Male"))
# print(utils.predict("Dream", 46.5, 17.9, 192.0, 3500.0, "Female"))
# print(utils.predict("Dream", 50.0, 19.5, 196., 3900.0, "Male"))

# print(utils.predict("Torgersen", 40.3, 18.0, 195.0, 3650.0, "Female"))
# print(utils.predict("Torgersen", 38.9, 17.8, 190.0, 3700.0, "Male"))
# print(utils.predict("Biscoe", 45.2, 14.3, 210.0, 4600.0, "Female"))
# print(utils.predict("Biscoe", 49.1, 15.2, 220.0, 5500.0, "Male"))
# print(utils.predict("Dream", 47.0, 18.5, 200.0, 3600.0, "Female"))
# print(utils.predict("Dream", 51.0, 20.0, 205.0, 4000.0, "Male"))
# print(utils.predict("Torgersen", 39.7, 18.2, 185.0, 3800.0, "Female"))
# print(utils.predict("Torgersen", 40.1, 17.5, 188.0, 3900.0, "Male"))
# print(utils.predict("Biscoe", 46.3, 13.5, 215.0, 4700.0, "Female"))
# print(utils.predict("Biscoe", 48.5, 16.0, 225.0, 5600.0, "Male"))
# print(utils.predict("Dream", 48.0, 19.0, 195.0, 3700.0, "Female"))
# print(utils.predict("Dream", 52.0, 21.0, 200.0, 4100.0, "Male"))
# print(utils.predict("Torgersen", 41.0, 18.3, 190.0, 3850.0, "Female"))
# print(utils.predict("Torgersen", 39.0, 17.6, 192.0, 3950.0, "Male"))
# print(utils.predict("Biscoe", 47.1, 14.0, 220.0, 4800.0, "Female"))
# print(utils.predict("Biscoe", 50.2, 15.5, 230.0, 5700.0, "Male"))
# print(utils.predict("Dream", 49.0, 18.7, 200.0, 3800.0, "Female"))
# print(utils.predict("Dream", 53.0, 20.5, 205.0, 4200.0, "Male"))
# print(utils.predict("Torgersen", 40.5, 18.1, 185.0, 3750.0, "Female"))
# print(utils.predict("Torgersen", 38.5, 17.3, 190.0, 3850.0, "Male"))