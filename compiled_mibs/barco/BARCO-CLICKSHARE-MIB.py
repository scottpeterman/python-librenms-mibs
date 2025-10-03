# SNMP MIB module (BARCO-CLICKSHARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\barco\BARCO-CLICKSHARE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:47 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

clickShare = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7312, 2468)
)
if mibBuilder.loadTexts:
    clickShare.setRevisions(
        ("2018-12-04 09:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Barco_ObjectIdentity = ObjectIdentity
barco = _Barco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7312)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7312, 2468, 0)
)
_BaseUnit_ObjectIdentity = ObjectIdentity
baseUnit = _BaseUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7312, 2468, 1)
)
_DeviceInfo_ObjectIdentity = ObjectIdentity
deviceInfo = _DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7312, 2468, 1, 1)
)
_DiRoomName_Type = DisplayString
_DiRoomName_Object = MibScalar
diRoomName = _DiRoomName_Object(
    (1, 3, 6, 1, 4, 1, 7312, 2468, 1, 1, 1),
    _DiRoomName_Type()
)
diRoomName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diRoomName.setStatus("current")
_DiWelcomeMessage_Type = DisplayString
_DiWelcomeMessage_Object = MibScalar
diWelcomeMessage = _DiWelcomeMessage_Object(
    (1, 3, 6, 1, 4, 1, 7312, 2468, 1, 1, 2),
    _DiWelcomeMessage_Type()
)
diWelcomeMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diWelcomeMessage.setStatus("current")
_DiLocation_Type = DisplayString
_DiLocation_Object = MibScalar
diLocation = _DiLocation_Object(
    (1, 3, 6, 1, 4, 1, 7312, 2468, 1, 1, 3),
    _DiLocation_Type()
)
diLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diLocation.setStatus("current")
_DiArticleCode_Type = DisplayString
_DiArticleCode_Object = MibScalar
diArticleCode = _DiArticleCode_Object(
    (1, 3, 6, 1, 4, 1, 7312, 2468, 1, 1, 4),
    _DiArticleCode_Type()
)
diArticleCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diArticleCode.setStatus("current")
_DiSerialNumber_Type = DisplayString
_DiSerialNumber_Object = MibScalar
diSerialNumber = _DiSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7312, 2468, 1, 1, 5),
    _DiSerialNumber_Type()
)
diSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diSerialNumber.setStatus("current")
_DiUptime_Type = Unsigned32
_DiUptime_Object = MibScalar
diUptime = _DiUptime_Object(
    (1, 3, 6, 1, 4, 1, 7312, 2468, 1, 1, 6),
    _DiUptime_Type()
)
diUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diUptime.setStatus("current")
_DiTotalUptime_Type = Unsigned32
_DiTotalUptime_Object = MibScalar
diTotalUptime = _DiTotalUptime_Object(
    (1, 3, 6, 1, 4, 1, 7312, 2468, 1, 1, 7),
    _DiTotalUptime_Type()
)
diTotalUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diTotalUptime.setStatus("current")
_Sensors_ObjectIdentity = ObjectIdentity
sensors = _Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7312, 2468, 1, 2)
)
_SensorCaseFanSpeed_Type = DisplayString
_SensorCaseFanSpeed_Object = MibScalar
sensorCaseFanSpeed = _SensorCaseFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7312, 2468, 1, 2, 1),
    _SensorCaseFanSpeed_Type()
)
sensorCaseFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorCaseFanSpeed.setStatus("current")
_SensorCpuFanSpeed_Type = DisplayString
_SensorCpuFanSpeed_Object = MibScalar
sensorCpuFanSpeed = _SensorCpuFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7312, 2468, 1, 2, 2),
    _SensorCpuFanSpeed_Type()
)
sensorCpuFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorCpuFanSpeed.setStatus("current")
_SensorCpuTemperature_Type = DisplayString
_SensorCpuTemperature_Object = MibScalar
sensorCpuTemperature = _SensorCpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7312, 2468, 1, 2, 3),
    _SensorCpuTemperature_Type()
)
sensorCpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorCpuTemperature.setStatus("current")
_SensorCpuTemperatureThreshold_Type = DisplayString
_SensorCpuTemperatureThreshold_Object = MibScalar
sensorCpuTemperatureThreshold = _SensorCpuTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7312, 2468, 1, 2, 4),
    _SensorCpuTemperatureThreshold_Type()
)
sensorCpuTemperatureThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorCpuTemperatureThreshold.setStatus("current")
_ClickShareMIB_ObjectIdentity = ObjectIdentity
clickShareMIB = _ClickShareMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7312, 2469)
)
_ClickShareMIBCompliances_ObjectIdentity = ObjectIdentity
clickShareMIBCompliances = _ClickShareMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7312, 2469, 1)
)
_ClickShareMIBGroups_ObjectIdentity = ObjectIdentity
clickShareMIBGroups = _ClickShareMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7312, 2469, 2)
)

# Managed Objects groups

deviceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7312, 2469, 2, 1)
)
deviceInfoGroup.setObjects(
      *(("BARCO-CLICKSHARE-MIB", "diRoomName"),
        ("BARCO-CLICKSHARE-MIB", "diWelcomeMessage"),
        ("BARCO-CLICKSHARE-MIB", "diLocation"),
        ("BARCO-CLICKSHARE-MIB", "diArticleCode"),
        ("BARCO-CLICKSHARE-MIB", "diSerialNumber"),
        ("BARCO-CLICKSHARE-MIB", "diUptime"),
        ("BARCO-CLICKSHARE-MIB", "diTotalUptime"))
)
if mibBuilder.loadTexts:
    deviceInfoGroup.setStatus("current")

sensorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7312, 2469, 2, 2)
)
sensorsGroup.setObjects(
      *(("BARCO-CLICKSHARE-MIB", "sensorCaseFanSpeed"),
        ("BARCO-CLICKSHARE-MIB", "sensorCpuFanSpeed"),
        ("BARCO-CLICKSHARE-MIB", "sensorCpuTemperature"),
        ("BARCO-CLICKSHARE-MIB", "sensorCpuTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    sensorsGroup.setStatus("current")


# Notification objects

alarmCpuTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 7312, 2468, 0, 1)
)
if mibBuilder.loadTexts:
    alarmCpuTemperature.setStatus(
        "current"
    )

alarmCaseFanSpeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7312, 2468, 0, 2)
)
if mibBuilder.loadTexts:
    alarmCaseFanSpeed.setStatus(
        "current"
    )

alarmProcessNotRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 7312, 2468, 0, 3)
)
if mibBuilder.loadTexts:
    alarmProcessNotRunning.setStatus(
        "current"
    )


# Notifications groups

eventsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7312, 2469, 2, 99)
)
eventsGroup.setObjects(
      *(("BARCO-CLICKSHARE-MIB", "alarmCpuTemperature"),
        ("BARCO-CLICKSHARE-MIB", "alarmCaseFanSpeed"),
        ("BARCO-CLICKSHARE-MIB", "alarmProcessNotRunning"))
)
if mibBuilder.loadTexts:
    eventsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

clickShareMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7312, 2469, 1, 1)
)
clickShareMIBCompliance.setObjects(
      *(("BARCO-CLICKSHARE-MIB", "deviceInfoGroup"),
        ("BARCO-CLICKSHARE-MIB", "sensorsGroup"),
        ("BARCO-CLICKSHARE-MIB", "eventsGroup"))
)
if mibBuilder.loadTexts:
    clickShareMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BARCO-CLICKSHARE-MIB",
    **{"barco": barco,
       "clickShare": clickShare,
       "events": events,
       "alarmCpuTemperature": alarmCpuTemperature,
       "alarmCaseFanSpeed": alarmCaseFanSpeed,
       "alarmProcessNotRunning": alarmProcessNotRunning,
       "baseUnit": baseUnit,
       "deviceInfo": deviceInfo,
       "diRoomName": diRoomName,
       "diWelcomeMessage": diWelcomeMessage,
       "diLocation": diLocation,
       "diArticleCode": diArticleCode,
       "diSerialNumber": diSerialNumber,
       "diUptime": diUptime,
       "diTotalUptime": diTotalUptime,
       "sensors": sensors,
       "sensorCaseFanSpeed": sensorCaseFanSpeed,
       "sensorCpuFanSpeed": sensorCpuFanSpeed,
       "sensorCpuTemperature": sensorCpuTemperature,
       "sensorCpuTemperatureThreshold": sensorCpuTemperatureThreshold,
       "clickShareMIB": clickShareMIB,
       "clickShareMIBCompliances": clickShareMIBCompliances,
       "clickShareMIBCompliance": clickShareMIBCompliance,
       "clickShareMIBGroups": clickShareMIBGroups,
       "deviceInfoGroup": deviceInfoGroup,
       "sensorsGroup": sensorsGroup,
       "eventsGroup": eventsGroup}
)
