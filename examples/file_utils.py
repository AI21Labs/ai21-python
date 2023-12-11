import os


def create_file(path: str, name: str):
    content = ("Sloths are a Neotropical group of xenarthran mammals constituting the suborder Folivora,"
               " including the extant arboreal tree sloths and extinct terrestrial ground sloths."
               " Noted for their slowness of movement, tree sloths spend most of their lives hanging "
               "upside down in the trees of the tropical rainforests of South America and Central America."
               " Sloths are considered to be most closely related to anteaters, together making up the"
               " xenarthran order Pilosa. There are six extant sloth species in two genera – Bradypus"
               " (three–toed sloths) and Choloepus (two–toed sloths). Despite this traditional naming,"
               " all sloths have three toes on each rear limb-- although two-toed sloths have only two digits"
               " on each forelimb.[3] The two groups of sloths are from different, distantly related families,"
               " and are thought to have evolved their morphology via parallel evolution from terrestrial ancestors."
               " Besides the extant species, many species of ground sloths ranging up to the size of elephants"
               " (like Megatherium) inhabited both North and South America during the Pleistocene Epoch. However,"
               " they became extinct during the Quaternary extinction event around 12,000 years ago,"
               " along with most large bodied animals in the New World. The extinction correlates in time "
               "with the arrival of humans, but climate change has also been suggested to have contributed. Members of an endemic radiation of Caribbean sloths also formerly lived in the Greater Antilles but became extinct after humans settled the archipelago in the mid-Holocene, around 6,000 years ago.")
    f = open(os.path.join(path, name), "w")
    f.write(content)
    f.close()


def delete_file(path: str, name: str):
    full_file_path = os.path.join(path, name)
    if os.path.isfile(full_file_path):
        os.remove(full_file_path)
        print(f"Delete file: {full_file_path}")
    else:
        print(f"Error: file not found: {full_file_path}")
