# SNMP MIB module (SLE-AM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-AM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:17 2025
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

(sleMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleMgmt")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "zeroDotZero")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleAlarmMgr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15)
)
if mibBuilder.loadTexts:
    sleAlarmMgr.setRevisions(
        ("2014-02-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AMAlarmClassId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class AMAlarmId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class AMAlarmSeverity(TextualConvention, Integer32):
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("intermediate", 5),
          ("default", 6))
    )



class AMTrapState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )



class AMAlarmGuardTime(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )



class AMAlarmSrc(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(68, 68),
    )
    fixed_length = 68



class AlarmStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("raised", 1),
          ("masked", 2),
          ("disabled", 3),
          ("forcedClear", 4),
          ("event", 5),
          ("unmasked", 6))
    )



class AMAlarmReason(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class AMDateTime(TextualConvention, Unsigned32):
    status = "current"


class AMAlarmAco(TextualConvention, Integer32):
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
        *(("acoOff", 1),
          ("acoOn", 2),
          ("acoOpr", 3))
    )



class AMAlarmLed(TextualConvention, Integer32):
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
        *(("setLedOff", 1),
          ("setLedOn", 2),
          ("oprLed", 3))
    )



# MIB Managed Objects in the order of their OIDs



class _SleAMAlarmTrapNeId_Type(OctetString):
    """Custom type sleAMAlarmTrapNeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_SleAMAlarmTrapNeId_Type.__name__ = "OctetString"
_SleAMAlarmTrapNeId_Object = MibScalar
sleAMAlarmTrapNeId = _SleAMAlarmTrapNeId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 1),
    _SleAMAlarmTrapNeId_Type()
)
sleAMAlarmTrapNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMAlarmTrapNeId.setStatus("current")
_SleAMConfigBase_ObjectIdentity = ObjectIdentity
sleAMConfigBase = _SleAMConfigBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2)
)
_SleAMConfigTable_Object = MibTable
sleAMConfigTable = _SleAMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 1)
)
if mibBuilder.loadTexts:
    sleAMConfigTable.setStatus("current")
_SleAMConfigEntry_Object = MibTableRow
sleAMConfigEntry = _SleAMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 1, 1)
)
sleAMConfigEntry.setIndexNames(
    (0, "SLE-AM-MIB", "sleAMConfigAlarmClassId"),
    (0, "SLE-AM-MIB", "sleAMConfigAlarmId"),
)
if mibBuilder.loadTexts:
    sleAMConfigEntry.setStatus("current")
_SleAMConfigAlarmClassId_Type = AMAlarmClassId
_SleAMConfigAlarmClassId_Object = MibTableColumn
sleAMConfigAlarmClassId = _SleAMConfigAlarmClassId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 1, 1, 1),
    _SleAMConfigAlarmClassId_Type()
)
sleAMConfigAlarmClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMConfigAlarmClassId.setStatus("current")
_SleAMConfigAlarmId_Type = AMAlarmId
_SleAMConfigAlarmId_Object = MibTableColumn
sleAMConfigAlarmId = _SleAMConfigAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 1, 1, 2),
    _SleAMConfigAlarmId_Type()
)
sleAMConfigAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMConfigAlarmId.setStatus("current")
_SleAMConfigAlarmName_Type = OctetString
_SleAMConfigAlarmName_Object = MibTableColumn
sleAMConfigAlarmName = _SleAMConfigAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 1, 1, 3),
    _SleAMConfigAlarmName_Type()
)
sleAMConfigAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMConfigAlarmName.setStatus("current")
_SleAMConfigAlarmSeverity_Type = AMAlarmSeverity
_SleAMConfigAlarmSeverity_Object = MibTableColumn
sleAMConfigAlarmSeverity = _SleAMConfigAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 1, 1, 4),
    _SleAMConfigAlarmSeverity_Type()
)
sleAMConfigAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMConfigAlarmSeverity.setStatus("current")
_SleAMConfigAlarmEnableState_Type = AMTrapState
_SleAMConfigAlarmEnableState_Object = MibTableColumn
sleAMConfigAlarmEnableState = _SleAMConfigAlarmEnableState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 1, 1, 5),
    _SleAMConfigAlarmEnableState_Type()
)
sleAMConfigAlarmEnableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMConfigAlarmEnableState.setStatus("current")
_SleAMConfigAlarmRaiseGuardTime_Type = AMAlarmGuardTime
_SleAMConfigAlarmRaiseGuardTime_Object = MibTableColumn
sleAMConfigAlarmRaiseGuardTime = _SleAMConfigAlarmRaiseGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 1, 1, 6),
    _SleAMConfigAlarmRaiseGuardTime_Type()
)
sleAMConfigAlarmRaiseGuardTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMConfigAlarmRaiseGuardTime.setStatus("current")
_SleAMConfigAlarmClearGuardTime_Type = AMAlarmGuardTime
_SleAMConfigAlarmClearGuardTime_Object = MibTableColumn
sleAMConfigAlarmClearGuardTime = _SleAMConfigAlarmClearGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 1, 1, 7),
    _SleAMConfigAlarmClearGuardTime_Type()
)
sleAMConfigAlarmClearGuardTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMConfigAlarmClearGuardTime.setStatus("current")


class _SleAMConfigAlarmLed_Type(Integer32):
    """Custom type sleAMConfigAlarmLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleAMConfigAlarmLed_Type.__name__ = "Integer32"
_SleAMConfigAlarmLed_Object = MibTableColumn
sleAMConfigAlarmLed = _SleAMConfigAlarmLed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 1, 1, 8),
    _SleAMConfigAlarmLed_Type()
)
sleAMConfigAlarmLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMConfigAlarmLed.setStatus("current")
_SleAMConfigSpecificId_Type = Integer32
_SleAMConfigSpecificId_Object = MibTableColumn
sleAMConfigSpecificId = _SleAMConfigSpecificId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 1, 1, 9),
    _SleAMConfigSpecificId_Type()
)
sleAMConfigSpecificId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMConfigSpecificId.setStatus("current")
_SleAMConfigControl_ObjectIdentity = ObjectIdentity
sleAMConfigControl = _SleAMConfigControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 2)
)


class _SleAMConfigControlRequest_Type(Integer32):
    """Custom type sleAMConfigControlRequest based on Integer32"""
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
        *(("setAMConfigTrapEnableState", 1),
          ("setAMConfigRaiseGuardTime", 2),
          ("setAMConfigClearGuardTime", 3),
          ("setAMConfigSeverity", 4),
          ("setAMConfigLed", 5))
    )


_SleAMConfigControlRequest_Type.__name__ = "Integer32"
_SleAMConfigControlRequest_Object = MibScalar
sleAMConfigControlRequest = _SleAMConfigControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 2, 1),
    _SleAMConfigControlRequest_Type()
)
sleAMConfigControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMConfigControlRequest.setStatus("current")
_SleAMConfigControlStatus_Type = SleControlStatusType
_SleAMConfigControlStatus_Object = MibScalar
sleAMConfigControlStatus = _SleAMConfigControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 2, 2),
    _SleAMConfigControlStatus_Type()
)
sleAMConfigControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMConfigControlStatus.setStatus("current")
_SleAMConfigControlTimer_Type = Gauge32
_SleAMConfigControlTimer_Object = MibScalar
sleAMConfigControlTimer = _SleAMConfigControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 2, 3),
    _SleAMConfigControlTimer_Type()
)
sleAMConfigControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMConfigControlTimer.setStatus("current")
_SleAMConfigControlTimeStamp_Type = TimeTicks
_SleAMConfigControlTimeStamp_Object = MibScalar
sleAMConfigControlTimeStamp = _SleAMConfigControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 2, 4),
    _SleAMConfigControlTimeStamp_Type()
)
sleAMConfigControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMConfigControlTimeStamp.setStatus("current")
_SleAMConfigControlReqResult_Type = SleControlRequestResultType
_SleAMConfigControlReqResult_Object = MibScalar
sleAMConfigControlReqResult = _SleAMConfigControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 2, 5),
    _SleAMConfigControlReqResult_Type()
)
sleAMConfigControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMConfigControlReqResult.setStatus("current")
_SleAMConfigControlAlarmClassId_Type = AMAlarmClassId
_SleAMConfigControlAlarmClassId_Object = MibScalar
sleAMConfigControlAlarmClassId = _SleAMConfigControlAlarmClassId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 2, 6),
    _SleAMConfigControlAlarmClassId_Type()
)
sleAMConfigControlAlarmClassId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMConfigControlAlarmClassId.setStatus("current")
_SleAMConfigControlAlarmId_Type = AMAlarmId
_SleAMConfigControlAlarmId_Object = MibScalar
sleAMConfigControlAlarmId = _SleAMConfigControlAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 2, 7),
    _SleAMConfigControlAlarmId_Type()
)
sleAMConfigControlAlarmId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMConfigControlAlarmId.setStatus("current")
_SleAMConfigControlSeverity_Type = AMAlarmSeverity
_SleAMConfigControlSeverity_Object = MibScalar
sleAMConfigControlSeverity = _SleAMConfigControlSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 2, 8),
    _SleAMConfigControlSeverity_Type()
)
sleAMConfigControlSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMConfigControlSeverity.setStatus("current")
_SleAMConfigControlEnableState_Type = AMTrapState
_SleAMConfigControlEnableState_Object = MibScalar
sleAMConfigControlEnableState = _SleAMConfigControlEnableState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 2, 9),
    _SleAMConfigControlEnableState_Type()
)
sleAMConfigControlEnableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMConfigControlEnableState.setStatus("current")
_SleAMConfigControlRaiseGuardTime_Type = AMAlarmGuardTime
_SleAMConfigControlRaiseGuardTime_Object = MibScalar
sleAMConfigControlRaiseGuardTime = _SleAMConfigControlRaiseGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 2, 10),
    _SleAMConfigControlRaiseGuardTime_Type()
)
sleAMConfigControlRaiseGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMConfigControlRaiseGuardTime.setStatus("current")
_SleAMConfigControlClearGuardTime_Type = AMAlarmGuardTime
_SleAMConfigControlClearGuardTime_Object = MibScalar
sleAMConfigControlClearGuardTime = _SleAMConfigControlClearGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 2, 11),
    _SleAMConfigControlClearGuardTime_Type()
)
sleAMConfigControlClearGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMConfigControlClearGuardTime.setStatus("current")
_SleAMConfigControlLed_Type = Integer32
_SleAMConfigControlLed_Object = MibScalar
sleAMConfigControlLed = _SleAMConfigControlLed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 2, 12),
    _SleAMConfigControlLed_Type()
)
sleAMConfigControlLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMConfigControlLed.setStatus("current")
_SleAMConfigNotification_ObjectIdentity = ObjectIdentity
sleAMConfigNotification = _SleAMConfigNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 3)
)
_SleAMCurrentBase_ObjectIdentity = ObjectIdentity
sleAMCurrentBase = _SleAMCurrentBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3)
)
_SleAMCurrentTable_Object = MibTable
sleAMCurrentTable = _SleAMCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 1)
)
if mibBuilder.loadTexts:
    sleAMCurrentTable.setStatus("current")
_SleAMCurrentEntry_Object = MibTableRow
sleAMCurrentEntry = _SleAMCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 1, 1)
)
sleAMCurrentEntry.setIndexNames(
    (0, "SLE-AM-MIB", "sleAMCurrentSeqId"),
)
if mibBuilder.loadTexts:
    sleAMCurrentEntry.setStatus("current")


class _SleAMCurrentSeqId_Type(Unsigned32):
    """Custom type sleAMCurrentSeqId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleAMCurrentSeqId_Type.__name__ = "Unsigned32"
_SleAMCurrentSeqId_Object = MibTableColumn
sleAMCurrentSeqId = _SleAMCurrentSeqId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 1, 1, 1),
    _SleAMCurrentSeqId_Type()
)
sleAMCurrentSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMCurrentSeqId.setStatus("current")
_SleAMCurrentAlarmSource_Type = AMAlarmSrc
_SleAMCurrentAlarmSource_Object = MibTableColumn
sleAMCurrentAlarmSource = _SleAMCurrentAlarmSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 1, 1, 2),
    _SleAMCurrentAlarmSource_Type()
)
sleAMCurrentAlarmSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMCurrentAlarmSource.setStatus("current")
_SleAMCurrentAlarmClassId_Type = AMAlarmClassId
_SleAMCurrentAlarmClassId_Object = MibTableColumn
sleAMCurrentAlarmClassId = _SleAMCurrentAlarmClassId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 1, 1, 3),
    _SleAMCurrentAlarmClassId_Type()
)
sleAMCurrentAlarmClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMCurrentAlarmClassId.setStatus("current")
_SleAMCurrentAlarmId_Type = AMAlarmId
_SleAMCurrentAlarmId_Object = MibTableColumn
sleAMCurrentAlarmId = _SleAMCurrentAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 1, 1, 4),
    _SleAMCurrentAlarmId_Type()
)
sleAMCurrentAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMCurrentAlarmId.setStatus("current")
_SleAMCurrentAlarmStatus_Type = AlarmStatus
_SleAMCurrentAlarmStatus_Object = MibTableColumn
sleAMCurrentAlarmStatus = _SleAMCurrentAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 1, 1, 5),
    _SleAMCurrentAlarmStatus_Type()
)
sleAMCurrentAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMCurrentAlarmStatus.setStatus("current")
_SleAMCurrentAlarmSeverity_Type = AMAlarmSeverity
_SleAMCurrentAlarmSeverity_Object = MibTableColumn
sleAMCurrentAlarmSeverity = _SleAMCurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 1, 1, 6),
    _SleAMCurrentAlarmSeverity_Type()
)
sleAMCurrentAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMCurrentAlarmSeverity.setStatus("current")
_SleAMCurrentAlarmReason_Type = AMAlarmReason
_SleAMCurrentAlarmReason_Object = MibTableColumn
sleAMCurrentAlarmReason = _SleAMCurrentAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 1, 1, 7),
    _SleAMCurrentAlarmReason_Type()
)
sleAMCurrentAlarmReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMCurrentAlarmReason.setStatus("current")
_SleAMCurrentTimeAndDate_Type = TimeTicks
_SleAMCurrentTimeAndDate_Object = MibTableColumn
sleAMCurrentTimeAndDate = _SleAMCurrentTimeAndDate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 1, 1, 8),
    _SleAMCurrentTimeAndDate_Type()
)
sleAMCurrentTimeAndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMCurrentTimeAndDate.setStatus("current")
_SleAMCurrentSpecificId_Type = Integer32
_SleAMCurrentSpecificId_Object = MibTableColumn
sleAMCurrentSpecificId = _SleAMCurrentSpecificId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 1, 1, 9),
    _SleAMCurrentSpecificId_Type()
)
sleAMCurrentSpecificId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMCurrentSpecificId.setStatus("current")
_SleAMCurrentControl_ObjectIdentity = ObjectIdentity
sleAMCurrentControl = _SleAMCurrentControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 2)
)


class _SleAMCurrentControlRequest_Type(Integer32):
    """Custom type sleAMCurrentControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allAlarmClear", 1),
          ("alarmClearBySeqId", 2),
          ("alarmClearBySource", 3))
    )


_SleAMCurrentControlRequest_Type.__name__ = "Integer32"
_SleAMCurrentControlRequest_Object = MibScalar
sleAMCurrentControlRequest = _SleAMCurrentControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 2, 1),
    _SleAMCurrentControlRequest_Type()
)
sleAMCurrentControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMCurrentControlRequest.setStatus("current")
_SleAMCurrentControlStatus_Type = SleControlStatusType
_SleAMCurrentControlStatus_Object = MibScalar
sleAMCurrentControlStatus = _SleAMCurrentControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 2, 2),
    _SleAMCurrentControlStatus_Type()
)
sleAMCurrentControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMCurrentControlStatus.setStatus("current")
_SleAMCurrentControlTimer_Type = Gauge32
_SleAMCurrentControlTimer_Object = MibScalar
sleAMCurrentControlTimer = _SleAMCurrentControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 2, 3),
    _SleAMCurrentControlTimer_Type()
)
sleAMCurrentControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMCurrentControlTimer.setStatus("current")
_SleAMCurrentControlTimeStamp_Type = TimeTicks
_SleAMCurrentControlTimeStamp_Object = MibScalar
sleAMCurrentControlTimeStamp = _SleAMCurrentControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 2, 4),
    _SleAMCurrentControlTimeStamp_Type()
)
sleAMCurrentControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMCurrentControlTimeStamp.setStatus("current")
_SleAMCurrentControlReqResult_Type = SleControlRequestResultType
_SleAMCurrentControlReqResult_Object = MibScalar
sleAMCurrentControlReqResult = _SleAMCurrentControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 2, 5),
    _SleAMCurrentControlReqResult_Type()
)
sleAMCurrentControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMCurrentControlReqResult.setStatus("current")
_SleAMCurrentControlSeqId_Type = Unsigned32
_SleAMCurrentControlSeqId_Object = MibScalar
sleAMCurrentControlSeqId = _SleAMCurrentControlSeqId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 2, 6),
    _SleAMCurrentControlSeqId_Type()
)
sleAMCurrentControlSeqId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMCurrentControlSeqId.setStatus("current")
_SleAMCurrentControlSource_Type = AMAlarmSrc
_SleAMCurrentControlSource_Object = MibScalar
sleAMCurrentControlSource = _SleAMCurrentControlSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 2, 7),
    _SleAMCurrentControlSource_Type()
)
sleAMCurrentControlSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMCurrentControlSource.setStatus("current")
_SleAMCurrentNotification_ObjectIdentity = ObjectIdentity
sleAMCurrentNotification = _SleAMCurrentNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 3)
)
_SleAMHistoryBase_ObjectIdentity = ObjectIdentity
sleAMHistoryBase = _SleAMHistoryBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4)
)
_SleAMHistoryTable_Object = MibTable
sleAMHistoryTable = _SleAMHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 1)
)
if mibBuilder.loadTexts:
    sleAMHistoryTable.setStatus("current")
_SleAMHistoryEntry_Object = MibTableRow
sleAMHistoryEntry = _SleAMHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 1, 1)
)
sleAMHistoryEntry.setIndexNames(
    (0, "SLE-AM-MIB", "sleAMHistorySeqId"),
)
if mibBuilder.loadTexts:
    sleAMHistoryEntry.setStatus("current")


class _SleAMHistorySeqId_Type(Unsigned32):
    """Custom type sleAMHistorySeqId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleAMHistorySeqId_Type.__name__ = "Unsigned32"
_SleAMHistorySeqId_Object = MibTableColumn
sleAMHistorySeqId = _SleAMHistorySeqId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 1, 1, 1),
    _SleAMHistorySeqId_Type()
)
sleAMHistorySeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMHistorySeqId.setStatus("current")
_SleAMHistoryAlarmSource_Type = AMAlarmSrc
_SleAMHistoryAlarmSource_Object = MibTableColumn
sleAMHistoryAlarmSource = _SleAMHistoryAlarmSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 1, 1, 2),
    _SleAMHistoryAlarmSource_Type()
)
sleAMHistoryAlarmSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMHistoryAlarmSource.setStatus("current")
_SleAMHistoryAlarmClassId_Type = AMAlarmClassId
_SleAMHistoryAlarmClassId_Object = MibTableColumn
sleAMHistoryAlarmClassId = _SleAMHistoryAlarmClassId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 1, 1, 3),
    _SleAMHistoryAlarmClassId_Type()
)
sleAMHistoryAlarmClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMHistoryAlarmClassId.setStatus("current")
_SleAMHistoryAlarmId_Type = AMAlarmId
_SleAMHistoryAlarmId_Object = MibTableColumn
sleAMHistoryAlarmId = _SleAMHistoryAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 1, 1, 4),
    _SleAMHistoryAlarmId_Type()
)
sleAMHistoryAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMHistoryAlarmId.setStatus("current")
_SleAMHistoryAlarmStatus_Type = AlarmStatus
_SleAMHistoryAlarmStatus_Object = MibTableColumn
sleAMHistoryAlarmStatus = _SleAMHistoryAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 1, 1, 5),
    _SleAMHistoryAlarmStatus_Type()
)
sleAMHistoryAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMHistoryAlarmStatus.setStatus("current")
_SleAMHistoryAlarmSeverity_Type = AMAlarmSeverity
_SleAMHistoryAlarmSeverity_Object = MibTableColumn
sleAMHistoryAlarmSeverity = _SleAMHistoryAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 1, 1, 6),
    _SleAMHistoryAlarmSeverity_Type()
)
sleAMHistoryAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMHistoryAlarmSeverity.setStatus("current")
_SleAMHistoryAlarmReason_Type = AMAlarmReason
_SleAMHistoryAlarmReason_Object = MibTableColumn
sleAMHistoryAlarmReason = _SleAMHistoryAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 1, 1, 7),
    _SleAMHistoryAlarmReason_Type()
)
sleAMHistoryAlarmReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMHistoryAlarmReason.setStatus("current")
_SleAMHistoryAlarmTimeDate_Type = TimeTicks
_SleAMHistoryAlarmTimeDate_Object = MibTableColumn
sleAMHistoryAlarmTimeDate = _SleAMHistoryAlarmTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 1, 1, 8),
    _SleAMHistoryAlarmTimeDate_Type()
)
sleAMHistoryAlarmTimeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMHistoryAlarmTimeDate.setStatus("current")
_SleAMHistorySpecificId_Type = Integer32
_SleAMHistorySpecificId_Object = MibTableColumn
sleAMHistorySpecificId = _SleAMHistorySpecificId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 1, 1, 9),
    _SleAMHistorySpecificId_Type()
)
sleAMHistorySpecificId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMHistorySpecificId.setStatus("current")
_SleAMHistoryControl_ObjectIdentity = ObjectIdentity
sleAMHistoryControl = _SleAMHistoryControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 2)
)


class _SleAMHistoryControlRequest_Type(Integer32):
    """Custom type sleAMHistoryControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allAlarmHistoryClear", 1),
          ("alarmHistoryClearBySeqId", 2),
          ("alarmHistoryClearBySource", 3))
    )


_SleAMHistoryControlRequest_Type.__name__ = "Integer32"
_SleAMHistoryControlRequest_Object = MibScalar
sleAMHistoryControlRequest = _SleAMHistoryControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 2, 1),
    _SleAMHistoryControlRequest_Type()
)
sleAMHistoryControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMHistoryControlRequest.setStatus("current")
_SleAMHistoryControlStatus_Type = SleControlStatusType
_SleAMHistoryControlStatus_Object = MibScalar
sleAMHistoryControlStatus = _SleAMHistoryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 2, 2),
    _SleAMHistoryControlStatus_Type()
)
sleAMHistoryControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMHistoryControlStatus.setStatus("current")
_SleAMHistoryControlTimer_Type = Gauge32
_SleAMHistoryControlTimer_Object = MibScalar
sleAMHistoryControlTimer = _SleAMHistoryControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 2, 3),
    _SleAMHistoryControlTimer_Type()
)
sleAMHistoryControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMHistoryControlTimer.setStatus("current")
_SleAMHistoryControlTimeStamp_Type = TimeTicks
_SleAMHistoryControlTimeStamp_Object = MibScalar
sleAMHistoryControlTimeStamp = _SleAMHistoryControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 2, 4),
    _SleAMHistoryControlTimeStamp_Type()
)
sleAMHistoryControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMHistoryControlTimeStamp.setStatus("current")
_SleAMHistoryControlReqResult_Type = SleControlRequestResultType
_SleAMHistoryControlReqResult_Object = MibScalar
sleAMHistoryControlReqResult = _SleAMHistoryControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 2, 5),
    _SleAMHistoryControlReqResult_Type()
)
sleAMHistoryControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMHistoryControlReqResult.setStatus("current")
_SleAMHistoryControSeqId_Type = Unsigned32
_SleAMHistoryControSeqId_Object = MibScalar
sleAMHistoryControSeqId = _SleAMHistoryControSeqId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 2, 6),
    _SleAMHistoryControSeqId_Type()
)
sleAMHistoryControSeqId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMHistoryControSeqId.setStatus("current")
_SleAMHistoryControSource_Type = AMAlarmSrc
_SleAMHistoryControSource_Object = MibScalar
sleAMHistoryControSource = _SleAMHistoryControSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 2, 7),
    _SleAMHistoryControSource_Type()
)
sleAMHistoryControSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMHistoryControSource.setStatus("current")
_SleAMHistoryNotification_ObjectIdentity = ObjectIdentity
sleAMHistoryNotification = _SleAMHistoryNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 3)
)
_SleAMAcoBase_ObjectIdentity = ObjectIdentity
sleAMAcoBase = _SleAMAcoBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 5)
)
_SleAMAcoInfoEntry_ObjectIdentity = ObjectIdentity
sleAMAcoInfoEntry = _SleAMAcoInfoEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 5, 1)
)
_SleAMAcoInfo_Type = AMAlarmAco
_SleAMAcoInfo_Object = MibScalar
sleAMAcoInfo = _SleAMAcoInfo_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 5, 1, 1),
    _SleAMAcoInfo_Type()
)
sleAMAcoInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMAcoInfo.setStatus("current")
_SleAMAcoControl_ObjectIdentity = ObjectIdentity
sleAMAcoControl = _SleAMAcoControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 5, 2)
)


class _SleAMAcoControlRequest_Type(Integer32):
    """Custom type sleAMAcoControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oprAco", 1),
          ("setAco", 2))
    )


_SleAMAcoControlRequest_Type.__name__ = "Integer32"
_SleAMAcoControlRequest_Object = MibScalar
sleAMAcoControlRequest = _SleAMAcoControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 5, 2, 1),
    _SleAMAcoControlRequest_Type()
)
sleAMAcoControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMAcoControlRequest.setStatus("current")
_SleAMAcogControlStatus_Type = SleControlStatusType
_SleAMAcogControlStatus_Object = MibScalar
sleAMAcogControlStatus = _SleAMAcogControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 5, 2, 2),
    _SleAMAcogControlStatus_Type()
)
sleAMAcogControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMAcogControlStatus.setStatus("current")
_SleAMAcoControlTimer_Type = Gauge32
_SleAMAcoControlTimer_Object = MibScalar
sleAMAcoControlTimer = _SleAMAcoControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 5, 2, 3),
    _SleAMAcoControlTimer_Type()
)
sleAMAcoControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMAcoControlTimer.setStatus("current")
_SleAMAcoControlTimeStamp_Type = TimeTicks
_SleAMAcoControlTimeStamp_Object = MibScalar
sleAMAcoControlTimeStamp = _SleAMAcoControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 5, 2, 4),
    _SleAMAcoControlTimeStamp_Type()
)
sleAMAcoControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMAcoControlTimeStamp.setStatus("current")
_SleAMAcoControlReqResult_Type = SleControlRequestResultType
_SleAMAcoControlReqResult_Object = MibScalar
sleAMAcoControlReqResult = _SleAMAcoControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 5, 2, 5),
    _SleAMAcoControlReqResult_Type()
)
sleAMAcoControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMAcoControlReqResult.setStatus("current")
_SleAMAcoControlSet_Type = AMAlarmAco
_SleAMAcoControlSet_Object = MibScalar
sleAMAcoControlSet = _SleAMAcoControlSet_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 5, 2, 6),
    _SleAMAcoControlSet_Type()
)
sleAMAcoControlSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMAcoControlSet.setStatus("current")
_SleAMAcoNotification_ObjectIdentity = ObjectIdentity
sleAMAcoNotification = _SleAMAcoNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 5, 3)
)
_SleAMLedBase_ObjectIdentity = ObjectIdentity
sleAMLedBase = _SleAMLedBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 6)
)
_SleAMLedTable_Object = MibTable
sleAMLedTable = _SleAMLedTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 6, 1)
)
if mibBuilder.loadTexts:
    sleAMLedTable.setStatus("current")
_SleAMLedEntry_Object = MibTableRow
sleAMLedEntry = _SleAMLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 6, 1, 1)
)
sleAMLedEntry.setIndexNames(
    (0, "SLE-AM-MIB", "sleAMLedSeverity"),
)
if mibBuilder.loadTexts:
    sleAMLedEntry.setStatus("current")


class _SleAMLedSeverity_Type(Integer32):
    """Custom type sleAMLedSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3))
    )


_SleAMLedSeverity_Type.__name__ = "Integer32"
_SleAMLedSeverity_Object = MibTableColumn
sleAMLedSeverity = _SleAMLedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 6, 1, 1, 1),
    _SleAMLedSeverity_Type()
)
sleAMLedSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMLedSeverity.setStatus("current")
_SleAMLedSet_Type = AMAlarmLed
_SleAMLedSet_Object = MibTableColumn
sleAMLedSet = _SleAMLedSet_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 6, 1, 1, 2),
    _SleAMLedSet_Type()
)
sleAMLedSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMLedSet.setStatus("current")
_SleAMLedCount_Type = Integer32
_SleAMLedCount_Object = MibTableColumn
sleAMLedCount = _SleAMLedCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 6, 1, 1, 3),
    _SleAMLedCount_Type()
)
sleAMLedCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMLedCount.setStatus("current")
_SleAMLedControl_ObjectIdentity = ObjectIdentity
sleAMLedControl = _SleAMLedControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 6, 2)
)


class _SleAMLedControlRequest_Type(Integer32):
    """Custom type sleAMLedControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oprLed", 1),
          ("setLed", 2),
          ("ledCount", 3))
    )


_SleAMLedControlRequest_Type.__name__ = "Integer32"
_SleAMLedControlRequest_Object = MibScalar
sleAMLedControlRequest = _SleAMLedControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 6, 2, 1),
    _SleAMLedControlRequest_Type()
)
sleAMLedControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMLedControlRequest.setStatus("current")
_SleAMLedControlStatus_Type = SleControlStatusType
_SleAMLedControlStatus_Object = MibScalar
sleAMLedControlStatus = _SleAMLedControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 6, 2, 2),
    _SleAMLedControlStatus_Type()
)
sleAMLedControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMLedControlStatus.setStatus("current")
_SleAMLedControlTimer_Type = Gauge32
_SleAMLedControlTimer_Object = MibScalar
sleAMLedControlTimer = _SleAMLedControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 6, 2, 3),
    _SleAMLedControlTimer_Type()
)
sleAMLedControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMLedControlTimer.setStatus("current")
_SleAMLedControlTimeStamp_Type = TimeTicks
_SleAMLedControlTimeStamp_Object = MibScalar
sleAMLedControlTimeStamp = _SleAMLedControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 6, 2, 4),
    _SleAMLedControlTimeStamp_Type()
)
sleAMLedControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMLedControlTimeStamp.setStatus("current")
_SleAMLedControlReqResult_Type = SleControlRequestResultType
_SleAMLedControlReqResult_Object = MibScalar
sleAMLedControlReqResult = _SleAMLedControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 6, 2, 5),
    _SleAMLedControlReqResult_Type()
)
sleAMLedControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAMLedControlReqResult.setStatus("current")


class _SleAMLedControlSeverity_Type(Integer32):
    """Custom type sleAMLedControlSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("critical", 1),
          ("major", 2),
          ("minor", 3))
    )


_SleAMLedControlSeverity_Type.__name__ = "Integer32"
_SleAMLedControlSeverity_Object = MibScalar
sleAMLedControlSeverity = _SleAMLedControlSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 6, 2, 6),
    _SleAMLedControlSeverity_Type()
)
sleAMLedControlSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMLedControlSeverity.setStatus("current")
_SleAMLedControlSet_Type = AMAlarmLed
_SleAMLedControlSet_Object = MibScalar
sleAMLedControlSet = _SleAMLedControlSet_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 6, 2, 7),
    _SleAMLedControlSet_Type()
)
sleAMLedControlSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAMLedControlSet.setStatus("current")
_SleAMLedNotification_ObjectIdentity = ObjectIdentity
sleAMLedNotification = _SleAMLedNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 6, 3)
)

# Managed Objects groups


# Notification objects

sleAMConfigSeverityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 3, 1)
)
sleAMConfigSeverityChanged.setObjects(
      *(("SLE-AM-MIB", "sleAMAlarmTrapNeId"),
        ("SLE-AM-MIB", "sleAMConfigControlRequest"),
        ("SLE-AM-MIB", "sleAMConfigControlTimeStamp"),
        ("SLE-AM-MIB", "sleAMConfigControlReqResult"),
        ("SLE-AM-MIB", "sleAMConfigControlAlarmClassId"),
        ("SLE-AM-MIB", "sleAMConfigControlAlarmId"),
        ("SLE-AM-MIB", "sleAMConfigControlSeverity"))
)
if mibBuilder.loadTexts:
    sleAMConfigSeverityChanged.setStatus(
        "current"
    )

sleAMConfigEnableStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 3, 2)
)
sleAMConfigEnableStateChanged.setObjects(
      *(("SLE-AM-MIB", "sleAMAlarmTrapNeId"),
        ("SLE-AM-MIB", "sleAMConfigControlRequest"),
        ("SLE-AM-MIB", "sleAMConfigControlTimeStamp"),
        ("SLE-AM-MIB", "sleAMConfigControlReqResult"),
        ("SLE-AM-MIB", "sleAMConfigControlAlarmClassId"),
        ("SLE-AM-MIB", "sleAMConfigControlAlarmId"),
        ("SLE-AM-MIB", "sleAMConfigControlEnableState"))
)
if mibBuilder.loadTexts:
    sleAMConfigEnableStateChanged.setStatus(
        "current"
    )

sleAMConfigRaiseGuardTimeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 3, 3)
)
sleAMConfigRaiseGuardTimeChanged.setObjects(
      *(("SLE-AM-MIB", "sleAMAlarmTrapNeId"),
        ("SLE-AM-MIB", "sleAMConfigControlRequest"),
        ("SLE-AM-MIB", "sleAMConfigControlReqResult"),
        ("SLE-AM-MIB", "sleAMConfigControlTimeStamp"),
        ("SLE-AM-MIB", "sleAMConfigControlAlarmClassId"),
        ("SLE-AM-MIB", "sleAMConfigControlAlarmId"),
        ("SLE-AM-MIB", "sleAMConfigControlRaiseGuardTime"))
)
if mibBuilder.loadTexts:
    sleAMConfigRaiseGuardTimeChanged.setStatus(
        "current"
    )

sleAMConfigClearGuardTimeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 3, 4)
)
sleAMConfigClearGuardTimeChanged.setObjects(
      *(("SLE-AM-MIB", "sleAMAlarmTrapNeId"),
        ("SLE-AM-MIB", "sleAMConfigControlRequest"),
        ("SLE-AM-MIB", "sleAMConfigControlTimeStamp"),
        ("SLE-AM-MIB", "sleAMConfigControlReqResult"),
        ("SLE-AM-MIB", "sleAMConfigControlAlarmClassId"),
        ("SLE-AM-MIB", "sleAMConfigControlAlarmId"),
        ("SLE-AM-MIB", "sleAMConfigControlClearGuardTime"))
)
if mibBuilder.loadTexts:
    sleAMConfigClearGuardTimeChanged.setStatus(
        "current"
    )

sleAMConfigLedChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 2, 3, 5)
)
sleAMConfigLedChanged.setObjects(
      *(("SLE-AM-MIB", "sleAMAlarmTrapNeId"),
        ("SLE-AM-MIB", "sleAMConfigControlRequest"),
        ("SLE-AM-MIB", "sleAMConfigControlTimeStamp"),
        ("SLE-AM-MIB", "sleAMConfigControlReqResult"),
        ("SLE-AM-MIB", "sleAMConfigControlAlarmClassId"),
        ("SLE-AM-MIB", "sleAMConfigControlAlarmId"),
        ("SLE-AM-MIB", "sleAMConfigControlLed"))
)
if mibBuilder.loadTexts:
    sleAMConfigLedChanged.setStatus(
        "current"
    )

sleAMCurrentAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 3, 1)
)
sleAMCurrentAlarmCleared.setObjects(
      *(("SLE-AM-MIB", "sleAMAlarmTrapNeId"),
        ("SLE-AM-MIB", "sleAMCurrentControlRequest"),
        ("SLE-AM-MIB", "sleAMCurrentControlTimeStamp"),
        ("SLE-AM-MIB", "sleAMCurrentControlReqResult"),
        ("SLE-AM-MIB", "sleAMCurrentControlSeqId"))
)
if mibBuilder.loadTexts:
    sleAMCurrentAlarmCleared.setStatus(
        "current"
    )

sleAlarmTrapAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 3, 2)
)
sleAlarmTrapAlarm.setObjects(
      *(("SLE-AM-MIB", "sleAMAlarmTrapNeId"),
        ("SLE-AM-MIB", "sleAMCurrentSeqId"),
        ("SLE-AM-MIB", "sleAMCurrentAlarmSource"),
        ("SLE-AM-MIB", "sleAMCurrentAlarmReason"),
        ("SLE-AM-MIB", "sleAMCurrentSpecificId"),
        ("SLE-AM-MIB", "sleAMCurrentAlarmId"),
        ("SLE-AM-MIB", "sleAMCurrentAlarmClassId"),
        ("SLE-AM-MIB", "sleAMCurrentAlarmStatus"),
        ("SLE-AM-MIB", "sleAMCurrentAlarmSeverity"),
        ("SLE-AM-MIB", "sleAMCurrentTimeAndDate"))
)
if mibBuilder.loadTexts:
    sleAlarmTrapAlarm.setStatus(
        "current"
    )

sleAlarmTrapEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 3, 3, 3)
)
sleAlarmTrapEvent.setObjects(
      *(("SLE-AM-MIB", "sleAMAlarmTrapNeId"),
        ("SLE-AM-MIB", "sleAMCurrentSeqId"),
        ("SLE-AM-MIB", "sleAMCurrentAlarmSource"),
        ("SLE-AM-MIB", "sleAMCurrentAlarmClassId"),
        ("SLE-AM-MIB", "sleAMCurrentAlarmId"),
        ("SLE-AM-MIB", "sleAMCurrentAlarmStatus"),
        ("SLE-AM-MIB", "sleAMCurrentAlarmSeverity"),
        ("SLE-AM-MIB", "sleAMCurrentSpecificId"),
        ("SLE-AM-MIB", "sleAMCurrentTimeAndDate"),
        ("SLE-AM-MIB", "sleAMCurrentAlarmReason"))
)
if mibBuilder.loadTexts:
    sleAlarmTrapEvent.setStatus(
        "current"
    )

sleAMHistoryAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 4, 3, 1)
)
sleAMHistoryAlarmCleared.setObjects(
      *(("SLE-AM-MIB", "sleAMAlarmTrapNeId"),
        ("SLE-AM-MIB", "sleAMHistoryControlRequest"),
        ("SLE-AM-MIB", "sleAMHistoryControlTimeStamp"),
        ("SLE-AM-MIB", "sleAMHistoryControlReqResult"),
        ("SLE-AM-MIB", "sleAMHistoryControSeqId"))
)
if mibBuilder.loadTexts:
    sleAMHistoryAlarmCleared.setStatus(
        "current"
    )

sleAMAcoChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 5, 3, 1)
)
sleAMAcoChanged.setObjects(
      *(("SLE-AM-MIB", "sleAMAlarmTrapNeId"),
        ("SLE-AM-MIB", "sleAMAcoControlRequest"),
        ("SLE-AM-MIB", "sleAMAcoControlTimeStamp"),
        ("SLE-AM-MIB", "sleAMAcoControlReqResult"),
        ("SLE-AM-MIB", "sleAMAcoControlSet"))
)
if mibBuilder.loadTexts:
    sleAMAcoChanged.setStatus(
        "current"
    )

sleAMLedChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 15, 6, 3, 1)
)
sleAMLedChanged.setObjects(
      *(("SLE-AM-MIB", "sleAMAlarmTrapNeId"),
        ("SLE-AM-MIB", "sleAMLedControlRequest"),
        ("SLE-AM-MIB", "sleAMLedControlTimeStamp"),
        ("SLE-AM-MIB", "sleAMLedControlReqResult"),
        ("SLE-AM-MIB", "sleAMLedControlSeverity"),
        ("SLE-AM-MIB", "sleAMLedControlSet"))
)
if mibBuilder.loadTexts:
    sleAMLedChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-AM-MIB",
    **{"AMAlarmClassId": AMAlarmClassId,
       "AMAlarmId": AMAlarmId,
       "AMAlarmSeverity": AMAlarmSeverity,
       "AMTrapState": AMTrapState,
       "AMAlarmGuardTime": AMAlarmGuardTime,
       "AMAlarmSrc": AMAlarmSrc,
       "AlarmStatus": AlarmStatus,
       "AMAlarmReason": AMAlarmReason,
       "AMDateTime": AMDateTime,
       "AMAlarmAco": AMAlarmAco,
       "AMAlarmLed": AMAlarmLed,
       "sleAlarmMgr": sleAlarmMgr,
       "sleAMAlarmTrapNeId": sleAMAlarmTrapNeId,
       "sleAMConfigBase": sleAMConfigBase,
       "sleAMConfigTable": sleAMConfigTable,
       "sleAMConfigEntry": sleAMConfigEntry,
       "sleAMConfigAlarmClassId": sleAMConfigAlarmClassId,
       "sleAMConfigAlarmId": sleAMConfigAlarmId,
       "sleAMConfigAlarmName": sleAMConfigAlarmName,
       "sleAMConfigAlarmSeverity": sleAMConfigAlarmSeverity,
       "sleAMConfigAlarmEnableState": sleAMConfigAlarmEnableState,
       "sleAMConfigAlarmRaiseGuardTime": sleAMConfigAlarmRaiseGuardTime,
       "sleAMConfigAlarmClearGuardTime": sleAMConfigAlarmClearGuardTime,
       "sleAMConfigAlarmLed": sleAMConfigAlarmLed,
       "sleAMConfigSpecificId": sleAMConfigSpecificId,
       "sleAMConfigControl": sleAMConfigControl,
       "sleAMConfigControlRequest": sleAMConfigControlRequest,
       "sleAMConfigControlStatus": sleAMConfigControlStatus,
       "sleAMConfigControlTimer": sleAMConfigControlTimer,
       "sleAMConfigControlTimeStamp": sleAMConfigControlTimeStamp,
       "sleAMConfigControlReqResult": sleAMConfigControlReqResult,
       "sleAMConfigControlAlarmClassId": sleAMConfigControlAlarmClassId,
       "sleAMConfigControlAlarmId": sleAMConfigControlAlarmId,
       "sleAMConfigControlSeverity": sleAMConfigControlSeverity,
       "sleAMConfigControlEnableState": sleAMConfigControlEnableState,
       "sleAMConfigControlRaiseGuardTime": sleAMConfigControlRaiseGuardTime,
       "sleAMConfigControlClearGuardTime": sleAMConfigControlClearGuardTime,
       "sleAMConfigControlLed": sleAMConfigControlLed,
       "sleAMConfigNotification": sleAMConfigNotification,
       "sleAMConfigSeverityChanged": sleAMConfigSeverityChanged,
       "sleAMConfigEnableStateChanged": sleAMConfigEnableStateChanged,
       "sleAMConfigRaiseGuardTimeChanged": sleAMConfigRaiseGuardTimeChanged,
       "sleAMConfigClearGuardTimeChanged": sleAMConfigClearGuardTimeChanged,
       "sleAMConfigLedChanged": sleAMConfigLedChanged,
       "sleAMCurrentBase": sleAMCurrentBase,
       "sleAMCurrentTable": sleAMCurrentTable,
       "sleAMCurrentEntry": sleAMCurrentEntry,
       "sleAMCurrentSeqId": sleAMCurrentSeqId,
       "sleAMCurrentAlarmSource": sleAMCurrentAlarmSource,
       "sleAMCurrentAlarmClassId": sleAMCurrentAlarmClassId,
       "sleAMCurrentAlarmId": sleAMCurrentAlarmId,
       "sleAMCurrentAlarmStatus": sleAMCurrentAlarmStatus,
       "sleAMCurrentAlarmSeverity": sleAMCurrentAlarmSeverity,
       "sleAMCurrentAlarmReason": sleAMCurrentAlarmReason,
       "sleAMCurrentTimeAndDate": sleAMCurrentTimeAndDate,
       "sleAMCurrentSpecificId": sleAMCurrentSpecificId,
       "sleAMCurrentControl": sleAMCurrentControl,
       "sleAMCurrentControlRequest": sleAMCurrentControlRequest,
       "sleAMCurrentControlStatus": sleAMCurrentControlStatus,
       "sleAMCurrentControlTimer": sleAMCurrentControlTimer,
       "sleAMCurrentControlTimeStamp": sleAMCurrentControlTimeStamp,
       "sleAMCurrentControlReqResult": sleAMCurrentControlReqResult,
       "sleAMCurrentControlSeqId": sleAMCurrentControlSeqId,
       "sleAMCurrentControlSource": sleAMCurrentControlSource,
       "sleAMCurrentNotification": sleAMCurrentNotification,
       "sleAMCurrentAlarmCleared": sleAMCurrentAlarmCleared,
       "sleAlarmTrapAlarm": sleAlarmTrapAlarm,
       "sleAlarmTrapEvent": sleAlarmTrapEvent,
       "sleAMHistoryBase": sleAMHistoryBase,
       "sleAMHistoryTable": sleAMHistoryTable,
       "sleAMHistoryEntry": sleAMHistoryEntry,
       "sleAMHistorySeqId": sleAMHistorySeqId,
       "sleAMHistoryAlarmSource": sleAMHistoryAlarmSource,
       "sleAMHistoryAlarmClassId": sleAMHistoryAlarmClassId,
       "sleAMHistoryAlarmId": sleAMHistoryAlarmId,
       "sleAMHistoryAlarmStatus": sleAMHistoryAlarmStatus,
       "sleAMHistoryAlarmSeverity": sleAMHistoryAlarmSeverity,
       "sleAMHistoryAlarmReason": sleAMHistoryAlarmReason,
       "sleAMHistoryAlarmTimeDate": sleAMHistoryAlarmTimeDate,
       "sleAMHistorySpecificId": sleAMHistorySpecificId,
       "sleAMHistoryControl": sleAMHistoryControl,
       "sleAMHistoryControlRequest": sleAMHistoryControlRequest,
       "sleAMHistoryControlStatus": sleAMHistoryControlStatus,
       "sleAMHistoryControlTimer": sleAMHistoryControlTimer,
       "sleAMHistoryControlTimeStamp": sleAMHistoryControlTimeStamp,
       "sleAMHistoryControlReqResult": sleAMHistoryControlReqResult,
       "sleAMHistoryControSeqId": sleAMHistoryControSeqId,
       "sleAMHistoryControSource": sleAMHistoryControSource,
       "sleAMHistoryNotification": sleAMHistoryNotification,
       "sleAMHistoryAlarmCleared": sleAMHistoryAlarmCleared,
       "sleAMAcoBase": sleAMAcoBase,
       "sleAMAcoInfoEntry": sleAMAcoInfoEntry,
       "sleAMAcoInfo": sleAMAcoInfo,
       "sleAMAcoControl": sleAMAcoControl,
       "sleAMAcoControlRequest": sleAMAcoControlRequest,
       "sleAMAcogControlStatus": sleAMAcogControlStatus,
       "sleAMAcoControlTimer": sleAMAcoControlTimer,
       "sleAMAcoControlTimeStamp": sleAMAcoControlTimeStamp,
       "sleAMAcoControlReqResult": sleAMAcoControlReqResult,
       "sleAMAcoControlSet": sleAMAcoControlSet,
       "sleAMAcoNotification": sleAMAcoNotification,
       "sleAMAcoChanged": sleAMAcoChanged,
       "sleAMLedBase": sleAMLedBase,
       "sleAMLedTable": sleAMLedTable,
       "sleAMLedEntry": sleAMLedEntry,
       "sleAMLedSeverity": sleAMLedSeverity,
       "sleAMLedSet": sleAMLedSet,
       "sleAMLedCount": sleAMLedCount,
       "sleAMLedControl": sleAMLedControl,
       "sleAMLedControlRequest": sleAMLedControlRequest,
       "sleAMLedControlStatus": sleAMLedControlStatus,
       "sleAMLedControlTimer": sleAMLedControlTimer,
       "sleAMLedControlTimeStamp": sleAMLedControlTimeStamp,
       "sleAMLedControlReqResult": sleAMLedControlReqResult,
       "sleAMLedControlSeverity": sleAMLedControlSeverity,
       "sleAMLedControlSet": sleAMLedControlSet,
       "sleAMLedNotification": sleAMLedNotification,
       "sleAMLedChanged": sleAMLedChanged}
)
