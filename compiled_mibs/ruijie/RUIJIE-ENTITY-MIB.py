# SNMP MIB module (RUIJIE-ENTITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ruijie\RUIJIE-ENTITY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:24:14 2025
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

(entPhysicalName,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalName")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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

ruijieEntityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21)
)
if mibBuilder.loadTexts:
    ruijieEntityMIB.setRevisions(
        ("2021-09-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieDeviceMIBObjects_ObjectIdentity = ObjectIdentity
ruijieDeviceMIBObjects = _RuijieDeviceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1)
)
_RuijieDeviceMaxNumber_Type = Integer32
_RuijieDeviceMaxNumber_Object = MibScalar
ruijieDeviceMaxNumber = _RuijieDeviceMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 1),
    _RuijieDeviceMaxNumber_Type()
)
ruijieDeviceMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceMaxNumber.setStatus("current")
_RuijieDeviceInfoTable_Object = MibTable
ruijieDeviceInfoTable = _RuijieDeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieDeviceInfoTable.setStatus("current")
_RuijieDeviceInfoEntry_Object = MibTableRow
ruijieDeviceInfoEntry = _RuijieDeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1)
)
ruijieDeviceInfoEntry.setIndexNames(
    (0, "RUIJIE-ENTITY-MIB", "ruijieDeviceInfoIndex"),
)
if mibBuilder.loadTexts:
    ruijieDeviceInfoEntry.setStatus("current")


class _RuijieDeviceInfoIndex_Type(Integer32):
    """Custom type ruijieDeviceInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieDeviceInfoIndex_Type.__name__ = "Integer32"
_RuijieDeviceInfoIndex_Object = MibTableColumn
ruijieDeviceInfoIndex = _RuijieDeviceInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 1),
    _RuijieDeviceInfoIndex_Type()
)
ruijieDeviceInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceInfoIndex.setStatus("current")


class _RuijieDeviceInfoDescr_Type(DisplayString):
    """Custom type ruijieDeviceInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieDeviceInfoDescr_Type.__name__ = "DisplayString"
_RuijieDeviceInfoDescr_Object = MibTableColumn
ruijieDeviceInfoDescr = _RuijieDeviceInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 2),
    _RuijieDeviceInfoDescr_Type()
)
ruijieDeviceInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceInfoDescr.setStatus("current")
_RuijieDeviceInfoSlotNumber_Type = Integer32
_RuijieDeviceInfoSlotNumber_Object = MibTableColumn
ruijieDeviceInfoSlotNumber = _RuijieDeviceInfoSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 3),
    _RuijieDeviceInfoSlotNumber_Type()
)
ruijieDeviceInfoSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceInfoSlotNumber.setStatus("current")


class _RuijieDevicePowerStatus_Type(Integer32):
    """Custom type ruijieDevicePowerStatus based on Integer32"""
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


_RuijieDevicePowerStatus_Type.__name__ = "Integer32"
_RuijieDevicePowerStatus_Object = MibTableColumn
ruijieDevicePowerStatus = _RuijieDevicePowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 4),
    _RuijieDevicePowerStatus_Type()
)
ruijieDevicePowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDevicePowerStatus.setStatus("current")
_RuijieDeviceMacAddress_Type = MacAddress
_RuijieDeviceMacAddress_Object = MibTableColumn
ruijieDeviceMacAddress = _RuijieDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 5),
    _RuijieDeviceMacAddress_Type()
)
ruijieDeviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceMacAddress.setStatus("current")


class _RuijieDevicePriority_Type(Integer32):
    """Custom type ruijieDevicePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RuijieDevicePriority_Type.__name__ = "Integer32"
_RuijieDevicePriority_Object = MibTableColumn
ruijieDevicePriority = _RuijieDevicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 6),
    _RuijieDevicePriority_Type()
)
ruijieDevicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDevicePriority.setStatus("current")


class _RuijieDeviceAlias_Type(DisplayString):
    """Custom type ruijieDeviceAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieDeviceAlias_Type.__name__ = "DisplayString"
_RuijieDeviceAlias_Object = MibTableColumn
ruijieDeviceAlias = _RuijieDeviceAlias_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 7),
    _RuijieDeviceAlias_Type()
)
ruijieDeviceAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDeviceAlias.setStatus("current")


class _RuijieDeviceSWVersion_Type(DisplayString):
    """Custom type ruijieDeviceSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieDeviceSWVersion_Type.__name__ = "DisplayString"
_RuijieDeviceSWVersion_Object = MibTableColumn
ruijieDeviceSWVersion = _RuijieDeviceSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 8),
    _RuijieDeviceSWVersion_Type()
)
ruijieDeviceSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceSWVersion.setStatus("current")


class _RuijieDeviceHWVersion_Type(DisplayString):
    """Custom type ruijieDeviceHWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieDeviceHWVersion_Type.__name__ = "DisplayString"
_RuijieDeviceHWVersion_Object = MibTableColumn
ruijieDeviceHWVersion = _RuijieDeviceHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 9),
    _RuijieDeviceHWVersion_Type()
)
ruijieDeviceHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceHWVersion.setStatus("current")


class _RuijieDeviceSerialNumber_Type(DisplayString):
    """Custom type ruijieDeviceSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieDeviceSerialNumber_Type.__name__ = "DisplayString"
_RuijieDeviceSerialNumber_Object = MibTableColumn
ruijieDeviceSerialNumber = _RuijieDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 10),
    _RuijieDeviceSerialNumber_Type()
)
ruijieDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceSerialNumber.setStatus("current")
_RuijieDeviceOid_Type = ObjectIdentifier
_RuijieDeviceOid_Object = MibTableColumn
ruijieDeviceOid = _RuijieDeviceOid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 11),
    _RuijieDeviceOid_Type()
)
ruijieDeviceOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceOid.setStatus("current")


class _RuijieDeviceProductionDate_Type(DisplayString):
    """Custom type ruijieDeviceProductionDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RuijieDeviceProductionDate_Type.__name__ = "DisplayString"
_RuijieDeviceProductionDate_Object = MibTableColumn
ruijieDeviceProductionDate = _RuijieDeviceProductionDate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 12),
    _RuijieDeviceProductionDate_Type()
)
ruijieDeviceProductionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceProductionDate.setStatus("current")
_RuijieDeviceOutPower_Type = Integer32
_RuijieDeviceOutPower_Object = MibTableColumn
ruijieDeviceOutPower = _RuijieDeviceOutPower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 13),
    _RuijieDeviceOutPower_Type()
)
ruijieDeviceOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceOutPower.setStatus("current")
_RuijieSlotInfoTable_Object = MibTable
ruijieSlotInfoTable = _RuijieSlotInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieSlotInfoTable.setStatus("current")
_RuijieSlotInfoEntry_Object = MibTableRow
ruijieSlotInfoEntry = _RuijieSlotInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1)
)
ruijieSlotInfoEntry.setIndexNames(
    (0, "RUIJIE-ENTITY-MIB", "ruijieSlotInfoDeviceIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijieSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    ruijieSlotInfoEntry.setStatus("current")


class _RuijieSlotInfoDeviceIndex_Type(Integer32):
    """Custom type ruijieSlotInfoDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieSlotInfoDeviceIndex_Type.__name__ = "Integer32"
_RuijieSlotInfoDeviceIndex_Object = MibTableColumn
ruijieSlotInfoDeviceIndex = _RuijieSlotInfoDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 1),
    _RuijieSlotInfoDeviceIndex_Type()
)
ruijieSlotInfoDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotInfoDeviceIndex.setStatus("current")


class _RuijieSlotInfoIndex_Type(Integer32):
    """Custom type ruijieSlotInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieSlotInfoIndex_Type.__name__ = "Integer32"
_RuijieSlotInfoIndex_Object = MibTableColumn
ruijieSlotInfoIndex = _RuijieSlotInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 2),
    _RuijieSlotInfoIndex_Type()
)
ruijieSlotInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotInfoIndex.setStatus("current")
_RuijieSlotModuleInfoDescr_Type = DisplayString
_RuijieSlotModuleInfoDescr_Object = MibTableColumn
ruijieSlotModuleInfoDescr = _RuijieSlotModuleInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 3),
    _RuijieSlotModuleInfoDescr_Type()
)
ruijieSlotModuleInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotModuleInfoDescr.setStatus("current")
_RuijieSlotInfoPortNumber_Type = Integer32
_RuijieSlotInfoPortNumber_Object = MibTableColumn
ruijieSlotInfoPortNumber = _RuijieSlotInfoPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 4),
    _RuijieSlotInfoPortNumber_Type()
)
ruijieSlotInfoPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotInfoPortNumber.setStatus("current")
_RuijieSlotInfoPortMaxNumber_Type = Integer32
_RuijieSlotInfoPortMaxNumber_Object = MibTableColumn
ruijieSlotInfoPortMaxNumber = _RuijieSlotInfoPortMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 5),
    _RuijieSlotInfoPortMaxNumber_Type()
)
ruijieSlotInfoPortMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotInfoPortMaxNumber.setStatus("current")


class _RuijieSlotInfoDesc_Type(DisplayString):
    """Custom type ruijieSlotInfoDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieSlotInfoDesc_Type.__name__ = "DisplayString"
_RuijieSlotInfoDesc_Object = MibTableColumn
ruijieSlotInfoDesc = _RuijieSlotInfoDesc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 6),
    _RuijieSlotInfoDesc_Type()
)
ruijieSlotInfoDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotInfoDesc.setStatus("current")


class _RuijieSlotConfigModuleInfoDescr_Type(DisplayString):
    """Custom type ruijieSlotConfigModuleInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieSlotConfigModuleInfoDescr_Type.__name__ = "DisplayString"
_RuijieSlotConfigModuleInfoDescr_Object = MibTableColumn
ruijieSlotConfigModuleInfoDescr = _RuijieSlotConfigModuleInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 7),
    _RuijieSlotConfigModuleInfoDescr_Type()
)
ruijieSlotConfigModuleInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotConfigModuleInfoDescr.setStatus("current")
_RuijieSlotUserStatus_Type = Integer32
_RuijieSlotUserStatus_Object = MibTableColumn
ruijieSlotUserStatus = _RuijieSlotUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 8),
    _RuijieSlotUserStatus_Type()
)
ruijieSlotUserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotUserStatus.setStatus("current")
_RuijieSlotSoftwareStatus_Type = Integer32
_RuijieSlotSoftwareStatus_Object = MibTableColumn
ruijieSlotSoftwareStatus = _RuijieSlotSoftwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 9),
    _RuijieSlotSoftwareStatus_Type()
)
ruijieSlotSoftwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotSoftwareStatus.setStatus("current")


class _RuijieSlotSerialNumber_Type(DisplayString):
    """Custom type ruijieSlotSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieSlotSerialNumber_Type.__name__ = "DisplayString"
_RuijieSlotSerialNumber_Object = MibTableColumn
ruijieSlotSerialNumber = _RuijieSlotSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 10),
    _RuijieSlotSerialNumber_Type()
)
ruijieSlotSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotSerialNumber.setStatus("current")


class _RuijieSlotHWVersion_Type(DisplayString):
    """Custom type ruijieSlotHWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieSlotHWVersion_Type.__name__ = "DisplayString"
_RuijieSlotHWVersion_Object = MibTableColumn
ruijieSlotHWVersion = _RuijieSlotHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 11),
    _RuijieSlotHWVersion_Type()
)
ruijieSlotHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotHWVersion.setStatus("current")


class _SlotSocID_Type(DisplayString):
    """Custom type slotSocID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SlotSocID_Type.__name__ = "DisplayString"
_SlotSocID_Object = MibTableColumn
slotSocID = _SlotSocID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 12),
    _SlotSocID_Type()
)
slotSocID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotSocID.setStatus("current")


class _RuijieSlotServiceState_Type(Integer32):
    """Custom type ruijieSlotServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2),
          ("servNA", 3))
    )


_RuijieSlotServiceState_Type.__name__ = "Integer32"
_RuijieSlotServiceState_Object = MibTableColumn
ruijieSlotServiceState = _RuijieSlotServiceState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 13),
    _RuijieSlotServiceState_Type()
)
ruijieSlotServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotServiceState.setStatus("current")


class _RuijieSlotModuleProductionDate_Type(DisplayString):
    """Custom type ruijieSlotModuleProductionDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RuijieSlotModuleProductionDate_Type.__name__ = "DisplayString"
_RuijieSlotModuleProductionDate_Object = MibTableColumn
ruijieSlotModuleProductionDate = _RuijieSlotModuleProductionDate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 14),
    _RuijieSlotModuleProductionDate_Type()
)
ruijieSlotModuleProductionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotModuleProductionDate.setStatus("current")


class _RuijieSlotSoftwareVersion_Type(DisplayString):
    """Custom type ruijieSlotSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieSlotSoftwareVersion_Type.__name__ = "DisplayString"
_RuijieSlotSoftwareVersion_Object = MibTableColumn
ruijieSlotSoftwareVersion = _RuijieSlotSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 15),
    _RuijieSlotSoftwareVersion_Type()
)
ruijieSlotSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotSoftwareVersion.setStatus("current")
_RuijieModuleTempStateTable_Object = MibTable
ruijieModuleTempStateTable = _RuijieModuleTempStateTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieModuleTempStateTable.setStatus("current")
_RuijieModuleTempStateEntry_Object = MibTableRow
ruijieModuleTempStateEntry = _RuijieModuleTempStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 4, 1)
)
ruijieModuleTempStateEntry.setIndexNames(
    (0, "RUIJIE-ENTITY-MIB", "ruijieModuleTempStateDeviceIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijieModuleTempStateIndex"),
)
if mibBuilder.loadTexts:
    ruijieModuleTempStateEntry.setStatus("current")


class _RuijieModuleTempStateDeviceIndex_Type(Integer32):
    """Custom type ruijieModuleTempStateDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieModuleTempStateDeviceIndex_Type.__name__ = "Integer32"
_RuijieModuleTempStateDeviceIndex_Object = MibTableColumn
ruijieModuleTempStateDeviceIndex = _RuijieModuleTempStateDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 4, 1, 1),
    _RuijieModuleTempStateDeviceIndex_Type()
)
ruijieModuleTempStateDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieModuleTempStateDeviceIndex.setStatus("current")


class _RuijieModuleTempStateIndex_Type(Integer32):
    """Custom type ruijieModuleTempStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieModuleTempStateIndex_Type.__name__ = "Integer32"
_RuijieModuleTempStateIndex_Object = MibTableColumn
ruijieModuleTempStateIndex = _RuijieModuleTempStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 4, 1, 2),
    _RuijieModuleTempStateIndex_Type()
)
ruijieModuleTempStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieModuleTempStateIndex.setStatus("current")


class _RuijieModuleTempState_Type(Integer32):
    """Custom type ruijieModuleTempState based on Integer32"""
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


_RuijieModuleTempState_Type.__name__ = "Integer32"
_RuijieModuleTempState_Object = MibTableColumn
ruijieModuleTempState = _RuijieModuleTempState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 4, 1, 3),
    _RuijieModuleTempState_Type()
)
ruijieModuleTempState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieModuleTempState.setStatus("current")
_RuijiePowerStateTable_Object = MibTable
ruijiePowerStateTable = _RuijiePowerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 5)
)
if mibBuilder.loadTexts:
    ruijiePowerStateTable.setStatus("current")
_RuijiePowerStateEntry_Object = MibTableRow
ruijiePowerStateEntry = _RuijiePowerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 5, 1)
)
ruijiePowerStateEntry.setIndexNames(
    (0, "RUIJIE-ENTITY-MIB", "ruijiePowerStateDeviceIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijiePowerStateIndex"),
)
if mibBuilder.loadTexts:
    ruijiePowerStateEntry.setStatus("current")


class _RuijiePowerStateDeviceIndex_Type(Integer32):
    """Custom type ruijiePowerStateDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijiePowerStateDeviceIndex_Type.__name__ = "Integer32"
_RuijiePowerStateDeviceIndex_Object = MibTableColumn
ruijiePowerStateDeviceIndex = _RuijiePowerStateDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 5, 1, 1),
    _RuijiePowerStateDeviceIndex_Type()
)
ruijiePowerStateDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePowerStateDeviceIndex.setStatus("current")


class _RuijiePowerStateIndex_Type(Integer32):
    """Custom type ruijiePowerStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijiePowerStateIndex_Type.__name__ = "Integer32"
_RuijiePowerStateIndex_Object = MibTableColumn
ruijiePowerStateIndex = _RuijiePowerStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 5, 1, 2),
    _RuijiePowerStateIndex_Type()
)
ruijiePowerStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePowerStateIndex.setStatus("current")


class _RuijiePowerState_Type(Integer32):
    """Custom type ruijiePowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("noLink", 1),
          ("linkAndNoPower", 2),
          ("linkAndReadyForPower", 3),
          ("linkAndPower", 4),
          ("linkAndPowerAbnormal", 5),
          ("linkAndUnknow", 6),
          ("linkAndLineFail", 7))
    )


_RuijiePowerState_Type.__name__ = "Integer32"
_RuijiePowerState_Object = MibTableColumn
ruijiePowerState = _RuijiePowerState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 5, 1, 3),
    _RuijiePowerState_Type()
)
ruijiePowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePowerState.setStatus("current")


class _RuijiePowerStatePowerDescr_Type(DisplayString):
    """Custom type ruijiePowerStatePowerDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijiePowerStatePowerDescr_Type.__name__ = "DisplayString"
_RuijiePowerStatePowerDescr_Object = MibTableColumn
ruijiePowerStatePowerDescr = _RuijiePowerStatePowerDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 5, 1, 4),
    _RuijiePowerStatePowerDescr_Type()
)
ruijiePowerStatePowerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePowerStatePowerDescr.setStatus("current")


class _RuijiePowerStateSerialNumber_Type(DisplayString):
    """Custom type ruijiePowerStateSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijiePowerStateSerialNumber_Type.__name__ = "DisplayString"
_RuijiePowerStateSerialNumber_Object = MibTableColumn
ruijiePowerStateSerialNumber = _RuijiePowerStateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 5, 1, 5),
    _RuijiePowerStateSerialNumber_Type()
)
ruijiePowerStateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePowerStateSerialNumber.setStatus("current")
_RuijieFanStateTable_Object = MibTable
ruijieFanStateTable = _RuijieFanStateTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieFanStateTable.setStatus("current")
_RuijieFanStateEntry_Object = MibTableRow
ruijieFanStateEntry = _RuijieFanStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 6, 1)
)
ruijieFanStateEntry.setIndexNames(
    (0, "RUIJIE-ENTITY-MIB", "ruijieFanStateDeviceIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijieFanStateIndex"),
)
if mibBuilder.loadTexts:
    ruijieFanStateEntry.setStatus("current")


class _RuijieFanStateDeviceIndex_Type(Integer32):
    """Custom type ruijieFanStateDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieFanStateDeviceIndex_Type.__name__ = "Integer32"
_RuijieFanStateDeviceIndex_Object = MibTableColumn
ruijieFanStateDeviceIndex = _RuijieFanStateDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 6, 1, 1),
    _RuijieFanStateDeviceIndex_Type()
)
ruijieFanStateDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFanStateDeviceIndex.setStatus("current")


class _RuijieFanStateIndex_Type(Integer32):
    """Custom type ruijieFanStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieFanStateIndex_Type.__name__ = "Integer32"
_RuijieFanStateIndex_Object = MibTableColumn
ruijieFanStateIndex = _RuijieFanStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 6, 1, 2),
    _RuijieFanStateIndex_Type()
)
ruijieFanStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFanStateIndex.setStatus("current")


class _RuijieFanState_Type(Integer32):
    """Custom type ruijieFanState based on Integer32"""
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


_RuijieFanState_Type.__name__ = "Integer32"
_RuijieFanState_Object = MibTableColumn
ruijieFanState = _RuijieFanState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 6, 1, 3),
    _RuijieFanState_Type()
)
ruijieFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFanState.setStatus("current")


class _RuijieFanStateFanDescr_Type(DisplayString):
    """Custom type ruijieFanStateFanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieFanStateFanDescr_Type.__name__ = "DisplayString"
_RuijieFanStateFanDescr_Object = MibTableColumn
ruijieFanStateFanDescr = _RuijieFanStateFanDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 6, 1, 4),
    _RuijieFanStateFanDescr_Type()
)
ruijieFanStateFanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFanStateFanDescr.setStatus("current")


class _RuijieFanStateSerialNumber_Type(DisplayString):
    """Custom type ruijieFanStateSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieFanStateSerialNumber_Type.__name__ = "DisplayString"
_RuijieFanStateSerialNumber_Object = MibTableColumn
ruijieFanStateSerialNumber = _RuijieFanStateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 6, 1, 5),
    _RuijieFanStateSerialNumber_Type()
)
ruijieFanStateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFanStateSerialNumber.setStatus("current")
_RuijieHolderInfoTable_Object = MibTable
ruijieHolderInfoTable = _RuijieHolderInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 7)
)
if mibBuilder.loadTexts:
    ruijieHolderInfoTable.setStatus("current")
_RuijieHolderInfoEntry_Object = MibTableRow
ruijieHolderInfoEntry = _RuijieHolderInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 7, 1)
)
ruijieHolderInfoEntry.setIndexNames(
    (0, "RUIJIE-ENTITY-MIB", "ruijieHolderInfoDeviceIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijieHolderInfoSlotIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijieHolderInfoSubSlotIndex"),
)
if mibBuilder.loadTexts:
    ruijieHolderInfoEntry.setStatus("current")


class _RuijieHolderInfoDeviceIndex_Type(Integer32):
    """Custom type ruijieHolderInfoDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieHolderInfoDeviceIndex_Type.__name__ = "Integer32"
_RuijieHolderInfoDeviceIndex_Object = MibTableColumn
ruijieHolderInfoDeviceIndex = _RuijieHolderInfoDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 7, 1, 1),
    _RuijieHolderInfoDeviceIndex_Type()
)
ruijieHolderInfoDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHolderInfoDeviceIndex.setStatus("current")


class _RuijieHolderInfoSlotIndex_Type(Integer32):
    """Custom type ruijieHolderInfoSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieHolderInfoSlotIndex_Type.__name__ = "Integer32"
_RuijieHolderInfoSlotIndex_Object = MibTableColumn
ruijieHolderInfoSlotIndex = _RuijieHolderInfoSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 7, 1, 2),
    _RuijieHolderInfoSlotIndex_Type()
)
ruijieHolderInfoSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHolderInfoSlotIndex.setStatus("current")


class _RuijieHolderInfoSubSlotIndex_Type(Integer32):
    """Custom type ruijieHolderInfoSubSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieHolderInfoSubSlotIndex_Type.__name__ = "Integer32"
_RuijieHolderInfoSubSlotIndex_Object = MibTableColumn
ruijieHolderInfoSubSlotIndex = _RuijieHolderInfoSubSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 7, 1, 3),
    _RuijieHolderInfoSubSlotIndex_Type()
)
ruijieHolderInfoSubSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHolderInfoSubSlotIndex.setStatus("current")
_RuijieHolderNumber_Type = Integer32
_RuijieHolderNumber_Object = MibTableColumn
ruijieHolderNumber = _RuijieHolderNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 7, 1, 4),
    _RuijieHolderNumber_Type()
)
ruijieHolderNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHolderNumber.setStatus("current")


class _RuijieHolderState_Type(Integer32):
    """Custom type ruijieHolderState based on Integer32"""
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
        *(("empty", 1),
          ("installed", 2),
          ("unavailable", 3),
          ("unknown", 4))
    )


_RuijieHolderState_Type.__name__ = "Integer32"
_RuijieHolderState_Object = MibTableColumn
ruijieHolderState = _RuijieHolderState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 7, 1, 5),
    _RuijieHolderState_Type()
)
ruijieHolderState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHolderState.setStatus("current")


class _RuijieHolderType_Type(Integer32):
    """Custom type ruijieHolderType based on Integer32"""
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
        *(("rack", 1),
          ("subRack", 2),
          ("shelf", 3),
          ("subShelf", 4),
          ("slot", 5),
          ("subSlot", 6))
    )


_RuijieHolderType_Type.__name__ = "Integer32"
_RuijieHolderType_Object = MibTableColumn
ruijieHolderType = _RuijieHolderType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 7, 1, 6),
    _RuijieHolderType_Type()
)
ruijieHolderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHolderType.setStatus("current")


class _RuijieHolderName_Type(DisplayString):
    """Custom type ruijieHolderName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHolderName_Type.__name__ = "DisplayString"
_RuijieHolderName_Object = MibTableColumn
ruijieHolderName = _RuijieHolderName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 7, 1, 7),
    _RuijieHolderName_Type()
)
ruijieHolderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHolderName.setStatus("current")
_RuijieSubslotInfoTable_Object = MibTable
ruijieSubslotInfoTable = _RuijieSubslotInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 8)
)
if mibBuilder.loadTexts:
    ruijieSubslotInfoTable.setStatus("current")
_RuijieSubslotInfoEntry_Object = MibTableRow
ruijieSubslotInfoEntry = _RuijieSubslotInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 8, 1)
)
ruijieSubslotInfoEntry.setIndexNames(
    (0, "RUIJIE-ENTITY-MIB", "ruijieSubslotInfoDeviceIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijieSubslotInfoSlotIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijieSubslotInfoIndex"),
)
if mibBuilder.loadTexts:
    ruijieSubslotInfoEntry.setStatus("current")


class _RuijieSubslotInfoDeviceIndex_Type(Integer32):
    """Custom type ruijieSubslotInfoDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieSubslotInfoDeviceIndex_Type.__name__ = "Integer32"
_RuijieSubslotInfoDeviceIndex_Object = MibTableColumn
ruijieSubslotInfoDeviceIndex = _RuijieSubslotInfoDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 8, 1, 1),
    _RuijieSubslotInfoDeviceIndex_Type()
)
ruijieSubslotInfoDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSubslotInfoDeviceIndex.setStatus("current")


class _RuijieSubslotInfoSlotIndex_Type(Integer32):
    """Custom type ruijieSubslotInfoSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieSubslotInfoSlotIndex_Type.__name__ = "Integer32"
_RuijieSubslotInfoSlotIndex_Object = MibTableColumn
ruijieSubslotInfoSlotIndex = _RuijieSubslotInfoSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 8, 1, 2),
    _RuijieSubslotInfoSlotIndex_Type()
)
ruijieSubslotInfoSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSubslotInfoSlotIndex.setStatus("current")


class _RuijieSubslotInfoIndex_Type(Integer32):
    """Custom type ruijieSubslotInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieSubslotInfoIndex_Type.__name__ = "Integer32"
_RuijieSubslotInfoIndex_Object = MibTableColumn
ruijieSubslotInfoIndex = _RuijieSubslotInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 8, 1, 3),
    _RuijieSubslotInfoIndex_Type()
)
ruijieSubslotInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSubslotInfoIndex.setStatus("current")
_RuijieSubslotModuleInfoDescr_Type = DisplayString
_RuijieSubslotModuleInfoDescr_Object = MibTableColumn
ruijieSubslotModuleInfoDescr = _RuijieSubslotModuleInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 8, 1, 4),
    _RuijieSubslotModuleInfoDescr_Type()
)
ruijieSubslotModuleInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSubslotModuleInfoDescr.setStatus("current")
_RuijieSubslotInfoPortNumber_Type = Integer32
_RuijieSubslotInfoPortNumber_Object = MibTableColumn
ruijieSubslotInfoPortNumber = _RuijieSubslotInfoPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 8, 1, 5),
    _RuijieSubslotInfoPortNumber_Type()
)
ruijieSubslotInfoPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSubslotInfoPortNumber.setStatus("current")
_RuijieSubslotInfoPortMaxNumber_Type = Integer32
_RuijieSubslotInfoPortMaxNumber_Object = MibTableColumn
ruijieSubslotInfoPortMaxNumber = _RuijieSubslotInfoPortMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 8, 1, 6),
    _RuijieSubslotInfoPortMaxNumber_Type()
)
ruijieSubslotInfoPortMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSubslotInfoPortMaxNumber.setStatus("current")


class _RuijieSubslotInfoDesc_Type(DisplayString):
    """Custom type ruijieSubslotInfoDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieSubslotInfoDesc_Type.__name__ = "DisplayString"
_RuijieSubslotInfoDesc_Object = MibTableColumn
ruijieSubslotInfoDesc = _RuijieSubslotInfoDesc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 8, 1, 7),
    _RuijieSubslotInfoDesc_Type()
)
ruijieSubslotInfoDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSubslotInfoDesc.setStatus("current")


class _RuijieSubslotConfigModuleInfoDescr_Type(DisplayString):
    """Custom type ruijieSubslotConfigModuleInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieSubslotConfigModuleInfoDescr_Type.__name__ = "DisplayString"
_RuijieSubslotConfigModuleInfoDescr_Object = MibTableColumn
ruijieSubslotConfigModuleInfoDescr = _RuijieSubslotConfigModuleInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 8, 1, 8),
    _RuijieSubslotConfigModuleInfoDescr_Type()
)
ruijieSubslotConfigModuleInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSubslotConfigModuleInfoDescr.setStatus("current")
_RuijieSubslotUserStatus_Type = Integer32
_RuijieSubslotUserStatus_Object = MibTableColumn
ruijieSubslotUserStatus = _RuijieSubslotUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 8, 1, 9),
    _RuijieSubslotUserStatus_Type()
)
ruijieSubslotUserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSubslotUserStatus.setStatus("current")
_RuijieSubslotSoftwareStatus_Type = Integer32
_RuijieSubslotSoftwareStatus_Object = MibTableColumn
ruijieSubslotSoftwareStatus = _RuijieSubslotSoftwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 8, 1, 10),
    _RuijieSubslotSoftwareStatus_Type()
)
ruijieSubslotSoftwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSubslotSoftwareStatus.setStatus("current")


class _RuijieSubslotSerialNumber_Type(DisplayString):
    """Custom type ruijieSubslotSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieSubslotSerialNumber_Type.__name__ = "DisplayString"
_RuijieSubslotSerialNumber_Object = MibTableColumn
ruijieSubslotSerialNumber = _RuijieSubslotSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 8, 1, 11),
    _RuijieSubslotSerialNumber_Type()
)
ruijieSubslotSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSubslotSerialNumber.setStatus("current")


class _RuijieSubslotHWVersion_Type(DisplayString):
    """Custom type ruijieSubslotHWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieSubslotHWVersion_Type.__name__ = "DisplayString"
_RuijieSubslotHWVersion_Object = MibTableColumn
ruijieSubslotHWVersion = _RuijieSubslotHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 8, 1, 12),
    _RuijieSubslotHWVersion_Type()
)
ruijieSubslotHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSubslotHWVersion.setStatus("current")


class _RuijieSubslotSoftwareVersion_Type(DisplayString):
    """Custom type ruijieSubslotSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieSubslotSoftwareVersion_Type.__name__ = "DisplayString"
_RuijieSubslotSoftwareVersion_Object = MibTableColumn
ruijieSubslotSoftwareVersion = _RuijieSubslotSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 8, 1, 13),
    _RuijieSubslotSoftwareVersion_Type()
)
ruijieSubslotSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSubslotSoftwareVersion.setStatus("current")


class _RuijieSubslotServiceState_Type(Integer32):
    """Custom type ruijieSubslotServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2),
          ("servNA", 3))
    )


_RuijieSubslotServiceState_Type.__name__ = "Integer32"
_RuijieSubslotServiceState_Object = MibTableColumn
ruijieSubslotServiceState = _RuijieSubslotServiceState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 8, 1, 14),
    _RuijieSubslotServiceState_Type()
)
ruijieSubslotServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSubslotServiceState.setStatus("current")
_RuijieSystemTotalOutPower_Type = Integer32
_RuijieSystemTotalOutPower_Object = MibScalar
ruijieSystemTotalOutPower = _RuijieSystemTotalOutPower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 9),
    _RuijieSystemTotalOutPower_Type()
)
ruijieSystemTotalOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemTotalOutPower.setStatus("current")
_RuijieComponentMIBObjects_ObjectIdentity = ObjectIdentity
ruijieComponentMIBObjects = _RuijieComponentMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10)
)
_RuijieComponentLicense_Type = OctetString
_RuijieComponentLicense_Object = MibScalar
ruijieComponentLicense = _RuijieComponentLicense_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 1),
    _RuijieComponentLicense_Type()
)
ruijieComponentLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieComponentLicense.setStatus("current")
_RuijieComponentInfo_ObjectIdentity = ObjectIdentity
ruijieComponentInfo = _RuijieComponentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 2)
)
_RuijieComponentKeyPos_Type = Unsigned32
_RuijieComponentKeyPos_Object = MibScalar
ruijieComponentKeyPos = _RuijieComponentKeyPos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 2, 1),
    _RuijieComponentKeyPos_Type()
)
ruijieComponentKeyPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieComponentKeyPos.setStatus("current")
_RuijieComponentBoardTable_Object = MibTable
ruijieComponentBoardTable = _RuijieComponentBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 2, 2)
)
if mibBuilder.loadTexts:
    ruijieComponentBoardTable.setStatus("current")
_RuijieComponentBoardEntry_Object = MibTableRow
ruijieComponentBoardEntry = _RuijieComponentBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 2, 2, 1)
)
ruijieComponentBoardEntry.setIndexNames(
    (0, "RUIJIE-ENTITY-MIB", "ruijieComponentBoardDeviceIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijieComponentBoardSlotIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijieComponentBoardSubslotIndex"),
)
if mibBuilder.loadTexts:
    ruijieComponentBoardEntry.setStatus("current")


class _RuijieComponentBoardDeviceIndex_Type(Unsigned32):
    """Custom type ruijieComponentBoardDeviceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieComponentBoardDeviceIndex_Type.__name__ = "Unsigned32"
_RuijieComponentBoardDeviceIndex_Object = MibTableColumn
ruijieComponentBoardDeviceIndex = _RuijieComponentBoardDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 2, 2, 1, 1),
    _RuijieComponentBoardDeviceIndex_Type()
)
ruijieComponentBoardDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieComponentBoardDeviceIndex.setStatus("current")


class _RuijieComponentBoardSlotIndex_Type(Unsigned32):
    """Custom type ruijieComponentBoardSlotIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieComponentBoardSlotIndex_Type.__name__ = "Unsigned32"
_RuijieComponentBoardSlotIndex_Object = MibTableColumn
ruijieComponentBoardSlotIndex = _RuijieComponentBoardSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 2, 2, 1, 2),
    _RuijieComponentBoardSlotIndex_Type()
)
ruijieComponentBoardSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieComponentBoardSlotIndex.setStatus("current")


class _RuijieComponentBoardSubslotIndex_Type(Unsigned32):
    """Custom type ruijieComponentBoardSubslotIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieComponentBoardSubslotIndex_Type.__name__ = "Unsigned32"
_RuijieComponentBoardSubslotIndex_Object = MibTableColumn
ruijieComponentBoardSubslotIndex = _RuijieComponentBoardSubslotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 2, 2, 1, 3),
    _RuijieComponentBoardSubslotIndex_Type()
)
ruijieComponentBoardSubslotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieComponentBoardSubslotIndex.setStatus("current")
_RuijieComponentSlotName_Type = DisplayString
_RuijieComponentSlotName_Object = MibTableColumn
ruijieComponentSlotName = _RuijieComponentSlotName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 2, 2, 1, 4),
    _RuijieComponentSlotName_Type()
)
ruijieComponentSlotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieComponentSlotName.setStatus("current")
_RuijieComponentBoardName_Type = DisplayString
_RuijieComponentBoardName_Object = MibTableColumn
ruijieComponentBoardName = _RuijieComponentBoardName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 2, 2, 1, 5),
    _RuijieComponentBoardName_Type()
)
ruijieComponentBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieComponentBoardName.setStatus("current")
_RuijieComponentTable_Object = MibTable
ruijieComponentTable = _RuijieComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 2, 3)
)
if mibBuilder.loadTexts:
    ruijieComponentTable.setStatus("current")
_RuijieComponentEntry_Object = MibTableRow
ruijieComponentEntry = _RuijieComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 2, 3, 1)
)
ruijieComponentEntry.setIndexNames(
    (0, "RUIJIE-ENTITY-MIB", "ruijieComponentDeviceIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijieComponentSlotIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijieComponentSubslotIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijieComponentType"),
    (0, "RUIJIE-ENTITY-MIB", "ruijieComponentTypeIndex"),
)
if mibBuilder.loadTexts:
    ruijieComponentEntry.setStatus("current")


class _RuijieComponentDeviceIndex_Type(Unsigned32):
    """Custom type ruijieComponentDeviceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieComponentDeviceIndex_Type.__name__ = "Unsigned32"
_RuijieComponentDeviceIndex_Object = MibTableColumn
ruijieComponentDeviceIndex = _RuijieComponentDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 2, 3, 1, 1),
    _RuijieComponentDeviceIndex_Type()
)
ruijieComponentDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieComponentDeviceIndex.setStatus("current")


class _RuijieComponentSlotIndex_Type(Unsigned32):
    """Custom type ruijieComponentSlotIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieComponentSlotIndex_Type.__name__ = "Unsigned32"
_RuijieComponentSlotIndex_Object = MibTableColumn
ruijieComponentSlotIndex = _RuijieComponentSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 2, 3, 1, 2),
    _RuijieComponentSlotIndex_Type()
)
ruijieComponentSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieComponentSlotIndex.setStatus("current")


class _RuijieComponentSubslotIndex_Type(Unsigned32):
    """Custom type ruijieComponentSubslotIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieComponentSubslotIndex_Type.__name__ = "Unsigned32"
_RuijieComponentSubslotIndex_Object = MibTableColumn
ruijieComponentSubslotIndex = _RuijieComponentSubslotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 2, 3, 1, 3),
    _RuijieComponentSubslotIndex_Type()
)
ruijieComponentSubslotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieComponentSubslotIndex.setStatus("current")


class _RuijieComponentType_Type(Unsigned32):
    """Custom type ruijieComponentType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieComponentType_Type.__name__ = "Unsigned32"
_RuijieComponentType_Object = MibTableColumn
ruijieComponentType = _RuijieComponentType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 2, 3, 1, 4),
    _RuijieComponentType_Type()
)
ruijieComponentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieComponentType.setStatus("current")


class _RuijieComponentTypeIndex_Type(Unsigned32):
    """Custom type ruijieComponentTypeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieComponentTypeIndex_Type.__name__ = "Unsigned32"
_RuijieComponentTypeIndex_Object = MibTableColumn
ruijieComponentTypeIndex = _RuijieComponentTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 2, 3, 1, 5),
    _RuijieComponentTypeIndex_Type()
)
ruijieComponentTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieComponentTypeIndex.setStatus("current")
_RuijieComponentTypeName_Type = DisplayString
_RuijieComponentTypeName_Object = MibTableColumn
ruijieComponentTypeName = _RuijieComponentTypeName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 2, 3, 1, 6),
    _RuijieComponentTypeName_Type()
)
ruijieComponentTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieComponentTypeName.setStatus("current")
_RuijieComponentTypeCount_Type = DisplayString
_RuijieComponentTypeCount_Object = MibTableColumn
ruijieComponentTypeCount = _RuijieComponentTypeCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 10, 2, 3, 1, 7),
    _RuijieComponentTypeCount_Type()
)
ruijieComponentTypeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieComponentTypeCount.setStatus("current")
_RuijieEntityMIBTraps_ObjectIdentity = ObjectIdentity
ruijieEntityMIBTraps = _RuijieEntityMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2)
)
_RuijieEntityStateChgDesc_Type = DisplayString
_RuijieEntityStateChgDesc_Object = MibScalar
ruijieEntityStateChgDesc = _RuijieEntityStateChgDesc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 1),
    _RuijieEntityStateChgDesc_Type()
)
ruijieEntityStateChgDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieEntityStateChgDesc.setStatus("current")


class _RuijieTemperatureWarningDesc_Type(DisplayString):
    """Custom type ruijieTemperatureWarningDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieTemperatureWarningDesc_Type.__name__ = "DisplayString"
_RuijieTemperatureWarningDesc_Object = MibScalar
ruijieTemperatureWarningDesc = _RuijieTemperatureWarningDesc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 3),
    _RuijieTemperatureWarningDesc_Type()
)
ruijieTemperatureWarningDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieTemperatureWarningDesc.setStatus("current")
_RuijieEntityStateWarningDesc_Type = DisplayString
_RuijieEntityStateWarningDesc_Object = MibScalar
ruijieEntityStateWarningDesc = _RuijieEntityStateWarningDesc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 10),
    _RuijieEntityStateWarningDesc_Type()
)
ruijieEntityStateWarningDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieEntityStateWarningDesc.setStatus("current")
_RuijieEntityDeviceIndex_Type = Integer32
_RuijieEntityDeviceIndex_Object = MibScalar
ruijieEntityDeviceIndex = _RuijieEntityDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 13),
    _RuijieEntityDeviceIndex_Type()
)
ruijieEntityDeviceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieEntityDeviceIndex.setStatus("current")
_RuijieEntityPhysicalDescr_Type = DisplayString
_RuijieEntityPhysicalDescr_Object = MibScalar
ruijieEntityPhysicalDescr = _RuijieEntityPhysicalDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 14),
    _RuijieEntityPhysicalDescr_Type()
)
ruijieEntityPhysicalDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieEntityPhysicalDescr.setStatus("current")
_RuijieEntityCheckType_Type = Integer32
_RuijieEntityCheckType_Object = MibScalar
ruijieEntityCheckType = _RuijieEntityCheckType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 15),
    _RuijieEntityCheckType_Type()
)
ruijieEntityCheckType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieEntityCheckType.setStatus("current")
_RuijieRelatedEntityPhysicalDescr_Type = DisplayString
_RuijieRelatedEntityPhysicalDescr_Object = MibScalar
ruijieRelatedEntityPhysicalDescr = _RuijieRelatedEntityPhysicalDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 16),
    _RuijieRelatedEntityPhysicalDescr_Type()
)
ruijieRelatedEntityPhysicalDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRelatedEntityPhysicalDescr.setStatus("current")
_RuijieEntityCheckDescription_Type = DisplayString
_RuijieEntityCheckDescription_Object = MibScalar
ruijieEntityCheckDescription = _RuijieEntityCheckDescription_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 17),
    _RuijieEntityCheckDescription_Type()
)
ruijieEntityCheckDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieEntityCheckDescription.setStatus("current")
_RuijieDeviceMIBConformance_ObjectIdentity = ObjectIdentity
ruijieDeviceMIBConformance = _RuijieDeviceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3)
)
_RuijieDeviceMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieDeviceMIBCompliances = _RuijieDeviceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 1)
)
_RuijieDeviceMIBGroups_ObjectIdentity = ObjectIdentity
ruijieDeviceMIBGroups = _RuijieDeviceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2)
)

# Managed Objects groups

ruijieDeviceInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 1)
)
ruijieDeviceInfoMIBGroup.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieDeviceMaxNumber"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceInfoIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceInfoDescr"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceInfoSlotNumber"),
        ("RUIJIE-ENTITY-MIB", "ruijieDevicePowerStatus"))
)
if mibBuilder.loadTexts:
    ruijieDeviceInfoMIBGroup.setStatus("current")

ruijieOptionalDevInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 2)
)
ruijieOptionalDevInfoMIBGroup.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieDeviceMacAddress"),
        ("RUIJIE-ENTITY-MIB", "ruijieDevicePriority"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceAlias"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceSWVersion"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceHWVersion"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceSerialNumber"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceOid"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceProductionDate"))
)
if mibBuilder.loadTexts:
    ruijieOptionalDevInfoMIBGroup.setStatus("current")

ruijieModuleInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 3)
)
ruijieModuleInfoMIBGroup.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieSlotInfoDeviceIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotInfoIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotModuleInfoDescr"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotInfoPortNumber"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotInfoPortMaxNumber"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotInfoDesc"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotConfigModuleInfoDescr"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotUserStatus"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotSoftwareStatus"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotSerialNumber"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotHWVersion"),
        ("RUIJIE-ENTITY-MIB", "slotSocID"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotServiceState"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotModuleProductionDate"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotSoftwareVersion"))
)
if mibBuilder.loadTexts:
    ruijieModuleInfoMIBGroup.setStatus("current")

ruijieEntityChgDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 4)
)
ruijieEntityChgDescGroup.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieEntityStateChgDesc")
)
if mibBuilder.loadTexts:
    ruijieEntityChgDescGroup.setStatus("current")

ruijieModuleTempStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 6)
)
ruijieModuleTempStateGroup.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieModuleTempStateDeviceIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijieModuleTempStateIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijieModuleTempState"))
)
if mibBuilder.loadTexts:
    ruijieModuleTempStateGroup.setStatus("current")

ruijiePowerStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 7)
)
ruijiePowerStateGroup.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijiePowerStateDeviceIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijiePowerStateIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijiePowerState"),
        ("RUIJIE-ENTITY-MIB", "ruijiePowerStatePowerDescr"))
)
if mibBuilder.loadTexts:
    ruijiePowerStateGroup.setStatus("current")

ruijieFanStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 8)
)
ruijieFanStateGroup.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieFanStateDeviceIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijieFanStateIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijieFanState"),
        ("RUIJIE-ENTITY-MIB", "ruijieFanStateFanDescr"))
)
if mibBuilder.loadTexts:
    ruijieFanStateGroup.setStatus("current")

ruijieTemperatureWarningDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 9)
)
ruijieTemperatureWarningDescGroup.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieTemperatureWarningDesc")
)
if mibBuilder.loadTexts:
    ruijieTemperatureWarningDescGroup.setStatus("current")

ruijieHolderInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 11)
)
ruijieHolderInfoGroup.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieHolderNumber"),
        ("RUIJIE-ENTITY-MIB", "ruijieHolderState"),
        ("RUIJIE-ENTITY-MIB", "ruijieHolderType"),
        ("RUIJIE-ENTITY-MIB", "ruijieHolderName"))
)
if mibBuilder.loadTexts:
    ruijieHolderInfoGroup.setStatus("current")

ruijieComponentBoardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 12)
)
ruijieComponentBoardGroup.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieComponentSlotName"),
        ("RUIJIE-ENTITY-MIB", "ruijieComponentBoardName"))
)
if mibBuilder.loadTexts:
    ruijieComponentBoardGroup.setStatus("current")

ruijieComponentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 13)
)
ruijieComponentGroup.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieComponentTypeName"),
        ("RUIJIE-ENTITY-MIB", "ruijieComponentTypeCount"))
)
if mibBuilder.loadTexts:
    ruijieComponentGroup.setStatus("current")


# Notification objects

ruijieEntityStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 2)
)
ruijieEntityStatusChange.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieEntityStateChgDesc")
)
if mibBuilder.loadTexts:
    ruijieEntityStatusChange.setStatus(
        "current"
    )

ruijieTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 4)
)
ruijieTemperatureWarning.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieTemperatureWarningDesc")
)
if mibBuilder.loadTexts:
    ruijieTemperatureWarning.setStatus(
        "current"
    )

ruijieEntityPhyInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 5)
)
ruijieEntityPhyInsert.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    ruijieEntityPhyInsert.setStatus(
        "current"
    )

ruijieEntityPhyRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 6)
)
ruijieEntityPhyRemove.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    ruijieEntityPhyRemove.setStatus(
        "current"
    )

ruijieTemperatureWarningRecov = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 7)
)
ruijieTemperatureWarningRecov.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieTemperatureWarningDesc")
)
if mibBuilder.loadTexts:
    ruijieTemperatureWarningRecov.setStatus(
        "current"
    )

ruijieTemperaturePoeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 8)
)
ruijieTemperaturePoeWarning.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieTemperatureWarningDesc")
)
if mibBuilder.loadTexts:
    ruijieTemperaturePoeWarning.setStatus(
        "current"
    )

ruijieTemperaturePoeWarningRecov = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 9)
)
ruijieTemperaturePoeWarningRecov.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieTemperatureWarningDesc")
)
if mibBuilder.loadTexts:
    ruijieTemperaturePoeWarningRecov.setStatus(
        "current"
    )

ruijieEntityStateWarningActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 11)
)
ruijieEntityStateWarningActive.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieEntityStateWarningDesc")
)
if mibBuilder.loadTexts:
    ruijieEntityStateWarningActive.setStatus(
        "current"
    )

ruijieEntityStateWarningClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 12)
)
ruijieEntityStateWarningClear.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieEntityStateWarningDesc")
)
if mibBuilder.loadTexts:
    ruijieEntityStateWarningClear.setStatus(
        "current"
    )

ruijieEntityCheckFailActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 18)
)
ruijieEntityCheckFailActive.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieEntityDeviceIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijieEntityPhysicalDescr"),
        ("RUIJIE-ENTITY-MIB", "ruijieEntityCheckType"),
        ("RUIJIE-ENTITY-MIB", "ruijieEntityCheckDescription"))
)
if mibBuilder.loadTexts:
    ruijieEntityCheckFailActive.setStatus(
        "current"
    )

ruijieEntityCheckFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 19)
)
ruijieEntityCheckFailClear.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieEntityDeviceIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijieEntityPhysicalDescr"),
        ("RUIJIE-ENTITY-MIB", "ruijieEntityCheckType"),
        ("RUIJIE-ENTITY-MIB", "ruijieEntityCheckDescription"))
)
if mibBuilder.loadTexts:
    ruijieEntityCheckFailClear.setStatus(
        "current"
    )

ruijieBoardCheckFailActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 20)
)
ruijieBoardCheckFailActive.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieEntityDeviceIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijieEntityPhysicalDescr"),
        ("RUIJIE-ENTITY-MIB", "ruijieEntityCheckType"),
        ("RUIJIE-ENTITY-MIB", "ruijieRelatedEntityPhysicalDescr"),
        ("RUIJIE-ENTITY-MIB", "ruijieEntityCheckDescription"))
)
if mibBuilder.loadTexts:
    ruijieBoardCheckFailActive.setStatus(
        "current"
    )

ruijieBoardCheckFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 21)
)
ruijieBoardCheckFailClear.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieEntityDeviceIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijieEntityPhysicalDescr"),
        ("RUIJIE-ENTITY-MIB", "ruijieEntityCheckType"),
        ("RUIJIE-ENTITY-MIB", "ruijieRelatedEntityPhysicalDescr"),
        ("RUIJIE-ENTITY-MIB", "ruijieEntityCheckDescription"))
)
if mibBuilder.loadTexts:
    ruijieBoardCheckFailClear.setStatus(
        "current"
    )


# Notifications groups

ruijieDeviceMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 5)
)
ruijieDeviceMIBNotificationGroup.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieEntityStatusChange")
)
if mibBuilder.loadTexts:
    ruijieDeviceMIBNotificationGroup.setStatus(
        "current"
    )

ruijieTemperatureWarningGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 10)
)
ruijieTemperatureWarningGroup.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieTemperatureWarning")
)
if mibBuilder.loadTexts:
    ruijieTemperatureWarningGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieDeviceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 1, 1)
)
ruijieDeviceMIBCompliance.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieDeviceInfoMIBGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieModuleInfoMIBGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieOptionalDevInfoMIBGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieEntityChgDescGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceMIBNotificationGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieModuleTempStateGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijiePowerStateGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieFanStateGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieTemperatureWarningDescGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieTemperatureWarningGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieHolderInfoGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieComponentBoardGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieComponentGroup"))
)
if mibBuilder.loadTexts:
    ruijieDeviceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-ENTITY-MIB",
    **{"ruijieEntityMIB": ruijieEntityMIB,
       "ruijieDeviceMIBObjects": ruijieDeviceMIBObjects,
       "ruijieDeviceMaxNumber": ruijieDeviceMaxNumber,
       "ruijieDeviceInfoTable": ruijieDeviceInfoTable,
       "ruijieDeviceInfoEntry": ruijieDeviceInfoEntry,
       "ruijieDeviceInfoIndex": ruijieDeviceInfoIndex,
       "ruijieDeviceInfoDescr": ruijieDeviceInfoDescr,
       "ruijieDeviceInfoSlotNumber": ruijieDeviceInfoSlotNumber,
       "ruijieDevicePowerStatus": ruijieDevicePowerStatus,
       "ruijieDeviceMacAddress": ruijieDeviceMacAddress,
       "ruijieDevicePriority": ruijieDevicePriority,
       "ruijieDeviceAlias": ruijieDeviceAlias,
       "ruijieDeviceSWVersion": ruijieDeviceSWVersion,
       "ruijieDeviceHWVersion": ruijieDeviceHWVersion,
       "ruijieDeviceSerialNumber": ruijieDeviceSerialNumber,
       "ruijieDeviceOid": ruijieDeviceOid,
       "ruijieDeviceProductionDate": ruijieDeviceProductionDate,
       "ruijieDeviceOutPower": ruijieDeviceOutPower,
       "ruijieSlotInfoTable": ruijieSlotInfoTable,
       "ruijieSlotInfoEntry": ruijieSlotInfoEntry,
       "ruijieSlotInfoDeviceIndex": ruijieSlotInfoDeviceIndex,
       "ruijieSlotInfoIndex": ruijieSlotInfoIndex,
       "ruijieSlotModuleInfoDescr": ruijieSlotModuleInfoDescr,
       "ruijieSlotInfoPortNumber": ruijieSlotInfoPortNumber,
       "ruijieSlotInfoPortMaxNumber": ruijieSlotInfoPortMaxNumber,
       "ruijieSlotInfoDesc": ruijieSlotInfoDesc,
       "ruijieSlotConfigModuleInfoDescr": ruijieSlotConfigModuleInfoDescr,
       "ruijieSlotUserStatus": ruijieSlotUserStatus,
       "ruijieSlotSoftwareStatus": ruijieSlotSoftwareStatus,
       "ruijieSlotSerialNumber": ruijieSlotSerialNumber,
       "ruijieSlotHWVersion": ruijieSlotHWVersion,
       "slotSocID": slotSocID,
       "ruijieSlotServiceState": ruijieSlotServiceState,
       "ruijieSlotModuleProductionDate": ruijieSlotModuleProductionDate,
       "ruijieSlotSoftwareVersion": ruijieSlotSoftwareVersion,
       "ruijieModuleTempStateTable": ruijieModuleTempStateTable,
       "ruijieModuleTempStateEntry": ruijieModuleTempStateEntry,
       "ruijieModuleTempStateDeviceIndex": ruijieModuleTempStateDeviceIndex,
       "ruijieModuleTempStateIndex": ruijieModuleTempStateIndex,
       "ruijieModuleTempState": ruijieModuleTempState,
       "ruijiePowerStateTable": ruijiePowerStateTable,
       "ruijiePowerStateEntry": ruijiePowerStateEntry,
       "ruijiePowerStateDeviceIndex": ruijiePowerStateDeviceIndex,
       "ruijiePowerStateIndex": ruijiePowerStateIndex,
       "ruijiePowerState": ruijiePowerState,
       "ruijiePowerStatePowerDescr": ruijiePowerStatePowerDescr,
       "ruijiePowerStateSerialNumber": ruijiePowerStateSerialNumber,
       "ruijieFanStateTable": ruijieFanStateTable,
       "ruijieFanStateEntry": ruijieFanStateEntry,
       "ruijieFanStateDeviceIndex": ruijieFanStateDeviceIndex,
       "ruijieFanStateIndex": ruijieFanStateIndex,
       "ruijieFanState": ruijieFanState,
       "ruijieFanStateFanDescr": ruijieFanStateFanDescr,
       "ruijieFanStateSerialNumber": ruijieFanStateSerialNumber,
       "ruijieHolderInfoTable": ruijieHolderInfoTable,
       "ruijieHolderInfoEntry": ruijieHolderInfoEntry,
       "ruijieHolderInfoDeviceIndex": ruijieHolderInfoDeviceIndex,
       "ruijieHolderInfoSlotIndex": ruijieHolderInfoSlotIndex,
       "ruijieHolderInfoSubSlotIndex": ruijieHolderInfoSubSlotIndex,
       "ruijieHolderNumber": ruijieHolderNumber,
       "ruijieHolderState": ruijieHolderState,
       "ruijieHolderType": ruijieHolderType,
       "ruijieHolderName": ruijieHolderName,
       "ruijieSubslotInfoTable": ruijieSubslotInfoTable,
       "ruijieSubslotInfoEntry": ruijieSubslotInfoEntry,
       "ruijieSubslotInfoDeviceIndex": ruijieSubslotInfoDeviceIndex,
       "ruijieSubslotInfoSlotIndex": ruijieSubslotInfoSlotIndex,
       "ruijieSubslotInfoIndex": ruijieSubslotInfoIndex,
       "ruijieSubslotModuleInfoDescr": ruijieSubslotModuleInfoDescr,
       "ruijieSubslotInfoPortNumber": ruijieSubslotInfoPortNumber,
       "ruijieSubslotInfoPortMaxNumber": ruijieSubslotInfoPortMaxNumber,
       "ruijieSubslotInfoDesc": ruijieSubslotInfoDesc,
       "ruijieSubslotConfigModuleInfoDescr": ruijieSubslotConfigModuleInfoDescr,
       "ruijieSubslotUserStatus": ruijieSubslotUserStatus,
       "ruijieSubslotSoftwareStatus": ruijieSubslotSoftwareStatus,
       "ruijieSubslotSerialNumber": ruijieSubslotSerialNumber,
       "ruijieSubslotHWVersion": ruijieSubslotHWVersion,
       "ruijieSubslotSoftwareVersion": ruijieSubslotSoftwareVersion,
       "ruijieSubslotServiceState": ruijieSubslotServiceState,
       "ruijieSystemTotalOutPower": ruijieSystemTotalOutPower,
       "ruijieComponentMIBObjects": ruijieComponentMIBObjects,
       "ruijieComponentLicense": ruijieComponentLicense,
       "ruijieComponentInfo": ruijieComponentInfo,
       "ruijieComponentKeyPos": ruijieComponentKeyPos,
       "ruijieComponentBoardTable": ruijieComponentBoardTable,
       "ruijieComponentBoardEntry": ruijieComponentBoardEntry,
       "ruijieComponentBoardDeviceIndex": ruijieComponentBoardDeviceIndex,
       "ruijieComponentBoardSlotIndex": ruijieComponentBoardSlotIndex,
       "ruijieComponentBoardSubslotIndex": ruijieComponentBoardSubslotIndex,
       "ruijieComponentSlotName": ruijieComponentSlotName,
       "ruijieComponentBoardName": ruijieComponentBoardName,
       "ruijieComponentTable": ruijieComponentTable,
       "ruijieComponentEntry": ruijieComponentEntry,
       "ruijieComponentDeviceIndex": ruijieComponentDeviceIndex,
       "ruijieComponentSlotIndex": ruijieComponentSlotIndex,
       "ruijieComponentSubslotIndex": ruijieComponentSubslotIndex,
       "ruijieComponentType": ruijieComponentType,
       "ruijieComponentTypeIndex": ruijieComponentTypeIndex,
       "ruijieComponentTypeName": ruijieComponentTypeName,
       "ruijieComponentTypeCount": ruijieComponentTypeCount,
       "ruijieEntityMIBTraps": ruijieEntityMIBTraps,
       "ruijieEntityStateChgDesc": ruijieEntityStateChgDesc,
       "ruijieEntityStatusChange": ruijieEntityStatusChange,
       "ruijieTemperatureWarningDesc": ruijieTemperatureWarningDesc,
       "ruijieTemperatureWarning": ruijieTemperatureWarning,
       "ruijieEntityPhyInsert": ruijieEntityPhyInsert,
       "ruijieEntityPhyRemove": ruijieEntityPhyRemove,
       "ruijieTemperatureWarningRecov": ruijieTemperatureWarningRecov,
       "ruijieTemperaturePoeWarning": ruijieTemperaturePoeWarning,
       "ruijieTemperaturePoeWarningRecov": ruijieTemperaturePoeWarningRecov,
       "ruijieEntityStateWarningDesc": ruijieEntityStateWarningDesc,
       "ruijieEntityStateWarningActive": ruijieEntityStateWarningActive,
       "ruijieEntityStateWarningClear": ruijieEntityStateWarningClear,
       "ruijieEntityDeviceIndex": ruijieEntityDeviceIndex,
       "ruijieEntityPhysicalDescr": ruijieEntityPhysicalDescr,
       "ruijieEntityCheckType": ruijieEntityCheckType,
       "ruijieRelatedEntityPhysicalDescr": ruijieRelatedEntityPhysicalDescr,
       "ruijieEntityCheckDescription": ruijieEntityCheckDescription,
       "ruijieEntityCheckFailActive": ruijieEntityCheckFailActive,
       "ruijieEntityCheckFailClear": ruijieEntityCheckFailClear,
       "ruijieBoardCheckFailActive": ruijieBoardCheckFailActive,
       "ruijieBoardCheckFailClear": ruijieBoardCheckFailClear,
       "ruijieDeviceMIBConformance": ruijieDeviceMIBConformance,
       "ruijieDeviceMIBCompliances": ruijieDeviceMIBCompliances,
       "ruijieDeviceMIBCompliance": ruijieDeviceMIBCompliance,
       "ruijieDeviceMIBGroups": ruijieDeviceMIBGroups,
       "ruijieDeviceInfoMIBGroup": ruijieDeviceInfoMIBGroup,
       "ruijieOptionalDevInfoMIBGroup": ruijieOptionalDevInfoMIBGroup,
       "ruijieModuleInfoMIBGroup": ruijieModuleInfoMIBGroup,
       "ruijieEntityChgDescGroup": ruijieEntityChgDescGroup,
       "ruijieDeviceMIBNotificationGroup": ruijieDeviceMIBNotificationGroup,
       "ruijieModuleTempStateGroup": ruijieModuleTempStateGroup,
       "ruijiePowerStateGroup": ruijiePowerStateGroup,
       "ruijieFanStateGroup": ruijieFanStateGroup,
       "ruijieTemperatureWarningDescGroup": ruijieTemperatureWarningDescGroup,
       "ruijieTemperatureWarningGroup": ruijieTemperatureWarningGroup,
       "ruijieHolderInfoGroup": ruijieHolderInfoGroup,
       "ruijieComponentBoardGroup": ruijieComponentBoardGroup,
       "ruijieComponentGroup": ruijieComponentGroup}
)
