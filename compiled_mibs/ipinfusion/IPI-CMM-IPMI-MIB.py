# SNMP MIB module (IPI-CMM-IPMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ipinfusion\IPI-CMM-IPMI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:56 2025
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

(cmmChassisObject,
 cmmStackUnitIndex) = mibBuilder.importSymbols(
    "IPI-CMM-CHASSIS-MIB",
    "cmmChassisObject",
    "cmmStackUnitIndex")

(ipi,) = mibBuilder.importSymbols(
    "IPI-MODULE-MIB",
    "ipi")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cmm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100)
)
if mibBuilder.loadTexts:
    cmm.setRevisions(
        ("2020-08-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmmIpmiDeviceObjects_ObjectIdentity = ObjectIdentity
cmmIpmiDeviceObjects = _CmmIpmiDeviceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5)
)
_CmmIpmiDeviceSensorTable_Object = MibTable
cmmIpmiDeviceSensorTable = _CmmIpmiDeviceSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorTable.setStatus("current")
_CmmIpmiDeviceSensorEntry_Object = MibTableRow
cmmIpmiDeviceSensorEntry = _CmmIpmiDeviceSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 1, 1)
)
cmmIpmiDeviceSensorEntry.setIndexNames(
    (0, "IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorIndex"),
)
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorEntry.setStatus("current")


class _CmmIpmiDeviceSensorIndex_Type(Integer32):
    """Custom type cmmIpmiDeviceSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmmIpmiDeviceSensorIndex_Type.__name__ = "Integer32"
_CmmIpmiDeviceSensorIndex_Object = MibTableColumn
cmmIpmiDeviceSensorIndex = _CmmIpmiDeviceSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 1, 1, 1),
    _CmmIpmiDeviceSensorIndex_Type()
)
cmmIpmiDeviceSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorIndex.setStatus("current")
_CmmIpmiDeviceSensorName_Type = DisplayString
_CmmIpmiDeviceSensorName_Object = MibTableColumn
cmmIpmiDeviceSensorName = _CmmIpmiDeviceSensorName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 1, 1, 2),
    _CmmIpmiDeviceSensorName_Type()
)
cmmIpmiDeviceSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorName.setStatus("current")
_CmmIpmiDeviceSensorValue_Type = Integer32
_CmmIpmiDeviceSensorValue_Object = MibTableColumn
cmmIpmiDeviceSensorValue = _CmmIpmiDeviceSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 1, 1, 3),
    _CmmIpmiDeviceSensorValue_Type()
)
cmmIpmiDeviceSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorValue.setStatus("current")
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorValue.setUnits("0.001 unit")
_CmmIpmiDeviceSensorUnits_Type = DisplayString
_CmmIpmiDeviceSensorUnits_Object = MibTableColumn
cmmIpmiDeviceSensorUnits = _CmmIpmiDeviceSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 1, 1, 4),
    _CmmIpmiDeviceSensorUnits_Type()
)
cmmIpmiDeviceSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorUnits.setStatus("current")
_CmmIpmiDeviceSensorState_Type = DisplayString
_CmmIpmiDeviceSensorState_Object = MibTableColumn
cmmIpmiDeviceSensorState = _CmmIpmiDeviceSensorState_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 1, 1, 5),
    _CmmIpmiDeviceSensorState_Type()
)
cmmIpmiDeviceSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorState.setStatus("current")
_CmmIpmiDeviceSensorLowerNonRecover_Type = Integer32
_CmmIpmiDeviceSensorLowerNonRecover_Object = MibTableColumn
cmmIpmiDeviceSensorLowerNonRecover = _CmmIpmiDeviceSensorLowerNonRecover_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 1, 1, 6),
    _CmmIpmiDeviceSensorLowerNonRecover_Type()
)
cmmIpmiDeviceSensorLowerNonRecover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorLowerNonRecover.setStatus("current")
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorLowerNonRecover.setUnits("0.001 unit")
_CmmIpmiDeviceSensorLowerCritical_Type = Integer32
_CmmIpmiDeviceSensorLowerCritical_Object = MibTableColumn
cmmIpmiDeviceSensorLowerCritical = _CmmIpmiDeviceSensorLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 1, 1, 7),
    _CmmIpmiDeviceSensorLowerCritical_Type()
)
cmmIpmiDeviceSensorLowerCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorLowerCritical.setStatus("current")
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorLowerCritical.setUnits("0.001 unit")
_CmmIpmiDeviceSensorLowerNonCritical_Type = Integer32
_CmmIpmiDeviceSensorLowerNonCritical_Object = MibTableColumn
cmmIpmiDeviceSensorLowerNonCritical = _CmmIpmiDeviceSensorLowerNonCritical_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 1, 1, 8),
    _CmmIpmiDeviceSensorLowerNonCritical_Type()
)
cmmIpmiDeviceSensorLowerNonCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorLowerNonCritical.setStatus("current")
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorLowerNonCritical.setUnits("0.001 unit")
_CmmIpmiDeviceSensorUpperNonCritical_Type = Integer32
_CmmIpmiDeviceSensorUpperNonCritical_Object = MibTableColumn
cmmIpmiDeviceSensorUpperNonCritical = _CmmIpmiDeviceSensorUpperNonCritical_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 1, 1, 9),
    _CmmIpmiDeviceSensorUpperNonCritical_Type()
)
cmmIpmiDeviceSensorUpperNonCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorUpperNonCritical.setStatus("current")
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorUpperNonCritical.setUnits("0.001 unit")
_CmmIpmiDeviceSensorUpperCritical_Type = Integer32
_CmmIpmiDeviceSensorUpperCritical_Object = MibTableColumn
cmmIpmiDeviceSensorUpperCritical = _CmmIpmiDeviceSensorUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 1, 1, 10),
    _CmmIpmiDeviceSensorUpperCritical_Type()
)
cmmIpmiDeviceSensorUpperCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorUpperCritical.setStatus("current")
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorUpperCritical.setUnits("0.001 unit")
_CmmIpmiDeviceSensorUpperNonRecover_Type = Integer32
_CmmIpmiDeviceSensorUpperNonRecover_Object = MibTableColumn
cmmIpmiDeviceSensorUpperNonRecover = _CmmIpmiDeviceSensorUpperNonRecover_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 1, 1, 11),
    _CmmIpmiDeviceSensorUpperNonRecover_Type()
)
cmmIpmiDeviceSensorUpperNonRecover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorUpperNonRecover.setStatus("current")
if mibBuilder.loadTexts:
    cmmIpmiDeviceSensorUpperNonRecover.setUnits("0.001 unit")
_CmmIpmiDeviceFRUTable_Object = MibTable
cmmIpmiDeviceFRUTable = _CmmIpmiDeviceFRUTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cmmIpmiDeviceFRUTable.setStatus("current")
_CmmIpmiDeviceFRUEntry_Object = MibTableRow
cmmIpmiDeviceFRUEntry = _CmmIpmiDeviceFRUEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 2, 1)
)
cmmIpmiDeviceFRUEntry.setIndexNames(
    (0, "IPI-CMM-IPMI-MIB", "cmmIpmiDeviceFRUIndex"),
)
if mibBuilder.loadTexts:
    cmmIpmiDeviceFRUEntry.setStatus("current")


class _CmmIpmiDeviceFRUIndex_Type(Integer32):
    """Custom type cmmIpmiDeviceFRUIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmmIpmiDeviceFRUIndex_Type.__name__ = "Integer32"
_CmmIpmiDeviceFRUIndex_Object = MibTableColumn
cmmIpmiDeviceFRUIndex = _CmmIpmiDeviceFRUIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 2, 1, 1),
    _CmmIpmiDeviceFRUIndex_Type()
)
cmmIpmiDeviceFRUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmmIpmiDeviceFRUIndex.setStatus("current")
_CmmIpmiDeviceBoardMfgDate_Type = DateAndTime
_CmmIpmiDeviceBoardMfgDate_Object = MibTableColumn
cmmIpmiDeviceBoardMfgDate = _CmmIpmiDeviceBoardMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 2, 1, 2),
    _CmmIpmiDeviceBoardMfgDate_Type()
)
cmmIpmiDeviceBoardMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceBoardMfgDate.setStatus("current")
_CmmIpmiDeviceBoardMfg_Type = DisplayString
_CmmIpmiDeviceBoardMfg_Object = MibTableColumn
cmmIpmiDeviceBoardMfg = _CmmIpmiDeviceBoardMfg_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 2, 1, 3),
    _CmmIpmiDeviceBoardMfg_Type()
)
cmmIpmiDeviceBoardMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceBoardMfg.setStatus("current")
_CmmIpmiDeviceBoardProduct_Type = DisplayString
_CmmIpmiDeviceBoardProduct_Object = MibTableColumn
cmmIpmiDeviceBoardProduct = _CmmIpmiDeviceBoardProduct_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 2, 1, 4),
    _CmmIpmiDeviceBoardProduct_Type()
)
cmmIpmiDeviceBoardProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceBoardProduct.setStatus("current")
_CmmIpmiDeviceBoardSerial_Type = DisplayString
_CmmIpmiDeviceBoardSerial_Object = MibTableColumn
cmmIpmiDeviceBoardSerial = _CmmIpmiDeviceBoardSerial_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 2, 1, 5),
    _CmmIpmiDeviceBoardSerial_Type()
)
cmmIpmiDeviceBoardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceBoardSerial.setStatus("current")
_CmmIpmiDeviceBoardPartNum_Type = DisplayString
_CmmIpmiDeviceBoardPartNum_Object = MibTableColumn
cmmIpmiDeviceBoardPartNum = _CmmIpmiDeviceBoardPartNum_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 2, 1, 6),
    _CmmIpmiDeviceBoardPartNum_Type()
)
cmmIpmiDeviceBoardPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceBoardPartNum.setStatus("current")
_CmmIpmiDeviceProductManufacturer_Type = DisplayString
_CmmIpmiDeviceProductManufacturer_Object = MibTableColumn
cmmIpmiDeviceProductManufacturer = _CmmIpmiDeviceProductManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 2, 1, 7),
    _CmmIpmiDeviceProductManufacturer_Type()
)
cmmIpmiDeviceProductManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceProductManufacturer.setStatus("current")
_CmmIpmiDeviceProductName_Type = DisplayString
_CmmIpmiDeviceProductName_Object = MibTableColumn
cmmIpmiDeviceProductName = _CmmIpmiDeviceProductName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 2, 1, 8),
    _CmmIpmiDeviceProductName_Type()
)
cmmIpmiDeviceProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceProductName.setStatus("current")
_CmmIpmiDeviceProductPartNum_Type = DisplayString
_CmmIpmiDeviceProductPartNum_Object = MibTableColumn
cmmIpmiDeviceProductPartNum = _CmmIpmiDeviceProductPartNum_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 2, 1, 9),
    _CmmIpmiDeviceProductPartNum_Type()
)
cmmIpmiDeviceProductPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceProductPartNum.setStatus("current")
_CmmIpmiDeviceProductVersion_Type = DisplayString
_CmmIpmiDeviceProductVersion_Object = MibTableColumn
cmmIpmiDeviceProductVersion = _CmmIpmiDeviceProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 2, 1, 10),
    _CmmIpmiDeviceProductVersion_Type()
)
cmmIpmiDeviceProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceProductVersion.setStatus("current")
_CmmIpmiDeviceProductSerial_Type = DisplayString
_CmmIpmiDeviceProductSerial_Object = MibTableColumn
cmmIpmiDeviceProductSerial = _CmmIpmiDeviceProductSerial_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 2, 1, 11),
    _CmmIpmiDeviceProductSerial_Type()
)
cmmIpmiDeviceProductSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceProductSerial.setStatus("current")
_CmmIpmiDeviceProductAssetTag_Type = DisplayString
_CmmIpmiDeviceProductAssetTag_Object = MibTableColumn
cmmIpmiDeviceProductAssetTag = _CmmIpmiDeviceProductAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 2, 1, 12),
    _CmmIpmiDeviceProductAssetTag_Type()
)
cmmIpmiDeviceProductAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceProductAssetTag.setStatus("current")
_CmmIpmiDeviceProductExtraInfo_Type = DisplayString
_CmmIpmiDeviceProductExtraInfo_Object = MibTableColumn
cmmIpmiDeviceProductExtraInfo = _CmmIpmiDeviceProductExtraInfo_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 2, 1, 13),
    _CmmIpmiDeviceProductExtraInfo_Type()
)
cmmIpmiDeviceProductExtraInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceProductExtraInfo.setStatus("current")
_CmmIpmiDeviceProductExtraInfo2_Type = DisplayString
_CmmIpmiDeviceProductExtraInfo2_Object = MibTableColumn
cmmIpmiDeviceProductExtraInfo2 = _CmmIpmiDeviceProductExtraInfo2_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 2, 1, 14),
    _CmmIpmiDeviceProductExtraInfo2_Type()
)
cmmIpmiDeviceProductExtraInfo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceProductExtraInfo2.setStatus("current")
_CmmIpmiDeviceDescription_Type = DisplayString
_CmmIpmiDeviceDescription_Object = MibTableColumn
cmmIpmiDeviceDescription = _CmmIpmiDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 5, 2, 1, 15),
    _CmmIpmiDeviceDescription_Type()
)
cmmIpmiDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpmiDeviceDescription.setStatus("current")
_CmmIpmiDeviceAlarmObjects_ObjectIdentity = ObjectIdentity
cmmIpmiDeviceAlarmObjects = _CmmIpmiDeviceAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 6)
)
_CmmIpmiDeviceAlarmNotifications_ObjectIdentity = ObjectIdentity
cmmIpmiDeviceAlarmNotifications = _CmmIpmiDeviceAlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 6, 1)
)

# Managed Objects groups


# Notification objects

cmmIpmiDeviceLNC = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 6, 1, 1)
)
cmmIpmiDeviceLNC.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorName"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorValue"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorLowerNonCritical"))
)
if mibBuilder.loadTexts:
    cmmIpmiDeviceLNC.setStatus(
        "current"
    )

cmmIpmiDeviceLNCRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 6, 1, 2)
)
cmmIpmiDeviceLNCRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorName"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorValue"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorLowerNonCritical"))
)
if mibBuilder.loadTexts:
    cmmIpmiDeviceLNCRecovery.setStatus(
        "current"
    )

cmmIpmiDeviceLC = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 6, 1, 3)
)
cmmIpmiDeviceLC.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorName"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorValue"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorLowerCritical"))
)
if mibBuilder.loadTexts:
    cmmIpmiDeviceLC.setStatus(
        "current"
    )

cmmIpmiDeviceLCRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 6, 1, 4)
)
cmmIpmiDeviceLCRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorName"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorValue"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorLowerCritical"))
)
if mibBuilder.loadTexts:
    cmmIpmiDeviceLCRecovery.setStatus(
        "current"
    )

cmmIpmiDeviceLNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 6, 1, 5)
)
cmmIpmiDeviceLNR.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorName"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorValue"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorLowerNonRecover"))
)
if mibBuilder.loadTexts:
    cmmIpmiDeviceLNR.setStatus(
        "current"
    )

cmmIpmiDeviceLNRRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 6, 1, 6)
)
cmmIpmiDeviceLNRRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorName"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorValue"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorLowerNonRecover"))
)
if mibBuilder.loadTexts:
    cmmIpmiDeviceLNRRecovery.setStatus(
        "current"
    )

cmmIpmiDeviceUNC = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 6, 1, 7)
)
cmmIpmiDeviceUNC.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorName"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorValue"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorUpperNonCritical"))
)
if mibBuilder.loadTexts:
    cmmIpmiDeviceUNC.setStatus(
        "current"
    )

cmmIpmiDeviceUNCRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 6, 1, 8)
)
cmmIpmiDeviceUNCRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorName"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorValue"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorUpperNonCritical"))
)
if mibBuilder.loadTexts:
    cmmIpmiDeviceUNCRecovery.setStatus(
        "current"
    )

cmmIpmiDeviceUC = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 6, 1, 9)
)
cmmIpmiDeviceUC.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorName"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorValue"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorUpperCritical"))
)
if mibBuilder.loadTexts:
    cmmIpmiDeviceUC.setStatus(
        "current"
    )

cmmIpmiDeviceUCRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 6, 1, 10)
)
cmmIpmiDeviceUCRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorName"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorValue"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorUpperCritical"))
)
if mibBuilder.loadTexts:
    cmmIpmiDeviceUCRecovery.setStatus(
        "current"
    )

cmmIpmiDeviceUNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 6, 1, 11)
)
cmmIpmiDeviceUNR.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorName"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorValue"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorUpperNonRecover"))
)
if mibBuilder.loadTexts:
    cmmIpmiDeviceUNR.setStatus(
        "current"
    )

cmmIpmiDeviceUNRRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 6, 1, 12)
)
cmmIpmiDeviceUNRRecovery.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorName"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorValue"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorUpperNonRecover"))
)
if mibBuilder.loadTexts:
    cmmIpmiDeviceUNRRecovery.setStatus(
        "current"
    )

cmmIpmiDevicePresence = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 6, 1, 13)
)
cmmIpmiDevicePresence.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorName"))
)
if mibBuilder.loadTexts:
    cmmIpmiDevicePresence.setStatus(
        "current"
    )

cmmIpmiDeviceStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 6, 1, 14)
)
cmmIpmiDeviceStatus.setObjects(
      *(("IPI-CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("IPI-CMM-IPMI-MIB", "cmmIpmiDeviceSensorName"))
)
if mibBuilder.loadTexts:
    cmmIpmiDeviceStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPI-CMM-IPMI-MIB",
    **{"cmm": cmm,
       "cmmIpmiDeviceObjects": cmmIpmiDeviceObjects,
       "cmmIpmiDeviceSensorTable": cmmIpmiDeviceSensorTable,
       "cmmIpmiDeviceSensorEntry": cmmIpmiDeviceSensorEntry,
       "cmmIpmiDeviceSensorIndex": cmmIpmiDeviceSensorIndex,
       "cmmIpmiDeviceSensorName": cmmIpmiDeviceSensorName,
       "cmmIpmiDeviceSensorValue": cmmIpmiDeviceSensorValue,
       "cmmIpmiDeviceSensorUnits": cmmIpmiDeviceSensorUnits,
       "cmmIpmiDeviceSensorState": cmmIpmiDeviceSensorState,
       "cmmIpmiDeviceSensorLowerNonRecover": cmmIpmiDeviceSensorLowerNonRecover,
       "cmmIpmiDeviceSensorLowerCritical": cmmIpmiDeviceSensorLowerCritical,
       "cmmIpmiDeviceSensorLowerNonCritical": cmmIpmiDeviceSensorLowerNonCritical,
       "cmmIpmiDeviceSensorUpperNonCritical": cmmIpmiDeviceSensorUpperNonCritical,
       "cmmIpmiDeviceSensorUpperCritical": cmmIpmiDeviceSensorUpperCritical,
       "cmmIpmiDeviceSensorUpperNonRecover": cmmIpmiDeviceSensorUpperNonRecover,
       "cmmIpmiDeviceFRUTable": cmmIpmiDeviceFRUTable,
       "cmmIpmiDeviceFRUEntry": cmmIpmiDeviceFRUEntry,
       "cmmIpmiDeviceFRUIndex": cmmIpmiDeviceFRUIndex,
       "cmmIpmiDeviceBoardMfgDate": cmmIpmiDeviceBoardMfgDate,
       "cmmIpmiDeviceBoardMfg": cmmIpmiDeviceBoardMfg,
       "cmmIpmiDeviceBoardProduct": cmmIpmiDeviceBoardProduct,
       "cmmIpmiDeviceBoardSerial": cmmIpmiDeviceBoardSerial,
       "cmmIpmiDeviceBoardPartNum": cmmIpmiDeviceBoardPartNum,
       "cmmIpmiDeviceProductManufacturer": cmmIpmiDeviceProductManufacturer,
       "cmmIpmiDeviceProductName": cmmIpmiDeviceProductName,
       "cmmIpmiDeviceProductPartNum": cmmIpmiDeviceProductPartNum,
       "cmmIpmiDeviceProductVersion": cmmIpmiDeviceProductVersion,
       "cmmIpmiDeviceProductSerial": cmmIpmiDeviceProductSerial,
       "cmmIpmiDeviceProductAssetTag": cmmIpmiDeviceProductAssetTag,
       "cmmIpmiDeviceProductExtraInfo": cmmIpmiDeviceProductExtraInfo,
       "cmmIpmiDeviceProductExtraInfo2": cmmIpmiDeviceProductExtraInfo2,
       "cmmIpmiDeviceDescription": cmmIpmiDeviceDescription,
       "cmmIpmiDeviceAlarmObjects": cmmIpmiDeviceAlarmObjects,
       "cmmIpmiDeviceAlarmNotifications": cmmIpmiDeviceAlarmNotifications,
       "cmmIpmiDeviceLNC": cmmIpmiDeviceLNC,
       "cmmIpmiDeviceLNCRecovery": cmmIpmiDeviceLNCRecovery,
       "cmmIpmiDeviceLC": cmmIpmiDeviceLC,
       "cmmIpmiDeviceLCRecovery": cmmIpmiDeviceLCRecovery,
       "cmmIpmiDeviceLNR": cmmIpmiDeviceLNR,
       "cmmIpmiDeviceLNRRecovery": cmmIpmiDeviceLNRRecovery,
       "cmmIpmiDeviceUNC": cmmIpmiDeviceUNC,
       "cmmIpmiDeviceUNCRecovery": cmmIpmiDeviceUNCRecovery,
       "cmmIpmiDeviceUC": cmmIpmiDeviceUC,
       "cmmIpmiDeviceUCRecovery": cmmIpmiDeviceUCRecovery,
       "cmmIpmiDeviceUNR": cmmIpmiDeviceUNR,
       "cmmIpmiDeviceUNRRecovery": cmmIpmiDeviceUNRRecovery,
       "cmmIpmiDevicePresence": cmmIpmiDevicePresence,
       "cmmIpmiDeviceStatus": cmmIpmiDeviceStatus}
)
