# SNMP MIB module (RAISECOM-OPTICAL-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\raisecom\RAISECOM-OPTICAL-MONITOR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:22:58 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

raisecomOpticalMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9)
)
if mibBuilder.loadTexts:
    raisecomOpticalMonitorMIB.setRevisions(
        ("2006-06-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OpticalParameterType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("temperature", 1),
          ("supplyVoltage", 2),
          ("biasCurrent", 3),
          ("txOutputPower", 4),
          ("receivedPower", 5))
    )



class OpticalParameterValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000, 65535),
    )



class OpticalPMPeriod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMin", 1),
          ("twentyFourHour", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RaisecomOpticalMonitorMIBObjects_ObjectIdentity = ObjectIdentity
raisecomOpticalMonitorMIBObjects = _RaisecomOpticalMonitorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1)
)
_RaisecomOpticalMonGroup_ObjectIdentity = ObjectIdentity
raisecomOpticalMonGroup = _RaisecomOpticalMonGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 1)
)
_RaisecomOpticalMonTable_Object = MibTable
raisecomOpticalMonTable = _RaisecomOpticalMonTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    raisecomOpticalMonTable.setStatus("current")
_RaisecomOpticalMonEntry_Object = MibTableRow
raisecomOpticalMonEntry = _RaisecomOpticalMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 1, 1, 1)
)
raisecomOpticalMonEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalMonParameterType"),
)
if mibBuilder.loadTexts:
    raisecomOpticalMonEntry.setStatus("current")
_RaisecomOpticalMonParameterType_Type = OpticalParameterType
_RaisecomOpticalMonParameterType_Object = MibTableColumn
raisecomOpticalMonParameterType = _RaisecomOpticalMonParameterType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 1, 1, 1, 1),
    _RaisecomOpticalMonParameterType_Type()
)
raisecomOpticalMonParameterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomOpticalMonParameterType.setStatus("current")
_RaisecomOpticalParameterValue_Type = OpticalParameterValue
_RaisecomOpticalParameterValue_Object = MibTableColumn
raisecomOpticalParameterValue = _RaisecomOpticalParameterValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 1, 1, 1, 2),
    _RaisecomOpticalParameterValue_Type()
)
raisecomOpticalParameterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOpticalParameterValue.setStatus("current")
_RaisecomOpticalParamHighAlarmThresh_Type = OpticalParameterValue
_RaisecomOpticalParamHighAlarmThresh_Object = MibTableColumn
raisecomOpticalParamHighAlarmThresh = _RaisecomOpticalParamHighAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 1, 1, 1, 3),
    _RaisecomOpticalParamHighAlarmThresh_Type()
)
raisecomOpticalParamHighAlarmThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOpticalParamHighAlarmThresh.setStatus("current")
_RaisecomOpticalParamHighWarningThresh_Type = OpticalParameterValue
_RaisecomOpticalParamHighWarningThresh_Object = MibTableColumn
raisecomOpticalParamHighWarningThresh = _RaisecomOpticalParamHighWarningThresh_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 1, 1, 1, 4),
    _RaisecomOpticalParamHighWarningThresh_Type()
)
raisecomOpticalParamHighWarningThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOpticalParamHighWarningThresh.setStatus("current")
_RaisecomOpticalParamLowAlarmThresh_Type = OpticalParameterValue
_RaisecomOpticalParamLowAlarmThresh_Object = MibTableColumn
raisecomOpticalParamLowAlarmThresh = _RaisecomOpticalParamLowAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 1, 1, 1, 5),
    _RaisecomOpticalParamLowAlarmThresh_Type()
)
raisecomOpticalParamLowAlarmThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOpticalParamLowAlarmThresh.setStatus("current")
_RaisecomOpticalParamLowWarningThresh_Type = OpticalParameterValue
_RaisecomOpticalParamLowWarningThresh_Object = MibTableColumn
raisecomOpticalParamLowWarningThresh = _RaisecomOpticalParamLowWarningThresh_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 1, 1, 1, 6),
    _RaisecomOpticalParamLowWarningThresh_Type()
)
raisecomOpticalParamLowWarningThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOpticalParamLowWarningThresh.setStatus("current")


class _RaisecomOpticalParamAlarmStatus_Type(Integer32):
    """Custom type raisecomOpticalParamAlarmStatus based on Integer32"""
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
        *(("none", 0),
          ("high-alarm-threshold", 1),
          ("high-warning-threshold", 2),
          ("low-alarm-threshold", 3),
          ("low-warning-threshold", 4))
    )


_RaisecomOpticalParamAlarmStatus_Type.__name__ = "Integer32"
_RaisecomOpticalParamAlarmStatus_Object = MibTableColumn
raisecomOpticalParamAlarmStatus = _RaisecomOpticalParamAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 1, 1, 1, 7),
    _RaisecomOpticalParamAlarmStatus_Type()
)
raisecomOpticalParamAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOpticalParamAlarmStatus.setStatus("current")
_RaisecomOpticalParamAlarmLastValue_Type = OpticalParameterValue
_RaisecomOpticalParamAlarmLastValue_Object = MibTableColumn
raisecomOpticalParamAlarmLastValue = _RaisecomOpticalParamAlarmLastValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 1, 1, 1, 8),
    _RaisecomOpticalParamAlarmLastValue_Type()
)
raisecomOpticalParamAlarmLastValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOpticalParamAlarmLastValue.setStatus("current")
_RaisecomOpticalParamAlarmLastChange_Type = TimeTicks
_RaisecomOpticalParamAlarmLastChange_Object = MibTableColumn
raisecomOpticalParamAlarmLastChange = _RaisecomOpticalParamAlarmLastChange_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 1, 1, 1, 9),
    _RaisecomOpticalParamAlarmLastChange_Type()
)
raisecomOpticalParamAlarmLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOpticalParamAlarmLastChange.setStatus("current")


class _RaisecomOpticalMon15MinValidIntervals_Type(Unsigned32):
    """Custom type raisecomOpticalMon15MinValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_RaisecomOpticalMon15MinValidIntervals_Type.__name__ = "Unsigned32"
_RaisecomOpticalMon15MinValidIntervals_Object = MibTableColumn
raisecomOpticalMon15MinValidIntervals = _RaisecomOpticalMon15MinValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 1, 1, 1, 10),
    _RaisecomOpticalMon15MinValidIntervals_Type()
)
raisecomOpticalMon15MinValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOpticalMon15MinValidIntervals.setStatus("current")


class _RaisecomOpticalMon24HrValidIntervals_Type(Unsigned32):
    """Custom type raisecomOpticalMon24HrValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RaisecomOpticalMon24HrValidIntervals_Type.__name__ = "Unsigned32"
_RaisecomOpticalMon24HrValidIntervals_Object = MibTableColumn
raisecomOpticalMon24HrValidIntervals = _RaisecomOpticalMon24HrValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 1, 1, 1, 11),
    _RaisecomOpticalMon24HrValidIntervals_Type()
)
raisecomOpticalMon24HrValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOpticalMon24HrValidIntervals.setStatus("current")


class _RaisecomOpticalMonValidStatus_Type(Integer32):
    """Custom type raisecomOpticalMonValidStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_RaisecomOpticalMonValidStatus_Type.__name__ = "Integer32"
_RaisecomOpticalMonValidStatus_Object = MibTableColumn
raisecomOpticalMonValidStatus = _RaisecomOpticalMonValidStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 1, 1, 1, 12),
    _RaisecomOpticalMonValidStatus_Type()
)
raisecomOpticalMonValidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOpticalMonValidStatus.setStatus("current")


class _RaisecomOpticalNotifyEnable_Type(EnableVar):
    """Custom type raisecomOpticalNotifyEnable based on EnableVar"""
    defaultValue = 1


_RaisecomOpticalNotifyEnable_Type.__name__ = "EnableVar"
_RaisecomOpticalNotifyEnable_Object = MibScalar
raisecomOpticalNotifyEnable = _RaisecomOpticalNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 1, 2),
    _RaisecomOpticalNotifyEnable_Type()
)
raisecomOpticalNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomOpticalNotifyEnable.setStatus("current")


class _RaisecomOpticalDigitalDiagnoticEnable_Type(EnableVar):
    """Custom type raisecomOpticalDigitalDiagnoticEnable based on EnableVar"""
    defaultValue = 2


_RaisecomOpticalDigitalDiagnoticEnable_Type.__name__ = "EnableVar"
_RaisecomOpticalDigitalDiagnoticEnable_Object = MibScalar
raisecomOpticalDigitalDiagnoticEnable = _RaisecomOpticalDigitalDiagnoticEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 1, 3),
    _RaisecomOpticalDigitalDiagnoticEnable_Type()
)
raisecomOpticalDigitalDiagnoticEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomOpticalDigitalDiagnoticEnable.setStatus("current")
_RaisecomOpticalPMGroup_ObjectIdentity = ObjectIdentity
raisecomOpticalPMGroup = _RaisecomOpticalPMGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 2)
)
_RaisecomOpticalPMCurrentTable_Object = MibTable
raisecomOpticalPMCurrentTable = _RaisecomOpticalPMCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    raisecomOpticalPMCurrentTable.setStatus("current")
_RaisecomOpticalPMCurrentEntry_Object = MibTableRow
raisecomOpticalPMCurrentEntry = _RaisecomOpticalPMCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 2, 1, 1)
)
raisecomOpticalPMCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalPMCurrentPeriod"),
    (0, "RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalPMCurrentParamType"),
)
if mibBuilder.loadTexts:
    raisecomOpticalPMCurrentEntry.setStatus("current")
_RaisecomOpticalPMCurrentPeriod_Type = OpticalPMPeriod
_RaisecomOpticalPMCurrentPeriod_Object = MibTableColumn
raisecomOpticalPMCurrentPeriod = _RaisecomOpticalPMCurrentPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 2, 1, 1, 1),
    _RaisecomOpticalPMCurrentPeriod_Type()
)
raisecomOpticalPMCurrentPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomOpticalPMCurrentPeriod.setStatus("current")
_RaisecomOpticalPMCurrentParamType_Type = OpticalParameterType
_RaisecomOpticalPMCurrentParamType_Object = MibTableColumn
raisecomOpticalPMCurrentParamType = _RaisecomOpticalPMCurrentParamType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 2, 1, 1, 2),
    _RaisecomOpticalPMCurrentParamType_Type()
)
raisecomOpticalPMCurrentParamType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomOpticalPMCurrentParamType.setStatus("current")
_RaisecomOpticalPMCurrentMaxParam_Type = OpticalParameterValue
_RaisecomOpticalPMCurrentMaxParam_Object = MibTableColumn
raisecomOpticalPMCurrentMaxParam = _RaisecomOpticalPMCurrentMaxParam_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 2, 1, 1, 3),
    _RaisecomOpticalPMCurrentMaxParam_Type()
)
raisecomOpticalPMCurrentMaxParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOpticalPMCurrentMaxParam.setStatus("current")
_RaisecomOpticalPMCurrentMinParam_Type = OpticalParameterValue
_RaisecomOpticalPMCurrentMinParam_Object = MibTableColumn
raisecomOpticalPMCurrentMinParam = _RaisecomOpticalPMCurrentMinParam_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 2, 1, 1, 4),
    _RaisecomOpticalPMCurrentMinParam_Type()
)
raisecomOpticalPMCurrentMinParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOpticalPMCurrentMinParam.setStatus("current")
_RaisecomOpticalPMCurrentMeanParam_Type = OpticalParameterValue
_RaisecomOpticalPMCurrentMeanParam_Object = MibTableColumn
raisecomOpticalPMCurrentMeanParam = _RaisecomOpticalPMCurrentMeanParam_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 2, 1, 1, 5),
    _RaisecomOpticalPMCurrentMeanParam_Type()
)
raisecomOpticalPMCurrentMeanParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOpticalPMCurrentMeanParam.setStatus("current")
_RaisecomOpticalPMIntervalTable_Object = MibTable
raisecomOpticalPMIntervalTable = _RaisecomOpticalPMIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    raisecomOpticalPMIntervalTable.setStatus("current")
_RaisecomOpticalPMIntervalEntry_Object = MibTableRow
raisecomOpticalPMIntervalEntry = _RaisecomOpticalPMIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 2, 2, 1)
)
raisecomOpticalPMIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalPMIntervalPeriod"),
    (0, "RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalPMIntervalNumber"),
    (0, "RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalPMIntervalParamType"),
)
if mibBuilder.loadTexts:
    raisecomOpticalPMIntervalEntry.setStatus("current")
_RaisecomOpticalPMIntervalPeriod_Type = OpticalPMPeriod
_RaisecomOpticalPMIntervalPeriod_Object = MibTableColumn
raisecomOpticalPMIntervalPeriod = _RaisecomOpticalPMIntervalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 2, 2, 1, 1),
    _RaisecomOpticalPMIntervalPeriod_Type()
)
raisecomOpticalPMIntervalPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomOpticalPMIntervalPeriod.setStatus("current")


class _RaisecomOpticalPMIntervalNumber_Type(Integer32):
    """Custom type raisecomOpticalPMIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_RaisecomOpticalPMIntervalNumber_Type.__name__ = "Integer32"
_RaisecomOpticalPMIntervalNumber_Object = MibTableColumn
raisecomOpticalPMIntervalNumber = _RaisecomOpticalPMIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 2, 2, 1, 2),
    _RaisecomOpticalPMIntervalNumber_Type()
)
raisecomOpticalPMIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomOpticalPMIntervalNumber.setStatus("current")
_RaisecomOpticalPMIntervalParamType_Type = OpticalParameterType
_RaisecomOpticalPMIntervalParamType_Object = MibTableColumn
raisecomOpticalPMIntervalParamType = _RaisecomOpticalPMIntervalParamType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 2, 2, 1, 3),
    _RaisecomOpticalPMIntervalParamType_Type()
)
raisecomOpticalPMIntervalParamType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomOpticalPMIntervalParamType.setStatus("current")
_RaisecomOpticalPMIntervalMaxParam_Type = OpticalParameterValue
_RaisecomOpticalPMIntervalMaxParam_Object = MibTableColumn
raisecomOpticalPMIntervalMaxParam = _RaisecomOpticalPMIntervalMaxParam_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 2, 2, 1, 4),
    _RaisecomOpticalPMIntervalMaxParam_Type()
)
raisecomOpticalPMIntervalMaxParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOpticalPMIntervalMaxParam.setStatus("current")
_RaisecomOpticalPMIntervalMinParam_Type = OpticalParameterValue
_RaisecomOpticalPMIntervalMinParam_Object = MibTableColumn
raisecomOpticalPMIntervalMinParam = _RaisecomOpticalPMIntervalMinParam_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 2, 2, 1, 5),
    _RaisecomOpticalPMIntervalMinParam_Type()
)
raisecomOpticalPMIntervalMinParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOpticalPMIntervalMinParam.setStatus("current")
_RaisecomOpticalPMIntervalMeanParam_Type = OpticalParameterValue
_RaisecomOpticalPMIntervalMeanParam_Object = MibTableColumn
raisecomOpticalPMIntervalMeanParam = _RaisecomOpticalPMIntervalMeanParam_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 2, 2, 1, 6),
    _RaisecomOpticalPMIntervalMeanParam_Type()
)
raisecomOpticalPMIntervalMeanParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOpticalPMIntervalMeanParam.setStatus("current")
_RaisecomTranceiverInfoTable_Object = MibTable
raisecomTranceiverInfoTable = _RaisecomTranceiverInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 4)
)
if mibBuilder.loadTexts:
    raisecomTranceiverInfoTable.setStatus("current")
_RaisecomTranceiverInfoEntry_Object = MibTableRow
raisecomTranceiverInfoEntry = _RaisecomTranceiverInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 4, 1)
)
raisecomTranceiverInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    raisecomTranceiverInfoEntry.setStatus("current")
_RaisecomTranceiverType_Type = OctetString
_RaisecomTranceiverType_Object = MibTableColumn
raisecomTranceiverType = _RaisecomTranceiverType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 4, 1, 1),
    _RaisecomTranceiverType_Type()
)
raisecomTranceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomTranceiverType.setStatus("current")
_RaisecomTranceiverConnectorType_Type = OctetString
_RaisecomTranceiverConnectorType_Object = MibTableColumn
raisecomTranceiverConnectorType = _RaisecomTranceiverConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 4, 1, 2),
    _RaisecomTranceiverConnectorType_Type()
)
raisecomTranceiverConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomTranceiverConnectorType.setStatus("current")
_RaisecomTranceiverWavelength_Type = Integer32
_RaisecomTranceiverWavelength_Object = MibTableColumn
raisecomTranceiverWavelength = _RaisecomTranceiverWavelength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 4, 1, 3),
    _RaisecomTranceiverWavelength_Type()
)
raisecomTranceiverWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomTranceiverWavelength.setStatus("current")
_RaisecomTranceiverVendorName_Type = OctetString
_RaisecomTranceiverVendorName_Object = MibTableColumn
raisecomTranceiverVendorName = _RaisecomTranceiverVendorName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 4, 1, 4),
    _RaisecomTranceiverVendorName_Type()
)
raisecomTranceiverVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomTranceiverVendorName.setStatus("current")
_RaisecomTranceiverVendorPN_Type = OctetString
_RaisecomTranceiverVendorPN_Object = MibTableColumn
raisecomTranceiverVendorPN = _RaisecomTranceiverVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 4, 1, 5),
    _RaisecomTranceiverVendorPN_Type()
)
raisecomTranceiverVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomTranceiverVendorPN.setStatus("current")
_RaisecomTranceiverVendorSN_Type = OctetString
_RaisecomTranceiverVendorSN_Object = MibTableColumn
raisecomTranceiverVendorSN = _RaisecomTranceiverVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 4, 1, 6),
    _RaisecomTranceiverVendorSN_Type()
)
raisecomTranceiverVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomTranceiverVendorSN.setStatus("current")


class _RaisecomTransceiverFiberType_Type(Integer32):
    """Custom type raisecomTransceiverFiberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("single-mode", 1),
          ("multi-mode", 2),
          ("none", 3))
    )


_RaisecomTransceiverFiberType_Type.__name__ = "Integer32"
_RaisecomTransceiverFiberType_Object = MibTableColumn
raisecomTransceiverFiberType = _RaisecomTransceiverFiberType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 4, 1, 7),
    _RaisecomTransceiverFiberType_Type()
)
raisecomTransceiverFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomTransceiverFiberType.setStatus("current")
_RaisecomTransceiverTransferDistance_Type = Integer32
_RaisecomTransceiverTransferDistance_Object = MibTableColumn
raisecomTransceiverTransferDistance = _RaisecomTransceiverTransferDistance_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 1, 4, 1, 8),
    _RaisecomTransceiverTransferDistance_Type()
)
raisecomTransceiverTransferDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomTransceiverTransferDistance.setStatus("current")
_RaisecomOpticalMonitorMIBNotifications_ObjectIdentity = ObjectIdentity
raisecomOpticalMonitorMIBNotifications = _RaisecomOpticalMonitorMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 2)
)
_RaisecomOpticalMonitorMIBConformance_ObjectIdentity = ObjectIdentity
raisecomOpticalMonitorMIBConformance = _RaisecomOpticalMonitorMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 3)
)
_RaisecomOpticalMonitorMIBCompliances_ObjectIdentity = ObjectIdentity
raisecomOpticalMonitorMIBCompliances = _RaisecomOpticalMonitorMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 3, 1)
)
_RaisecomOpticalMonitorMIBGroups_ObjectIdentity = ObjectIdentity
raisecomOpticalMonitorMIBGroups = _RaisecomOpticalMonitorMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 3, 2)
)

# Managed Objects groups

raisecomOpticalMIBMonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 3, 2, 1)
)
raisecomOpticalMIBMonGroup.setObjects(
    ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalParameterValue")
)
if mibBuilder.loadTexts:
    raisecomOpticalMIBMonGroup.setStatus("current")

raisecomOpticalMIBThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 3, 2, 2)
)
raisecomOpticalMIBThresholdGroup.setObjects(
      *(("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalParamHighAlarmThresh"),
        ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalParamHighWarningThresh"),
        ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalParamLowAlarmThresh"),
        ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalParamLowWarningThresh"),
        ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalParamAlarmStatus"),
        ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalParamAlarmLastValue"),
        ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalParamAlarmLastChange"))
)
if mibBuilder.loadTexts:
    raisecomOpticalMIBThresholdGroup.setStatus("current")

raisecomOpticalMIBPMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 3, 2, 3)
)
raisecomOpticalMIBPMGroup.setObjects(
      *(("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalMon15MinValidIntervals"),
        ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalMon24HrValidIntervals"),
        ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalPMCurrentMaxParam"),
        ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalPMCurrentMinParam"),
        ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalPMCurrentMeanParam"),
        ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalPMIntervalMaxParam"),
        ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalPMIntervalMinParam"),
        ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalPMIntervalMeanParam"))
)
if mibBuilder.loadTexts:
    raisecomOpticalMIBPMGroup.setStatus("current")

raisecomOpticalMIBNotifyEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 3, 2, 4)
)
raisecomOpticalMIBNotifyEnableGroup.setObjects(
    ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalNotifyEnable")
)
if mibBuilder.loadTexts:
    raisecomOpticalMIBNotifyEnableGroup.setStatus("current")


# Notification objects

raisecomOpticalMonParameterStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 2, 1)
)
raisecomOpticalMonParameterStatus.setObjects(
      *(("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalParameterValue"),
        ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalParamAlarmStatus"))
)
if mibBuilder.loadTexts:
    raisecomOpticalMonParameterStatus.setStatus(
        "current"
    )


# Notifications groups

raisecomOpticalMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 3, 2, 5)
)
raisecomOpticalMIBNotifGroup.setObjects(
    ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalMonParameterStatus")
)
if mibBuilder.loadTexts:
    raisecomOpticalMIBNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

raisecomOpticalMonitorMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8886, 1, 9, 3, 1, 1)
)
raisecomOpticalMonitorMIBCompliance.setObjects(
      *(("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalMIBMonGroup"),
        ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalMIBThresholdGroup"),
        ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalMIBPMGroup"),
        ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalMIBNotifyEnableGroup"),
        ("RAISECOM-OPTICAL-MONITOR-MIB", "raisecomOpticalMIBNotifGroup"))
)
if mibBuilder.loadTexts:
    raisecomOpticalMonitorMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-OPTICAL-MONITOR-MIB",
    **{"OpticalParameterType": OpticalParameterType,
       "OpticalParameterValue": OpticalParameterValue,
       "OpticalPMPeriod": OpticalPMPeriod,
       "raisecomOpticalMonitorMIB": raisecomOpticalMonitorMIB,
       "raisecomOpticalMonitorMIBObjects": raisecomOpticalMonitorMIBObjects,
       "raisecomOpticalMonGroup": raisecomOpticalMonGroup,
       "raisecomOpticalMonTable": raisecomOpticalMonTable,
       "raisecomOpticalMonEntry": raisecomOpticalMonEntry,
       "raisecomOpticalMonParameterType": raisecomOpticalMonParameterType,
       "raisecomOpticalParameterValue": raisecomOpticalParameterValue,
       "raisecomOpticalParamHighAlarmThresh": raisecomOpticalParamHighAlarmThresh,
       "raisecomOpticalParamHighWarningThresh": raisecomOpticalParamHighWarningThresh,
       "raisecomOpticalParamLowAlarmThresh": raisecomOpticalParamLowAlarmThresh,
       "raisecomOpticalParamLowWarningThresh": raisecomOpticalParamLowWarningThresh,
       "raisecomOpticalParamAlarmStatus": raisecomOpticalParamAlarmStatus,
       "raisecomOpticalParamAlarmLastValue": raisecomOpticalParamAlarmLastValue,
       "raisecomOpticalParamAlarmLastChange": raisecomOpticalParamAlarmLastChange,
       "raisecomOpticalMon15MinValidIntervals": raisecomOpticalMon15MinValidIntervals,
       "raisecomOpticalMon24HrValidIntervals": raisecomOpticalMon24HrValidIntervals,
       "raisecomOpticalMonValidStatus": raisecomOpticalMonValidStatus,
       "raisecomOpticalNotifyEnable": raisecomOpticalNotifyEnable,
       "raisecomOpticalDigitalDiagnoticEnable": raisecomOpticalDigitalDiagnoticEnable,
       "raisecomOpticalPMGroup": raisecomOpticalPMGroup,
       "raisecomOpticalPMCurrentTable": raisecomOpticalPMCurrentTable,
       "raisecomOpticalPMCurrentEntry": raisecomOpticalPMCurrentEntry,
       "raisecomOpticalPMCurrentPeriod": raisecomOpticalPMCurrentPeriod,
       "raisecomOpticalPMCurrentParamType": raisecomOpticalPMCurrentParamType,
       "raisecomOpticalPMCurrentMaxParam": raisecomOpticalPMCurrentMaxParam,
       "raisecomOpticalPMCurrentMinParam": raisecomOpticalPMCurrentMinParam,
       "raisecomOpticalPMCurrentMeanParam": raisecomOpticalPMCurrentMeanParam,
       "raisecomOpticalPMIntervalTable": raisecomOpticalPMIntervalTable,
       "raisecomOpticalPMIntervalEntry": raisecomOpticalPMIntervalEntry,
       "raisecomOpticalPMIntervalPeriod": raisecomOpticalPMIntervalPeriod,
       "raisecomOpticalPMIntervalNumber": raisecomOpticalPMIntervalNumber,
       "raisecomOpticalPMIntervalParamType": raisecomOpticalPMIntervalParamType,
       "raisecomOpticalPMIntervalMaxParam": raisecomOpticalPMIntervalMaxParam,
       "raisecomOpticalPMIntervalMinParam": raisecomOpticalPMIntervalMinParam,
       "raisecomOpticalPMIntervalMeanParam": raisecomOpticalPMIntervalMeanParam,
       "raisecomTranceiverInfoTable": raisecomTranceiverInfoTable,
       "raisecomTranceiverInfoEntry": raisecomTranceiverInfoEntry,
       "raisecomTranceiverType": raisecomTranceiverType,
       "raisecomTranceiverConnectorType": raisecomTranceiverConnectorType,
       "raisecomTranceiverWavelength": raisecomTranceiverWavelength,
       "raisecomTranceiverVendorName": raisecomTranceiverVendorName,
       "raisecomTranceiverVendorPN": raisecomTranceiverVendorPN,
       "raisecomTranceiverVendorSN": raisecomTranceiverVendorSN,
       "raisecomTransceiverFiberType": raisecomTransceiverFiberType,
       "raisecomTransceiverTransferDistance": raisecomTransceiverTransferDistance,
       "raisecomOpticalMonitorMIBNotifications": raisecomOpticalMonitorMIBNotifications,
       "raisecomOpticalMonParameterStatus": raisecomOpticalMonParameterStatus,
       "raisecomOpticalMonitorMIBConformance": raisecomOpticalMonitorMIBConformance,
       "raisecomOpticalMonitorMIBCompliances": raisecomOpticalMonitorMIBCompliances,
       "raisecomOpticalMonitorMIBCompliance": raisecomOpticalMonitorMIBCompliance,
       "raisecomOpticalMonitorMIBGroups": raisecomOpticalMonitorMIBGroups,
       "raisecomOpticalMIBMonGroup": raisecomOpticalMIBMonGroup,
       "raisecomOpticalMIBThresholdGroup": raisecomOpticalMIBThresholdGroup,
       "raisecomOpticalMIBPMGroup": raisecomOpticalMIBPMGroup,
       "raisecomOpticalMIBNotifyEnableGroup": raisecomOpticalMIBNotifyEnableGroup,
       "raisecomOpticalMIBNotifGroup": raisecomOpticalMIBNotifGroup}
)
