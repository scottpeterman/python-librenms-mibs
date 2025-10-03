# SNMP MIB module (VIPTELA-BFD) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\viptela\VIPTELA-BFD
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:59 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(viptela,) = mibBuilder.importSymbols(
    "VIPTELA-GLOBAL",
    "viptela")


# MODULE-IDENTITY

viptela_bfd = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 6)
)
if mibBuilder.loadTexts:
    viptela_bfd.setRevisions(
        ("2020-07-01 00:00",
         "2020-02-24 00:00",
         "2019-11-15 00:00",
         "2019-08-15 00:00",
         "2018-11-01 00:00",
         "2018-08-20 00:00",
         "2018-06-25 00:00",
         "2018-04-25 00:00",
         "2018-03-15 00:00",
         "2018-01-16 00:00",
         "2017-11-01 00:00",
         "2017-08-01 00:00",
         "2017-05-25 00:00",
         "2017-04-06 00:00",
         "2017-02-15 00:00",
         "2017-02-06 00:00",
         "2016-11-16 00:00",
         "2016-10-25 00:00",
         "2016-10-24 00:00",
         "2016-08-10 00:00",
         "2016-08-01 00:00",
         "2016-06-09 00:00",
         "2016-04-22 00:00",
         "2016-03-15 00:00",
         "2016-01-30 00:00",
         "2015-12-28 00:00",
         "2015-12-01 00:00",
         "2015-10-31 00:00",
         "2015-09-27 00:00",
         "2015-09-01 00:00",
         "2015-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class InetAddressIP(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class BfdmgrStateEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("admin-down", 0),
          ("down", 1),
          ("init", 2),
          ("up", 3),
          ("invalid", 4),
          ("inactive", 5))
    )



# MIB Managed Objects in the order of their OIDs

_Bfd_ObjectIdentity = ObjectIdentity
bfd = _Bfd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1)
)
_BfdSessionsListTable_Object = MibTable
bfdSessionsListTable = _BfdSessionsListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 1)
)
if mibBuilder.loadTexts:
    bfdSessionsListTable.setStatus("current")
_BfdSessionsListEntry_Object = MibTableRow
bfdSessionsListEntry = _BfdSessionsListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 1, 1)
)
bfdSessionsListEntry.setIndexNames(
    (0, "VIPTELA-BFD", "bfdSessionsListSrcIp"),
    (0, "VIPTELA-BFD", "bfdSessionsListDstIp"),
    (0, "VIPTELA-BFD", "bfdSessionsListProto"),
    (0, "VIPTELA-BFD", "bfdSessionsListSrcPort"),
    (0, "VIPTELA-BFD", "bfdSessionsListDstPort"),
)
if mibBuilder.loadTexts:
    bfdSessionsListEntry.setStatus("current")
_BfdSessionsListSrcIp_Type = InetAddressIP
_BfdSessionsListSrcIp_Object = MibTableColumn
bfdSessionsListSrcIp = _BfdSessionsListSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 1, 1, 1),
    _BfdSessionsListSrcIp_Type()
)
bfdSessionsListSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdSessionsListSrcIp.setStatus("current")
_BfdSessionsListDstIp_Type = InetAddressIP
_BfdSessionsListDstIp_Object = MibTableColumn
bfdSessionsListDstIp = _BfdSessionsListDstIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 1, 1, 2),
    _BfdSessionsListDstIp_Type()
)
bfdSessionsListDstIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdSessionsListDstIp.setStatus("current")


class _BfdSessionsListProto_Type(Integer32):
    """Custom type bfdSessionsListProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_BfdSessionsListProto_Type.__name__ = "Integer32"
_BfdSessionsListProto_Object = MibTableColumn
bfdSessionsListProto = _BfdSessionsListProto_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 1, 1, 3),
    _BfdSessionsListProto_Type()
)
bfdSessionsListProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdSessionsListProto.setStatus("current")
_BfdSessionsListSrcPort_Type = UnsignedShort
_BfdSessionsListSrcPort_Object = MibTableColumn
bfdSessionsListSrcPort = _BfdSessionsListSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 1, 1, 4),
    _BfdSessionsListSrcPort_Type()
)
bfdSessionsListSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdSessionsListSrcPort.setStatus("current")
_BfdSessionsListDstPort_Type = UnsignedShort
_BfdSessionsListDstPort_Object = MibTableColumn
bfdSessionsListDstPort = _BfdSessionsListDstPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 1, 1, 5),
    _BfdSessionsListDstPort_Type()
)
bfdSessionsListDstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdSessionsListDstPort.setStatus("current")
_BfdSessionsListSystemIp_Type = InetAddressIP
_BfdSessionsListSystemIp_Object = MibTableColumn
bfdSessionsListSystemIp = _BfdSessionsListSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 1, 1, 6),
    _BfdSessionsListSystemIp_Type()
)
bfdSessionsListSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessionsListSystemIp.setStatus("current")
_BfdSessionsListSiteId_Type = Unsigned32
_BfdSessionsListSiteId_Object = MibTableColumn
bfdSessionsListSiteId = _BfdSessionsListSiteId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 1, 1, 7),
    _BfdSessionsListSiteId_Type()
)
bfdSessionsListSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessionsListSiteId.setStatus("current")


class _BfdSessionsListLocalColor_Type(Integer32):
    """Custom type bfdSessionsListLocalColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_BfdSessionsListLocalColor_Type.__name__ = "Integer32"
_BfdSessionsListLocalColor_Object = MibTableColumn
bfdSessionsListLocalColor = _BfdSessionsListLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 1, 1, 8),
    _BfdSessionsListLocalColor_Type()
)
bfdSessionsListLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessionsListLocalColor.setStatus("current")


class _BfdSessionsListColor_Type(Integer32):
    """Custom type bfdSessionsListColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_BfdSessionsListColor_Type.__name__ = "Integer32"
_BfdSessionsListColor_Object = MibTableColumn
bfdSessionsListColor = _BfdSessionsListColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 1, 1, 9),
    _BfdSessionsListColor_Type()
)
bfdSessionsListColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessionsListColor.setStatus("current")
_BfdSessionsListState_Type = BfdmgrStateEnum
_BfdSessionsListState_Object = MibTableColumn
bfdSessionsListState = _BfdSessionsListState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 1, 1, 10),
    _BfdSessionsListState_Type()
)
bfdSessionsListState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessionsListState.setStatus("current")
_BfdSessionsListDetectMultiplier_Type = UnsignedByte
_BfdSessionsListDetectMultiplier_Object = MibTableColumn
bfdSessionsListDetectMultiplier = _BfdSessionsListDetectMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 1, 1, 11),
    _BfdSessionsListDetectMultiplier_Type()
)
bfdSessionsListDetectMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessionsListDetectMultiplier.setStatus("current")
_BfdSessionsListTxInterval_Type = Unsigned32
_BfdSessionsListTxInterval_Object = MibTableColumn
bfdSessionsListTxInterval = _BfdSessionsListTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 1, 1, 12),
    _BfdSessionsListTxInterval_Type()
)
bfdSessionsListTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessionsListTxInterval.setStatus("current")
_BfdSessionsListUptime_Type = String
_BfdSessionsListUptime_Object = MibTableColumn
bfdSessionsListUptime = _BfdSessionsListUptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 1, 1, 13),
    _BfdSessionsListUptime_Type()
)
bfdSessionsListUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessionsListUptime.setStatus("current")
_BfdSessionsListTransitions_Type = Integer32
_BfdSessionsListTransitions_Object = MibTableColumn
bfdSessionsListTransitions = _BfdSessionsListTransitions_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 1, 1, 14),
    _BfdSessionsListTransitions_Type()
)
bfdSessionsListTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessionsListTransitions.setStatus("current")
_BfdHistoryListTable_Object = MibTable
bfdHistoryListTable = _BfdHistoryListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 2)
)
if mibBuilder.loadTexts:
    bfdHistoryListTable.setStatus("current")
_BfdHistoryListEntry_Object = MibTableRow
bfdHistoryListEntry = _BfdHistoryListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 2, 1)
)
bfdHistoryListEntry.setIndexNames(
    (0, "VIPTELA-BFD", "bfdHistoryListSrcIp"),
    (0, "VIPTELA-BFD", "bfdHistoryListDstIp"),
    (0, "VIPTELA-BFD", "bfdHistoryListProto"),
    (0, "VIPTELA-BFD", "bfdHistoryListSrcPort"),
    (0, "VIPTELA-BFD", "bfdHistoryListDstPort"),
    (0, "VIPTELA-BFD", "bfdHistoryListIndex"),
)
if mibBuilder.loadTexts:
    bfdHistoryListEntry.setStatus("current")
_BfdHistoryListSrcIp_Type = InetAddressIP
_BfdHistoryListSrcIp_Object = MibTableColumn
bfdHistoryListSrcIp = _BfdHistoryListSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 2, 1, 1),
    _BfdHistoryListSrcIp_Type()
)
bfdHistoryListSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdHistoryListSrcIp.setStatus("current")
_BfdHistoryListDstIp_Type = InetAddressIP
_BfdHistoryListDstIp_Object = MibTableColumn
bfdHistoryListDstIp = _BfdHistoryListDstIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 2, 1, 2),
    _BfdHistoryListDstIp_Type()
)
bfdHistoryListDstIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdHistoryListDstIp.setStatus("current")


class _BfdHistoryListProto_Type(Integer32):
    """Custom type bfdHistoryListProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_BfdHistoryListProto_Type.__name__ = "Integer32"
_BfdHistoryListProto_Object = MibTableColumn
bfdHistoryListProto = _BfdHistoryListProto_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 2, 1, 3),
    _BfdHistoryListProto_Type()
)
bfdHistoryListProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdHistoryListProto.setStatus("current")
_BfdHistoryListSrcPort_Type = UnsignedShort
_BfdHistoryListSrcPort_Object = MibTableColumn
bfdHistoryListSrcPort = _BfdHistoryListSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 2, 1, 4),
    _BfdHistoryListSrcPort_Type()
)
bfdHistoryListSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdHistoryListSrcPort.setStatus("current")
_BfdHistoryListDstPort_Type = UnsignedShort
_BfdHistoryListDstPort_Object = MibTableColumn
bfdHistoryListDstPort = _BfdHistoryListDstPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 2, 1, 5),
    _BfdHistoryListDstPort_Type()
)
bfdHistoryListDstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdHistoryListDstPort.setStatus("current")
_BfdHistoryListIndex_Type = Unsigned32
_BfdHistoryListIndex_Object = MibTableColumn
bfdHistoryListIndex = _BfdHistoryListIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 2, 1, 6),
    _BfdHistoryListIndex_Type()
)
bfdHistoryListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdHistoryListIndex.setStatus("current")
_BfdHistoryListSystemIp_Type = InetAddressIP
_BfdHistoryListSystemIp_Object = MibTableColumn
bfdHistoryListSystemIp = _BfdHistoryListSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 2, 1, 7),
    _BfdHistoryListSystemIp_Type()
)
bfdHistoryListSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdHistoryListSystemIp.setStatus("current")
_BfdHistoryListSiteId_Type = Unsigned32
_BfdHistoryListSiteId_Object = MibTableColumn
bfdHistoryListSiteId = _BfdHistoryListSiteId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 2, 1, 8),
    _BfdHistoryListSiteId_Type()
)
bfdHistoryListSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdHistoryListSiteId.setStatus("current")


class _BfdHistoryListColor_Type(Integer32):
    """Custom type bfdHistoryListColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_BfdHistoryListColor_Type.__name__ = "Integer32"
_BfdHistoryListColor_Object = MibTableColumn
bfdHistoryListColor = _BfdHistoryListColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 2, 1, 9),
    _BfdHistoryListColor_Type()
)
bfdHistoryListColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdHistoryListColor.setStatus("current")
_BfdHistoryListState_Type = BfdmgrStateEnum
_BfdHistoryListState_Object = MibTableColumn
bfdHistoryListState = _BfdHistoryListState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 2, 1, 10),
    _BfdHistoryListState_Type()
)
bfdHistoryListState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdHistoryListState.setStatus("current")
_BfdHistoryListTime_Type = String
_BfdHistoryListTime_Object = MibTableColumn
bfdHistoryListTime = _BfdHistoryListTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 2, 1, 11),
    _BfdHistoryListTime_Type()
)
bfdHistoryListTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdHistoryListTime.setStatus("current")
_BfdHistoryListRxPkts_Type = Counter64
_BfdHistoryListRxPkts_Object = MibTableColumn
bfdHistoryListRxPkts = _BfdHistoryListRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 2, 1, 12),
    _BfdHistoryListRxPkts_Type()
)
bfdHistoryListRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdHistoryListRxPkts.setStatus("current")
_BfdHistoryListTxPkts_Type = Counter64
_BfdHistoryListTxPkts_Object = MibTableColumn
bfdHistoryListTxPkts = _BfdHistoryListTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 2, 1, 13),
    _BfdHistoryListTxPkts_Type()
)
bfdHistoryListTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdHistoryListTxPkts.setStatus("current")
_BfdHistoryListDel_Type = UnsignedByte
_BfdHistoryListDel_Object = MibTableColumn
bfdHistoryListDel = _BfdHistoryListDel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 2, 1, 14),
    _BfdHistoryListDel_Type()
)
bfdHistoryListDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdHistoryListDel.setStatus("current")
_BfdSummary_ObjectIdentity = ObjectIdentity
bfdSummary = _BfdSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 5)
)
_BfdSummaryBfdSessionsTotal_Type = Unsigned32
_BfdSummaryBfdSessionsTotal_Object = MibScalar
bfdSummaryBfdSessionsTotal = _BfdSummaryBfdSessionsTotal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 5, 1),
    _BfdSummaryBfdSessionsTotal_Type()
)
bfdSummaryBfdSessionsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSummaryBfdSessionsTotal.setStatus("current")
_BfdSummaryBfdSessionsUp_Type = Unsigned32
_BfdSummaryBfdSessionsUp_Object = MibScalar
bfdSummaryBfdSessionsUp = _BfdSummaryBfdSessionsUp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 5, 2),
    _BfdSummaryBfdSessionsUp_Type()
)
bfdSummaryBfdSessionsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSummaryBfdSessionsUp.setStatus("current")
_BfdSummaryBfdSessionsMax_Type = Unsigned32
_BfdSummaryBfdSessionsMax_Object = MibScalar
bfdSummaryBfdSessionsMax = _BfdSummaryBfdSessionsMax_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 5, 3),
    _BfdSummaryBfdSessionsMax_Type()
)
bfdSummaryBfdSessionsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSummaryBfdSessionsMax.setStatus("current")
_BfdSummaryBfdSessionsFlap_Type = Unsigned32
_BfdSummaryBfdSessionsFlap_Object = MibScalar
bfdSummaryBfdSessionsFlap = _BfdSummaryBfdSessionsFlap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 5, 4),
    _BfdSummaryBfdSessionsFlap_Type()
)
bfdSummaryBfdSessionsFlap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSummaryBfdSessionsFlap.setStatus("current")
_BfdSummaryPollInterval_Type = Unsigned32
_BfdSummaryPollInterval_Object = MibScalar
bfdSummaryPollInterval = _BfdSummaryPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 5, 5),
    _BfdSummaryPollInterval_Type()
)
bfdSummaryPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSummaryPollInterval.setStatus("current")
_BfdTlocSummaryListTable_Object = MibTable
bfdTlocSummaryListTable = _BfdTlocSummaryListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 6)
)
if mibBuilder.loadTexts:
    bfdTlocSummaryListTable.setStatus("current")
_BfdTlocSummaryListEntry_Object = MibTableRow
bfdTlocSummaryListEntry = _BfdTlocSummaryListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 6, 1)
)
bfdTlocSummaryListEntry.setIndexNames(
    (0, "VIPTELA-BFD", "bfdTlocSummaryListIfName"),
    (0, "VIPTELA-BFD", "bfdTlocSummaryListEncap"),
)
if mibBuilder.loadTexts:
    bfdTlocSummaryListEntry.setStatus("current")


class _BfdTlocSummaryListIfName_Type(String):
    """Custom type bfdTlocSummaryListIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BfdTlocSummaryListIfName_Type.__name__ = "String"
_BfdTlocSummaryListIfName_Object = MibTableColumn
bfdTlocSummaryListIfName = _BfdTlocSummaryListIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 6, 1, 1),
    _BfdTlocSummaryListIfName_Type()
)
bfdTlocSummaryListIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdTlocSummaryListIfName.setStatus("current")


class _BfdTlocSummaryListEncap_Type(Integer32):
    """Custom type bfdTlocSummaryListEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_BfdTlocSummaryListEncap_Type.__name__ = "Integer32"
_BfdTlocSummaryListEncap_Object = MibTableColumn
bfdTlocSummaryListEncap = _BfdTlocSummaryListEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 6, 1, 2),
    _BfdTlocSummaryListEncap_Type()
)
bfdTlocSummaryListEncap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdTlocSummaryListEncap.setStatus("current")
_BfdTlocSummaryListSessionsTotal_Type = Unsigned32
_BfdTlocSummaryListSessionsTotal_Object = MibTableColumn
bfdTlocSummaryListSessionsTotal = _BfdTlocSummaryListSessionsTotal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 6, 1, 3),
    _BfdTlocSummaryListSessionsTotal_Type()
)
bfdTlocSummaryListSessionsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdTlocSummaryListSessionsTotal.setStatus("current")
_BfdTlocSummaryListSessionsUp_Type = Unsigned32
_BfdTlocSummaryListSessionsUp_Object = MibTableColumn
bfdTlocSummaryListSessionsUp = _BfdTlocSummaryListSessionsUp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 6, 1, 4),
    _BfdTlocSummaryListSessionsUp_Type()
)
bfdTlocSummaryListSessionsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdTlocSummaryListSessionsUp.setStatus("current")
_BfdTlocSummaryListSessionsFlap_Type = Unsigned32
_BfdTlocSummaryListSessionsFlap_Object = MibTableColumn
bfdTlocSummaryListSessionsFlap = _BfdTlocSummaryListSessionsFlap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 6, 1, 6, 1, 5),
    _BfdTlocSummaryListSessionsFlap_Type()
)
bfdTlocSummaryListSessionsFlap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdTlocSummaryListSessionsFlap.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIPTELA-BFD",
    **{"InetAddressIP": InetAddressIP,
       "UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "ConfdString": ConfdString,
       "String": String,
       "BfdmgrStateEnum": BfdmgrStateEnum,
       "viptela-bfd": viptela_bfd,
       "bfd": bfd,
       "bfdSessionsListTable": bfdSessionsListTable,
       "bfdSessionsListEntry": bfdSessionsListEntry,
       "bfdSessionsListSrcIp": bfdSessionsListSrcIp,
       "bfdSessionsListDstIp": bfdSessionsListDstIp,
       "bfdSessionsListProto": bfdSessionsListProto,
       "bfdSessionsListSrcPort": bfdSessionsListSrcPort,
       "bfdSessionsListDstPort": bfdSessionsListDstPort,
       "bfdSessionsListSystemIp": bfdSessionsListSystemIp,
       "bfdSessionsListSiteId": bfdSessionsListSiteId,
       "bfdSessionsListLocalColor": bfdSessionsListLocalColor,
       "bfdSessionsListColor": bfdSessionsListColor,
       "bfdSessionsListState": bfdSessionsListState,
       "bfdSessionsListDetectMultiplier": bfdSessionsListDetectMultiplier,
       "bfdSessionsListTxInterval": bfdSessionsListTxInterval,
       "bfdSessionsListUptime": bfdSessionsListUptime,
       "bfdSessionsListTransitions": bfdSessionsListTransitions,
       "bfdHistoryListTable": bfdHistoryListTable,
       "bfdHistoryListEntry": bfdHistoryListEntry,
       "bfdHistoryListSrcIp": bfdHistoryListSrcIp,
       "bfdHistoryListDstIp": bfdHistoryListDstIp,
       "bfdHistoryListProto": bfdHistoryListProto,
       "bfdHistoryListSrcPort": bfdHistoryListSrcPort,
       "bfdHistoryListDstPort": bfdHistoryListDstPort,
       "bfdHistoryListIndex": bfdHistoryListIndex,
       "bfdHistoryListSystemIp": bfdHistoryListSystemIp,
       "bfdHistoryListSiteId": bfdHistoryListSiteId,
       "bfdHistoryListColor": bfdHistoryListColor,
       "bfdHistoryListState": bfdHistoryListState,
       "bfdHistoryListTime": bfdHistoryListTime,
       "bfdHistoryListRxPkts": bfdHistoryListRxPkts,
       "bfdHistoryListTxPkts": bfdHistoryListTxPkts,
       "bfdHistoryListDel": bfdHistoryListDel,
       "bfdSummary": bfdSummary,
       "bfdSummaryBfdSessionsTotal": bfdSummaryBfdSessionsTotal,
       "bfdSummaryBfdSessionsUp": bfdSummaryBfdSessionsUp,
       "bfdSummaryBfdSessionsMax": bfdSummaryBfdSessionsMax,
       "bfdSummaryBfdSessionsFlap": bfdSummaryBfdSessionsFlap,
       "bfdSummaryPollInterval": bfdSummaryPollInterval,
       "bfdTlocSummaryListTable": bfdTlocSummaryListTable,
       "bfdTlocSummaryListEntry": bfdTlocSummaryListEntry,
       "bfdTlocSummaryListIfName": bfdTlocSummaryListIfName,
       "bfdTlocSummaryListEncap": bfdTlocSummaryListEncap,
       "bfdTlocSummaryListSessionsTotal": bfdTlocSummaryListSessionsTotal,
       "bfdTlocSummaryListSessionsUp": bfdTlocSummaryListSessionsUp,
       "bfdTlocSummaryListSessionsFlap": bfdTlocSummaryListSessionsFlap}
)
