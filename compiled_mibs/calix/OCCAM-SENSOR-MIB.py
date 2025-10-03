# SNMP MIB module (OCCAM-SENSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\calix\OCCAM-SENSOR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:25 2025
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "OCCAM-ENTITY-MIB",
    "PhysicalIndex")

(occamGenericHardwareModules,) = mibBuilder.importSymbols(
    "OCCAM-REG-MODULE",
    "occamGenericHardwareModules")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

sensorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sensorMIB.setRevisions(
        ("2001-04-27 10:51",
         "2010-04-14 00:00",
         "2009-07-06 00:00",
         "2007-02-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SensorThresholdRelation(TextualConvention, Integer32):
    status = "current"
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
        *(("lessThan", 1),
          ("lessOrEqual", 2),
          ("greaterThan", 3),
          ("greaterOrEqual", 4),
          ("equalTo", 5),
          ("notEqualTo", 6))
    )



class SensorStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("unavailable", 2),
          ("nonoperational", 3))
    )



class SensorValue(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )



class SensorDataType(TextualConvention, Integer32):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("volts", 2),
          ("celsius", 3),
          ("rpm", 4),
          ("milliAmp", 5),
          ("microAmp", 6),
          ("milliWatt", 7),
          ("microWatt", 8),
          ("alarmInput", 9),
          ("sdram", 10),
          ("usage", 11),
          ("count", 12))
    )



class SensorThresholdSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              20,
              30)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("minor", 10),
          ("major", 20),
          ("critical", 30))
    )



class SensorDataScale(TextualConvention, Integer32):
    status = "current"
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
        *(("micro", 1),
          ("milli", 2),
          ("centi", 3),
          ("units", 4),
          ("kilo", 5),
          ("mega", 6))
    )



# MIB Managed Objects in the order of their OIDs

_SensorMIBObjects_ObjectIdentity = ObjectIdentity
sensorMIBObjects = _SensorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1)
)
_SensorValues_ObjectIdentity = ObjectIdentity
sensorValues = _SensorValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 1)
)
_SensorTable_Object = MibTable
sensorTable = _SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sensorTable.setStatus("current")
_SensorEntry_Object = MibTableRow
sensorEntry = _SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 1, 1, 1)
)
sensorEntry.setIndexNames(
    (0, "OCCAM-SENSOR-MIB", "sensorIndex"),
)
if mibBuilder.loadTexts:
    sensorEntry.setStatus("current")
_SensorIndex_Type = PhysicalIndex
_SensorIndex_Object = MibTableColumn
sensorIndex = _SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 1, 1, 1, 1),
    _SensorIndex_Type()
)
sensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sensorIndex.setStatus("current")
_SensorName_Type = SnmpAdminString
_SensorName_Object = MibTableColumn
sensorName = _SensorName_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 1, 1, 1, 2),
    _SensorName_Type()
)
sensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorName.setStatus("current")
_SensorType_Type = SensorDataType
_SensorType_Object = MibTableColumn
sensorType = _SensorType_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 1, 1, 1, 3),
    _SensorType_Type()
)
sensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorType.setStatus("current")
_SensorValue_Type = SensorValue
_SensorValue_Object = MibTableColumn
sensorValue = _SensorValue_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 1, 1, 1, 4),
    _SensorValue_Type()
)
sensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorValue.setStatus("current")
_SensorScale_Type = SensorDataScale
_SensorScale_Object = MibTableColumn
sensorScale = _SensorScale_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 1, 1, 1, 5),
    _SensorScale_Type()
)
sensorScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorScale.setStatus("current")
_SensorTimeStamp_Type = TimeStamp
_SensorTimeStamp_Object = MibTableColumn
sensorTimeStamp = _SensorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 1, 1, 1, 6),
    _SensorTimeStamp_Type()
)
sensorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTimeStamp.setStatus("current")
_SensorEventType_Type = DisplayString
_SensorEventType_Object = MibTableColumn
sensorEventType = _SensorEventType_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 1, 1, 1, 7),
    _SensorEventType_Type()
)
sensorEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorEventType.setStatus("current")
_OccamExtAlarmDescription_Type = DisplayString
_OccamExtAlarmDescription_Object = MibScalar
occamExtAlarmDescription = _OccamExtAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 1, 2),
    _OccamExtAlarmDescription_Type()
)
occamExtAlarmDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    occamExtAlarmDescription.setStatus("current")
_SensorThresholds_ObjectIdentity = ObjectIdentity
sensorThresholds = _SensorThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 2)
)
_SensorThresholdTable_Object = MibTable
sensorThresholdTable = _SensorThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sensorThresholdTable.setStatus("current")
_SensorThresholdEntry_Object = MibTableRow
sensorThresholdEntry = _SensorThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 2, 1, 1)
)
sensorThresholdEntry.setIndexNames(
    (0, "OCCAM-SENSOR-MIB", "sensorThresholdIndex"),
    (0, "OCCAM-SENSOR-MIB", "sensorIndex"),
)
if mibBuilder.loadTexts:
    sensorThresholdEntry.setStatus("current")


class _SensorThresholdIndex_Type(Integer32):
    """Custom type sensorThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999999),
    )


_SensorThresholdIndex_Type.__name__ = "Integer32"
_SensorThresholdIndex_Object = MibTableColumn
sensorThresholdIndex = _SensorThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 2, 1, 1, 1),
    _SensorThresholdIndex_Type()
)
sensorThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sensorThresholdIndex.setStatus("current")
_SensorThresholdSeverity_Type = SensorThresholdSeverity
_SensorThresholdSeverity_Object = MibTableColumn
sensorThresholdSeverity = _SensorThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 2, 1, 1, 2),
    _SensorThresholdSeverity_Type()
)
sensorThresholdSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorThresholdSeverity.setStatus("current")
_SensorThresholdRelation_Type = SensorThresholdRelation
_SensorThresholdRelation_Object = MibTableColumn
sensorThresholdRelation = _SensorThresholdRelation_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 2, 1, 1, 3),
    _SensorThresholdRelation_Type()
)
sensorThresholdRelation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorThresholdRelation.setStatus("current")
_SensorThresholdValue_Type = SensorValue
_SensorThresholdValue_Object = MibTableColumn
sensorThresholdValue = _SensorThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 2, 1, 1, 4),
    _SensorThresholdValue_Type()
)
sensorThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorThresholdValue.setStatus("current")
_SensorThresholdNotificationEnable_Type = TruthValue
_SensorThresholdNotificationEnable_Object = MibTableColumn
sensorThresholdNotificationEnable = _SensorThresholdNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 1, 2, 1, 1, 5),
    _SensorThresholdNotificationEnable_Type()
)
sensorThresholdNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorThresholdNotificationEnable.setStatus("current")
_SensorMIBTraps_ObjectIdentity = ObjectIdentity
sensorMIBTraps = _SensorMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 2)
)
_SensorMIBTrapsSubID_ObjectIdentity = ObjectIdentity
sensorMIBTrapsSubID = _SensorMIBTrapsSubID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 2, 0)
)
_SensorMIBConformance_ObjectIdentity = ObjectIdentity
sensorMIBConformance = _SensorMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 3)
)
_SensorMIBGroups_ObjectIdentity = ObjectIdentity
sensorMIBGroups = _SensorMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 3, 1)
)
_SensorMIBObjectGroups_ObjectIdentity = ObjectIdentity
sensorMIBObjectGroups = _SensorMIBObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 3, 1, 1)
)
_SensorMIBEventGroups_ObjectIdentity = ObjectIdentity
sensorMIBEventGroups = _SensorMIBEventGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 3, 1, 2)
)
_SensorMIBCompliances_ObjectIdentity = ObjectIdentity
sensorMIBCompliances = _SensorMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 3, 2)
)

# Managed Objects groups

sensorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 3, 1, 1, 1)
)
sensorGroup.setObjects(
      *(("OCCAM-SENSOR-MIB", "sensorType"),
        ("OCCAM-SENSOR-MIB", "sensorValue"),
        ("OCCAM-SENSOR-MIB", "sensorTimeStamp"),
        ("OCCAM-SENSOR-MIB", "sensorName"))
)
if mibBuilder.loadTexts:
    sensorGroup.setStatus("current")

sensorThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 3, 1, 1, 2)
)
sensorThresholdGroup.setObjects(
      *(("OCCAM-SENSOR-MIB", "sensorThresholdSeverity"),
        ("OCCAM-SENSOR-MIB", "sensorThresholdRelation"),
        ("OCCAM-SENSOR-MIB", "sensorThresholdValue"),
        ("OCCAM-SENSOR-MIB", "sensorThresholdNotificationEnable"))
)
if mibBuilder.loadTexts:
    sensorThresholdGroup.setStatus("current")


# Notification objects

sensorThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 2, 0, 1)
)
sensorThresholdNotification.setObjects(
      *(("OCCAM-SENSOR-MIB", "sensorName"),
        ("OCCAM-SENSOR-MIB", "sensorType"),
        ("OCCAM-SENSOR-MIB", "sensorThresholdValue"),
        ("OCCAM-SENSOR-MIB", "sensorThresholdSeverity"),
        ("OCCAM-SENSOR-MIB", "sensorEventType"))
)
if mibBuilder.loadTexts:
    sensorThresholdNotification.setStatus(
        "current"
    )

occamExtAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 2, 0, 2)
)
occamExtAlarmRaised.setObjects(
    ("OCCAM-SENSOR-MIB", "occamExtAlarmDescription")
)
if mibBuilder.loadTexts:
    occamExtAlarmRaised.setStatus(
        "current"
    )

occamExtAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 2, 0, 3)
)
occamExtAlarmCleared.setObjects(
    ("OCCAM-SENSOR-MIB", "occamExtAlarmDescription")
)
if mibBuilder.loadTexts:
    occamExtAlarmCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

sensorMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 2, 3, 2, 1)
)
sensorMIBCompliance.setObjects(
      *(("OCCAM-SENSOR-MIB", "sensorGroup"),
        ("OCCAM-SENSOR-MIB", "sensorThresholdGroup"))
)
if mibBuilder.loadTexts:
    sensorMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OCCAM-SENSOR-MIB",
    **{"SensorThresholdRelation": SensorThresholdRelation,
       "SensorStatus": SensorStatus,
       "SensorValue": SensorValue,
       "SensorDataType": SensorDataType,
       "SensorThresholdSeverity": SensorThresholdSeverity,
       "SensorDataScale": SensorDataScale,
       "sensorMIB": sensorMIB,
       "sensorMIBObjects": sensorMIBObjects,
       "sensorValues": sensorValues,
       "sensorTable": sensorTable,
       "sensorEntry": sensorEntry,
       "sensorIndex": sensorIndex,
       "sensorName": sensorName,
       "sensorType": sensorType,
       "sensorValue": sensorValue,
       "sensorScale": sensorScale,
       "sensorTimeStamp": sensorTimeStamp,
       "sensorEventType": sensorEventType,
       "occamExtAlarmDescription": occamExtAlarmDescription,
       "sensorThresholds": sensorThresholds,
       "sensorThresholdTable": sensorThresholdTable,
       "sensorThresholdEntry": sensorThresholdEntry,
       "sensorThresholdIndex": sensorThresholdIndex,
       "sensorThresholdSeverity": sensorThresholdSeverity,
       "sensorThresholdRelation": sensorThresholdRelation,
       "sensorThresholdValue": sensorThresholdValue,
       "sensorThresholdNotificationEnable": sensorThresholdNotificationEnable,
       "sensorMIBTraps": sensorMIBTraps,
       "sensorMIBTrapsSubID": sensorMIBTrapsSubID,
       "sensorThresholdNotification": sensorThresholdNotification,
       "occamExtAlarmRaised": occamExtAlarmRaised,
       "occamExtAlarmCleared": occamExtAlarmCleared,
       "sensorMIBConformance": sensorMIBConformance,
       "sensorMIBGroups": sensorMIBGroups,
       "sensorMIBObjectGroups": sensorMIBObjectGroups,
       "sensorGroup": sensorGroup,
       "sensorThresholdGroup": sensorThresholdGroup,
       "sensorMIBEventGroups": sensorMIBEventGroups,
       "sensorMIBCompliances": sensorMIBCompliances,
       "sensorMIBCompliance": sensorMIBCompliance}
)
