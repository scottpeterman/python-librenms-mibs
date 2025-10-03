# SNMP MIB module (MDS-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\gemds\MDS-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:38 2025
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

(mdsSystem,) = mibBuilder.importSymbols(
    "MDS-ORBIT-SMI-MIB",
    "mdsSystem")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mdsSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1)
)
if mibBuilder.loadTexts:
    mdsSystemMIB.setRevisions(
        ("2019-11-18 00:00",
         "2018-05-16 00:00",
         "2014-02-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FirmwareLocation(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_MSysMIBObjects_ObjectIdentity = ObjectIdentity
mSysMIBObjects = _MSysMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1)
)
_MSysConfig_ObjectIdentity = ObjectIdentity
mSysConfig = _MSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 1)
)
_MSysStatus_ObjectIdentity = ObjectIdentity
mSysStatus = _MSysStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2)
)
_MSysSerialNumberCore_Type = Unsigned32
_MSysSerialNumberCore_Object = MibScalar
mSysSerialNumberCore = _MSysSerialNumberCore_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 1),
    _MSysSerialNumberCore_Type()
)
mSysSerialNumberCore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysSerialNumberCore.setStatus("current")
_MSysSerialNumberPlatform_Type = Unsigned32
_MSysSerialNumberPlatform_Object = MibScalar
mSysSerialNumberPlatform = _MSysSerialNumberPlatform_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 2),
    _MSysSerialNumberPlatform_Type()
)
mSysSerialNumberPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysSerialNumberPlatform.setStatus("current")
_MSysProductConfiguration_Type = OctetString
_MSysProductConfiguration_Object = MibScalar
mSysProductConfiguration = _MSysProductConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 3),
    _MSysProductConfiguration_Type()
)
mSysProductConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysProductConfiguration.setStatus("current")
_MSysGuid_Type = OctetString
_MSysGuid_Object = MibScalar
mSysGuid = _MSysGuid_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 4),
    _MSysGuid_Type()
)
mSysGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysGuid.setStatus("current")
_MSysUptime_Type = OctetString
_MSysUptime_Object = MibScalar
mSysUptime = _MSysUptime_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 5),
    _MSysUptime_Type()
)
mSysUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysUptime.setStatus("current")
_MSysTemperature_Type = Integer32
_MSysTemperature_Object = MibScalar
mSysTemperature = _MSysTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 6),
    _MSysTemperature_Type()
)
mSysTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysTemperature.setStatus("current")
_MSysFirmwareVersionTable_Object = MibTable
mSysFirmwareVersionTable = _MSysFirmwareVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    mSysFirmwareVersionTable.setStatus("current")
_MSysFirmwareVersionEntry_Object = MibTableRow
mSysFirmwareVersionEntry = _MSysFirmwareVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 7, 1)
)
mSysFirmwareVersionEntry.setIndexNames(
    (0, "MDS-SYSTEM-MIB", "mSysLocation"),
)
if mibBuilder.loadTexts:
    mSysFirmwareVersionEntry.setStatus("current")
_MSysLocation_Type = FirmwareLocation
_MSysLocation_Object = MibTableColumn
mSysLocation = _MSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 7, 1, 1),
    _MSysLocation_Type()
)
mSysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysLocation.setStatus("current")
_MSysVersion_Type = OctetString
_MSysVersion_Object = MibTableColumn
mSysVersion = _MSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 7, 1, 2),
    _MSysVersion_Type()
)
mSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysVersion.setStatus("current")
_MSysActive_Type = TruthValue
_MSysActive_Object = MibTableColumn
mSysActive = _MSysActive_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 7, 1, 3),
    _MSysActive_Type()
)
mSysActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysActive.setStatus("current")
_MSysMprStatus_ObjectIdentity = ObjectIdentity
mSysMprStatus = _MSysMprStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 8)
)
_MSysMprHeatsinkTemperature1_Type = Integer32
_MSysMprHeatsinkTemperature1_Object = MibScalar
mSysMprHeatsinkTemperature1 = _MSysMprHeatsinkTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 8, 1),
    _MSysMprHeatsinkTemperature1_Type()
)
mSysMprHeatsinkTemperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysMprHeatsinkTemperature1.setStatus("current")
_MSysMprHeatsinkTemperature2_Type = Integer32
_MSysMprHeatsinkTemperature2_Object = MibScalar
mSysMprHeatsinkTemperature2 = _MSysMprHeatsinkTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 8, 2),
    _MSysMprHeatsinkTemperature2_Type()
)
mSysMprHeatsinkTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysMprHeatsinkTemperature2.setStatus("current")
_MSysMprPowerSupplyVoltage1_Type = OctetString
_MSysMprPowerSupplyVoltage1_Object = MibScalar
mSysMprPowerSupplyVoltage1 = _MSysMprPowerSupplyVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 8, 3),
    _MSysMprPowerSupplyVoltage1_Type()
)
mSysMprPowerSupplyVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysMprPowerSupplyVoltage1.setStatus("current")
_MSysMprPowerSupplyVoltage2_Type = OctetString
_MSysMprPowerSupplyVoltage2_Object = MibScalar
mSysMprPowerSupplyVoltage2 = _MSysMprPowerSupplyVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 8, 4),
    _MSysMprPowerSupplyVoltage2_Type()
)
mSysMprPowerSupplyVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysMprPowerSupplyVoltage2.setStatus("current")
_MSysMprRelaySwitchPosition_Type = OctetString
_MSysMprRelaySwitchPosition_Object = MibScalar
mSysMprRelaySwitchPosition = _MSysMprRelaySwitchPosition_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 8, 5),
    _MSysMprRelaySwitchPosition_Type()
)
mSysMprRelaySwitchPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysMprRelaySwitchPosition.setStatus("current")
_MSysPowerSupplyVoltage_Type = OctetString
_MSysPowerSupplyVoltage_Object = MibScalar
mSysPowerSupplyVoltage = _MSysPowerSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 9),
    _MSysPowerSupplyVoltage_Type()
)
mSysPowerSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysPowerSupplyVoltage.setStatus("current")
_MSysCurrentDateTime_Type = DateAndTime
_MSysCurrentDateTime_Object = MibScalar
mSysCurrentDateTime = _MSysCurrentDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 10),
    _MSysCurrentDateTime_Type()
)
mSysCurrentDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysCurrentDateTime.setStatus("current")
_MSysBootDateTime_Type = DateAndTime
_MSysBootDateTime_Object = MibScalar
mSysBootDateTime = _MSysBootDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 11),
    _MSysBootDateTime_Type()
)
mSysBootDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysBootDateTime.setStatus("current")
_MSysAutoUpdateState_Type = Unsigned32
_MSysAutoUpdateState_Object = MibScalar
mSysAutoUpdateState = _MSysAutoUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 12),
    _MSysAutoUpdateState_Type()
)
mSysAutoUpdateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysAutoUpdateState.setStatus("current")
_MSysAutoUpdateDetails_Type = OctetString
_MSysAutoUpdateDetails_Object = MibScalar
mSysAutoUpdateDetails = _MSysAutoUpdateDetails_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 13),
    _MSysAutoUpdateDetails_Type()
)
mSysAutoUpdateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysAutoUpdateDetails.setStatus("current")
_MdsSysMIBConformance_ObjectIdentity = ObjectIdentity
mdsSysMIBConformance = _MdsSysMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 3)
)
_MdsSysMIBCompliances_ObjectIdentity = ObjectIdentity
mdsSysMIBCompliances = _MdsSysMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 3, 1)
)
_MdsSysMIBGroups_ObjectIdentity = ObjectIdentity
mdsSysMIBGroups = _MdsSysMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 3, 2)
)

# Managed Objects groups

mSysStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 3, 2, 1)
)
mSysStatusGroup.setObjects(
      *(("MDS-SYSTEM-MIB", "mSysSerialNumberCore"),
        ("MDS-SYSTEM-MIB", "mSysSerialNumberPlatform"),
        ("MDS-SYSTEM-MIB", "mSysProductConfiguration"),
        ("MDS-SYSTEM-MIB", "mSysGuid"),
        ("MDS-SYSTEM-MIB", "mSysUptime"),
        ("MDS-SYSTEM-MIB", "mSysTemperature"),
        ("MDS-SYSTEM-MIB", "mSysPowerSupplyVoltage"),
        ("MDS-SYSTEM-MIB", "mSysLocation"),
        ("MDS-SYSTEM-MIB", "mSysVersion"),
        ("MDS-SYSTEM-MIB", "mSysActive"))
)
if mibBuilder.loadTexts:
    mSysStatusGroup.setStatus("current")

mSysMprStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 3, 2, 2)
)
mSysMprStatusGroup.setObjects(
      *(("MDS-SYSTEM-MIB", "mSysMprHeatsinkTemperature1"),
        ("MDS-SYSTEM-MIB", "mSysMprHeatsinkTemperature2"),
        ("MDS-SYSTEM-MIB", "mSysMprPowerSupplyVoltage1"),
        ("MDS-SYSTEM-MIB", "mSysMprPowerSupplyVoltage2"),
        ("MDS-SYSTEM-MIB", "mSysMprRelaySwitchPosition"))
)
if mibBuilder.loadTexts:
    mSysMprStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mSysCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 3, 1, 1)
)
mSysCompliance.setObjects(
      *(("MDS-SYSTEM-MIB", "mSysStatusGroup"),
        ("MDS-SYSTEM-MIB", "mSysMprStatusGroup"))
)
if mibBuilder.loadTexts:
    mSysCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MDS-SYSTEM-MIB",
    **{"FirmwareLocation": FirmwareLocation,
       "mdsSystemMIB": mdsSystemMIB,
       "mSysMIBObjects": mSysMIBObjects,
       "mSysConfig": mSysConfig,
       "mSysStatus": mSysStatus,
       "mSysSerialNumberCore": mSysSerialNumberCore,
       "mSysSerialNumberPlatform": mSysSerialNumberPlatform,
       "mSysProductConfiguration": mSysProductConfiguration,
       "mSysGuid": mSysGuid,
       "mSysUptime": mSysUptime,
       "mSysTemperature": mSysTemperature,
       "mSysFirmwareVersionTable": mSysFirmwareVersionTable,
       "mSysFirmwareVersionEntry": mSysFirmwareVersionEntry,
       "mSysLocation": mSysLocation,
       "mSysVersion": mSysVersion,
       "mSysActive": mSysActive,
       "mSysMprStatus": mSysMprStatus,
       "mSysMprHeatsinkTemperature1": mSysMprHeatsinkTemperature1,
       "mSysMprHeatsinkTemperature2": mSysMprHeatsinkTemperature2,
       "mSysMprPowerSupplyVoltage1": mSysMprPowerSupplyVoltage1,
       "mSysMprPowerSupplyVoltage2": mSysMprPowerSupplyVoltage2,
       "mSysMprRelaySwitchPosition": mSysMprRelaySwitchPosition,
       "mSysPowerSupplyVoltage": mSysPowerSupplyVoltage,
       "mSysCurrentDateTime": mSysCurrentDateTime,
       "mSysBootDateTime": mSysBootDateTime,
       "mSysAutoUpdateState": mSysAutoUpdateState,
       "mSysAutoUpdateDetails": mSysAutoUpdateDetails,
       "mdsSysMIBConformance": mdsSysMIBConformance,
       "mdsSysMIBCompliances": mdsSysMIBCompliances,
       "mSysCompliance": mSysCompliance,
       "mdsSysMIBGroups": mdsSysMIBGroups,
       "mSysStatusGroup": mSysStatusGroup,
       "mSysMprStatusGroup": mSysMprStatusGroup}
)
