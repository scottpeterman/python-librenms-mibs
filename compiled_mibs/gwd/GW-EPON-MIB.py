# SNMP MIB module (GW-EPON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\gwd\GW-EPON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:48:06 2025
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

(devices,) = mibBuilder.importSymbols(
    "GWTT-SMI",
    "devices")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

gwEponMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20)
)
if mibBuilder.loadTexts:
    gwEponMib.setRevisions(
        ("2006-03-24 09:59",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ChassisSlotSupportType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("sw", 0),
          ("epon", 1),
          ("gpon", 2),
          ("get", 3),
          ("geo", 4),
          ("tdm", 5),
          ("stm1", 6),
          ("pwu48", 7),
          ("pwu220", 8),
          ("smb", 9),
          ("gem", 10),
          ("sig", 11),
          ("onuEponB", 12),
          ("onu6FeC", 13),
          ("onu8FeD", 14),
          ("onu16FeD", 15),
          ("onu8PotsA", 16),
          ("onu8PotsB", 17),
          ("onu8FxsA", 18),
          ("onu8FxsB", 19),
          ("oltMain", 20),
          ("olt2Epon", 21),
          ("e1", 22),
          ("oltE1", 23),
          ("onuE1A", 24),
          ("onuE1B", 25),
          ("sw_6900", 26),
          ("olt4epon", 27),
          ("olt8epon", 28),
          ("olt12epon", 29),
          ("gem4ge", 30),
          ("gem10ge", 31),
          ("fan_6900", 32),
          ("pwu_48", 33),
          ("pwu_220", 34),
          ("olt4epon4ge", 35),
          ("pwu_220_6900m", 36),
          ("pwu_48_6900m", 37),
          ("fan_6900s", 38),
          ("pwu_220_6900s", 39),
          ("pwu_48_6900s", 40))
    )


class OnuAlarmLevelList(TextualConvention, OctetString):
    status = "current"


class EponDeviceType(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class OnuList(TextualConvention, OctetString):
    status = "current"


class ChassisSlotBoardType(TextualConvention, Integer32):
    status = "current"
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
              42)
        )
    )
    namedValues = NamedValues(
        *(("null", 1),
          ("unknown", 2),
          ("sw", 3),
          ("epon", 4),
          ("gpon", 5),
          ("get", 6),
          ("geo", 7),
          ("tdm", 8),
          ("stm1", 9),
          ("pwu48", 10),
          ("pwu220", 11),
          ("smb", 12),
          ("gem", 13),
          ("sig", 14),
          ("onuEponB", 15),
          ("onu6FeC", 16),
          ("onu8FeD", 17),
          ("onu16FeD", 18),
          ("onu8PotsA", 19),
          ("onu8PotsB", 20),
          ("onu8FxsA", 21),
          ("onu8FxsB", 22),
          ("oltMain", 23),
          ("olt2Epon", 24),
          ("e1", 25),
          ("oltE1", 26),
          ("onuE1A", 27),
          ("onuE1B", 28),
          ("sw_6900", 29),
          ("olt4epon", 30),
          ("olt8epon", 31),
          ("olt12epon", 32),
          ("gem4ge", 33),
          ("gem10ge", 34),
          ("fan_6900", 35),
          ("pwu_48", 36),
          ("pwu_220", 37),
          ("olt4epon4ge", 38),
          ("pwu_220_6900m", 39),
          ("fan_6900s", 40),
          ("pwu_48_6900s", 41),
          ("pwu_220_6900s", 42))
    )



# MIB Managed Objects in the order of their OIDs

_GwEponMibObjects_ObjectIdentity = ObjectIdentity
gwEponMibObjects = _GwEponMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1)
)
_GwEponCfgGroup_ObjectIdentity = ObjectIdentity
gwEponCfgGroup = _GwEponCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1)
)
_GwEponDevice_ObjectIdentity = ObjectIdentity
gwEponDevice = _GwEponDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1)
)
_GwEponDevTable_Object = MibTable
gwEponDevTable = _GwEponDevTable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    gwEponDevTable.setStatus("current")
_GwEponDevEntry_Object = MibTableRow
gwEponDevEntry = _GwEponDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1)
)
gwEponDevEntry.setIndexNames(
    (0, "GW-EPON-MIB", "deviceIndex"),
)
if mibBuilder.loadTexts:
    gwEponDevEntry.setStatus("current")
_DeviceIndex_Type = Integer32
_DeviceIndex_Object = MibTableColumn
deviceIndex = _DeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 1),
    _DeviceIndex_Type()
)
deviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIndex.setStatus("current")
_DeviceType_Type = EponDeviceType
_DeviceType_Object = MibTableColumn
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 2),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("current")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibTableColumn
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 3),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")


class _DeviceDescription_Type(DisplayString):
    """Custom type deviceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DeviceDescription_Type.__name__ = "DisplayString"
_DeviceDescription_Object = MibTableColumn
deviceDescription = _DeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 4),
    _DeviceDescription_Type()
)
deviceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceDescription.setStatus("current")


class _DeviceLocation_Type(DisplayString):
    """Custom type deviceLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DeviceLocation_Type.__name__ = "DisplayString"
_DeviceLocation_Object = MibTableColumn
deviceLocation = _DeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 5),
    _DeviceLocation_Type()
)
deviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceLocation.setStatus("current")


class _DeviceVendor_Type(DisplayString):
    """Custom type deviceVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DeviceVendor_Type.__name__ = "DisplayString"
_DeviceVendor_Object = MibTableColumn
deviceVendor = _DeviceVendor_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 6),
    _DeviceVendor_Type()
)
deviceVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceVendor.setStatus("current")


class _DeviceFirmWareVersion_Type(DisplayString):
    """Custom type deviceFirmWareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_DeviceFirmWareVersion_Type.__name__ = "DisplayString"
_DeviceFirmWareVersion_Object = MibTableColumn
deviceFirmWareVersion = _DeviceFirmWareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 7),
    _DeviceFirmWareVersion_Type()
)
deviceFirmWareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFirmWareVersion.setStatus("current")


class _DeviceSoftWareVersion_Type(DisplayString):
    """Custom type deviceSoftWareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_DeviceSoftWareVersion_Type.__name__ = "DisplayString"
_DeviceSoftWareVersion_Object = MibTableColumn
deviceSoftWareVersion = _DeviceSoftWareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 8),
    _DeviceSoftWareVersion_Type()
)
deviceSoftWareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSoftWareVersion.setStatus("current")


class _DeviceHardWareVersion_Type(DisplayString):
    """Custom type deviceHardWareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_DeviceHardWareVersion_Type.__name__ = "DisplayString"
_DeviceHardWareVersion_Object = MibTableColumn
deviceHardWareVersion = _DeviceHardWareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 9),
    _DeviceHardWareVersion_Type()
)
deviceHardWareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHardWareVersion.setStatus("current")


class _DeviceOperStatus_Type(Integer32):
    """Custom type deviceOperStatus based on Integer32"""
    defaultValue = 2

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
        *(("up", 1),
          ("down", 2),
          ("unknown", 3),
          ("dormant", 4),
          ("powerDown", 5))
    )


_DeviceOperStatus_Type.__name__ = "Integer32"
_DeviceOperStatus_Object = MibTableColumn
deviceOperStatus = _DeviceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 10),
    _DeviceOperStatus_Type()
)
deviceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOperStatus.setStatus("current")


class _DeviceAlarmStatus_Type(Integer32):
    """Custom type deviceAlarmStatus based on Integer32"""
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
        *(("vital", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("clear", 5))
    )


_DeviceAlarmStatus_Type.__name__ = "Integer32"
_DeviceAlarmStatus_Object = MibTableColumn
deviceAlarmStatus = _DeviceAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 11),
    _DeviceAlarmStatus_Type()
)
deviceAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAlarmStatus.setStatus("current")


class _DeviceMacAddress_Type(MacAddress):
    """Custom type deviceMacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_DeviceMacAddress_Type.__name__ = "MacAddress"
_DeviceMacAddress_Object = MibTableColumn
deviceMacAddress = _DeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 12),
    _DeviceMacAddress_Type()
)
deviceMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceMacAddress.setStatus("current")
_DeviceLastChange_Type = TimeTicks
_DeviceLastChange_Object = MibTableColumn
deviceLastChange = _DeviceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 15),
    _DeviceLastChange_Type()
)
deviceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLastChange.setStatus("current")


class _DeviceReset_Type(Integer32):
    """Custom type deviceReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("reset", 2))
    )


_DeviceReset_Type.__name__ = "Integer32"
_DeviceReset_Object = MibTableColumn
deviceReset = _DeviceReset_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 16),
    _DeviceReset_Type()
)
deviceReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceReset.setStatus("current")


class _DeviceEntLogicalIndex_Type(Integer32):
    """Custom type deviceEntLogicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DeviceEntLogicalIndex_Type.__name__ = "Integer32"
_DeviceEntLogicalIndex_Object = MibTableColumn
deviceEntLogicalIndex = _DeviceEntLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 17),
    _DeviceEntLogicalIndex_Type()
)
deviceEntLogicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceEntLogicalIndex.setStatus("current")


class _DeviceEntLogicalCommunity_Type(DisplayString):
    """Custom type deviceEntLogicalCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DeviceEntLogicalCommunity_Type.__name__ = "DisplayString"
_DeviceEntLogicalCommunity_Object = MibTableColumn
deviceEntLogicalCommunity = _DeviceEntLogicalCommunity_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 18),
    _DeviceEntLogicalCommunity_Type()
)
deviceEntLogicalCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceEntLogicalCommunity.setStatus("current")
_DeviceOnuTestDistance_Type = Integer32
_DeviceOnuTestDistance_Object = MibTableColumn
deviceOnuTestDistance = _DeviceOnuTestDistance_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 19),
    _DeviceOnuTestDistance_Type()
)
deviceOnuTestDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOnuTestDistance.setStatus("current")
_DeviceUpTime_Type = TimeTicks
_DeviceUpTime_Object = MibTableColumn
deviceUpTime = _DeviceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 20),
    _DeviceUpTime_Type()
)
deviceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUpTime.setStatus("current")


class _DeviceStpEnable_Type(Integer32):
    """Custom type deviceStpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DeviceStpEnable_Type.__name__ = "Integer32"
_DeviceStpEnable_Object = MibTableColumn
deviceStpEnable = _DeviceStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 21),
    _DeviceStpEnable_Type()
)
deviceStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceStpEnable.setStatus("current")
_DeviceChipsetVendor_Type = DisplayString
_DeviceChipsetVendor_Object = MibTableColumn
deviceChipsetVendor = _DeviceChipsetVendor_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 22),
    _DeviceChipsetVendor_Type()
)
deviceChipsetVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceChipsetVendor.setStatus("current")
_DeviceChipsetMode_Type = Integer32
_DeviceChipsetMode_Object = MibTableColumn
deviceChipsetMode = _DeviceChipsetMode_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 23),
    _DeviceChipsetMode_Type()
)
deviceChipsetMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceChipsetMode.setStatus("current")
_DeviceChipsetRevision_Type = DisplayString
_DeviceChipsetRevision_Object = MibTableColumn
deviceChipsetRevision = _DeviceChipsetRevision_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 24),
    _DeviceChipsetRevision_Type()
)
deviceChipsetRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceChipsetRevision.setStatus("current")
_DeviceChipsetDate_Type = DisplayString
_DeviceChipsetDate_Object = MibTableColumn
deviceChipsetDate = _DeviceChipsetDate_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 25),
    _DeviceChipsetDate_Type()
)
deviceChipsetDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceChipsetDate.setStatus("current")
_DeviceCapPortDesc_Type = DisplayString
_DeviceCapPortDesc_Object = MibTableColumn
deviceCapPortDesc = _DeviceCapPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 26),
    _DeviceCapPortDesc_Type()
)
deviceCapPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCapPortDesc.setStatus("current")
_DeviceCapEthPortNum_Type = Integer32
_DeviceCapEthPortNum_Object = MibTableColumn
deviceCapEthPortNum = _DeviceCapEthPortNum_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 27),
    _DeviceCapEthPortNum_Type()
)
deviceCapEthPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCapEthPortNum.setStatus("current")
_DeviceCapIadPotsPortNum_Type = Integer32
_DeviceCapIadPotsPortNum_Object = MibTableColumn
deviceCapIadPotsPortNum = _DeviceCapIadPotsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 28),
    _DeviceCapIadPotsPortNum_Type()
)
deviceCapIadPotsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCapIadPotsPortNum.setStatus("current")
_DeviceCapE1PortNum_Type = Integer32
_DeviceCapE1PortNum_Object = MibTableColumn
deviceCapE1PortNum = _DeviceCapE1PortNum_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 29),
    _DeviceCapE1PortNum_Type()
)
deviceCapE1PortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCapE1PortNum.setStatus("current")
_DeviceCapUQueueTotal_Type = Integer32
_DeviceCapUQueueTotal_Object = MibTableColumn
deviceCapUQueueTotal = _DeviceCapUQueueTotal_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 30),
    _DeviceCapUQueueTotal_Type()
)
deviceCapUQueueTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCapUQueueTotal.setStatus("current")
_DeviceCapUQueuePort_Type = Integer32
_DeviceCapUQueuePort_Object = MibTableColumn
deviceCapUQueuePort = _DeviceCapUQueuePort_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 31),
    _DeviceCapUQueuePort_Type()
)
deviceCapUQueuePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCapUQueuePort.setStatus("current")
_DeviceCapDQueueTotal_Type = Integer32
_DeviceCapDQueueTotal_Object = MibTableColumn
deviceCapDQueueTotal = _DeviceCapDQueueTotal_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 32),
    _DeviceCapDQueueTotal_Type()
)
deviceCapDQueueTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCapDQueueTotal.setStatus("current")
_DeviceCapDQueuePort_Type = Integer32
_DeviceCapDQueuePort_Object = MibTableColumn
deviceCapDQueuePort = _DeviceCapDQueuePort_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 33),
    _DeviceCapDQueuePort_Type()
)
deviceCapDQueuePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCapDQueuePort.setStatus("current")


class _DeviceCapBattery_Type(Integer32):
    """Custom type deviceCapBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DeviceCapBattery_Type.__name__ = "Integer32"
_DeviceCapBattery_Object = MibTableColumn
deviceCapBattery = _DeviceCapBattery_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 34),
    _DeviceCapBattery_Type()
)
deviceCapBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCapBattery.setStatus("current")


class _DeviceMulticastSwitch_Type(Integer32):
    """Custom type deviceMulticastSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snooping", 1),
          ("ctc", 2))
    )


_DeviceMulticastSwitch_Type.__name__ = "Integer32"
_DeviceMulticastSwitch_Object = MibTableColumn
deviceMulticastSwitch = _DeviceMulticastSwitch_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 35),
    _DeviceMulticastSwitch_Type()
)
deviceMulticastSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceMulticastSwitch.setStatus("current")
_DeviceSystemTime_Type = DateAndTime
_DeviceSystemTime_Object = MibTableColumn
deviceSystemTime = _DeviceSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 36),
    _DeviceSystemTime_Type()
)
deviceSystemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceSystemTime.setStatus("current")
_DeviceRestartupTime_Type = DateAndTime
_DeviceRestartupTime_Object = MibTableColumn
deviceRestartupTime = _DeviceRestartupTime_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 37),
    _DeviceRestartupTime_Type()
)
deviceRestartupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceRestartupTime.setStatus("current")


class _DeviceTrafficServiceStatus_Type(Integer32):
    """Custom type deviceTrafficServiceStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DeviceTrafficServiceStatus_Type.__name__ = "Integer32"
_DeviceTrafficServiceStatus_Object = MibTableColumn
deviceTrafficServiceStatus = _DeviceTrafficServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 38),
    _DeviceTrafficServiceStatus_Type()
)
deviceTrafficServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceTrafficServiceStatus.setStatus("current")


class _DeviceAlarmMask_Type(Bits):
    """Custom type deviceAlarmMask based on Bits"""
    namedValues = NamedValues(
        *(("power", 0),
          ("fan", 1),
          ("cpu", 2),
          ("temperature", 3),
          ("register", 4),
          ("present", 5),
          ("ethlink", 6),
          ("ethfer", 7),
          ("ethflr", 8),
          ("ethti", 9),
          ("ethloop", 10),
          ("ponber", 11),
          ("ponfer", 12),
          ("ponabnormal", 13),
          ("ponaps", 14),
          ("ponlink", 15),
          ("onuLaserAlwayOn", 16),
          ("onuOpticalPowerLow", 17),
          ("onuOpticalPowerHigh", 18),
          ("ponLOS", 19))
    )

_DeviceAlarmMask_Type.__name__ = "Bits"
_DeviceAlarmMask_Object = MibTableColumn
deviceAlarmMask = _DeviceAlarmMask_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 39),
    _DeviceAlarmMask_Type()
)
deviceAlarmMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceAlarmMask.setStatus("current")


class _DeviceModel_Type(DisplayString):
    """Custom type deviceModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DeviceModel_Type.__name__ = "DisplayString"
_DeviceModel_Object = MibTableColumn
deviceModel = _DeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 40),
    _DeviceModel_Type()
)
deviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceModel.setStatus("current")


class _DeviceMulticastFastLeaveAbility_Type(Bits):
    """Custom type deviceMulticastFastLeaveAbility based on Bits"""
    namedValues = NamedValues(
        *(("ctc", 0),
          ("snooping", 1))
    )

_DeviceMulticastFastLeaveAbility_Type.__name__ = "Bits"
_DeviceMulticastFastLeaveAbility_Object = MibTableColumn
deviceMulticastFastLeaveAbility = _DeviceMulticastFastLeaveAbility_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 41),
    _DeviceMulticastFastLeaveAbility_Type()
)
deviceMulticastFastLeaveAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMulticastFastLeaveAbility.setStatus("current")


class _DeviceMulticastFastLeaveOperState_Type(Integer32):
    """Custom type deviceMulticastFastLeaveOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("deactive", 2))
    )


_DeviceMulticastFastLeaveOperState_Type.__name__ = "Integer32"
_DeviceMulticastFastLeaveOperState_Object = MibTableColumn
deviceMulticastFastLeaveOperState = _DeviceMulticastFastLeaveOperState_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 42),
    _DeviceMulticastFastLeaveOperState_Type()
)
deviceMulticastFastLeaveOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMulticastFastLeaveOperState.setStatus("current")


class _DeviceMulticastFastLeaveAdminState_Type(Integer32):
    """Custom type deviceMulticastFastLeaveAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("deactive", 2))
    )


_DeviceMulticastFastLeaveAdminState_Type.__name__ = "Integer32"
_DeviceMulticastFastLeaveAdminState_Object = MibTableColumn
deviceMulticastFastLeaveAdminState = _DeviceMulticastFastLeaveAdminState_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 43),
    _DeviceMulticastFastLeaveAdminState_Type()
)
deviceMulticastFastLeaveAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceMulticastFastLeaveAdminState.setStatus("current")
_OnuMacTableAlarmThreshold_Type = Integer32
_OnuMacTableAlarmThreshold_Object = MibTableColumn
onuMacTableAlarmThreshold = _OnuMacTableAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 44),
    _OnuMacTableAlarmThreshold_Type()
)
onuMacTableAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuMacTableAlarmThreshold.setStatus("current")
_OnuMacNumbers_Type = Integer32
_OnuMacNumbers_Object = MibTableColumn
onuMacNumbers = _OnuMacNumbers_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 1, 1, 1, 45),
    _OnuMacNumbers_Type()
)
onuMacNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuMacNumbers.setStatus("current")
_GwEponBoard_ObjectIdentity = ObjectIdentity
gwEponBoard = _GwEponBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2)
)
_GwEponBoardTable_Object = MibTable
gwEponBoardTable = _GwEponBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    gwEponBoardTable.setStatus("current")
_GwEponBoardEntry_Object = MibTableRow
gwEponBoardEntry = _GwEponBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1)
)
gwEponBoardEntry.setIndexNames(
    (0, "GW-EPON-MIB", "deviceIndex"),
    (0, "GW-EPON-MIB", "boardIndex"),
)
if mibBuilder.loadTexts:
    gwEponBoardEntry.setStatus("current")
_BoardIndex_Type = Integer32
_BoardIndex_Object = MibTableColumn
boardIndex = _BoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 1),
    _BoardIndex_Type()
)
boardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardIndex.setStatus("current")
_CurBoardType_Type = ChassisSlotBoardType
_CurBoardType_Object = MibTableColumn
curBoardType = _CurBoardType_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 2),
    _CurBoardType_Type()
)
curBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curBoardType.setStatus("current")


class _BoardDescription_Type(DisplayString):
    """Custom type boardDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BoardDescription_Type.__name__ = "DisplayString"
_BoardDescription_Object = MibTableColumn
boardDescription = _BoardDescription_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 3),
    _BoardDescription_Type()
)
boardDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardDescription.setStatus("current")


class _BoardActMode_Type(Integer32):
    """Custom type boardActMode based on Integer32"""
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
        *(("master-active", 1),
          ("master-redundancy", 2),
          ("slave", 3),
          ("unknown", 4))
    )


_BoardActMode_Type.__name__ = "Integer32"
_BoardActMode_Object = MibTableColumn
boardActMode = _BoardActMode_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 4),
    _BoardActMode_Type()
)
boardActMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardActMode.setStatus("current")


class _BoardOperStatus_Type(Integer32):
    """Custom type boardOperStatus based on Integer32"""
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
        *(("null", 1),
          ("initing", 2),
          ("upgrating", 3),
          ("running", 4),
          ("exception", 5))
    )


_BoardOperStatus_Type.__name__ = "Integer32"
_BoardOperStatus_Object = MibTableColumn
boardOperStatus = _BoardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 5),
    _BoardOperStatus_Type()
)
boardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardOperStatus.setStatus("current")


class _BoardAlarmLevel_Type(Integer32):
    """Custom type boardAlarmLevel based on Integer32"""
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
        *(("vital", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("noAlarm", 5))
    )


_BoardAlarmLevel_Type.__name__ = "Integer32"
_BoardAlarmLevel_Object = MibTableColumn
boardAlarmLevel = _BoardAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 6),
    _BoardAlarmLevel_Type()
)
boardAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardAlarmLevel.setStatus("current")
_BoardLastChangeTime_Type = TimeTicks
_BoardLastChangeTime_Object = MibTableColumn
boardLastChangeTime = _BoardLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 7),
    _BoardLastChangeTime_Type()
)
boardLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardLastChangeTime.setStatus("current")
_BoardSupprotType_Type = ChassisSlotSupportType
_BoardSupprotType_Object = MibTableColumn
boardSupprotType = _BoardSupprotType_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 8),
    _BoardSupprotType_Type()
)
boardSupprotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardSupprotType.setStatus("current")


class _BoardReset_Type(Integer32):
    """Custom type boardReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("reset", 2))
    )


_BoardReset_Type.__name__ = "Integer32"
_BoardReset_Object = MibTableColumn
boardReset = _BoardReset_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 9),
    _BoardReset_Type()
)
boardReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardReset.setStatus("current")
_BoardTemperature_Type = Integer32
_BoardTemperature_Object = MibTableColumn
boardTemperature = _BoardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 10),
    _BoardTemperature_Type()
)
boardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardTemperature.setStatus("current")


class _BoardEntLogicalIndex_Type(Integer32):
    """Custom type boardEntLogicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BoardEntLogicalIndex_Type.__name__ = "Integer32"
_BoardEntLogicalIndex_Object = MibTableColumn
boardEntLogicalIndex = _BoardEntLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 11),
    _BoardEntLogicalIndex_Type()
)
boardEntLogicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardEntLogicalIndex.setStatus("current")


class _BoardEntLogicalCommunity_Type(DisplayString):
    """Custom type boardEntLogicalCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_BoardEntLogicalCommunity_Type.__name__ = "DisplayString"
_BoardEntLogicalCommunity_Object = MibTableColumn
boardEntLogicalCommunity = _BoardEntLogicalCommunity_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 12),
    _BoardEntLogicalCommunity_Type()
)
boardEntLogicalCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardEntLogicalCommunity.setStatus("current")


class _BoardSoftwareVersion_Type(DisplayString):
    """Custom type boardSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_BoardSoftwareVersion_Type.__name__ = "DisplayString"
_BoardSoftwareVersion_Object = MibTableColumn
boardSoftwareVersion = _BoardSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 13),
    _BoardSoftwareVersion_Type()
)
boardSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardSoftwareVersion.setStatus("current")


class _BoardFirmwareVersion_Type(DisplayString):
    """Custom type boardFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_BoardFirmwareVersion_Type.__name__ = "DisplayString"
_BoardFirmwareVersion_Object = MibTableColumn
boardFirmwareVersion = _BoardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 14),
    _BoardFirmwareVersion_Type()
)
boardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardFirmwareVersion.setStatus("current")


class _BoardBootVersion_Type(DisplayString):
    """Custom type boardBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_BoardBootVersion_Type.__name__ = "DisplayString"
_BoardBootVersion_Object = MibTableColumn
boardBootVersion = _BoardBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 15),
    _BoardBootVersion_Type()
)
boardBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardBootVersion.setStatus("current")


class _BoardHardwareVersion_Type(DisplayString):
    """Custom type boardHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_BoardHardwareVersion_Type.__name__ = "DisplayString"
_BoardHardwareVersion_Object = MibTableColumn
boardHardwareVersion = _BoardHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 16),
    _BoardHardwareVersion_Type()
)
boardHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardHardwareVersion.setStatus("current")


class _BoardManufactureDate_Type(DisplayString):
    """Custom type boardManufactureDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_BoardManufactureDate_Type.__name__ = "DisplayString"
_BoardManufactureDate_Object = MibTableColumn
boardManufactureDate = _BoardManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 17),
    _BoardManufactureDate_Type()
)
boardManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardManufactureDate.setStatus("current")


class _BoardSerialNo_Type(DisplayString):
    """Custom type boardSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_BoardSerialNo_Type.__name__ = "DisplayString"
_BoardSerialNo_Object = MibTableColumn
boardSerialNo = _BoardSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 18),
    _BoardSerialNo_Type()
)
boardSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardSerialNo.setStatus("current")
_BoardCpuUsage_Type = Integer32
_BoardCpuUsage_Object = MibTableColumn
boardCpuUsage = _BoardCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 19),
    _BoardCpuUsage_Type()
)
boardCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardCpuUsage.setStatus("current")
_BoardMemoryUsage_Type = Integer32
_BoardMemoryUsage_Object = MibTableColumn
boardMemoryUsage = _BoardMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 20),
    _BoardMemoryUsage_Type()
)
boardMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardMemoryUsage.setStatus("current")


class _BoardHasSnmpAgent_Type(Integer32):
    """Custom type boardHasSnmpAgent based on Integer32"""
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
        *(("notpresent", 0),
          ("snmpv1", 1),
          ("snmpv2c", 2),
          ("snmpv3", 3))
    )


_BoardHasSnmpAgent_Type.__name__ = "Integer32"
_BoardHasSnmpAgent_Object = MibTableColumn
boardHasSnmpAgent = _BoardHasSnmpAgent_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 21),
    _BoardHasSnmpAgent_Type()
)
boardHasSnmpAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardHasSnmpAgent.setStatus("current")
_BoardSnmpAgentIpAddr_Type = IpAddress
_BoardSnmpAgentIpAddr_Object = MibTableColumn
boardSnmpAgentIpAddr = _BoardSnmpAgentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 22),
    _BoardSnmpAgentIpAddr_Type()
)
boardSnmpAgentIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardSnmpAgentIpAddr.setStatus("current")


class _BoardSnmpAgentReadCommunity_Type(DisplayString):
    """Custom type boardSnmpAgentReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BoardSnmpAgentReadCommunity_Type.__name__ = "DisplayString"
_BoardSnmpAgentReadCommunity_Object = MibTableColumn
boardSnmpAgentReadCommunity = _BoardSnmpAgentReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 23),
    _BoardSnmpAgentReadCommunity_Type()
)
boardSnmpAgentReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardSnmpAgentReadCommunity.setStatus("current")


class _BoardSnmpAgentWriteCommunity_Type(DisplayString):
    """Custom type boardSnmpAgentWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BoardSnmpAgentWriteCommunity_Type.__name__ = "DisplayString"
_BoardSnmpAgentWriteCommunity_Object = MibTableColumn
boardSnmpAgentWriteCommunity = _BoardSnmpAgentWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 24),
    _BoardSnmpAgentWriteCommunity_Type()
)
boardSnmpAgentWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardSnmpAgentWriteCommunity.setStatus("current")
_BoardTemperatureHighThresholds_Type = Integer32
_BoardTemperatureHighThresholds_Object = MibTableColumn
boardTemperatureHighThresholds = _BoardTemperatureHighThresholds_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 25),
    _BoardTemperatureHighThresholds_Type()
)
boardTemperatureHighThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardTemperatureHighThresholds.setStatus("current")
_BoardCpuUsageThresholds_Type = Integer32
_BoardCpuUsageThresholds_Object = MibTableColumn
boardCpuUsageThresholds = _BoardCpuUsageThresholds_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 26),
    _BoardCpuUsageThresholds_Type()
)
boardCpuUsageThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardCpuUsageThresholds.setStatus("current")
_BoardMemoryUsageThresholds_Type = Integer32
_BoardMemoryUsageThresholds_Object = MibTableColumn
boardMemoryUsageThresholds = _BoardMemoryUsageThresholds_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 27),
    _BoardMemoryUsageThresholds_Type()
)
boardMemoryUsageThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardMemoryUsageThresholds.setStatus("current")
_BoardMemorySize_Type = Integer32
_BoardMemorySize_Object = MibTableColumn
boardMemorySize = _BoardMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 28),
    _BoardMemorySize_Type()
)
boardMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardMemorySize.setStatus("current")
_BoardTemperatureLowThresholds_Type = Integer32
_BoardTemperatureLowThresholds_Object = MibTableColumn
boardTemperatureLowThresholds = _BoardTemperatureLowThresholds_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 29),
    _BoardTemperatureLowThresholds_Type()
)
boardTemperatureLowThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardTemperatureLowThresholds.setStatus("current")


class _BoardAdminStatus_Type(Integer32):
    """Custom type boardAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_BoardAdminStatus_Type.__name__ = "Integer32"
_BoardAdminStatus_Object = MibTableColumn
boardAdminStatus = _BoardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 2, 1, 1, 30),
    _BoardAdminStatus_Type()
)
boardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardAdminStatus.setStatus("current")
_GwEponPon_ObjectIdentity = ObjectIdentity
gwEponPon = _GwEponPon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3)
)
_PonPortTable_Object = MibTable
ponPortTable = _PonPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ponPortTable.setStatus("current")
_PonPortEntry_Object = MibTableRow
ponPortEntry = _PonPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1)
)
ponPortEntry.setIndexNames(
    (0, "GW-EPON-MIB", "deviceIndex"),
    (0, "GW-EPON-MIB", "boardIndex"),
    (0, "GW-EPON-MIB", "ponPortIndex"),
)
if mibBuilder.loadTexts:
    ponPortEntry.setStatus("current")


class _PonPortIndex_Type(Integer32):
    """Custom type ponPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PonPortIndex_Type.__name__ = "Integer32"
_PonPortIndex_Object = MibTableColumn
ponPortIndex = _PonPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 1),
    _PonPortIndex_Type()
)
ponPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortIndex.setStatus("current")


class _PonPortIfIndex_Type(Integer32):
    """Custom type ponPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PonPortIfIndex_Type.__name__ = "Integer32"
_PonPortIfIndex_Object = MibTableColumn
ponPortIfIndex = _PonPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 2),
    _PonPortIfIndex_Type()
)
ponPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortIfIndex.setStatus("current")


class _PonPortDot1dBasePort_Type(Integer32):
    """Custom type ponPortDot1dBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_PonPortDot1dBasePort_Type.__name__ = "Integer32"
_PonPortDot1dBasePort_Object = MibTableColumn
ponPortDot1dBasePort = _PonPortDot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 3),
    _PonPortDot1dBasePort_Type()
)
ponPortDot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortDot1dBasePort.setStatus("current")
_PonPortPartnerDev_Type = Integer32
_PonPortPartnerDev_Object = MibTableColumn
ponPortPartnerDev = _PonPortPartnerDev_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 4),
    _PonPortPartnerDev_Type()
)
ponPortPartnerDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortPartnerDev.setStatus("current")
_PonPortPartnerBrd_Type = Integer32
_PonPortPartnerBrd_Object = MibTableColumn
ponPortPartnerBrd = _PonPortPartnerBrd_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 5),
    _PonPortPartnerBrd_Type()
)
ponPortPartnerBrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortPartnerBrd.setStatus("current")
_PonPortPartnerPort_Type = Integer32
_PonPortPartnerPort_Object = MibTableColumn
ponPortPartnerPort = _PonPortPartnerPort_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 6),
    _PonPortPartnerPort_Type()
)
ponPortPartnerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortPartnerPort.setStatus("current")
_PonPortProtectionDev_Type = Integer32
_PonPortProtectionDev_Object = MibTableColumn
ponPortProtectionDev = _PonPortProtectionDev_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 7),
    _PonPortProtectionDev_Type()
)
ponPortProtectionDev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortProtectionDev.setStatus("current")
_PonPortProtectionBrd_Type = Integer32
_PonPortProtectionBrd_Object = MibTableColumn
ponPortProtectionBrd = _PonPortProtectionBrd_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 8),
    _PonPortProtectionBrd_Type()
)
ponPortProtectionBrd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortProtectionBrd.setStatus("current")
_PonPortProtectionPort_Type = Integer32
_PonPortProtectionPort_Object = MibTableColumn
ponPortProtectionPort = _PonPortProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 9),
    _PonPortProtectionPort_Type()
)
ponPortProtectionPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortProtectionPort.setStatus("current")


class _PonPortType_Type(Integer32):
    """Custom type ponPortType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("eponMauType1000BasePXOLT", 1),
          ("eponMauType1000BasePXONU", 2),
          ("eponMauType1000BasePX10DOLT", 3),
          ("eponMauType1000BasePX10DONU", 4),
          ("eponMauType1000BasePX10UOLT", 5),
          ("eponMauType1000BasePX10UONU", 6),
          ("eponMauType1000BasePX20DOLT", 7),
          ("eponMauType1000BasePX20DONU", 8),
          ("eponMauType1000BasePX20UOLT", 9),
          ("eponMauType1000BasePX20UONU", 10))
    )


_PonPortType_Type.__name__ = "Integer32"
_PonPortType_Object = MibTableColumn
ponPortType = _PonPortType_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 10),
    _PonPortType_Type()
)
ponPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortType.setStatus("current")


class _PonPortMaxOnu_Type(Integer32):
    """Custom type ponPortMaxOnu based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PonPortMaxOnu_Type.__name__ = "Integer32"
_PonPortMaxOnu_Object = MibTableColumn
ponPortMaxOnu = _PonPortMaxOnu_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 11),
    _PonPortMaxOnu_Type()
)
ponPortMaxOnu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortMaxOnu.setStatus("current")


class _PonPortCurrOnu_Type(Integer32):
    """Custom type ponPortCurrOnu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PonPortCurrOnu_Type.__name__ = "Integer32"
_PonPortCurrOnu_Object = MibTableColumn
ponPortCurrOnu = _PonPortCurrOnu_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 12),
    _PonPortCurrOnu_Type()
)
ponPortCurrOnu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortCurrOnu.setStatus("current")


class _PonPortOperStatus_Type(Integer32):
    """Custom type ponPortOperStatus based on Integer32"""
    defaultValue = 2

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
        *(("up", 1),
          ("down", 2),
          ("unknown", 3),
          ("loop", 4))
    )


_PonPortOperStatus_Type.__name__ = "Integer32"
_PonPortOperStatus_Object = MibTableColumn
ponPortOperStatus = _PonPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 13),
    _PonPortOperStatus_Type()
)
ponPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortOperStatus.setStatus("current")


class _PonPortAlarmStatus_Type(Bits):
    """Custom type ponPortAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("ber", 0),
          ("fer", 1),
          ("abnormal", 2),
          ("aps", 3),
          ("link", 4),
          ("onuLaserAlwaysOn", 5),
          ("onuOpticalPowerLow", 6),
          ("onuOpticalPowerHigh", 7),
          ("ponLOS", 8))
    )

_PonPortAlarmStatus_Type.__name__ = "Bits"
_PonPortAlarmStatus_Object = MibTableColumn
ponPortAlarmStatus = _PonPortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 14),
    _PonPortAlarmStatus_Type()
)
ponPortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortAlarmStatus.setStatus("current")


class _PonPortAlarmMask_Type(Bits):
    """Custom type ponPortAlarmMask based on Bits"""
    namedValues = NamedValues(
        *(("ber", 0),
          ("fer", 1),
          ("abnormal", 2),
          ("aps", 3),
          ("link", 4),
          ("onuLaserAlwaysOn", 5),
          ("onuOpticalPowerLow", 6),
          ("onuOpticalPowerHigh", 7),
          ("ponLOS", 8))
    )

_PonPortAlarmMask_Type.__name__ = "Bits"
_PonPortAlarmMask_Object = MibTableColumn
ponPortAlarmMask = _PonPortAlarmMask_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 15),
    _PonPortAlarmMask_Type()
)
ponPortAlarmMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortAlarmMask.setStatus("current")


class _PonPortMaxBW_Type(Integer32):
    """Custom type ponPortMaxBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_PonPortMaxBW_Type.__name__ = "Integer32"
_PonPortMaxBW_Object = MibTableColumn
ponPortMaxBW = _PonPortMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 16),
    _PonPortMaxBW_Type()
)
ponPortMaxBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortMaxBW.setStatus("current")


class _PonPortActBW_Type(Integer32):
    """Custom type ponPortActBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PonPortActBW_Type.__name__ = "Integer32"
_PonPortActBW_Object = MibTableColumn
ponPortActBW = _PonPortActBW_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 17),
    _PonPortActBW_Type()
)
ponPortActBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortActBW.setStatus("current")


class _PonPortRemainBW_Type(Integer32):
    """Custom type ponPortRemainBW based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_PonPortRemainBW_Type.__name__ = "Integer32"
_PonPortRemainBW_Object = MibTableColumn
ponPortRemainBW = _PonPortRemainBW_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 18),
    _PonPortRemainBW_Type()
)
ponPortRemainBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortRemainBW.setStatus("current")


class _PonPortApsCtrl_Type(Integer32):
    """Custom type ponPortApsCtrl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("auto", 2),
          ("force", 3))
    )


_PonPortApsCtrl_Type.__name__ = "Integer32"
_PonPortApsCtrl_Object = MibTableColumn
ponPortApsCtrl = _PonPortApsCtrl_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 19),
    _PonPortApsCtrl_Type()
)
ponPortApsCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortApsCtrl.setStatus("current")


class _PonPortApsStatus_Type(Integer32):
    """Custom type ponPortApsStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("active", 2),
          ("passive", 3))
    )


_PonPortApsStatus_Type.__name__ = "Integer32"
_PonPortApsStatus_Object = MibTableColumn
ponPortApsStatus = _PonPortApsStatus_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 20),
    _PonPortApsStatus_Type()
)
ponPortApsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortApsStatus.setStatus("current")


class _PonPortEncryptSet_Type(Integer32):
    """Custom type ponPortEncryptSet based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pure", 1),
          ("downstreamonly", 2),
          ("bidirectional", 3))
    )


_PonPortEncryptSet_Type.__name__ = "Integer32"
_PonPortEncryptSet_Object = MibTableColumn
ponPortEncryptSet = _PonPortEncryptSet_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 21),
    _PonPortEncryptSet_Type()
)
ponPortEncryptSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortEncryptSet.setStatus("current")


class _PonPortOnuLpbCtrl_Type(Integer32):
    """Custom type ponPortOnuLpbCtrl based on Integer32"""
    defaultValue = 1

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
        *(("noop", 1),
          ("lpbStart", 2),
          ("lpbStop", 3),
          ("inProcess", 4))
    )


_PonPortOnuLpbCtrl_Type.__name__ = "Integer32"
_PonPortOnuLpbCtrl_Object = MibTableColumn
ponPortOnuLpbCtrl = _PonPortOnuLpbCtrl_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 22),
    _PonPortOnuLpbCtrl_Type()
)
ponPortOnuLpbCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortOnuLpbCtrl.setStatus("current")


class _PonPortOnuLpbSource_Type(Integer32):
    """Custom type ponPortOnuLpbSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_PonPortOnuLpbSource_Type.__name__ = "Integer32"
_PonPortOnuLpbSource_Object = MibTableColumn
ponPortOnuLpbSource = _PonPortOnuLpbSource_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 23),
    _PonPortOnuLpbSource_Type()
)
ponPortOnuLpbSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortOnuLpbSource.setStatus("current")


class _PonPortOnuLpbTime_Type(Integer32):
    """Custom type ponPortOnuLpbTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PonPortOnuLpbTime_Type.__name__ = "Integer32"
_PonPortOnuLpbTime_Object = MibTableColumn
ponPortOnuLpbTime = _PonPortOnuLpbTime_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 24),
    _PonPortOnuLpbTime_Type()
)
ponPortOnuLpbTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortOnuLpbTime.setStatus("current")
_PonPortOnuLpbTxFrms_Type = Counter32
_PonPortOnuLpbTxFrms_Object = MibTableColumn
ponPortOnuLpbTxFrms = _PonPortOnuLpbTxFrms_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 25),
    _PonPortOnuLpbTxFrms_Type()
)
ponPortOnuLpbTxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortOnuLpbTxFrms.setStatus("current")
_PonPortOnuLpbRxFrms_Type = Counter32
_PonPortOnuLpbRxFrms_Object = MibTableColumn
ponPortOnuLpbRxFrms = _PonPortOnuLpbRxFrms_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 26),
    _PonPortOnuLpbRxFrms_Type()
)
ponPortOnuLpbRxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortOnuLpbRxFrms.setStatus("current")


class _PonEntLogicalIndex_Type(Integer32):
    """Custom type ponEntLogicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PonEntLogicalIndex_Type.__name__ = "Integer32"
_PonEntLogicalIndex_Object = MibTableColumn
ponEntLogicalIndex = _PonEntLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 27),
    _PonEntLogicalIndex_Type()
)
ponEntLogicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponEntLogicalIndex.setStatus("current")


class _PonEntLogicalCommunity_Type(DisplayString):
    """Custom type ponEntLogicalCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_PonEntLogicalCommunity_Type.__name__ = "DisplayString"
_PonEntLogicalCommunity_Object = MibTableColumn
ponEntLogicalCommunity = _PonEntLogicalCommunity_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 28),
    _PonEntLogicalCommunity_Type()
)
ponEntLogicalCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponEntLogicalCommunity.setStatus("current")


class _PonPortLinkedOnuCounter_Type(Integer32):
    """Custom type ponPortLinkedOnuCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PonPortLinkedOnuCounter_Type.__name__ = "Integer32"
_PonPortLinkedOnuCounter_Object = MibTableColumn
ponPortLinkedOnuCounter = _PonPortLinkedOnuCounter_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 29),
    _PonPortLinkedOnuCounter_Type()
)
ponPortLinkedOnuCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortLinkedOnuCounter.setStatus("current")


class _PonPortAdminStatus_Type(Integer32):
    """Custom type ponPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_PonPortAdminStatus_Type.__name__ = "Integer32"
_PonPortAdminStatus_Object = MibTableColumn
ponPortAdminStatus = _PonPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 30),
    _PonPortAdminStatus_Type()
)
ponPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortAdminStatus.setStatus("current")


class _PonPortReset_Type(Integer32):
    """Custom type ponPortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("reset", 2))
    )


_PonPortReset_Type.__name__ = "Integer32"
_PonPortReset_Object = MibTableColumn
ponPortReset = _PonPortReset_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 31),
    _PonPortReset_Type()
)
ponPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortReset.setStatus("current")


class _PonPortWindowRange_Type(Integer32):
    """Custom type ponPortWindowRange based on Integer32"""
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
        *(("disable", 1),
          ("wr20km", 2),
          ("wr40km", 3),
          ("wr60km", 4))
    )


_PonPortWindowRange_Type.__name__ = "Integer32"
_PonPortWindowRange_Object = MibTableColumn
ponPortWindowRange = _PonPortWindowRange_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 32),
    _PonPortWindowRange_Type()
)
ponPortWindowRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortWindowRange.setStatus("current")


class _PonPortDownlinkPolicingEbl_Type(Integer32):
    """Custom type ponPortDownlinkPolicingEbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PonPortDownlinkPolicingEbl_Type.__name__ = "Integer32"
_PonPortDownlinkPolicingEbl_Object = MibTableColumn
ponPortDownlinkPolicingEbl = _PonPortDownlinkPolicingEbl_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 33),
    _PonPortDownlinkPolicingEbl_Type()
)
ponPortDownlinkPolicingEbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortDownlinkPolicingEbl.setStatus("current")
_PonPortAllOnuAlmLevel_Type = OnuAlarmLevelList
_PonPortAllOnuAlmLevel_Object = MibTableColumn
ponPortAllOnuAlmLevel = _PonPortAllOnuAlmLevel_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 1, 1, 34),
    _PonPortAllOnuAlmLevel_Type()
)
ponPortAllOnuAlmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortAllOnuAlmLevel.setStatus("current")
_PonOnuMapTable_Object = MibTable
ponOnuMapTable = _PonOnuMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ponOnuMapTable.setStatus("current")
_PonOnuMapEntry_Object = MibTableRow
ponOnuMapEntry = _PonOnuMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 2, 1)
)
ponOnuMapEntry.setIndexNames(
    (0, "GW-EPON-MIB", "deviceIndex"),
    (0, "GW-EPON-MIB", "boardIndex"),
    (0, "GW-EPON-MIB", "ponPortIndex"),
    (0, "GW-EPON-MIB", "mappingOnuIndex"),
)
if mibBuilder.loadTexts:
    ponOnuMapEntry.setStatus("current")


class _MappingOnuIndex_Type(Integer32):
    """Custom type mappingOnuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MappingOnuIndex_Type.__name__ = "Integer32"
_MappingOnuIndex_Object = MibTableColumn
mappingOnuIndex = _MappingOnuIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 2, 1, 1),
    _MappingOnuIndex_Type()
)
mappingOnuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingOnuIndex.setStatus("current")


class _OnuDevIndex_Type(Integer32):
    """Custom type onuDevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OnuDevIndex_Type.__name__ = "Integer32"
_OnuDevIndex_Object = MibTableColumn
onuDevIndex = _OnuDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 2, 1, 2),
    _OnuDevIndex_Type()
)
onuDevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuDevIndex.setStatus("current")


class _OnuName_Type(DisplayString):
    """Custom type onuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_OnuName_Type.__name__ = "DisplayString"
_OnuName_Object = MibTableColumn
onuName = _OnuName_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 2, 1, 3),
    _OnuName_Type()
)
onuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuName.setStatus("current")
_PonPerfMonTable_Object = MibTable
ponPerfMonTable = _PonPerfMonTable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ponPerfMonTable.setStatus("current")
_PonPerfMonEntry_Object = MibTableRow
ponPerfMonEntry = _PonPerfMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 3, 1)
)
ponPerfMonEntry.setIndexNames(
    (0, "GW-EPON-MIB", "deviceIndex"),
    (0, "GW-EPON-MIB", "boardIndex"),
    (0, "GW-EPON-MIB", "ponPortIndex"),
)
if mibBuilder.loadTexts:
    ponPerfMonEntry.setStatus("current")
_PonPerfBER_Type = Counter32
_PonPerfBER_Object = MibTableColumn
ponPerfBER = _PonPerfBER_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 3, 1, 1),
    _PonPerfBER_Type()
)
ponPerfBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPerfBER.setStatus("current")
_PonPerfFER_Type = Counter32
_PonPerfFER_Object = MibTableColumn
ponPerfFER = _PonPerfFER_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 3, 1, 4),
    _PonPerfFER_Type()
)
ponPerfFER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPerfFER.setStatus("current")


class _PonPerfBerAlmEnable_Type(Integer32):
    """Custom type ponPerfBerAlmEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PonPerfBerAlmEnable_Type.__name__ = "Integer32"
_PonPerfBerAlmEnable_Object = MibTableColumn
ponPerfBerAlmEnable = _PonPerfBerAlmEnable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 3, 1, 5),
    _PonPerfBerAlmEnable_Type()
)
ponPerfBerAlmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPerfBerAlmEnable.setStatus("current")


class _PonPerfFerAlmEnable_Type(Integer32):
    """Custom type ponPerfFerAlmEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PonPerfFerAlmEnable_Type.__name__ = "Integer32"
_PonPerfFerAlmEnable_Object = MibTableColumn
ponPerfFerAlmEnable = _PonPerfFerAlmEnable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 3, 1, 6),
    _PonPerfFerAlmEnable_Type()
)
ponPerfFerAlmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPerfFerAlmEnable.setStatus("current")
_PonPerfUpBandwidth_Type = Counter32
_PonPerfUpBandwidth_Object = MibTableColumn
ponPerfUpBandwidth = _PonPerfUpBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 3, 1, 7),
    _PonPerfUpBandwidth_Type()
)
ponPerfUpBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPerfUpBandwidth.setStatus("current")
_PonPerfDownBandwidth_Type = Counter32
_PonPerfDownBandwidth_Object = MibTableColumn
ponPerfDownBandwidth = _PonPerfDownBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 3, 1, 8),
    _PonPerfDownBandwidth_Type()
)
ponPerfDownBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPerfDownBandwidth.setStatus("current")
_PonHisCtrlTable_Object = MibTable
ponHisCtrlTable = _PonHisCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    ponHisCtrlTable.setStatus("current")
_PonHisCtrlEntry_Object = MibTableRow
ponHisCtrlEntry = _PonHisCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 4, 1)
)
ponHisCtrlEntry.setIndexNames(
    (0, "GW-EPON-MIB", "deviceIndex"),
    (0, "GW-EPON-MIB", "boardIndex"),
    (0, "GW-EPON-MIB", "ponPortIndex"),
)
if mibBuilder.loadTexts:
    ponHisCtrlEntry.setStatus("current")


class _PonHis15MinuteEnable_Type(Integer32):
    """Custom type ponHis15MinuteEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PonHis15MinuteEnable_Type.__name__ = "Integer32"
_PonHis15MinuteEnable_Object = MibTableColumn
ponHis15MinuteEnable = _PonHis15MinuteEnable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 4, 1, 1),
    _PonHis15MinuteEnable_Type()
)
ponHis15MinuteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponHis15MinuteEnable.setStatus("current")


class _PonHis24HourEnable_Type(Integer32):
    """Custom type ponHis24HourEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PonHis24HourEnable_Type.__name__ = "Integer32"
_PonHis24HourEnable_Object = MibTableColumn
ponHis24HourEnable = _PonHis24HourEnable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 4, 1, 2),
    _PonHis24HourEnable_Type()
)
ponHis24HourEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponHis24HourEnable.setStatus("current")


class _PonBERThreashold_Type(Integer32):
    """Custom type ponBERThreashold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PonBERThreashold_Type.__name__ = "Integer32"
_PonBERThreashold_Object = MibScalar
ponBERThreashold = _PonBERThreashold_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 5),
    _PonBERThreashold_Type()
)
ponBERThreashold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponBERThreashold.setStatus("current")


class _PonFERThreashold_Type(Integer32):
    """Custom type ponFERThreashold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PonFERThreashold_Type.__name__ = "Integer32"
_PonFERThreashold_Object = MibScalar
ponFERThreashold = _PonFERThreashold_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 6),
    _PonFERThreashold_Type()
)
ponFERThreashold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponFERThreashold.setStatus("current")
_GwEponPonCtcExt_ObjectIdentity = ObjectIdentity
gwEponPonCtcExt = _GwEponPonCtcExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 7)
)


class _GwEponPonCtcExtOamDiscoveryTiming_Type(Integer32):
    """Custom type gwEponPonCtcExtOamDiscoveryTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2550),
    )


_GwEponPonCtcExtOamDiscoveryTiming_Type.__name__ = "Integer32"
_GwEponPonCtcExtOamDiscoveryTiming_Object = MibScalar
gwEponPonCtcExtOamDiscoveryTiming = _GwEponPonCtcExtOamDiscoveryTiming_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 7, 1),
    _GwEponPonCtcExtOamDiscoveryTiming_Type()
)
gwEponPonCtcExtOamDiscoveryTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwEponPonCtcExtOamDiscoveryTiming.setStatus("current")


class _GwEponPonCtcExtOamCtcOui_Type(DisplayString):
    """Custom type gwEponPonCtcExtOamCtcOui based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_GwEponPonCtcExtOamCtcOui_Type.__name__ = "DisplayString"
_GwEponPonCtcExtOamCtcOui_Object = MibScalar
gwEponPonCtcExtOamCtcOui = _GwEponPonCtcExtOamCtcOui_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 7, 2),
    _GwEponPonCtcExtOamCtcOui_Type()
)
gwEponPonCtcExtOamCtcOui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwEponPonCtcExtOamCtcOui.setStatus("current")


class _GwEponPonCtcExtOamCtcVer_Type(Integer32):
    """Custom type gwEponPonCtcExtOamCtcVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GwEponPonCtcExtOamCtcVer_Type.__name__ = "Integer32"
_GwEponPonCtcExtOamCtcVer_Object = MibScalar
gwEponPonCtcExtOamCtcVer = _GwEponPonCtcExtOamCtcVer_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 7, 3),
    _GwEponPonCtcExtOamCtcVer_Type()
)
gwEponPonCtcExtOamCtcVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwEponPonCtcExtOamCtcVer.setStatus("current")


class _GwEponPonCtcEncrypUpdKeyTime_Type(Integer32):
    """Custom type gwEponPonCtcEncrypUpdKeyTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GwEponPonCtcEncrypUpdKeyTime_Type.__name__ = "Integer32"
_GwEponPonCtcEncrypUpdKeyTime_Object = MibScalar
gwEponPonCtcEncrypUpdKeyTime = _GwEponPonCtcEncrypUpdKeyTime_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 7, 4),
    _GwEponPonCtcEncrypUpdKeyTime_Type()
)
gwEponPonCtcEncrypUpdKeyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwEponPonCtcEncrypUpdKeyTime.setStatus("current")


class _GwEponPonCtcEncrypNoReplyTimeout_Type(Integer32):
    """Custom type gwEponPonCtcEncrypNoReplyTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2550),
    )


_GwEponPonCtcEncrypNoReplyTimeout_Type.__name__ = "Integer32"
_GwEponPonCtcEncrypNoReplyTimeout_Object = MibScalar
gwEponPonCtcEncrypNoReplyTimeout = _GwEponPonCtcEncrypNoReplyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 7, 5),
    _GwEponPonCtcEncrypNoReplyTimeout_Type()
)
gwEponPonCtcEncrypNoReplyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwEponPonCtcEncrypNoReplyTimeout.setStatus("current")
_GwEponPonCtcEncrypTimingThreshold_Type = Integer32
_GwEponPonCtcEncrypTimingThreshold_Object = MibScalar
gwEponPonCtcEncrypTimingThreshold = _GwEponPonCtcEncrypTimingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 3, 7, 6),
    _GwEponPonCtcEncrypTimingThreshold_Type()
)
gwEponPonCtcEncrypTimingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwEponPonCtcEncrypTimingThreshold.setStatus("current")
_GwEponPonOnuAuth_ObjectIdentity = ObjectIdentity
gwEponPonOnuAuth = _GwEponPonOnuAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4)
)


class _OnuAuthEnable_Type(Integer32):
    """Custom type onuAuthEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("auth_new_only", 2),
          ("auth_all", 3))
    )


_OnuAuthEnable_Type.__name__ = "Integer32"
_OnuAuthEnable_Object = MibScalar
onuAuthEnable = _OnuAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 1),
    _OnuAuthEnable_Type()
)
onuAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAuthEnable.setStatus("deprecated")
_OnuAuthTable_Object = MibTable
onuAuthTable = _OnuAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    onuAuthTable.setStatus("current")
_OnuAuthEntry_Object = MibTableRow
onuAuthEntry = _OnuAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 2, 1)
)
onuAuthEntry.setIndexNames(
    (0, "GW-EPON-MIB", "eponBoardIndex"),
    (0, "GW-EPON-MIB", "eponPonPortIndex"),
    (0, "GW-EPON-MIB", "onuAuthIndex"),
)
if mibBuilder.loadTexts:
    onuAuthEntry.setStatus("current")
_EponBoardIndex_Type = Integer32
_EponBoardIndex_Object = MibTableColumn
eponBoardIndex = _EponBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 2, 1, 1),
    _EponBoardIndex_Type()
)
eponBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponBoardIndex.setStatus("current")
_EponPonPortIndex_Type = Integer32
_EponPonPortIndex_Object = MibTableColumn
eponPonPortIndex = _EponPonPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 2, 1, 2),
    _EponPonPortIndex_Type()
)
eponPonPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponPonPortIndex.setStatus("current")
_OnuAuthIndex_Type = Integer32
_OnuAuthIndex_Object = MibTableColumn
onuAuthIndex = _OnuAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 2, 1, 3),
    _OnuAuthIndex_Type()
)
onuAuthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAuthIndex.setStatus("current")
_OnuAuthMacAddress_Type = MacAddress
_OnuAuthMacAddress_Object = MibTableColumn
onuAuthMacAddress = _OnuAuthMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 2, 1, 4),
    _OnuAuthMacAddress_Type()
)
onuAuthMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthMacAddress.setStatus("current")
_OnuAuthRowStatus_Type = RowStatus
_OnuAuthRowStatus_Object = MibTableColumn
onuAuthRowStatus = _OnuAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 2, 1, 5),
    _OnuAuthRowStatus_Type()
)
onuAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthRowStatus.setStatus("current")


class _OnuToPonBindingEnable_Type(Integer32):
    """Custom type onuToPonBindingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_OnuToPonBindingEnable_Type.__name__ = "Integer32"
_OnuToPonBindingEnable_Object = MibScalar
onuToPonBindingEnable = _OnuToPonBindingEnable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 3),
    _OnuToPonBindingEnable_Type()
)
onuToPonBindingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuToPonBindingEnable.setStatus("current")
_OnuAuthModeTable_Object = MibTable
onuAuthModeTable = _OnuAuthModeTable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    onuAuthModeTable.setStatus("current")
_OnuAuthModeEntry_Object = MibTableRow
onuAuthModeEntry = _OnuAuthModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 4, 1)
)
onuAuthModeEntry.setIndexNames(
    (0, "GW-EPON-MIB", "onuAuthModeBrdIdx"),
    (0, "GW-EPON-MIB", "onuAuthModePonIdx"),
)
if mibBuilder.loadTexts:
    onuAuthModeEntry.setStatus("current")
_OnuAuthModeBrdIdx_Type = Integer32
_OnuAuthModeBrdIdx_Object = MibTableColumn
onuAuthModeBrdIdx = _OnuAuthModeBrdIdx_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 4, 1, 1),
    _OnuAuthModeBrdIdx_Type()
)
onuAuthModeBrdIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAuthModeBrdIdx.setStatus("current")
_OnuAuthModePonIdx_Type = Integer32
_OnuAuthModePonIdx_Object = MibTableColumn
onuAuthModePonIdx = _OnuAuthModePonIdx_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 4, 1, 2),
    _OnuAuthModePonIdx_Type()
)
onuAuthModePonIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAuthModePonIdx.setStatus("current")


class _OnuAuthMode_Type(Integer32):
    """Custom type onuAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("macAddr", 1),
          ("loid", 2),
          ("hybrid", 3),
          ("loidNoPwd", 4),
          ("hybridNoPwd", 5),
          ("disable", 6))
    )


_OnuAuthMode_Type.__name__ = "Integer32"
_OnuAuthMode_Object = MibTableColumn
onuAuthMode = _OnuAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 4, 1, 3),
    _OnuAuthMode_Type()
)
onuAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAuthMode.setStatus("current")


class _OnuAuthEnableForPon_Type(Integer32):
    """Custom type onuAuthEnableForPon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("auth_new_only", 2),
          ("auth_all", 3))
    )


_OnuAuthEnableForPon_Type.__name__ = "Integer32"
_OnuAuthEnableForPon_Object = MibTableColumn
onuAuthEnableForPon = _OnuAuthEnableForPon_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 4, 1, 4),
    _OnuAuthEnableForPon_Type()
)
onuAuthEnableForPon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAuthEnableForPon.setStatus("current")


class _OnuAuthEntryReorganize_Type(Integer32):
    """Custom type onuAuthEntryReorganize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("organize", 1)
    )


_OnuAuthEntryReorganize_Type.__name__ = "Integer32"
_OnuAuthEntryReorganize_Object = MibTableColumn
onuAuthEntryReorganize = _OnuAuthEntryReorganize_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 4, 1, 5),
    _OnuAuthEntryReorganize_Type()
)
onuAuthEntryReorganize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAuthEntryReorganize.setStatus("current")
_OnuAuthLoidTable_Object = MibTable
onuAuthLoidTable = _OnuAuthLoidTable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 5)
)
if mibBuilder.loadTexts:
    onuAuthLoidTable.setStatus("current")
_OnuAuthLoidEntry_Object = MibTableRow
onuAuthLoidEntry = _OnuAuthLoidEntry_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 5, 1)
)
onuAuthLoidEntry.setIndexNames(
    (0, "GW-EPON-MIB", "onuAuthLoidBrdIdx"),
    (0, "GW-EPON-MIB", "onuAuthLoidPonIdx"),
    (0, "GW-EPON-MIB", "onuAuthLoidIdx"),
)
if mibBuilder.loadTexts:
    onuAuthLoidEntry.setStatus("current")
_OnuAuthLoidBrdIdx_Type = Integer32
_OnuAuthLoidBrdIdx_Object = MibTableColumn
onuAuthLoidBrdIdx = _OnuAuthLoidBrdIdx_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 5, 1, 1),
    _OnuAuthLoidBrdIdx_Type()
)
onuAuthLoidBrdIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAuthLoidBrdIdx.setStatus("current")
_OnuAuthLoidPonIdx_Type = Integer32
_OnuAuthLoidPonIdx_Object = MibTableColumn
onuAuthLoidPonIdx = _OnuAuthLoidPonIdx_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 5, 1, 2),
    _OnuAuthLoidPonIdx_Type()
)
onuAuthLoidPonIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAuthLoidPonIdx.setStatus("current")


class _OnuAuthLoidIdx_Type(Integer32):
    """Custom type onuAuthLoidIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_OnuAuthLoidIdx_Type.__name__ = "Integer32"
_OnuAuthLoidIdx_Object = MibTableColumn
onuAuthLoidIdx = _OnuAuthLoidIdx_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 5, 1, 3),
    _OnuAuthLoidIdx_Type()
)
onuAuthLoidIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAuthLoidIdx.setStatus("current")


class _OnuAuthLoid_Type(DisplayString):
    """Custom type onuAuthLoid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )
    fixed_length = 24


_OnuAuthLoid_Type.__name__ = "DisplayString"
_OnuAuthLoid_Object = MibTableColumn
onuAuthLoid = _OnuAuthLoid_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 5, 1, 4),
    _OnuAuthLoid_Type()
)
onuAuthLoid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthLoid.setStatus("current")


class _OnuAuthLoidPassword_Type(DisplayString):
    """Custom type onuAuthLoidPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_OnuAuthLoidPassword_Type.__name__ = "DisplayString"
_OnuAuthLoidPassword_Object = MibTableColumn
onuAuthLoidPassword = _OnuAuthLoidPassword_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 5, 1, 5),
    _OnuAuthLoidPassword_Type()
)
onuAuthLoidPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthLoidPassword.setStatus("current")
_OnuAuthLoidDevIdx_Type = Integer32
_OnuAuthLoidDevIdx_Object = MibTableColumn
onuAuthLoidDevIdx = _OnuAuthLoidDevIdx_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 5, 1, 6),
    _OnuAuthLoidDevIdx_Type()
)
onuAuthLoidDevIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthLoidDevIdx.setStatus("current")
_OnuAuthLoidRowStatus_Type = RowStatus
_OnuAuthLoidRowStatus_Object = MibTableColumn
onuAuthLoidRowStatus = _OnuAuthLoidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 5, 1, 7),
    _OnuAuthLoidRowStatus_Type()
)
onuAuthLoidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthLoidRowStatus.setStatus("current")
_OnuUnauthenticatedTable_Object = MibTable
onuUnauthenticatedTable = _OnuUnauthenticatedTable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 6)
)
if mibBuilder.loadTexts:
    onuUnauthenticatedTable.setStatus("current")
_OnuUnauthenticatedEntry_Object = MibTableRow
onuUnauthenticatedEntry = _OnuUnauthenticatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 6, 1)
)
onuUnauthenticatedEntry.setIndexNames(
    (0, "GW-EPON-MIB", "eponUnauthenticatedBoardIndex"),
    (0, "GW-EPON-MIB", "eponUnauthenticatedPonPortIndex"),
    (0, "GW-EPON-MIB", "onuUnauthenticatedIndex"),
)
if mibBuilder.loadTexts:
    onuUnauthenticatedEntry.setStatus("current")
_EponUnauthenticatedBoardIndex_Type = Integer32
_EponUnauthenticatedBoardIndex_Object = MibTableColumn
eponUnauthenticatedBoardIndex = _EponUnauthenticatedBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 6, 1, 1),
    _EponUnauthenticatedBoardIndex_Type()
)
eponUnauthenticatedBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponUnauthenticatedBoardIndex.setStatus("current")
_EponUnauthenticatedPonPortIndex_Type = Integer32
_EponUnauthenticatedPonPortIndex_Object = MibTableColumn
eponUnauthenticatedPonPortIndex = _EponUnauthenticatedPonPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 6, 1, 2),
    _EponUnauthenticatedPonPortIndex_Type()
)
eponUnauthenticatedPonPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponUnauthenticatedPonPortIndex.setStatus("current")
_OnuUnauthenticatedIndex_Type = Integer32
_OnuUnauthenticatedIndex_Object = MibTableColumn
onuUnauthenticatedIndex = _OnuUnauthenticatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 6, 1, 3),
    _OnuUnauthenticatedIndex_Type()
)
onuUnauthenticatedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUnauthenticatedIndex.setStatus("current")
_OnuUnauthenticatedMacAddress_Type = MacAddress
_OnuUnauthenticatedMacAddress_Object = MibTableColumn
onuUnauthenticatedMacAddress = _OnuUnauthenticatedMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 6, 1, 4),
    _OnuUnauthenticatedMacAddress_Type()
)
onuUnauthenticatedMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUnauthenticatedMacAddress.setStatus("current")


class _OnuAuthEntryReorganizeForAll_Type(Integer32):
    """Custom type onuAuthEntryReorganizeForAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("organize", 1)
    )


_OnuAuthEntryReorganizeForAll_Type.__name__ = "Integer32"
_OnuAuthEntryReorganizeForAll_Object = MibScalar
onuAuthEntryReorganizeForAll = _OnuAuthEntryReorganizeForAll_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 4, 9),
    _OnuAuthEntryReorganizeForAll_Type()
)
onuAuthEntryReorganizeForAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAuthEntryReorganizeForAll.setStatus("current")
_GwEponLlid_ObjectIdentity = ObjectIdentity
gwEponLlid = _GwEponLlid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5)
)
_PonLlidTable_Object = MibTable
ponLlidTable = _PonLlidTable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ponLlidTable.setStatus("current")
_PonLlidEntry_Object = MibTableRow
ponLlidEntry = _PonLlidEntry_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1)
)
ponLlidEntry.setIndexNames(
    (0, "GW-EPON-MIB", "deviceIndex"),
    (0, "GW-EPON-MIB", "ponLlidIndex"),
)
if mibBuilder.loadTexts:
    ponLlidEntry.setStatus("current")
_PonLlidIndex_Type = Integer32
_PonLlidIndex_Object = MibTableColumn
ponLlidIndex = _PonLlidIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 1),
    _PonLlidIndex_Type()
)
ponLlidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponLlidIndex.setStatus("current")


class _PonLlidType_Type(Integer32):
    """Custom type ponLlidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unkown", 0),
          ("ethlink", 1))
    )


_PonLlidType_Type.__name__ = "Integer32"
_PonLlidType_Object = MibTableColumn
ponLlidType = _PonLlidType_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 2),
    _PonLlidType_Type()
)
ponLlidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponLlidType.setStatus("current")
_PonLlidOltBoard_Type = Integer32
_PonLlidOltBoard_Object = MibTableColumn
ponLlidOltBoard = _PonLlidOltBoard_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 3),
    _PonLlidOltBoard_Type()
)
ponLlidOltBoard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ponLlidOltBoard.setStatus("current")
_PonLlidOltPort_Type = Integer32
_PonLlidOltPort_Object = MibTableColumn
ponLlidOltPort = _PonLlidOltPort_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 4),
    _PonLlidOltPort_Type()
)
ponLlidOltPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ponLlidOltPort.setStatus("current")
_PonLlidOltPortIfIndex_Type = Integer32
_PonLlidOltPortIfIndex_Object = MibTableColumn
ponLlidOltPortIfIndex = _PonLlidOltPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 5),
    _PonLlidOltPortIfIndex_Type()
)
ponLlidOltPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ponLlidOltPortIfIndex.setStatus("current")
_PonLlidOnuPortIfIndex_Type = Integer32
_PonLlidOnuPortIfIndex_Object = MibTableColumn
ponLlidOnuPortIfIndex = _PonLlidOnuPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 6),
    _PonLlidOnuPortIfIndex_Type()
)
ponLlidOnuPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ponLlidOnuPortIfIndex.setStatus("current")
_PonLlidOnuBoard_Type = Integer32
_PonLlidOnuBoard_Object = MibTableColumn
ponLlidOnuBoard = _PonLlidOnuBoard_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 7),
    _PonLlidOnuBoard_Type()
)
ponLlidOnuBoard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ponLlidOnuBoard.setStatus("current")
_PonLlidOnuPort_Type = Integer32
_PonLlidOnuPort_Object = MibTableColumn
ponLlidOnuPort = _PonLlidOnuPort_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 8),
    _PonLlidOnuPort_Type()
)
ponLlidOnuPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ponLlidOnuPort.setStatus("current")


class _PonLlidLLID_Type(Integer32):
    """Custom type ponLlidLLID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PonLlidLLID_Type.__name__ = "Integer32"
_PonLlidLLID_Object = MibTableColumn
ponLlidLLID = _PonLlidLLID_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 9),
    _PonLlidLLID_Type()
)
ponLlidLLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponLlidLLID.setStatus("obsolete")


class _PonLlidIfIndex_Type(Integer32):
    """Custom type ponLlidIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PonLlidIfIndex_Type.__name__ = "Integer32"
_PonLlidIfIndex_Object = MibTableColumn
ponLlidIfIndex = _PonLlidIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 10),
    _PonLlidIfIndex_Type()
)
ponLlidIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponLlidIfIndex.setStatus("current")


class _PonLlidUpFixedBW_Type(Integer32):
    """Custom type ponLlidUpFixedBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_PonLlidUpFixedBW_Type.__name__ = "Integer32"
_PonLlidUpFixedBW_Object = MibTableColumn
ponLlidUpFixedBW = _PonLlidUpFixedBW_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 11),
    _PonLlidUpFixedBW_Type()
)
ponLlidUpFixedBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ponLlidUpFixedBW.setStatus("current")


class _PonLlidDownFixedBW_Type(Integer32):
    """Custom type ponLlidDownFixedBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_PonLlidDownFixedBW_Type.__name__ = "Integer32"
_PonLlidDownFixedBW_Object = MibTableColumn
ponLlidDownFixedBW = _PonLlidDownFixedBW_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 12),
    _PonLlidDownFixedBW_Type()
)
ponLlidDownFixedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponLlidDownFixedBW.setStatus("obsolete")
_PonLlidDesc_Type = DisplayString
_PonLlidDesc_Object = MibTableColumn
ponLlidDesc = _PonLlidDesc_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 13),
    _PonLlidDesc_Type()
)
ponLlidDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ponLlidDesc.setStatus("current")


class _PonLlidSurportMacNum_Type(Integer32):
    """Custom type ponLlidSurportMacNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_PonLlidSurportMacNum_Type.__name__ = "Integer32"
_PonLlidSurportMacNum_Object = MibTableColumn
ponLlidSurportMacNum = _PonLlidSurportMacNum_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 14),
    _PonLlidSurportMacNum_Type()
)
ponLlidSurportMacNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ponLlidSurportMacNum.setStatus("deprecated")


class _PonLlidOnuMacAddress_Type(MacAddress):
    """Custom type ponLlidOnuMacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_PonLlidOnuMacAddress_Type.__name__ = "MacAddress"
_PonLlidOnuMacAddress_Object = MibTableColumn
ponLlidOnuMacAddress = _PonLlidOnuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 15),
    _PonLlidOnuMacAddress_Type()
)
ponLlidOnuMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ponLlidOnuMacAddress.setStatus("current")
_PonLlidRowStatus_Type = RowStatus
_PonLlidRowStatus_Object = MibTableColumn
ponLlidRowStatus = _PonLlidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 16),
    _PonLlidRowStatus_Type()
)
ponLlidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ponLlidRowStatus.setStatus("current")


class _PonLlidUpBWClass_Type(Integer32):
    """Custom type ponLlidUpBWClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PonLlidUpBWClass_Type.__name__ = "Integer32"
_PonLlidUpBWClass_Object = MibTableColumn
ponLlidUpBWClass = _PonLlidUpBWClass_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 17),
    _PonLlidUpBWClass_Type()
)
ponLlidUpBWClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ponLlidUpBWClass.setStatus("current")


class _PonLlidUpDelay_Type(Integer32):
    """Custom type ponLlidUpDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_PonLlidUpDelay_Type.__name__ = "Integer32"
_PonLlidUpDelay_Object = MibTableColumn
ponLlidUpDelay = _PonLlidUpDelay_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 18),
    _PonLlidUpDelay_Type()
)
ponLlidUpDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponLlidUpDelay.setStatus("deprecated")


class _PonLlidUpAssuredBW_Type(Integer32):
    """Custom type ponLlidUpAssuredBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1000000),
    )


_PonLlidUpAssuredBW_Type.__name__ = "Integer32"
_PonLlidUpAssuredBW_Object = MibTableColumn
ponLlidUpAssuredBW = _PonLlidUpAssuredBW_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 19),
    _PonLlidUpAssuredBW_Type()
)
ponLlidUpAssuredBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ponLlidUpAssuredBW.setStatus("current")


class _PonLlidUpBesteffortBW_Type(Integer32):
    """Custom type ponLlidUpBesteffortBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1000000),
    )


_PonLlidUpBesteffortBW_Type.__name__ = "Integer32"
_PonLlidUpBesteffortBW_Object = MibTableColumn
ponLlidUpBesteffortBW = _PonLlidUpBesteffortBW_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 20),
    _PonLlidUpBesteffortBW_Type()
)
ponLlidUpBesteffortBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ponLlidUpBesteffortBW.setStatus("current")


class _PonLlidDownBWClass_Type(Integer32):
    """Custom type ponLlidDownBWClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PonLlidDownBWClass_Type.__name__ = "Integer32"
_PonLlidDownBWClass_Object = MibTableColumn
ponLlidDownBWClass = _PonLlidDownBWClass_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 21),
    _PonLlidDownBWClass_Type()
)
ponLlidDownBWClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponLlidDownBWClass.setStatus("obsolete")


class _PonLlidDownDelay_Type(Integer32):
    """Custom type ponLlidDownDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_PonLlidDownDelay_Type.__name__ = "Integer32"
_PonLlidDownDelay_Object = MibTableColumn
ponLlidDownDelay = _PonLlidDownDelay_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 22),
    _PonLlidDownDelay_Type()
)
ponLlidDownDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponLlidDownDelay.setStatus("obsolete")


class _PonLlidDownAssuredBW_Type(Integer32):
    """Custom type ponLlidDownAssuredBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1000000),
    )


_PonLlidDownAssuredBW_Type.__name__ = "Integer32"
_PonLlidDownAssuredBW_Object = MibTableColumn
ponLlidDownAssuredBW = _PonLlidDownAssuredBW_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 23),
    _PonLlidDownAssuredBW_Type()
)
ponLlidDownAssuredBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ponLlidDownAssuredBW.setStatus("current")


class _PonLlidDownBesteffortBW_Type(Integer32):
    """Custom type ponLlidDownBesteffortBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1000000),
    )


_PonLlidDownBesteffortBW_Type.__name__ = "Integer32"
_PonLlidDownBesteffortBW_Object = MibTableColumn
ponLlidDownBesteffortBW = _PonLlidDownBesteffortBW_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 24),
    _PonLlidDownBesteffortBW_Type()
)
ponLlidDownBesteffortBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponLlidDownBesteffortBW.setStatus("obsolete")


class _PonLlidCtcFecAbility_Type(Integer32):
    """Custom type ponLlidCtcFecAbility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("supported", 2),
          ("notSupported", 3))
    )


_PonLlidCtcFecAbility_Type.__name__ = "Integer32"
_PonLlidCtcFecAbility_Object = MibTableColumn
ponLlidCtcFecAbility = _PonLlidCtcFecAbility_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 25),
    _PonLlidCtcFecAbility_Type()
)
ponLlidCtcFecAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponLlidCtcFecAbility.setStatus("current")


class _PonLlidCtcFecMode_Type(Integer32):
    """Custom type ponLlidCtcFecMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enable", 2),
          ("disable", 3))
    )


_PonLlidCtcFecMode_Type.__name__ = "Integer32"
_PonLlidCtcFecMode_Object = MibTableColumn
ponLlidCtcFecMode = _PonLlidCtcFecMode_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 26),
    _PonLlidCtcFecMode_Type()
)
ponLlidCtcFecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponLlidCtcFecMode.setStatus("current")


class _PonLlidCtcEncrypCtrl_Type(Integer32):
    """Custom type ponLlidCtcEncrypCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PonLlidCtcEncrypCtrl_Type.__name__ = "Integer32"
_PonLlidCtcEncrypCtrl_Object = MibTableColumn
ponLlidCtcEncrypCtrl = _PonLlidCtcEncrypCtrl_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 27),
    _PonLlidCtcEncrypCtrl_Type()
)
ponLlidCtcEncrypCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponLlidCtcEncrypCtrl.setStatus("current")


class _PonLlidCtcDbaQueSetNum_Type(Integer32):
    """Custom type ponLlidCtcDbaQueSetNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PonLlidCtcDbaQueSetNum_Type.__name__ = "Integer32"
_PonLlidCtcDbaQueSetNum_Object = MibTableColumn
ponLlidCtcDbaQueSetNum = _PonLlidCtcDbaQueSetNum_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 28),
    _PonLlidCtcDbaQueSetNum_Type()
)
ponLlidCtcDbaQueSetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponLlidCtcDbaQueSetNum.setStatus("current")


class _PonLlidCtcDbaQueSetCfgStatus_Type(Integer32):
    """Custom type ponLlidCtcDbaQueSetCfgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("get", 2),
          ("set", 3))
    )


_PonLlidCtcDbaQueSetCfgStatus_Type.__name__ = "Integer32"
_PonLlidCtcDbaQueSetCfgStatus_Object = MibTableColumn
ponLlidCtcDbaQueSetCfgStatus = _PonLlidCtcDbaQueSetCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 1, 1, 29),
    _PonLlidCtcDbaQueSetCfgStatus_Type()
)
ponLlidCtcDbaQueSetCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponLlidCtcDbaQueSetCfgStatus.setStatus("current")
_PonLlidCtcDbaQueSetTable_Object = MibTable
ponLlidCtcDbaQueSetTable = _PonLlidCtcDbaQueSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ponLlidCtcDbaQueSetTable.setStatus("current")
_PonLlidCtcDbaQueSetEntry_Object = MibTableRow
ponLlidCtcDbaQueSetEntry = _PonLlidCtcDbaQueSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 2, 1)
)
ponLlidCtcDbaQueSetEntry.setIndexNames(
    (0, "GW-EPON-MIB", "deviceIndex"),
    (0, "GW-EPON-MIB", "ponLlidIndex"),
    (0, "GW-EPON-MIB", "ponLlidCtcDbaQueSetIndex"),
)
if mibBuilder.loadTexts:
    ponLlidCtcDbaQueSetEntry.setStatus("current")
_PonLlidCtcDbaQueSetIndex_Type = Integer32
_PonLlidCtcDbaQueSetIndex_Object = MibTableColumn
ponLlidCtcDbaQueSetIndex = _PonLlidCtcDbaQueSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 2, 1, 1),
    _PonLlidCtcDbaQueSetIndex_Type()
)
ponLlidCtcDbaQueSetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponLlidCtcDbaQueSetIndex.setStatus("current")


class _PonLlidCtcDbaReportBitmap_Type(Bits):
    """Custom type ponLlidCtcDbaReportBitmap based on Bits"""
    namedValues = NamedValues(
        *(("queue0", 0),
          ("queue1", 1),
          ("queue2", 2),
          ("queue3", 3),
          ("queue4", 4),
          ("queue5", 5),
          ("queue6", 6),
          ("queue7", 7))
    )

_PonLlidCtcDbaReportBitmap_Type.__name__ = "Bits"
_PonLlidCtcDbaReportBitmap_Object = MibTableColumn
ponLlidCtcDbaReportBitmap = _PonLlidCtcDbaReportBitmap_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 2, 1, 2),
    _PonLlidCtcDbaReportBitmap_Type()
)
ponLlidCtcDbaReportBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponLlidCtcDbaReportBitmap.setStatus("current")


class _PonLlidCtcDbaQueue0Threshold_Type(Integer32):
    """Custom type ponLlidCtcDbaQueue0Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PonLlidCtcDbaQueue0Threshold_Type.__name__ = "Integer32"
_PonLlidCtcDbaQueue0Threshold_Object = MibTableColumn
ponLlidCtcDbaQueue0Threshold = _PonLlidCtcDbaQueue0Threshold_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 2, 1, 3),
    _PonLlidCtcDbaQueue0Threshold_Type()
)
ponLlidCtcDbaQueue0Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponLlidCtcDbaQueue0Threshold.setStatus("current")


class _PonLlidCtcDbaQueue1Threshold_Type(Integer32):
    """Custom type ponLlidCtcDbaQueue1Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PonLlidCtcDbaQueue1Threshold_Type.__name__ = "Integer32"
_PonLlidCtcDbaQueue1Threshold_Object = MibTableColumn
ponLlidCtcDbaQueue1Threshold = _PonLlidCtcDbaQueue1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 2, 1, 4),
    _PonLlidCtcDbaQueue1Threshold_Type()
)
ponLlidCtcDbaQueue1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponLlidCtcDbaQueue1Threshold.setStatus("current")


class _PonLlidCtcDbaQueue2Threshold_Type(Integer32):
    """Custom type ponLlidCtcDbaQueue2Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PonLlidCtcDbaQueue2Threshold_Type.__name__ = "Integer32"
_PonLlidCtcDbaQueue2Threshold_Object = MibTableColumn
ponLlidCtcDbaQueue2Threshold = _PonLlidCtcDbaQueue2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 2, 1, 5),
    _PonLlidCtcDbaQueue2Threshold_Type()
)
ponLlidCtcDbaQueue2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponLlidCtcDbaQueue2Threshold.setStatus("current")


class _PonLlidCtcDbaQueue3Threshold_Type(Integer32):
    """Custom type ponLlidCtcDbaQueue3Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PonLlidCtcDbaQueue3Threshold_Type.__name__ = "Integer32"
_PonLlidCtcDbaQueue3Threshold_Object = MibTableColumn
ponLlidCtcDbaQueue3Threshold = _PonLlidCtcDbaQueue3Threshold_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 2, 1, 6),
    _PonLlidCtcDbaQueue3Threshold_Type()
)
ponLlidCtcDbaQueue3Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponLlidCtcDbaQueue3Threshold.setStatus("current")


class _PonLlidCtcDbaQueue4Threshold_Type(Integer32):
    """Custom type ponLlidCtcDbaQueue4Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PonLlidCtcDbaQueue4Threshold_Type.__name__ = "Integer32"
_PonLlidCtcDbaQueue4Threshold_Object = MibTableColumn
ponLlidCtcDbaQueue4Threshold = _PonLlidCtcDbaQueue4Threshold_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 2, 1, 7),
    _PonLlidCtcDbaQueue4Threshold_Type()
)
ponLlidCtcDbaQueue4Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponLlidCtcDbaQueue4Threshold.setStatus("current")


class _PonLlidCtcDbaQueue5Threshold_Type(Integer32):
    """Custom type ponLlidCtcDbaQueue5Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PonLlidCtcDbaQueue5Threshold_Type.__name__ = "Integer32"
_PonLlidCtcDbaQueue5Threshold_Object = MibTableColumn
ponLlidCtcDbaQueue5Threshold = _PonLlidCtcDbaQueue5Threshold_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 2, 1, 8),
    _PonLlidCtcDbaQueue5Threshold_Type()
)
ponLlidCtcDbaQueue5Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponLlidCtcDbaQueue5Threshold.setStatus("current")


class _PonLlidCtcDbaQueue6Threshold_Type(Integer32):
    """Custom type ponLlidCtcDbaQueue6Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PonLlidCtcDbaQueue6Threshold_Type.__name__ = "Integer32"
_PonLlidCtcDbaQueue6Threshold_Object = MibTableColumn
ponLlidCtcDbaQueue6Threshold = _PonLlidCtcDbaQueue6Threshold_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 2, 1, 9),
    _PonLlidCtcDbaQueue6Threshold_Type()
)
ponLlidCtcDbaQueue6Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponLlidCtcDbaQueue6Threshold.setStatus("current")


class _PonLlidCtcDbaQueue7Threshold_Type(Integer32):
    """Custom type ponLlidCtcDbaQueue7Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PonLlidCtcDbaQueue7Threshold_Type.__name__ = "Integer32"
_PonLlidCtcDbaQueue7Threshold_Object = MibTableColumn
ponLlidCtcDbaQueue7Threshold = _PonLlidCtcDbaQueue7Threshold_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 5, 2, 1, 10),
    _PonLlidCtcDbaQueue7Threshold_Type()
)
ponLlidCtcDbaQueue7Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponLlidCtcDbaQueue7Threshold.setStatus("current")
_GwDevTrapGroup_ObjectIdentity = ObjectIdentity
gwDevTrapGroup = _GwDevTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6)
)
_GwAlarmLevelGroup_ObjectIdentity = ObjectIdentity
gwAlarmLevelGroup = _GwAlarmLevelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 7)
)


class _OnuNotPresentAlmLevel_Type(Integer32):
    """Custom type onuNotPresentAlmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_OnuNotPresentAlmLevel_Type.__name__ = "Integer32"
_OnuNotPresentAlmLevel_Object = MibScalar
onuNotPresentAlmLevel = _OnuNotPresentAlmLevel_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 7, 1),
    _OnuNotPresentAlmLevel_Type()
)
onuNotPresentAlmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuNotPresentAlmLevel.setStatus("current")


class _DevPowerOffAlmLevel_Type(Integer32):
    """Custom type devPowerOffAlmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DevPowerOffAlmLevel_Type.__name__ = "Integer32"
_DevPowerOffAlmLevel_Object = MibScalar
devPowerOffAlmLevel = _DevPowerOffAlmLevel_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 7, 2),
    _DevPowerOffAlmLevel_Type()
)
devPowerOffAlmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devPowerOffAlmLevel.setStatus("current")


class _PonPortBERAlarmLevel_Type(Integer32):
    """Custom type ponPortBERAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_PonPortBERAlarmLevel_Type.__name__ = "Integer32"
_PonPortBERAlarmLevel_Object = MibScalar
ponPortBERAlarmLevel = _PonPortBERAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 7, 3),
    _PonPortBERAlarmLevel_Type()
)
ponPortBERAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortBERAlarmLevel.setStatus("current")


class _PonPortFERAlarmLevel_Type(Integer32):
    """Custom type ponPortFERAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_PonPortFERAlarmLevel_Type.__name__ = "Integer32"
_PonPortFERAlarmLevel_Object = MibScalar
ponPortFERAlarmLevel = _PonPortFERAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 7, 4),
    _PonPortFERAlarmLevel_Type()
)
ponPortFERAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortFERAlarmLevel.setStatus("current")


class _LlidActBWExceedingAlarmLevel_Type(Integer32):
    """Custom type llidActBWExceedingAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_LlidActBWExceedingAlarmLevel_Type.__name__ = "Integer32"
_LlidActBWExceedingAlarmLevel_Object = MibScalar
llidActBWExceedingAlarmLevel = _LlidActBWExceedingAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 7, 5),
    _LlidActBWExceedingAlarmLevel_Type()
)
llidActBWExceedingAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llidActBWExceedingAlarmLevel.setStatus("current")


class _PowerOffAlarmLevel_Type(Integer32):
    """Custom type powerOffAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_PowerOffAlarmLevel_Type.__name__ = "Integer32"
_PowerOffAlarmLevel_Object = MibScalar
powerOffAlarmLevel = _PowerOffAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 7, 6),
    _PowerOffAlarmLevel_Type()
)
powerOffAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerOffAlarmLevel.setStatus("current")


class _BoardTemperatureHighAlarmLevel_Type(Integer32):
    """Custom type boardTemperatureHighAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BoardTemperatureHighAlarmLevel_Type.__name__ = "Integer32"
_BoardTemperatureHighAlarmLevel_Object = MibScalar
boardTemperatureHighAlarmLevel = _BoardTemperatureHighAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 7, 7),
    _BoardTemperatureHighAlarmLevel_Type()
)
boardTemperatureHighAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardTemperatureHighAlarmLevel.setStatus("current")


class _DevBoardPullAlarmLevel_Type(Integer32):
    """Custom type devBoardPullAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DevBoardPullAlarmLevel_Type.__name__ = "Integer32"
_DevBoardPullAlarmLevel_Object = MibScalar
devBoardPullAlarmLevel = _DevBoardPullAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 7, 8),
    _DevBoardPullAlarmLevel_Type()
)
devBoardPullAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devBoardPullAlarmLevel.setStatus("current")


class _EthLinkdownAlarmLevel_Type(Integer32):
    """Custom type ethLinkdownAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EthLinkdownAlarmLevel_Type.__name__ = "Integer32"
_EthLinkdownAlarmLevel_Object = MibScalar
ethLinkdownAlarmLevel = _EthLinkdownAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 7, 9),
    _EthLinkdownAlarmLevel_Type()
)
ethLinkdownAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethLinkdownAlarmLevel.setStatus("current")


class _DevFanAlarmAlarmLevel_Type(Integer32):
    """Custom type devFanAlarmAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DevFanAlarmAlarmLevel_Type.__name__ = "Integer32"
_DevFanAlarmAlarmLevel_Object = MibScalar
devFanAlarmAlarmLevel = _DevFanAlarmAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 7, 10),
    _DevFanAlarmAlarmLevel_Type()
)
devFanAlarmAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFanAlarmAlarmLevel.setStatus("current")


class _EthFlrAlarmLevel_Type(Integer32):
    """Custom type ethFlrAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EthFlrAlarmLevel_Type.__name__ = "Integer32"
_EthFlrAlarmLevel_Object = MibScalar
ethFlrAlarmLevel = _EthFlrAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 7, 11),
    _EthFlrAlarmLevel_Type()
)
ethFlrAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFlrAlarmLevel.setStatus("current")


class _EthFerAlarmLevel_Type(Integer32):
    """Custom type ethFerAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EthFerAlarmLevel_Type.__name__ = "Integer32"
_EthFerAlarmLevel_Object = MibScalar
ethFerAlarmLevel = _EthFerAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 7, 12),
    _EthFerAlarmLevel_Type()
)
ethFerAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFerAlarmLevel.setStatus("current")


class _EthTransmittalIntermitAlarmLevel_Type(Integer32):
    """Custom type ethTransmittalIntermitAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EthTransmittalIntermitAlarmLevel_Type.__name__ = "Integer32"
_EthTransmittalIntermitAlarmLevel_Object = MibScalar
ethTransmittalIntermitAlarmLevel = _EthTransmittalIntermitAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 7, 13),
    _EthTransmittalIntermitAlarmLevel_Type()
)
ethTransmittalIntermitAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethTransmittalIntermitAlarmLevel.setStatus("current")
_GwConsoleCfgGroup_ObjectIdentity = ObjectIdentity
gwConsoleCfgGroup = _GwConsoleCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 8)
)


class _GwConsoleBaudRate_Type(Integer32):
    """Custom type gwConsoleBaudRate based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("b300", 1),
          ("b600", 2),
          ("b1200", 3),
          ("b2400", 4),
          ("b4800", 5),
          ("b9600", 6),
          ("b19200", 7),
          ("b38400", 8),
          ("b115200", 9),
          ("b230400", 10))
    )


_GwConsoleBaudRate_Type.__name__ = "Integer32"
_GwConsoleBaudRate_Object = MibScalar
gwConsoleBaudRate = _GwConsoleBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 8, 1),
    _GwConsoleBaudRate_Type()
)
gwConsoleBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConsoleBaudRate.setStatus("current")


class _GwConsoleDataBits_Type(Integer32):
    """Custom type gwConsoleDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("b5", 5),
          ("b6", 6),
          ("b7", 7),
          ("b8", 8))
    )


_GwConsoleDataBits_Type.__name__ = "Integer32"
_GwConsoleDataBits_Object = MibScalar
gwConsoleDataBits = _GwConsoleDataBits_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 8, 2),
    _GwConsoleDataBits_Type()
)
gwConsoleDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConsoleDataBits.setStatus("current")


class _GwConsoleStopBitSet_Type(Integer32):
    """Custom type gwConsoleStopBitSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sb1", 1),
          ("sb2", 2))
    )


_GwConsoleStopBitSet_Type.__name__ = "Integer32"
_GwConsoleStopBitSet_Object = MibScalar
gwConsoleStopBitSet = _GwConsoleStopBitSet_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 8, 3),
    _GwConsoleStopBitSet_Type()
)
gwConsoleStopBitSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConsoleStopBitSet.setStatus("current")


class _GwConsoleParitySet_Type(Integer32):
    """Custom type gwConsoleParitySet based on Integer32"""
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
        *(("none", 1),
          ("even", 2),
          ("odd", 3),
          ("space", 4))
    )


_GwConsoleParitySet_Type.__name__ = "Integer32"
_GwConsoleParitySet_Object = MibScalar
gwConsoleParitySet = _GwConsoleParitySet_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 8, 4),
    _GwConsoleParitySet_Type()
)
gwConsoleParitySet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConsoleParitySet.setStatus("current")


class _GwConsoleFlowCtrlSet_Type(Integer32):
    """Custom type gwConsoleFlowCtrlSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_GwConsoleFlowCtrlSet_Type.__name__ = "Integer32"
_GwConsoleFlowCtrlSet_Object = MibScalar
gwConsoleFlowCtrlSet = _GwConsoleFlowCtrlSet_Object(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 8, 5),
    _GwConsoleFlowCtrlSet_Type()
)
gwConsoleFlowCtrlSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConsoleFlowCtrlSet.setStatus("current")

# Managed Objects groups


# Notification objects

onuNewRegSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 1)
)
onuNewRegSuccess.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "deviceType"),
        ("GW-EPON-MIB", "deviceSoftWareVersion"),
        ("GW-EPON-MIB", "deviceFirmWareVersion"),
        ("GW-EPON-MIB", "deviceHardWareVersion"))
)
if mibBuilder.loadTexts:
    onuNewRegSuccess.setStatus(
        "current"
    )

onuReregSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 2)
)
onuReregSuccess.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "deviceType"),
        ("GW-EPON-MIB", "deviceSoftWareVersion"),
        ("GW-EPON-MIB", "deviceFirmWareVersion"),
        ("GW-EPON-MIB", "deviceHardWareVersion"))
)
if mibBuilder.loadTexts:
    onuReregSuccess.setStatus(
        "current"
    )

onuNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 3)
)
onuNotPresent.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    onuNotPresent.setStatus(
        "current"
    )

devPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 4)
)
devPowerOff.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    devPowerOff.setStatus(
        "current"
    )

devPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 5)
)
devPowerOn.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "deviceType"),
        ("GW-EPON-MIB", "deviceSoftWareVersion"),
        ("GW-EPON-MIB", "deviceFirmWareVersion"),
        ("GW-EPON-MIB", "deviceHardWareVersion"),
        ("GW-EPON-MIB", "deviceRestartupTime"))
)
if mibBuilder.loadTexts:
    devPowerOn.setStatus(
        "current"
    )

cfgDataSaveSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 6)
)
cfgDataSaveSuccess.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    cfgDataSaveSuccess.setStatus(
        "current"
    )

cfgDataSaveFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 7)
)
cfgDataSaveFail.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    cfgDataSaveFail.setStatus(
        "current"
    )

flashClearSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 8)
)
flashClearSuccess.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    flashClearSuccess.setStatus(
        "current"
    )

flashClearFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 9)
)
flashClearFail.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    flashClearFail.setStatus(
        "current"
    )

softwareUpdateSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 10)
)
softwareUpdateSuccess.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    softwareUpdateSuccess.setStatus(
        "current"
    )

softwareUpdateFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 11)
)
softwareUpdateFail.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    softwareUpdateFail.setStatus(
        "current"
    )

firmwareUpdateSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 12)
)
firmwareUpdateSuccess.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    firmwareUpdateSuccess.setStatus(
        "current"
    )

firmwareUpdateFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 13)
)
firmwareUpdateFail.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    firmwareUpdateFail.setStatus(
        "current"
    )

cfgDataBackupSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 14)
)
cfgDataBackupSuccess.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    cfgDataBackupSuccess.setStatus(
        "current"
    )

cfgDataBackupFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 15)
)
cfgDataBackupFail.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    cfgDataBackupFail.setStatus(
        "current"
    )

cfgDataRestoreSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 16)
)
cfgDataRestoreSuccess.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    cfgDataRestoreSuccess.setStatus(
        "current"
    )

cfgDataRestoreFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 17)
)
cfgDataRestoreFail.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    cfgDataRestoreFail.setStatus(
        "current"
    )

autoProtectSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 18)
)
autoProtectSwitch.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    autoProtectSwitch.setStatus(
        "current"
    )

cpuUsageFactorHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 19)
)
cpuUsageFactorHigh.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    cpuUsageFactorHigh.setStatus(
        "current"
    )

ponPortBERAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 20)
)
ponPortBERAlarm.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "ponPortBrdIndex"),
        ("GW-EPON-MIB", "ponPortIndex"),
        ("GW-EPON-MIB", "ponPortBER"))
)
if mibBuilder.loadTexts:
    ponPortBERAlarm.setStatus(
        "current"
    )

ponPortBERAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 21)
)
ponPortBERAlarmClear.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "ponPortBrdIndex"),
        ("GW-EPON-MIB", "ponPortIndex"),
        ("GW-EPON-MIB", "ponPortBER"))
)
if mibBuilder.loadTexts:
    ponPortBERAlarmClear.setStatus(
        "current"
    )

ponPortFERAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 22)
)
ponPortFERAlarm.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "ponPortBrdIndex"),
        ("GW-EPON-MIB", "ponPortIndex"),
        ("GW-EPON-MIB", "ponPortFER"))
)
if mibBuilder.loadTexts:
    ponPortFERAlarm.setStatus(
        "current"
    )

ponPortFERAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 23)
)
ponPortFERAlarmClear.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "ponPortBrdIndex"),
        ("GW-EPON-MIB", "ponPortIndex"),
        ("GW-EPON-MIB", "ponPortFER"))
)
if mibBuilder.loadTexts:
    ponPortFERAlarmClear.setStatus(
        "current"
    )

llidActBWExceeding = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 24)
)
llidActBWExceeding.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "ponPortBrdIndex"),
        ("GW-EPON-MIB", "ponPortIndex"),
        ("GW-EPON-MIB", "ponLlidIndex"))
)
if mibBuilder.loadTexts:
    llidActBWExceeding.setStatus(
        "current"
    )

llidActBWExceedingClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 25)
)
llidActBWExceedingClear.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "ponPortBrdIndex"),
        ("GW-EPON-MIB", "ponPortIndex"),
        ("GW-EPON-MIB", "ponLlidIndex"))
)
if mibBuilder.loadTexts:
    llidActBWExceedingClear.setStatus(
        "current"
    )

devBoardInterted = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 26)
)
devBoardInterted.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "curBoardType"))
)
if mibBuilder.loadTexts:
    devBoardInterted.setStatus(
        "current"
    )

devBoardPull = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 27)
)
devBoardPull.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "curBoardType"))
)
if mibBuilder.loadTexts:
    devBoardPull.setStatus(
        "current"
    )

powerOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 30)
)
powerOffAlarm.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"))
)
if mibBuilder.loadTexts:
    powerOffAlarm.setStatus(
        "current"
    )

powerOnAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 31)
)
powerOnAlarm.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"))
)
if mibBuilder.loadTexts:
    powerOnAlarm.setStatus(
        "current"
    )

boardTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 32)
)
boardTemperatureHigh.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"))
)
if mibBuilder.loadTexts:
    boardTemperatureHigh.setStatus(
        "current"
    )

boardTemperatureHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 33)
)
boardTemperatureHighClear.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"))
)
if mibBuilder.loadTexts:
    boardTemperatureHighClear.setStatus(
        "current"
    )

ponBoardReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 34)
)
ponBoardReset.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"))
)
if mibBuilder.loadTexts:
    ponBoardReset.setStatus(
        "current"
    )

swBoardProtectedSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 35)
)
swBoardProtectedSwitch.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"))
)
if mibBuilder.loadTexts:
    swBoardProtectedSwitch.setStatus(
        "current"
    )

ponPortAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 36)
)
ponPortAbnormal.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    ponPortAbnormal.setStatus(
        "current"
    )

onuRegisterConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 37)
)
onuRegisterConflict.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    onuRegisterConflict.setStatus(
        "current"
    )

firmwareLoadSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 38)
)
firmwareLoadSuccess.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    firmwareLoadSuccess.setStatus(
        "current"
    )

firmwareLoadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 39)
)
firmwareLoadFailure.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    firmwareLoadFailure.setStatus(
        "current"
    )

dbaUpdateSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 40)
)
dbaUpdateSuccess.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    dbaUpdateSuccess.setStatus(
        "current"
    )

dbaUpdateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 41)
)
dbaUpdateFailure.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    dbaUpdateFailure.setStatus(
        "current"
    )

dbaLoadSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 42)
)
dbaLoadSuccess.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    dbaLoadSuccess.setStatus(
        "current"
    )

dbaLoadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 43)
)
dbaLoadFailure.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    dbaLoadFailure.setStatus(
        "current"
    )

ponToEthLinkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 44)
)
ponToEthLinkdown.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    ponToEthLinkdown.setStatus(
        "current"
    )

ponToEthLinkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 45)
)
ponToEthLinkup.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    ponToEthLinkup.setStatus(
        "current"
    )

onuSoftwareLoadSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 46)
)
onuSoftwareLoadSuccess.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    onuSoftwareLoadSuccess.setStatus(
        "current"
    )

onuSoftwareLoadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 47)
)
onuSoftwareLoadFailure.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    onuSoftwareLoadFailure.setStatus(
        "current"
    )

ethLinkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 54)
)
ethLinkdown.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ethPortIndex"))
)
if mibBuilder.loadTexts:
    ethLinkdown.setStatus(
        "current"
    )

ethLinkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 55)
)
ethLinkup.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ethPortIndex"))
)
if mibBuilder.loadTexts:
    ethLinkup.setStatus(
        "current"
    )

bootUpdateSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 56)
)
bootUpdateSuccess.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    bootUpdateSuccess.setStatus(
        "current"
    )

bootUpdateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 57)
)
bootUpdateFailure.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    bootUpdateFailure.setStatus(
        "current"
    )

batFileBackupSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 58)
)
batFileBackupSuccess.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    batFileBackupSuccess.setStatus(
        "current"
    )

batFileBackupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 59)
)
batFileBackupFailure.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    batFileBackupFailure.setStatus(
        "current"
    )

batFileRestoreSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 60)
)
batFileRestoreSuccess.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    batFileRestoreSuccess.setStatus(
        "current"
    )

batFileRestoreFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 61)
)
batFileRestoreFailure.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    batFileRestoreFailure.setStatus(
        "current"
    )

onuRegAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 62)
)
onuRegAuthFailure.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"),
        ("GW-EPON-MIB", "deviceMacAddress"))
)
if mibBuilder.loadTexts:
    onuRegAuthFailure.setStatus(
        "current"
    )

deviceColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 63)
)
deviceColdStart.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "deviceType"),
        ("GW-EPON-MIB", "deviceSoftWareVersion"),
        ("GW-EPON-MIB", "deviceFirmWareVersion"),
        ("GW-EPON-MIB", "deviceHardWareVersion"),
        ("GW-EPON-MIB", "deviceRestartupTime"))
)
if mibBuilder.loadTexts:
    deviceColdStart.setStatus(
        "current"
    )

deviceWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 64)
)
deviceWarmStart.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "deviceType"),
        ("GW-EPON-MIB", "deviceSoftWareVersion"),
        ("GW-EPON-MIB", "deviceFirmWareVersion"),
        ("GW-EPON-MIB", "deviceHardWareVersion"),
        ("GW-EPON-MIB", "deviceRestartupTime"))
)
if mibBuilder.loadTexts:
    deviceWarmStart.setStatus(
        "current"
    )

deviceExceptionRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 65)
)
deviceExceptionRestart.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "deviceType"),
        ("GW-EPON-MIB", "deviceSoftWareVersion"),
        ("GW-EPON-MIB", "deviceFirmWareVersion"),
        ("GW-EPON-MIB", "deviceHardWareVersion"),
        ("GW-EPON-MIB", "deviceRestartupTime"))
)
if mibBuilder.loadTexts:
    deviceExceptionRestart.setStatus(
        "current"
    )

ethLoopAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 84)
)
ethLoopAlarm.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ethPortIndex"))
)
if mibBuilder.loadTexts:
    ethLoopAlarm.setStatus(
        "current"
    )

ethLoopAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 85)
)
ethLoopAlarmClear.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ethPortIndex"))
)
if mibBuilder.loadTexts:
    ethLoopAlarmClear.setStatus(
        "current"
    )

onuLoopAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 86)
)
onuLoopAlarm.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    onuLoopAlarm.setStatus(
        "current"
    )

onuLoopAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 87)
)
onuLoopAlarmClear.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    onuLoopAlarmClear.setStatus(
        "current"
    )

backboneEthLinkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 88)
)
backboneEthLinkdown.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ethPortIndex"))
)
if mibBuilder.loadTexts:
    backboneEthLinkdown.setStatus(
        "current"
    )

backboneEthLinkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 89)
)
backboneEthLinkup.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ethPortIndex"))
)
if mibBuilder.loadTexts:
    backboneEthLinkup.setStatus(
        "current"
    )

boardCpuUsageAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 116)
)
boardCpuUsageAlarm.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"))
)
if mibBuilder.loadTexts:
    boardCpuUsageAlarm.setStatus(
        "current"
    )

boardCpuUsageAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 117)
)
boardCpuUsageAlarmClear.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"))
)
if mibBuilder.loadTexts:
    boardCpuUsageAlarmClear.setStatus(
        "current"
    )

boardMemoryUsageAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 118)
)
boardMemoryUsageAlarm.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"))
)
if mibBuilder.loadTexts:
    boardMemoryUsageAlarm.setStatus(
        "current"
    )

boardMemoryUsageAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 119)
)
boardMemoryUsageAlarmClear.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"))
)
if mibBuilder.loadTexts:
    boardMemoryUsageAlarmClear.setStatus(
        "current"
    )

ponPortFullAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 132)
)
ponPortFullAlarm.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    ponPortFullAlarm.setStatus(
        "current"
    )

ponPortAbnormalClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 133)
)
ponPortAbnormalClear.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    ponPortAbnormalClear.setStatus(
        "current"
    )

ethPortBroadCastFloodControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 136)
)
ethPortBroadCastFloodControl.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ethPortIndex"))
)
if mibBuilder.loadTexts:
    ethPortBroadCastFloodControl.setStatus(
        "current"
    )

ethPortBroadCastFloodControlClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 137)
)
ethPortBroadCastFloodControlClear.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ethPortIndex"))
)
if mibBuilder.loadTexts:
    ethPortBroadCastFloodControlClear.setStatus(
        "current"
    )

sysfileUploadsuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 138)
)
sysfileUploadsuccess.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    sysfileUploadsuccess.setStatus(
        "current"
    )

sysfileUploadfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 139)
)
sysfileUploadfailure.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    sysfileUploadfailure.setStatus(
        "current"
    )

sysfileDownloadsuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 140)
)
sysfileDownloadsuccess.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    sysfileDownloadsuccess.setStatus(
        "current"
    )

sysfileDownloadfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 141)
)
sysfileDownloadfailure.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    sysfileDownloadfailure.setStatus(
        "current"
    )

ponPortLosAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 142)
)
ponPortLosAlarm.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    ponPortLosAlarm.setStatus(
        "current"
    )

ponPortLosAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 143)
)
ponPortLosAlarmClear.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    ponPortLosAlarmClear.setStatus(
        "current"
    )

ponFWVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 144)
)
ponFWVersionMismatch.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    ponFWVersionMismatch.setStatus(
        "current"
    )

ponFWVersionMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 145)
)
ponFWVersionMatch.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    ponFWVersionMatch.setStatus(
        "current"
    )

ponDBAVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 146)
)
ponDBAVersionMismatch.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    ponDBAVersionMismatch.setStatus(
        "current"
    )

ponDBAVersionMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 147)
)
ponDBAVersionMatch.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    ponDBAVersionMatch.setStatus(
        "current"
    )

ponSFPTypeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 148)
)
ponSFPTypeMismatch.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    ponSFPTypeMismatch.setStatus(
        "current"
    )

ponSFPTypeMitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 149)
)
ponSFPTypeMitch.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    ponSFPTypeMitch.setStatus(
        "current"
    )

ponPortBRASAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 150)
)
ponPortBRASAlarm.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"),
        ("GW-EPON-MIB", "brasMacAddress"))
)
if mibBuilder.loadTexts:
    ponPortBRASAlarm.setStatus(
        "current"
    )

ponPortBRASAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 151)
)
ponPortBRASAlarmClear.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"),
        ("GW-EPON-MIB", "brasMacAddress"))
)
if mibBuilder.loadTexts:
    ponPortBRASAlarmClear.setStatus(
        "current"
    )

ponPortUpNoTraffic = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 152)
)
ponPortUpNoTraffic.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    ponPortUpNoTraffic.setStatus(
        "current"
    )

ponPortUpNoTrafficClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 153)
)
ponPortUpNoTrafficClear.setObjects(
      *(("GW-EPON-MIB", "deviceIndex"),
        ("GW-EPON-MIB", "boardIndex"),
        ("GW-EPON-MIB", "ponPortIndex"))
)
if mibBuilder.loadTexts:
    ponPortUpNoTrafficClear.setStatus(
        "current"
    )

onuDeletingNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 154)
)
onuDeletingNotify.setObjects(
      *(("GW-EPON-MIB", "onuPredefPonSlotIdx"),
        ("GW-EPON-MIB", "onuPredefPonPortIdx"),
        ("GW-EPON-MIB", "onuPredefOnuIdx"),
        ("GW-EPON-MIB", "onuPredefOnuMacAddr"),
        ("GW-EPON-MIB", "onuPredefOnuDevIdx"))
)
if mibBuilder.loadTexts:
    onuDeletingNotify.setStatus(
        "current"
    )

onuMacTableOverFlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 208)
)
onuMacTableOverFlow.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    onuMacTableOverFlow.setStatus(
        "current"
    )

onuMacTableOverFlowClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 10072, 2, 20, 1, 1, 6, 209)
)
onuMacTableOverFlowClear.setObjects(
    ("GW-EPON-MIB", "deviceIndex")
)
if mibBuilder.loadTexts:
    onuMacTableOverFlowClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GW-EPON-MIB",
    **{"ChassisSlotSupportType": ChassisSlotSupportType,
       "OnuAlarmLevelList": OnuAlarmLevelList,
       "EponDeviceType": EponDeviceType,
       "OnuList": OnuList,
       "ChassisSlotBoardType": ChassisSlotBoardType,
       "gwEponMib": gwEponMib,
       "gwEponMibObjects": gwEponMibObjects,
       "gwEponCfgGroup": gwEponCfgGroup,
       "gwEponDevice": gwEponDevice,
       "gwEponDevTable": gwEponDevTable,
       "gwEponDevEntry": gwEponDevEntry,
       "deviceIndex": deviceIndex,
       "deviceType": deviceType,
       "deviceName": deviceName,
       "deviceDescription": deviceDescription,
       "deviceLocation": deviceLocation,
       "deviceVendor": deviceVendor,
       "deviceFirmWareVersion": deviceFirmWareVersion,
       "deviceSoftWareVersion": deviceSoftWareVersion,
       "deviceHardWareVersion": deviceHardWareVersion,
       "deviceOperStatus": deviceOperStatus,
       "deviceAlarmStatus": deviceAlarmStatus,
       "deviceMacAddress": deviceMacAddress,
       "deviceLastChange": deviceLastChange,
       "deviceReset": deviceReset,
       "deviceEntLogicalIndex": deviceEntLogicalIndex,
       "deviceEntLogicalCommunity": deviceEntLogicalCommunity,
       "deviceOnuTestDistance": deviceOnuTestDistance,
       "deviceUpTime": deviceUpTime,
       "deviceStpEnable": deviceStpEnable,
       "deviceChipsetVendor": deviceChipsetVendor,
       "deviceChipsetMode": deviceChipsetMode,
       "deviceChipsetRevision": deviceChipsetRevision,
       "deviceChipsetDate": deviceChipsetDate,
       "deviceCapPortDesc": deviceCapPortDesc,
       "deviceCapEthPortNum": deviceCapEthPortNum,
       "deviceCapIadPotsPortNum": deviceCapIadPotsPortNum,
       "deviceCapE1PortNum": deviceCapE1PortNum,
       "deviceCapUQueueTotal": deviceCapUQueueTotal,
       "deviceCapUQueuePort": deviceCapUQueuePort,
       "deviceCapDQueueTotal": deviceCapDQueueTotal,
       "deviceCapDQueuePort": deviceCapDQueuePort,
       "deviceCapBattery": deviceCapBattery,
       "deviceMulticastSwitch": deviceMulticastSwitch,
       "deviceSystemTime": deviceSystemTime,
       "deviceRestartupTime": deviceRestartupTime,
       "deviceTrafficServiceStatus": deviceTrafficServiceStatus,
       "deviceAlarmMask": deviceAlarmMask,
       "deviceModel": deviceModel,
       "deviceMulticastFastLeaveAbility": deviceMulticastFastLeaveAbility,
       "deviceMulticastFastLeaveOperState": deviceMulticastFastLeaveOperState,
       "deviceMulticastFastLeaveAdminState": deviceMulticastFastLeaveAdminState,
       "onuMacTableAlarmThreshold": onuMacTableAlarmThreshold,
       "onuMacNumbers": onuMacNumbers,
       "gwEponBoard": gwEponBoard,
       "gwEponBoardTable": gwEponBoardTable,
       "gwEponBoardEntry": gwEponBoardEntry,
       "boardIndex": boardIndex,
       "curBoardType": curBoardType,
       "boardDescription": boardDescription,
       "boardActMode": boardActMode,
       "boardOperStatus": boardOperStatus,
       "boardAlarmLevel": boardAlarmLevel,
       "boardLastChangeTime": boardLastChangeTime,
       "boardSupprotType": boardSupprotType,
       "boardReset": boardReset,
       "boardTemperature": boardTemperature,
       "boardEntLogicalIndex": boardEntLogicalIndex,
       "boardEntLogicalCommunity": boardEntLogicalCommunity,
       "boardSoftwareVersion": boardSoftwareVersion,
       "boardFirmwareVersion": boardFirmwareVersion,
       "boardBootVersion": boardBootVersion,
       "boardHardwareVersion": boardHardwareVersion,
       "boardManufactureDate": boardManufactureDate,
       "boardSerialNo": boardSerialNo,
       "boardCpuUsage": boardCpuUsage,
       "boardMemoryUsage": boardMemoryUsage,
       "boardHasSnmpAgent": boardHasSnmpAgent,
       "boardSnmpAgentIpAddr": boardSnmpAgentIpAddr,
       "boardSnmpAgentReadCommunity": boardSnmpAgentReadCommunity,
       "boardSnmpAgentWriteCommunity": boardSnmpAgentWriteCommunity,
       "boardTemperatureHighThresholds": boardTemperatureHighThresholds,
       "boardCpuUsageThresholds": boardCpuUsageThresholds,
       "boardMemoryUsageThresholds": boardMemoryUsageThresholds,
       "boardMemorySize": boardMemorySize,
       "boardTemperatureLowThresholds": boardTemperatureLowThresholds,
       "boardAdminStatus": boardAdminStatus,
       "gwEponPon": gwEponPon,
       "ponPortTable": ponPortTable,
       "ponPortEntry": ponPortEntry,
       "ponPortIndex": ponPortIndex,
       "ponPortIfIndex": ponPortIfIndex,
       "ponPortDot1dBasePort": ponPortDot1dBasePort,
       "ponPortPartnerDev": ponPortPartnerDev,
       "ponPortPartnerBrd": ponPortPartnerBrd,
       "ponPortPartnerPort": ponPortPartnerPort,
       "ponPortProtectionDev": ponPortProtectionDev,
       "ponPortProtectionBrd": ponPortProtectionBrd,
       "ponPortProtectionPort": ponPortProtectionPort,
       "ponPortType": ponPortType,
       "ponPortMaxOnu": ponPortMaxOnu,
       "ponPortCurrOnu": ponPortCurrOnu,
       "ponPortOperStatus": ponPortOperStatus,
       "ponPortAlarmStatus": ponPortAlarmStatus,
       "ponPortAlarmMask": ponPortAlarmMask,
       "ponPortMaxBW": ponPortMaxBW,
       "ponPortActBW": ponPortActBW,
       "ponPortRemainBW": ponPortRemainBW,
       "ponPortApsCtrl": ponPortApsCtrl,
       "ponPortApsStatus": ponPortApsStatus,
       "ponPortEncryptSet": ponPortEncryptSet,
       "ponPortOnuLpbCtrl": ponPortOnuLpbCtrl,
       "ponPortOnuLpbSource": ponPortOnuLpbSource,
       "ponPortOnuLpbTime": ponPortOnuLpbTime,
       "ponPortOnuLpbTxFrms": ponPortOnuLpbTxFrms,
       "ponPortOnuLpbRxFrms": ponPortOnuLpbRxFrms,
       "ponEntLogicalIndex": ponEntLogicalIndex,
       "ponEntLogicalCommunity": ponEntLogicalCommunity,
       "ponPortLinkedOnuCounter": ponPortLinkedOnuCounter,
       "ponPortAdminStatus": ponPortAdminStatus,
       "ponPortReset": ponPortReset,
       "ponPortWindowRange": ponPortWindowRange,
       "ponPortDownlinkPolicingEbl": ponPortDownlinkPolicingEbl,
       "ponPortAllOnuAlmLevel": ponPortAllOnuAlmLevel,
       "ponOnuMapTable": ponOnuMapTable,
       "ponOnuMapEntry": ponOnuMapEntry,
       "mappingOnuIndex": mappingOnuIndex,
       "onuDevIndex": onuDevIndex,
       "onuName": onuName,
       "ponPerfMonTable": ponPerfMonTable,
       "ponPerfMonEntry": ponPerfMonEntry,
       "ponPerfBER": ponPerfBER,
       "ponPerfFER": ponPerfFER,
       "ponPerfBerAlmEnable": ponPerfBerAlmEnable,
       "ponPerfFerAlmEnable": ponPerfFerAlmEnable,
       "ponPerfUpBandwidth": ponPerfUpBandwidth,
       "ponPerfDownBandwidth": ponPerfDownBandwidth,
       "ponHisCtrlTable": ponHisCtrlTable,
       "ponHisCtrlEntry": ponHisCtrlEntry,
       "ponHis15MinuteEnable": ponHis15MinuteEnable,
       "ponHis24HourEnable": ponHis24HourEnable,
       "ponBERThreashold": ponBERThreashold,
       "ponFERThreashold": ponFERThreashold,
       "gwEponPonCtcExt": gwEponPonCtcExt,
       "gwEponPonCtcExtOamDiscoveryTiming": gwEponPonCtcExtOamDiscoveryTiming,
       "gwEponPonCtcExtOamCtcOui": gwEponPonCtcExtOamCtcOui,
       "gwEponPonCtcExtOamCtcVer": gwEponPonCtcExtOamCtcVer,
       "gwEponPonCtcEncrypUpdKeyTime": gwEponPonCtcEncrypUpdKeyTime,
       "gwEponPonCtcEncrypNoReplyTimeout": gwEponPonCtcEncrypNoReplyTimeout,
       "gwEponPonCtcEncrypTimingThreshold": gwEponPonCtcEncrypTimingThreshold,
       "gwEponPonOnuAuth": gwEponPonOnuAuth,
       "onuAuthEnable": onuAuthEnable,
       "onuAuthTable": onuAuthTable,
       "onuAuthEntry": onuAuthEntry,
       "eponBoardIndex": eponBoardIndex,
       "eponPonPortIndex": eponPonPortIndex,
       "onuAuthIndex": onuAuthIndex,
       "onuAuthMacAddress": onuAuthMacAddress,
       "onuAuthRowStatus": onuAuthRowStatus,
       "onuToPonBindingEnable": onuToPonBindingEnable,
       "onuAuthModeTable": onuAuthModeTable,
       "onuAuthModeEntry": onuAuthModeEntry,
       "onuAuthModeBrdIdx": onuAuthModeBrdIdx,
       "onuAuthModePonIdx": onuAuthModePonIdx,
       "onuAuthMode": onuAuthMode,
       "onuAuthEnableForPon": onuAuthEnableForPon,
       "onuAuthEntryReorganize": onuAuthEntryReorganize,
       "onuAuthLoidTable": onuAuthLoidTable,
       "onuAuthLoidEntry": onuAuthLoidEntry,
       "onuAuthLoidBrdIdx": onuAuthLoidBrdIdx,
       "onuAuthLoidPonIdx": onuAuthLoidPonIdx,
       "onuAuthLoidIdx": onuAuthLoidIdx,
       "onuAuthLoid": onuAuthLoid,
       "onuAuthLoidPassword": onuAuthLoidPassword,
       "onuAuthLoidDevIdx": onuAuthLoidDevIdx,
       "onuAuthLoidRowStatus": onuAuthLoidRowStatus,
       "onuUnauthenticatedTable": onuUnauthenticatedTable,
       "onuUnauthenticatedEntry": onuUnauthenticatedEntry,
       "eponUnauthenticatedBoardIndex": eponUnauthenticatedBoardIndex,
       "eponUnauthenticatedPonPortIndex": eponUnauthenticatedPonPortIndex,
       "onuUnauthenticatedIndex": onuUnauthenticatedIndex,
       "onuUnauthenticatedMacAddress": onuUnauthenticatedMacAddress,
       "onuAuthEntryReorganizeForAll": onuAuthEntryReorganizeForAll,
       "gwEponLlid": gwEponLlid,
       "ponLlidTable": ponLlidTable,
       "ponLlidEntry": ponLlidEntry,
       "ponLlidIndex": ponLlidIndex,
       "ponLlidType": ponLlidType,
       "ponLlidOltBoard": ponLlidOltBoard,
       "ponLlidOltPort": ponLlidOltPort,
       "ponLlidOltPortIfIndex": ponLlidOltPortIfIndex,
       "ponLlidOnuPortIfIndex": ponLlidOnuPortIfIndex,
       "ponLlidOnuBoard": ponLlidOnuBoard,
       "ponLlidOnuPort": ponLlidOnuPort,
       "ponLlidLLID": ponLlidLLID,
       "ponLlidIfIndex": ponLlidIfIndex,
       "ponLlidUpFixedBW": ponLlidUpFixedBW,
       "ponLlidDownFixedBW": ponLlidDownFixedBW,
       "ponLlidDesc": ponLlidDesc,
       "ponLlidSurportMacNum": ponLlidSurportMacNum,
       "ponLlidOnuMacAddress": ponLlidOnuMacAddress,
       "ponLlidRowStatus": ponLlidRowStatus,
       "ponLlidUpBWClass": ponLlidUpBWClass,
       "ponLlidUpDelay": ponLlidUpDelay,
       "ponLlidUpAssuredBW": ponLlidUpAssuredBW,
       "ponLlidUpBesteffortBW": ponLlidUpBesteffortBW,
       "ponLlidDownBWClass": ponLlidDownBWClass,
       "ponLlidDownDelay": ponLlidDownDelay,
       "ponLlidDownAssuredBW": ponLlidDownAssuredBW,
       "ponLlidDownBesteffortBW": ponLlidDownBesteffortBW,
       "ponLlidCtcFecAbility": ponLlidCtcFecAbility,
       "ponLlidCtcFecMode": ponLlidCtcFecMode,
       "ponLlidCtcEncrypCtrl": ponLlidCtcEncrypCtrl,
       "ponLlidCtcDbaQueSetNum": ponLlidCtcDbaQueSetNum,
       "ponLlidCtcDbaQueSetCfgStatus": ponLlidCtcDbaQueSetCfgStatus,
       "ponLlidCtcDbaQueSetTable": ponLlidCtcDbaQueSetTable,
       "ponLlidCtcDbaQueSetEntry": ponLlidCtcDbaQueSetEntry,
       "ponLlidCtcDbaQueSetIndex": ponLlidCtcDbaQueSetIndex,
       "ponLlidCtcDbaReportBitmap": ponLlidCtcDbaReportBitmap,
       "ponLlidCtcDbaQueue0Threshold": ponLlidCtcDbaQueue0Threshold,
       "ponLlidCtcDbaQueue1Threshold": ponLlidCtcDbaQueue1Threshold,
       "ponLlidCtcDbaQueue2Threshold": ponLlidCtcDbaQueue2Threshold,
       "ponLlidCtcDbaQueue3Threshold": ponLlidCtcDbaQueue3Threshold,
       "ponLlidCtcDbaQueue4Threshold": ponLlidCtcDbaQueue4Threshold,
       "ponLlidCtcDbaQueue5Threshold": ponLlidCtcDbaQueue5Threshold,
       "ponLlidCtcDbaQueue6Threshold": ponLlidCtcDbaQueue6Threshold,
       "ponLlidCtcDbaQueue7Threshold": ponLlidCtcDbaQueue7Threshold,
       "gwDevTrapGroup": gwDevTrapGroup,
       "onuNewRegSuccess": onuNewRegSuccess,
       "onuReregSuccess": onuReregSuccess,
       "onuNotPresent": onuNotPresent,
       "devPowerOff": devPowerOff,
       "devPowerOn": devPowerOn,
       "cfgDataSaveSuccess": cfgDataSaveSuccess,
       "cfgDataSaveFail": cfgDataSaveFail,
       "flashClearSuccess": flashClearSuccess,
       "flashClearFail": flashClearFail,
       "softwareUpdateSuccess": softwareUpdateSuccess,
       "softwareUpdateFail": softwareUpdateFail,
       "firmwareUpdateSuccess": firmwareUpdateSuccess,
       "firmwareUpdateFail": firmwareUpdateFail,
       "cfgDataBackupSuccess": cfgDataBackupSuccess,
       "cfgDataBackupFail": cfgDataBackupFail,
       "cfgDataRestoreSuccess": cfgDataRestoreSuccess,
       "cfgDataRestoreFail": cfgDataRestoreFail,
       "autoProtectSwitch": autoProtectSwitch,
       "cpuUsageFactorHigh": cpuUsageFactorHigh,
       "ponPortBERAlarm": ponPortBERAlarm,
       "ponPortBERAlarmClear": ponPortBERAlarmClear,
       "ponPortFERAlarm": ponPortFERAlarm,
       "ponPortFERAlarmClear": ponPortFERAlarmClear,
       "llidActBWExceeding": llidActBWExceeding,
       "llidActBWExceedingClear": llidActBWExceedingClear,
       "devBoardInterted": devBoardInterted,
       "devBoardPull": devBoardPull,
       "powerOffAlarm": powerOffAlarm,
       "powerOnAlarm": powerOnAlarm,
       "boardTemperatureHigh": boardTemperatureHigh,
       "boardTemperatureHighClear": boardTemperatureHighClear,
       "ponBoardReset": ponBoardReset,
       "swBoardProtectedSwitch": swBoardProtectedSwitch,
       "ponPortAbnormal": ponPortAbnormal,
       "onuRegisterConflict": onuRegisterConflict,
       "firmwareLoadSuccess": firmwareLoadSuccess,
       "firmwareLoadFailure": firmwareLoadFailure,
       "dbaUpdateSuccess": dbaUpdateSuccess,
       "dbaUpdateFailure": dbaUpdateFailure,
       "dbaLoadSuccess": dbaLoadSuccess,
       "dbaLoadFailure": dbaLoadFailure,
       "ponToEthLinkdown": ponToEthLinkdown,
       "ponToEthLinkup": ponToEthLinkup,
       "onuSoftwareLoadSuccess": onuSoftwareLoadSuccess,
       "onuSoftwareLoadFailure": onuSoftwareLoadFailure,
       "ethLinkdown": ethLinkdown,
       "ethLinkup": ethLinkup,
       "bootUpdateSuccess": bootUpdateSuccess,
       "bootUpdateFailure": bootUpdateFailure,
       "batFileBackupSuccess": batFileBackupSuccess,
       "batFileBackupFailure": batFileBackupFailure,
       "batFileRestoreSuccess": batFileRestoreSuccess,
       "batFileRestoreFailure": batFileRestoreFailure,
       "onuRegAuthFailure": onuRegAuthFailure,
       "deviceColdStart": deviceColdStart,
       "deviceWarmStart": deviceWarmStart,
       "deviceExceptionRestart": deviceExceptionRestart,
       "ethLoopAlarm": ethLoopAlarm,
       "ethLoopAlarmClear": ethLoopAlarmClear,
       "onuLoopAlarm": onuLoopAlarm,
       "onuLoopAlarmClear": onuLoopAlarmClear,
       "backboneEthLinkdown": backboneEthLinkdown,
       "backboneEthLinkup": backboneEthLinkup,
       "boardCpuUsageAlarm": boardCpuUsageAlarm,
       "boardCpuUsageAlarmClear": boardCpuUsageAlarmClear,
       "boardMemoryUsageAlarm": boardMemoryUsageAlarm,
       "boardMemoryUsageAlarmClear": boardMemoryUsageAlarmClear,
       "ponPortFullAlarm": ponPortFullAlarm,
       "ponPortAbnormalClear": ponPortAbnormalClear,
       "ethPortBroadCastFloodControl": ethPortBroadCastFloodControl,
       "ethPortBroadCastFloodControlClear": ethPortBroadCastFloodControlClear,
       "sysfileUploadsuccess": sysfileUploadsuccess,
       "sysfileUploadfailure": sysfileUploadfailure,
       "sysfileDownloadsuccess": sysfileDownloadsuccess,
       "sysfileDownloadfailure": sysfileDownloadfailure,
       "ponPortLosAlarm": ponPortLosAlarm,
       "ponPortLosAlarmClear": ponPortLosAlarmClear,
       "ponFWVersionMismatch": ponFWVersionMismatch,
       "ponFWVersionMatch": ponFWVersionMatch,
       "ponDBAVersionMismatch": ponDBAVersionMismatch,
       "ponDBAVersionMatch": ponDBAVersionMatch,
       "ponSFPTypeMismatch": ponSFPTypeMismatch,
       "ponSFPTypeMitch": ponSFPTypeMitch,
       "ponPortBRASAlarm": ponPortBRASAlarm,
       "ponPortBRASAlarmClear": ponPortBRASAlarmClear,
       "ponPortUpNoTraffic": ponPortUpNoTraffic,
       "ponPortUpNoTrafficClear": ponPortUpNoTrafficClear,
       "onuDeletingNotify": onuDeletingNotify,
       "onuMacTableOverFlow": onuMacTableOverFlow,
       "onuMacTableOverFlowClear": onuMacTableOverFlowClear,
       "gwAlarmLevelGroup": gwAlarmLevelGroup,
       "onuNotPresentAlmLevel": onuNotPresentAlmLevel,
       "devPowerOffAlmLevel": devPowerOffAlmLevel,
       "ponPortBERAlarmLevel": ponPortBERAlarmLevel,
       "ponPortFERAlarmLevel": ponPortFERAlarmLevel,
       "llidActBWExceedingAlarmLevel": llidActBWExceedingAlarmLevel,
       "powerOffAlarmLevel": powerOffAlarmLevel,
       "boardTemperatureHighAlarmLevel": boardTemperatureHighAlarmLevel,
       "devBoardPullAlarmLevel": devBoardPullAlarmLevel,
       "ethLinkdownAlarmLevel": ethLinkdownAlarmLevel,
       "devFanAlarmAlarmLevel": devFanAlarmAlarmLevel,
       "ethFlrAlarmLevel": ethFlrAlarmLevel,
       "ethFerAlarmLevel": ethFerAlarmLevel,
       "ethTransmittalIntermitAlarmLevel": ethTransmittalIntermitAlarmLevel,
       "gwConsoleCfgGroup": gwConsoleCfgGroup,
       "gwConsoleBaudRate": gwConsoleBaudRate,
       "gwConsoleDataBits": gwConsoleDataBits,
       "gwConsoleStopBitSet": gwConsoleStopBitSet,
       "gwConsoleParitySet": gwConsoleParitySet,
       "gwConsoleFlowCtrlSet": gwConsoleFlowCtrlSet}
)
