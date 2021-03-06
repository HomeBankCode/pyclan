def user_comments(self):
    return [line for line in self.line_map if line.is_user_comment]

def conv_block(self, block_num):
    line_map = []
    for index, line in enumerate(self.line_map):
        if line.conv_block_num == block_num:
            line_map.append(line)

    return ClanBlock(block_num, line_map)

def conv_blocks(self, begin=1, end=None, select=None):
    """ Get specified conversation blocks

    Args:
        self:
        begin (int): beginning of contiguous range (default start from beginning)
        end (end): end of contiguous range (default go to the end)
        select : list of specific block indices to retrieve
                (result will be sorted in ascending order)

    Returns: a BlockGroup of specified conversation blocks
    """
    blocks = []

    if select:

        selection_list = sorted(select)

        for block_num in selection_list:
            temp_block_lines = [line for line in self.line_map
                                    if line.conv_block_num == block_num]
            blocks.append(ClanBlock(block_num, temp_block_lines))

        return BlockGroup(blocks)

    if not end:
        end = self.num_blocks

    selection_list = range(begin, end+1)

    for block_num in selection_list:
        temp_block_lines = [line for line in self.line_map
                                if line.conv_block_num == block_num]
        blocks.append(ClanBlock(block_num, temp_block_lines))

    return BlockGroup(blocks)


def tier(self, *tiers):
    """ Get all ClanLines with specified tiers

    Args:
        self:
        *tiers: a list of tiers, e.g. ["MAN", "FAN", "CHN

    Returns: LineRange with all the lines
    """
    results = []
    for line in self.line_map:
        if line.tier in tiers:
            results.append(line)
        if line.multi_line_parent and\
           line.multi_line_parent.tier in tiers:
            results.append(line)
    return LineRange(results)

def filter_out_tier(self, *tiers):
    """ Remove all lines with specified tiers

    This function scans the lines that are held by the calling object
    and removes all the lines that contain the specified tiers.

    Args:
        self:
        *tiers (str): variable number of arguments specifying
                      which tiered lines to remove

    Returns:
        LineRange: With all the lines that were filtered out

    Examples:
        >>> clan_file = ClanFile("/path/to/file.cha")
        >>> block_33 = clan_file.get_block(33)
        >>> filtered_line_range = block_33.filter_out_tiers("MAN", "CHN")

    Will delete all the "MAN" and "CHN" tiered lines from the object
    representing block 33.
    """
    results = []
    for index, line in enumerate(self.line_map):
        if line.tier in tiers:
            results.append(line)
            del self.line_map[index]
    return LineRange(results)

def time(self, begin=None, end=None):
    """ Get all lines within a time range

    Args:
        self:
        begin (int): beginning time in milliseconds
        end (int): ending time in milliseconds

    Returns:
        LineRange: With all the lines within the time range


    Examples:
        >>> clan_file = ClanFile("/path/to/file.cha")
        >>> lines_in_time_range = clan_file.get_within_time(begin=12345, end=123456)
    """
    results = []

    region_started = False
    region_ended = False

    if begin and not end:
        for line in self.line_map:
            if line.time_onset >= begin:
                region_started = True
            if region_started:
                results.append(line)

    elif end and not begin:
        for line in self.line_map:
            if line.time_offset >= end:
                region_ended = True
            if not region_ended:
                if line.is_header:
                    continue
                results.append(line)

    elif begin and end:
        for line in self.line_map:
            if line.time_onset >= end:
                region_ended = True
            if line.time_onset >= begin:
                region_started = True
            if region_started and not region_ended:
                results.append(line)

    return LineRange(results)

def get_with_keyword(self, keyword):
    """
    Args:
        self:
        keyword: some string to search for

    Returns:
    """
    line_map = []

    for index, line in enumerate(self.line_map):
        if line.content:
            if keyword in line.content:
                line_map.append(line)

    return LineRange(line_map)

def replace_with_keyword(self, line_range, orig_key, new_key):
    for line in line_range.line_map:
        if orig_key in line.content:
            line.content = line.content.replace(orig_key, new_key)
            line.line  = line.line.replace(orig_key, new_key)

from elements import *
from clanfile import *