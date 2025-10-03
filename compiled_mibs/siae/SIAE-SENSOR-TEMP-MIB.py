# SNMP MIB module (SIAE-SENSOR-TEMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-SENSOR-TEMP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:39 2025
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

(AlarmSeverityCode,
 AlarmStatus) = mibBuilder.importSymbols(
    "SIAE-ALARM-MIB",
    "AlarmSeverityCode",
    "AlarmStatus")

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sensorTemp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77)
)
if mibBuilder.loadTexts:
    sensorTemp.setRevisions(
        ("2016-05-03 00:00",
         "2014-03-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SensorTempMibVersion_Type = Integer32
_SensorTempMibVersion_Object = MibScalar
sensorTempMibVersion = _SensorTempMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 1),
    _SensorTempMibVersion_Type()
)
sensorTempMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempMibVersion.setStatus("current")
_SensorTempTable_Object = MibTable
sensorTempTable = _SensorTempTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2)
)
if mibBuilder.loadTexts:
    sensorTempTable.setStatus("current")
_SensorTempEntry_Object = MibTableRow
sensorTempEntry = _SensorTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1)
)
sensorTempEntry.setIndexNames(
    (0, "SIAE-SENSOR-TEMP-MIB", "sensorTempIndex"),
)
if mibBuilder.loadTexts:
    sensorTempEntry.setStatus("current")
_SensorTempIndex_Type = Integer32
_SensorTempIndex_Object = MibTableColumn
sensorTempIndex = _SensorTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1, 1),
    _SensorTempIndex_Type()
)
sensorTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempIndex.setStatus("current")
_SensorTempValue_Type = Integer32
_SensorTempValue_Object = MibTableColumn
sensorTempValue = _SensorTempValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1, 2),
    _SensorTempValue_Type()
)
sensorTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempValue.setStatus("current")
_SensorTempThreshold1_Type = Integer32
_SensorTempThreshold1_Object = MibTableColumn
sensorTempThreshold1 = _SensorTempThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1, 3),
    _SensorTempThreshold1_Type()
)
sensorTempThreshold1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempThreshold1.setStatus("current")
_SensorTempThreshold2_Type = Integer32
_SensorTempThreshold2_Object = MibTableColumn
sensorTempThreshold2 = _SensorTempThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1, 4),
    _SensorTempThreshold2_Type()
)
sensorTempThreshold2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempThreshold2.setStatus("current")
_SensorTempHysteresis1_Type = Integer32
_SensorTempHysteresis1_Object = MibTableColumn
sensorTempHysteresis1 = _SensorTempHysteresis1_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1, 5),
    _SensorTempHysteresis1_Type()
)
sensorTempHysteresis1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempHysteresis1.setStatus("current")
_SensorTempHysteresis2_Type = Integer32
_SensorTempHysteresis2_Object = MibTableColumn
sensorTempHysteresis2 = _SensorTempHysteresis2_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1, 6),
    _SensorTempHysteresis2_Type()
)
sensorTempHysteresis2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempHysteresis2.setStatus("current")


class _SensorTempStatus1_Type(Integer32):
    """Custom type sensorTempStatus1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("alarmed", 2),
          ("hysteresis", 3))
    )


_SensorTempStatus1_Type.__name__ = "Integer32"
_SensorTempStatus1_Object = MibTableColumn
sensorTempStatus1 = _SensorTempStatus1_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1, 7),
    _SensorTempStatus1_Type()
)
sensorTempStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempStatus1.setStatus("current")


class _SensorTempStatus2_Type(Integer32):
    """Custom type sensorTempStatus2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("alarmed", 2),
          ("hysteresis", 3))
    )


_SensorTempStatus2_Type.__name__ = "Integer32"
_SensorTempStatus2_Object = MibTableColumn
sensorTempStatus2 = _SensorTempStatus2_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1, 8),
    _SensorTempStatus2_Type()
)
sensorTempStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempStatus2.setStatus("current")


class _SensorTempLabel_Type(DisplayString):
    """Custom type sensorTempLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SensorTempLabel_Type.__name__ = "DisplayString"
_SensorTempLabel_Object = MibTableColumn
sensorTempLabel = _SensorTempLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1, 9),
    _SensorTempLabel_Type()
)
sensorTempLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempLabel.setStatus("current")
_SensorTempAlarmThreshold1_Type = AlarmStatus
_SensorTempAlarmThreshold1_Object = MibScalar
sensorTempAlarmThreshold1 = _SensorTempAlarmThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 3),
    _SensorTempAlarmThreshold1_Type()
)
sensorTempAlarmThreshold1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempAlarmThreshold1.setStatus("current")
_SensorTempAlarmThreshold2_Type = AlarmStatus
_SensorTempAlarmThreshold2_Object = MibScalar
sensorTempAlarmThreshold2 = _SensorTempAlarmThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 4),
    _SensorTempAlarmThreshold2_Type()
)
sensorTempAlarmThreshold2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempAlarmThreshold2.setStatus("current")


class _SensorTempAlarmThreshold1Severity_Type(AlarmSeverityCode):
    """Custom type sensorTempAlarmThreshold1Severity based on AlarmSeverityCode"""
    defaultValue = 3


_SensorTempAlarmThreshold1Severity_Type.__name__ = "AlarmSeverityCode"
_SensorTempAlarmThreshold1Severity_Object = MibScalar
sensorTempAlarmThreshold1Severity = _SensorTempAlarmThreshold1Severity_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 5),
    _SensorTempAlarmThreshold1Severity_Type()
)
sensorTempAlarmThreshold1Severity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorTempAlarmThreshold1Severity.setStatus("current")


class _SensorTempAlarmThreshold2Severity_Type(AlarmSeverityCode):
    """Custom type sensorTempAlarmThreshold2Severity based on AlarmSeverityCode"""
    defaultValue = 6


_SensorTempAlarmThreshold2Severity_Type.__name__ = "AlarmSeverityCode"
_SensorTempAlarmThreshold2Severity_Object = MibScalar
sensorTempAlarmThreshold2Severity = _SensorTempAlarmThreshold2Severity_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 6),
    _SensorTempAlarmThreshold2Severity_Type()
)
sensorTempAlarmThreshold2Severity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorTempAlarmThreshold2Severity.setStatus("current")
_SensorTempMonitorTable_Object = MibTable
sensorTempMonitorTable = _SensorTempMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 7)
)
if mibBuilder.loadTexts:
    sensorTempMonitorTable.setStatus("current")
_SensorTempMonitorEntry_Object = MibTableRow
sensorTempMonitorEntry = _SensorTempMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 7, 1)
)
sensorTempMonitorEntry.setIndexNames(
    (0, "SIAE-SENSOR-TEMP-MIB", "sensorTempIndex"),
)
if mibBuilder.loadTexts:
    sensorTempMonitorEntry.setStatus("current")


class _SensorTempMonitorAdminStatus_Type(Integer32):
    """Custom type sensorTempMonitorAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SensorTempMonitorAdminStatus_Type.__name__ = "Integer32"
_SensorTempMonitorAdminStatus_Object = MibTableColumn
sensorTempMonitorAdminStatus = _SensorTempMonitorAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 7, 1, 1),
    _SensorTempMonitorAdminStatus_Type()
)
sensorTempMonitorAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorTempMonitorAdminStatus.setStatus("current")


class _SensorTempMonitorOperStatus_Type(Integer32):
    """Custom type sensorTempMonitorOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SensorTempMonitorOperStatus_Type.__name__ = "Integer32"
_SensorTempMonitorOperStatus_Object = MibTableColumn
sensorTempMonitorOperStatus = _SensorTempMonitorOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 7, 1, 2),
    _SensorTempMonitorOperStatus_Type()
)
sensorTempMonitorOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempMonitorOperStatus.setStatus("current")
_SensorTempMonitorMinTemp_Type = Integer32
_SensorTempMonitorMinTemp_Object = MibTableColumn
sensorTempMonitorMinTemp = _SensorTempMonitorMinTemp_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 7, 1, 3),
    _SensorTempMonitorMinTemp_Type()
)
sensorTempMonitorMinTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempMonitorMinTemp.setStatus("current")
_SensorTempMonitorMaxTemp_Type = Integer32
_SensorTempMonitorMaxTemp_Object = MibTableColumn
sensorTempMonitorMaxTemp = _SensorTempMonitorMaxTemp_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 7, 1, 4),
    _SensorTempMonitorMaxTemp_Type()
)
sensorTempMonitorMaxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempMonitorMaxTemp.setStatus("current")
_SensorTempMonitorAverageTemp_Type = Integer32
_SensorTempMonitorAverageTemp_Object = MibTableColumn
sensorTempMonitorAverageTemp = _SensorTempMonitorAverageTemp_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 7, 1, 5),
    _SensorTempMonitorAverageTemp_Type()
)
sensorTempMonitorAverageTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempMonitorAverageTemp.setStatus("current")


class _SensorTempMonitorSystemControl_Type(Integer32):
    """Custom type sensorTempMonitorSystemControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_SensorTempMonitorSystemControl_Type.__name__ = "Integer32"
_SensorTempMonitorSystemControl_Object = MibScalar
sensorTempMonitorSystemControl = _SensorTempMonitorSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 77, 8),
    _SensorTempMonitorSystemControl_Type()
)
sensorTempMonitorSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorTempMonitorSystemControl.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-SENSOR-TEMP-MIB",
    **{"sensorTemp": sensorTemp,
       "sensorTempMibVersion": sensorTempMibVersion,
       "sensorTempTable": sensorTempTable,
       "sensorTempEntry": sensorTempEntry,
       "sensorTempIndex": sensorTempIndex,
       "sensorTempValue": sensorTempValue,
       "sensorTempThreshold1": sensorTempThreshold1,
       "sensorTempThreshold2": sensorTempThreshold2,
       "sensorTempHysteresis1": sensorTempHysteresis1,
       "sensorTempHysteresis2": sensorTempHysteresis2,
       "sensorTempStatus1": sensorTempStatus1,
       "sensorTempStatus2": sensorTempStatus2,
       "sensorTempLabel": sensorTempLabel,
       "sensorTempAlarmThreshold1": sensorTempAlarmThreshold1,
       "sensorTempAlarmThreshold2": sensorTempAlarmThreshold2,
       "sensorTempAlarmThreshold1Severity": sensorTempAlarmThreshold1Severity,
       "sensorTempAlarmThreshold2Severity": sensorTempAlarmThreshold2Severity,
       "sensorTempMonitorTable": sensorTempMonitorTable,
       "sensorTempMonitorEntry": sensorTempMonitorEntry,
       "sensorTempMonitorAdminStatus": sensorTempMonitorAdminStatus,
       "sensorTempMonitorOperStatus": sensorTempMonitorOperStatus,
       "sensorTempMonitorMinTemp": sensorTempMonitorMinTemp,
       "sensorTempMonitorMaxTemp": sensorTempMonitorMaxTemp,
       "sensorTempMonitorAverageTemp": sensorTempMonitorAverageTemp,
       "sensorTempMonitorSystemControl": sensorTempMonitorSystemControl}
)
