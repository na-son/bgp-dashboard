# BGP Attributes
PREFIX = 0
ORIGIN = 1
AS_PATH = 2
NEXT_HOP = 3
MULTI_EXIT_DISC = 4
LOCAL_PREF = 5
ATOMIC_AGGREGATE = 6
AGGREGATOR = 7
COMMUNITY = 8
ORIGINATOR_ID = 9
CLUSTER_LIST = 10
DPA = 11
ADVERTISER = 12
CLUSTER_ID = 13
MP_REACH_NLRI = 14
MP_UNREACH_NLRI = 15
EXTENDED_COMMUNITIES = 16
#
WITHDRAWAL = 11
AGE = 12
#
ORIGIN_CODE = {
    0: 'IGP',
    1: 'EGP',
    2: 'INCOMPLETE'
}
# BGP UPDATE CODES
OPEN = 1
UPDATE = 2
NOTIFICATION = 3
KEEPALIVE = 4
#
AS_PATH_SEGMENT_CODE = {
    1: 'AS_SET',
    2: 'AS_SEQUENCE'
}