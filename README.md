# pyclan

This is a library for working with CLAN (.cha) files


## usage examples:

```python

import pyclan

clan_file = ClanFile("/path/to/cha/file.cha")

# pull out all comments entered by the user
# It'll leave out machine generated comments
all_user_comments = clan_file.get_user_comments()

# get a single specific conversation block by index
block_33 = clan_file.get_block(33)

# get a group of blocks by specific index
blocks_5_19_12_and_45 = clan_file.get_blocks(select=[5, 19, 12, 45])

# get a range of blocks
blocks_7_through_33 = clan_file.get_blocks(begin=7, end=33)

# get all FAN and MAN tiered lines
# (function takes variable number of arguments)
all_FAN_and_MAN_tiers = clan_file.get_tiers("FAN", "MAN")

```