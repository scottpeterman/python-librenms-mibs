# SNMP MIB module (IFOTEC-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ifotec\IFOTEC-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:26 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ifotec = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21362)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IfotecDataStatus(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("noData", 1),
          ("ok", 2),
          ("warning", 3),
          ("warningLowThreshold", 4),
          ("warningHighThreshold", 5),
          ("error", 6),
          ("errorLowThreshold", 7),
          ("errorHighThreshold", 8),
          ("errorWrongData", 9),
          ("errorLowDataOverflow", 10),
          ("errorHighDataOverflow", 11))
    )



# MIB Managed Objects in the order of their OIDs

_IfotecGeneral_ObjectIdentity = ObjectIdentity
ifotecGeneral = _IfotecGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21362, 101)
)
if mibBuilder.loadTexts:
    ifotecGeneral.setStatus("current")
_IfotecSystem_ObjectIdentity = ObjectIdentity
ifotecSystem = _IfotecSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1)
)
if mibBuilder.loadTexts:
    ifotecSystem.setStatus("current")
_IfoSysProductIndex_Type = Integer32
_IfoSysProductIndex_Object = MibScalar
ifoSysProductIndex = _IfoSysProductIndex_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 1),
    _IfoSysProductIndex_Type()
)
ifoSysProductIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoSysProductIndex.setStatus("current")
_IfoSysTable_Object = MibTable
ifoSysTable = _IfoSysTable_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 2)
)
if mibBuilder.loadTexts:
    ifoSysTable.setStatus("current")
_IfoSysEntry_Object = MibTableRow
ifoSysEntry = _IfoSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1)
)
ifoSysEntry.setIndexNames(
    (0, "IFOTEC-SMI", "ifoSysIndex"),
)
if mibBuilder.loadTexts:
    ifoSysEntry.setStatus("current")
_IfoSysIndex_Type = Integer32
_IfoSysIndex_Object = MibTableColumn
ifoSysIndex = _IfoSysIndex_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 1),
    _IfoSysIndex_Type()
)
ifoSysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifoSysIndex.setStatus("current")
_IfoSysRef_Type = DisplayString
_IfoSysRef_Object = MibTableColumn
ifoSysRef = _IfoSysRef_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 2),
    _IfoSysRef_Type()
)
ifoSysRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoSysRef.setStatus("current")
_IfoSysInfo_Type = DisplayString
_IfoSysInfo_Object = MibTableColumn
ifoSysInfo = _IfoSysInfo_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 3),
    _IfoSysInfo_Type()
)
ifoSysInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoSysInfo.setStatus("current")
_IfoSysFamilly_Type = DisplayString
_IfoSysFamilly_Object = MibTableColumn
ifoSysFamilly = _IfoSysFamilly_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 4),
    _IfoSysFamilly_Type()
)
ifoSysFamilly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoSysFamilly.setStatus("current")
_IfoSysSerialNumber_Type = DisplayString
_IfoSysSerialNumber_Object = MibTableColumn
ifoSysSerialNumber = _IfoSysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 5),
    _IfoSysSerialNumber_Type()
)
ifoSysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoSysSerialNumber.setStatus("current")
_IfoSysDateCode_Type = DisplayString
_IfoSysDateCode_Object = MibTableColumn
ifoSysDateCode = _IfoSysDateCode_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 6),
    _IfoSysDateCode_Type()
)
ifoSysDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoSysDateCode.setStatus("current")
_IfoSysFirmware_Type = DisplayString
_IfoSysFirmware_Object = MibTableColumn
ifoSysFirmware = _IfoSysFirmware_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 7),
    _IfoSysFirmware_Type()
)
ifoSysFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoSysFirmware.setStatus("current")
_IfoSysBootloader_Type = DisplayString
_IfoSysBootloader_Object = MibTableColumn
ifoSysBootloader = _IfoSysBootloader_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 8),
    _IfoSysBootloader_Type()
)
ifoSysBootloader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoSysBootloader.setStatus("current")
_IfoSysDescr_Type = DisplayString
_IfoSysDescr_Object = MibTableColumn
ifoSysDescr = _IfoSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 9),
    _IfoSysDescr_Type()
)
ifoSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoSysDescr.setStatus("current")
_IfoSysLocation_Type = DisplayString
_IfoSysLocation_Object = MibTableColumn
ifoSysLocation = _IfoSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 10),
    _IfoSysLocation_Type()
)
ifoSysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoSysLocation.setStatus("current")
_IfoSysContact_Type = DisplayString
_IfoSysContact_Object = MibTableColumn
ifoSysContact = _IfoSysContact_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 11),
    _IfoSysContact_Type()
)
ifoSysContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoSysContact.setStatus("current")
_IfoSysUpTime_Type = TimeTicks
_IfoSysUpTime_Object = MibTableColumn
ifoSysUpTime = _IfoSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 12),
    _IfoSysUpTime_Type()
)
ifoSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoSysUpTime.setStatus("current")
_IfoSysMibTable_Object = MibTable
ifoSysMibTable = _IfoSysMibTable_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 3)
)
if mibBuilder.loadTexts:
    ifoSysMibTable.setStatus("current")
_IfoSysMibEntry_Object = MibTableRow
ifoSysMibEntry = _IfoSysMibEntry_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 3, 1)
)
ifoSysMibEntry.setIndexNames(
    (0, "IFOTEC-SMI", "ifoSysORIfoSysIndex"),
    (0, "IFOTEC-SMI", "ifoSysORIndex"),
)
if mibBuilder.loadTexts:
    ifoSysMibEntry.setStatus("current")
_IfoSysORIfoSysIndex_Type = Integer32
_IfoSysORIfoSysIndex_Object = MibTableColumn
ifoSysORIfoSysIndex = _IfoSysORIfoSysIndex_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 3, 1, 1),
    _IfoSysORIfoSysIndex_Type()
)
ifoSysORIfoSysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifoSysORIfoSysIndex.setStatus("current")
_IfoSysORIndex_Type = Integer32
_IfoSysORIndex_Object = MibTableColumn
ifoSysORIndex = _IfoSysORIndex_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 3, 1, 2),
    _IfoSysORIndex_Type()
)
ifoSysORIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifoSysORIndex.setStatus("current")
_IfoSysORID_Type = ObjectIdentifier
_IfoSysORID_Object = MibTableColumn
ifoSysORID = _IfoSysORID_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 3, 1, 3),
    _IfoSysORID_Type()
)
ifoSysORID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoSysORID.setStatus("current")
_IfoSysORDescr_Type = DisplayString
_IfoSysORDescr_Object = MibTableColumn
ifoSysORDescr = _IfoSysORDescr_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 1, 3, 1, 4),
    _IfoSysORDescr_Type()
)
ifoSysORDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoSysORDescr.setStatus("current")
_IfotecTemperatures_ObjectIdentity = ObjectIdentity
ifotecTemperatures = _IfotecTemperatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21362, 101, 2)
)
if mibBuilder.loadTexts:
    ifotecTemperatures.setStatus("current")
_IfoTemperatureTable_Object = MibTable
ifoTemperatureTable = _IfoTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 2, 1)
)
if mibBuilder.loadTexts:
    ifoTemperatureTable.setStatus("current")
_IfoTemperatureEntry_Object = MibTableRow
ifoTemperatureEntry = _IfoTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1)
)
ifoTemperatureEntry.setIndexNames(
    (0, "IFOTEC-SMI", "ifoTempIfoSysIndex"),
    (0, "IFOTEC-SMI", "ifoTempIndex"),
)
if mibBuilder.loadTexts:
    ifoTemperatureEntry.setStatus("current")
_IfoTempIfoSysIndex_Type = Integer32
_IfoTempIfoSysIndex_Object = MibTableColumn
ifoTempIfoSysIndex = _IfoTempIfoSysIndex_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 1),
    _IfoTempIfoSysIndex_Type()
)
ifoTempIfoSysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifoTempIfoSysIndex.setStatus("current")
_IfoTempIndex_Type = Integer32
_IfoTempIndex_Object = MibTableColumn
ifoTempIndex = _IfoTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 2),
    _IfoTempIndex_Type()
)
ifoTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifoTempIndex.setStatus("current")
_IfoTempName_Type = DisplayString
_IfoTempName_Object = MibTableColumn
ifoTempName = _IfoTempName_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 3),
    _IfoTempName_Type()
)
ifoTempName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoTempName.setStatus("current")
_IfoTempDescr_Type = DisplayString
_IfoTempDescr_Object = MibTableColumn
ifoTempDescr = _IfoTempDescr_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 4),
    _IfoTempDescr_Type()
)
ifoTempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoTempDescr.setStatus("current")
_IfoTempValue_Type = Integer32
_IfoTempValue_Object = MibTableColumn
ifoTempValue = _IfoTempValue_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 5),
    _IfoTempValue_Type()
)
ifoTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoTempValue.setStatus("current")
_IfoTempAlarmStatus_Type = IfotecDataStatus
_IfoTempAlarmStatus_Object = MibTableColumn
ifoTempAlarmStatus = _IfoTempAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 6),
    _IfoTempAlarmStatus_Type()
)
ifoTempAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoTempAlarmStatus.setStatus("current")
_IfoTempLowThldAlarm_Type = Integer32
_IfoTempLowThldAlarm_Object = MibTableColumn
ifoTempLowThldAlarm = _IfoTempLowThldAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 7),
    _IfoTempLowThldAlarm_Type()
)
ifoTempLowThldAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoTempLowThldAlarm.setStatus("current")
_IfoTempHighThldAlarm_Type = Integer32
_IfoTempHighThldAlarm_Object = MibTableColumn
ifoTempHighThldAlarm = _IfoTempHighThldAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 8),
    _IfoTempHighThldAlarm_Type()
)
ifoTempHighThldAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoTempHighThldAlarm.setStatus("current")
_IfoTempLowThldWarning_Type = Integer32
_IfoTempLowThldWarning_Object = MibTableColumn
ifoTempLowThldWarning = _IfoTempLowThldWarning_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 9),
    _IfoTempLowThldWarning_Type()
)
ifoTempLowThldWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoTempLowThldWarning.setStatus("current")
_IfoTempHighThldWarning_Type = Integer32
_IfoTempHighThldWarning_Object = MibTableColumn
ifoTempHighThldWarning = _IfoTempHighThldWarning_Object(
    (1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 10),
    _IfoTempHighThldWarning_Type()
)
ifoTempHighThldWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoTempHighThldWarning.setStatus("current")
_IfotecModules_ObjectIdentity = ObjectIdentity
ifotecModules = _IfotecModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21362, 102)
)
if mibBuilder.loadTexts:
    ifotecModules.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IFOTEC-SMI",
    **{"IfotecDataStatus": IfotecDataStatus,
       "ifotec": ifotec,
       "ifotecGeneral": ifotecGeneral,
       "ifotecSystem": ifotecSystem,
       "ifoSysProductIndex": ifoSysProductIndex,
       "ifoSysTable": ifoSysTable,
       "ifoSysEntry": ifoSysEntry,
       "ifoSysIndex": ifoSysIndex,
       "ifoSysRef": ifoSysRef,
       "ifoSysInfo": ifoSysInfo,
       "ifoSysFamilly": ifoSysFamilly,
       "ifoSysSerialNumber": ifoSysSerialNumber,
       "ifoSysDateCode": ifoSysDateCode,
       "ifoSysFirmware": ifoSysFirmware,
       "ifoSysBootloader": ifoSysBootloader,
       "ifoSysDescr": ifoSysDescr,
       "ifoSysLocation": ifoSysLocation,
       "ifoSysContact": ifoSysContact,
       "ifoSysUpTime": ifoSysUpTime,
       "ifoSysMibTable": ifoSysMibTable,
       "ifoSysMibEntry": ifoSysMibEntry,
       "ifoSysORIfoSysIndex": ifoSysORIfoSysIndex,
       "ifoSysORIndex": ifoSysORIndex,
       "ifoSysORID": ifoSysORID,
       "ifoSysORDescr": ifoSysORDescr,
       "ifotecTemperatures": ifotecTemperatures,
       "ifoTemperatureTable": ifoTemperatureTable,
       "ifoTemperatureEntry": ifoTemperatureEntry,
       "ifoTempIfoSysIndex": ifoTempIfoSysIndex,
       "ifoTempIndex": ifoTempIndex,
       "ifoTempName": ifoTempName,
       "ifoTempDescr": ifoTempDescr,
       "ifoTempValue": ifoTempValue,
       "ifoTempAlarmStatus": ifoTempAlarmStatus,
       "ifoTempLowThldAlarm": ifoTempLowThldAlarm,
       "ifoTempHighThldAlarm": ifoTempHighThldAlarm,
       "ifoTempLowThldWarning": ifoTempLowThldWarning,
       "ifoTempHighThldWarning": ifoTempHighThldWarning,
       "ifotecModules": ifotecModules}
)
