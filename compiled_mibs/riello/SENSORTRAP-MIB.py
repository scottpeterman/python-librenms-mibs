# SNMP MIB module (SENSORTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\riello\SENSORTRAP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:26 2025
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RielloMIB_ObjectIdentity = ObjectIdentity
rielloMIB = _RielloMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5491)
)
_Sensorgroup_ObjectIdentity = ObjectIdentity
sensorgroup = _Sensorgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5491, 9)
)
_Sensor_ObjectIdentity = ObjectIdentity
sensor = _Sensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5491, 9, 1)
)
_SensorId_Type = Integer32
_SensorId_Object = MibScalar
sensorId = _SensorId_Object(
    (1, 3, 6, 1, 4, 1, 5491, 9, 1, 1),
    _SensorId_Type()
)
sensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorId.setStatus("mandatory")
_SensorTrapGroup_ObjectIdentity = ObjectIdentity
sensorTrapGroup = _SensorTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5491, 9, 1, 2)
)

# Managed Objects groups


# Notification objects

sensorAlarmTMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 5491, 9, 1, 2, 0, 1)
)
sensorAlarmTMax.setObjects(
    ("SENSORTRAP-MIB", "sensorId")
)
if mibBuilder.loadTexts:
    sensorAlarmTMax.setStatus(
        ""
    )

sensorAlarmTMaxRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 5491, 9, 1, 2, 0, 2)
)
sensorAlarmTMaxRemoved.setObjects(
    ("SENSORTRAP-MIB", "sensorId")
)
if mibBuilder.loadTexts:
    sensorAlarmTMaxRemoved.setStatus(
        ""
    )

sensorAlarmTMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 5491, 9, 1, 2, 0, 3)
)
sensorAlarmTMin.setObjects(
    ("SENSORTRAP-MIB", "sensorId")
)
if mibBuilder.loadTexts:
    sensorAlarmTMin.setStatus(
        ""
    )

sensorAlarmTMinRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 5491, 9, 1, 2, 0, 4)
)
sensorAlarmTMinRemoved.setObjects(
    ("SENSORTRAP-MIB", "sensorId")
)
if mibBuilder.loadTexts:
    sensorAlarmTMinRemoved.setStatus(
        ""
    )

sensorIOAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5491, 9, 1, 2, 0, 5)
)
sensorIOAlarm.setObjects(
    ("SENSORTRAP-MIB", "sensorId")
)
if mibBuilder.loadTexts:
    sensorIOAlarm.setStatus(
        ""
    )

sensorIOAlarmRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 5491, 9, 1, 2, 0, 6)
)
sensorIOAlarmRemoved.setObjects(
    ("SENSORTRAP-MIB", "sensorId")
)
if mibBuilder.loadTexts:
    sensorIOAlarmRemoved.setStatus(
        ""
    )

sensorHumidityAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5491, 9, 1, 2, 0, 7)
)
sensorHumidityAlarm.setObjects(
    ("SENSORTRAP-MIB", "sensorId")
)
if mibBuilder.loadTexts:
    sensorHumidityAlarm.setStatus(
        ""
    )

sensorHumidityAlarmRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 5491, 9, 1, 2, 0, 8)
)
sensorHumidityAlarmRemoved.setObjects(
    ("SENSORTRAP-MIB", "sensorId")
)
if mibBuilder.loadTexts:
    sensorHumidityAlarmRemoved.setStatus(
        ""
    )

sensorHumidityLowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5491, 9, 1, 2, 0, 9)
)
sensorHumidityLowAlarm.setObjects(
    ("SENSORTRAP-MIB", "sensorId")
)
if mibBuilder.loadTexts:
    sensorHumidityLowAlarm.setStatus(
        ""
    )

sensorHumidityLowAlarmRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 5491, 9, 1, 2, 0, 10)
)
sensorHumidityLowAlarmRemoved.setObjects(
    ("SENSORTRAP-MIB", "sensorId")
)
if mibBuilder.loadTexts:
    sensorHumidityLowAlarmRemoved.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SENSORTRAP-MIB",
    **{"rielloMIB": rielloMIB,
       "sensorgroup": sensorgroup,
       "sensor": sensor,
       "sensorId": sensorId,
       "sensorTrapGroup": sensorTrapGroup,
       "sensorAlarmTMax": sensorAlarmTMax,
       "sensorAlarmTMaxRemoved": sensorAlarmTMaxRemoved,
       "sensorAlarmTMin": sensorAlarmTMin,
       "sensorAlarmTMinRemoved": sensorAlarmTMinRemoved,
       "sensorIOAlarm": sensorIOAlarm,
       "sensorIOAlarmRemoved": sensorIOAlarmRemoved,
       "sensorHumidityAlarm": sensorHumidityAlarm,
       "sensorHumidityAlarmRemoved": sensorHumidityAlarmRemoved,
       "sensorHumidityLowAlarm": sensorHumidityLowAlarm,
       "sensorHumidityLowAlarmRemoved": sensorHumidityLowAlarmRemoved}
)
