from pathlib import Path
import xml.etree.ElementTree as ET
import logging

XML_FILE_NAME = "groups.xml"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)
logger = logging.getLogger("log_event")

def get_timingExbytes_for_group(xml_tree, group_number_filter, log):
    root = xml_tree.getroot()

    for group in root.findall('group'):
        group_number = group.find('number')

        if  group_number is None or not group_number.text == group_number_filter:
            continue

        timing_exbytes = group.find('timingExbytes')

        if timing_exbytes is None:
            continue

        incoming  = timing_exbytes.find('incoming')

        if incoming  is not None:
            log.info(incoming.text)

tree = ET.parse(XML_FILE_NAME)
group = '0'

get_timingExbytes_for_group(tree, group, logger)
