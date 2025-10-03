# SNMP MIB module (FS-ENTITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fs\FS-ENTITY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:45:46 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fsEntityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21)
)
if mibBuilder.loadTexts:
    fsEntityMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsDeviceMIBObjects_ObjectIdentity = ObjectIdentity
fsDeviceMIBObjects = _FsDeviceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1)
)
_FsDeviceMaxNumber_Type = Integer32
_FsDeviceMaxNumber_Object = MibScalar
fsDeviceMaxNumber = _FsDeviceMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 1),
    _FsDeviceMaxNumber_Type()
)
fsDeviceMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDeviceMaxNumber.setStatus("current")
_FsDeviceInfoTable_Object = MibTable
fsDeviceInfoTable = _FsDeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 2)
)
if mibBuilder.loadTexts:
    fsDeviceInfoTable.setStatus("current")
_FsDeviceInfoEntry_Object = MibTableRow
fsDeviceInfoEntry = _FsDeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 2, 1)
)
fsDeviceInfoEntry.setIndexNames(
    (0, "FS-ENTITY-MIB", "fsDeviceInfoIndex"),
)
if mibBuilder.loadTexts:
    fsDeviceInfoEntry.setStatus("current")
_FsDeviceInfoIndex_Type = Integer32
_FsDeviceInfoIndex_Object = MibTableColumn
fsDeviceInfoIndex = _FsDeviceInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 2, 1, 1),
    _FsDeviceInfoIndex_Type()
)
fsDeviceInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDeviceInfoIndex.setStatus("current")


class _FsDeviceInfoDescr_Type(DisplayString):
    """Custom type fsDeviceInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsDeviceInfoDescr_Type.__name__ = "DisplayString"
_FsDeviceInfoDescr_Object = MibTableColumn
fsDeviceInfoDescr = _FsDeviceInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 2, 1, 2),
    _FsDeviceInfoDescr_Type()
)
fsDeviceInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDeviceInfoDescr.setStatus("current")
_FsDeviceInfoSlotNumber_Type = Integer32
_FsDeviceInfoSlotNumber_Object = MibTableColumn
fsDeviceInfoSlotNumber = _FsDeviceInfoSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 2, 1, 3),
    _FsDeviceInfoSlotNumber_Type()
)
fsDeviceInfoSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDeviceInfoSlotNumber.setStatus("current")


class _FsDevicePowerStatus_Type(Integer32):
    """Custom type fsDevicePowerStatus based on Integer32"""
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
        *(("rpsNoLink", 1),
          ("rpsLinkAndNoPower", 2),
          ("rpsLinkAndReadyForPower", 3),
          ("rpsLinkAndPower", 4))
    )


_FsDevicePowerStatus_Type.__name__ = "Integer32"
_FsDevicePowerStatus_Object = MibTableColumn
fsDevicePowerStatus = _FsDevicePowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 2, 1, 4),
    _FsDevicePowerStatus_Type()
)
fsDevicePowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDevicePowerStatus.setStatus("current")
_FsDeviceMacAddress_Type = MacAddress
_FsDeviceMacAddress_Object = MibTableColumn
fsDeviceMacAddress = _FsDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 2, 1, 5),
    _FsDeviceMacAddress_Type()
)
fsDeviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDeviceMacAddress.setStatus("current")


class _FsDevicePriority_Type(Integer32):
    """Custom type fsDevicePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsDevicePriority_Type.__name__ = "Integer32"
_FsDevicePriority_Object = MibTableColumn
fsDevicePriority = _FsDevicePriority_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 2, 1, 6),
    _FsDevicePriority_Type()
)
fsDevicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDevicePriority.setStatus("current")


class _FsDeviceAlias_Type(DisplayString):
    """Custom type fsDeviceAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsDeviceAlias_Type.__name__ = "DisplayString"
_FsDeviceAlias_Object = MibTableColumn
fsDeviceAlias = _FsDeviceAlias_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 2, 1, 7),
    _FsDeviceAlias_Type()
)
fsDeviceAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDeviceAlias.setStatus("current")


class _FsDeviceSWVersion_Type(DisplayString):
    """Custom type fsDeviceSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsDeviceSWVersion_Type.__name__ = "DisplayString"
_FsDeviceSWVersion_Object = MibTableColumn
fsDeviceSWVersion = _FsDeviceSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 2, 1, 8),
    _FsDeviceSWVersion_Type()
)
fsDeviceSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDeviceSWVersion.setStatus("current")


class _FsDeviceHWVersion_Type(DisplayString):
    """Custom type fsDeviceHWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsDeviceHWVersion_Type.__name__ = "DisplayString"
_FsDeviceHWVersion_Object = MibTableColumn
fsDeviceHWVersion = _FsDeviceHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 2, 1, 9),
    _FsDeviceHWVersion_Type()
)
fsDeviceHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDeviceHWVersion.setStatus("current")


class _FsDeviceSerialNumber_Type(DisplayString):
    """Custom type fsDeviceSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsDeviceSerialNumber_Type.__name__ = "DisplayString"
_FsDeviceSerialNumber_Object = MibTableColumn
fsDeviceSerialNumber = _FsDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 2, 1, 10),
    _FsDeviceSerialNumber_Type()
)
fsDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDeviceSerialNumber.setStatus("current")
_FsDeviceOid_Type = ObjectIdentifier
_FsDeviceOid_Object = MibTableColumn
fsDeviceOid = _FsDeviceOid_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 2, 1, 11),
    _FsDeviceOid_Type()
)
fsDeviceOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDeviceOid.setStatus("current")
_FsSlotInfoTable_Object = MibTable
fsSlotInfoTable = _FsSlotInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 3)
)
if mibBuilder.loadTexts:
    fsSlotInfoTable.setStatus("current")
_FsSlotInfoEntry_Object = MibTableRow
fsSlotInfoEntry = _FsSlotInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 3, 1)
)
fsSlotInfoEntry.setIndexNames(
    (0, "FS-ENTITY-MIB", "fsSlotInfoDeviceIndex"),
    (0, "FS-ENTITY-MIB", "fsSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    fsSlotInfoEntry.setStatus("current")
_FsSlotInfoDeviceIndex_Type = Integer32
_FsSlotInfoDeviceIndex_Object = MibTableColumn
fsSlotInfoDeviceIndex = _FsSlotInfoDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 3, 1, 1),
    _FsSlotInfoDeviceIndex_Type()
)
fsSlotInfoDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSlotInfoDeviceIndex.setStatus("current")
_FsSlotInfoIndex_Type = Integer32
_FsSlotInfoIndex_Object = MibTableColumn
fsSlotInfoIndex = _FsSlotInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 3, 1, 2),
    _FsSlotInfoIndex_Type()
)
fsSlotInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSlotInfoIndex.setStatus("current")
_FsSlotModuleInfoDescr_Type = DisplayString
_FsSlotModuleInfoDescr_Object = MibTableColumn
fsSlotModuleInfoDescr = _FsSlotModuleInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 3, 1, 3),
    _FsSlotModuleInfoDescr_Type()
)
fsSlotModuleInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSlotModuleInfoDescr.setStatus("current")
_FsSlotInfoPortNumber_Type = Integer32
_FsSlotInfoPortNumber_Object = MibTableColumn
fsSlotInfoPortNumber = _FsSlotInfoPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 3, 1, 4),
    _FsSlotInfoPortNumber_Type()
)
fsSlotInfoPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSlotInfoPortNumber.setStatus("current")
_FsSlotInfoPortMaxNumber_Type = Integer32
_FsSlotInfoPortMaxNumber_Object = MibTableColumn
fsSlotInfoPortMaxNumber = _FsSlotInfoPortMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 3, 1, 5),
    _FsSlotInfoPortMaxNumber_Type()
)
fsSlotInfoPortMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSlotInfoPortMaxNumber.setStatus("current")


class _FsSlotInfoDesc_Type(DisplayString):
    """Custom type fsSlotInfoDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsSlotInfoDesc_Type.__name__ = "DisplayString"
_FsSlotInfoDesc_Object = MibTableColumn
fsSlotInfoDesc = _FsSlotInfoDesc_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 3, 1, 6),
    _FsSlotInfoDesc_Type()
)
fsSlotInfoDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSlotInfoDesc.setStatus("current")


class _FsSlotConfigModuleInfoDescr_Type(DisplayString):
    """Custom type fsSlotConfigModuleInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsSlotConfigModuleInfoDescr_Type.__name__ = "DisplayString"
_FsSlotConfigModuleInfoDescr_Object = MibTableColumn
fsSlotConfigModuleInfoDescr = _FsSlotConfigModuleInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 3, 1, 7),
    _FsSlotConfigModuleInfoDescr_Type()
)
fsSlotConfigModuleInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSlotConfigModuleInfoDescr.setStatus("current")
_FsSlotUserStatus_Type = Integer32
_FsSlotUserStatus_Object = MibTableColumn
fsSlotUserStatus = _FsSlotUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 3, 1, 8),
    _FsSlotUserStatus_Type()
)
fsSlotUserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSlotUserStatus.setStatus("current")
_FsSlotSoftwareStatus_Type = Integer32
_FsSlotSoftwareStatus_Object = MibTableColumn
fsSlotSoftwareStatus = _FsSlotSoftwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 3, 1, 9),
    _FsSlotSoftwareStatus_Type()
)
fsSlotSoftwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSlotSoftwareStatus.setStatus("current")


class _FsSlotSerialNumber_Type(DisplayString):
    """Custom type fsSlotSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsSlotSerialNumber_Type.__name__ = "DisplayString"
_FsSlotSerialNumber_Object = MibTableColumn
fsSlotSerialNumber = _FsSlotSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 3, 1, 10),
    _FsSlotSerialNumber_Type()
)
fsSlotSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSlotSerialNumber.setStatus("current")


class _FsSlotHWVersion_Type(DisplayString):
    """Custom type fsSlotHWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsSlotHWVersion_Type.__name__ = "DisplayString"
_FsSlotHWVersion_Object = MibTableColumn
fsSlotHWVersion = _FsSlotHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 3, 1, 11),
    _FsSlotHWVersion_Type()
)
fsSlotHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSlotHWVersion.setStatus("current")
_FsModuleTempStateTable_Object = MibTable
fsModuleTempStateTable = _FsModuleTempStateTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 4)
)
if mibBuilder.loadTexts:
    fsModuleTempStateTable.setStatus("current")
_FsModuleTempStateEntry_Object = MibTableRow
fsModuleTempStateEntry = _FsModuleTempStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 4, 1)
)
fsModuleTempStateEntry.setIndexNames(
    (0, "FS-ENTITY-MIB", "fsModuleTempStateDeviceIndex"),
    (0, "FS-ENTITY-MIB", "fsModuleTempStateIndex"),
)
if mibBuilder.loadTexts:
    fsModuleTempStateEntry.setStatus("current")
_FsModuleTempStateDeviceIndex_Type = Integer32
_FsModuleTempStateDeviceIndex_Object = MibTableColumn
fsModuleTempStateDeviceIndex = _FsModuleTempStateDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 4, 1, 1),
    _FsModuleTempStateDeviceIndex_Type()
)
fsModuleTempStateDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsModuleTempStateDeviceIndex.setStatus("current")
_FsModuleTempStateIndex_Type = Integer32
_FsModuleTempStateIndex_Object = MibTableColumn
fsModuleTempStateIndex = _FsModuleTempStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 4, 1, 2),
    _FsModuleTempStateIndex_Type()
)
fsModuleTempStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsModuleTempStateIndex.setStatus("current")


class _FsModuleTempState_Type(Integer32):
    """Custom type fsModuleTempState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tempNormal", 1),
          ("tempWarning", 2))
    )


_FsModuleTempState_Type.__name__ = "Integer32"
_FsModuleTempState_Object = MibTableColumn
fsModuleTempState = _FsModuleTempState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 4, 1, 3),
    _FsModuleTempState_Type()
)
fsModuleTempState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsModuleTempState.setStatus("current")
_FsPowerStateTable_Object = MibTable
fsPowerStateTable = _FsPowerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 5)
)
if mibBuilder.loadTexts:
    fsPowerStateTable.setStatus("current")
_FsPowerStateEntry_Object = MibTableRow
fsPowerStateEntry = _FsPowerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 5, 1)
)
fsPowerStateEntry.setIndexNames(
    (0, "FS-ENTITY-MIB", "fsPowerStateDeviceIndex"),
    (0, "FS-ENTITY-MIB", "fsPowerStateIndex"),
)
if mibBuilder.loadTexts:
    fsPowerStateEntry.setStatus("current")
_FsPowerStateDeviceIndex_Type = Integer32
_FsPowerStateDeviceIndex_Object = MibTableColumn
fsPowerStateDeviceIndex = _FsPowerStateDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 5, 1, 1),
    _FsPowerStateDeviceIndex_Type()
)
fsPowerStateDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPowerStateDeviceIndex.setStatus("current")
_FsPowerStateIndex_Type = Integer32
_FsPowerStateIndex_Object = MibTableColumn
fsPowerStateIndex = _FsPowerStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 5, 1, 2),
    _FsPowerStateIndex_Type()
)
fsPowerStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPowerStateIndex.setStatus("current")


class _FsPowerState_Type(Integer32):
    """Custom type fsPowerState based on Integer32"""
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
        *(("noLink", 1),
          ("linkAndNoPower", 2),
          ("linkAndReadyForPower", 3),
          ("linkAndPower", 4),
          ("linkAndPowerAbnormal", 5))
    )


_FsPowerState_Type.__name__ = "Integer32"
_FsPowerState_Object = MibTableColumn
fsPowerState = _FsPowerState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 5, 1, 3),
    _FsPowerState_Type()
)
fsPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPowerState.setStatus("current")


class _FsPowerStatePowerDescr_Type(DisplayString):
    """Custom type fsPowerStatePowerDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsPowerStatePowerDescr_Type.__name__ = "DisplayString"
_FsPowerStatePowerDescr_Object = MibTableColumn
fsPowerStatePowerDescr = _FsPowerStatePowerDescr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 5, 1, 4),
    _FsPowerStatePowerDescr_Type()
)
fsPowerStatePowerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPowerStatePowerDescr.setStatus("current")


class _FsPowerStateSerialNumber_Type(DisplayString):
    """Custom type fsPowerStateSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsPowerStateSerialNumber_Type.__name__ = "DisplayString"
_FsPowerStateSerialNumber_Object = MibTableColumn
fsPowerStateSerialNumber = _FsPowerStateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 5, 1, 5),
    _FsPowerStateSerialNumber_Type()
)
fsPowerStateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPowerStateSerialNumber.setStatus("current")
_FsFanStateTable_Object = MibTable
fsFanStateTable = _FsFanStateTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 6)
)
if mibBuilder.loadTexts:
    fsFanStateTable.setStatus("current")
_FsFanStateEntry_Object = MibTableRow
fsFanStateEntry = _FsFanStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 6, 1)
)
fsFanStateEntry.setIndexNames(
    (0, "FS-ENTITY-MIB", "fsFanStateDeviceIndex"),
    (0, "FS-ENTITY-MIB", "fsFanStateIndex"),
)
if mibBuilder.loadTexts:
    fsFanStateEntry.setStatus("current")
_FsFanStateDeviceIndex_Type = Integer32
_FsFanStateDeviceIndex_Object = MibTableColumn
fsFanStateDeviceIndex = _FsFanStateDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 6, 1, 1),
    _FsFanStateDeviceIndex_Type()
)
fsFanStateDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFanStateDeviceIndex.setStatus("current")
_FsFanStateIndex_Type = Integer32
_FsFanStateIndex_Object = MibTableColumn
fsFanStateIndex = _FsFanStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 6, 1, 2),
    _FsFanStateIndex_Type()
)
fsFanStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFanStateIndex.setStatus("current")


class _FsFanState_Type(Integer32):
    """Custom type fsFanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("work", 1),
          ("stop", 2))
    )


_FsFanState_Type.__name__ = "Integer32"
_FsFanState_Object = MibTableColumn
fsFanState = _FsFanState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 6, 1, 3),
    _FsFanState_Type()
)
fsFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFanState.setStatus("current")


class _FsFanStateFanDescr_Type(DisplayString):
    """Custom type fsFanStateFanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsFanStateFanDescr_Type.__name__ = "DisplayString"
_FsFanStateFanDescr_Object = MibTableColumn
fsFanStateFanDescr = _FsFanStateFanDescr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 6, 1, 4),
    _FsFanStateFanDescr_Type()
)
fsFanStateFanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFanStateFanDescr.setStatus("current")


class _FsFanStateSerialNumber_Type(DisplayString):
    """Custom type fsFanStateSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsFanStateSerialNumber_Type.__name__ = "DisplayString"
_FsFanStateSerialNumber_Object = MibTableColumn
fsFanStateSerialNumber = _FsFanStateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 1, 6, 1, 5),
    _FsFanStateSerialNumber_Type()
)
fsFanStateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFanStateSerialNumber.setStatus("current")
_FsEntityMIBTraps_ObjectIdentity = ObjectIdentity
fsEntityMIBTraps = _FsEntityMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 2)
)
_FsEntityStateChgDesc_Type = DisplayString
_FsEntityStateChgDesc_Object = MibScalar
fsEntityStateChgDesc = _FsEntityStateChgDesc_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 2, 1),
    _FsEntityStateChgDesc_Type()
)
fsEntityStateChgDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsEntityStateChgDesc.setStatus("current")


class _FsTemperatureWarningDesc_Type(DisplayString):
    """Custom type fsTemperatureWarningDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsTemperatureWarningDesc_Type.__name__ = "DisplayString"
_FsTemperatureWarningDesc_Object = MibScalar
fsTemperatureWarningDesc = _FsTemperatureWarningDesc_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 2, 3),
    _FsTemperatureWarningDesc_Type()
)
fsTemperatureWarningDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsTemperatureWarningDesc.setStatus("current")
_FsDeviceMIBConformance_ObjectIdentity = ObjectIdentity
fsDeviceMIBConformance = _FsDeviceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 3)
)
_FsDeviceMIBCompliances_ObjectIdentity = ObjectIdentity
fsDeviceMIBCompliances = _FsDeviceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 3, 1)
)
_FsDeviceMIBGroups_ObjectIdentity = ObjectIdentity
fsDeviceMIBGroups = _FsDeviceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 3, 2)
)

# Managed Objects groups

fsDeviceInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 3, 2, 1)
)
fsDeviceInfoMIBGroup.setObjects(
      *(("FS-ENTITY-MIB", "fsDeviceMaxNumber"),
        ("FS-ENTITY-MIB", "fsDeviceInfoIndex"),
        ("FS-ENTITY-MIB", "fsDeviceInfoDescr"),
        ("FS-ENTITY-MIB", "fsDeviceInfoSlotNumber"),
        ("FS-ENTITY-MIB", "fsDevicePowerStatus"))
)
if mibBuilder.loadTexts:
    fsDeviceInfoMIBGroup.setStatus("current")

fsOptionalDevInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 3, 2, 2)
)
fsOptionalDevInfoMIBGroup.setObjects(
      *(("FS-ENTITY-MIB", "fsDeviceMacAddress"),
        ("FS-ENTITY-MIB", "fsDevicePriority"),
        ("FS-ENTITY-MIB", "fsDeviceAlias"),
        ("FS-ENTITY-MIB", "fsDeviceSWVersion"),
        ("FS-ENTITY-MIB", "fsDeviceHWVersion"),
        ("FS-ENTITY-MIB", "fsDeviceSerialNumber"),
        ("FS-ENTITY-MIB", "fsDeviceOid"))
)
if mibBuilder.loadTexts:
    fsOptionalDevInfoMIBGroup.setStatus("current")

fsModuleInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 3, 2, 3)
)
fsModuleInfoMIBGroup.setObjects(
      *(("FS-ENTITY-MIB", "fsSlotInfoDeviceIndex"),
        ("FS-ENTITY-MIB", "fsSlotInfoIndex"),
        ("FS-ENTITY-MIB", "fsSlotModuleInfoDescr"),
        ("FS-ENTITY-MIB", "fsSlotInfoPortNumber"),
        ("FS-ENTITY-MIB", "fsSlotInfoPortMaxNumber"),
        ("FS-ENTITY-MIB", "fsSlotInfoDesc"),
        ("FS-ENTITY-MIB", "fsSlotConfigModuleInfoDescr"),
        ("FS-ENTITY-MIB", "fsSlotUserStatus"),
        ("FS-ENTITY-MIB", "fsSlotSoftwareStatus"),
        ("FS-ENTITY-MIB", "fsSlotSerialNumber"),
        ("FS-ENTITY-MIB", "fsSlotHWVersion"))
)
if mibBuilder.loadTexts:
    fsModuleInfoMIBGroup.setStatus("current")

fsEntityChgDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 3, 2, 4)
)
fsEntityChgDescGroup.setObjects(
    ("FS-ENTITY-MIB", "fsEntityStateChgDesc")
)
if mibBuilder.loadTexts:
    fsEntityChgDescGroup.setStatus("current")

fsModuleTempStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 3, 2, 6)
)
fsModuleTempStateGroup.setObjects(
      *(("FS-ENTITY-MIB", "fsModuleTempStateDeviceIndex"),
        ("FS-ENTITY-MIB", "fsModuleTempStateIndex"),
        ("FS-ENTITY-MIB", "fsModuleTempState"))
)
if mibBuilder.loadTexts:
    fsModuleTempStateGroup.setStatus("current")

fsPowerStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 3, 2, 7)
)
fsPowerStateGroup.setObjects(
      *(("FS-ENTITY-MIB", "fsPowerStateDeviceIndex"),
        ("FS-ENTITY-MIB", "fsPowerStateIndex"),
        ("FS-ENTITY-MIB", "fsPowerState"),
        ("FS-ENTITY-MIB", "fsPowerStatePowerDescr"))
)
if mibBuilder.loadTexts:
    fsPowerStateGroup.setStatus("current")

fsFanStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 3, 2, 8)
)
fsFanStateGroup.setObjects(
      *(("FS-ENTITY-MIB", "fsFanStateDeviceIndex"),
        ("FS-ENTITY-MIB", "fsFanStateIndex"),
        ("FS-ENTITY-MIB", "fsFanState"),
        ("FS-ENTITY-MIB", "fsFanStateFanDescr"))
)
if mibBuilder.loadTexts:
    fsFanStateGroup.setStatus("current")

fsTemperatureWarningDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 3, 2, 9)
)
fsTemperatureWarningDescGroup.setObjects(
    ("FS-ENTITY-MIB", "fsTemperatureWarningDesc")
)
if mibBuilder.loadTexts:
    fsTemperatureWarningDescGroup.setStatus("current")


# Notification objects

fsEntityStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 2, 2)
)
fsEntityStatusChange.setObjects(
    ("FS-ENTITY-MIB", "fsEntityStateChgDesc")
)
if mibBuilder.loadTexts:
    fsEntityStatusChange.setStatus(
        "current"
    )

fsTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 2, 4)
)
fsTemperatureWarning.setObjects(
    ("FS-ENTITY-MIB", "fsTemperatureWarningDesc")
)
if mibBuilder.loadTexts:
    fsTemperatureWarning.setStatus(
        "current"
    )


# Notifications groups

fsDeviceMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 3, 2, 5)
)
fsDeviceMIBNotificationGroup.setObjects(
    ("FS-ENTITY-MIB", "fsEntityStatusChange")
)
if mibBuilder.loadTexts:
    fsDeviceMIBNotificationGroup.setStatus(
        "current"
    )

fsTemperatureWarningGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 3, 2, 10)
)
fsTemperatureWarningGroup.setObjects(
    ("FS-ENTITY-MIB", "fsTemperatureWarning")
)
if mibBuilder.loadTexts:
    fsTemperatureWarningGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsDeviceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 21, 3, 1, 1)
)
fsDeviceMIBCompliance.setObjects(
      *(("FS-ENTITY-MIB", "fsDeviceInfoMIBGroup"),
        ("FS-ENTITY-MIB", "fsModuleInfoMIBGroup"),
        ("FS-ENTITY-MIB", "fsOptionalDevInfoMIBGroup"),
        ("FS-ENTITY-MIB", "fsEntityChgDescGroup"),
        ("FS-ENTITY-MIB", "fsDeviceMIBNotificationGroup"),
        ("FS-ENTITY-MIB", "fsModuleTempStateGroup"),
        ("FS-ENTITY-MIB", "fsPowerStateGroup"),
        ("FS-ENTITY-MIB", "fsFanStateGroup"),
        ("FS-ENTITY-MIB", "fsTemperatureWarningDescGroup"),
        ("FS-ENTITY-MIB", "fsTemperatureWarningGroup"))
)
if mibBuilder.loadTexts:
    fsDeviceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-ENTITY-MIB",
    **{"fsEntityMIB": fsEntityMIB,
       "fsDeviceMIBObjects": fsDeviceMIBObjects,
       "fsDeviceMaxNumber": fsDeviceMaxNumber,
       "fsDeviceInfoTable": fsDeviceInfoTable,
       "fsDeviceInfoEntry": fsDeviceInfoEntry,
       "fsDeviceInfoIndex": fsDeviceInfoIndex,
       "fsDeviceInfoDescr": fsDeviceInfoDescr,
       "fsDeviceInfoSlotNumber": fsDeviceInfoSlotNumber,
       "fsDevicePowerStatus": fsDevicePowerStatus,
       "fsDeviceMacAddress": fsDeviceMacAddress,
       "fsDevicePriority": fsDevicePriority,
       "fsDeviceAlias": fsDeviceAlias,
       "fsDeviceSWVersion": fsDeviceSWVersion,
       "fsDeviceHWVersion": fsDeviceHWVersion,
       "fsDeviceSerialNumber": fsDeviceSerialNumber,
       "fsDeviceOid": fsDeviceOid,
       "fsSlotInfoTable": fsSlotInfoTable,
       "fsSlotInfoEntry": fsSlotInfoEntry,
       "fsSlotInfoDeviceIndex": fsSlotInfoDeviceIndex,
       "fsSlotInfoIndex": fsSlotInfoIndex,
       "fsSlotModuleInfoDescr": fsSlotModuleInfoDescr,
       "fsSlotInfoPortNumber": fsSlotInfoPortNumber,
       "fsSlotInfoPortMaxNumber": fsSlotInfoPortMaxNumber,
       "fsSlotInfoDesc": fsSlotInfoDesc,
       "fsSlotConfigModuleInfoDescr": fsSlotConfigModuleInfoDescr,
       "fsSlotUserStatus": fsSlotUserStatus,
       "fsSlotSoftwareStatus": fsSlotSoftwareStatus,
       "fsSlotSerialNumber": fsSlotSerialNumber,
       "fsSlotHWVersion": fsSlotHWVersion,
       "fsModuleTempStateTable": fsModuleTempStateTable,
       "fsModuleTempStateEntry": fsModuleTempStateEntry,
       "fsModuleTempStateDeviceIndex": fsModuleTempStateDeviceIndex,
       "fsModuleTempStateIndex": fsModuleTempStateIndex,
       "fsModuleTempState": fsModuleTempState,
       "fsPowerStateTable": fsPowerStateTable,
       "fsPowerStateEntry": fsPowerStateEntry,
       "fsPowerStateDeviceIndex": fsPowerStateDeviceIndex,
       "fsPowerStateIndex": fsPowerStateIndex,
       "fsPowerState": fsPowerState,
       "fsPowerStatePowerDescr": fsPowerStatePowerDescr,
       "fsPowerStateSerialNumber": fsPowerStateSerialNumber,
       "fsFanStateTable": fsFanStateTable,
       "fsFanStateEntry": fsFanStateEntry,
       "fsFanStateDeviceIndex": fsFanStateDeviceIndex,
       "fsFanStateIndex": fsFanStateIndex,
       "fsFanState": fsFanState,
       "fsFanStateFanDescr": fsFanStateFanDescr,
       "fsFanStateSerialNumber": fsFanStateSerialNumber,
       "fsEntityMIBTraps": fsEntityMIBTraps,
       "fsEntityStateChgDesc": fsEntityStateChgDesc,
       "fsEntityStatusChange": fsEntityStatusChange,
       "fsTemperatureWarningDesc": fsTemperatureWarningDesc,
       "fsTemperatureWarning": fsTemperatureWarning,
       "fsDeviceMIBConformance": fsDeviceMIBConformance,
       "fsDeviceMIBCompliances": fsDeviceMIBCompliances,
       "fsDeviceMIBCompliance": fsDeviceMIBCompliance,
       "fsDeviceMIBGroups": fsDeviceMIBGroups,
       "fsDeviceInfoMIBGroup": fsDeviceInfoMIBGroup,
       "fsOptionalDevInfoMIBGroup": fsOptionalDevInfoMIBGroup,
       "fsModuleInfoMIBGroup": fsModuleInfoMIBGroup,
       "fsEntityChgDescGroup": fsEntityChgDescGroup,
       "fsDeviceMIBNotificationGroup": fsDeviceMIBNotificationGroup,
       "fsModuleTempStateGroup": fsModuleTempStateGroup,
       "fsPowerStateGroup": fsPowerStateGroup,
       "fsFanStateGroup": fsFanStateGroup,
       "fsTemperatureWarningDescGroup": fsTemperatureWarningDescGroup,
       "fsTemperatureWarningGroup": fsTemperatureWarningGroup}
)
