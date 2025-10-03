# SNMP MIB module (SONOMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\endrun\SONOMA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:40:02 2025
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

endRunTechnologies = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 0)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EndRunTechnologiesMIB_ObjectIdentity = ObjectIdentity
endRunTechnologiesMIB = _EndRunTechnologiesMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827)
)
_SonomaCDMA_ObjectIdentity = ObjectIdentity
sonomaCDMA = _SonomaCDMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 11)
)
_Cntp_ObjectIdentity = ObjectIdentity
cntp = _Cntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1)
)
_Cntptrap_ObjectIdentity = ObjectIdentity
cntptrap = _Cntptrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 0)
)
_CntpTimeSinceRst_Type = Counter32
_CntpTimeSinceRst_Object = MibScalar
cntpTimeSinceRst = _CntpTimeSinceRst_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 1),
    _CntpTimeSinceRst_Type()
)
cntpTimeSinceRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpTimeSinceRst.setStatus("current")
_CntpIRQsHandled_Type = Counter32
_CntpIRQsHandled_Object = MibScalar
cntpIRQsHandled = _CntpIRQsHandled_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 2),
    _CntpIRQsHandled_Type()
)
cntpIRQsHandled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpIRQsHandled.setStatus("current")
_CntpRxPkts_Type = Counter32
_CntpRxPkts_Object = MibScalar
cntpRxPkts = _CntpRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 3),
    _CntpRxPkts_Type()
)
cntpRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpRxPkts.setStatus("current")
_CntpRxPktsByIRQ_Type = Counter32
_CntpRxPktsByIRQ_Object = MibScalar
cntpRxPktsByIRQ = _CntpRxPktsByIRQ_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 4),
    _CntpRxPktsByIRQ_Type()
)
cntpRxPktsByIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpRxPktsByIRQ.setStatus("current")
_CntpTxPkts_Type = Counter32
_CntpTxPkts_Object = MibScalar
cntpTxPkts = _CntpTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 5),
    _CntpTxPkts_Type()
)
cntpTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpTxPkts.setStatus("current")
_CntpSentPktsPerSecond_Type = Integer32
_CntpSentPktsPerSecond_Object = MibScalar
cntpSentPktsPerSecond = _CntpSentPktsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 6),
    _CntpSentPktsPerSecond_Type()
)
cntpSentPktsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpSentPktsPerSecond.setStatus("current")
_CntpUnSentPkts_Type = Counter32
_CntpUnSentPkts_Object = MibScalar
cntpUnSentPkts = _CntpUnSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 7),
    _CntpUnSentPkts_Type()
)
cntpUnSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpUnSentPkts.setStatus("current")
_CntpIgnoredPkts_Type = Counter32
_CntpIgnoredPkts_Object = MibScalar
cntpIgnoredPkts = _CntpIgnoredPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 8),
    _CntpIgnoredPkts_Type()
)
cntpIgnoredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpIgnoredPkts.setStatus("current")
_CntpDroppedPkts_Type = Counter32
_CntpDroppedPkts_Object = MibScalar
cntpDroppedPkts = _CntpDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 9),
    _CntpDroppedPkts_Type()
)
cntpDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpDroppedPkts.setStatus("current")
_CntpAuthFail_Type = Counter32
_CntpAuthFail_Object = MibScalar
cntpAuthFail = _CntpAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 10),
    _CntpAuthFail_Type()
)
cntpAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpAuthFail.setStatus("current")


class _CntpTimeFigureOfMerit_Type(Integer32):
    """Custom type cntpTimeFigureOfMerit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("lessthan100us", 6),
          ("lessthan1ms", 7),
          ("lessthan10ms", 8),
          ("greaterthan10ms", 9))
    )


_CntpTimeFigureOfMerit_Type.__name__ = "Integer32"
_CntpTimeFigureOfMerit_Object = MibScalar
cntpTimeFigureOfMerit = _CntpTimeFigureOfMerit_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 11),
    _CntpTimeFigureOfMerit_Type()
)
cntpTimeFigureOfMerit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpTimeFigureOfMerit.setStatus("current")


class _CntpLeapIndBits_Type(Integer32):
    """Custom type cntpLeapIndBits based on Integer32"""
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
        *(("noFaultorLeap", 0),
          ("leapInsWarning", 1),
          ("leapDelWarning", 2),
          ("unSynchronized", 3))
    )


_CntpLeapIndBits_Type.__name__ = "Integer32"
_CntpLeapIndBits_Object = MibScalar
cntpLeapIndBits = _CntpLeapIndBits_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 12),
    _CntpLeapIndBits_Type()
)
cntpLeapIndBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpLeapIndBits.setStatus("current")


class _CntpSyncSource_Type(DisplayString):
    """Custom type cntpSyncSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CntpSyncSource_Type.__name__ = "DisplayString"
_CntpSyncSource_Object = MibScalar
cntpSyncSource = _CntpSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 13),
    _CntpSyncSource_Type()
)
cntpSyncSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpSyncSource.setStatus("current")


class _CntpOffsetToCDMAReference_Type(DisplayString):
    """Custom type cntpOffsetToCDMAReference based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CntpOffsetToCDMAReference_Type.__name__ = "DisplayString"
_CntpOffsetToCDMAReference_Object = MibScalar
cntpOffsetToCDMAReference = _CntpOffsetToCDMAReference_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 14),
    _CntpOffsetToCDMAReference_Type()
)
cntpOffsetToCDMAReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpOffsetToCDMAReference.setStatus("current")


class _CntpStratum_Type(Integer32):
    """Custom type cntpStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              16)
        )
    )
    namedValues = NamedValues(
        *(("cntpStratumOne", 1),
          ("cntpStratumTwo", 2),
          ("cntpStratumUnsync", 16))
    )


_CntpStratum_Type.__name__ = "Integer32"
_CntpStratum_Object = MibScalar
cntpStratum = _CntpStratum_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 15),
    _CntpStratum_Type()
)
cntpStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpStratum.setStatus("current")


class _CntpVersion_Type(DisplayString):
    """Custom type cntpVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CntpVersion_Type.__name__ = "DisplayString"
_CntpVersion_Object = MibScalar
cntpVersion = _CntpVersion_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 16),
    _CntpVersion_Type()
)
cntpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpVersion.setStatus("current")


class _CntpKernelVersion_Type(DisplayString):
    """Custom type cntpKernelVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CntpKernelVersion_Type.__name__ = "DisplayString"
_CntpKernelVersion_Object = MibScalar
cntpKernelVersion = _CntpKernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 17),
    _CntpKernelVersion_Type()
)
cntpKernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpKernelVersion.setStatus("current")


class _CntpOscType_Type(DisplayString):
    """Custom type cntpOscType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CntpOscType_Type.__name__ = "DisplayString"
_CntpOscType_Object = MibScalar
cntpOscType = _CntpOscType_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 18),
    _CntpOscType_Type()
)
cntpOscType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpOscType.setStatus("current")


class _CntpTimeMode_Type(DisplayString):
    """Custom type cntpTimeMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CntpTimeMode_Type.__name__ = "DisplayString"
_CntpTimeMode_Object = MibScalar
cntpTimeMode = _CntpTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 19),
    _CntpTimeMode_Type()
)
cntpTimeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpTimeMode.setStatus("current")
_CntpLocalOffset_Type = Integer32
_CntpLocalOffset_Object = MibScalar
cntpLocalOffset = _CntpLocalOffset_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 20),
    _CntpLocalOffset_Type()
)
cntpLocalOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpLocalOffset.setStatus("current")


class _CntpDSTStartMonth_Type(Integer32):
    """Custom type cntpDSTStartMonth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_CntpDSTStartMonth_Type.__name__ = "Integer32"
_CntpDSTStartMonth_Object = MibScalar
cntpDSTStartMonth = _CntpDSTStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 21),
    _CntpDSTStartMonth_Type()
)
cntpDSTStartMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpDSTStartMonth.setStatus("current")


class _CntpDSTStartSunday_Type(Integer32):
    """Custom type cntpDSTStartSunday based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("firstSunday", 1),
          ("secondSunday", 2),
          ("thirdSunday", 3),
          ("fourthSunday", 4),
          ("lastSunday", 5))
    )


_CntpDSTStartSunday_Type.__name__ = "Integer32"
_CntpDSTStartSunday_Object = MibScalar
cntpDSTStartSunday = _CntpDSTStartSunday_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 22),
    _CntpDSTStartSunday_Type()
)
cntpDSTStartSunday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpDSTStartSunday.setStatus("current")
_CntpDSTStartHour_Type = Integer32
_CntpDSTStartHour_Object = MibScalar
cntpDSTStartHour = _CntpDSTStartHour_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 23),
    _CntpDSTStartHour_Type()
)
cntpDSTStartHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpDSTStartHour.setStatus("current")


class _CntpDSTStopMonth_Type(Integer32):
    """Custom type cntpDSTStopMonth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_CntpDSTStopMonth_Type.__name__ = "Integer32"
_CntpDSTStopMonth_Object = MibScalar
cntpDSTStopMonth = _CntpDSTStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 24),
    _CntpDSTStopMonth_Type()
)
cntpDSTStopMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpDSTStopMonth.setStatus("current")


class _CntpDSTStopSunday_Type(Integer32):
    """Custom type cntpDSTStopSunday based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("firstSunday", 1),
          ("secondSunday", 2),
          ("thirdSunday", 3),
          ("fourthSunday", 4),
          ("lastSunday", 5))
    )


_CntpDSTStopSunday_Type.__name__ = "Integer32"
_CntpDSTStopSunday_Object = MibScalar
cntpDSTStopSunday = _CntpDSTStopSunday_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 25),
    _CntpDSTStopSunday_Type()
)
cntpDSTStopSunday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpDSTStopSunday.setStatus("current")
_CntpDSTStopHour_Type = Integer32
_CntpDSTStopHour_Object = MibScalar
cntpDSTStopHour = _CntpDSTStopHour_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 26),
    _CntpDSTStopHour_Type()
)
cntpDSTStopHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpDSTStopHour.setStatus("current")


class _CntpCPUDieTemperature_Type(DisplayString):
    """Custom type cntpCPUDieTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CntpCPUDieTemperature_Type.__name__ = "DisplayString"
_CntpCPUDieTemperature_Object = MibScalar
cntpCPUDieTemperature = _CntpCPUDieTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 27),
    _CntpCPUDieTemperature_Type()
)
cntpCPUDieTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpCPUDieTemperature.setStatus("current")
_CntpCPUFreeMemory_Type = Integer32
_CntpCPUFreeMemory_Object = MibScalar
cntpCPUFreeMemory = _CntpCPUFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 28),
    _CntpCPUFreeMemory_Type()
)
cntpCPUFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpCPUFreeMemory.setStatus("current")
_CntpCPULoadAveragePerCent_Type = Integer32
_CntpCPULoadAveragePerCent_Object = MibScalar
cntpCPULoadAveragePerCent = _CntpCPULoadAveragePerCent_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 29),
    _CntpCPULoadAveragePerCent_Type()
)
cntpCPULoadAveragePerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpCPULoadAveragePerCent.setStatus("current")
_Cdma_ObjectIdentity = ObjectIdentity
cdma = _Cdma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2)
)
_Cdmatrap_ObjectIdentity = ObjectIdentity
cdmatrap = _Cdmatrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 0)
)


class _CdmaFaultStatus_Type(Bits):
    """Custom type cdmaFaultStatus based on Bits"""
    namedValues = NamedValues(
        *(("cdmaReceiverFlt", 0),
          ("cdmaNTPNotPolling", 1),
          ("cdmaRefTimeFlt", 2),
          ("cdmaReceiverCommFlt", 3),
          ("cdmaFLASHWriteFlt", 4),
          ("cdmaFPGACfgFlt", 5),
          ("cdmaNoSignalTimeout", 6),
          ("cdmaDACNearLimit", 7))
    )

_CdmaFaultStatus_Type.__name__ = "Bits"
_CdmaFaultStatus_Object = MibScalar
cdmaFaultStatus = _CdmaFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 1),
    _CdmaFaultStatus_Type()
)
cdmaFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaFaultStatus.setStatus("current")


class _CdmaFault2Status_Type(Bits):
    """Custom type cdmaFault2Status based on Bits"""
    namedValues = NamedValues(
        *(("cdmaSysPwrOvld", 0),
          ("cdmaNotUsed1", 1),
          ("cdmaNotUsed2", 2),
          ("cdmaNotUsed3", 3),
          ("cdmaNotUsed4", 4),
          ("cdmaOscPLLFlt", 5),
          ("cdmaSecPwrSplyFlt", 6),
          ("cdmaPriPwrSplyFlt", 7))
    )

_CdmaFault2Status_Type.__name__ = "Bits"
_CdmaFault2Status_Object = MibScalar
cdmaFault2Status = _CdmaFault2Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 2),
    _CdmaFault2Status_Type()
)
cdmaFault2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaFault2Status.setStatus("current")


class _CdmaReceiverFaultNibble0Status_Type(Bits):
    """Custom type cdmaReceiverFaultNibble0Status based on Bits"""
    namedValues = NamedValues(
        *(("cdmaFLASHWriteFlt", 0),
          ("cdmaFPGACfgFlt", 1),
          ("cdmaNoSignalTimeout", 2),
          ("cdmaDACNearLimit", 3))
    )

_CdmaReceiverFaultNibble0Status_Type.__name__ = "Bits"
_CdmaReceiverFaultNibble0Status_Object = MibScalar
cdmaReceiverFaultNibble0Status = _CdmaReceiverFaultNibble0Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 3),
    _CdmaReceiverFaultNibble0Status_Type()
)
cdmaReceiverFaultNibble0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaReceiverFaultNibble0Status.setStatus("current")


class _CdmaReceiverFaultNibble1Status_Type(Bits):
    """Custom type cdmaReceiverFaultNibble1Status based on Bits"""
    namedValues = NamedValues(
        *(("cdmaMainOscFlt", 0),
          ("cdmaRefTimeFlt", 1),
          ("cdmaSynthFlt", 2),
          ("cdmaSynthNearLimit", 3))
    )

_CdmaReceiverFaultNibble1Status_Type.__name__ = "Bits"
_CdmaReceiverFaultNibble1Status_Object = MibScalar
cdmaReceiverFaultNibble1Status = _CdmaReceiverFaultNibble1Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 4),
    _CdmaReceiverFaultNibble1Status_Type()
)
cdmaReceiverFaultNibble1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaReceiverFaultNibble1Status.setStatus("current")


class _CdmaTimeFigureOfMerit_Type(Integer32):
    """Custom type cdmaTimeFigureOfMerit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("lessthan100us", 6),
          ("lessthan1ms", 7),
          ("lessthan10ms", 8),
          ("greaterthan10ms", 9))
    )


_CdmaTimeFigureOfMerit_Type.__name__ = "Integer32"
_CdmaTimeFigureOfMerit_Object = MibScalar
cdmaTimeFigureOfMerit = _CdmaTimeFigureOfMerit_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 5),
    _CdmaTimeFigureOfMerit_Type()
)
cdmaTimeFigureOfMerit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaTimeFigureOfMerit.setStatus("current")


class _CdmaSigProcState_Type(DisplayString):
    """Custom type cdmaSigProcState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CdmaSigProcState_Type.__name__ = "DisplayString"
_CdmaSigProcState_Object = MibScalar
cdmaSigProcState = _CdmaSigProcState_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 6),
    _CdmaSigProcState_Type()
)
cdmaSigProcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaSigProcState.setStatus("current")


class _CdmaReceiverSigProcState_Type(DisplayString):
    """Custom type cdmaReceiverSigProcState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CdmaReceiverSigProcState_Type.__name__ = "DisplayString"
_CdmaReceiverSigProcState_Object = MibScalar
cdmaReceiverSigProcState = _CdmaReceiverSigProcState_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 7),
    _CdmaReceiverSigProcState_Type()
)
cdmaReceiverSigProcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaReceiverSigProcState.setStatus("current")


class _CdmaChannel_Type(DisplayString):
    """Custom type cdmaChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_CdmaChannel_Type.__name__ = "DisplayString"
_CdmaChannel_Object = MibScalar
cdmaChannel = _CdmaChannel_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 8),
    _CdmaChannel_Type()
)
cdmaChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaChannel.setStatus("current")


class _CdmaPNO_Type(Integer32):
    """Custom type cdmaPNO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_CdmaPNO_Type.__name__ = "Integer32"
_CdmaPNO_Object = MibScalar
cdmaPNO = _CdmaPNO_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 9),
    _CdmaPNO_Type()
)
cdmaPNO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaPNO.setStatus("current")


class _CdmaAGC_Type(Integer32):
    """Custom type cdmaAGC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CdmaAGC_Type.__name__ = "Integer32"
_CdmaAGC_Object = MibScalar
cdmaAGC = _CdmaAGC_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 10),
    _CdmaAGC_Type()
)
cdmaAGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaAGC.setStatus("current")


class _CdmaReceiverVCDAC_Type(Integer32):
    """Custom type cdmaReceiverVCDAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CdmaReceiverVCDAC_Type.__name__ = "Integer32"
_CdmaReceiverVCDAC_Object = MibScalar
cdmaReceiverVCDAC = _CdmaReceiverVCDAC_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 11),
    _CdmaReceiverVCDAC_Type()
)
cdmaReceiverVCDAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaReceiverVCDAC.setStatus("current")


class _CdmaCarrierToNoiseRatio_Type(DisplayString):
    """Custom type cdmaCarrierToNoiseRatio based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CdmaCarrierToNoiseRatio_Type.__name__ = "DisplayString"
_CdmaCarrierToNoiseRatio_Object = MibScalar
cdmaCarrierToNoiseRatio = _CdmaCarrierToNoiseRatio_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 12),
    _CdmaCarrierToNoiseRatio_Type()
)
cdmaCarrierToNoiseRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaCarrierToNoiseRatio.setStatus("current")


class _CdmaFrameErrorRate_Type(DisplayString):
    """Custom type cdmaFrameErrorRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CdmaFrameErrorRate_Type.__name__ = "DisplayString"
_CdmaFrameErrorRate_Object = MibScalar
cdmaFrameErrorRate = _CdmaFrameErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 13),
    _CdmaFrameErrorRate_Type()
)
cdmaFrameErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaFrameErrorRate.setStatus("current")


class _CdmaLeapMode_Type(DisplayString):
    """Custom type cdmaLeapMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CdmaLeapMode_Type.__name__ = "DisplayString"
_CdmaLeapMode_Object = MibScalar
cdmaLeapMode = _CdmaLeapMode_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 14),
    _CdmaLeapMode_Type()
)
cdmaLeapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaLeapMode.setStatus("current")
_CdmaUserCurrentLeapSeconds_Type = Integer32
_CdmaUserCurrentLeapSeconds_Object = MibScalar
cdmaUserCurrentLeapSeconds = _CdmaUserCurrentLeapSeconds_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 15),
    _CdmaUserCurrentLeapSeconds_Type()
)
cdmaUserCurrentLeapSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaUserCurrentLeapSeconds.setStatus("current")
_CdmaUserFutureLeapSeconds_Type = Integer32
_CdmaUserFutureLeapSeconds_Object = MibScalar
cdmaUserFutureLeapSeconds = _CdmaUserFutureLeapSeconds_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 16),
    _CdmaUserFutureLeapSeconds_Type()
)
cdmaUserFutureLeapSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaUserFutureLeapSeconds.setStatus("current")
_CdmaCurrentLeapSeconds_Type = Integer32
_CdmaCurrentLeapSeconds_Object = MibScalar
cdmaCurrentLeapSeconds = _CdmaCurrentLeapSeconds_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 17),
    _CdmaCurrentLeapSeconds_Type()
)
cdmaCurrentLeapSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaCurrentLeapSeconds.setStatus("current")
_CdmaFutureLeapSeconds_Type = Integer32
_CdmaFutureLeapSeconds_Object = MibScalar
cdmaFutureLeapSeconds = _CdmaFutureLeapSeconds_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 18),
    _CdmaFutureLeapSeconds_Type()
)
cdmaFutureLeapSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaFutureLeapSeconds.setStatus("current")


class _CdmaVersion_Type(DisplayString):
    """Custom type cdmaVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CdmaVersion_Type.__name__ = "DisplayString"
_CdmaVersion_Object = MibScalar
cdmaVersion = _CdmaVersion_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 19),
    _CdmaVersion_Type()
)
cdmaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaVersion.setStatus("current")


class _CdmaReceiverVersion_Type(DisplayString):
    """Custom type cdmaReceiverVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CdmaReceiverVersion_Type.__name__ = "DisplayString"
_CdmaReceiverVersion_Object = MibScalar
cdmaReceiverVersion = _CdmaReceiverVersion_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 20),
    _CdmaReceiverVersion_Type()
)
cdmaReceiverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaReceiverVersion.setStatus("current")


class _CdmaCalibrationDelay_Type(Integer32):
    """Custom type cdmaCalibrationDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500000, 500000),
    )


_CdmaCalibrationDelay_Type.__name__ = "Integer32"
_CdmaCalibrationDelay_Object = MibScalar
cdmaCalibrationDelay = _CdmaCalibrationDelay_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 21),
    _CdmaCalibrationDelay_Type()
)
cdmaCalibrationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaCalibrationDelay.setStatus("current")


class _CdmaCoastDuration_Type(Integer32):
    """Custom type cdmaCoastDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CdmaCoastDuration_Type.__name__ = "Integer32"
_CdmaCoastDuration_Object = MibScalar
cdmaCoastDuration = _CdmaCoastDuration_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 22),
    _CdmaCoastDuration_Type()
)
cdmaCoastDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaCoastDuration.setStatus("current")


class _CdmaEstimatedTimeError_Type(DisplayString):
    """Custom type cdmaEstimatedTimeError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CdmaEstimatedTimeError_Type.__name__ = "DisplayString"
_CdmaEstimatedTimeError_Object = MibScalar
cdmaEstimatedTimeError = _CdmaEstimatedTimeError_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 23),
    _CdmaEstimatedTimeError_Type()
)
cdmaEstimatedTimeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaEstimatedTimeError.setStatus("current")


class _CdmaMeasuredTimeError_Type(DisplayString):
    """Custom type cdmaMeasuredTimeError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CdmaMeasuredTimeError_Type.__name__ = "DisplayString"
_CdmaMeasuredTimeError_Object = MibScalar
cdmaMeasuredTimeError = _CdmaMeasuredTimeError_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 24),
    _CdmaMeasuredTimeError_Type()
)
cdmaMeasuredTimeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaMeasuredTimeError.setStatus("current")


class _CdmaMeasurementTimeDeviation_Type(DisplayString):
    """Custom type cdmaMeasurementTimeDeviation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CdmaMeasurementTimeDeviation_Type.__name__ = "DisplayString"
_CdmaMeasurementTimeDeviation_Object = MibScalar
cdmaMeasurementTimeDeviation = _CdmaMeasurementTimeDeviation_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 25),
    _CdmaMeasurementTimeDeviation_Type()
)
cdmaMeasurementTimeDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaMeasurementTimeDeviation.setStatus("current")


class _CdmaSystemOSCDAC_Type(Integer32):
    """Custom type cdmaSystemOSCDAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CdmaSystemOSCDAC_Type.__name__ = "Integer32"
_CdmaSystemOSCDAC_Object = MibScalar
cdmaSystemOSCDAC = _CdmaSystemOSCDAC_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 26),
    _CdmaSystemOSCDAC_Type()
)
cdmaSystemOSCDAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaSystemOSCDAC.setStatus("current")


class _CdmaMeasuredOscillatorAgeing_Type(DisplayString):
    """Custom type cdmaMeasuredOscillatorAgeing based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CdmaMeasuredOscillatorAgeing_Type.__name__ = "DisplayString"
_CdmaMeasuredOscillatorAgeing_Object = MibScalar
cdmaMeasuredOscillatorAgeing = _CdmaMeasuredOscillatorAgeing_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 27),
    _CdmaMeasuredOscillatorAgeing_Type()
)
cdmaMeasuredOscillatorAgeing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaMeasuredOscillatorAgeing.setStatus("current")


class _CdmaControlLoopTimeConstant_Type(DisplayString):
    """Custom type cdmaControlLoopTimeConstant based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CdmaControlLoopTimeConstant_Type.__name__ = "DisplayString"
_CdmaControlLoopTimeConstant_Object = MibScalar
cdmaControlLoopTimeConstant = _CdmaControlLoopTimeConstant_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 28),
    _CdmaControlLoopTimeConstant_Type()
)
cdmaControlLoopTimeConstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaControlLoopTimeConstant.setStatus("current")


class _CdmaInternalTemperature_Type(DisplayString):
    """Custom type cdmaInternalTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CdmaInternalTemperature_Type.__name__ = "DisplayString"
_CdmaInternalTemperature_Object = MibScalar
cdmaInternalTemperature = _CdmaInternalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 29),
    _CdmaInternalTemperature_Type()
)
cdmaInternalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaInternalTemperature.setStatus("current")


class _CdmaSignalLossFaultMask_Type(DisplayString):
    """Custom type cdmaSignalLossFaultMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CdmaSignalLossFaultMask_Type.__name__ = "DisplayString"
_CdmaSignalLossFaultMask_Object = MibScalar
cdmaSignalLossFaultMask = _CdmaSignalLossFaultMask_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 30),
    _CdmaSignalLossFaultMask_Type()
)
cdmaSignalLossFaultMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaSignalLossFaultMask.setStatus("current")


class _CdmaPrimaryPowerFaultAlarmMask_Type(DisplayString):
    """Custom type cdmaPrimaryPowerFaultAlarmMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CdmaPrimaryPowerFaultAlarmMask_Type.__name__ = "DisplayString"
_CdmaPrimaryPowerFaultAlarmMask_Object = MibScalar
cdmaPrimaryPowerFaultAlarmMask = _CdmaPrimaryPowerFaultAlarmMask_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 31),
    _CdmaPrimaryPowerFaultAlarmMask_Type()
)
cdmaPrimaryPowerFaultAlarmMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaPrimaryPowerFaultAlarmMask.setStatus("current")


class _CdmaSecondaryPowerFaultAlarmMask_Type(DisplayString):
    """Custom type cdmaSecondaryPowerFaultAlarmMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CdmaSecondaryPowerFaultAlarmMask_Type.__name__ = "DisplayString"
_CdmaSecondaryPowerFaultAlarmMask_Object = MibScalar
cdmaSecondaryPowerFaultAlarmMask = _CdmaSecondaryPowerFaultAlarmMask_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 32),
    _CdmaSecondaryPowerFaultAlarmMask_Type()
)
cdmaSecondaryPowerFaultAlarmMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaSecondaryPowerFaultAlarmMask.setStatus("current")


class _CdmaFaultNibble0Status_Type(Bits):
    """Custom type cdmaFaultNibble0Status based on Bits"""
    namedValues = NamedValues(
        *(("cdmaFLASHWriteFlt", 0),
          ("cdmaFPGACfgFlt", 1),
          ("cdmaNoSignalTimeout", 2),
          ("cdmaDACNearLimit", 3))
    )

_CdmaFaultNibble0Status_Type.__name__ = "Bits"
_CdmaFaultNibble0Status_Object = MibScalar
cdmaFaultNibble0Status = _CdmaFaultNibble0Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 33),
    _CdmaFaultNibble0Status_Type()
)
cdmaFaultNibble0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaFaultNibble0Status.setStatus("current")


class _CdmaFaultNibble1Status_Type(Bits):
    """Custom type cdmaFaultNibble1Status based on Bits"""
    namedValues = NamedValues(
        *(("cdmaReceiverFlt", 0),
          ("cdmaNTPNotPolling", 1),
          ("cdmaRefTimeFlt", 2),
          ("cdmaReceiverCommFlt", 3))
    )

_CdmaFaultNibble1Status_Type.__name__ = "Bits"
_CdmaFaultNibble1Status_Object = MibScalar
cdmaFaultNibble1Status = _CdmaFaultNibble1Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 34),
    _CdmaFaultNibble1Status_Type()
)
cdmaFaultNibble1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaFaultNibble1Status.setStatus("current")


class _CdmaFaultNibble2Status_Type(Bits):
    """Custom type cdmaFaultNibble2Status based on Bits"""
    namedValues = NamedValues(
        *(("cdmaNotUsed4", 0),
          ("cdmaOscPLLFlt", 1),
          ("cdmaSecPwrSplyFlt", 2),
          ("cdmaPriPwrSplyFlt", 3))
    )

_CdmaFaultNibble2Status_Type.__name__ = "Bits"
_CdmaFaultNibble2Status_Object = MibScalar
cdmaFaultNibble2Status = _CdmaFaultNibble2Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 35),
    _CdmaFaultNibble2Status_Type()
)
cdmaFaultNibble2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaFaultNibble2Status.setStatus("current")


class _CdmaFaultNibble3Status_Type(Bits):
    """Custom type cdmaFaultNibble3Status based on Bits"""
    namedValues = NamedValues(
        *(("cdmaSysPwrOvld", 0),
          ("cdmaNotUsed1", 1),
          ("cdmaNotUsed2", 2),
          ("cdmaNotUsed3", 3))
    )

_CdmaFaultNibble3Status_Type.__name__ = "Bits"
_CdmaFaultNibble3Status_Object = MibScalar
cdmaFaultNibble3Status = _CdmaFaultNibble3Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 36),
    _CdmaFaultNibble3Status_Type()
)
cdmaFaultNibble3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaFaultNibble3Status.setStatus("current")
_CCPUIO_ObjectIdentity = ObjectIdentity
cCPUIO = _CCPUIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 11, 3)
)


class _Csysio1PPSWidth_Type(DisplayString):
    """Custom type csysio1PPSWidth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Csysio1PPSWidth_Type.__name__ = "DisplayString"
_Csysio1PPSWidth_Object = MibScalar
csysio1PPSWidth = _Csysio1PPSWidth_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 3, 1),
    _Csysio1PPSWidth_Type()
)
csysio1PPSWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csysio1PPSWidth.setStatus("current")


class _CsysioTimeCodeFormat_Type(DisplayString):
    """Custom type csysioTimeCodeFormat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CsysioTimeCodeFormat_Type.__name__ = "DisplayString"
_CsysioTimeCodeFormat_Object = MibScalar
csysioTimeCodeFormat = _CsysioTimeCodeFormat_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 3, 2),
    _CsysioTimeCodeFormat_Type()
)
csysioTimeCodeFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csysioTimeCodeFormat.setStatus("current")


class _CsysioSynthesizerHz_Type(Integer32):
    """Custom type csysioSynthesizerHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_CsysioSynthesizerHz_Type.__name__ = "Integer32"
_CsysioSynthesizerHz_Object = MibScalar
csysioSynthesizerHz = _CsysioSynthesizerHz_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 3, 3),
    _CsysioSynthesizerHz_Type()
)
csysioSynthesizerHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csysioSynthesizerHz.setStatus("current")


class _CsysioSerialTimeOutputBaudrate_Type(DisplayString):
    """Custom type csysioSerialTimeOutputBaudrate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CsysioSerialTimeOutputBaudrate_Type.__name__ = "DisplayString"
_CsysioSerialTimeOutputBaudrate_Object = MibScalar
csysioSerialTimeOutputBaudrate = _CsysioSerialTimeOutputBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 3, 4),
    _CsysioSerialTimeOutputBaudrate_Type()
)
csysioSerialTimeOutputBaudrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csysioSerialTimeOutputBaudrate.setStatus("current")


class _CsysioSerialTimeOutputFormat_Type(DisplayString):
    """Custom type csysioSerialTimeOutputFormat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CsysioSerialTimeOutputFormat_Type.__name__ = "DisplayString"
_CsysioSerialTimeOutputFormat_Object = MibScalar
csysioSerialTimeOutputFormat = _CsysioSerialTimeOutputFormat_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 3, 5),
    _CsysioSerialTimeOutputFormat_Type()
)
csysioSerialTimeOutputFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csysioSerialTimeOutputFormat.setStatus("current")


class _CsysioSerialTimeOutputParity_Type(DisplayString):
    """Custom type csysioSerialTimeOutputParity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CsysioSerialTimeOutputParity_Type.__name__ = "DisplayString"
_CsysioSerialTimeOutputParity_Object = MibScalar
csysioSerialTimeOutputParity = _CsysioSerialTimeOutputParity_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 3, 6),
    _CsysioSerialTimeOutputParity_Type()
)
csysioSerialTimeOutputParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csysioSerialTimeOutputParity.setStatus("current")


class _CsysioSerialTimeNMEASentence1_Type(DisplayString):
    """Custom type csysioSerialTimeNMEASentence1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CsysioSerialTimeNMEASentence1_Type.__name__ = "DisplayString"
_CsysioSerialTimeNMEASentence1_Object = MibScalar
csysioSerialTimeNMEASentence1 = _CsysioSerialTimeNMEASentence1_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 3, 7),
    _CsysioSerialTimeNMEASentence1_Type()
)
csysioSerialTimeNMEASentence1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csysioSerialTimeNMEASentence1.setStatus("current")


class _CsysioSerialTimeNMEASentence2_Type(DisplayString):
    """Custom type csysioSerialTimeNMEASentence2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CsysioSerialTimeNMEASentence2_Type.__name__ = "DisplayString"
_CsysioSerialTimeNMEASentence2_Object = MibScalar
csysioSerialTimeNMEASentence2 = _CsysioSerialTimeNMEASentence2_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 3, 8),
    _CsysioSerialTimeNMEASentence2_Type()
)
csysioSerialTimeNMEASentence2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csysioSerialTimeNMEASentence2.setStatus("current")


class _CsysioSerialTimeNMEASentence3_Type(DisplayString):
    """Custom type csysioSerialTimeNMEASentence3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CsysioSerialTimeNMEASentence3_Type.__name__ = "DisplayString"
_CsysioSerialTimeNMEASentence3_Object = MibScalar
csysioSerialTimeNMEASentence3 = _CsysioSerialTimeNMEASentence3_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 3, 9),
    _CsysioSerialTimeNMEASentence3_Type()
)
csysioSerialTimeNMEASentence3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csysioSerialTimeNMEASentence3.setStatus("current")


class _CcpuioConnA_Type(DisplayString):
    """Custom type ccpuioConnA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CcpuioConnA_Type.__name__ = "DisplayString"
_CcpuioConnA_Object = MibScalar
ccpuioConnA = _CcpuioConnA_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 3, 10),
    _CcpuioConnA_Type()
)
ccpuioConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpuioConnA.setStatus("current")


class _CcpuioConnB_Type(DisplayString):
    """Custom type ccpuioConnB based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CcpuioConnB_Type.__name__ = "DisplayString"
_CcpuioConnB_Object = MibScalar
ccpuioConnB = _CcpuioConnB_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 3, 11),
    _CcpuioConnB_Type()
)
ccpuioConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpuioConnB.setStatus("current")


class _CcpuioConnC_Type(DisplayString):
    """Custom type ccpuioConnC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CcpuioConnC_Type.__name__ = "DisplayString"
_CcpuioConnC_Object = MibScalar
ccpuioConnC = _CcpuioConnC_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 3, 12),
    _CcpuioConnC_Type()
)
ccpuioConnC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpuioConnC.setStatus("current")
_Cptp0_ObjectIdentity = ObjectIdentity
cptp0 = _Cptp0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4)
)
_Cptp0Version_Type = Integer32
_Cptp0Version_Object = MibScalar
cptp0Version = _Cptp0Version_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 1),
    _Cptp0Version_Type()
)
cptp0Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0Version.setStatus("current")


class _Cptp0SyncInterval_Type(Integer32):
    """Custom type cptp0SyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-7,
              -6,
              -5,
              -4,
              -3,
              -2,
              -1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("msec8", -7),
          ("msec16", -6),
          ("msec31", -5),
          ("msec63", -4),
          ("msec125", -3),
          ("msec250", -2),
          ("msec500", -1),
          ("sec1", 0))
    )


_Cptp0SyncInterval_Type.__name__ = "Integer32"
_Cptp0SyncInterval_Object = MibScalar
cptp0SyncInterval = _Cptp0SyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 2),
    _Cptp0SyncInterval_Type()
)
cptp0SyncInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0SyncInterval.setStatus("current")


class _Cptp0AnnounceInterval_Type(Integer32):
    """Custom type cptp0AnnounceInterval based on Integer32"""
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
        *(("sec1", 0),
          ("sec2", 1),
          ("sec4", 2),
          ("sec8", 3),
          ("sec16", 4))
    )


_Cptp0AnnounceInterval_Type.__name__ = "Integer32"
_Cptp0AnnounceInterval_Object = MibScalar
cptp0AnnounceInterval = _Cptp0AnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 3),
    _Cptp0AnnounceInterval_Type()
)
cptp0AnnounceInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0AnnounceInterval.setStatus("current")
_Cptp0Priority1_Type = Integer32
_Cptp0Priority1_Object = MibScalar
cptp0Priority1 = _Cptp0Priority1_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 4),
    _Cptp0Priority1_Type()
)
cptp0Priority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0Priority1.setStatus("current")
_Cptp0Priority2_Type = Integer32
_Cptp0Priority2_Object = MibScalar
cptp0Priority2 = _Cptp0Priority2_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 5),
    _Cptp0Priority2_Type()
)
cptp0Priority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0Priority2.setStatus("current")


class _Cptp0DelayMechanism_Type(Integer32):
    """Custom type cptp0DelayMechanism based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              254)
        )
    )
    namedValues = NamedValues(
        *(("e2e", 0),
          ("p2p", 1),
          ("disabled", 254))
    )


_Cptp0DelayMechanism_Type.__name__ = "Integer32"
_Cptp0DelayMechanism_Object = MibScalar
cptp0DelayMechanism = _Cptp0DelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 6),
    _Cptp0DelayMechanism_Type()
)
cptp0DelayMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0DelayMechanism.setStatus("current")
_Cptp0Domain_Type = Integer32
_Cptp0Domain_Object = MibScalar
cptp0Domain = _Cptp0Domain_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 7),
    _Cptp0Domain_Type()
)
cptp0Domain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0Domain.setStatus("current")


class _Cptp0TimeMode_Type(Integer32):
    """Custom type cptp0TimeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("utc", 0),
          ("ptp", 1))
    )


_Cptp0TimeMode_Type.__name__ = "Integer32"
_Cptp0TimeMode_Object = MibScalar
cptp0TimeMode = _Cptp0TimeMode_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 8),
    _Cptp0TimeMode_Type()
)
cptp0TimeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0TimeMode.setStatus("current")
_Cptp0TTL_Type = Integer32
_Cptp0TTL_Object = MibScalar
cptp0TTL = _Cptp0TTL_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 9),
    _Cptp0TTL_Type()
)
cptp0TTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0TTL.setStatus("current")


class _Cptp0ClockClass_Type(Integer32):
    """Custom type cptp0ClockClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              13,
              14,
              52,
              58)
        )
    )
    namedValues = NamedValues(
        *(("lockedPTP", 6),
          ("holdoverPTP", 7),
          ("lockedARB", 13),
          ("holdoverARB", 14),
          ("unlockedPTP", 52),
          ("unlockedARB", 58))
    )


_Cptp0ClockClass_Type.__name__ = "Integer32"
_Cptp0ClockClass_Object = MibScalar
cptp0ClockClass = _Cptp0ClockClass_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 10),
    _Cptp0ClockClass_Type()
)
cptp0ClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0ClockClass.setStatus("current")


class _Cptp0TimeScale_Type(Integer32):
    """Custom type cptp0TimeScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("arb", 0),
          ("ptp", 1))
    )


_Cptp0TimeScale_Type.__name__ = "Integer32"
_Cptp0TimeScale_Object = MibScalar
cptp0TimeScale = _Cptp0TimeScale_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 11),
    _Cptp0TimeScale_Type()
)
cptp0TimeScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0TimeScale.setStatus("current")


class _Cptp0PortState_Type(Integer32):
    """Custom type cptp0PortState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("faulty", 2),
          ("disabled", 3),
          ("listening", 4),
          ("preMaster", 5),
          ("master", 6),
          ("passive", 7),
          ("unCalibrated", 8),
          ("slave", 9))
    )


_Cptp0PortState_Type.__name__ = "Integer32"
_Cptp0PortState_Object = MibScalar
cptp0PortState = _Cptp0PortState_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 12),
    _Cptp0PortState_Type()
)
cptp0PortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0PortState.setStatus("current")


class _Cptp0TimeSource_Type(Integer32):
    """Custom type cptp0TimeSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              64,
              80,
              96,
              144,
              160)
        )
    )
    namedValues = NamedValues(
        *(("atom", 16),
          ("gps", 32),
          ("radio", 48),
          ("ptp", 64),
          ("ntp", 80),
          ("hand", 96),
          ("other", 144),
          ("oscillator", 160))
    )


_Cptp0TimeSource_Type.__name__ = "Integer32"
_Cptp0TimeSource_Object = MibScalar
cptp0TimeSource = _Cptp0TimeSource_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 13),
    _Cptp0TimeSource_Type()
)
cptp0TimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0TimeSource.setStatus("current")
_Cptp0UTCOffset_Type = Integer32
_Cptp0UTCOffset_Object = MibScalar
cptp0UTCOffset = _Cptp0UTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 14),
    _Cptp0UTCOffset_Type()
)
cptp0UTCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0UTCOffset.setStatus("current")


class _Cptp0UTCOffsetValid_Type(Integer32):
    """Custom type cptp0UTCOffsetValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Cptp0UTCOffsetValid_Type.__name__ = "Integer32"
_Cptp0UTCOffsetValid_Object = MibScalar
cptp0UTCOffsetValid = _Cptp0UTCOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 15),
    _Cptp0UTCOffsetValid_Type()
)
cptp0UTCOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0UTCOffsetValid.setStatus("current")


class _Cptp0ClockAccuracy_Type(Integer32):
    """Custom type cptp0ClockAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              254)
        )
    )
    namedValues = NamedValues(
        *(("nsec25", 32),
          ("nsec100", 33),
          ("nsec250", 34),
          ("nsec1000", 35),
          ("nsec2500", 36),
          ("usec10", 37),
          ("usec25", 38),
          ("usec100", 39),
          ("usec250", 40),
          ("usec1000", 41),
          ("usec2500", 42),
          ("msec10", 43),
          ("unknown", 254))
    )


_Cptp0ClockAccuracy_Type.__name__ = "Integer32"
_Cptp0ClockAccuracy_Object = MibScalar
cptp0ClockAccuracy = _Cptp0ClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 16),
    _Cptp0ClockAccuracy_Type()
)
cptp0ClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0ClockAccuracy.setStatus("current")


class _Cptp0Leap59_Type(Integer32):
    """Custom type cptp0Leap59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Cptp0Leap59_Type.__name__ = "Integer32"
_Cptp0Leap59_Object = MibScalar
cptp0Leap59 = _Cptp0Leap59_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 17),
    _Cptp0Leap59_Type()
)
cptp0Leap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0Leap59.setStatus("current")


class _Cptp0Leap61_Type(Integer32):
    """Custom type cptp0Leap61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Cptp0Leap61_Type.__name__ = "Integer32"
_Cptp0Leap61_Object = MibScalar
cptp0Leap61 = _Cptp0Leap61_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 18),
    _Cptp0Leap61_Type()
)
cptp0Leap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0Leap61.setStatus("current")


class _Cptp0TimeTraceable_Type(Integer32):
    """Custom type cptp0TimeTraceable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Cptp0TimeTraceable_Type.__name__ = "Integer32"
_Cptp0TimeTraceable_Object = MibScalar
cptp0TimeTraceable = _Cptp0TimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 19),
    _Cptp0TimeTraceable_Type()
)
cptp0TimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0TimeTraceable.setStatus("current")


class _Cptp0FreqTraceable_Type(Integer32):
    """Custom type cptp0FreqTraceable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Cptp0FreqTraceable_Type.__name__ = "Integer32"
_Cptp0FreqTraceable_Object = MibScalar
cptp0FreqTraceable = _Cptp0FreqTraceable_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 4, 20),
    _Cptp0FreqTraceable_Type()
)
cptp0FreqTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp0FreqTraceable.setStatus("current")
_Cptp1_ObjectIdentity = ObjectIdentity
cptp1 = _Cptp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5)
)
_Cptp1Version_Type = Integer32
_Cptp1Version_Object = MibScalar
cptp1Version = _Cptp1Version_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 1),
    _Cptp1Version_Type()
)
cptp1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1Version.setStatus("current")


class _Cptp1SyncInterval_Type(Integer32):
    """Custom type cptp1SyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-7,
              -6,
              -5,
              -4,
              -3,
              -2,
              -1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("msec8", -7),
          ("msec16", -6),
          ("msec31", -5),
          ("msec63", -4),
          ("msec125", -3),
          ("msec250", -2),
          ("msec500", -1),
          ("sec1", 0))
    )


_Cptp1SyncInterval_Type.__name__ = "Integer32"
_Cptp1SyncInterval_Object = MibScalar
cptp1SyncInterval = _Cptp1SyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 2),
    _Cptp1SyncInterval_Type()
)
cptp1SyncInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1SyncInterval.setStatus("current")


class _Cptp1AnnounceInterval_Type(Integer32):
    """Custom type cptp1AnnounceInterval based on Integer32"""
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
        *(("sec1", 0),
          ("sec2", 1),
          ("sec4", 2),
          ("sec8", 3),
          ("sec16", 4))
    )


_Cptp1AnnounceInterval_Type.__name__ = "Integer32"
_Cptp1AnnounceInterval_Object = MibScalar
cptp1AnnounceInterval = _Cptp1AnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 3),
    _Cptp1AnnounceInterval_Type()
)
cptp1AnnounceInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1AnnounceInterval.setStatus("current")
_Cptp1Priority1_Type = Integer32
_Cptp1Priority1_Object = MibScalar
cptp1Priority1 = _Cptp1Priority1_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 4),
    _Cptp1Priority1_Type()
)
cptp1Priority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1Priority1.setStatus("current")
_Cptp1Priority2_Type = Integer32
_Cptp1Priority2_Object = MibScalar
cptp1Priority2 = _Cptp1Priority2_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 5),
    _Cptp1Priority2_Type()
)
cptp1Priority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1Priority2.setStatus("current")


class _Cptp1DelayMechanism_Type(Integer32):
    """Custom type cptp1DelayMechanism based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              254)
        )
    )
    namedValues = NamedValues(
        *(("e2e", 0),
          ("p2p", 1),
          ("disabled", 254))
    )


_Cptp1DelayMechanism_Type.__name__ = "Integer32"
_Cptp1DelayMechanism_Object = MibScalar
cptp1DelayMechanism = _Cptp1DelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 6),
    _Cptp1DelayMechanism_Type()
)
cptp1DelayMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1DelayMechanism.setStatus("current")
_Cptp1Domain_Type = Integer32
_Cptp1Domain_Object = MibScalar
cptp1Domain = _Cptp1Domain_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 7),
    _Cptp1Domain_Type()
)
cptp1Domain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1Domain.setStatus("current")


class _Cptp1TimeMode_Type(Integer32):
    """Custom type cptp1TimeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("utc", 0),
          ("ptp", 1))
    )


_Cptp1TimeMode_Type.__name__ = "Integer32"
_Cptp1TimeMode_Object = MibScalar
cptp1TimeMode = _Cptp1TimeMode_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 8),
    _Cptp1TimeMode_Type()
)
cptp1TimeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1TimeMode.setStatus("current")
_Cptp1TTL_Type = Integer32
_Cptp1TTL_Object = MibScalar
cptp1TTL = _Cptp1TTL_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 9),
    _Cptp1TTL_Type()
)
cptp1TTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1TTL.setStatus("current")


class _Cptp1ClockClass_Type(Integer32):
    """Custom type cptp1ClockClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              13,
              14,
              52,
              58)
        )
    )
    namedValues = NamedValues(
        *(("lockedPTP", 6),
          ("holdoverPTP", 7),
          ("lockedARB", 13),
          ("holdoverARB", 14),
          ("unlockedPTP", 52),
          ("unlockedARB", 58))
    )


_Cptp1ClockClass_Type.__name__ = "Integer32"
_Cptp1ClockClass_Object = MibScalar
cptp1ClockClass = _Cptp1ClockClass_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 10),
    _Cptp1ClockClass_Type()
)
cptp1ClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1ClockClass.setStatus("current")


class _Cptp1TimeScale_Type(Integer32):
    """Custom type cptp1TimeScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("arb", 0),
          ("ptp", 1))
    )


_Cptp1TimeScale_Type.__name__ = "Integer32"
_Cptp1TimeScale_Object = MibScalar
cptp1TimeScale = _Cptp1TimeScale_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 11),
    _Cptp1TimeScale_Type()
)
cptp1TimeScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1TimeScale.setStatus("current")


class _Cptp1PortState_Type(Integer32):
    """Custom type cptp1PortState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("faulty", 2),
          ("disabled", 3),
          ("listening", 4),
          ("preMaster", 5),
          ("master", 6),
          ("passive", 7),
          ("unCalibrated", 8),
          ("slave", 9))
    )


_Cptp1PortState_Type.__name__ = "Integer32"
_Cptp1PortState_Object = MibScalar
cptp1PortState = _Cptp1PortState_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 12),
    _Cptp1PortState_Type()
)
cptp1PortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1PortState.setStatus("current")


class _Cptp1TimeSource_Type(Integer32):
    """Custom type cptp1TimeSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              64,
              80,
              96,
              144,
              160)
        )
    )
    namedValues = NamedValues(
        *(("atom", 16),
          ("gps", 32),
          ("radio", 48),
          ("ptp", 64),
          ("ntp", 80),
          ("hand", 96),
          ("other", 144),
          ("oscillator", 160))
    )


_Cptp1TimeSource_Type.__name__ = "Integer32"
_Cptp1TimeSource_Object = MibScalar
cptp1TimeSource = _Cptp1TimeSource_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 13),
    _Cptp1TimeSource_Type()
)
cptp1TimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1TimeSource.setStatus("current")
_Cptp1UTCOffset_Type = Integer32
_Cptp1UTCOffset_Object = MibScalar
cptp1UTCOffset = _Cptp1UTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 14),
    _Cptp1UTCOffset_Type()
)
cptp1UTCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1UTCOffset.setStatus("current")


class _Cptp1UTCOffsetValid_Type(Integer32):
    """Custom type cptp1UTCOffsetValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Cptp1UTCOffsetValid_Type.__name__ = "Integer32"
_Cptp1UTCOffsetValid_Object = MibScalar
cptp1UTCOffsetValid = _Cptp1UTCOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 15),
    _Cptp1UTCOffsetValid_Type()
)
cptp1UTCOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1UTCOffsetValid.setStatus("current")


class _Cptp1ClockAccuracy_Type(Integer32):
    """Custom type cptp1ClockAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              254)
        )
    )
    namedValues = NamedValues(
        *(("nsec25", 32),
          ("nsec100", 33),
          ("nsec250", 34),
          ("nsec1000", 35),
          ("nsec2500", 36),
          ("usec10", 37),
          ("usec25", 38),
          ("usec100", 39),
          ("usec250", 40),
          ("usec1000", 41),
          ("usec2500", 42),
          ("msec10", 43),
          ("unknown", 254))
    )


_Cptp1ClockAccuracy_Type.__name__ = "Integer32"
_Cptp1ClockAccuracy_Object = MibScalar
cptp1ClockAccuracy = _Cptp1ClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 16),
    _Cptp1ClockAccuracy_Type()
)
cptp1ClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1ClockAccuracy.setStatus("current")


class _Cptp1Leap59_Type(Integer32):
    """Custom type cptp1Leap59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Cptp1Leap59_Type.__name__ = "Integer32"
_Cptp1Leap59_Object = MibScalar
cptp1Leap59 = _Cptp1Leap59_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 17),
    _Cptp1Leap59_Type()
)
cptp1Leap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1Leap59.setStatus("current")


class _Cptp1Leap61_Type(Integer32):
    """Custom type cptp1Leap61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Cptp1Leap61_Type.__name__ = "Integer32"
_Cptp1Leap61_Object = MibScalar
cptp1Leap61 = _Cptp1Leap61_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 18),
    _Cptp1Leap61_Type()
)
cptp1Leap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1Leap61.setStatus("current")


class _Cptp1TimeTraceable_Type(Integer32):
    """Custom type cptp1TimeTraceable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Cptp1TimeTraceable_Type.__name__ = "Integer32"
_Cptp1TimeTraceable_Object = MibScalar
cptp1TimeTraceable = _Cptp1TimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 19),
    _Cptp1TimeTraceable_Type()
)
cptp1TimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1TimeTraceable.setStatus("current")


class _Cptp1FreqTraceable_Type(Integer32):
    """Custom type cptp1FreqTraceable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Cptp1FreqTraceable_Type.__name__ = "Integer32"
_Cptp1FreqTraceable_Object = MibScalar
cptp1FreqTraceable = _Cptp1FreqTraceable_Object(
    (1, 3, 6, 1, 4, 1, 13827, 11, 5, 20),
    _Cptp1FreqTraceable_Type()
)
cptp1FreqTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptp1FreqTraceable.setStatus("current")
_SonomaGPS_ObjectIdentity = ObjectIdentity
sonomaGPS = _SonomaGPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 12)
)
_Gntp_ObjectIdentity = ObjectIdentity
gntp = _Gntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1)
)
_Gntptrap_ObjectIdentity = ObjectIdentity
gntptrap = _Gntptrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 0)
)
_GntpTimeSinceRst_Type = Counter32
_GntpTimeSinceRst_Object = MibScalar
gntpTimeSinceRst = _GntpTimeSinceRst_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 1),
    _GntpTimeSinceRst_Type()
)
gntpTimeSinceRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpTimeSinceRst.setStatus("current")
_GntpIRQsHandled_Type = Counter32
_GntpIRQsHandled_Object = MibScalar
gntpIRQsHandled = _GntpIRQsHandled_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 2),
    _GntpIRQsHandled_Type()
)
gntpIRQsHandled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpIRQsHandled.setStatus("current")
_GntpRxPkts_Type = Counter32
_GntpRxPkts_Object = MibScalar
gntpRxPkts = _GntpRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 3),
    _GntpRxPkts_Type()
)
gntpRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpRxPkts.setStatus("current")
_GntpRxPktsByIRQ_Type = Counter32
_GntpRxPktsByIRQ_Object = MibScalar
gntpRxPktsByIRQ = _GntpRxPktsByIRQ_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 4),
    _GntpRxPktsByIRQ_Type()
)
gntpRxPktsByIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpRxPktsByIRQ.setStatus("current")
_GntpTxPkts_Type = Counter32
_GntpTxPkts_Object = MibScalar
gntpTxPkts = _GntpTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 5),
    _GntpTxPkts_Type()
)
gntpTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpTxPkts.setStatus("current")
_GntpSentPktsPerSecond_Type = Integer32
_GntpSentPktsPerSecond_Object = MibScalar
gntpSentPktsPerSecond = _GntpSentPktsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 6),
    _GntpSentPktsPerSecond_Type()
)
gntpSentPktsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpSentPktsPerSecond.setStatus("current")
_GntpUnSentPkts_Type = Counter32
_GntpUnSentPkts_Object = MibScalar
gntpUnSentPkts = _GntpUnSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 7),
    _GntpUnSentPkts_Type()
)
gntpUnSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpUnSentPkts.setStatus("current")
_GntpIgnoredPkts_Type = Counter32
_GntpIgnoredPkts_Object = MibScalar
gntpIgnoredPkts = _GntpIgnoredPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 8),
    _GntpIgnoredPkts_Type()
)
gntpIgnoredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpIgnoredPkts.setStatus("current")
_GntpDroppedPkts_Type = Counter32
_GntpDroppedPkts_Object = MibScalar
gntpDroppedPkts = _GntpDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 9),
    _GntpDroppedPkts_Type()
)
gntpDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpDroppedPkts.setStatus("current")
_GntpAuthFail_Type = Counter32
_GntpAuthFail_Object = MibScalar
gntpAuthFail = _GntpAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 10),
    _GntpAuthFail_Type()
)
gntpAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpAuthFail.setStatus("current")


class _GntpTimeFigureOfMerit_Type(Integer32):
    """Custom type gntpTimeFigureOfMerit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("lessthan100ns", 3),
          ("lessthan1us", 4),
          ("lessthan10us", 5),
          ("lessthan100us", 6),
          ("lessthan1ms", 7),
          ("lessthan10ms", 8),
          ("greaterthan10ms", 9))
    )


_GntpTimeFigureOfMerit_Type.__name__ = "Integer32"
_GntpTimeFigureOfMerit_Object = MibScalar
gntpTimeFigureOfMerit = _GntpTimeFigureOfMerit_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 11),
    _GntpTimeFigureOfMerit_Type()
)
gntpTimeFigureOfMerit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpTimeFigureOfMerit.setStatus("current")


class _GntpLeapIndBits_Type(Integer32):
    """Custom type gntpLeapIndBits based on Integer32"""
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
        *(("noFaultorLeap", 0),
          ("leapInsWarning", 1),
          ("leapDelWarning", 2),
          ("unSynchronized", 3))
    )


_GntpLeapIndBits_Type.__name__ = "Integer32"
_GntpLeapIndBits_Object = MibScalar
gntpLeapIndBits = _GntpLeapIndBits_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 12),
    _GntpLeapIndBits_Type()
)
gntpLeapIndBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpLeapIndBits.setStatus("current")


class _GntpSyncSource_Type(DisplayString):
    """Custom type gntpSyncSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_GntpSyncSource_Type.__name__ = "DisplayString"
_GntpSyncSource_Object = MibScalar
gntpSyncSource = _GntpSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 13),
    _GntpSyncSource_Type()
)
gntpSyncSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpSyncSource.setStatus("current")


class _GntpOffsetToGPSReference_Type(DisplayString):
    """Custom type gntpOffsetToGPSReference based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GntpOffsetToGPSReference_Type.__name__ = "DisplayString"
_GntpOffsetToGPSReference_Object = MibScalar
gntpOffsetToGPSReference = _GntpOffsetToGPSReference_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 14),
    _GntpOffsetToGPSReference_Type()
)
gntpOffsetToGPSReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpOffsetToGPSReference.setStatus("current")


class _GntpStratum_Type(Integer32):
    """Custom type gntpStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              16)
        )
    )
    namedValues = NamedValues(
        *(("gntpStratumOne", 1),
          ("gntpStratumTwo", 2),
          ("gntpStratumUnsync", 16))
    )


_GntpStratum_Type.__name__ = "Integer32"
_GntpStratum_Object = MibScalar
gntpStratum = _GntpStratum_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 15),
    _GntpStratum_Type()
)
gntpStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpStratum.setStatus("current")


class _GntpVersion_Type(DisplayString):
    """Custom type gntpVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GntpVersion_Type.__name__ = "DisplayString"
_GntpVersion_Object = MibScalar
gntpVersion = _GntpVersion_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 16),
    _GntpVersion_Type()
)
gntpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpVersion.setStatus("current")


class _GntpKernelVersion_Type(DisplayString):
    """Custom type gntpKernelVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GntpKernelVersion_Type.__name__ = "DisplayString"
_GntpKernelVersion_Object = MibScalar
gntpKernelVersion = _GntpKernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 17),
    _GntpKernelVersion_Type()
)
gntpKernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpKernelVersion.setStatus("current")


class _GntpOscType_Type(DisplayString):
    """Custom type gntpOscType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GntpOscType_Type.__name__ = "DisplayString"
_GntpOscType_Object = MibScalar
gntpOscType = _GntpOscType_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 18),
    _GntpOscType_Type()
)
gntpOscType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpOscType.setStatus("current")


class _GntpTimeMode_Type(DisplayString):
    """Custom type gntpTimeMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_GntpTimeMode_Type.__name__ = "DisplayString"
_GntpTimeMode_Object = MibScalar
gntpTimeMode = _GntpTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 19),
    _GntpTimeMode_Type()
)
gntpTimeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpTimeMode.setStatus("current")
_GntpLocalOffset_Type = Integer32
_GntpLocalOffset_Object = MibScalar
gntpLocalOffset = _GntpLocalOffset_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 20),
    _GntpLocalOffset_Type()
)
gntpLocalOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpLocalOffset.setStatus("current")


class _GntpDSTStartMonth_Type(Integer32):
    """Custom type gntpDSTStartMonth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_GntpDSTStartMonth_Type.__name__ = "Integer32"
_GntpDSTStartMonth_Object = MibScalar
gntpDSTStartMonth = _GntpDSTStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 21),
    _GntpDSTStartMonth_Type()
)
gntpDSTStartMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpDSTStartMonth.setStatus("current")


class _GntpDSTStartSunday_Type(Integer32):
    """Custom type gntpDSTStartSunday based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("firstSunday", 1),
          ("secondSunday", 2),
          ("thirdSunday", 3),
          ("fourthSunday", 4),
          ("lastSunday", 5))
    )


_GntpDSTStartSunday_Type.__name__ = "Integer32"
_GntpDSTStartSunday_Object = MibScalar
gntpDSTStartSunday = _GntpDSTStartSunday_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 22),
    _GntpDSTStartSunday_Type()
)
gntpDSTStartSunday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpDSTStartSunday.setStatus("current")
_GntpDSTStartHour_Type = Integer32
_GntpDSTStartHour_Object = MibScalar
gntpDSTStartHour = _GntpDSTStartHour_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 23),
    _GntpDSTStartHour_Type()
)
gntpDSTStartHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpDSTStartHour.setStatus("current")


class _GntpDSTStopMonth_Type(Integer32):
    """Custom type gntpDSTStopMonth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_GntpDSTStopMonth_Type.__name__ = "Integer32"
_GntpDSTStopMonth_Object = MibScalar
gntpDSTStopMonth = _GntpDSTStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 24),
    _GntpDSTStopMonth_Type()
)
gntpDSTStopMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpDSTStopMonth.setStatus("current")


class _GntpDSTStopSunday_Type(Integer32):
    """Custom type gntpDSTStopSunday based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("firstSunday", 1),
          ("secondSunday", 2),
          ("thirdSunday", 3),
          ("fourthSunday", 4),
          ("lastSunday", 5))
    )


_GntpDSTStopSunday_Type.__name__ = "Integer32"
_GntpDSTStopSunday_Object = MibScalar
gntpDSTStopSunday = _GntpDSTStopSunday_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 25),
    _GntpDSTStopSunday_Type()
)
gntpDSTStopSunday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpDSTStopSunday.setStatus("current")
_GntpDSTStopHour_Type = Integer32
_GntpDSTStopHour_Object = MibScalar
gntpDSTStopHour = _GntpDSTStopHour_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 26),
    _GntpDSTStopHour_Type()
)
gntpDSTStopHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpDSTStopHour.setStatus("current")


class _GntpCPUDieTemperature_Type(DisplayString):
    """Custom type gntpCPUDieTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GntpCPUDieTemperature_Type.__name__ = "DisplayString"
_GntpCPUDieTemperature_Object = MibScalar
gntpCPUDieTemperature = _GntpCPUDieTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 27),
    _GntpCPUDieTemperature_Type()
)
gntpCPUDieTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpCPUDieTemperature.setStatus("current")
_GntpCPUFreeMemory_Type = Integer32
_GntpCPUFreeMemory_Object = MibScalar
gntpCPUFreeMemory = _GntpCPUFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 28),
    _GntpCPUFreeMemory_Type()
)
gntpCPUFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpCPUFreeMemory.setStatus("current")
_GntpCPULoadAveragePerCent_Type = Integer32
_GntpCPULoadAveragePerCent_Object = MibScalar
gntpCPULoadAveragePerCent = _GntpCPULoadAveragePerCent_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 29),
    _GntpCPULoadAveragePerCent_Type()
)
gntpCPULoadAveragePerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpCPULoadAveragePerCent.setStatus("current")
_Gps_ObjectIdentity = ObjectIdentity
gps = _Gps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2)
)
_Gpstrap_ObjectIdentity = ObjectIdentity
gpstrap = _Gpstrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 0)
)


class _GpsFaultStatus_Type(Bits):
    """Custom type gpsFaultStatus based on Bits"""
    namedValues = NamedValues(
        *(("gpsAntennaFlt", 0),
          ("gpsNTPNotPolling", 1),
          ("gpsRefTimeFlt", 2),
          ("gpsReceiverCommFlt", 3),
          ("gpsFLASHWriteFlt", 4),
          ("gpsFPGACfgFlt", 5),
          ("gpsNoSignalTimeout", 6),
          ("gpsDACNearLimit", 7))
    )

_GpsFaultStatus_Type.__name__ = "Bits"
_GpsFaultStatus_Object = MibScalar
gpsFaultStatus = _GpsFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 1),
    _GpsFaultStatus_Type()
)
gpsFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsFaultStatus.setStatus("current")


class _GpsFault2Status_Type(Bits):
    """Custom type gpsFault2Status based on Bits"""
    namedValues = NamedValues(
        *(("gpsSysPwrOvld", 0),
          ("gpsNotUsed1", 1),
          ("gpsNotUsed2", 2),
          ("gpsNotUsed3", 3),
          ("gpsNotUsed4", 4),
          ("gpsOscPLLFlt", 5),
          ("gpsSecPwrSplyFlt", 6),
          ("gpsPriPwrSplyFlt", 7))
    )

_GpsFault2Status_Type.__name__ = "Bits"
_GpsFault2Status_Object = MibScalar
gpsFault2Status = _GpsFault2Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 2),
    _GpsFault2Status_Type()
)
gpsFault2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsFault2Status.setStatus("current")


class _GpsTimeFigureOfMerit_Type(Integer32):
    """Custom type gpsTimeFigureOfMerit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("lessthan100ns", 3),
          ("lessthan1us", 4),
          ("lessthan10us", 5),
          ("lessthan100us", 6),
          ("lessthan1ms", 7),
          ("lessthan10ms", 8),
          ("greaterthan10ms", 9))
    )


_GpsTimeFigureOfMerit_Type.__name__ = "Integer32"
_GpsTimeFigureOfMerit_Object = MibScalar
gpsTimeFigureOfMerit = _GpsTimeFigureOfMerit_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 3),
    _GpsTimeFigureOfMerit_Type()
)
gpsTimeFigureOfMerit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsTimeFigureOfMerit.setStatus("current")


class _GpsSigProcState_Type(DisplayString):
    """Custom type gpsSigProcState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_GpsSigProcState_Type.__name__ = "DisplayString"
_GpsSigProcState_Object = MibScalar
gpsSigProcState = _GpsSigProcState_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 4),
    _GpsSigProcState_Type()
)
gpsSigProcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSigProcState.setStatus("current")


class _GpsNumTrackSats_Type(Integer32):
    """Custom type gpsNumTrackSats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_GpsNumTrackSats_Type.__name__ = "Integer32"
_GpsNumTrackSats_Object = MibScalar
gpsNumTrackSats = _GpsNumTrackSats_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 5),
    _GpsNumTrackSats_Type()
)
gpsNumTrackSats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsNumTrackSats.setStatus("current")


class _GpsAvgCarrierToNoiseRatiodB_Type(DisplayString):
    """Custom type gpsAvgCarrierToNoiseRatiodB based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_GpsAvgCarrierToNoiseRatiodB_Type.__name__ = "DisplayString"
_GpsAvgCarrierToNoiseRatiodB_Object = MibScalar
gpsAvgCarrierToNoiseRatiodB = _GpsAvgCarrierToNoiseRatiodB_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 6),
    _GpsAvgCarrierToNoiseRatiodB_Type()
)
gpsAvgCarrierToNoiseRatiodB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAvgCarrierToNoiseRatiodB.setStatus("current")


class _GpsChannelTrkStat1_Type(DisplayString):
    """Custom type gpsChannelTrkStat1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GpsChannelTrkStat1_Type.__name__ = "DisplayString"
_GpsChannelTrkStat1_Object = MibScalar
gpsChannelTrkStat1 = _GpsChannelTrkStat1_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 7),
    _GpsChannelTrkStat1_Type()
)
gpsChannelTrkStat1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsChannelTrkStat1.setStatus("current")


class _GpsChannelTrkStat2_Type(DisplayString):
    """Custom type gpsChannelTrkStat2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GpsChannelTrkStat2_Type.__name__ = "DisplayString"
_GpsChannelTrkStat2_Object = MibScalar
gpsChannelTrkStat2 = _GpsChannelTrkStat2_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 8),
    _GpsChannelTrkStat2_Type()
)
gpsChannelTrkStat2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsChannelTrkStat2.setStatus("current")


class _GpsChannelTrkStat3_Type(DisplayString):
    """Custom type gpsChannelTrkStat3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GpsChannelTrkStat3_Type.__name__ = "DisplayString"
_GpsChannelTrkStat3_Object = MibScalar
gpsChannelTrkStat3 = _GpsChannelTrkStat3_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 9),
    _GpsChannelTrkStat3_Type()
)
gpsChannelTrkStat3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsChannelTrkStat3.setStatus("current")


class _GpsChannelTrkStat4_Type(DisplayString):
    """Custom type gpsChannelTrkStat4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GpsChannelTrkStat4_Type.__name__ = "DisplayString"
_GpsChannelTrkStat4_Object = MibScalar
gpsChannelTrkStat4 = _GpsChannelTrkStat4_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 10),
    _GpsChannelTrkStat4_Type()
)
gpsChannelTrkStat4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsChannelTrkStat4.setStatus("current")


class _GpsChannelTrkStat5_Type(DisplayString):
    """Custom type gpsChannelTrkStat5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GpsChannelTrkStat5_Type.__name__ = "DisplayString"
_GpsChannelTrkStat5_Object = MibScalar
gpsChannelTrkStat5 = _GpsChannelTrkStat5_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 11),
    _GpsChannelTrkStat5_Type()
)
gpsChannelTrkStat5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsChannelTrkStat5.setStatus("current")


class _GpsChannelTrkStat6_Type(DisplayString):
    """Custom type gpsChannelTrkStat6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GpsChannelTrkStat6_Type.__name__ = "DisplayString"
_GpsChannelTrkStat6_Object = MibScalar
gpsChannelTrkStat6 = _GpsChannelTrkStat6_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 12),
    _GpsChannelTrkStat6_Type()
)
gpsChannelTrkStat6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsChannelTrkStat6.setStatus("current")


class _GpsChannelTrkStat7_Type(DisplayString):
    """Custom type gpsChannelTrkStat7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GpsChannelTrkStat7_Type.__name__ = "DisplayString"
_GpsChannelTrkStat7_Object = MibScalar
gpsChannelTrkStat7 = _GpsChannelTrkStat7_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 13),
    _GpsChannelTrkStat7_Type()
)
gpsChannelTrkStat7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsChannelTrkStat7.setStatus("current")


class _GpsChannelTrkStat8_Type(DisplayString):
    """Custom type gpsChannelTrkStat8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GpsChannelTrkStat8_Type.__name__ = "DisplayString"
_GpsChannelTrkStat8_Object = MibScalar
gpsChannelTrkStat8 = _GpsChannelTrkStat8_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 14),
    _GpsChannelTrkStat8_Type()
)
gpsChannelTrkStat8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsChannelTrkStat8.setStatus("current")


class _GpsChannelTrkStat9_Type(DisplayString):
    """Custom type gpsChannelTrkStat9 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GpsChannelTrkStat9_Type.__name__ = "DisplayString"
_GpsChannelTrkStat9_Object = MibScalar
gpsChannelTrkStat9 = _GpsChannelTrkStat9_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 15),
    _GpsChannelTrkStat9_Type()
)
gpsChannelTrkStat9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsChannelTrkStat9.setStatus("current")


class _GpsChannelTrkStat10_Type(DisplayString):
    """Custom type gpsChannelTrkStat10 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GpsChannelTrkStat10_Type.__name__ = "DisplayString"
_GpsChannelTrkStat10_Object = MibScalar
gpsChannelTrkStat10 = _GpsChannelTrkStat10_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 16),
    _GpsChannelTrkStat10_Type()
)
gpsChannelTrkStat10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsChannelTrkStat10.setStatus("current")


class _GpsChannelTrkStat11_Type(DisplayString):
    """Custom type gpsChannelTrkStat11 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GpsChannelTrkStat11_Type.__name__ = "DisplayString"
_GpsChannelTrkStat11_Object = MibScalar
gpsChannelTrkStat11 = _GpsChannelTrkStat11_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 17),
    _GpsChannelTrkStat11_Type()
)
gpsChannelTrkStat11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsChannelTrkStat11.setStatus("current")


class _GpsChannelTrkStat12_Type(DisplayString):
    """Custom type gpsChannelTrkStat12 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GpsChannelTrkStat12_Type.__name__ = "DisplayString"
_GpsChannelTrkStat12_Object = MibScalar
gpsChannelTrkStat12 = _GpsChannelTrkStat12_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 18),
    _GpsChannelTrkStat12_Type()
)
gpsChannelTrkStat12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsChannelTrkStat12.setStatus("current")


class _GpsLastPositionFix_Type(DisplayString):
    """Custom type gpsLastPositionFix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GpsLastPositionFix_Type.__name__ = "DisplayString"
_GpsLastPositionFix_Object = MibScalar
gpsLastPositionFix = _GpsLastPositionFix_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 19),
    _GpsLastPositionFix_Type()
)
gpsLastPositionFix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLastPositionFix.setStatus("current")


class _GpsReferencePosition_Type(DisplayString):
    """Custom type gpsReferencePosition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GpsReferencePosition_Type.__name__ = "DisplayString"
_GpsReferencePosition_Object = MibScalar
gpsReferencePosition = _GpsReferencePosition_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 20),
    _GpsReferencePosition_Type()
)
gpsReferencePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsReferencePosition.setStatus("current")


class _GpsRefPosSource_Type(DisplayString):
    """Custom type gpsRefPosSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_GpsRefPosSource_Type.__name__ = "DisplayString"
_GpsRefPosSource_Object = MibScalar
gpsRefPosSource = _GpsRefPosSource_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 21),
    _GpsRefPosSource_Type()
)
gpsRefPosSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsRefPosSource.setStatus("current")
_GpsCurrentLeapSeconds_Type = Integer32
_GpsCurrentLeapSeconds_Object = MibScalar
gpsCurrentLeapSeconds = _GpsCurrentLeapSeconds_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 22),
    _GpsCurrentLeapSeconds_Type()
)
gpsCurrentLeapSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsCurrentLeapSeconds.setStatus("current")
_GpsFutureLeapSeconds_Type = Integer32
_GpsFutureLeapSeconds_Object = MibScalar
gpsFutureLeapSeconds = _GpsFutureLeapSeconds_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 23),
    _GpsFutureLeapSeconds_Type()
)
gpsFutureLeapSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsFutureLeapSeconds.setStatus("current")
_GpsAlmanacLS_Type = Integer32
_GpsAlmanacLS_Object = MibScalar
gpsAlmanacLS = _GpsAlmanacLS_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 24),
    _GpsAlmanacLS_Type()
)
gpsAlmanacLS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacLS.setStatus("current")
_GpsAlmanacLSF_Type = Integer32
_GpsAlmanacLSF_Object = MibScalar
gpsAlmanacLSF = _GpsAlmanacLSF_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 25),
    _GpsAlmanacLSF_Type()
)
gpsAlmanacLSF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacLSF.setStatus("current")
_GpsAlmanacUTCWNlsf_Type = Integer32
_GpsAlmanacUTCWNlsf_Object = MibScalar
gpsAlmanacUTCWNlsf = _GpsAlmanacUTCWNlsf_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 26),
    _GpsAlmanacUTCWNlsf_Type()
)
gpsAlmanacUTCWNlsf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacUTCWNlsf.setStatus("current")
_GpsAlmanacUTCDN_Type = Integer32
_GpsAlmanacUTCDN_Object = MibScalar
gpsAlmanacUTCDN = _GpsAlmanacUTCDN_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 27),
    _GpsAlmanacUTCDN_Type()
)
gpsAlmanacUTCDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacUTCDN.setStatus("current")


class _GpsAlmanacA0_Type(DisplayString):
    """Custom type gpsAlmanacA0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsAlmanacA0_Type.__name__ = "DisplayString"
_GpsAlmanacA0_Object = MibScalar
gpsAlmanacA0 = _GpsAlmanacA0_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 28),
    _GpsAlmanacA0_Type()
)
gpsAlmanacA0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacA0.setStatus("current")


class _GpsAlmanacA1_Type(DisplayString):
    """Custom type gpsAlmanacA1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsAlmanacA1_Type.__name__ = "DisplayString"
_GpsAlmanacA1_Object = MibScalar
gpsAlmanacA1 = _GpsAlmanacA1_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 29),
    _GpsAlmanacA1_Type()
)
gpsAlmanacA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacA1.setStatus("current")
_GpsAlmanacUTCWNt_Type = Integer32
_GpsAlmanacUTCWNt_Object = MibScalar
gpsAlmanacUTCWNt = _GpsAlmanacUTCWNt_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 30),
    _GpsAlmanacUTCWNt_Type()
)
gpsAlmanacUTCWNt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacUTCWNt.setStatus("current")
_GpsAlmanacUTCtot_Type = Integer32
_GpsAlmanacUTCtot_Object = MibScalar
gpsAlmanacUTCtot = _GpsAlmanacUTCtot_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 31),
    _GpsAlmanacUTCtot_Type()
)
gpsAlmanacUTCtot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacUTCtot.setStatus("current")
_GpsGPSminusUTCOffset_Type = Integer32
_GpsGPSminusUTCOffset_Object = MibScalar
gpsGPSminusUTCOffset = _GpsGPSminusUTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 32),
    _GpsGPSminusUTCOffset_Type()
)
gpsGPSminusUTCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsGPSminusUTCOffset.setStatus("current")


class _GpsVersion_Type(DisplayString):
    """Custom type gpsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsVersion_Type.__name__ = "DisplayString"
_GpsVersion_Object = MibScalar
gpsVersion = _GpsVersion_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 33),
    _GpsVersion_Type()
)
gpsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsVersion.setStatus("current")


class _GpsDynamicMode_Type(Integer32):
    """Custom type gpsDynamicMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("gpsDynModeOFF", 0),
          ("gpsDynModeON", 1))
    )


_GpsDynamicMode_Type.__name__ = "Integer32"
_GpsDynamicMode_Object = MibScalar
gpsDynamicMode = _GpsDynamicMode_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 34),
    _GpsDynamicMode_Type()
)
gpsDynamicMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsDynamicMode.setStatus("current")


class _GpsCalibrationDelay_Type(Integer32):
    """Custom type gpsCalibrationDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500000, 500000),
    )


_GpsCalibrationDelay_Type.__name__ = "Integer32"
_GpsCalibrationDelay_Object = MibScalar
gpsCalibrationDelay = _GpsCalibrationDelay_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 35),
    _GpsCalibrationDelay_Type()
)
gpsCalibrationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsCalibrationDelay.setStatus("current")


class _GpsCoastDuration_Type(Integer32):
    """Custom type gpsCoastDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GpsCoastDuration_Type.__name__ = "Integer32"
_GpsCoastDuration_Object = MibScalar
gpsCoastDuration = _GpsCoastDuration_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 36),
    _GpsCoastDuration_Type()
)
gpsCoastDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsCoastDuration.setStatus("current")


class _GpsEstimatedTimeError_Type(DisplayString):
    """Custom type gpsEstimatedTimeError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsEstimatedTimeError_Type.__name__ = "DisplayString"
_GpsEstimatedTimeError_Object = MibScalar
gpsEstimatedTimeError = _GpsEstimatedTimeError_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 37),
    _GpsEstimatedTimeError_Type()
)
gpsEstimatedTimeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsEstimatedTimeError.setStatus("current")


class _GpsMeasuredTimeError_Type(DisplayString):
    """Custom type gpsMeasuredTimeError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsMeasuredTimeError_Type.__name__ = "DisplayString"
_GpsMeasuredTimeError_Object = MibScalar
gpsMeasuredTimeError = _GpsMeasuredTimeError_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 38),
    _GpsMeasuredTimeError_Type()
)
gpsMeasuredTimeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsMeasuredTimeError.setStatus("current")


class _GpsMeasurementTimeDeviation_Type(DisplayString):
    """Custom type gpsMeasurementTimeDeviation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsMeasurementTimeDeviation_Type.__name__ = "DisplayString"
_GpsMeasurementTimeDeviation_Object = MibScalar
gpsMeasurementTimeDeviation = _GpsMeasurementTimeDeviation_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 39),
    _GpsMeasurementTimeDeviation_Type()
)
gpsMeasurementTimeDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsMeasurementTimeDeviation.setStatus("current")


class _GpsOSCDAC_Type(Integer32):
    """Custom type gpsOSCDAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_GpsOSCDAC_Type.__name__ = "Integer32"
_GpsOSCDAC_Object = MibScalar
gpsOSCDAC = _GpsOSCDAC_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 40),
    _GpsOSCDAC_Type()
)
gpsOSCDAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsOSCDAC.setStatus("current")


class _GpsMeasuredOscillatorAgeing_Type(DisplayString):
    """Custom type gpsMeasuredOscillatorAgeing based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsMeasuredOscillatorAgeing_Type.__name__ = "DisplayString"
_GpsMeasuredOscillatorAgeing_Object = MibScalar
gpsMeasuredOscillatorAgeing = _GpsMeasuredOscillatorAgeing_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 41),
    _GpsMeasuredOscillatorAgeing_Type()
)
gpsMeasuredOscillatorAgeing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsMeasuredOscillatorAgeing.setStatus("current")


class _GpsControlLoopTimeConstant_Type(DisplayString):
    """Custom type gpsControlLoopTimeConstant based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsControlLoopTimeConstant_Type.__name__ = "DisplayString"
_GpsControlLoopTimeConstant_Object = MibScalar
gpsControlLoopTimeConstant = _GpsControlLoopTimeConstant_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 42),
    _GpsControlLoopTimeConstant_Type()
)
gpsControlLoopTimeConstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsControlLoopTimeConstant.setStatus("current")


class _GpsInternalTemperature_Type(DisplayString):
    """Custom type gpsInternalTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsInternalTemperature_Type.__name__ = "DisplayString"
_GpsInternalTemperature_Object = MibScalar
gpsInternalTemperature = _GpsInternalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 43),
    _GpsInternalTemperature_Type()
)
gpsInternalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsInternalTemperature.setStatus("current")


class _GpsAntennaFaultMask_Type(DisplayString):
    """Custom type gpsAntennaFaultMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GpsAntennaFaultMask_Type.__name__ = "DisplayString"
_GpsAntennaFaultMask_Object = MibScalar
gpsAntennaFaultMask = _GpsAntennaFaultMask_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 44),
    _GpsAntennaFaultMask_Type()
)
gpsAntennaFaultMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAntennaFaultMask.setStatus("current")


class _GpsSignalLossFaultMask_Type(DisplayString):
    """Custom type gpsSignalLossFaultMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GpsSignalLossFaultMask_Type.__name__ = "DisplayString"
_GpsSignalLossFaultMask_Object = MibScalar
gpsSignalLossFaultMask = _GpsSignalLossFaultMask_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 45),
    _GpsSignalLossFaultMask_Type()
)
gpsSignalLossFaultMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSignalLossFaultMask.setStatus("current")


class _GpsPrimaryPowerFaultAlarmMask_Type(DisplayString):
    """Custom type gpsPrimaryPowerFaultAlarmMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GpsPrimaryPowerFaultAlarmMask_Type.__name__ = "DisplayString"
_GpsPrimaryPowerFaultAlarmMask_Object = MibScalar
gpsPrimaryPowerFaultAlarmMask = _GpsPrimaryPowerFaultAlarmMask_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 46),
    _GpsPrimaryPowerFaultAlarmMask_Type()
)
gpsPrimaryPowerFaultAlarmMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsPrimaryPowerFaultAlarmMask.setStatus("current")


class _GpsSecondaryPowerFaultAlarmMask_Type(DisplayString):
    """Custom type gpsSecondaryPowerFaultAlarmMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GpsSecondaryPowerFaultAlarmMask_Type.__name__ = "DisplayString"
_GpsSecondaryPowerFaultAlarmMask_Object = MibScalar
gpsSecondaryPowerFaultAlarmMask = _GpsSecondaryPowerFaultAlarmMask_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 47),
    _GpsSecondaryPowerFaultAlarmMask_Type()
)
gpsSecondaryPowerFaultAlarmMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSecondaryPowerFaultAlarmMask.setStatus("current")


class _GpsFaultNibble0Status_Type(Bits):
    """Custom type gpsFaultNibble0Status based on Bits"""
    namedValues = NamedValues(
        *(("gpsFLASHWriteFlt", 0),
          ("gpsFPGACfgFlt", 1),
          ("gpsNoSignalTimeout", 2),
          ("gpsDACNearLimit", 3))
    )

_GpsFaultNibble0Status_Type.__name__ = "Bits"
_GpsFaultNibble0Status_Object = MibScalar
gpsFaultNibble0Status = _GpsFaultNibble0Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 48),
    _GpsFaultNibble0Status_Type()
)
gpsFaultNibble0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsFaultNibble0Status.setStatus("current")


class _GpsFaultNibble1Status_Type(Bits):
    """Custom type gpsFaultNibble1Status based on Bits"""
    namedValues = NamedValues(
        *(("gpsAntennaFlt", 0),
          ("gpsNTPNotPolling", 1),
          ("gpsRefTimeFlt", 2),
          ("gpsReceiverCommFlt", 3))
    )

_GpsFaultNibble1Status_Type.__name__ = "Bits"
_GpsFaultNibble1Status_Object = MibScalar
gpsFaultNibble1Status = _GpsFaultNibble1Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 49),
    _GpsFaultNibble1Status_Type()
)
gpsFaultNibble1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsFaultNibble1Status.setStatus("current")


class _GpsFaultNibble2Status_Type(Bits):
    """Custom type gpsFaultNibble2Status based on Bits"""
    namedValues = NamedValues(
        *(("gpsNotUsed4", 0),
          ("gpsOscPLLFlt", 1),
          ("gpsSecPwrSplyFlt", 2),
          ("gpsPriPwrSplyFlt", 3))
    )

_GpsFaultNibble2Status_Type.__name__ = "Bits"
_GpsFaultNibble2Status_Object = MibScalar
gpsFaultNibble2Status = _GpsFaultNibble2Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 50),
    _GpsFaultNibble2Status_Type()
)
gpsFaultNibble2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsFaultNibble2Status.setStatus("current")


class _GpsFaultNibble3Status_Type(Bits):
    """Custom type gpsFaultNibble3Status based on Bits"""
    namedValues = NamedValues(
        *(("gpsSysPwrOvld", 0),
          ("gpsNotUsed1", 1),
          ("gpsNotUsed2", 2),
          ("gpsNotUsed3", 3))
    )

_GpsFaultNibble3Status_Type.__name__ = "Bits"
_GpsFaultNibble3Status_Object = MibScalar
gpsFaultNibble3Status = _GpsFaultNibble3Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 51),
    _GpsFaultNibble3Status_Type()
)
gpsFaultNibble3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsFaultNibble3Status.setStatus("current")
_GCPUIO_ObjectIdentity = ObjectIdentity
gCPUIO = _GCPUIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 12, 3)
)


class _Gsysio1PPSWidth_Type(DisplayString):
    """Custom type gsysio1PPSWidth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Gsysio1PPSWidth_Type.__name__ = "DisplayString"
_Gsysio1PPSWidth_Object = MibScalar
gsysio1PPSWidth = _Gsysio1PPSWidth_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 3, 1),
    _Gsysio1PPSWidth_Type()
)
gsysio1PPSWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsysio1PPSWidth.setStatus("current")


class _GsysioTimeCodeFormat_Type(DisplayString):
    """Custom type gsysioTimeCodeFormat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GsysioTimeCodeFormat_Type.__name__ = "DisplayString"
_GsysioTimeCodeFormat_Object = MibScalar
gsysioTimeCodeFormat = _GsysioTimeCodeFormat_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 3, 2),
    _GsysioTimeCodeFormat_Type()
)
gsysioTimeCodeFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsysioTimeCodeFormat.setStatus("current")


class _GsysioSynthesizerHz_Type(Integer32):
    """Custom type gsysioSynthesizerHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_GsysioSynthesizerHz_Type.__name__ = "Integer32"
_GsysioSynthesizerHz_Object = MibScalar
gsysioSynthesizerHz = _GsysioSynthesizerHz_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 3, 3),
    _GsysioSynthesizerHz_Type()
)
gsysioSynthesizerHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsysioSynthesizerHz.setStatus("current")


class _GsysioSerialTimeOutputBaudrate_Type(DisplayString):
    """Custom type gsysioSerialTimeOutputBaudrate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GsysioSerialTimeOutputBaudrate_Type.__name__ = "DisplayString"
_GsysioSerialTimeOutputBaudrate_Object = MibScalar
gsysioSerialTimeOutputBaudrate = _GsysioSerialTimeOutputBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 3, 4),
    _GsysioSerialTimeOutputBaudrate_Type()
)
gsysioSerialTimeOutputBaudrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsysioSerialTimeOutputBaudrate.setStatus("current")


class _GsysioSerialTimeOutputFormat_Type(DisplayString):
    """Custom type gsysioSerialTimeOutputFormat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GsysioSerialTimeOutputFormat_Type.__name__ = "DisplayString"
_GsysioSerialTimeOutputFormat_Object = MibScalar
gsysioSerialTimeOutputFormat = _GsysioSerialTimeOutputFormat_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 3, 5),
    _GsysioSerialTimeOutputFormat_Type()
)
gsysioSerialTimeOutputFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsysioSerialTimeOutputFormat.setStatus("current")


class _GsysioSerialTimeOutputParity_Type(DisplayString):
    """Custom type gsysioSerialTimeOutputParity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GsysioSerialTimeOutputParity_Type.__name__ = "DisplayString"
_GsysioSerialTimeOutputParity_Object = MibScalar
gsysioSerialTimeOutputParity = _GsysioSerialTimeOutputParity_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 3, 6),
    _GsysioSerialTimeOutputParity_Type()
)
gsysioSerialTimeOutputParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsysioSerialTimeOutputParity.setStatus("current")


class _GsysioSerialTimeNMEASentence1_Type(DisplayString):
    """Custom type gsysioSerialTimeNMEASentence1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GsysioSerialTimeNMEASentence1_Type.__name__ = "DisplayString"
_GsysioSerialTimeNMEASentence1_Object = MibScalar
gsysioSerialTimeNMEASentence1 = _GsysioSerialTimeNMEASentence1_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 3, 7),
    _GsysioSerialTimeNMEASentence1_Type()
)
gsysioSerialTimeNMEASentence1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsysioSerialTimeNMEASentence1.setStatus("current")


class _GsysioSerialTimeNMEASentence2_Type(DisplayString):
    """Custom type gsysioSerialTimeNMEASentence2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GsysioSerialTimeNMEASentence2_Type.__name__ = "DisplayString"
_GsysioSerialTimeNMEASentence2_Object = MibScalar
gsysioSerialTimeNMEASentence2 = _GsysioSerialTimeNMEASentence2_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 3, 8),
    _GsysioSerialTimeNMEASentence2_Type()
)
gsysioSerialTimeNMEASentence2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsysioSerialTimeNMEASentence2.setStatus("current")


class _GsysioSerialTimeNMEASentence3_Type(DisplayString):
    """Custom type gsysioSerialTimeNMEASentence3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GsysioSerialTimeNMEASentence3_Type.__name__ = "DisplayString"
_GsysioSerialTimeNMEASentence3_Object = MibScalar
gsysioSerialTimeNMEASentence3 = _GsysioSerialTimeNMEASentence3_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 3, 9),
    _GsysioSerialTimeNMEASentence3_Type()
)
gsysioSerialTimeNMEASentence3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsysioSerialTimeNMEASentence3.setStatus("current")


class _GcpuioConnA_Type(DisplayString):
    """Custom type gcpuioConnA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GcpuioConnA_Type.__name__ = "DisplayString"
_GcpuioConnA_Object = MibScalar
gcpuioConnA = _GcpuioConnA_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 3, 10),
    _GcpuioConnA_Type()
)
gcpuioConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gcpuioConnA.setStatus("current")


class _GcpuioConnB_Type(DisplayString):
    """Custom type gcpuioConnB based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GcpuioConnB_Type.__name__ = "DisplayString"
_GcpuioConnB_Object = MibScalar
gcpuioConnB = _GcpuioConnB_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 3, 11),
    _GcpuioConnB_Type()
)
gcpuioConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gcpuioConnB.setStatus("current")


class _GcpuioConnC_Type(DisplayString):
    """Custom type gcpuioConnC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GcpuioConnC_Type.__name__ = "DisplayString"
_GcpuioConnC_Object = MibScalar
gcpuioConnC = _GcpuioConnC_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 3, 12),
    _GcpuioConnC_Type()
)
gcpuioConnC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gcpuioConnC.setStatus("current")
_Gptp0_ObjectIdentity = ObjectIdentity
gptp0 = _Gptp0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4)
)
_Gptp0Version_Type = Integer32
_Gptp0Version_Object = MibScalar
gptp0Version = _Gptp0Version_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 1),
    _Gptp0Version_Type()
)
gptp0Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0Version.setStatus("current")


class _Gptp0SyncInterval_Type(Integer32):
    """Custom type gptp0SyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-7,
              -6,
              -5,
              -4,
              -3,
              -2,
              -1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("msec8", -7),
          ("msec16", -6),
          ("msec31", -5),
          ("msec63", -4),
          ("msec125", -3),
          ("msec250", -2),
          ("msec500", -1),
          ("sec1", 0))
    )


_Gptp0SyncInterval_Type.__name__ = "Integer32"
_Gptp0SyncInterval_Object = MibScalar
gptp0SyncInterval = _Gptp0SyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 2),
    _Gptp0SyncInterval_Type()
)
gptp0SyncInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0SyncInterval.setStatus("current")


class _Gptp0AnnounceInterval_Type(Integer32):
    """Custom type gptp0AnnounceInterval based on Integer32"""
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
        *(("sec1", 0),
          ("sec2", 1),
          ("sec4", 2),
          ("sec8", 3),
          ("sec16", 4))
    )


_Gptp0AnnounceInterval_Type.__name__ = "Integer32"
_Gptp0AnnounceInterval_Object = MibScalar
gptp0AnnounceInterval = _Gptp0AnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 3),
    _Gptp0AnnounceInterval_Type()
)
gptp0AnnounceInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0AnnounceInterval.setStatus("current")
_Gptp0Priority1_Type = Integer32
_Gptp0Priority1_Object = MibScalar
gptp0Priority1 = _Gptp0Priority1_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 4),
    _Gptp0Priority1_Type()
)
gptp0Priority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0Priority1.setStatus("current")
_Gptp0Priority2_Type = Integer32
_Gptp0Priority2_Object = MibScalar
gptp0Priority2 = _Gptp0Priority2_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 5),
    _Gptp0Priority2_Type()
)
gptp0Priority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0Priority2.setStatus("current")


class _Gptp0DelayMechanism_Type(Integer32):
    """Custom type gptp0DelayMechanism based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              254)
        )
    )
    namedValues = NamedValues(
        *(("e2e", 0),
          ("p2p", 1),
          ("disabled", 254))
    )


_Gptp0DelayMechanism_Type.__name__ = "Integer32"
_Gptp0DelayMechanism_Object = MibScalar
gptp0DelayMechanism = _Gptp0DelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 6),
    _Gptp0DelayMechanism_Type()
)
gptp0DelayMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0DelayMechanism.setStatus("current")
_Gptp0Domain_Type = Integer32
_Gptp0Domain_Object = MibScalar
gptp0Domain = _Gptp0Domain_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 7),
    _Gptp0Domain_Type()
)
gptp0Domain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0Domain.setStatus("current")


class _Gptp0TimeMode_Type(Integer32):
    """Custom type gptp0TimeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("utc", 0),
          ("ptp", 1))
    )


_Gptp0TimeMode_Type.__name__ = "Integer32"
_Gptp0TimeMode_Object = MibScalar
gptp0TimeMode = _Gptp0TimeMode_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 8),
    _Gptp0TimeMode_Type()
)
gptp0TimeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0TimeMode.setStatus("current")
_Gptp0TTL_Type = Integer32
_Gptp0TTL_Object = MibScalar
gptp0TTL = _Gptp0TTL_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 9),
    _Gptp0TTL_Type()
)
gptp0TTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0TTL.setStatus("current")


class _Gptp0ClockClass_Type(Integer32):
    """Custom type gptp0ClockClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              13,
              14,
              52,
              58)
        )
    )
    namedValues = NamedValues(
        *(("lockedPTP", 6),
          ("holdoverPTP", 7),
          ("lockedARB", 13),
          ("holdoverARB", 14),
          ("unlockedPTP", 52),
          ("unlockedARB", 58))
    )


_Gptp0ClockClass_Type.__name__ = "Integer32"
_Gptp0ClockClass_Object = MibScalar
gptp0ClockClass = _Gptp0ClockClass_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 10),
    _Gptp0ClockClass_Type()
)
gptp0ClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0ClockClass.setStatus("current")


class _Gptp0TimeScale_Type(Integer32):
    """Custom type gptp0TimeScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("arb", 0),
          ("ptp", 1))
    )


_Gptp0TimeScale_Type.__name__ = "Integer32"
_Gptp0TimeScale_Object = MibScalar
gptp0TimeScale = _Gptp0TimeScale_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 11),
    _Gptp0TimeScale_Type()
)
gptp0TimeScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0TimeScale.setStatus("current")


class _Gptp0PortState_Type(Integer32):
    """Custom type gptp0PortState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("faulty", 2),
          ("disabled", 3),
          ("listening", 4),
          ("preMaster", 5),
          ("master", 6),
          ("passive", 7),
          ("unCalibrated", 8),
          ("slave", 9))
    )


_Gptp0PortState_Type.__name__ = "Integer32"
_Gptp0PortState_Object = MibScalar
gptp0PortState = _Gptp0PortState_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 12),
    _Gptp0PortState_Type()
)
gptp0PortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0PortState.setStatus("current")


class _Gptp0TimeSource_Type(Integer32):
    """Custom type gptp0TimeSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              64,
              80,
              96,
              144,
              160)
        )
    )
    namedValues = NamedValues(
        *(("atom", 16),
          ("gps", 32),
          ("radio", 48),
          ("ptp", 64),
          ("ntp", 80),
          ("hand", 96),
          ("other", 144),
          ("oscillator", 160))
    )


_Gptp0TimeSource_Type.__name__ = "Integer32"
_Gptp0TimeSource_Object = MibScalar
gptp0TimeSource = _Gptp0TimeSource_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 13),
    _Gptp0TimeSource_Type()
)
gptp0TimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0TimeSource.setStatus("current")
_Gptp0UTCOffset_Type = Integer32
_Gptp0UTCOffset_Object = MibScalar
gptp0UTCOffset = _Gptp0UTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 14),
    _Gptp0UTCOffset_Type()
)
gptp0UTCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0UTCOffset.setStatus("current")


class _Gptp0UTCOffsetValid_Type(Integer32):
    """Custom type gptp0UTCOffsetValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Gptp0UTCOffsetValid_Type.__name__ = "Integer32"
_Gptp0UTCOffsetValid_Object = MibScalar
gptp0UTCOffsetValid = _Gptp0UTCOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 15),
    _Gptp0UTCOffsetValid_Type()
)
gptp0UTCOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0UTCOffsetValid.setStatus("current")


class _Gptp0ClockAccuracy_Type(Integer32):
    """Custom type gptp0ClockAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              254)
        )
    )
    namedValues = NamedValues(
        *(("nsec25", 32),
          ("nsec100", 33),
          ("nsec250", 34),
          ("nsec1000", 35),
          ("nsec2500", 36),
          ("usec10", 37),
          ("usec25", 38),
          ("usec100", 39),
          ("usec250", 40),
          ("usec1000", 41),
          ("usec2500", 42),
          ("msec10", 43),
          ("unknown", 254))
    )


_Gptp0ClockAccuracy_Type.__name__ = "Integer32"
_Gptp0ClockAccuracy_Object = MibScalar
gptp0ClockAccuracy = _Gptp0ClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 16),
    _Gptp0ClockAccuracy_Type()
)
gptp0ClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0ClockAccuracy.setStatus("current")


class _Gptp0Leap59_Type(Integer32):
    """Custom type gptp0Leap59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Gptp0Leap59_Type.__name__ = "Integer32"
_Gptp0Leap59_Object = MibScalar
gptp0Leap59 = _Gptp0Leap59_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 17),
    _Gptp0Leap59_Type()
)
gptp0Leap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0Leap59.setStatus("current")


class _Gptp0Leap61_Type(Integer32):
    """Custom type gptp0Leap61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Gptp0Leap61_Type.__name__ = "Integer32"
_Gptp0Leap61_Object = MibScalar
gptp0Leap61 = _Gptp0Leap61_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 18),
    _Gptp0Leap61_Type()
)
gptp0Leap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0Leap61.setStatus("current")


class _Gptp0TimeTraceable_Type(Integer32):
    """Custom type gptp0TimeTraceable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Gptp0TimeTraceable_Type.__name__ = "Integer32"
_Gptp0TimeTraceable_Object = MibScalar
gptp0TimeTraceable = _Gptp0TimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 19),
    _Gptp0TimeTraceable_Type()
)
gptp0TimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0TimeTraceable.setStatus("current")


class _Gptp0FreqTraceable_Type(Integer32):
    """Custom type gptp0FreqTraceable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Gptp0FreqTraceable_Type.__name__ = "Integer32"
_Gptp0FreqTraceable_Object = MibScalar
gptp0FreqTraceable = _Gptp0FreqTraceable_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 4, 20),
    _Gptp0FreqTraceable_Type()
)
gptp0FreqTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0FreqTraceable.setStatus("current")
_Gptp1_ObjectIdentity = ObjectIdentity
gptp1 = _Gptp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5)
)
_Gptp1Version_Type = Integer32
_Gptp1Version_Object = MibScalar
gptp1Version = _Gptp1Version_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 1),
    _Gptp1Version_Type()
)
gptp1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1Version.setStatus("current")


class _Gptp1SyncInterval_Type(Integer32):
    """Custom type gptp1SyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-7,
              -6,
              -5,
              -4,
              -3,
              -2,
              -1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("msec8", -7),
          ("msec16", -6),
          ("msec31", -5),
          ("msec63", -4),
          ("msec125", -3),
          ("msec250", -2),
          ("msec500", -1),
          ("sec1", 0))
    )


_Gptp1SyncInterval_Type.__name__ = "Integer32"
_Gptp1SyncInterval_Object = MibScalar
gptp1SyncInterval = _Gptp1SyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 2),
    _Gptp1SyncInterval_Type()
)
gptp1SyncInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1SyncInterval.setStatus("current")


class _Gptp1AnnounceInterval_Type(Integer32):
    """Custom type gptp1AnnounceInterval based on Integer32"""
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
        *(("sec1", 0),
          ("sec2", 1),
          ("sec4", 2),
          ("sec8", 3),
          ("sec16", 4))
    )


_Gptp1AnnounceInterval_Type.__name__ = "Integer32"
_Gptp1AnnounceInterval_Object = MibScalar
gptp1AnnounceInterval = _Gptp1AnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 3),
    _Gptp1AnnounceInterval_Type()
)
gptp1AnnounceInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1AnnounceInterval.setStatus("current")
_Gptp1Priority1_Type = Integer32
_Gptp1Priority1_Object = MibScalar
gptp1Priority1 = _Gptp1Priority1_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 4),
    _Gptp1Priority1_Type()
)
gptp1Priority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1Priority1.setStatus("current")
_Gptp1Priority2_Type = Integer32
_Gptp1Priority2_Object = MibScalar
gptp1Priority2 = _Gptp1Priority2_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 5),
    _Gptp1Priority2_Type()
)
gptp1Priority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1Priority2.setStatus("current")


class _Gptp1DelayMechanism_Type(Integer32):
    """Custom type gptp1DelayMechanism based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              254)
        )
    )
    namedValues = NamedValues(
        *(("e2e", 0),
          ("p2p", 1),
          ("disabled", 254))
    )


_Gptp1DelayMechanism_Type.__name__ = "Integer32"
_Gptp1DelayMechanism_Object = MibScalar
gptp1DelayMechanism = _Gptp1DelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 6),
    _Gptp1DelayMechanism_Type()
)
gptp1DelayMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1DelayMechanism.setStatus("current")
_Gptp1Domain_Type = Integer32
_Gptp1Domain_Object = MibScalar
gptp1Domain = _Gptp1Domain_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 7),
    _Gptp1Domain_Type()
)
gptp1Domain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1Domain.setStatus("current")


class _Gptp1TimeMode_Type(Integer32):
    """Custom type gptp1TimeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("utc", 0),
          ("ptp", 1))
    )


_Gptp1TimeMode_Type.__name__ = "Integer32"
_Gptp1TimeMode_Object = MibScalar
gptp1TimeMode = _Gptp1TimeMode_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 8),
    _Gptp1TimeMode_Type()
)
gptp1TimeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1TimeMode.setStatus("current")
_Gptp1TTL_Type = Integer32
_Gptp1TTL_Object = MibScalar
gptp1TTL = _Gptp1TTL_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 9),
    _Gptp1TTL_Type()
)
gptp1TTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1TTL.setStatus("current")


class _Gptp1ClockClass_Type(Integer32):
    """Custom type gptp1ClockClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              13,
              14,
              52,
              58)
        )
    )
    namedValues = NamedValues(
        *(("lockedPTP", 6),
          ("holdoverPTP", 7),
          ("lockedARB", 13),
          ("holdoverARB", 14),
          ("unlockedPTP", 52),
          ("unlockedARB", 58))
    )


_Gptp1ClockClass_Type.__name__ = "Integer32"
_Gptp1ClockClass_Object = MibScalar
gptp1ClockClass = _Gptp1ClockClass_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 10),
    _Gptp1ClockClass_Type()
)
gptp1ClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1ClockClass.setStatus("current")


class _Gptp1TimeScale_Type(Integer32):
    """Custom type gptp1TimeScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("arb", 0),
          ("ptp", 1))
    )


_Gptp1TimeScale_Type.__name__ = "Integer32"
_Gptp1TimeScale_Object = MibScalar
gptp1TimeScale = _Gptp1TimeScale_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 11),
    _Gptp1TimeScale_Type()
)
gptp1TimeScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1TimeScale.setStatus("current")


class _Gptp1PortState_Type(Integer32):
    """Custom type gptp1PortState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("faulty", 2),
          ("disabled", 3),
          ("listening", 4),
          ("preMaster", 5),
          ("master", 6),
          ("passive", 7),
          ("unCalibrated", 8),
          ("slave", 9))
    )


_Gptp1PortState_Type.__name__ = "Integer32"
_Gptp1PortState_Object = MibScalar
gptp1PortState = _Gptp1PortState_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 12),
    _Gptp1PortState_Type()
)
gptp1PortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1PortState.setStatus("current")


class _Gptp1TimeSource_Type(Integer32):
    """Custom type gptp1TimeSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              64,
              80,
              96,
              144,
              160)
        )
    )
    namedValues = NamedValues(
        *(("atom", 16),
          ("gps", 32),
          ("radio", 48),
          ("ptp", 64),
          ("ntp", 80),
          ("hand", 96),
          ("other", 144),
          ("oscillator", 160))
    )


_Gptp1TimeSource_Type.__name__ = "Integer32"
_Gptp1TimeSource_Object = MibScalar
gptp1TimeSource = _Gptp1TimeSource_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 13),
    _Gptp1TimeSource_Type()
)
gptp1TimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1TimeSource.setStatus("current")
_Gptp1UTCOffset_Type = Integer32
_Gptp1UTCOffset_Object = MibScalar
gptp1UTCOffset = _Gptp1UTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 14),
    _Gptp1UTCOffset_Type()
)
gptp1UTCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1UTCOffset.setStatus("current")


class _Gptp1UTCOffsetValid_Type(Integer32):
    """Custom type gptp1UTCOffsetValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Gptp1UTCOffsetValid_Type.__name__ = "Integer32"
_Gptp1UTCOffsetValid_Object = MibScalar
gptp1UTCOffsetValid = _Gptp1UTCOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 15),
    _Gptp1UTCOffsetValid_Type()
)
gptp1UTCOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1UTCOffsetValid.setStatus("current")


class _Gptp1ClockAccuracy_Type(Integer32):
    """Custom type gptp1ClockAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              254)
        )
    )
    namedValues = NamedValues(
        *(("nsec25", 32),
          ("nsec100", 33),
          ("nsec250", 34),
          ("nsec1000", 35),
          ("nsec2500", 36),
          ("usec10", 37),
          ("usec25", 38),
          ("usec100", 39),
          ("usec250", 40),
          ("usec1000", 41),
          ("usec2500", 42),
          ("msec10", 43),
          ("unknown", 254))
    )


_Gptp1ClockAccuracy_Type.__name__ = "Integer32"
_Gptp1ClockAccuracy_Object = MibScalar
gptp1ClockAccuracy = _Gptp1ClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 16),
    _Gptp1ClockAccuracy_Type()
)
gptp1ClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1ClockAccuracy.setStatus("current")


class _Gptp1Leap59_Type(Integer32):
    """Custom type gptp1Leap59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Gptp1Leap59_Type.__name__ = "Integer32"
_Gptp1Leap59_Object = MibScalar
gptp1Leap59 = _Gptp1Leap59_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 17),
    _Gptp1Leap59_Type()
)
gptp1Leap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1Leap59.setStatus("current")


class _Gptp1Leap61_Type(Integer32):
    """Custom type gptp1Leap61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Gptp1Leap61_Type.__name__ = "Integer32"
_Gptp1Leap61_Object = MibScalar
gptp1Leap61 = _Gptp1Leap61_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 18),
    _Gptp1Leap61_Type()
)
gptp1Leap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1Leap61.setStatus("current")


class _Gptp1TimeTraceable_Type(Integer32):
    """Custom type gptp1TimeTraceable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Gptp1TimeTraceable_Type.__name__ = "Integer32"
_Gptp1TimeTraceable_Object = MibScalar
gptp1TimeTraceable = _Gptp1TimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 19),
    _Gptp1TimeTraceable_Type()
)
gptp1TimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1TimeTraceable.setStatus("current")


class _Gptp1FreqTraceable_Type(Integer32):
    """Custom type gptp1FreqTraceable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Gptp1FreqTraceable_Type.__name__ = "Integer32"
_Gptp1FreqTraceable_Object = MibScalar
gptp1FreqTraceable = _Gptp1FreqTraceable_Object(
    (1, 3, 6, 1, 4, 1, 13827, 12, 5, 20),
    _Gptp1FreqTraceable_Type()
)
gptp1FreqTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1FreqTraceable.setStatus("current")

# Managed Objects groups


# Notification objects

cntpTrapLeapIndBitsChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 0, 1)
)
cntpTrapLeapIndBitsChange.setObjects(
    ("SONOMA-MIB", "cntpLeapIndBits")
)
if mibBuilder.loadTexts:
    cntpTrapLeapIndBitsChange.setStatus(
        "current"
    )

cntpTrapStratumChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 11, 1, 0, 2)
)
cntpTrapStratumChange.setObjects(
    ("SONOMA-MIB", "cntpStratum")
)
if mibBuilder.loadTexts:
    cntpTrapStratumChange.setStatus(
        "current"
    )

cdmaTrapFaultStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 0, 1)
)
cdmaTrapFaultStatusChange.setObjects(
    ("SONOMA-MIB", "cdmaFaultStatus")
)
if mibBuilder.loadTexts:
    cdmaTrapFaultStatusChange.setStatus(
        "current"
    )

cdmaTrapFault2StatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 0, 2)
)
cdmaTrapFault2StatusChange.setObjects(
    ("SONOMA-MIB", "cdmaFault2Status")
)
if mibBuilder.loadTexts:
    cdmaTrapFault2StatusChange.setStatus(
        "current"
    )

cdmaTrapTimeFigureOfMeritChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 11, 2, 0, 3)
)
cdmaTrapTimeFigureOfMeritChange.setObjects(
    ("SONOMA-MIB", "cdmaTimeFigureOfMerit")
)
if mibBuilder.loadTexts:
    cdmaTrapTimeFigureOfMeritChange.setStatus(
        "current"
    )

gntpTrapLeapIndBitsChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 0, 1)
)
gntpTrapLeapIndBitsChange.setObjects(
    ("SONOMA-MIB", "gntpLeapIndBits")
)
if mibBuilder.loadTexts:
    gntpTrapLeapIndBitsChange.setStatus(
        "current"
    )

gntpTrapStratumChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 12, 1, 0, 2)
)
gntpTrapStratumChange.setObjects(
    ("SONOMA-MIB", "gntpStratum")
)
if mibBuilder.loadTexts:
    gntpTrapStratumChange.setStatus(
        "current"
    )

gpsTrapFaultStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 0, 1)
)
gpsTrapFaultStatusChange.setObjects(
    ("SONOMA-MIB", "gpsFaultStatus")
)
if mibBuilder.loadTexts:
    gpsTrapFaultStatusChange.setStatus(
        "current"
    )

gpsTrapFault2StatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 0, 2)
)
gpsTrapFault2StatusChange.setObjects(
    ("SONOMA-MIB", "gpsFault2Status")
)
if mibBuilder.loadTexts:
    gpsTrapFault2StatusChange.setStatus(
        "current"
    )

gpsTrapTimeFigureOfMeritChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 12, 2, 0, 3)
)
gpsTrapTimeFigureOfMeritChange.setObjects(
    ("SONOMA-MIB", "gpsTimeFigureOfMerit")
)
if mibBuilder.loadTexts:
    gpsTrapTimeFigureOfMeritChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONOMA-MIB",
    **{"endRunTechnologiesMIB": endRunTechnologiesMIB,
       "endRunTechnologies": endRunTechnologies,
       "sonomaCDMA": sonomaCDMA,
       "cntp": cntp,
       "cntptrap": cntptrap,
       "cntpTrapLeapIndBitsChange": cntpTrapLeapIndBitsChange,
       "cntpTrapStratumChange": cntpTrapStratumChange,
       "cntpTimeSinceRst": cntpTimeSinceRst,
       "cntpIRQsHandled": cntpIRQsHandled,
       "cntpRxPkts": cntpRxPkts,
       "cntpRxPktsByIRQ": cntpRxPktsByIRQ,
       "cntpTxPkts": cntpTxPkts,
       "cntpSentPktsPerSecond": cntpSentPktsPerSecond,
       "cntpUnSentPkts": cntpUnSentPkts,
       "cntpIgnoredPkts": cntpIgnoredPkts,
       "cntpDroppedPkts": cntpDroppedPkts,
       "cntpAuthFail": cntpAuthFail,
       "cntpTimeFigureOfMerit": cntpTimeFigureOfMerit,
       "cntpLeapIndBits": cntpLeapIndBits,
       "cntpSyncSource": cntpSyncSource,
       "cntpOffsetToCDMAReference": cntpOffsetToCDMAReference,
       "cntpStratum": cntpStratum,
       "cntpVersion": cntpVersion,
       "cntpKernelVersion": cntpKernelVersion,
       "cntpOscType": cntpOscType,
       "cntpTimeMode": cntpTimeMode,
       "cntpLocalOffset": cntpLocalOffset,
       "cntpDSTStartMonth": cntpDSTStartMonth,
       "cntpDSTStartSunday": cntpDSTStartSunday,
       "cntpDSTStartHour": cntpDSTStartHour,
       "cntpDSTStopMonth": cntpDSTStopMonth,
       "cntpDSTStopSunday": cntpDSTStopSunday,
       "cntpDSTStopHour": cntpDSTStopHour,
       "cntpCPUDieTemperature": cntpCPUDieTemperature,
       "cntpCPUFreeMemory": cntpCPUFreeMemory,
       "cntpCPULoadAveragePerCent": cntpCPULoadAveragePerCent,
       "cdma": cdma,
       "cdmatrap": cdmatrap,
       "cdmaTrapFaultStatusChange": cdmaTrapFaultStatusChange,
       "cdmaTrapFault2StatusChange": cdmaTrapFault2StatusChange,
       "cdmaTrapTimeFigureOfMeritChange": cdmaTrapTimeFigureOfMeritChange,
       "cdmaFaultStatus": cdmaFaultStatus,
       "cdmaFault2Status": cdmaFault2Status,
       "cdmaReceiverFaultNibble0Status": cdmaReceiverFaultNibble0Status,
       "cdmaReceiverFaultNibble1Status": cdmaReceiverFaultNibble1Status,
       "cdmaTimeFigureOfMerit": cdmaTimeFigureOfMerit,
       "cdmaSigProcState": cdmaSigProcState,
       "cdmaReceiverSigProcState": cdmaReceiverSigProcState,
       "cdmaChannel": cdmaChannel,
       "cdmaPNO": cdmaPNO,
       "cdmaAGC": cdmaAGC,
       "cdmaReceiverVCDAC": cdmaReceiverVCDAC,
       "cdmaCarrierToNoiseRatio": cdmaCarrierToNoiseRatio,
       "cdmaFrameErrorRate": cdmaFrameErrorRate,
       "cdmaLeapMode": cdmaLeapMode,
       "cdmaUserCurrentLeapSeconds": cdmaUserCurrentLeapSeconds,
       "cdmaUserFutureLeapSeconds": cdmaUserFutureLeapSeconds,
       "cdmaCurrentLeapSeconds": cdmaCurrentLeapSeconds,
       "cdmaFutureLeapSeconds": cdmaFutureLeapSeconds,
       "cdmaVersion": cdmaVersion,
       "cdmaReceiverVersion": cdmaReceiverVersion,
       "cdmaCalibrationDelay": cdmaCalibrationDelay,
       "cdmaCoastDuration": cdmaCoastDuration,
       "cdmaEstimatedTimeError": cdmaEstimatedTimeError,
       "cdmaMeasuredTimeError": cdmaMeasuredTimeError,
       "cdmaMeasurementTimeDeviation": cdmaMeasurementTimeDeviation,
       "cdmaSystemOSCDAC": cdmaSystemOSCDAC,
       "cdmaMeasuredOscillatorAgeing": cdmaMeasuredOscillatorAgeing,
       "cdmaControlLoopTimeConstant": cdmaControlLoopTimeConstant,
       "cdmaInternalTemperature": cdmaInternalTemperature,
       "cdmaSignalLossFaultMask": cdmaSignalLossFaultMask,
       "cdmaPrimaryPowerFaultAlarmMask": cdmaPrimaryPowerFaultAlarmMask,
       "cdmaSecondaryPowerFaultAlarmMask": cdmaSecondaryPowerFaultAlarmMask,
       "cdmaFaultNibble0Status": cdmaFaultNibble0Status,
       "cdmaFaultNibble1Status": cdmaFaultNibble1Status,
       "cdmaFaultNibble2Status": cdmaFaultNibble2Status,
       "cdmaFaultNibble3Status": cdmaFaultNibble3Status,
       "cCPUIO": cCPUIO,
       "csysio1PPSWidth": csysio1PPSWidth,
       "csysioTimeCodeFormat": csysioTimeCodeFormat,
       "csysioSynthesizerHz": csysioSynthesizerHz,
       "csysioSerialTimeOutputBaudrate": csysioSerialTimeOutputBaudrate,
       "csysioSerialTimeOutputFormat": csysioSerialTimeOutputFormat,
       "csysioSerialTimeOutputParity": csysioSerialTimeOutputParity,
       "csysioSerialTimeNMEASentence1": csysioSerialTimeNMEASentence1,
       "csysioSerialTimeNMEASentence2": csysioSerialTimeNMEASentence2,
       "csysioSerialTimeNMEASentence3": csysioSerialTimeNMEASentence3,
       "ccpuioConnA": ccpuioConnA,
       "ccpuioConnB": ccpuioConnB,
       "ccpuioConnC": ccpuioConnC,
       "cptp0": cptp0,
       "cptp0Version": cptp0Version,
       "cptp0SyncInterval": cptp0SyncInterval,
       "cptp0AnnounceInterval": cptp0AnnounceInterval,
       "cptp0Priority1": cptp0Priority1,
       "cptp0Priority2": cptp0Priority2,
       "cptp0DelayMechanism": cptp0DelayMechanism,
       "cptp0Domain": cptp0Domain,
       "cptp0TimeMode": cptp0TimeMode,
       "cptp0TTL": cptp0TTL,
       "cptp0ClockClass": cptp0ClockClass,
       "cptp0TimeScale": cptp0TimeScale,
       "cptp0PortState": cptp0PortState,
       "cptp0TimeSource": cptp0TimeSource,
       "cptp0UTCOffset": cptp0UTCOffset,
       "cptp0UTCOffsetValid": cptp0UTCOffsetValid,
       "cptp0ClockAccuracy": cptp0ClockAccuracy,
       "cptp0Leap59": cptp0Leap59,
       "cptp0Leap61": cptp0Leap61,
       "cptp0TimeTraceable": cptp0TimeTraceable,
       "cptp0FreqTraceable": cptp0FreqTraceable,
       "cptp1": cptp1,
       "cptp1Version": cptp1Version,
       "cptp1SyncInterval": cptp1SyncInterval,
       "cptp1AnnounceInterval": cptp1AnnounceInterval,
       "cptp1Priority1": cptp1Priority1,
       "cptp1Priority2": cptp1Priority2,
       "cptp1DelayMechanism": cptp1DelayMechanism,
       "cptp1Domain": cptp1Domain,
       "cptp1TimeMode": cptp1TimeMode,
       "cptp1TTL": cptp1TTL,
       "cptp1ClockClass": cptp1ClockClass,
       "cptp1TimeScale": cptp1TimeScale,
       "cptp1PortState": cptp1PortState,
       "cptp1TimeSource": cptp1TimeSource,
       "cptp1UTCOffset": cptp1UTCOffset,
       "cptp1UTCOffsetValid": cptp1UTCOffsetValid,
       "cptp1ClockAccuracy": cptp1ClockAccuracy,
       "cptp1Leap59": cptp1Leap59,
       "cptp1Leap61": cptp1Leap61,
       "cptp1TimeTraceable": cptp1TimeTraceable,
       "cptp1FreqTraceable": cptp1FreqTraceable,
       "sonomaGPS": sonomaGPS,
       "gntp": gntp,
       "gntptrap": gntptrap,
       "gntpTrapLeapIndBitsChange": gntpTrapLeapIndBitsChange,
       "gntpTrapStratumChange": gntpTrapStratumChange,
       "gntpTimeSinceRst": gntpTimeSinceRst,
       "gntpIRQsHandled": gntpIRQsHandled,
       "gntpRxPkts": gntpRxPkts,
       "gntpRxPktsByIRQ": gntpRxPktsByIRQ,
       "gntpTxPkts": gntpTxPkts,
       "gntpSentPktsPerSecond": gntpSentPktsPerSecond,
       "gntpUnSentPkts": gntpUnSentPkts,
       "gntpIgnoredPkts": gntpIgnoredPkts,
       "gntpDroppedPkts": gntpDroppedPkts,
       "gntpAuthFail": gntpAuthFail,
       "gntpTimeFigureOfMerit": gntpTimeFigureOfMerit,
       "gntpLeapIndBits": gntpLeapIndBits,
       "gntpSyncSource": gntpSyncSource,
       "gntpOffsetToGPSReference": gntpOffsetToGPSReference,
       "gntpStratum": gntpStratum,
       "gntpVersion": gntpVersion,
       "gntpKernelVersion": gntpKernelVersion,
       "gntpOscType": gntpOscType,
       "gntpTimeMode": gntpTimeMode,
       "gntpLocalOffset": gntpLocalOffset,
       "gntpDSTStartMonth": gntpDSTStartMonth,
       "gntpDSTStartSunday": gntpDSTStartSunday,
       "gntpDSTStartHour": gntpDSTStartHour,
       "gntpDSTStopMonth": gntpDSTStopMonth,
       "gntpDSTStopSunday": gntpDSTStopSunday,
       "gntpDSTStopHour": gntpDSTStopHour,
       "gntpCPUDieTemperature": gntpCPUDieTemperature,
       "gntpCPUFreeMemory": gntpCPUFreeMemory,
       "gntpCPULoadAveragePerCent": gntpCPULoadAveragePerCent,
       "gps": gps,
       "gpstrap": gpstrap,
       "gpsTrapFaultStatusChange": gpsTrapFaultStatusChange,
       "gpsTrapFault2StatusChange": gpsTrapFault2StatusChange,
       "gpsTrapTimeFigureOfMeritChange": gpsTrapTimeFigureOfMeritChange,
       "gpsFaultStatus": gpsFaultStatus,
       "gpsFault2Status": gpsFault2Status,
       "gpsTimeFigureOfMerit": gpsTimeFigureOfMerit,
       "gpsSigProcState": gpsSigProcState,
       "gpsNumTrackSats": gpsNumTrackSats,
       "gpsAvgCarrierToNoiseRatiodB": gpsAvgCarrierToNoiseRatiodB,
       "gpsChannelTrkStat1": gpsChannelTrkStat1,
       "gpsChannelTrkStat2": gpsChannelTrkStat2,
       "gpsChannelTrkStat3": gpsChannelTrkStat3,
       "gpsChannelTrkStat4": gpsChannelTrkStat4,
       "gpsChannelTrkStat5": gpsChannelTrkStat5,
       "gpsChannelTrkStat6": gpsChannelTrkStat6,
       "gpsChannelTrkStat7": gpsChannelTrkStat7,
       "gpsChannelTrkStat8": gpsChannelTrkStat8,
       "gpsChannelTrkStat9": gpsChannelTrkStat9,
       "gpsChannelTrkStat10": gpsChannelTrkStat10,
       "gpsChannelTrkStat11": gpsChannelTrkStat11,
       "gpsChannelTrkStat12": gpsChannelTrkStat12,
       "gpsLastPositionFix": gpsLastPositionFix,
       "gpsReferencePosition": gpsReferencePosition,
       "gpsRefPosSource": gpsRefPosSource,
       "gpsCurrentLeapSeconds": gpsCurrentLeapSeconds,
       "gpsFutureLeapSeconds": gpsFutureLeapSeconds,
       "gpsAlmanacLS": gpsAlmanacLS,
       "gpsAlmanacLSF": gpsAlmanacLSF,
       "gpsAlmanacUTCWNlsf": gpsAlmanacUTCWNlsf,
       "gpsAlmanacUTCDN": gpsAlmanacUTCDN,
       "gpsAlmanacA0": gpsAlmanacA0,
       "gpsAlmanacA1": gpsAlmanacA1,
       "gpsAlmanacUTCWNt": gpsAlmanacUTCWNt,
       "gpsAlmanacUTCtot": gpsAlmanacUTCtot,
       "gpsGPSminusUTCOffset": gpsGPSminusUTCOffset,
       "gpsVersion": gpsVersion,
       "gpsDynamicMode": gpsDynamicMode,
       "gpsCalibrationDelay": gpsCalibrationDelay,
       "gpsCoastDuration": gpsCoastDuration,
       "gpsEstimatedTimeError": gpsEstimatedTimeError,
       "gpsMeasuredTimeError": gpsMeasuredTimeError,
       "gpsMeasurementTimeDeviation": gpsMeasurementTimeDeviation,
       "gpsOSCDAC": gpsOSCDAC,
       "gpsMeasuredOscillatorAgeing": gpsMeasuredOscillatorAgeing,
       "gpsControlLoopTimeConstant": gpsControlLoopTimeConstant,
       "gpsInternalTemperature": gpsInternalTemperature,
       "gpsAntennaFaultMask": gpsAntennaFaultMask,
       "gpsSignalLossFaultMask": gpsSignalLossFaultMask,
       "gpsPrimaryPowerFaultAlarmMask": gpsPrimaryPowerFaultAlarmMask,
       "gpsSecondaryPowerFaultAlarmMask": gpsSecondaryPowerFaultAlarmMask,
       "gpsFaultNibble0Status": gpsFaultNibble0Status,
       "gpsFaultNibble1Status": gpsFaultNibble1Status,
       "gpsFaultNibble2Status": gpsFaultNibble2Status,
       "gpsFaultNibble3Status": gpsFaultNibble3Status,
       "gCPUIO": gCPUIO,
       "gsysio1PPSWidth": gsysio1PPSWidth,
       "gsysioTimeCodeFormat": gsysioTimeCodeFormat,
       "gsysioSynthesizerHz": gsysioSynthesizerHz,
       "gsysioSerialTimeOutputBaudrate": gsysioSerialTimeOutputBaudrate,
       "gsysioSerialTimeOutputFormat": gsysioSerialTimeOutputFormat,
       "gsysioSerialTimeOutputParity": gsysioSerialTimeOutputParity,
       "gsysioSerialTimeNMEASentence1": gsysioSerialTimeNMEASentence1,
       "gsysioSerialTimeNMEASentence2": gsysioSerialTimeNMEASentence2,
       "gsysioSerialTimeNMEASentence3": gsysioSerialTimeNMEASentence3,
       "gcpuioConnA": gcpuioConnA,
       "gcpuioConnB": gcpuioConnB,
       "gcpuioConnC": gcpuioConnC,
       "gptp0": gptp0,
       "gptp0Version": gptp0Version,
       "gptp0SyncInterval": gptp0SyncInterval,
       "gptp0AnnounceInterval": gptp0AnnounceInterval,
       "gptp0Priority1": gptp0Priority1,
       "gptp0Priority2": gptp0Priority2,
       "gptp0DelayMechanism": gptp0DelayMechanism,
       "gptp0Domain": gptp0Domain,
       "gptp0TimeMode": gptp0TimeMode,
       "gptp0TTL": gptp0TTL,
       "gptp0ClockClass": gptp0ClockClass,
       "gptp0TimeScale": gptp0TimeScale,
       "gptp0PortState": gptp0PortState,
       "gptp0TimeSource": gptp0TimeSource,
       "gptp0UTCOffset": gptp0UTCOffset,
       "gptp0UTCOffsetValid": gptp0UTCOffsetValid,
       "gptp0ClockAccuracy": gptp0ClockAccuracy,
       "gptp0Leap59": gptp0Leap59,
       "gptp0Leap61": gptp0Leap61,
       "gptp0TimeTraceable": gptp0TimeTraceable,
       "gptp0FreqTraceable": gptp0FreqTraceable,
       "gptp1": gptp1,
       "gptp1Version": gptp1Version,
       "gptp1SyncInterval": gptp1SyncInterval,
       "gptp1AnnounceInterval": gptp1AnnounceInterval,
       "gptp1Priority1": gptp1Priority1,
       "gptp1Priority2": gptp1Priority2,
       "gptp1DelayMechanism": gptp1DelayMechanism,
       "gptp1Domain": gptp1Domain,
       "gptp1TimeMode": gptp1TimeMode,
       "gptp1TTL": gptp1TTL,
       "gptp1ClockClass": gptp1ClockClass,
       "gptp1TimeScale": gptp1TimeScale,
       "gptp1PortState": gptp1PortState,
       "gptp1TimeSource": gptp1TimeSource,
       "gptp1UTCOffset": gptp1UTCOffset,
       "gptp1UTCOffsetValid": gptp1UTCOffsetValid,
       "gptp1ClockAccuracy": gptp1ClockAccuracy,
       "gptp1Leap59": gptp1Leap59,
       "gptp1Leap61": gptp1Leap61,
       "gptp1TimeTraceable": gptp1TimeTraceable,
       "gptp1FreqTraceable": gptp1FreqTraceable}
)
