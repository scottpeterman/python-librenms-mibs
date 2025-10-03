# SNMP MIB module (CISCOSB-SENSORENTMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-SENSORENTMIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:29:48 2025
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

(rlEnv,) = mibBuilder.importSymbols(
    "CISCOSB-HWENVIROMENT",
    "rlEnv")

(entPhysicalIndex,
 entityPhysicalGroup) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entityPhysicalGroup")

(EntitySensorValue,
 entPhySensorEntry) = mibBuilder.importSymbols(
    "ENTITY-SENSOR-MIB",
    "EntitySensorValue",
    "entPhySensorEntry")

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

rlSensor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 4)
)
if mibBuilder.loadTexts:
    rlSensor.setRevisions(
        ("2003-09-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlEntPhySensorTable_Object = MibTable
rlEntPhySensorTable = _RlEntPhySensorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 3)
)
if mibBuilder.loadTexts:
    rlEntPhySensorTable.setStatus("current")
_RlEntPhySensorEntry_Object = MibTableRow
rlEntPhySensorEntry = _RlEntPhySensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 3, 1)
)
if mibBuilder.loadTexts:
    rlEntPhySensorEntry.setStatus("current")
_RlEnvPhySensorMinValue_Type = EntitySensorValue
_RlEnvPhySensorMinValue_Object = MibTableColumn
rlEnvPhySensorMinValue = _RlEnvPhySensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 3, 1, 1),
    _RlEnvPhySensorMinValue_Type()
)
rlEnvPhySensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEnvPhySensorMinValue.setStatus("current")
_RlEnvPhySensorMaxValue_Type = EntitySensorValue
_RlEnvPhySensorMaxValue_Object = MibTableColumn
rlEnvPhySensorMaxValue = _RlEnvPhySensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 3, 1, 2),
    _RlEnvPhySensorMaxValue_Type()
)
rlEnvPhySensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEnvPhySensorMaxValue.setStatus("current")
_RlEnvPhySensorTestValue_Type = EntitySensorValue
_RlEnvPhySensorTestValue_Object = MibTableColumn
rlEnvPhySensorTestValue = _RlEnvPhySensorTestValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 3, 1, 3),
    _RlEnvPhySensorTestValue_Type()
)
rlEnvPhySensorTestValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEnvPhySensorTestValue.setStatus("current")
_RlEnvPhySensorLocation_Type = SnmpAdminString
_RlEnvPhySensorLocation_Object = MibTableColumn
rlEnvPhySensorLocation = _RlEnvPhySensorLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 3, 1, 4),
    _RlEnvPhySensorLocation_Type()
)
rlEnvPhySensorLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEnvPhySensorLocation.setStatus("current")
entPhySensorEntry.registerAugmentions(
    ("CISCOSB-SENSORENTMIB",
     "rlEntPhySensorEntry")
)
rlEntPhySensorEntry.setIndexNames(*entPhySensorEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-SENSORENTMIB",
    **{"rlEntPhySensorTable": rlEntPhySensorTable,
       "rlEntPhySensorEntry": rlEntPhySensorEntry,
       "rlEnvPhySensorMinValue": rlEnvPhySensorMinValue,
       "rlEnvPhySensorMaxValue": rlEnvPhySensorMaxValue,
       "rlEnvPhySensorTestValue": rlEnvPhySensorTestValue,
       "rlEnvPhySensorLocation": rlEnvPhySensorLocation,
       "rlSensor": rlSensor}
)
