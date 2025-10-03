# SNMP MIB module (OPENBSD-SENSORS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\openbsd\OPENBSD-SENSORS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:20 2025
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

(openBSD,) = mibBuilder.importSymbols(
    "OPENBSD-BASE-MIB",
    "openBSD")

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

sensorsMIBObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 2)
)
if mibBuilder.loadTexts:
    sensorsMIBObjects.setRevisions(
        ("2018-12-10 00:00",
         "2012-09-20 00:00",
         "2012-01-31 00:00",
         "2008-12-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sensors_ObjectIdentity = ObjectIdentity
sensors = _Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1)
)
_SensorNumber_Type = Integer32
_SensorNumber_Object = MibScalar
sensorNumber = _SensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 1),
    _SensorNumber_Type()
)
sensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorNumber.setStatus("current")
_SensorTable_Object = MibTable
sensorTable = _SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 2)
)
if mibBuilder.loadTexts:
    sensorTable.setStatus("current")
_SensorEntry_Object = MibTableRow
sensorEntry = _SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1)
)
sensorEntry.setIndexNames(
    (0, "OPENBSD-SENSORS-MIB", "sensorIndex"),
)
if mibBuilder.loadTexts:
    sensorEntry.setStatus("current")


class _SensorIndex_Type(Integer32):
    """Custom type sensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SensorIndex_Type.__name__ = "Integer32"
_SensorIndex_Object = MibTableColumn
sensorIndex = _SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 1),
    _SensorIndex_Type()
)
sensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorIndex.setStatus("current")
_SensorDescr_Type = OctetString
_SensorDescr_Object = MibTableColumn
sensorDescr = _SensorDescr_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 2),
    _SensorDescr_Type()
)
sensorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorDescr.setStatus("current")


class _SensorType_Type(Integer32):
    """Custom type sensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("temperature", 0),
          ("fan", 1),
          ("voltsdc", 2),
          ("voltsac", 3),
          ("resistance", 4),
          ("power", 5),
          ("current", 6),
          ("watthour", 7),
          ("amphour", 8),
          ("indicator", 9),
          ("raw", 10),
          ("percent", 11),
          ("illuminance", 12),
          ("drive", 13),
          ("timedelta", 14),
          ("humidity", 15),
          ("freq", 16),
          ("angle", 17),
          ("distance", 18),
          ("pressure", 19),
          ("accel", 20),
          ("velocity", 21))
    )


_SensorType_Type.__name__ = "Integer32"
_SensorType_Object = MibTableColumn
sensorType = _SensorType_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 3),
    _SensorType_Type()
)
sensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorType.setStatus("current")
_SensorDevice_Type = OctetString
_SensorDevice_Object = MibTableColumn
sensorDevice = _SensorDevice_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 4),
    _SensorDevice_Type()
)
sensorDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorDevice.setStatus("current")
_SensorValue_Type = OctetString
_SensorValue_Object = MibTableColumn
sensorValue = _SensorValue_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 5),
    _SensorValue_Type()
)
sensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorValue.setStatus("current")
_SensorUnits_Type = OctetString
_SensorUnits_Object = MibTableColumn
sensorUnits = _SensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 6),
    _SensorUnits_Type()
)
sensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorUnits.setStatus("current")


class _SensorStatus_Type(Integer32):
    """Custom type sensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("ok", 1),
          ("warn", 2),
          ("critical", 3),
          ("unknown", 4))
    )


_SensorStatus_Type.__name__ = "Integer32"
_SensorStatus_Object = MibTableColumn
sensorStatus = _SensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 7),
    _SensorStatus_Type()
)
sensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPENBSD-SENSORS-MIB",
    **{"sensorsMIBObjects": sensorsMIBObjects,
       "sensors": sensors,
       "sensorNumber": sensorNumber,
       "sensorTable": sensorTable,
       "sensorEntry": sensorEntry,
       "sensorIndex": sensorIndex,
       "sensorDescr": sensorDescr,
       "sensorType": sensorType,
       "sensorDevice": sensorDevice,
       "sensorValue": sensorValue,
       "sensorUnits": sensorUnits,
       "sensorStatus": sensorStatus}
)
