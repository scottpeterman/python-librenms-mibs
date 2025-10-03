# SNMP MIB module (ISM-STORAGE-SVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\huawei\ISM-STORAGE-SVC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:59:55 2025
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 enterprises,
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
    "enterprises",
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

huaweistorage = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34774)
)
if mibBuilder.loadTexts:
    huaweistorage.setRevisions(
        ("2013-04-07 19:15",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NodeCodeString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 17),
    )



# MIB Managed Objects in the order of their OIDs

_HwStorage_ObjectIdentity = ObjectIdentity
hwStorage = _HwStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4)
)
_HwISM_ObjectIdentity = ObjectIdentity
hwISM = _HwISM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 1)
)
_DeviceId_Type = DisplayString
_DeviceId_Object = MibScalar
deviceId = _DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 1, 1),
    _DeviceId_Type()
)
deviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceId.setStatus("current")
_DeviceType_Type = Integer32
_DeviceType_Object = MibScalar
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 1, 2),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("current")
_Status_Type = Integer32
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 1, 3),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("current")
_UsedCapacity_Type = Counter64
_UsedCapacity_Object = MibScalar
usedCapacity = _UsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 1, 4),
    _UsedCapacity_Type()
)
usedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usedCapacity.setStatus("current")
_TotalCapacity_Type = Counter64
_TotalCapacity_Object = MibScalar
totalCapacity = _TotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 1, 5),
    _TotalCapacity_Type()
)
totalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalCapacity.setStatus("current")
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 1, 6),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_HwStorageService_ObjectIdentity = ObjectIdentity
hwStorageService = _HwStorageService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19)
)
_HwStoragePhysicalModule_ObjectIdentity = ObjectIdentity
hwStoragePhysicalModule = _HwStoragePhysicalModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8)
)
_HwStorageFCPortTable_Object = MibTable
hwStorageFCPortTable = _HwStorageFCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 7)
)
if mibBuilder.loadTexts:
    hwStorageFCPortTable.setStatus("current")
_HwStorageFCPortEntry_Object = MibTableRow
hwStorageFCPortEntry = _HwStorageFCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 7, 1)
)
hwStorageFCPortEntry.setIndexNames(
    (0, "ISM-STORAGE-SVC-MIB", "hwStorageFCPortIfIndex"),
)
if mibBuilder.loadTexts:
    hwStorageFCPortEntry.setStatus("current")
_HwStorageFCPortIfIndex_Type = Unsigned32
_HwStorageFCPortIfIndex_Object = MibTableColumn
hwStorageFCPortIfIndex = _HwStorageFCPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 7, 1, 1),
    _HwStorageFCPortIfIndex_Type()
)
hwStorageFCPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageFCPortIfIndex.setStatus("current")
_HwStorageFCPortBoardIfIndex_Type = Unsigned32
_HwStorageFCPortBoardIfIndex_Object = MibTableColumn
hwStorageFCPortBoardIfIndex = _HwStorageFCPortBoardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 7, 1, 2),
    _HwStorageFCPortBoardIfIndex_Type()
)
hwStorageFCPortBoardIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageFCPortBoardIfIndex.setStatus("current")
_HwStorageFCPortID_Type = Unsigned32
_HwStorageFCPortID_Object = MibTableColumn
hwStorageFCPortID = _HwStorageFCPortID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 7, 1, 3),
    _HwStorageFCPortID_Type()
)
hwStorageFCPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageFCPortID.setStatus("current")


class _HwStorageFCPortStatus_Type(Integer32):
    """Custom type hwStorageFCPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkdown", 0),
          ("linkup", 1),
          ("fault", 2))
    )


_HwStorageFCPortStatus_Type.__name__ = "Integer32"
_HwStorageFCPortStatus_Object = MibTableColumn
hwStorageFCPortStatus = _HwStorageFCPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 7, 1, 4),
    _HwStorageFCPortStatus_Type()
)
hwStorageFCPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageFCPortStatus.setStatus("current")


class _HwStorageFCPortConfigRate_Type(Integer32):
    """Custom type hwStorageFCPortConfigRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("gbps1", 1),
          ("gbps2", 2),
          ("gbps4", 4),
          ("gbps8", 8),
          ("gbps16", 16))
    )


_HwStorageFCPortConfigRate_Type.__name__ = "Integer32"
_HwStorageFCPortConfigRate_Object = MibTableColumn
hwStorageFCPortConfigRate = _HwStorageFCPortConfigRate_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 7, 1, 5),
    _HwStorageFCPortConfigRate_Type()
)
hwStorageFCPortConfigRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStorageFCPortConfigRate.setStatus("current")


class _HwStorageFCPortMode_Type(Integer32):
    """Custom type hwStorageFCPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fabric", 1),
          ("publicloop", 2),
          ("pointtopoint", 3))
    )


_HwStorageFCPortMode_Type.__name__ = "Integer32"
_HwStorageFCPortMode_Object = MibTableColumn
hwStorageFCPortMode = _HwStorageFCPortMode_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 7, 1, 6),
    _HwStorageFCPortMode_Type()
)
hwStorageFCPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStorageFCPortMode.setStatus("current")
_HwStorageFCPortWWN_Type = OctetString
_HwStorageFCPortWWN_Object = MibTableColumn
hwStorageFCPortWWN = _HwStorageFCPortWWN_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 7, 1, 7),
    _HwStorageFCPortWWN_Type()
)
hwStorageFCPortWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageFCPortWWN.setStatus("current")


class _HwStorageFCPortLogicType_Type(Integer32):
    """Custom type hwStorageFCPortLogicType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("service", 1),
          ("ibc", 2),
          ("ibs", 3),
          ("expansion", 4),
          ("management", 5),
          ("upsmanagement", 6),
          ("maintenance", 8))
    )


_HwStorageFCPortLogicType_Type.__name__ = "Integer32"
_HwStorageFCPortLogicType_Object = MibTableColumn
hwStorageFCPortLogicType = _HwStorageFCPortLogicType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 7, 1, 8),
    _HwStorageFCPortLogicType_Type()
)
hwStorageFCPortLogicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageFCPortLogicType.setStatus("current")


class _HwStorageFCPortSpeedRate_Type(Integer32):
    """Custom type hwStorageFCPortSpeedRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("gbps1", 1),
          ("gbps2", 2),
          ("gbps4", 4),
          ("gbps8", 8),
          ("gbps16", 16))
    )


_HwStorageFCPortSpeedRate_Type.__name__ = "Integer32"
_HwStorageFCPortSpeedRate_Object = MibTableColumn
hwStorageFCPortSpeedRate = _HwStorageFCPortSpeedRate_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 7, 1, 9),
    _HwStorageFCPortSpeedRate_Type()
)
hwStorageFCPortSpeedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageFCPortSpeedRate.setStatus("current")
_HwStorageSASPortTable_Object = MibTable
hwStorageSASPortTable = _HwStorageSASPortTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 8)
)
if mibBuilder.loadTexts:
    hwStorageSASPortTable.setStatus("current")
_HwStorageSASPortEntry_Object = MibTableRow
hwStorageSASPortEntry = _HwStorageSASPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 8, 1)
)
hwStorageSASPortEntry.setIndexNames(
    (0, "ISM-STORAGE-SVC-MIB", "hwStorageSASPortIfIndex"),
)
if mibBuilder.loadTexts:
    hwStorageSASPortEntry.setStatus("current")
_HwStorageSASPortIfIndex_Type = Unsigned32
_HwStorageSASPortIfIndex_Object = MibTableColumn
hwStorageSASPortIfIndex = _HwStorageSASPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 8, 1, 1),
    _HwStorageSASPortIfIndex_Type()
)
hwStorageSASPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageSASPortIfIndex.setStatus("current")
_HwStorageSASPortBoardIfIndex_Type = Unsigned32
_HwStorageSASPortBoardIfIndex_Object = MibTableColumn
hwStorageSASPortBoardIfIndex = _HwStorageSASPortBoardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 8, 1, 2),
    _HwStorageSASPortBoardIfIndex_Type()
)
hwStorageSASPortBoardIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageSASPortBoardIfIndex.setStatus("current")
_HwStorageSASPortID_Type = Unsigned32
_HwStorageSASPortID_Object = MibTableColumn
hwStorageSASPortID = _HwStorageSASPortID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 8, 1, 3),
    _HwStorageSASPortID_Type()
)
hwStorageSASPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageSASPortID.setStatus("current")


class _HwStorageSASPortStatus_Type(Integer32):
    """Custom type hwStorageSASPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkdown", 0),
          ("linkup", 1),
          ("fault", 2))
    )


_HwStorageSASPortStatus_Type.__name__ = "Integer32"
_HwStorageSASPortStatus_Object = MibTableColumn
hwStorageSASPortStatus = _HwStorageSASPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 8, 1, 4),
    _HwStorageSASPortStatus_Type()
)
hwStorageSASPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageSASPortStatus.setStatus("current")


class _HwStorageSASPortConfigRate_Type(Integer32):
    """Custom type hwStorageSASPortConfigRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1500,
              3000,
              6000)
        )
    )
    namedValues = NamedValues(
        *(("gbps15", 1500),
          ("gbps30", 3000),
          ("gbps60", 6000))
    )


_HwStorageSASPortConfigRate_Type.__name__ = "Integer32"
_HwStorageSASPortConfigRate_Object = MibTableColumn
hwStorageSASPortConfigRate = _HwStorageSASPortConfigRate_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 8, 1, 5),
    _HwStorageSASPortConfigRate_Type()
)
hwStorageSASPortConfigRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageSASPortConfigRate.setStatus("current")
_HwStorageSASPortWWN_Type = OctetString
_HwStorageSASPortWWN_Object = MibTableColumn
hwStorageSASPortWWN = _HwStorageSASPortWWN_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 8, 1, 6),
    _HwStorageSASPortWWN_Type()
)
hwStorageSASPortWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageSASPortWWN.setStatus("current")


class _HwStorageSASPortLogicType_Type(Integer32):
    """Custom type hwStorageSASPortLogicType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("service", 1),
          ("ibc", 2),
          ("ibs", 3),
          ("expansion", 4),
          ("management", 5),
          ("upsmanagement", 6),
          ("maintenance", 8))
    )


_HwStorageSASPortLogicType_Type.__name__ = "Integer32"
_HwStorageSASPortLogicType_Object = MibTableColumn
hwStorageSASPortLogicType = _HwStorageSASPortLogicType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 8, 1, 7),
    _HwStorageSASPortLogicType_Type()
)
hwStorageSASPortLogicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageSASPortLogicType.setStatus("current")


class _HwStorageSASPortSpeedRate_Type(Integer32):
    """Custom type hwStorageSASPortSpeedRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1500,
              3000,
              6000)
        )
    )
    namedValues = NamedValues(
        *(("gbps15", 1500),
          ("gbps30", 3000),
          ("gbps60", 6000))
    )


_HwStorageSASPortSpeedRate_Type.__name__ = "Integer32"
_HwStorageSASPortSpeedRate_Object = MibTableColumn
hwStorageSASPortSpeedRate = _HwStorageSASPortSpeedRate_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 8, 1, 8),
    _HwStorageSASPortSpeedRate_Type()
)
hwStorageSASPortSpeedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageSASPortSpeedRate.setStatus("current")
_HwStorageISCSIPortTable_Object = MibTable
hwStorageISCSIPortTable = _HwStorageISCSIPortTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 9)
)
if mibBuilder.loadTexts:
    hwStorageISCSIPortTable.setStatus("current")
_HwStorageISCSIPortEntry_Object = MibTableRow
hwStorageISCSIPortEntry = _HwStorageISCSIPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 9, 1)
)
hwStorageISCSIPortEntry.setIndexNames(
    (0, "ISM-STORAGE-SVC-MIB", "hwStorageISCSIPortIfIndex"),
)
if mibBuilder.loadTexts:
    hwStorageISCSIPortEntry.setStatus("current")
_HwStorageISCSIPortIfIndex_Type = Unsigned32
_HwStorageISCSIPortIfIndex_Object = MibTableColumn
hwStorageISCSIPortIfIndex = _HwStorageISCSIPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 9, 1, 1),
    _HwStorageISCSIPortIfIndex_Type()
)
hwStorageISCSIPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageISCSIPortIfIndex.setStatus("current")
_HwStorageISCSIPortBoardIfIndex_Type = Unsigned32
_HwStorageISCSIPortBoardIfIndex_Object = MibTableColumn
hwStorageISCSIPortBoardIfIndex = _HwStorageISCSIPortBoardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 9, 1, 2),
    _HwStorageISCSIPortBoardIfIndex_Type()
)
hwStorageISCSIPortBoardIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageISCSIPortBoardIfIndex.setStatus("current")
_HwStorageISCSIPortID_Type = Unsigned32
_HwStorageISCSIPortID_Object = MibTableColumn
hwStorageISCSIPortID = _HwStorageISCSIPortID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 9, 1, 3),
    _HwStorageISCSIPortID_Type()
)
hwStorageISCSIPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageISCSIPortID.setStatus("current")


class _HwStorageISCSIPortStatus_Type(Integer32):
    """Custom type hwStorageISCSIPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkdown", 0),
          ("linkup", 1),
          ("fault", 2))
    )


_HwStorageISCSIPortStatus_Type.__name__ = "Integer32"
_HwStorageISCSIPortStatus_Object = MibTableColumn
hwStorageISCSIPortStatus = _HwStorageISCSIPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 9, 1, 4),
    _HwStorageISCSIPortStatus_Type()
)
hwStorageISCSIPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageISCSIPortStatus.setStatus("current")
_HwStorageISCSIPortIP_Type = IpAddress
_HwStorageISCSIPortIP_Object = MibTableColumn
hwStorageISCSIPortIP = _HwStorageISCSIPortIP_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 9, 1, 5),
    _HwStorageISCSIPortIP_Type()
)
hwStorageISCSIPortIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStorageISCSIPortIP.setStatus("current")
_HwStorageISCSIPortNetMask_Type = IpAddress
_HwStorageISCSIPortNetMask_Object = MibTableColumn
hwStorageISCSIPortNetMask = _HwStorageISCSIPortNetMask_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 9, 1, 6),
    _HwStorageISCSIPortNetMask_Type()
)
hwStorageISCSIPortNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStorageISCSIPortNetMask.setStatus("current")
_HwStorageISCSIPortBindMode_Type = Integer32
_HwStorageISCSIPortBindMode_Object = MibTableColumn
hwStorageISCSIPortBindMode = _HwStorageISCSIPortBindMode_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 9, 1, 7),
    _HwStorageISCSIPortBindMode_Type()
)
hwStorageISCSIPortBindMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageISCSIPortBindMode.setStatus("current")


class _HwStorageISCSIPortLogicType_Type(Integer32):
    """Custom type hwStorageISCSIPortLogicType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("service", 1),
          ("ibc", 2),
          ("ibs", 3),
          ("expansion", 4),
          ("management", 5),
          ("upsmanagement", 6),
          ("maintenance", 8))
    )


_HwStorageISCSIPortLogicType_Type.__name__ = "Integer32"
_HwStorageISCSIPortLogicType_Object = MibTableColumn
hwStorageISCSIPortLogicType = _HwStorageISCSIPortLogicType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 9, 1, 8),
    _HwStorageISCSIPortLogicType_Type()
)
hwStorageISCSIPortLogicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageISCSIPortLogicType.setStatus("current")
_HwStorageFrontEndHostPortTable_Object = MibTable
hwStorageFrontEndHostPortTable = _HwStorageFrontEndHostPortTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 11)
)
if mibBuilder.loadTexts:
    hwStorageFrontEndHostPortTable.setStatus("current")
_HwStorageFrontEndHostPortEntry_Object = MibTableRow
hwStorageFrontEndHostPortEntry = _HwStorageFrontEndHostPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 11, 1)
)
hwStorageFrontEndHostPortEntry.setIndexNames(
    (0, "ISM-STORAGE-SVC-MIB", "hwStorageFrontEndHostPortIfIndex"),
)
if mibBuilder.loadTexts:
    hwStorageFrontEndHostPortEntry.setStatus("current")
_HwStorageFrontEndHostPortIfIndex_Type = Unsigned32
_HwStorageFrontEndHostPortIfIndex_Object = MibTableColumn
hwStorageFrontEndHostPortIfIndex = _HwStorageFrontEndHostPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 11, 1, 1),
    _HwStorageFrontEndHostPortIfIndex_Type()
)
hwStorageFrontEndHostPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageFrontEndHostPortIfIndex.setStatus("current")


class _HwStorageFrontEndHostPortType_Type(Integer32):
    """Custom type hwStorageFrontEndHostPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              5)
        )
    )
    namedValues = NamedValues(
        *(("sas", 0),
          ("fc", 1),
          ("iscsi", 5))
    )


_HwStorageFrontEndHostPortType_Type.__name__ = "Integer32"
_HwStorageFrontEndHostPortType_Object = MibTableColumn
hwStorageFrontEndHostPortType = _HwStorageFrontEndHostPortType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 11, 1, 2),
    _HwStorageFrontEndHostPortType_Type()
)
hwStorageFrontEndHostPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageFrontEndHostPortType.setStatus("current")


class _HwStorageFrontEndHostPortStatus_Type(Integer32):
    """Custom type hwStorageFrontEndHostPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkdown", 0),
          ("linkup", 1),
          ("fault", 2),
          ("unknown", 3))
    )


_HwStorageFrontEndHostPortStatus_Type.__name__ = "Integer32"
_HwStorageFrontEndHostPortStatus_Object = MibTableColumn
hwStorageFrontEndHostPortStatus = _HwStorageFrontEndHostPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 11, 1, 3),
    _HwStorageFrontEndHostPortStatus_Type()
)
hwStorageFrontEndHostPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageFrontEndHostPortStatus.setStatus("current")
_HwStorageFrontEndHostPortPhysAddress_Type = OctetString
_HwStorageFrontEndHostPortPhysAddress_Object = MibTableColumn
hwStorageFrontEndHostPortPhysAddress = _HwStorageFrontEndHostPortPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 11, 1, 4),
    _HwStorageFrontEndHostPortPhysAddress_Type()
)
hwStorageFrontEndHostPortPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageFrontEndHostPortPhysAddress.setStatus("current")
_HwStorageFrontEndHostPortDescription_Type = OctetString
_HwStorageFrontEndHostPortDescription_Object = MibTableColumn
hwStorageFrontEndHostPortDescription = _HwStorageFrontEndHostPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 11, 1, 5),
    _HwStorageFrontEndHostPortDescription_Type()
)
hwStorageFrontEndHostPortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageFrontEndHostPortDescription.setStatus("current")
_HwStorageControllerTable_Object = MibTable
hwStorageControllerTable = _HwStorageControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 12)
)
if mibBuilder.loadTexts:
    hwStorageControllerTable.setStatus("current")
_HwStorageControllerEntry_Object = MibTableRow
hwStorageControllerEntry = _HwStorageControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 12, 1)
)
hwStorageControllerEntry.setIndexNames(
    (0, "ISM-STORAGE-SVC-MIB", "hwStorageControllerID"),
)
if mibBuilder.loadTexts:
    hwStorageControllerEntry.setStatus("current")
_HwStorageControllerID_Type = Unsigned32
_HwStorageControllerID_Object = MibTableColumn
hwStorageControllerID = _HwStorageControllerID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 12, 1, 1),
    _HwStorageControllerID_Type()
)
hwStorageControllerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageControllerID.setStatus("current")
_HwStorageControllerName_Type = OctetString
_HwStorageControllerName_Object = MibTableColumn
hwStorageControllerName = _HwStorageControllerName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 12, 1, 2),
    _HwStorageControllerName_Type()
)
hwStorageControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageControllerName.setStatus("current")
_HwStorageControllerLocation_Type = OctetString
_HwStorageControllerLocation_Object = MibTableColumn
hwStorageControllerLocation = _HwStorageControllerLocation_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 12, 1, 3),
    _HwStorageControllerLocation_Type()
)
hwStorageControllerLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageControllerLocation.setStatus("current")


class _HwStorageControllerHealthStatus_Type(Integer32):
    """Custom type hwStorageControllerHealthStatus based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("fault", 2),
          ("preFail", 3),
          ("partiallyBroken", 4),
          ("degraded", 5),
          ("badSectorsFound", 6),
          ("bitErrorsFound", 7),
          ("consistent", 8),
          ("inconsistent", 9),
          ("busy", 10),
          ("noInput", 11),
          ("lowBattery", 12),
          ("singleLinkFault", 13))
    )


_HwStorageControllerHealthStatus_Type.__name__ = "Integer32"
_HwStorageControllerHealthStatus_Object = MibTableColumn
hwStorageControllerHealthStatus = _HwStorageControllerHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 12, 1, 4),
    _HwStorageControllerHealthStatus_Type()
)
hwStorageControllerHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageControllerHealthStatus.setStatus("current")


class _HwStorageControllerRunningStatus_Type(Integer32):
    """Custom type hwStorageControllerRunningStatus based on Integer32"""
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
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              63,
              64)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("running", 2),
          ("notRunning", 3),
          ("notExisted", 4),
          ("sleepInHighTemperature", 5),
          ("starting", 6),
          ("powerFailureProtecting", 7),
          ("spinDown", 8),
          ("started", 9),
          ("linkUp", 10),
          ("linkDown", 11),
          ("poweringOn", 12),
          ("poweredOff", 13),
          ("precopy", 14),
          ("copyback", 15),
          ("reconstruction", 16),
          ("expansion", 17),
          ("unformatted", 18),
          ("formatting", 19),
          ("unmapped", 20),
          ("initialSynchronizing", 21),
          ("consistent", 22),
          ("synchronizing", 23),
          ("synchronized", 24),
          ("unsynchronized", 25),
          ("splited", 26),
          ("online", 27),
          ("offline", 28),
          ("locked", 29),
          ("enabled", 30),
          ("disabled", 31),
          ("balancing", 32),
          ("toBeRecoverd", 33),
          ("interrupted", 34),
          ("invalid", 35),
          ("notStart", 36),
          ("queuing", 37),
          ("stopped", 38),
          ("copying", 39),
          ("completed", 40),
          ("paused", 41),
          ("reverseSynchronizing", 42),
          ("activated", 43),
          ("restore", 44),
          ("inactive", 45),
          ("idle", 46),
          ("poweringOff", 47),
          ("charging", 48),
          ("chargingCompleted", 49),
          ("discharging", 50),
          ("upgrading", 51),
          ("runningNormal", 63),
          ("runningFail", 64))
    )


_HwStorageControllerRunningStatus_Type.__name__ = "Integer32"
_HwStorageControllerRunningStatus_Object = MibTableColumn
hwStorageControllerRunningStatus = _HwStorageControllerRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 12, 1, 5),
    _HwStorageControllerRunningStatus_Type()
)
hwStorageControllerRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageControllerRunningStatus.setStatus("current")
_HwStorageControllerSoftVer_Type = OctetString
_HwStorageControllerSoftVer_Object = MibTableColumn
hwStorageControllerSoftVer = _HwStorageControllerSoftVer_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 12, 1, 6),
    _HwStorageControllerSoftVer_Type()
)
hwStorageControllerSoftVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageControllerSoftVer.setStatus("current")
_HwStorageControllerTemperature_Type = Integer32
_HwStorageControllerTemperature_Object = MibTableColumn
hwStorageControllerTemperature = _HwStorageControllerTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 12, 1, 7),
    _HwStorageControllerTemperature_Type()
)
hwStorageControllerTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageControllerTemperature.setStatus("current")
_HwStorageControllerIsMaster_Type = Unsigned32
_HwStorageControllerIsMaster_Object = MibTableColumn
hwStorageControllerIsMaster = _HwStorageControllerIsMaster_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 12, 1, 8),
    _HwStorageControllerIsMaster_Type()
)
hwStorageControllerIsMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageControllerIsMaster.setStatus("current")
_HwStorageControllerELabel_Type = OctetString
_HwStorageControllerELabel_Object = MibTableColumn
hwStorageControllerELabel = _HwStorageControllerELabel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 12, 1, 9),
    _HwStorageControllerELabel_Type()
)
hwStorageControllerELabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageControllerELabel.setStatus("current")
_HwStorageControllerPCBVer_Type = OctetString
_HwStorageControllerPCBVer_Object = MibTableColumn
hwStorageControllerPCBVer = _HwStorageControllerPCBVer_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 12, 1, 10),
    _HwStorageControllerPCBVer_Type()
)
hwStorageControllerPCBVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageControllerPCBVer.setStatus("current")
_HwStorageControllerBMCVer_Type = OctetString
_HwStorageControllerBMCVer_Object = MibTableColumn
hwStorageControllerBMCVer = _HwStorageControllerBMCVer_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 12, 1, 11),
    _HwStorageControllerBMCVer_Type()
)
hwStorageControllerBMCVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageControllerBMCVer.setStatus("current")
_HwStorageControllerLogicVer_Type = OctetString
_HwStorageControllerLogicVer_Object = MibTableColumn
hwStorageControllerLogicVer = _HwStorageControllerLogicVer_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 12, 1, 12),
    _HwStorageControllerLogicVer_Type()
)
hwStorageControllerLogicVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageControllerLogicVer.setStatus("current")
_HwStorageControllerBIOSVer_Type = OctetString
_HwStorageControllerBIOSVer_Object = MibTableColumn
hwStorageControllerBIOSVer = _HwStorageControllerBIOSVer_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 12, 1, 13),
    _HwStorageControllerBIOSVer_Type()
)
hwStorageControllerBIOSVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageControllerBIOSVer.setStatus("current")
_HwStorageControllerMemorySize_Type = Unsigned32
_HwStorageControllerMemorySize_Object = MibTableColumn
hwStorageControllerMemorySize = _HwStorageControllerMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 12, 1, 14),
    _HwStorageControllerMemorySize_Type()
)
hwStorageControllerMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageControllerMemorySize.setStatus("current")
_HwStorageControllerCPUInfo_Type = OctetString
_HwStorageControllerCPUInfo_Object = MibTableColumn
hwStorageControllerCPUInfo = _HwStorageControllerCPUInfo_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 12, 1, 15),
    _HwStorageControllerCPUInfo_Type()
)
hwStorageControllerCPUInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageControllerCPUInfo.setStatus("current")
_HwStorageControllerVoltage_Type = Unsigned32
_HwStorageControllerVoltage_Object = MibTableColumn
hwStorageControllerVoltage = _HwStorageControllerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 8, 12, 1, 16),
    _HwStorageControllerVoltage_Type()
)
hwStorageControllerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageControllerVoltage.setStatus("current")
_HwStorageLogicModule_ObjectIdentity = ObjectIdentity
hwStorageLogicModule = _HwStorageLogicModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9)
)
_HwStorageCacheTable_Object = MibTable
hwStorageCacheTable = _HwStorageCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 1)
)
if mibBuilder.loadTexts:
    hwStorageCacheTable.setStatus("current")
_HwStorageCacheEntry_Object = MibTableRow
hwStorageCacheEntry = _HwStorageCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 1, 1)
)
hwStorageCacheEntry.setIndexNames(
    (0, "ISM-STORAGE-SVC-MIB", "hwStorageCacheID"),
)
if mibBuilder.loadTexts:
    hwStorageCacheEntry.setStatus("current")
_HwStorageCacheID_Type = Unsigned32
_HwStorageCacheID_Object = MibTableColumn
hwStorageCacheID = _HwStorageCacheID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 1, 1, 1),
    _HwStorageCacheID_Type()
)
hwStorageCacheID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageCacheID.setStatus("current")
_HwStorageCacheTotalCapacity_Type = Unsigned32
_HwStorageCacheTotalCapacity_Object = MibTableColumn
hwStorageCacheTotalCapacity = _HwStorageCacheTotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 1, 1, 2),
    _HwStorageCacheTotalCapacity_Type()
)
hwStorageCacheTotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageCacheTotalCapacity.setStatus("current")
if mibBuilder.loadTexts:
    hwStorageCacheTotalCapacity.setUnits("MB")
_HwStorageCacheHighWaterLevel_Type = Unsigned32
_HwStorageCacheHighWaterLevel_Object = MibTableColumn
hwStorageCacheHighWaterLevel = _HwStorageCacheHighWaterLevel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 1, 1, 3),
    _HwStorageCacheHighWaterLevel_Type()
)
hwStorageCacheHighWaterLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStorageCacheHighWaterLevel.setStatus("current")
_HwStorageCacheLowWaterLevel_Type = Unsigned32
_HwStorageCacheLowWaterLevel_Object = MibTableColumn
hwStorageCacheLowWaterLevel = _HwStorageCacheLowWaterLevel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 1, 1, 4),
    _HwStorageCacheLowWaterLevel_Type()
)
hwStorageCacheLowWaterLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStorageCacheLowWaterLevel.setStatus("current")
_HwStorageCacheRowStatus_Type = RowStatus
_HwStorageCacheRowStatus_Object = MibTableColumn
hwStorageCacheRowStatus = _HwStorageCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 1, 1, 5),
    _HwStorageCacheRowStatus_Type()
)
hwStorageCacheRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStorageCacheRowStatus.setStatus("current")
_HwStorageLunTable_Object = MibTable
hwStorageLunTable = _HwStorageLunTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 4)
)
if mibBuilder.loadTexts:
    hwStorageLunTable.setStatus("current")
_HwStorageLunEntry_Object = MibTableRow
hwStorageLunEntry = _HwStorageLunEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 4, 1)
)
hwStorageLunEntry.setIndexNames(
    (0, "ISM-STORAGE-SVC-MIB", "hwStorageLunID"),
)
if mibBuilder.loadTexts:
    hwStorageLunEntry.setStatus("current")
_HwStorageLunID_Type = Unsigned32
_HwStorageLunID_Object = MibTableColumn
hwStorageLunID = _HwStorageLunID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 4, 1, 1),
    _HwStorageLunID_Type()
)
hwStorageLunID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageLunID.setStatus("current")
_HwStorageLunName_Type = OctetString
_HwStorageLunName_Object = MibTableColumn
hwStorageLunName = _HwStorageLunName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 4, 1, 2),
    _HwStorageLunName_Type()
)
hwStorageLunName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageLunName.setStatus("current")
_HwStorageLunWWN_Type = OctetString
_HwStorageLunWWN_Object = MibTableColumn
hwStorageLunWWN = _HwStorageLunWWN_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 4, 1, 3),
    _HwStorageLunWWN_Type()
)
hwStorageLunWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageLunWWN.setStatus("current")
_HwStorageLunPoolID_Type = Unsigned32
_HwStorageLunPoolID_Object = MibTableColumn
hwStorageLunPoolID = _HwStorageLunPoolID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 4, 1, 4),
    _HwStorageLunPoolID_Type()
)
hwStorageLunPoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageLunPoolID.setStatus("current")
_HwStorageLunCapacity_Type = Counter64
_HwStorageLunCapacity_Object = MibTableColumn
hwStorageLunCapacity = _HwStorageLunCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 4, 1, 5),
    _HwStorageLunCapacity_Type()
)
hwStorageLunCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageLunCapacity.setStatus("current")
_HwStorageLunOwningController_Type = Unsigned32
_HwStorageLunOwningController_Object = MibTableColumn
hwStorageLunOwningController = _HwStorageLunOwningController_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 4, 1, 6),
    _HwStorageLunOwningController_Type()
)
hwStorageLunOwningController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageLunOwningController.setStatus("current")
_HwStorageLunStripDepth_Type = Unsigned32
_HwStorageLunStripDepth_Object = MibTableColumn
hwStorageLunStripDepth = _HwStorageLunStripDepth_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 4, 1, 7),
    _HwStorageLunStripDepth_Type()
)
hwStorageLunStripDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageLunStripDepth.setStatus("current")


class _HwStorageLunWriteStrategy_Type(Integer32):
    """Custom type hwStorageLunWriteStrategy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("writethrough", 1),
          ("writebacknomirroring", 2),
          ("writebackmirroring", 3),
          ("writebackmandatorynomirroring", 4),
          ("writebackmandatorymirroring", 5))
    )


_HwStorageLunWriteStrategy_Type.__name__ = "Integer32"
_HwStorageLunWriteStrategy_Object = MibTableColumn
hwStorageLunWriteStrategy = _HwStorageLunWriteStrategy_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 4, 1, 8),
    _HwStorageLunWriteStrategy_Type()
)
hwStorageLunWriteStrategy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageLunWriteStrategy.setStatus("current")


class _HwStorageLunPrefetchStrategy_Type(Integer32):
    """Custom type hwStorageLunPrefetchStrategy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("constant", 1),
          ("variable", 2),
          ("intelligent", 3))
    )


_HwStorageLunPrefetchStrategy_Type.__name__ = "Integer32"
_HwStorageLunPrefetchStrategy_Object = MibTableColumn
hwStorageLunPrefetchStrategy = _HwStorageLunPrefetchStrategy_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 4, 1, 9),
    _HwStorageLunPrefetchStrategy_Type()
)
hwStorageLunPrefetchStrategy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageLunPrefetchStrategy.setStatus("current")
_HwStorageLunPrefetchValue_Type = Unsigned32
_HwStorageLunPrefetchValue_Object = MibTableColumn
hwStorageLunPrefetchValue = _HwStorageLunPrefetchValue_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 4, 1, 10),
    _HwStorageLunPrefetchValue_Type()
)
hwStorageLunPrefetchValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageLunPrefetchValue.setStatus("current")


class _HwStorageLunStatus_Type(Integer32):
    """Custom type hwStorageLunStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("fault", 2),
          ("notformat", 3),
          ("formatting", 4))
    )


_HwStorageLunStatus_Type.__name__ = "Integer32"
_HwStorageLunStatus_Object = MibTableColumn
hwStorageLunStatus = _HwStorageLunStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 4, 1, 11),
    _HwStorageLunStatus_Type()
)
hwStorageLunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageLunStatus.setStatus("current")
_HwStorageLunRowStatus_Type = RowStatus
_HwStorageLunRowStatus_Object = MibTableColumn
hwStorageLunRowStatus = _HwStorageLunRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 4, 1, 50),
    _HwStorageLunRowStatus_Type()
)
hwStorageLunRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageLunRowStatus.setStatus("current")
_HwStorageNodeTable_Object = MibTable
hwStorageNodeTable = _HwStorageNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 6)
)
if mibBuilder.loadTexts:
    hwStorageNodeTable.setStatus("current")
_HwStorageNodeEntry_Object = MibTableRow
hwStorageNodeEntry = _HwStorageNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 6, 1)
)
hwStorageNodeEntry.setIndexNames(
    (0, "ISM-STORAGE-SVC-MIB", "hwStorageNodeIfIndex"),
)
if mibBuilder.loadTexts:
    hwStorageNodeEntry.setStatus("current")
_HwStorageNodeIfIndex_Type = Unsigned32
_HwStorageNodeIfIndex_Object = MibTableColumn
hwStorageNodeIfIndex = _HwStorageNodeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 6, 1, 1),
    _HwStorageNodeIfIndex_Type()
)
hwStorageNodeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageNodeIfIndex.setStatus("current")
_HwStorageNodeIPAddress_Type = IpAddress
_HwStorageNodeIPAddress_Object = MibTableColumn
hwStorageNodeIPAddress = _HwStorageNodeIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 6, 1, 2),
    _HwStorageNodeIPAddress_Type()
)
hwStorageNodeIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStorageNodeIPAddress.setStatus("current")
_HwStorageNodeStatus_Type = Unsigned32
_HwStorageNodeStatus_Object = MibTableColumn
hwStorageNodeStatus = _HwStorageNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 6, 1, 3),
    _HwStorageNodeStatus_Type()
)
hwStorageNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageNodeStatus.setStatus("current")
_HwStorageNodeIsMaster_Type = Unsigned32
_HwStorageNodeIsMaster_Object = MibTableColumn
hwStorageNodeIsMaster = _HwStorageNodeIsMaster_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 6, 1, 4),
    _HwStorageNodeIsMaster_Type()
)
hwStorageNodeIsMaster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStorageNodeIsMaster.setStatus("current")
_HwStorageNodeRowStatus_Type = RowStatus
_HwStorageNodeRowStatus_Object = MibTableColumn
hwStorageNodeRowStatus = _HwStorageNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 19, 9, 6, 1, 20),
    _HwStorageNodeRowStatus_Type()
)
hwStorageNodeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStorageNodeRowStatus.setStatus("current")
_IsoConformance_ObjectIdentity = ObjectIdentity
isoConformance = _IsoConformance_ObjectIdentity(
    (1, 6)
)
_IsoGroups_ObjectIdentity = ObjectIdentity
isoGroups = _IsoGroups_ObjectIdentity(
    (1, 6, 1)
)
_IsoCompliances_ObjectIdentity = ObjectIdentity
isoCompliances = _IsoCompliances_ObjectIdentity(
    (1, 6, 2)
)

# Managed Objects groups

currentObjectGroup = ObjectGroup(
    (1, 6, 1, 1)
)
currentObjectGroup.setObjects(
      *(("ISM-STORAGE-SVC-MIB", "hwStorageFCPortIfIndex"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageFCPortBoardIfIndex"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageFCPortID"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageFCPortStatus"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageFCPortConfigRate"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageFCPortMode"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageFCPortWWN"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageISCSIPortIfIndex"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageISCSIPortBoardIfIndex"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageISCSIPortID"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageISCSIPortStatus"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageISCSIPortIP"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageISCSIPortNetMask"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageISCSIPortBindMode"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageLunID"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageLunName"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageLunWWN"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageLunPoolID"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageLunCapacity"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageLunOwningController"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageLunStripDepth"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageLunWriteStrategy"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageLunPrefetchValue"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageLunStatus"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageLunRowStatus"),
        ("ISM-STORAGE-SVC-MIB", "version"),
        ("ISM-STORAGE-SVC-MIB", "totalCapacity"),
        ("ISM-STORAGE-SVC-MIB", "usedCapacity"),
        ("ISM-STORAGE-SVC-MIB", "deviceType"),
        ("ISM-STORAGE-SVC-MIB", "deviceId"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageSASPortIfIndex"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageSASPortBoardIfIndex"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageSASPortID"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageSASPortStatus"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageSASPortConfigRate"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageFrontEndHostPortIfIndex"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageFrontEndHostPortType"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageFrontEndHostPortStatus"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageFrontEndHostPortPhysAddress"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageFrontEndHostPortDescription"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageCacheID"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageCacheTotalCapacity"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageCacheHighWaterLevel"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageCacheLowWaterLevel"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageCacheRowStatus"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageNodeIfIndex"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageNodeIPAddress"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageNodeStatus"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageNodeIsMaster"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageNodeRowStatus"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageControllerID"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageControllerName"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageControllerLocation"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageControllerRunningStatus"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageControllerSoftVer"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageControllerTemperature"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageControllerIsMaster"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageControllerELabel"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageControllerPCBVer"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageControllerBMCVer"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageControllerLogicVer"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageControllerBIOSVer"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageControllerMemorySize"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageControllerCPUInfo"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageControllerVoltage"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageSASPortWWN"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageFCPortLogicType"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageFCPortSpeedRate"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageSASPortLogicType"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageSASPortSpeedRate"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageISCSIPortLogicType"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageLunPrefetchStrategy"),
        ("ISM-STORAGE-SVC-MIB", "status"),
        ("ISM-STORAGE-SVC-MIB", "hwStorageControllerHealthStatus"))
)
if mibBuilder.loadTexts:
    currentObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

basicCompliance = ModuleCompliance(
    (1, 6, 2, 1)
)
basicCompliance.setObjects(
    ("ISM-STORAGE-SVC-MIB", "currentObjectGroup")
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISM-STORAGE-SVC-MIB",
    **{"NodeCodeString": NodeCodeString,
       "huaweistorage": huaweistorage,
       "hwStorage": hwStorage,
       "hwISM": hwISM,
       "common": common,
       "deviceId": deviceId,
       "deviceType": deviceType,
       "status": status,
       "usedCapacity": usedCapacity,
       "totalCapacity": totalCapacity,
       "version": version,
       "hwStorageService": hwStorageService,
       "hwStoragePhysicalModule": hwStoragePhysicalModule,
       "hwStorageFCPortTable": hwStorageFCPortTable,
       "hwStorageFCPortEntry": hwStorageFCPortEntry,
       "hwStorageFCPortIfIndex": hwStorageFCPortIfIndex,
       "hwStorageFCPortBoardIfIndex": hwStorageFCPortBoardIfIndex,
       "hwStorageFCPortID": hwStorageFCPortID,
       "hwStorageFCPortStatus": hwStorageFCPortStatus,
       "hwStorageFCPortConfigRate": hwStorageFCPortConfigRate,
       "hwStorageFCPortMode": hwStorageFCPortMode,
       "hwStorageFCPortWWN": hwStorageFCPortWWN,
       "hwStorageFCPortLogicType": hwStorageFCPortLogicType,
       "hwStorageFCPortSpeedRate": hwStorageFCPortSpeedRate,
       "hwStorageSASPortTable": hwStorageSASPortTable,
       "hwStorageSASPortEntry": hwStorageSASPortEntry,
       "hwStorageSASPortIfIndex": hwStorageSASPortIfIndex,
       "hwStorageSASPortBoardIfIndex": hwStorageSASPortBoardIfIndex,
       "hwStorageSASPortID": hwStorageSASPortID,
       "hwStorageSASPortStatus": hwStorageSASPortStatus,
       "hwStorageSASPortConfigRate": hwStorageSASPortConfigRate,
       "hwStorageSASPortWWN": hwStorageSASPortWWN,
       "hwStorageSASPortLogicType": hwStorageSASPortLogicType,
       "hwStorageSASPortSpeedRate": hwStorageSASPortSpeedRate,
       "hwStorageISCSIPortTable": hwStorageISCSIPortTable,
       "hwStorageISCSIPortEntry": hwStorageISCSIPortEntry,
       "hwStorageISCSIPortIfIndex": hwStorageISCSIPortIfIndex,
       "hwStorageISCSIPortBoardIfIndex": hwStorageISCSIPortBoardIfIndex,
       "hwStorageISCSIPortID": hwStorageISCSIPortID,
       "hwStorageISCSIPortStatus": hwStorageISCSIPortStatus,
       "hwStorageISCSIPortIP": hwStorageISCSIPortIP,
       "hwStorageISCSIPortNetMask": hwStorageISCSIPortNetMask,
       "hwStorageISCSIPortBindMode": hwStorageISCSIPortBindMode,
       "hwStorageISCSIPortLogicType": hwStorageISCSIPortLogicType,
       "hwStorageFrontEndHostPortTable": hwStorageFrontEndHostPortTable,
       "hwStorageFrontEndHostPortEntry": hwStorageFrontEndHostPortEntry,
       "hwStorageFrontEndHostPortIfIndex": hwStorageFrontEndHostPortIfIndex,
       "hwStorageFrontEndHostPortType": hwStorageFrontEndHostPortType,
       "hwStorageFrontEndHostPortStatus": hwStorageFrontEndHostPortStatus,
       "hwStorageFrontEndHostPortPhysAddress": hwStorageFrontEndHostPortPhysAddress,
       "hwStorageFrontEndHostPortDescription": hwStorageFrontEndHostPortDescription,
       "hwStorageControllerTable": hwStorageControllerTable,
       "hwStorageControllerEntry": hwStorageControllerEntry,
       "hwStorageControllerID": hwStorageControllerID,
       "hwStorageControllerName": hwStorageControllerName,
       "hwStorageControllerLocation": hwStorageControllerLocation,
       "hwStorageControllerHealthStatus": hwStorageControllerHealthStatus,
       "hwStorageControllerRunningStatus": hwStorageControllerRunningStatus,
       "hwStorageControllerSoftVer": hwStorageControllerSoftVer,
       "hwStorageControllerTemperature": hwStorageControllerTemperature,
       "hwStorageControllerIsMaster": hwStorageControllerIsMaster,
       "hwStorageControllerELabel": hwStorageControllerELabel,
       "hwStorageControllerPCBVer": hwStorageControllerPCBVer,
       "hwStorageControllerBMCVer": hwStorageControllerBMCVer,
       "hwStorageControllerLogicVer": hwStorageControllerLogicVer,
       "hwStorageControllerBIOSVer": hwStorageControllerBIOSVer,
       "hwStorageControllerMemorySize": hwStorageControllerMemorySize,
       "hwStorageControllerCPUInfo": hwStorageControllerCPUInfo,
       "hwStorageControllerVoltage": hwStorageControllerVoltage,
       "hwStorageLogicModule": hwStorageLogicModule,
       "hwStorageCacheTable": hwStorageCacheTable,
       "hwStorageCacheEntry": hwStorageCacheEntry,
       "hwStorageCacheID": hwStorageCacheID,
       "hwStorageCacheTotalCapacity": hwStorageCacheTotalCapacity,
       "hwStorageCacheHighWaterLevel": hwStorageCacheHighWaterLevel,
       "hwStorageCacheLowWaterLevel": hwStorageCacheLowWaterLevel,
       "hwStorageCacheRowStatus": hwStorageCacheRowStatus,
       "hwStorageLunTable": hwStorageLunTable,
       "hwStorageLunEntry": hwStorageLunEntry,
       "hwStorageLunID": hwStorageLunID,
       "hwStorageLunName": hwStorageLunName,
       "hwStorageLunWWN": hwStorageLunWWN,
       "hwStorageLunPoolID": hwStorageLunPoolID,
       "hwStorageLunCapacity": hwStorageLunCapacity,
       "hwStorageLunOwningController": hwStorageLunOwningController,
       "hwStorageLunStripDepth": hwStorageLunStripDepth,
       "hwStorageLunWriteStrategy": hwStorageLunWriteStrategy,
       "hwStorageLunPrefetchStrategy": hwStorageLunPrefetchStrategy,
       "hwStorageLunPrefetchValue": hwStorageLunPrefetchValue,
       "hwStorageLunStatus": hwStorageLunStatus,
       "hwStorageLunRowStatus": hwStorageLunRowStatus,
       "hwStorageNodeTable": hwStorageNodeTable,
       "hwStorageNodeEntry": hwStorageNodeEntry,
       "hwStorageNodeIfIndex": hwStorageNodeIfIndex,
       "hwStorageNodeIPAddress": hwStorageNodeIPAddress,
       "hwStorageNodeStatus": hwStorageNodeStatus,
       "hwStorageNodeIsMaster": hwStorageNodeIsMaster,
       "hwStorageNodeRowStatus": hwStorageNodeRowStatus,
       "isoConformance": isoConformance,
       "isoGroups": isoGroups,
       "currentObjectGroup": currentObjectGroup,
       "isoCompliances": isoCompliances,
       "basicCompliance": basicCompliance}
)
