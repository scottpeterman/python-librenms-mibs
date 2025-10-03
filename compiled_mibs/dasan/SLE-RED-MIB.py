# SNMP MIB module (SLE-RED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-RED-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:59 2025
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


# MODULE-IDENTITY

sleRed = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22)
)


# Types definitions



class SleRedBoardIdType(Integer32):
    """Custom type SleRedBoardIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sfuA", 1),
          ("sfuB", 2))
    )





class SleRedModeType(Integer32):
    """Custom type SleRedModeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redundant", 1),
          ("standalone", 2))
    )





class SleRedFaultActionType(Integer32):
    """Custom type SleRedFaultActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("switchover", 1),
          ("log", 2),
          ("disable", 3))
    )





class SleRedReloadOSType(Integer32):
    """Custom type SleRedReloadOSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("os1", 1),
          ("os2", 2),
          ("default", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleRedBase_ObjectIdentity = ObjectIdentity
sleRedBase = _SleRedBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1)
)
_SleRedInfo_ObjectIdentity = ObjectIdentity
sleRedInfo = _SleRedInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 1)
)
_SleRedActiveBoard_Type = SleRedBoardIdType
_SleRedActiveBoard_Object = MibScalar
sleRedActiveBoard = _SleRedActiveBoard_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 1, 1),
    _SleRedActiveBoard_Type()
)
sleRedActiveBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRedActiveBoard.setStatus("current")
_SleRedMode_Type = SleRedModeType
_SleRedMode_Object = MibScalar
sleRedMode = _SleRedMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 1, 2),
    _SleRedMode_Type()
)
sleRedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRedMode.setStatus("current")
_SleRedFaultCrashAction_Type = SleRedFaultActionType
_SleRedFaultCrashAction_Object = MibScalar
sleRedFaultCrashAction = _SleRedFaultCrashAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 1, 3),
    _SleRedFaultCrashAction_Type()
)
sleRedFaultCrashAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRedFaultCrashAction.setStatus("current")
_SleRedFaultTimeoutAction_Type = SleRedFaultActionType
_SleRedFaultTimeoutAction_Object = MibScalar
sleRedFaultTimeoutAction = _SleRedFaultTimeoutAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 1, 4),
    _SleRedFaultTimeoutAction_Type()
)
sleRedFaultTimeoutAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRedFaultTimeoutAction.setStatus("current")


class _SleRedFaultTimeout_Type(Integer32):
    """Custom type sleRedFaultTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 720000),
    )


_SleRedFaultTimeout_Type.__name__ = "Integer32"
_SleRedFaultTimeout_Object = MibScalar
sleRedFaultTimeout = _SleRedFaultTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 1, 5),
    _SleRedFaultTimeout_Type()
)
sleRedFaultTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRedFaultTimeout.setStatus("current")


class _SleRedActivePrevState_Type(Integer32):
    """Custom type sleRedActivePrevState based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("activeInit", 0),
          ("singleActiveReady", 1),
          ("versionReport", 2),
          ("softwareXfer", 3),
          ("softwareXferDone", 4),
          ("configXfer", 5),
          ("configXferDone", 6),
          ("stateXfer", 7),
          ("activeReady", 8),
          ("disconnectStandby", 9),
          ("standbyWait", 10),
          ("versionCheck", 11),
          ("updateMac", 12),
          ("softwareSync", 13),
          ("softwareSyncDone", 14),
          ("configSync", 15),
          ("configSyncDone", 16),
          ("startupSync", 17),
          ("standbyReady", 18),
          ("standbyReset", 19))
    )


_SleRedActivePrevState_Type.__name__ = "Integer32"
_SleRedActivePrevState_Object = MibScalar
sleRedActivePrevState = _SleRedActivePrevState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 1, 6),
    _SleRedActivePrevState_Type()
)
sleRedActivePrevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRedActivePrevState.setStatus("current")


class _SleRedActiveCurrState_Type(Integer32):
    """Custom type sleRedActiveCurrState based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("activeInit", 0),
          ("singleActiveReady", 1),
          ("versionReport", 2),
          ("softwareXfer", 3),
          ("softwareXferDone", 4),
          ("configXfer", 5),
          ("configXferDone", 6),
          ("stateXfer", 7),
          ("activeReady", 8),
          ("disconnectStandby", 9),
          ("standbyWait", 10),
          ("versionCheck", 11),
          ("updateMac", 12),
          ("softwareSync", 13),
          ("softwareSyncDone", 14),
          ("configSync", 15),
          ("configSyncDone", 16),
          ("startupSync", 17),
          ("standbyReady", 18),
          ("standbyReset", 19))
    )


_SleRedActiveCurrState_Type.__name__ = "Integer32"
_SleRedActiveCurrState_Object = MibScalar
sleRedActiveCurrState = _SleRedActiveCurrState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 1, 7),
    _SleRedActiveCurrState_Type()
)
sleRedActiveCurrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRedActiveCurrState.setStatus("current")
_SleRedControl_ObjectIdentity = ObjectIdentity
sleRedControl = _SleRedControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2)
)


class _SleRedControlRequest_Type(Integer32):
    """Custom type sleRedControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reloadStandby", 1),
          ("switchover", 2),
          ("setFaultMonitor", 3))
    )


_SleRedControlRequest_Type.__name__ = "Integer32"
_SleRedControlRequest_Object = MibScalar
sleRedControlRequest = _SleRedControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2, 1),
    _SleRedControlRequest_Type()
)
sleRedControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRedControlRequest.setStatus("current")
_SleRedControlStatus_Type = SleControlStatusType
_SleRedControlStatus_Object = MibScalar
sleRedControlStatus = _SleRedControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2, 2),
    _SleRedControlStatus_Type()
)
sleRedControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRedControlStatus.setStatus("current")
_SleRedControlTimer_Type = Gauge32
_SleRedControlTimer_Object = MibScalar
sleRedControlTimer = _SleRedControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2, 3),
    _SleRedControlTimer_Type()
)
sleRedControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRedControlTimer.setStatus("current")
_SleRedControlTimeStamp_Type = TimeTicks
_SleRedControlTimeStamp_Object = MibScalar
sleRedControlTimeStamp = _SleRedControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2, 4),
    _SleRedControlTimeStamp_Type()
)
sleRedControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRedControlTimeStamp.setStatus("current")
_SleRedControlReqResult_Type = SleControlRequestResultType
_SleRedControlReqResult_Object = MibScalar
sleRedControlReqResult = _SleRedControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2, 5),
    _SleRedControlReqResult_Type()
)
sleRedControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRedControlReqResult.setStatus("current")
_SleRedControlReloadOS_Type = SleRedReloadOSType
_SleRedControlReloadOS_Object = MibScalar
sleRedControlReloadOS = _SleRedControlReloadOS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2, 6),
    _SleRedControlReloadOS_Type()
)
sleRedControlReloadOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRedControlReloadOS.setStatus("current")
_SleRedControlFaultCrashAction_Type = SleRedFaultActionType
_SleRedControlFaultCrashAction_Object = MibScalar
sleRedControlFaultCrashAction = _SleRedControlFaultCrashAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2, 7),
    _SleRedControlFaultCrashAction_Type()
)
sleRedControlFaultCrashAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRedControlFaultCrashAction.setStatus("current")
_SleRedControlFaultTimeoutAction_Type = SleRedFaultActionType
_SleRedControlFaultTimeoutAction_Object = MibScalar
sleRedControlFaultTimeoutAction = _SleRedControlFaultTimeoutAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2, 8),
    _SleRedControlFaultTimeoutAction_Type()
)
sleRedControlFaultTimeoutAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRedControlFaultTimeoutAction.setStatus("current")


class _SleRedControlFaultTimeout_Type(Integer32):
    """Custom type sleRedControlFaultTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 720000),
    )


_SleRedControlFaultTimeout_Type.__name__ = "Integer32"
_SleRedControlFaultTimeout_Object = MibScalar
sleRedControlFaultTimeout = _SleRedControlFaultTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2, 9),
    _SleRedControlFaultTimeout_Type()
)
sleRedControlFaultTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRedControlFaultTimeout.setStatus("current")
_SleRedNotification_ObjectIdentity = ObjectIdentity
sleRedNotification = _SleRedNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 3)
)

# Managed Objects groups

sleRedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 2)
)
sleRedGroup.setObjects(
      *(("SLE-RED-MIB", "sleRedActiveBoard"),
        ("SLE-RED-MIB", "sleRedMode"),
        ("SLE-RED-MIB", "sleRedFaultCrashAction"),
        ("SLE-RED-MIB", "sleRedFaultTimeoutAction"),
        ("SLE-RED-MIB", "sleRedFaultTimeout"),
        ("SLE-RED-MIB", "sleRedControlStatus"),
        ("SLE-RED-MIB", "sleRedControlTimer"),
        ("SLE-RED-MIB", "sleRedControlTimeStamp"),
        ("SLE-RED-MIB", "sleRedControlReqResult"),
        ("SLE-RED-MIB", "sleRedControlReloadOS"),
        ("SLE-RED-MIB", "sleRedControlFaultCrashAction"),
        ("SLE-RED-MIB", "sleRedControlFaultTimeoutAction"),
        ("SLE-RED-MIB", "sleRedActivePrevState"),
        ("SLE-RED-MIB", "sleRedActiveCurrState"),
        ("SLE-RED-MIB", "sleRedControlFaultTimeout"),
        ("SLE-RED-MIB", "sleRedControlRequest"))
)
if mibBuilder.loadTexts:
    sleRedGroup.setStatus("current")


# Notification objects

sleRedMateReloadRequested = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 3, 1)
)
sleRedMateReloadRequested.setObjects(
      *(("SLE-RED-MIB", "sleRedControlRequest"),
        ("SLE-RED-MIB", "sleRedControlTimeStamp"),
        ("SLE-RED-MIB", "sleRedControlReqResult"),
        ("SLE-RED-MIB", "sleRedActiveBoard"))
)
if mibBuilder.loadTexts:
    sleRedMateReloadRequested.setStatus(
        "current"
    )

sleRedSwitchoverRequested = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 3, 2)
)
sleRedSwitchoverRequested.setObjects(
      *(("SLE-RED-MIB", "sleRedControlRequest"),
        ("SLE-RED-MIB", "sleRedControlTimeStamp"),
        ("SLE-RED-MIB", "sleRedControlReqResult"))
)
if mibBuilder.loadTexts:
    sleRedSwitchoverRequested.setStatus(
        "current"
    )

sleRedFaultMonitorChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 3, 3)
)
sleRedFaultMonitorChanged.setObjects(
      *(("SLE-RED-MIB", "sleRedControlRequest"),
        ("SLE-RED-MIB", "sleRedControlTimeStamp"),
        ("SLE-RED-MIB", "sleRedControlReqResult"),
        ("SLE-RED-MIB", "sleRedControlFaultCrashAction"),
        ("SLE-RED-MIB", "sleRedControlFaultTimeoutAction"),
        ("SLE-RED-MIB", "sleRedControlFaultTimeout"))
)
if mibBuilder.loadTexts:
    sleRedFaultMonitorChanged.setStatus(
        "current"
    )


# Notifications groups

sleRedNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 22, 3)
)
sleRedNotificationGroup.setObjects(
      *(("SLE-RED-MIB", "sleRedMateReloadRequested"),
        ("SLE-RED-MIB", "sleRedSwitchoverRequested"),
        ("SLE-RED-MIB", "sleRedFaultMonitorChanged"))
)
if mibBuilder.loadTexts:
    sleRedNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-RED-MIB",
    **{"SleRedBoardIdType": SleRedBoardIdType,
       "SleRedModeType": SleRedModeType,
       "SleRedFaultActionType": SleRedFaultActionType,
       "SleRedReloadOSType": SleRedReloadOSType,
       "sleRed": sleRed,
       "sleRedBase": sleRedBase,
       "sleRedInfo": sleRedInfo,
       "sleRedActiveBoard": sleRedActiveBoard,
       "sleRedMode": sleRedMode,
       "sleRedFaultCrashAction": sleRedFaultCrashAction,
       "sleRedFaultTimeoutAction": sleRedFaultTimeoutAction,
       "sleRedFaultTimeout": sleRedFaultTimeout,
       "sleRedActivePrevState": sleRedActivePrevState,
       "sleRedActiveCurrState": sleRedActiveCurrState,
       "sleRedControl": sleRedControl,
       "sleRedControlRequest": sleRedControlRequest,
       "sleRedControlStatus": sleRedControlStatus,
       "sleRedControlTimer": sleRedControlTimer,
       "sleRedControlTimeStamp": sleRedControlTimeStamp,
       "sleRedControlReqResult": sleRedControlReqResult,
       "sleRedControlReloadOS": sleRedControlReloadOS,
       "sleRedControlFaultCrashAction": sleRedControlFaultCrashAction,
       "sleRedControlFaultTimeoutAction": sleRedControlFaultTimeoutAction,
       "sleRedControlFaultTimeout": sleRedControlFaultTimeout,
       "sleRedNotification": sleRedNotification,
       "sleRedMateReloadRequested": sleRedMateReloadRequested,
       "sleRedSwitchoverRequested": sleRedSwitchoverRequested,
       "sleRedFaultMonitorChanged": sleRedFaultMonitorChanged,
       "sleRedGroup": sleRedGroup,
       "sleRedNotificationGroup": sleRedNotificationGroup}
)
