# SNMP MIB module (HH3C-FLEXE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-FLEXE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:31:43 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cFlexE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177)
)
if mibBuilder.loadTexts:
    hh3cFlexE.setRevisions(
        ("2019-04-03 19:36",
         "2018-08-03 14:36")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cFlexESubSlotInfo_ObjectIdentity = ObjectIdentity
hh3cFlexESubSlotInfo = _Hh3cFlexESubSlotInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 1)
)
_Hh3cFlexESubSlotTable_Object = MibTable
hh3cFlexESubSlotTable = _Hh3cFlexESubSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cFlexESubSlotTable.setStatus("current")
_Hh3cFlexESubSlotEntry_Object = MibTableRow
hh3cFlexESubSlotEntry = _Hh3cFlexESubSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 1, 1, 1)
)
hh3cFlexESubSlotEntry.setIndexNames(
    (0, "HH3C-FLEXE-MIB", "hh3cFlexEFrameIndex"),
    (0, "HH3C-FLEXE-MIB", "hh3cFlexESlotIndex"),
    (0, "HH3C-FLEXE-MIB", "hh3cFlexESubslotIndex"),
)
if mibBuilder.loadTexts:
    hh3cFlexESubSlotEntry.setStatus("current")


class _Hh3cFlexEFrameIndex_Type(Integer32):
    """Custom type hh3cFlexEFrameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cFlexEFrameIndex_Type.__name__ = "Integer32"
_Hh3cFlexEFrameIndex_Object = MibTableColumn
hh3cFlexEFrameIndex = _Hh3cFlexEFrameIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 1, 1, 1, 1),
    _Hh3cFlexEFrameIndex_Type()
)
hh3cFlexEFrameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlexEFrameIndex.setStatus("current")


class _Hh3cFlexESlotIndex_Type(Integer32):
    """Custom type hh3cFlexESlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cFlexESlotIndex_Type.__name__ = "Integer32"
_Hh3cFlexESlotIndex_Object = MibTableColumn
hh3cFlexESlotIndex = _Hh3cFlexESlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 1, 1, 1, 2),
    _Hh3cFlexESlotIndex_Type()
)
hh3cFlexESlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlexESlotIndex.setStatus("current")


class _Hh3cFlexESubslotIndex_Type(Integer32):
    """Custom type hh3cFlexESubslotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cFlexESubslotIndex_Type.__name__ = "Integer32"
_Hh3cFlexESubslotIndex_Object = MibTableColumn
hh3cFlexESubslotIndex = _Hh3cFlexESubslotIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 1, 1, 1, 3),
    _Hh3cFlexESubslotIndex_Type()
)
hh3cFlexESubslotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlexESubslotIndex.setStatus("current")
_Hh3cFlexESubTimeSlotGranular_Type = Integer32
_Hh3cFlexESubTimeSlotGranular_Object = MibTableColumn
hh3cFlexESubTimeSlotGranular = _Hh3cFlexESubTimeSlotGranular_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 1, 1, 1, 4),
    _Hh3cFlexESubTimeSlotGranular_Type()
)
hh3cFlexESubTimeSlotGranular.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFlexESubTimeSlotGranular.setStatus("current")
_Hh3cFlexEGroupTable_Object = MibTable
hh3cFlexEGroupTable = _Hh3cFlexEGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cFlexEGroupTable.setStatus("current")
_Hh3cFlexEGroupEntry_Object = MibTableRow
hh3cFlexEGroupEntry = _Hh3cFlexEGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 1, 2, 1)
)
hh3cFlexEGroupEntry.setIndexNames(
    (0, "HH3C-FLEXE-MIB", "hh3cFlexEFrameIndex"),
    (0, "HH3C-FLEXE-MIB", "hh3cFlexESlotIndex"),
    (0, "HH3C-FLEXE-MIB", "hh3cFlexESubslotIndex"),
    (0, "HH3C-FLEXE-MIB", "hh3cFlexEGroupID"),
)
if mibBuilder.loadTexts:
    hh3cFlexEGroupEntry.setStatus("current")


class _Hh3cFlexEGroupID_Type(Integer32):
    """Custom type hh3cFlexEGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048574),
    )


_Hh3cFlexEGroupID_Type.__name__ = "Integer32"
_Hh3cFlexEGroupID_Object = MibTableColumn
hh3cFlexEGroupID = _Hh3cFlexEGroupID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 1, 2, 1, 1),
    _Hh3cFlexEGroupID_Type()
)
hh3cFlexEGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlexEGroupID.setStatus("current")
_Hh3cFlexEGroupRowStatus_Type = RowStatus
_Hh3cFlexEGroupRowStatus_Object = MibTableColumn
hh3cFlexEGroupRowStatus = _Hh3cFlexEGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 1, 2, 1, 2),
    _Hh3cFlexEGroupRowStatus_Type()
)
hh3cFlexEGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlexEGroupRowStatus.setStatus("current")
_Hh3cFlexEPhyIfTable_Object = MibTable
hh3cFlexEPhyIfTable = _Hh3cFlexEPhyIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 2)
)
if mibBuilder.loadTexts:
    hh3cFlexEPhyIfTable.setStatus("current")
_Hh3cFlexEPhyIfEntry_Object = MibTableRow
hh3cFlexEPhyIfEntry = _Hh3cFlexEPhyIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 2, 1)
)
hh3cFlexEPhyIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cFlexEPhyIfEntry.setStatus("current")


class _Hh3cFlexEPhyGroupID_Type(Integer32):
    """Custom type hh3cFlexEPhyGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048574),
    )


_Hh3cFlexEPhyGroupID_Type.__name__ = "Integer32"
_Hh3cFlexEPhyGroupID_Object = MibTableColumn
hh3cFlexEPhyGroupID = _Hh3cFlexEPhyGroupID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 2, 1, 1),
    _Hh3cFlexEPhyGroupID_Type()
)
hh3cFlexEPhyGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFlexEPhyGroupID.setStatus("current")


class _Hh3cFlexEPhyNumber_Type(Integer32):
    """Custom type hh3cFlexEPhyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 254),
    )


_Hh3cFlexEPhyNumber_Type.__name__ = "Integer32"
_Hh3cFlexEPhyNumber_Object = MibTableColumn
hh3cFlexEPhyNumber = _Hh3cFlexEPhyNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 2, 1, 2),
    _Hh3cFlexEPhyNumber_Type()
)
hh3cFlexEPhyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFlexEPhyNumber.setStatus("current")


class _Hh3cFlexEClockPort_Type(OctetString):
    """Custom type hh3cFlexEClockPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_Hh3cFlexEClockPort_Type.__name__ = "OctetString"
_Hh3cFlexEClockPort_Object = MibTableColumn
hh3cFlexEClockPort = _Hh3cFlexEClockPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 2, 1, 3),
    _Hh3cFlexEClockPort_Type()
)
hh3cFlexEClockPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFlexEClockPort.setStatus("current")
_Hh3cFlexEIfTable_Object = MibTable
hh3cFlexEIfTable = _Hh3cFlexEIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 3)
)
if mibBuilder.loadTexts:
    hh3cFlexEIfTable.setStatus("current")
_Hh3cFlexEIfEntry_Object = MibTableRow
hh3cFlexEIfEntry = _Hh3cFlexEIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 3, 1)
)
hh3cFlexEIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cFlexEIfEntry.setStatus("current")


class _Hh3cFlexEIfGroupID_Type(Integer32):
    """Custom type hh3cFlexEIfGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048574),
    )


_Hh3cFlexEIfGroupID_Type.__name__ = "Integer32"
_Hh3cFlexEIfGroupID_Object = MibTableColumn
hh3cFlexEIfGroupID = _Hh3cFlexEIfGroupID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 3, 1, 1),
    _Hh3cFlexEIfGroupID_Type()
)
hh3cFlexEIfGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFlexEIfGroupID.setStatus("current")
_Hh3cFlexEBandwidth_Type = Integer32
_Hh3cFlexEBandwidth_Object = MibTableColumn
hh3cFlexEBandwidth = _Hh3cFlexEBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 3, 1, 2),
    _Hh3cFlexEBandwidth_Type()
)
hh3cFlexEBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFlexEBandwidth.setStatus("current")


class _Hh3cFlexEClientID_Type(Integer32):
    """Custom type hh3cFlexEClientID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_Hh3cFlexEClientID_Type.__name__ = "Integer32"
_Hh3cFlexEClientID_Object = MibTableColumn
hh3cFlexEClientID = _Hh3cFlexEClientID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 3, 1, 3),
    _Hh3cFlexEClientID_Type()
)
hh3cFlexEClientID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFlexEClientID.setStatus("current")


class _Hh3cFlexEMinAvailableBandwidth_Type(Integer32):
    """Custom type hh3cFlexEMinAvailableBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_Hh3cFlexEMinAvailableBandwidth_Type.__name__ = "Integer32"
_Hh3cFlexEMinAvailableBandwidth_Object = MibTableColumn
hh3cFlexEMinAvailableBandwidth = _Hh3cFlexEMinAvailableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 3, 1, 4),
    _Hh3cFlexEMinAvailableBandwidth_Type()
)
hh3cFlexEMinAvailableBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFlexEMinAvailableBandwidth.setStatus("current")
_Hh3cFlexETrapObjects_ObjectIdentity = ObjectIdentity
hh3cFlexETrapObjects = _Hh3cFlexETrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 4)
)
_Hh3cFlexERemotePhyNumber_Type = Integer32
_Hh3cFlexERemotePhyNumber_Object = MibScalar
hh3cFlexERemotePhyNumber = _Hh3cFlexERemotePhyNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 4, 1),
    _Hh3cFlexERemotePhyNumber_Type()
)
hh3cFlexERemotePhyNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cFlexERemotePhyNumber.setStatus("current")
_Hh3cFlexERemotePhyGroupID_Type = Integer32
_Hh3cFlexERemotePhyGroupID_Object = MibScalar
hh3cFlexERemotePhyGroupID = _Hh3cFlexERemotePhyGroupID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 4, 2),
    _Hh3cFlexERemotePhyGroupID_Type()
)
hh3cFlexERemotePhyGroupID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cFlexERemotePhyGroupID.setStatus("current")
_Hh3cFlexEGroupMemberCount_Type = Integer32
_Hh3cFlexEGroupMemberCount_Object = MibScalar
hh3cFlexEGroupMemberCount = _Hh3cFlexEGroupMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 4, 3),
    _Hh3cFlexEGroupMemberCount_Type()
)
hh3cFlexEGroupMemberCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cFlexEGroupMemberCount.setStatus("current")
_Hh3cFlexEPortList_Type = OctetString
_Hh3cFlexEPortList_Object = MibScalar
hh3cFlexEPortList = _Hh3cFlexEPortList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 4, 4),
    _Hh3cFlexEPortList_Type()
)
hh3cFlexEPortList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cFlexEPortList.setStatus("current")
_Hh3cFlexETrap_ObjectIdentity = ObjectIdentity
hh3cFlexETrap = _Hh3cFlexETrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5)
)
_Hh3cFlexETrapPrex_ObjectIdentity = ObjectIdentity
hh3cFlexETrapPrex = _Hh3cFlexETrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0)
)

# Managed Objects groups


# Notification objects

hh3cFlexEPhyNumberMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 1)
)
hh3cFlexEPhyNumberMismatch.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-FLEXE-MIB", "hh3cFlexEPhyNumber"),
        ("HH3C-FLEXE-MIB", "hh3cFlexERemotePhyNumber"))
)
if mibBuilder.loadTexts:
    hh3cFlexEPhyNumberMismatch.setStatus(
        "current"
    )

hh3cFlexEPhyNumberMismatchRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 2)
)
hh3cFlexEPhyNumberMismatchRecover.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-FLEXE-MIB", "hh3cFlexEPhyNumber"),
        ("HH3C-FLEXE-MIB", "hh3cFlexERemotePhyNumber"))
)
if mibBuilder.loadTexts:
    hh3cFlexEPhyNumberMismatchRecover.setStatus(
        "current"
    )

hh3cFlexEPhyGroupMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 3)
)
hh3cFlexEPhyGroupMismatch.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-FLEXE-MIB", "hh3cFlexEPhyGroupID"),
        ("HH3C-FLEXE-MIB", "hh3cFlexERemotePhyGroupID"))
)
if mibBuilder.loadTexts:
    hh3cFlexEPhyGroupMismatch.setStatus(
        "current"
    )

hh3cFlexEPhyGroupMismatchRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 4)
)
hh3cFlexEPhyGroupMismatchRecover.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-FLEXE-MIB", "hh3cFlexEPhyGroupID"),
        ("HH3C-FLEXE-MIB", "hh3cFlexERemotePhyGroupID"))
)
if mibBuilder.loadTexts:
    hh3cFlexEPhyGroupMismatchRecover.setStatus(
        "current"
    )

hh3cFlexEClientIDMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 5)
)
hh3cFlexEClientIDMismatch.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cFlexEClientIDMismatch.setStatus(
        "current"
    )

hh3cFlexEClientIDMismatchRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 6)
)
hh3cFlexEClientIDMismatchRecover.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cFlexEClientIDMismatchRecover.setStatus(
        "current"
    )

hh3cFlexEBandwidthReduce = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 7)
)
hh3cFlexEBandwidthReduce.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-FLEXE-MIB", "hh3cFlexEBandwidth"))
)
if mibBuilder.loadTexts:
    hh3cFlexEBandwidthReduce.setStatus(
        "current"
    )

hh3cFlexEBandwidthReduceRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 8)
)
hh3cFlexEBandwidthReduceRecover.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-FLEXE-MIB", "hh3cFlexEBandwidth"))
)
if mibBuilder.loadTexts:
    hh3cFlexEBandwidthReduceRecover.setStatus(
        "current"
    )

hh3cFlexEPhyFcsSdAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 9)
)
hh3cFlexEPhyFcsSdAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cFlexEPhyFcsSdAlarm.setStatus(
        "current"
    )

hh3cFlexEPhyFcsSdAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 10)
)
hh3cFlexEPhyFcsSdAlarmRecover.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cFlexEPhyFcsSdAlarmRecover.setStatus(
        "current"
    )

hh3cFlexEPhyLocalFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 11)
)
hh3cFlexEPhyLocalFault.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cFlexEPhyLocalFault.setStatus(
        "current"
    )

hh3cFlexEPhyLocalFaultRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 12)
)
hh3cFlexEPhyLocalFaultRecover.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cFlexEPhyLocalFaultRecover.setStatus(
        "current"
    )

hh3cFlexEPhyRemoteFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 13)
)
hh3cFlexEPhyRemoteFault.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cFlexEPhyRemoteFault.setStatus(
        "current"
    )

hh3cFlexEPhyRemoteFaultRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 14)
)
hh3cFlexEPhyRemoteFaultRecover.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cFlexEPhyRemoteFaultRecover.setStatus(
        "current"
    )

hh3cFlexEBandwidthMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 15)
)
hh3cFlexEBandwidthMismatch.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cFlexEBandwidthMismatch.setStatus(
        "current"
    )

hh3cFlexEBandwidthMismatchRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 16)
)
hh3cFlexEBandwidthMismatchRecover.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cFlexEBandwidthMismatchRecover.setStatus(
        "current"
    )

hh3cFlexEPhyDelayOverAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 17)
)
hh3cFlexEPhyDelayOverAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-FLEXE-MIB", "hh3cFlexEPortList"))
)
if mibBuilder.loadTexts:
    hh3cFlexEPhyDelayOverAlarm.setStatus(
        "current"
    )

hh3cFlexEPhyDelayOverAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 18)
)
hh3cFlexEPhyDelayOverAlarmRecover.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-FLEXE-MIB", "hh3cFlexEPortList"))
)
if mibBuilder.loadTexts:
    hh3cFlexEPhyDelayOverAlarmRecover.setStatus(
        "current"
    )

hh3cFlexESTSGMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 19)
)
hh3cFlexESTSGMismatch.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-FLEXE-MIB", "hh3cFlexESubTimeSlotGranular"))
)
if mibBuilder.loadTexts:
    hh3cFlexESTSGMismatch.setStatus(
        "current"
    )

hh3cFlexESTSGMismatchRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 20)
)
hh3cFlexESTSGMismatchRecover.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-FLEXE-MIB", "hh3cFlexESubTimeSlotGranular"))
)
if mibBuilder.loadTexts:
    hh3cFlexESTSGMismatchRecover.setStatus(
        "current"
    )

hh3cFlexEGroupMemberFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 21)
)
hh3cFlexEGroupMemberFault.setObjects(
      *(("HH3C-FLEXE-MIB", "hh3cFlexEFrameIndex"),
        ("HH3C-FLEXE-MIB", "hh3cFlexESlotIndex"),
        ("HH3C-FLEXE-MIB", "hh3cFlexESubslotIndex"),
        ("HH3C-FLEXE-MIB", "hh3cFlexEGroupID"),
        ("HH3C-FLEXE-MIB", "hh3cFlexEGroupMemberCount"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cFlexEGroupMemberFault.setStatus(
        "current"
    )

hh3cFlexEGroupMemberFaultRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 22)
)
hh3cFlexEGroupMemberFaultRecover.setObjects(
      *(("HH3C-FLEXE-MIB", "hh3cFlexEFrameIndex"),
        ("HH3C-FLEXE-MIB", "hh3cFlexESlotIndex"),
        ("HH3C-FLEXE-MIB", "hh3cFlexESubslotIndex"),
        ("HH3C-FLEXE-MIB", "hh3cFlexEGroupID"),
        ("HH3C-FLEXE-MIB", "hh3cFlexEGroupMemberCount"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cFlexEGroupMemberFaultRecover.setStatus(
        "current"
    )

hh3cFlexEGroupFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 23)
)
hh3cFlexEGroupFaultAlarm.setObjects(
      *(("HH3C-FLEXE-MIB", "hh3cFlexEFrameIndex"),
        ("HH3C-FLEXE-MIB", "hh3cFlexESlotIndex"),
        ("HH3C-FLEXE-MIB", "hh3cFlexESubslotIndex"),
        ("HH3C-FLEXE-MIB", "hh3cFlexEGroupID"))
)
if mibBuilder.loadTexts:
    hh3cFlexEGroupFaultAlarm.setStatus(
        "current"
    )

hh3cFlexEGroupFaultAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 177, 5, 0, 24)
)
hh3cFlexEGroupFaultAlarmRecover.setObjects(
      *(("HH3C-FLEXE-MIB", "hh3cFlexEFrameIndex"),
        ("HH3C-FLEXE-MIB", "hh3cFlexESlotIndex"),
        ("HH3C-FLEXE-MIB", "hh3cFlexESubslotIndex"),
        ("HH3C-FLEXE-MIB", "hh3cFlexEGroupID"))
)
if mibBuilder.loadTexts:
    hh3cFlexEGroupFaultAlarmRecover.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FLEXE-MIB",
    **{"hh3cFlexE": hh3cFlexE,
       "hh3cFlexESubSlotInfo": hh3cFlexESubSlotInfo,
       "hh3cFlexESubSlotTable": hh3cFlexESubSlotTable,
       "hh3cFlexESubSlotEntry": hh3cFlexESubSlotEntry,
       "hh3cFlexEFrameIndex": hh3cFlexEFrameIndex,
       "hh3cFlexESlotIndex": hh3cFlexESlotIndex,
       "hh3cFlexESubslotIndex": hh3cFlexESubslotIndex,
       "hh3cFlexESubTimeSlotGranular": hh3cFlexESubTimeSlotGranular,
       "hh3cFlexEGroupTable": hh3cFlexEGroupTable,
       "hh3cFlexEGroupEntry": hh3cFlexEGroupEntry,
       "hh3cFlexEGroupID": hh3cFlexEGroupID,
       "hh3cFlexEGroupRowStatus": hh3cFlexEGroupRowStatus,
       "hh3cFlexEPhyIfTable": hh3cFlexEPhyIfTable,
       "hh3cFlexEPhyIfEntry": hh3cFlexEPhyIfEntry,
       "hh3cFlexEPhyGroupID": hh3cFlexEPhyGroupID,
       "hh3cFlexEPhyNumber": hh3cFlexEPhyNumber,
       "hh3cFlexEClockPort": hh3cFlexEClockPort,
       "hh3cFlexEIfTable": hh3cFlexEIfTable,
       "hh3cFlexEIfEntry": hh3cFlexEIfEntry,
       "hh3cFlexEIfGroupID": hh3cFlexEIfGroupID,
       "hh3cFlexEBandwidth": hh3cFlexEBandwidth,
       "hh3cFlexEClientID": hh3cFlexEClientID,
       "hh3cFlexEMinAvailableBandwidth": hh3cFlexEMinAvailableBandwidth,
       "hh3cFlexETrapObjects": hh3cFlexETrapObjects,
       "hh3cFlexERemotePhyNumber": hh3cFlexERemotePhyNumber,
       "hh3cFlexERemotePhyGroupID": hh3cFlexERemotePhyGroupID,
       "hh3cFlexEGroupMemberCount": hh3cFlexEGroupMemberCount,
       "hh3cFlexEPortList": hh3cFlexEPortList,
       "hh3cFlexETrap": hh3cFlexETrap,
       "hh3cFlexETrapPrex": hh3cFlexETrapPrex,
       "hh3cFlexEPhyNumberMismatch": hh3cFlexEPhyNumberMismatch,
       "hh3cFlexEPhyNumberMismatchRecover": hh3cFlexEPhyNumberMismatchRecover,
       "hh3cFlexEPhyGroupMismatch": hh3cFlexEPhyGroupMismatch,
       "hh3cFlexEPhyGroupMismatchRecover": hh3cFlexEPhyGroupMismatchRecover,
       "hh3cFlexEClientIDMismatch": hh3cFlexEClientIDMismatch,
       "hh3cFlexEClientIDMismatchRecover": hh3cFlexEClientIDMismatchRecover,
       "hh3cFlexEBandwidthReduce": hh3cFlexEBandwidthReduce,
       "hh3cFlexEBandwidthReduceRecover": hh3cFlexEBandwidthReduceRecover,
       "hh3cFlexEPhyFcsSdAlarm": hh3cFlexEPhyFcsSdAlarm,
       "hh3cFlexEPhyFcsSdAlarmRecover": hh3cFlexEPhyFcsSdAlarmRecover,
       "hh3cFlexEPhyLocalFault": hh3cFlexEPhyLocalFault,
       "hh3cFlexEPhyLocalFaultRecover": hh3cFlexEPhyLocalFaultRecover,
       "hh3cFlexEPhyRemoteFault": hh3cFlexEPhyRemoteFault,
       "hh3cFlexEPhyRemoteFaultRecover": hh3cFlexEPhyRemoteFaultRecover,
       "hh3cFlexEBandwidthMismatch": hh3cFlexEBandwidthMismatch,
       "hh3cFlexEBandwidthMismatchRecover": hh3cFlexEBandwidthMismatchRecover,
       "hh3cFlexEPhyDelayOverAlarm": hh3cFlexEPhyDelayOverAlarm,
       "hh3cFlexEPhyDelayOverAlarmRecover": hh3cFlexEPhyDelayOverAlarmRecover,
       "hh3cFlexESTSGMismatch": hh3cFlexESTSGMismatch,
       "hh3cFlexESTSGMismatchRecover": hh3cFlexESTSGMismatchRecover,
       "hh3cFlexEGroupMemberFault": hh3cFlexEGroupMemberFault,
       "hh3cFlexEGroupMemberFaultRecover": hh3cFlexEGroupMemberFaultRecover,
       "hh3cFlexEGroupFaultAlarm": hh3cFlexEGroupFaultAlarm,
       "hh3cFlexEGroupFaultAlarmRecover": hh3cFlexEGroupFaultAlarmRecover}
)
