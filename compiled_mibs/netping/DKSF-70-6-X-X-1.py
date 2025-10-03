# SNMP MIB module (DKSF-70-6-X-X-1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\netping\DKSF-70-6-X-X-1
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:56 2025
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

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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

uniPingServerSolutionV3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 70)
)
if mibBuilder.loadTexts:
    uniPingServerSolutionV3.setRevisions(
        ("2016-08-24 00:00",
         "2015-07-14 00:00",
         "2015-05-29 00:00",
         "2014-12-03 00:00",
         "2014-11-26 00:00",
         "2014-02-02 00:00",
         "2014-01-29 00:00",
         "2014-01-21 00:00",
         "2013-04-11 00:00",
         "2012-05-31 00:00",
         "2012-04-17 00:00",
         "2012-03-23 00:00",
         "2011-09-23 00:00",
         "2011-03-24 00:00",
         "2010-10-14 00:00",
         "2010-09-20 00:00",
         "2010-05-31 00:00",
         "2010-04-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FixedPoint1000(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


# MIB Managed Objects in the order of their OIDs

_Lightcom_ObjectIdentity = ObjectIdentity
lightcom = _Lightcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728)
)
_NpTrapInfo_ObjectIdentity = ObjectIdentity
npTrapInfo = _NpTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 90)
)
_NpTrapEmailTo_Type = DisplayString
_NpTrapEmailTo_Object = MibScalar
npTrapEmailTo = _NpTrapEmailTo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 90, 1),
    _NpTrapEmailTo_Type()
)
npTrapEmailTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npTrapEmailTo.setStatus("current")
_NpReboot_ObjectIdentity = ObjectIdentity
npReboot = _NpReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 911)
)
_NpSoftReboot_Type = Integer32
_NpSoftReboot_Object = MibScalar
npSoftReboot = _NpSoftReboot_Object(
    (1, 3, 6, 1, 4, 1, 25728, 911, 1),
    _NpSoftReboot_Type()
)
npSoftReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSoftReboot.setStatus("current")
_NpResetStack_Type = Integer32
_NpResetStack_Object = MibScalar
npResetStack = _NpResetStack_Object(
    (1, 3, 6, 1, 4, 1, 25728, 911, 2),
    _NpResetStack_Type()
)
npResetStack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npResetStack.setStatus("current")
_NpForcedReboot_Type = Integer32
_NpForcedReboot_Object = MibScalar
npForcedReboot = _NpForcedReboot_Object(
    (1, 3, 6, 1, 4, 1, 25728, 911, 3),
    _NpForcedReboot_Type()
)
npForcedReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npForcedReboot.setStatus("current")
_NpGsm_ObjectIdentity = ObjectIdentity
npGsm = _NpGsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 3800)
)
_NpGsmInfo_ObjectIdentity = ObjectIdentity
npGsmInfo = _NpGsmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1)
)


class _NpGsmFailed_Type(Integer32):
    """Custom type npGsmFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("failed", 1),
          ("fatalError", 2))
    )


_NpGsmFailed_Type.__name__ = "Integer32"
_NpGsmFailed_Object = MibScalar
npGsmFailed = _NpGsmFailed_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 1),
    _NpGsmFailed_Type()
)
npGsmFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npGsmFailed.setStatus("current")


class _NpGsmRegistration_Type(Integer32):
    """Custom type npGsmRegistration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("impossible", 0),
          ("homeNetwork", 1),
          ("searching", 2),
          ("denied", 3),
          ("unknown", 4),
          ("roaming", 5),
          ("infoUpdate", 255))
    )


_NpGsmRegistration_Type.__name__ = "Integer32"
_NpGsmRegistration_Object = MibScalar
npGsmRegistration = _NpGsmRegistration_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 2),
    _NpGsmRegistration_Type()
)
npGsmRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npGsmRegistration.setStatus("current")


class _NpGsmStrength_Type(Integer32):
    """Custom type npGsmStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NpGsmStrength_Type.__name__ = "Integer32"
_NpGsmStrength_Object = MibScalar
npGsmStrength = _NpGsmStrength_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 3),
    _NpGsmStrength_Type()
)
npGsmStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npGsmStrength.setStatus("current")
_NpGsmSendSmsUtf8_Type = DisplayString
_NpGsmSendSmsUtf8_Object = MibScalar
npGsmSendSmsUtf8 = _NpGsmSendSmsUtf8_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 9),
    _NpGsmSendSmsUtf8_Type()
)
npGsmSendSmsUtf8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npGsmSendSmsUtf8.setStatus("current")
_NpGsmSendSmsWin1251_Type = DisplayString
_NpGsmSendSmsWin1251_Object = MibScalar
npGsmSendSmsWin1251 = _NpGsmSendSmsWin1251_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 10),
    _NpGsmSendSmsWin1251_Type()
)
npGsmSendSmsWin1251.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npGsmSendSmsWin1251.setStatus("current")
_NpGsmTraps_ObjectIdentity = ObjectIdentity
npGsmTraps = _NpGsmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 2)
)
_NpGsmTrapPrefix_ObjectIdentity = ObjectIdentity
npGsmTrapPrefix = _NpGsmTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 2, 0)
)
_NpRelay_ObjectIdentity = ObjectIdentity
npRelay = _NpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 5500)
)
_NpRelayTable_Object = MibTable
npRelayTable = _NpRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5)
)
if mibBuilder.loadTexts:
    npRelayTable.setStatus("current")
_NpRelayEntry_Object = MibTableRow
npRelayEntry = _NpRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1)
)
npRelayEntry.setIndexNames(
    (0, "DKSF-70-6-X-X-1", "npRelayN"),
)
if mibBuilder.loadTexts:
    npRelayEntry.setStatus("current")


class _NpRelayN_Type(Integer32):
    """Custom type npRelayN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_NpRelayN_Type.__name__ = "Integer32"
_NpRelayN_Object = MibTableColumn
npRelayN = _NpRelayN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 1),
    _NpRelayN_Type()
)
npRelayN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelayN.setStatus("current")


class _NpRelayMode_Type(Integer32):
    """Custom type npRelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("flip", -1),
          ("off", 0),
          ("on", 1),
          ("watchdog", 2),
          ("schedule", 3),
          ("scheduleAndWatchdog", 4),
          ("logic", 5))
    )


_NpRelayMode_Type.__name__ = "Integer32"
_NpRelayMode_Object = MibTableColumn
npRelayMode = _NpRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 2),
    _NpRelayMode_Type()
)
npRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npRelayMode.setStatus("current")
_NpRelayStartReset_Type = Integer32
_NpRelayStartReset_Object = MibTableColumn
npRelayStartReset = _NpRelayStartReset_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 3),
    _NpRelayStartReset_Type()
)
npRelayStartReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npRelayStartReset.setStatus("current")
_NpRelayMemo_Type = DisplayString
_NpRelayMemo_Object = MibTableColumn
npRelayMemo = _NpRelayMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 6),
    _NpRelayMemo_Type()
)
npRelayMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelayMemo.setStatus("current")


class _NpRelayState_Type(Integer32):
    """Custom type npRelayState based on Integer32"""
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


_NpRelayState_Type.__name__ = "Integer32"
_NpRelayState_Object = MibTableColumn
npRelayState = _NpRelayState_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 15),
    _NpRelayState_Type()
)
npRelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelayState.setStatus("current")
_NpIr_ObjectIdentity = ObjectIdentity
npIr = _NpIr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 7900)
)
_NpIrCtrl_ObjectIdentity = ObjectIdentity
npIrCtrl = _NpIrCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 7900, 1)
)


class _NpIrPlayCmd_Type(Integer32):
    """Custom type npIrPlayCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NpIrPlayCmd_Type.__name__ = "Integer32"
_NpIrPlayCmd_Object = MibScalar
npIrPlayCmd = _NpIrPlayCmd_Object(
    (1, 3, 6, 1, 4, 1, 25728, 7900, 1, 1),
    _NpIrPlayCmd_Type()
)
npIrPlayCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIrPlayCmd.setStatus("current")


class _NpIrReset_Type(Integer32):
    """Custom type npIrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpIrReset_Type.__name__ = "Integer32"
_NpIrReset_Object = MibScalar
npIrReset = _NpIrReset_Object(
    (1, 3, 6, 1, 4, 1, 25728, 7900, 1, 2),
    _NpIrReset_Type()
)
npIrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIrReset.setStatus("current")


class _NpIrStatus_Type(Integer32):
    """Custom type npIrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("commandCompleted", 0),
          ("protocolError", 1),
          ("commandAccepted", 2),
          ("errorUnknown", 16),
          ("errorBadNumber", 17),
          ("errorEmptyRecord", 18),
          ("errorFlashChip", 19),
          ("errorTimeout", 20),
          ("errorExtBusBusy", 21))
    )


_NpIrStatus_Type.__name__ = "Integer32"
_NpIrStatus_Object = MibScalar
npIrStatus = _NpIrStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 7900, 1, 3),
    _NpIrStatus_Type()
)
npIrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIrStatus.setStatus("current")
_NpSmoke_ObjectIdentity = ObjectIdentity
npSmoke = _NpSmoke_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8200)
)
_NpSmokeTable_Object = MibTable
npSmokeTable = _NpSmokeTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1)
)
if mibBuilder.loadTexts:
    npSmokeTable.setStatus("current")
_NpSmokeEntry_Object = MibTableRow
npSmokeEntry = _NpSmokeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1)
)
npSmokeEntry.setIndexNames(
    (0, "DKSF-70-6-X-X-1", "npSmokeSensorN"),
)
if mibBuilder.loadTexts:
    npSmokeEntry.setStatus("current")


class _NpSmokeSensorN_Type(Integer32):
    """Custom type npSmokeSensorN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NpSmokeSensorN_Type.__name__ = "Integer32"
_NpSmokeSensorN_Object = MibTableColumn
npSmokeSensorN = _NpSmokeSensorN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 1),
    _NpSmokeSensorN_Type()
)
npSmokeSensorN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSmokeSensorN.setStatus("current")


class _NpSmokeStatus_Type(Integer32):
    """Custom type npSmokeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("alarm", 1),
          ("off", 4),
          ("failed", 5))
    )


_NpSmokeStatus_Type.__name__ = "Integer32"
_NpSmokeStatus_Object = MibTableColumn
npSmokeStatus = _NpSmokeStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 2),
    _NpSmokeStatus_Type()
)
npSmokeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSmokeStatus.setStatus("current")


class _NpSmokePower_Type(Integer32):
    """Custom type npSmokePower based on Integer32"""
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


_NpSmokePower_Type.__name__ = "Integer32"
_NpSmokePower_Object = MibTableColumn
npSmokePower = _NpSmokePower_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 3),
    _NpSmokePower_Type()
)
npSmokePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSmokePower.setStatus("current")
_NpSmokeReset_Type = Integer32
_NpSmokeReset_Object = MibTableColumn
npSmokeReset = _NpSmokeReset_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 4),
    _NpSmokeReset_Type()
)
npSmokeReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSmokeReset.setStatus("current")
_NpSmokeMemo_Type = DisplayString
_NpSmokeMemo_Object = MibTableColumn
npSmokeMemo = _NpSmokeMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 6),
    _NpSmokeMemo_Type()
)
npSmokeMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSmokeMemo.setStatus("current")
_NpSmokeTraps_ObjectIdentity = ObjectIdentity
npSmokeTraps = _NpSmokeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2)
)
_NpSmokeTrapPrefix_ObjectIdentity = ObjectIdentity
npSmokeTrapPrefix = _NpSmokeTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2, 0)
)


class _NpSmokeTrapSensorN_Type(Integer32):
    """Custom type npSmokeTrapSensorN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NpSmokeTrapSensorN_Type.__name__ = "Integer32"
_NpSmokeTrapSensorN_Object = MibScalar
npSmokeTrapSensorN = _NpSmokeTrapSensorN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2, 1),
    _NpSmokeTrapSensorN_Type()
)
npSmokeTrapSensorN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSmokeTrapSensorN.setStatus("current")


class _NpSmokeTrapStatus_Type(Integer32):
    """Custom type npSmokeTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("alarm", 1),
          ("off", 4),
          ("failed", 5))
    )


_NpSmokeTrapStatus_Type.__name__ = "Integer32"
_NpSmokeTrapStatus_Object = MibScalar
npSmokeTrapStatus = _NpSmokeTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2, 2),
    _NpSmokeTrapStatus_Type()
)
npSmokeTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSmokeTrapStatus.setStatus("current")
_NpSmokeTrapMemo_Type = DisplayString
_NpSmokeTrapMemo_Object = MibScalar
npSmokeTrapMemo = _NpSmokeTrapMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2, 6),
    _NpSmokeTrapMemo_Type()
)
npSmokeTrapMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSmokeTrapMemo.setStatus("current")
_NpCurLoop_ObjectIdentity = ObjectIdentity
npCurLoop = _NpCurLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8300)
)
_NpCurLoopTable_Object = MibTable
npCurLoopTable = _NpCurLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1)
)
if mibBuilder.loadTexts:
    npCurLoopTable.setStatus("current")
_NpCurLoopEntry_Object = MibTableRow
npCurLoopEntry = _NpCurLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1)
)
npCurLoopEntry.setIndexNames(
    (0, "DKSF-70-6-X-X-1", "npCurLoopN"),
)
if mibBuilder.loadTexts:
    npCurLoopEntry.setStatus("current")


class _NpCurLoopN_Type(Integer32):
    """Custom type npCurLoopN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpCurLoopN_Type.__name__ = "Integer32"
_NpCurLoopN_Object = MibTableColumn
npCurLoopN = _NpCurLoopN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 1),
    _NpCurLoopN_Type()
)
npCurLoopN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopN.setStatus("current")


class _NpCurLoopStatus_Type(Integer32):
    """Custom type npCurLoopStatus based on Integer32"""
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
        *(("ok", 0),
          ("alert", 1),
          ("cut", 2),
          ("short", 3),
          ("notPowered", 4))
    )


_NpCurLoopStatus_Type.__name__ = "Integer32"
_NpCurLoopStatus_Object = MibTableColumn
npCurLoopStatus = _NpCurLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 2),
    _NpCurLoopStatus_Type()
)
npCurLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopStatus.setStatus("current")


class _NpCurLoopI_Type(Integer32):
    """Custom type npCurLoopI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopI_Type.__name__ = "Integer32"
_NpCurLoopI_Object = MibTableColumn
npCurLoopI = _NpCurLoopI_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 3),
    _NpCurLoopI_Type()
)
npCurLoopI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopI.setStatus("current")


class _NpCurLoopV_Type(Integer32):
    """Custom type npCurLoopV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopV_Type.__name__ = "Integer32"
_NpCurLoopV_Object = MibTableColumn
npCurLoopV = _NpCurLoopV_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 4),
    _NpCurLoopV_Type()
)
npCurLoopV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopV.setStatus("current")


class _NpCurLoopR_Type(Integer32):
    """Custom type npCurLoopR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopR_Type.__name__ = "Integer32"
_NpCurLoopR_Object = MibTableColumn
npCurLoopR = _NpCurLoopR_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 5),
    _NpCurLoopR_Type()
)
npCurLoopR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopR.setStatus("current")


class _NpCurLoopPower_Type(Integer32):
    """Custom type npCurLoopPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("cyclePower", 2))
    )


_NpCurLoopPower_Type.__name__ = "Integer32"
_NpCurLoopPower_Object = MibTableColumn
npCurLoopPower = _NpCurLoopPower_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 7),
    _NpCurLoopPower_Type()
)
npCurLoopPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCurLoopPower.setStatus("current")
_NpCurLoopTraps_ObjectIdentity = ObjectIdentity
npCurLoopTraps = _NpCurLoopTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2)
)
_NpCurLoopTrapPrefix_ObjectIdentity = ObjectIdentity
npCurLoopTrapPrefix = _NpCurLoopTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 0)
)


class _NpCurLoopTrapN_Type(Integer32):
    """Custom type npCurLoopTrapN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpCurLoopTrapN_Type.__name__ = "Integer32"
_NpCurLoopTrapN_Object = MibScalar
npCurLoopTrapN = _NpCurLoopTrapN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 1),
    _NpCurLoopTrapN_Type()
)
npCurLoopTrapN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopTrapN.setStatus("current")


class _NpCurLoopTrapStatus_Type(Integer32):
    """Custom type npCurLoopTrapStatus based on Integer32"""
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
        *(("ok", 0),
          ("alert", 1),
          ("cut", 2),
          ("short", 3),
          ("notPowered", 4))
    )


_NpCurLoopTrapStatus_Type.__name__ = "Integer32"
_NpCurLoopTrapStatus_Object = MibScalar
npCurLoopTrapStatus = _NpCurLoopTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 2),
    _NpCurLoopTrapStatus_Type()
)
npCurLoopTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopTrapStatus.setStatus("current")


class _NpCurLoopTrapI_Type(Integer32):
    """Custom type npCurLoopTrapI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopTrapI_Type.__name__ = "Integer32"
_NpCurLoopTrapI_Object = MibScalar
npCurLoopTrapI = _NpCurLoopTrapI_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 3),
    _NpCurLoopTrapI_Type()
)
npCurLoopTrapI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopTrapI.setStatus("current")


class _NpCurLoopTrapV_Type(Integer32):
    """Custom type npCurLoopTrapV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopTrapV_Type.__name__ = "Integer32"
_NpCurLoopTrapV_Object = MibScalar
npCurLoopTrapV = _NpCurLoopTrapV_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 4),
    _NpCurLoopTrapV_Type()
)
npCurLoopTrapV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopTrapV.setStatus("current")


class _NpCurLoopTrapR_Type(Integer32):
    """Custom type npCurLoopTrapR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopTrapR_Type.__name__ = "Integer32"
_NpCurLoopTrapR_Object = MibScalar
npCurLoopTrapR = _NpCurLoopTrapR_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 5),
    _NpCurLoopTrapR_Type()
)
npCurLoopTrapR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopTrapR.setStatus("current")


class _NpCurLoopTrapPower_Type(Integer32):
    """Custom type npCurLoopTrapPower based on Integer32"""
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


_NpCurLoopTrapPower_Type.__name__ = "Integer32"
_NpCurLoopTrapPower_Object = MibScalar
npCurLoopTrapPower = _NpCurLoopTrapPower_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 7),
    _NpCurLoopTrapPower_Type()
)
npCurLoopTrapPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCurLoopTrapPower.setStatus("current")
_NpRelHumidity_ObjectIdentity = ObjectIdentity
npRelHumidity = _NpRelHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8400)
)
_NpRelHumTable_Object = MibTable
npRelHumTable = _NpRelHumTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1)
)
if mibBuilder.loadTexts:
    npRelHumTable.setStatus("current")
_NpRelHumEntry_Object = MibTableRow
npRelHumEntry = _NpRelHumEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1)
)
npRelHumEntry.setIndexNames(
    (0, "DKSF-70-6-X-X-1", "npRelHumN"),
)
if mibBuilder.loadTexts:
    npRelHumEntry.setStatus("current")


class _NpRelHumN_Type(Integer32):
    """Custom type npRelHumN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NpRelHumN_Type.__name__ = "Integer32"
_NpRelHumN_Object = MibTableColumn
npRelHumN = _NpRelHumN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 1),
    _NpRelHumN_Type()
)
npRelHumN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumN.setStatus("current")


class _NpRelHumValue_Type(Integer32):
    """Custom type npRelHumValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NpRelHumValue_Type.__name__ = "Integer32"
_NpRelHumValue_Object = MibTableColumn
npRelHumValue = _NpRelHumValue_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 2),
    _NpRelHumValue_Type()
)
npRelHumValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumValue.setStatus("current")


class _NpRelHumStatus_Type(Integer32):
    """Custom type npRelHumStatus based on Integer32"""
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
        *(("sensorFailed", 0),
          ("belowSafeRange", 1),
          ("inSafeRange", 2),
          ("aboveSafeRange", 3))
    )


_NpRelHumStatus_Type.__name__ = "Integer32"
_NpRelHumStatus_Object = MibTableColumn
npRelHumStatus = _NpRelHumStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 3),
    _NpRelHumStatus_Type()
)
npRelHumStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumStatus.setStatus("current")


class _NpRelHumTempValue_Type(Integer32):
    """Custom type npRelHumTempValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 200),
    )


_NpRelHumTempValue_Type.__name__ = "Integer32"
_NpRelHumTempValue_Object = MibTableColumn
npRelHumTempValue = _NpRelHumTempValue_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 4),
    _NpRelHumTempValue_Type()
)
npRelHumTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTempValue.setStatus("current")


class _NpRelHumTempStatus_Type(Integer32):
    """Custom type npRelHumTempStatus based on Integer32"""
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
        *(("sensorFailed", 0),
          ("belowSafeRange", 1),
          ("inSafeRange", 2),
          ("aboveSafeRange", 3))
    )


_NpRelHumTempStatus_Type.__name__ = "Integer32"
_NpRelHumTempStatus_Object = MibTableColumn
npRelHumTempStatus = _NpRelHumTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 5),
    _NpRelHumTempStatus_Type()
)
npRelHumTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTempStatus.setStatus("current")
_NpRelHumMemo_Type = DisplayString
_NpRelHumMemo_Object = MibTableColumn
npRelHumMemo = _NpRelHumMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 6),
    _NpRelHumMemo_Type()
)
npRelHumMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumMemo.setStatus("current")


class _NpRelHumSafeRangeHigh_Type(Integer32):
    """Custom type npRelHumSafeRangeHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NpRelHumSafeRangeHigh_Type.__name__ = "Integer32"
_NpRelHumSafeRangeHigh_Object = MibTableColumn
npRelHumSafeRangeHigh = _NpRelHumSafeRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 7),
    _NpRelHumSafeRangeHigh_Type()
)
npRelHumSafeRangeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumSafeRangeHigh.setStatus("current")


class _NpRelHumSafeRangeLow_Type(Integer32):
    """Custom type npRelHumSafeRangeLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NpRelHumSafeRangeLow_Type.__name__ = "Integer32"
_NpRelHumSafeRangeLow_Object = MibTableColumn
npRelHumSafeRangeLow = _NpRelHumSafeRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 8),
    _NpRelHumSafeRangeLow_Type()
)
npRelHumSafeRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumSafeRangeLow.setStatus("current")


class _NpRelHumTempSafeRangeHigh_Type(Integer32):
    """Custom type npRelHumTempSafeRangeHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-55, 150),
    )


_NpRelHumTempSafeRangeHigh_Type.__name__ = "Integer32"
_NpRelHumTempSafeRangeHigh_Object = MibTableColumn
npRelHumTempSafeRangeHigh = _NpRelHumTempSafeRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 9),
    _NpRelHumTempSafeRangeHigh_Type()
)
npRelHumTempSafeRangeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTempSafeRangeHigh.setStatus("current")


class _NpRelHumTempSafeRangeLow_Type(Integer32):
    """Custom type npRelHumTempSafeRangeLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-55, 150),
    )


_NpRelHumTempSafeRangeLow_Type.__name__ = "Integer32"
_NpRelHumTempSafeRangeLow_Object = MibTableColumn
npRelHumTempSafeRangeLow = _NpRelHumTempSafeRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 10),
    _NpRelHumTempSafeRangeLow_Type()
)
npRelHumTempSafeRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTempSafeRangeLow.setStatus("current")
_NpRelHumTrapData_ObjectIdentity = ObjectIdentity
npRelHumTrapData = _NpRelHumTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 3)
)


class _NpRelHumTrapDataN_Type(Integer32):
    """Custom type npRelHumTrapDataN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NpRelHumTrapDataN_Type.__name__ = "Integer32"
_NpRelHumTrapDataN_Object = MibScalar
npRelHumTrapDataN = _NpRelHumTrapDataN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 3, 1),
    _NpRelHumTrapDataN_Type()
)
npRelHumTrapDataN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTrapDataN.setStatus("current")
_NpRelHumTrapDataValue_Type = Integer32
_NpRelHumTrapDataValue_Object = MibScalar
npRelHumTrapDataValue = _NpRelHumTrapDataValue_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 3, 2),
    _NpRelHumTrapDataValue_Type()
)
npRelHumTrapDataValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTrapDataValue.setStatus("current")


class _NpRelHumTrapDataStatus_Type(Integer32):
    """Custom type npRelHumTrapDataStatus based on Integer32"""
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
        *(("sensorFailed", 0),
          ("belowSafeRange", 1),
          ("inSafeRange", 2),
          ("aboveSafeRange", 3))
    )


_NpRelHumTrapDataStatus_Type.__name__ = "Integer32"
_NpRelHumTrapDataStatus_Object = MibScalar
npRelHumTrapDataStatus = _NpRelHumTrapDataStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 3, 4),
    _NpRelHumTrapDataStatus_Type()
)
npRelHumTrapDataStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTrapDataStatus.setStatus("current")
_NpRelHumTrapDataMemo_Type = DisplayString
_NpRelHumTrapDataMemo_Object = MibScalar
npRelHumTrapDataMemo = _NpRelHumTrapDataMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 3, 6),
    _NpRelHumTrapDataMemo_Type()
)
npRelHumTrapDataMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTrapDataMemo.setStatus("current")
_NpRelHumTrapDataSafeRangeHigh_Type = Integer32
_NpRelHumTrapDataSafeRangeHigh_Object = MibScalar
npRelHumTrapDataSafeRangeHigh = _NpRelHumTrapDataSafeRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 3, 7),
    _NpRelHumTrapDataSafeRangeHigh_Type()
)
npRelHumTrapDataSafeRangeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTrapDataSafeRangeHigh.setStatus("current")
_NpRelHumTrapDataSafeRangeLow_Type = Integer32
_NpRelHumTrapDataSafeRangeLow_Object = MibScalar
npRelHumTrapDataSafeRangeLow = _NpRelHumTrapDataSafeRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 3, 8),
    _NpRelHumTrapDataSafeRangeLow_Type()
)
npRelHumTrapDataSafeRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTrapDataSafeRangeLow.setStatus("current")
_NpRelHumTrap_ObjectIdentity = ObjectIdentity
npRelHumTrap = _NpRelHumTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 6)
)
_NpRelHumTrapAllEvents_ObjectIdentity = ObjectIdentity
npRelHumTrapAllEvents = _NpRelHumTrapAllEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 6, 127)
)
_NpRelHumTrapTemp_ObjectIdentity = ObjectIdentity
npRelHumTrapTemp = _NpRelHumTrapTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 7)
)
_NpRelHumTrapTempAllEvents_ObjectIdentity = ObjectIdentity
npRelHumTrapTempAllEvents = _NpRelHumTrapTempAllEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 7, 127)
)
_NpThermo_ObjectIdentity = ObjectIdentity
npThermo = _NpThermo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8800)
)
_NpThermoTable_Object = MibTable
npThermoTable = _NpThermoTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1)
)
if mibBuilder.loadTexts:
    npThermoTable.setStatus("current")
_NpThermoEntry_Object = MibTableRow
npThermoEntry = _NpThermoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1)
)
npThermoEntry.setIndexNames(
    (0, "DKSF-70-6-X-X-1", "npThermoSensorN"),
)
if mibBuilder.loadTexts:
    npThermoEntry.setStatus("current")


class _NpThermoSensorN_Type(Integer32):
    """Custom type npThermoSensorN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpThermoSensorN_Type.__name__ = "Integer32"
_NpThermoSensorN_Object = MibTableColumn
npThermoSensorN = _NpThermoSensorN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 1),
    _NpThermoSensorN_Type()
)
npThermoSensorN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoSensorN.setStatus("current")


class _NpThermoValue_Type(Integer32):
    """Custom type npThermoValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoValue_Type.__name__ = "Integer32"
_NpThermoValue_Object = MibTableColumn
npThermoValue = _NpThermoValue_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 2),
    _NpThermoValue_Type()
)
npThermoValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoValue.setStatus("current")


class _NpThermoStatus_Type(Integer32):
    """Custom type npThermoStatus based on Integer32"""
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
        *(("failed", 0),
          ("low", 1),
          ("norm", 2),
          ("high", 3))
    )


_NpThermoStatus_Type.__name__ = "Integer32"
_NpThermoStatus_Object = MibTableColumn
npThermoStatus = _NpThermoStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 3),
    _NpThermoStatus_Type()
)
npThermoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoStatus.setStatus("current")


class _NpThermoLow_Type(Integer32):
    """Custom type npThermoLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoLow_Type.__name__ = "Integer32"
_NpThermoLow_Object = MibTableColumn
npThermoLow = _NpThermoLow_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 4),
    _NpThermoLow_Type()
)
npThermoLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoLow.setStatus("current")


class _NpThermoHigh_Type(Integer32):
    """Custom type npThermoHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoHigh_Type.__name__ = "Integer32"
_NpThermoHigh_Object = MibTableColumn
npThermoHigh = _NpThermoHigh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 5),
    _NpThermoHigh_Type()
)
npThermoHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoHigh.setStatus("current")
_NpThermoMemo_Type = DisplayString
_NpThermoMemo_Object = MibTableColumn
npThermoMemo = _NpThermoMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 6),
    _NpThermoMemo_Type()
)
npThermoMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoMemo.setStatus("current")
_NpThermoValuePrecise_Type = FixedPoint1000
_NpThermoValuePrecise_Object = MibTableColumn
npThermoValuePrecise = _NpThermoValuePrecise_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 7),
    _NpThermoValuePrecise_Type()
)
npThermoValuePrecise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoValuePrecise.setStatus("current")
_NpThermoTraps_ObjectIdentity = ObjectIdentity
npThermoTraps = _NpThermoTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2)
)
_NpThermoTrapPrefix_ObjectIdentity = ObjectIdentity
npThermoTrapPrefix = _NpThermoTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 0)
)


class _NpThermoTrapSensorN_Type(Integer32):
    """Custom type npThermoTrapSensorN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpThermoTrapSensorN_Type.__name__ = "Integer32"
_NpThermoTrapSensorN_Object = MibScalar
npThermoTrapSensorN = _NpThermoTrapSensorN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 1),
    _NpThermoTrapSensorN_Type()
)
npThermoTrapSensorN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoTrapSensorN.setStatus("current")


class _NpThermoTrapValue_Type(Integer32):
    """Custom type npThermoTrapValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoTrapValue_Type.__name__ = "Integer32"
_NpThermoTrapValue_Object = MibScalar
npThermoTrapValue = _NpThermoTrapValue_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 2),
    _NpThermoTrapValue_Type()
)
npThermoTrapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoTrapValue.setStatus("current")


class _NpThermoTrapStatus_Type(Integer32):
    """Custom type npThermoTrapStatus based on Integer32"""
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
        *(("failed", 0),
          ("low", 1),
          ("norm", 2),
          ("high", 3))
    )


_NpThermoTrapStatus_Type.__name__ = "Integer32"
_NpThermoTrapStatus_Object = MibScalar
npThermoTrapStatus = _NpThermoTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 3),
    _NpThermoTrapStatus_Type()
)
npThermoTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoTrapStatus.setStatus("current")


class _NpThermoTrapLow_Type(Integer32):
    """Custom type npThermoTrapLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoTrapLow_Type.__name__ = "Integer32"
_NpThermoTrapLow_Object = MibScalar
npThermoTrapLow = _NpThermoTrapLow_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 4),
    _NpThermoTrapLow_Type()
)
npThermoTrapLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoTrapLow.setStatus("current")


class _NpThermoTrapHigh_Type(Integer32):
    """Custom type npThermoTrapHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoTrapHigh_Type.__name__ = "Integer32"
_NpThermoTrapHigh_Object = MibScalar
npThermoTrapHigh = _NpThermoTrapHigh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 5),
    _NpThermoTrapHigh_Type()
)
npThermoTrapHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoTrapHigh.setStatus("current")
_NpThermoTrapMemo_Type = DisplayString
_NpThermoTrapMemo_Object = MibScalar
npThermoTrapMemo = _NpThermoTrapMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 6),
    _NpThermoTrapMemo_Type()
)
npThermoTrapMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoTrapMemo.setStatus("current")
_NpIo_ObjectIdentity = ObjectIdentity
npIo = _NpIo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8900)
)
_NpIoTable_Object = MibTable
npIoTable = _NpIoTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1)
)
if mibBuilder.loadTexts:
    npIoTable.setStatus("current")
_NpIoEntry_Object = MibTableRow
npIoEntry = _NpIoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1)
)
npIoEntry.setIndexNames(
    (0, "DKSF-70-6-X-X-1", "npIoLineN"),
)
if mibBuilder.loadTexts:
    npIoEntry.setStatus("current")


class _NpIoLineN_Type(Integer32):
    """Custom type npIoLineN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpIoLineN_Type.__name__ = "Integer32"
_NpIoLineN_Object = MibTableColumn
npIoLineN = _NpIoLineN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 1),
    _NpIoLineN_Type()
)
npIoLineN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoLineN.setStatus("current")


class _NpIoLevelIn_Type(Integer32):
    """Custom type npIoLevelIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpIoLevelIn_Type.__name__ = "Integer32"
_NpIoLevelIn_Object = MibTableColumn
npIoLevelIn = _NpIoLevelIn_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 2),
    _NpIoLevelIn_Type()
)
npIoLevelIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoLevelIn.setStatus("current")


class _NpIoLevelOut_Type(Integer32):
    """Custom type npIoLevelOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("flip", -1),
          ("low", 0),
          ("high", 1))
    )


_NpIoLevelOut_Type.__name__ = "Integer32"
_NpIoLevelOut_Object = MibTableColumn
npIoLevelOut = _NpIoLevelOut_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 3),
    _NpIoLevelOut_Type()
)
npIoLevelOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIoLevelOut.setStatus("current")
_NpIoMemo_Type = DisplayString
_NpIoMemo_Object = MibTableColumn
npIoMemo = _NpIoMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 6),
    _NpIoMemo_Type()
)
npIoMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoMemo.setStatus("current")
_NpIoPulseCounter_Type = Counter32
_NpIoPulseCounter_Object = MibTableColumn
npIoPulseCounter = _NpIoPulseCounter_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 9),
    _NpIoPulseCounter_Type()
)
npIoPulseCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIoPulseCounter.setStatus("current")


class _NpIoSinglePulseDuration_Type(Integer32):
    """Custom type npIoSinglePulseDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 25500),
    )


_NpIoSinglePulseDuration_Type.__name__ = "Integer32"
_NpIoSinglePulseDuration_Object = MibTableColumn
npIoSinglePulseDuration = _NpIoSinglePulseDuration_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 12),
    _NpIoSinglePulseDuration_Type()
)
npIoSinglePulseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIoSinglePulseDuration.setStatus("current")
_NpIoSinglePulseStart_Type = Integer32
_NpIoSinglePulseStart_Object = MibTableColumn
npIoSinglePulseStart = _NpIoSinglePulseStart_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 13),
    _NpIoSinglePulseStart_Type()
)
npIoSinglePulseStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIoSinglePulseStart.setStatus("current")
_NpIoTraps_ObjectIdentity = ObjectIdentity
npIoTraps = _NpIoTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2)
)
_NpIoTrapPrefix_ObjectIdentity = ObjectIdentity
npIoTrapPrefix = _NpIoTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 0)
)


class _NpIoTrapLineN_Type(Integer32):
    """Custom type npIoTrapLineN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_NpIoTrapLineN_Type.__name__ = "Integer32"
_NpIoTrapLineN_Object = MibScalar
npIoTrapLineN = _NpIoTrapLineN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 1),
    _NpIoTrapLineN_Type()
)
npIoTrapLineN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapLineN.setStatus("current")


class _NpIoTrapLevelIn_Type(Integer32):
    """Custom type npIoTrapLevelIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpIoTrapLevelIn_Type.__name__ = "Integer32"
_NpIoTrapLevelIn_Object = MibScalar
npIoTrapLevelIn = _NpIoTrapLevelIn_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 2),
    _NpIoTrapLevelIn_Type()
)
npIoTrapLevelIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapLevelIn.setStatus("current")
_NpIoTrapMemo_Type = DisplayString
_NpIoTrapMemo_Object = MibScalar
npIoTrapMemo = _NpIoTrapMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 6),
    _NpIoTrapMemo_Type()
)
npIoTrapMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapMemo.setStatus("current")
_NpIoTrapLevelLegend_Type = DisplayString
_NpIoTrapLevelLegend_Object = MibScalar
npIoTrapLevelLegend = _NpIoTrapLevelLegend_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 7),
    _NpIoTrapLevelLegend_Type()
)
npIoTrapLevelLegend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapLevelLegend.setStatus("current")

# Managed Objects groups


# Notification objects

npGsmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 2, 0, 1)
)
npGsmTrap.setObjects(
      *(("DKSF-70-6-X-X-1", "npGsmFailed"),
        ("DKSF-70-6-X-X-1", "npGsmRegistration"),
        ("DKSF-70-6-X-X-1", "npGsmStrength"))
)
if mibBuilder.loadTexts:
    npGsmTrap.setStatus(
        "current"
    )

npSmokeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2, 0, 1)
)
npSmokeTrap.setObjects(
      *(("DKSF-70-6-X-X-1", "npSmokeTrapSensorN"),
        ("DKSF-70-6-X-X-1", "npSmokeTrapStatus"),
        ("DKSF-70-6-X-X-1", "npSmokeTrapMemo"))
)
if mibBuilder.loadTexts:
    npSmokeTrap.setStatus(
        "current"
    )

npCurLoopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 0, 1)
)
npCurLoopTrap.setObjects(
      *(("DKSF-70-6-X-X-1", "npCurLoopTrapN"),
        ("DKSF-70-6-X-X-1", "npCurLoopTrapStatus"),
        ("DKSF-70-6-X-X-1", "npCurLoopTrapI"),
        ("DKSF-70-6-X-X-1", "npCurLoopTrapV"),
        ("DKSF-70-6-X-X-1", "npCurLoopTrapR"),
        ("DKSF-70-6-X-X-1", "npCurLoopTrapPower"),
        ("DKSF-70-6-X-X-1", "npTrapEmailTo"))
)
if mibBuilder.loadTexts:
    npCurLoopTrap.setStatus(
        "current"
    )

npRelHumTrapFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 6, 100)
)
npRelHumTrapFail.setObjects(
      *(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapFail.setStatus(
        "current"
    )

npRelHumTrapBelowSafe = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 6, 101)
)
npRelHumTrapBelowSafe.setObjects(
      *(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapBelowSafe.setStatus(
        "current"
    )

npRelHumTrapSafe = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 6, 102)
)
npRelHumTrapSafe.setObjects(
      *(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapSafe.setStatus(
        "current"
    )

npRelHumTrapAboveSafe = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 6, 103)
)
npRelHumTrapAboveSafe.setObjects(
      *(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapAboveSafe.setStatus(
        "current"
    )

npRelHumTrapAllChannels = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 6, 127, 99)
)
npRelHumTrapAllChannels.setObjects(
      *(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapAllChannels.setStatus(
        "current"
    )

npRelHumTrapTempFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 7, 100)
)
npRelHumTrapTempFail.setObjects(
      *(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapTempFail.setStatus(
        "current"
    )

npRelHumTrapTempBelowSafe = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 7, 101)
)
npRelHumTrapTempBelowSafe.setObjects(
      *(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapTempBelowSafe.setStatus(
        "current"
    )

npRelHumTrapTempSafe = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 7, 102)
)
npRelHumTrapTempSafe.setObjects(
      *(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapTempSafe.setStatus(
        "current"
    )

npRelHumTrapTempAboveSafe = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 7, 103)
)
npRelHumTrapTempAboveSafe.setObjects(
      *(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapTempAboveSafe.setStatus(
        "current"
    )

npRelHumTrapTempAllChannels = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 7, 127, 99)
)
npRelHumTrapTempAllChannels.setObjects(
      *(("DKSF-70-6-X-X-1", "npRelHumTrapDataN"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataStatus"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataValue"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataMemo"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-6-X-X-1", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapTempAllChannels.setStatus(
        "current"
    )

npThermoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 0, 1)
)
npThermoTrap.setObjects(
      *(("DKSF-70-6-X-X-1", "npThermoTrapSensorN"),
        ("DKSF-70-6-X-X-1", "npThermoTrapValue"),
        ("DKSF-70-6-X-X-1", "npThermoTrapStatus"),
        ("DKSF-70-6-X-X-1", "npThermoTrapLow"),
        ("DKSF-70-6-X-X-1", "npThermoTrapHigh"),
        ("DKSF-70-6-X-X-1", "npThermoTrapMemo"))
)
if mibBuilder.loadTexts:
    npThermoTrap.setStatus(
        "current"
    )

npIoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 0, 1)
)
npIoTrap.setObjects(
      *(("DKSF-70-6-X-X-1", "npIoTrapLineN"),
        ("DKSF-70-6-X-X-1", "npIoTrapLevelIn"),
        ("DKSF-70-6-X-X-1", "npIoTrapMemo"),
        ("DKSF-70-6-X-X-1", "npIoTrapLevelLegend"))
)
if mibBuilder.loadTexts:
    npIoTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DKSF-70-6-X-X-1",
    **{"FixedPoint1000": FixedPoint1000,
       "lightcom": lightcom,
       "uniPingServerSolutionV3": uniPingServerSolutionV3,
       "npTrapInfo": npTrapInfo,
       "npTrapEmailTo": npTrapEmailTo,
       "npReboot": npReboot,
       "npSoftReboot": npSoftReboot,
       "npResetStack": npResetStack,
       "npForcedReboot": npForcedReboot,
       "npGsm": npGsm,
       "npGsmInfo": npGsmInfo,
       "npGsmFailed": npGsmFailed,
       "npGsmRegistration": npGsmRegistration,
       "npGsmStrength": npGsmStrength,
       "npGsmSendSmsUtf8": npGsmSendSmsUtf8,
       "npGsmSendSmsWin1251": npGsmSendSmsWin1251,
       "npGsmTraps": npGsmTraps,
       "npGsmTrapPrefix": npGsmTrapPrefix,
       "npGsmTrap": npGsmTrap,
       "npRelay": npRelay,
       "npRelayTable": npRelayTable,
       "npRelayEntry": npRelayEntry,
       "npRelayN": npRelayN,
       "npRelayMode": npRelayMode,
       "npRelayStartReset": npRelayStartReset,
       "npRelayMemo": npRelayMemo,
       "npRelayState": npRelayState,
       "npIr": npIr,
       "npIrCtrl": npIrCtrl,
       "npIrPlayCmd": npIrPlayCmd,
       "npIrReset": npIrReset,
       "npIrStatus": npIrStatus,
       "npSmoke": npSmoke,
       "npSmokeTable": npSmokeTable,
       "npSmokeEntry": npSmokeEntry,
       "npSmokeSensorN": npSmokeSensorN,
       "npSmokeStatus": npSmokeStatus,
       "npSmokePower": npSmokePower,
       "npSmokeReset": npSmokeReset,
       "npSmokeMemo": npSmokeMemo,
       "npSmokeTraps": npSmokeTraps,
       "npSmokeTrapPrefix": npSmokeTrapPrefix,
       "npSmokeTrap": npSmokeTrap,
       "npSmokeTrapSensorN": npSmokeTrapSensorN,
       "npSmokeTrapStatus": npSmokeTrapStatus,
       "npSmokeTrapMemo": npSmokeTrapMemo,
       "npCurLoop": npCurLoop,
       "npCurLoopTable": npCurLoopTable,
       "npCurLoopEntry": npCurLoopEntry,
       "npCurLoopN": npCurLoopN,
       "npCurLoopStatus": npCurLoopStatus,
       "npCurLoopI": npCurLoopI,
       "npCurLoopV": npCurLoopV,
       "npCurLoopR": npCurLoopR,
       "npCurLoopPower": npCurLoopPower,
       "npCurLoopTraps": npCurLoopTraps,
       "npCurLoopTrapPrefix": npCurLoopTrapPrefix,
       "npCurLoopTrap": npCurLoopTrap,
       "npCurLoopTrapN": npCurLoopTrapN,
       "npCurLoopTrapStatus": npCurLoopTrapStatus,
       "npCurLoopTrapI": npCurLoopTrapI,
       "npCurLoopTrapV": npCurLoopTrapV,
       "npCurLoopTrapR": npCurLoopTrapR,
       "npCurLoopTrapPower": npCurLoopTrapPower,
       "npRelHumidity": npRelHumidity,
       "npRelHumTable": npRelHumTable,
       "npRelHumEntry": npRelHumEntry,
       "npRelHumN": npRelHumN,
       "npRelHumValue": npRelHumValue,
       "npRelHumStatus": npRelHumStatus,
       "npRelHumTempValue": npRelHumTempValue,
       "npRelHumTempStatus": npRelHumTempStatus,
       "npRelHumMemo": npRelHumMemo,
       "npRelHumSafeRangeHigh": npRelHumSafeRangeHigh,
       "npRelHumSafeRangeLow": npRelHumSafeRangeLow,
       "npRelHumTempSafeRangeHigh": npRelHumTempSafeRangeHigh,
       "npRelHumTempSafeRangeLow": npRelHumTempSafeRangeLow,
       "npRelHumTrapData": npRelHumTrapData,
       "npRelHumTrapDataN": npRelHumTrapDataN,
       "npRelHumTrapDataValue": npRelHumTrapDataValue,
       "npRelHumTrapDataStatus": npRelHumTrapDataStatus,
       "npRelHumTrapDataMemo": npRelHumTrapDataMemo,
       "npRelHumTrapDataSafeRangeHigh": npRelHumTrapDataSafeRangeHigh,
       "npRelHumTrapDataSafeRangeLow": npRelHumTrapDataSafeRangeLow,
       "npRelHumTrap": npRelHumTrap,
       "npRelHumTrapFail": npRelHumTrapFail,
       "npRelHumTrapBelowSafe": npRelHumTrapBelowSafe,
       "npRelHumTrapSafe": npRelHumTrapSafe,
       "npRelHumTrapAboveSafe": npRelHumTrapAboveSafe,
       "npRelHumTrapAllEvents": npRelHumTrapAllEvents,
       "npRelHumTrapAllChannels": npRelHumTrapAllChannels,
       "npRelHumTrapTemp": npRelHumTrapTemp,
       "npRelHumTrapTempFail": npRelHumTrapTempFail,
       "npRelHumTrapTempBelowSafe": npRelHumTrapTempBelowSafe,
       "npRelHumTrapTempSafe": npRelHumTrapTempSafe,
       "npRelHumTrapTempAboveSafe": npRelHumTrapTempAboveSafe,
       "npRelHumTrapTempAllEvents": npRelHumTrapTempAllEvents,
       "npRelHumTrapTempAllChannels": npRelHumTrapTempAllChannels,
       "npThermo": npThermo,
       "npThermoTable": npThermoTable,
       "npThermoEntry": npThermoEntry,
       "npThermoSensorN": npThermoSensorN,
       "npThermoValue": npThermoValue,
       "npThermoStatus": npThermoStatus,
       "npThermoLow": npThermoLow,
       "npThermoHigh": npThermoHigh,
       "npThermoMemo": npThermoMemo,
       "npThermoValuePrecise": npThermoValuePrecise,
       "npThermoTraps": npThermoTraps,
       "npThermoTrapPrefix": npThermoTrapPrefix,
       "npThermoTrap": npThermoTrap,
       "npThermoTrapSensorN": npThermoTrapSensorN,
       "npThermoTrapValue": npThermoTrapValue,
       "npThermoTrapStatus": npThermoTrapStatus,
       "npThermoTrapLow": npThermoTrapLow,
       "npThermoTrapHigh": npThermoTrapHigh,
       "npThermoTrapMemo": npThermoTrapMemo,
       "npIo": npIo,
       "npIoTable": npIoTable,
       "npIoEntry": npIoEntry,
       "npIoLineN": npIoLineN,
       "npIoLevelIn": npIoLevelIn,
       "npIoLevelOut": npIoLevelOut,
       "npIoMemo": npIoMemo,
       "npIoPulseCounter": npIoPulseCounter,
       "npIoSinglePulseDuration": npIoSinglePulseDuration,
       "npIoSinglePulseStart": npIoSinglePulseStart,
       "npIoTraps": npIoTraps,
       "npIoTrapPrefix": npIoTrapPrefix,
       "npIoTrap": npIoTrap,
       "npIoTrapLineN": npIoTrapLineN,
       "npIoTrapLevelIn": npIoTrapLevelIn,
       "npIoTrapMemo": npIoTrapMemo,
       "npIoTrapLevelLegend": npIoTrapLevelLegend}
)
