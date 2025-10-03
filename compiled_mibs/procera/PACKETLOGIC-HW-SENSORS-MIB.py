# SNMP MIB module (PACKETLOGIC-HW-SENSORS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\procera\PACKETLOGIC-HW-SENSORS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:21:09 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(hw,) = mibBuilder.importSymbols(
    "PACKETLOGIC-HW-MIB",
    "hw")

(packetlogic2,) = mibBuilder.importSymbols(
    "PACKETLOGIC-MIB",
    "packetlogic2")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sensors = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 3)
)
if mibBuilder.loadTexts:
    sensors.setRevisions(
        ("2019-09-12 15:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TempSensors_Object = MibTable
tempSensors = _TempSensors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1)
)
if mibBuilder.loadTexts:
    tempSensors.setStatus("current")
_TempSensorEntry_Object = MibTableRow
tempSensorEntry = _TempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1, 1)
)
tempSensorEntry.setIndexNames(
    (0, "PACKETLOGIC-HW-SENSORS-MIB", "tempSensorEntryIndex"),
)
if mibBuilder.loadTexts:
    tempSensorEntry.setStatus("current")
_TempSensorId_Type = DisplayString
_TempSensorId_Object = MibTableColumn
tempSensorId = _TempSensorId_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1, 1, 1),
    _TempSensorId_Type()
)
tempSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorId.setStatus("current")
_TempSensorReading_Type = Unsigned32
_TempSensorReading_Object = MibTableColumn
tempSensorReading = _TempSensorReading_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1, 1, 2),
    _TempSensorReading_Type()
)
tempSensorReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorReading.setStatus("current")
_TempSensorStatus_Type = DisplayString
_TempSensorStatus_Object = MibTableColumn
tempSensorStatus = _TempSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1, 1, 3),
    _TempSensorStatus_Type()
)
tempSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorStatus.setStatus("current")
_TempSensorUnit_Type = DisplayString
_TempSensorUnit_Object = MibTableColumn
tempSensorUnit = _TempSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1, 1, 4),
    _TempSensorUnit_Type()
)
tempSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorUnit.setStatus("current")


class _TempSensorEntryIndex_Type(Integer32):
    """Custom type tempSensorEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TempSensorEntryIndex_Type.__name__ = "Integer32"
_TempSensorEntryIndex_Object = MibTableColumn
tempSensorEntryIndex = _TempSensorEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1, 1, 999),
    _TempSensorEntryIndex_Type()
)
tempSensorEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tempSensorEntryIndex.setStatus("current")
_FanSensors_Object = MibTable
fanSensors = _FanSensors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4)
)
if mibBuilder.loadTexts:
    fanSensors.setStatus("current")
_FanSensorEntry_Object = MibTableRow
fanSensorEntry = _FanSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4, 1)
)
fanSensorEntry.setIndexNames(
    (0, "PACKETLOGIC-HW-SENSORS-MIB", "fanSensorEntryIndex"),
)
if mibBuilder.loadTexts:
    fanSensorEntry.setStatus("current")
_FanSensorId_Type = DisplayString
_FanSensorId_Object = MibTableColumn
fanSensorId = _FanSensorId_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4, 1, 1),
    _FanSensorId_Type()
)
fanSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSensorId.setStatus("current")
_FanSensorSpeed_Type = Unsigned32
_FanSensorSpeed_Object = MibTableColumn
fanSensorSpeed = _FanSensorSpeed_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4, 1, 2),
    _FanSensorSpeed_Type()
)
fanSensorSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSensorSpeed.setStatus("current")
_FanSensorStatus_Type = DisplayString
_FanSensorStatus_Object = MibTableColumn
fanSensorStatus = _FanSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4, 1, 3),
    _FanSensorStatus_Type()
)
fanSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSensorStatus.setStatus("current")
_FanSensorUnit_Type = DisplayString
_FanSensorUnit_Object = MibTableColumn
fanSensorUnit = _FanSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4, 1, 4),
    _FanSensorUnit_Type()
)
fanSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSensorUnit.setStatus("current")


class _FanSensorEntryIndex_Type(Integer32):
    """Custom type fanSensorEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FanSensorEntryIndex_Type.__name__ = "Integer32"
_FanSensorEntryIndex_Object = MibTableColumn
fanSensorEntryIndex = _FanSensorEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4, 1, 999),
    _FanSensorEntryIndex_Type()
)
fanSensorEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fanSensorEntryIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETLOGIC-HW-SENSORS-MIB",
    **{"sensors": sensors,
       "tempSensors": tempSensors,
       "tempSensorEntry": tempSensorEntry,
       "tempSensorId": tempSensorId,
       "tempSensorReading": tempSensorReading,
       "tempSensorStatus": tempSensorStatus,
       "tempSensorUnit": tempSensorUnit,
       "tempSensorEntryIndex": tempSensorEntryIndex,
       "fanSensors": fanSensors,
       "fanSensorEntry": fanSensorEntry,
       "fanSensorId": fanSensorId,
       "fanSensorSpeed": fanSensorSpeed,
       "fanSensorStatus": fanSensorStatus,
       "fanSensorUnit": fanSensorUnit,
       "fanSensorEntryIndex": fanSensorEntryIndex}
)
