# SNMP MIB module (ENTITY-SENSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ENTITY-SENSOR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:22 2025
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

(entPhysicalIndex,
 entityPhysicalGroup) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entityPhysicalGroup")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

entitySensorMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 99)
)
if mibBuilder.loadTexts:
    entitySensorMIB.setRevisions(
        ("2002-12-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EntitySensorDataType(TextualConvention, Integer32):
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
          ("unknown", 2),
          ("voltsAC", 3),
          ("voltsDC", 4),
          ("amperes", 5),
          ("watts", 6),
          ("hertz", 7),
          ("celsius", 8),
          ("percentRH", 9),
          ("rpm", 10),
          ("cmm", 11),
          ("truthvalue", 12))
    )



class EntitySensorDataScale(TextualConvention, Integer32):
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("yocto", 1),
          ("zepto", 2),
          ("atto", 3),
          ("femto", 4),
          ("pico", 5),
          ("nano", 6),
          ("micro", 7),
          ("milli", 8),
          ("units", 9),
          ("kilo", 10),
          ("mega", 11),
          ("giga", 12),
          ("tera", 13),
          ("exa", 14),
          ("peta", 15),
          ("zetta", 16),
          ("yotta", 17))
    )



class EntitySensorPrecision(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-8, 9),
    )



class EntitySensorValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )



class EntitySensorStatus(TextualConvention, Integer32):
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



# MIB Managed Objects in the order of their OIDs

_EntitySensorObjects_ObjectIdentity = ObjectIdentity
entitySensorObjects = _EntitySensorObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 99, 1)
)
_EntPhySensorTable_Object = MibTable
entPhySensorTable = _EntPhySensorTable_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1)
)
if mibBuilder.loadTexts:
    entPhySensorTable.setStatus("current")
_EntPhySensorEntry_Object = MibTableRow
entPhySensorEntry = _EntPhySensorEntry_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1)
)
entPhySensorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    entPhySensorEntry.setStatus("current")
_EntPhySensorType_Type = EntitySensorDataType
_EntPhySensorType_Object = MibTableColumn
entPhySensorType = _EntPhySensorType_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 1),
    _EntPhySensorType_Type()
)
entPhySensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorType.setStatus("current")
_EntPhySensorScale_Type = EntitySensorDataScale
_EntPhySensorScale_Object = MibTableColumn
entPhySensorScale = _EntPhySensorScale_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 2),
    _EntPhySensorScale_Type()
)
entPhySensorScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorScale.setStatus("current")
_EntPhySensorPrecision_Type = EntitySensorPrecision
_EntPhySensorPrecision_Object = MibTableColumn
entPhySensorPrecision = _EntPhySensorPrecision_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 3),
    _EntPhySensorPrecision_Type()
)
entPhySensorPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorPrecision.setStatus("current")
_EntPhySensorValue_Type = EntitySensorValue
_EntPhySensorValue_Object = MibTableColumn
entPhySensorValue = _EntPhySensorValue_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 4),
    _EntPhySensorValue_Type()
)
entPhySensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorValue.setStatus("current")
_EntPhySensorOperStatus_Type = EntitySensorStatus
_EntPhySensorOperStatus_Object = MibTableColumn
entPhySensorOperStatus = _EntPhySensorOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 5),
    _EntPhySensorOperStatus_Type()
)
entPhySensorOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorOperStatus.setStatus("current")
_EntPhySensorUnitsDisplay_Type = SnmpAdminString
_EntPhySensorUnitsDisplay_Object = MibTableColumn
entPhySensorUnitsDisplay = _EntPhySensorUnitsDisplay_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 6),
    _EntPhySensorUnitsDisplay_Type()
)
entPhySensorUnitsDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorUnitsDisplay.setStatus("current")
_EntPhySensorValueTimeStamp_Type = TimeStamp
_EntPhySensorValueTimeStamp_Object = MibTableColumn
entPhySensorValueTimeStamp = _EntPhySensorValueTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 7),
    _EntPhySensorValueTimeStamp_Type()
)
entPhySensorValueTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorValueTimeStamp.setStatus("current")
_EntPhySensorValueUpdateRate_Type = Unsigned32
_EntPhySensorValueUpdateRate_Object = MibTableColumn
entPhySensorValueUpdateRate = _EntPhySensorValueUpdateRate_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 8),
    _EntPhySensorValueUpdateRate_Type()
)
entPhySensorValueUpdateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorValueUpdateRate.setStatus("current")
if mibBuilder.loadTexts:
    entPhySensorValueUpdateRate.setUnits("milliseconds")
_EntitySensorConformance_ObjectIdentity = ObjectIdentity
entitySensorConformance = _EntitySensorConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 99, 3)
)
_EntitySensorCompliances_ObjectIdentity = ObjectIdentity
entitySensorCompliances = _EntitySensorCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 99, 3, 1)
)
_EntitySensorGroups_ObjectIdentity = ObjectIdentity
entitySensorGroups = _EntitySensorGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 99, 3, 2)
)

# Managed Objects groups

entitySensorValueGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 99, 3, 2, 1)
)
entitySensorValueGroup.setObjects(
      *(("ENTITY-SENSOR-MIB", "entPhySensorType"),
        ("ENTITY-SENSOR-MIB", "entPhySensorScale"),
        ("ENTITY-SENSOR-MIB", "entPhySensorPrecision"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("ENTITY-SENSOR-MIB", "entPhySensorOperStatus"),
        ("ENTITY-SENSOR-MIB", "entPhySensorUnitsDisplay"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValueTimeStamp"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValueUpdateRate"))
)
if mibBuilder.loadTexts:
    entitySensorValueGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

entitySensorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 99, 3, 1, 1)
)
entitySensorCompliance.setObjects(
      *(("ENTITY-SENSOR-MIB", "entitySensorValueGroup"),
        ("ENTITY-MIB", "entityPhysicalGroup"))
)
if mibBuilder.loadTexts:
    entitySensorCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTITY-SENSOR-MIB",
    **{"EntitySensorDataType": EntitySensorDataType,
       "EntitySensorDataScale": EntitySensorDataScale,
       "EntitySensorPrecision": EntitySensorPrecision,
       "EntitySensorValue": EntitySensorValue,
       "EntitySensorStatus": EntitySensorStatus,
       "entitySensorMIB": entitySensorMIB,
       "entitySensorObjects": entitySensorObjects,
       "entPhySensorTable": entPhySensorTable,
       "entPhySensorEntry": entPhySensorEntry,
       "entPhySensorType": entPhySensorType,
       "entPhySensorScale": entPhySensorScale,
       "entPhySensorPrecision": entPhySensorPrecision,
       "entPhySensorValue": entPhySensorValue,
       "entPhySensorOperStatus": entPhySensorOperStatus,
       "entPhySensorUnitsDisplay": entPhySensorUnitsDisplay,
       "entPhySensorValueTimeStamp": entPhySensorValueTimeStamp,
       "entPhySensorValueUpdateRate": entPhySensorValueUpdateRate,
       "entitySensorConformance": entitySensorConformance,
       "entitySensorCompliances": entitySensorCompliances,
       "entitySensorCompliance": entitySensorCompliance,
       "entitySensorGroups": entitySensorGroups,
       "entitySensorValueGroup": entitySensorValueGroup}
)
