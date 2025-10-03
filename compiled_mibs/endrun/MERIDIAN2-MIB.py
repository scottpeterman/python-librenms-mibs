# SNMP MIB module (MERIDIAN2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\endrun\MERIDIAN2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:40:01 2025
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
_Meridian2GPS_ObjectIdentity = ObjectIdentity
meridian2GPS = _Meridian2GPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 14)
)
_Gntp_ObjectIdentity = ObjectIdentity
gntp = _Gntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1)
)
_Gntptrap_ObjectIdentity = ObjectIdentity
gntptrap = _Gntptrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 0)
)
_GntpTimeSinceRst_Type = Counter32
_GntpTimeSinceRst_Object = MibScalar
gntpTimeSinceRst = _GntpTimeSinceRst_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 1),
    _GntpTimeSinceRst_Type()
)
gntpTimeSinceRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpTimeSinceRst.setStatus("current")
_GntpIRQsHandled_Type = Counter32
_GntpIRQsHandled_Object = MibScalar
gntpIRQsHandled = _GntpIRQsHandled_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 2),
    _GntpIRQsHandled_Type()
)
gntpIRQsHandled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpIRQsHandled.setStatus("current")
_GntpRxPkts_Type = Counter32
_GntpRxPkts_Object = MibScalar
gntpRxPkts = _GntpRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 3),
    _GntpRxPkts_Type()
)
gntpRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpRxPkts.setStatus("current")
_GntpRxPktsByIRQ_Type = Counter32
_GntpRxPktsByIRQ_Object = MibScalar
gntpRxPktsByIRQ = _GntpRxPktsByIRQ_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 4),
    _GntpRxPktsByIRQ_Type()
)
gntpRxPktsByIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpRxPktsByIRQ.setStatus("current")
_GntpTxPkts_Type = Counter32
_GntpTxPkts_Object = MibScalar
gntpTxPkts = _GntpTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 5),
    _GntpTxPkts_Type()
)
gntpTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpTxPkts.setStatus("current")
_GntpSentPktsPerSecond_Type = Integer32
_GntpSentPktsPerSecond_Object = MibScalar
gntpSentPktsPerSecond = _GntpSentPktsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 6),
    _GntpSentPktsPerSecond_Type()
)
gntpSentPktsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpSentPktsPerSecond.setStatus("current")
_GntpUnSentPkts_Type = Counter32
_GntpUnSentPkts_Object = MibScalar
gntpUnSentPkts = _GntpUnSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 7),
    _GntpUnSentPkts_Type()
)
gntpUnSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpUnSentPkts.setStatus("current")
_GntpIgnoredPkts_Type = Counter32
_GntpIgnoredPkts_Object = MibScalar
gntpIgnoredPkts = _GntpIgnoredPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 8),
    _GntpIgnoredPkts_Type()
)
gntpIgnoredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpIgnoredPkts.setStatus("current")
_GntpDroppedPkts_Type = Counter32
_GntpDroppedPkts_Object = MibScalar
gntpDroppedPkts = _GntpDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 9),
    _GntpDroppedPkts_Type()
)
gntpDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpDroppedPkts.setStatus("current")
_GntpAuthFail_Type = Counter32
_GntpAuthFail_Object = MibScalar
gntpAuthFail = _GntpAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 19),
    _GntpTimeMode_Type()
)
gntpTimeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpTimeMode.setStatus("current")
_GntpLocalOffset_Type = Integer32
_GntpLocalOffset_Object = MibScalar
gntpLocalOffset = _GntpLocalOffset_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 20),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 21),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 22),
    _GntpDSTStartSunday_Type()
)
gntpDSTStartSunday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpDSTStartSunday.setStatus("current")
_GntpDSTStartHour_Type = Integer32
_GntpDSTStartHour_Object = MibScalar
gntpDSTStartHour = _GntpDSTStartHour_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 23),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 24),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 25),
    _GntpDSTStopSunday_Type()
)
gntpDSTStopSunday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpDSTStopSunday.setStatus("current")
_GntpDSTStopHour_Type = Integer32
_GntpDSTStopHour_Object = MibScalar
gntpDSTStopHour = _GntpDSTStopHour_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 26),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 27),
    _GntpCPUDieTemperature_Type()
)
gntpCPUDieTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpCPUDieTemperature.setStatus("current")
_GntpCPUFreeMemory_Type = Integer32
_GntpCPUFreeMemory_Object = MibScalar
gntpCPUFreeMemory = _GntpCPUFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 28),
    _GntpCPUFreeMemory_Type()
)
gntpCPUFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpCPUFreeMemory.setStatus("current")
_GntpCPULoadAveragePerCent_Type = Integer32
_GntpCPULoadAveragePerCent_Object = MibScalar
gntpCPULoadAveragePerCent = _GntpCPULoadAveragePerCent_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 29),
    _GntpCPULoadAveragePerCent_Type()
)
gntpCPULoadAveragePerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpCPULoadAveragePerCent.setStatus("current")
_Gps_ObjectIdentity = ObjectIdentity
gps = _Gps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2)
)
_Gpstrap_ObjectIdentity = ObjectIdentity
gpstrap = _Gpstrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 0)
)


class _GpsFaultStatus_Type(Bits):
    """Custom type gpsFaultStatus based on Bits"""
    namedValues = NamedValues(
        *(("gpsReceiverFlt", 0),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 1),
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
          ("gpsHP5071a", 2),
          ("gpsPlugInOpts", 3),
          ("gpsAntennaFlt", 4),
          ("gpsOscPLLFlt", 5),
          ("gpsSecPwrSplyFlt", 6),
          ("gpsPriPwrSplyFlt", 7))
    )

_GpsFault2Status_Type.__name__ = "Bits"
_GpsFault2Status_Object = MibScalar
gpsFault2Status = _GpsFault2Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 2),
    _GpsFault2Status_Type()
)
gpsFault2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsFault2Status.setStatus("current")


class _GpsReceiverFaultNibble0Status_Type(Bits):
    """Custom type gpsReceiverFaultNibble0Status based on Bits"""
    namedValues = NamedValues(
        *(("gpsFLASHWriteFlt", 0),
          ("gpsFPGACfgFlt", 1),
          ("gpsNoSignalTimeout", 2),
          ("gpsDACNearLimit", 3))
    )

_GpsReceiverFaultNibble0Status_Type.__name__ = "Bits"
_GpsReceiverFaultNibble0Status_Object = MibScalar
gpsReceiverFaultNibble0Status = _GpsReceiverFaultNibble0Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 3),
    _GpsReceiverFaultNibble0Status_Type()
)
gpsReceiverFaultNibble0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsReceiverFaultNibble0Status.setStatus("current")


class _GpsReceiverFaultNibble1Status_Type(Bits):
    """Custom type gpsReceiverFaultNibble1Status based on Bits"""
    namedValues = NamedValues(
        *(("gpsMainOscFlt", 0),
          ("gpsRefTimeFlt", 1),
          ("gpsSynthFlt", 2),
          ("gpsSynthNearLimit", 3))
    )

_GpsReceiverFaultNibble1Status_Type.__name__ = "Bits"
_GpsReceiverFaultNibble1Status_Object = MibScalar
gpsReceiverFaultNibble1Status = _GpsReceiverFaultNibble1Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 4),
    _GpsReceiverFaultNibble1Status_Type()
)
gpsReceiverFaultNibble1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsReceiverFaultNibble1Status.setStatus("current")


class _GpsReceiverFaultNibble2Status_Type(Bits):
    """Custom type gpsReceiverFaultNibble2Status based on Bits"""
    namedValues = NamedValues(
        *(("gpsNotUsed0", 0),
          ("gpsOscPLLFlt", 1),
          ("gpsAntennaOpen", 2),
          ("gpsAntennaShort", 3))
    )

_GpsReceiverFaultNibble2Status_Type.__name__ = "Bits"
_GpsReceiverFaultNibble2Status_Object = MibScalar
gpsReceiverFaultNibble2Status = _GpsReceiverFaultNibble2Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 5),
    _GpsReceiverFaultNibble2Status_Type()
)
gpsReceiverFaultNibble2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsReceiverFaultNibble2Status.setStatus("current")


class _GpsReceiverFaultNibble3Status_Type(Bits):
    """Custom type gpsReceiverFaultNibble3Status based on Bits"""
    namedValues = NamedValues(
        *(("gpsNotUsed0", 0),
          ("gpsNotUsed1", 1),
          ("gpsNotUsed2", 2),
          ("gpsNotUsed3", 3))
    )

_GpsReceiverFaultNibble3Status_Type.__name__ = "Bits"
_GpsReceiverFaultNibble3Status_Object = MibScalar
gpsReceiverFaultNibble3Status = _GpsReceiverFaultNibble3Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 6),
    _GpsReceiverFaultNibble3Status_Type()
)
gpsReceiverFaultNibble3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsReceiverFaultNibble3Status.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 7),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 8),
    _GpsSigProcState_Type()
)
gpsSigProcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSigProcState.setStatus("current")


class _GpsReceiverSigProcState_Type(DisplayString):
    """Custom type gpsReceiverSigProcState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_GpsReceiverSigProcState_Type.__name__ = "DisplayString"
_GpsReceiverSigProcState_Object = MibScalar
gpsReceiverSigProcState = _GpsReceiverSigProcState_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 9),
    _GpsReceiverSigProcState_Type()
)
gpsReceiverSigProcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsReceiverSigProcState.setStatus("current")


class _GpsNumTrackSats_Type(Integer32):
    """Custom type gpsNumTrackSats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_GpsNumTrackSats_Type.__name__ = "Integer32"
_GpsNumTrackSats_Object = MibScalar
gpsNumTrackSats = _GpsNumTrackSats_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 10),
    _GpsNumTrackSats_Type()
)
gpsNumTrackSats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsNumTrackSats.setStatus("current")


class _GpsAGC_Type(Integer32):
    """Custom type gpsAGC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GpsAGC_Type.__name__ = "Integer32"
_GpsAGC_Object = MibScalar
gpsAGC = _GpsAGC_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 11),
    _GpsAGC_Type()
)
gpsAGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAGC.setStatus("current")


class _GpsAvgCarrierToNoiseRatiodB_Type(DisplayString):
    """Custom type gpsAvgCarrierToNoiseRatiodB based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_GpsAvgCarrierToNoiseRatiodB_Type.__name__ = "DisplayString"
_GpsAvgCarrierToNoiseRatiodB_Object = MibScalar
gpsAvgCarrierToNoiseRatiodB = _GpsAvgCarrierToNoiseRatiodB_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 12),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 13),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 14),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 15),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 16),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 17),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 18),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 19),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 20),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 21),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 22),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 23),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 24),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 25),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 26),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 27),
    _GpsRefPosSource_Type()
)
gpsRefPosSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsRefPosSource.setStatus("current")
_GpsCurrentLeapSeconds_Type = Integer32
_GpsCurrentLeapSeconds_Object = MibScalar
gpsCurrentLeapSeconds = _GpsCurrentLeapSeconds_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 28),
    _GpsCurrentLeapSeconds_Type()
)
gpsCurrentLeapSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsCurrentLeapSeconds.setStatus("current")
_GpsFutureLeapSeconds_Type = Integer32
_GpsFutureLeapSeconds_Object = MibScalar
gpsFutureLeapSeconds = _GpsFutureLeapSeconds_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 29),
    _GpsFutureLeapSeconds_Type()
)
gpsFutureLeapSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsFutureLeapSeconds.setStatus("current")
_GpsAlmanacLS_Type = Integer32
_GpsAlmanacLS_Object = MibScalar
gpsAlmanacLS = _GpsAlmanacLS_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 30),
    _GpsAlmanacLS_Type()
)
gpsAlmanacLS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacLS.setStatus("current")
_GpsAlmanacLSF_Type = Integer32
_GpsAlmanacLSF_Object = MibScalar
gpsAlmanacLSF = _GpsAlmanacLSF_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 31),
    _GpsAlmanacLSF_Type()
)
gpsAlmanacLSF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacLSF.setStatus("current")
_GpsAlmanacUTCWNlsf_Type = Integer32
_GpsAlmanacUTCWNlsf_Object = MibScalar
gpsAlmanacUTCWNlsf = _GpsAlmanacUTCWNlsf_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 32),
    _GpsAlmanacUTCWNlsf_Type()
)
gpsAlmanacUTCWNlsf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacUTCWNlsf.setStatus("current")
_GpsAlmanacUTCDN_Type = Integer32
_GpsAlmanacUTCDN_Object = MibScalar
gpsAlmanacUTCDN = _GpsAlmanacUTCDN_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 33),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 34),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 35),
    _GpsAlmanacA1_Type()
)
gpsAlmanacA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacA1.setStatus("current")
_GpsAlmanacUTCWNt_Type = Integer32
_GpsAlmanacUTCWNt_Object = MibScalar
gpsAlmanacUTCWNt = _GpsAlmanacUTCWNt_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 36),
    _GpsAlmanacUTCWNt_Type()
)
gpsAlmanacUTCWNt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacUTCWNt.setStatus("current")
_GpsAlmanacUTCtot_Type = Integer32
_GpsAlmanacUTCtot_Object = MibScalar
gpsAlmanacUTCtot = _GpsAlmanacUTCtot_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 37),
    _GpsAlmanacUTCtot_Type()
)
gpsAlmanacUTCtot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacUTCtot.setStatus("current")
_GpsGPSminusUTCOffsetPicoSecs_Type = Integer32
_GpsGPSminusUTCOffsetPicoSecs_Object = MibScalar
gpsGPSminusUTCOffsetPicoSecs = _GpsGPSminusUTCOffsetPicoSecs_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 38),
    _GpsGPSminusUTCOffsetPicoSecs_Type()
)
gpsGPSminusUTCOffsetPicoSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsGPSminusUTCOffsetPicoSecs.setStatus("current")


class _GpsSubsystemVersion_Type(DisplayString):
    """Custom type gpsSubsystemVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsSubsystemVersion_Type.__name__ = "DisplayString"
_GpsSubsystemVersion_Object = MibScalar
gpsSubsystemVersion = _GpsSubsystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 39),
    _GpsSubsystemVersion_Type()
)
gpsSubsystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSubsystemVersion.setStatus("current")


class _GpsReceiverVersion_Type(DisplayString):
    """Custom type gpsReceiverVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsReceiverVersion_Type.__name__ = "DisplayString"
_GpsReceiverVersion_Object = MibScalar
gpsReceiverVersion = _GpsReceiverVersion_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 40),
    _GpsReceiverVersion_Type()
)
gpsReceiverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsReceiverVersion.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 41),
    _GpsDynamicMode_Type()
)
gpsDynamicMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsDynamicMode.setStatus("current")


class _GpsCalibrationDelayNanoSecs_Type(Integer32):
    """Custom type gpsCalibrationDelayNanoSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500000, 500000),
    )


_GpsCalibrationDelayNanoSecs_Type.__name__ = "Integer32"
_GpsCalibrationDelayNanoSecs_Object = MibScalar
gpsCalibrationDelayNanoSecs = _GpsCalibrationDelayNanoSecs_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 42),
    _GpsCalibrationDelayNanoSecs_Type()
)
gpsCalibrationDelayNanoSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsCalibrationDelayNanoSecs.setStatus("current")


class _GpsCoastDuration_Type(Integer32):
    """Custom type gpsCoastDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GpsCoastDuration_Type.__name__ = "Integer32"
_GpsCoastDuration_Object = MibScalar
gpsCoastDuration = _GpsCoastDuration_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 43),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 44),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 45),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 46),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 47),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 48),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 49),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 50),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 51),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 52),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 53),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 54),
    _GpsSecondaryPowerFaultAlarmMask_Type()
)
gpsSecondaryPowerFaultAlarmMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSecondaryPowerFaultAlarmMask.setStatus("current")


class _GpsTimeFigureOfMeritFaultLevel_Type(Integer32):
    """Custom type gpsTimeFigureOfMeritFaultLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("lessthan1us", 4),
          ("lessthan10us", 5),
          ("lessthan100us", 6),
          ("lessthan1ms", 7),
          ("lessthan10ms", 8),
          ("greaterthan10ms", 9))
    )


_GpsTimeFigureOfMeritFaultLevel_Type.__name__ = "Integer32"
_GpsTimeFigureOfMeritFaultLevel_Object = MibScalar
gpsTimeFigureOfMeritFaultLevel = _GpsTimeFigureOfMeritFaultLevel_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 55),
    _GpsTimeFigureOfMeritFaultLevel_Type()
)
gpsTimeFigureOfMeritFaultLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsTimeFigureOfMeritFaultLevel.setStatus("current")


class _GpsInhibitOutputsMode_Type(Integer32):
    """Custom type gpsInhibitOutputsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("gpsInhibitOutputsModeOFF", 0),
          ("gpsInhibitOutputsModeON", 1))
    )


_GpsInhibitOutputsMode_Type.__name__ = "Integer32"
_GpsInhibitOutputsMode_Object = MibScalar
gpsInhibitOutputsMode = _GpsInhibitOutputsMode_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 56),
    _GpsInhibitOutputsMode_Type()
)
gpsInhibitOutputsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsInhibitOutputsMode.setStatus("current")


class _GpsAlmanacIonoAlpha0_Type(DisplayString):
    """Custom type gpsAlmanacIonoAlpha0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsAlmanacIonoAlpha0_Type.__name__ = "DisplayString"
_GpsAlmanacIonoAlpha0_Object = MibScalar
gpsAlmanacIonoAlpha0 = _GpsAlmanacIonoAlpha0_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 57),
    _GpsAlmanacIonoAlpha0_Type()
)
gpsAlmanacIonoAlpha0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacIonoAlpha0.setStatus("current")


class _GpsAlmanacIonoAlpha1_Type(DisplayString):
    """Custom type gpsAlmanacIonoAlpha1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsAlmanacIonoAlpha1_Type.__name__ = "DisplayString"
_GpsAlmanacIonoAlpha1_Object = MibScalar
gpsAlmanacIonoAlpha1 = _GpsAlmanacIonoAlpha1_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 58),
    _GpsAlmanacIonoAlpha1_Type()
)
gpsAlmanacIonoAlpha1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacIonoAlpha1.setStatus("current")


class _GpsAlmanacIonoAlpha2_Type(DisplayString):
    """Custom type gpsAlmanacIonoAlpha2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsAlmanacIonoAlpha2_Type.__name__ = "DisplayString"
_GpsAlmanacIonoAlpha2_Object = MibScalar
gpsAlmanacIonoAlpha2 = _GpsAlmanacIonoAlpha2_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 59),
    _GpsAlmanacIonoAlpha2_Type()
)
gpsAlmanacIonoAlpha2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacIonoAlpha2.setStatus("current")


class _GpsAlmanacIonoAlpha3_Type(DisplayString):
    """Custom type gpsAlmanacIonoAlpha3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsAlmanacIonoAlpha3_Type.__name__ = "DisplayString"
_GpsAlmanacIonoAlpha3_Object = MibScalar
gpsAlmanacIonoAlpha3 = _GpsAlmanacIonoAlpha3_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 60),
    _GpsAlmanacIonoAlpha3_Type()
)
gpsAlmanacIonoAlpha3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacIonoAlpha3.setStatus("current")


class _GpsAlmanacIonoBeta0_Type(DisplayString):
    """Custom type gpsAlmanacIonoBeta0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsAlmanacIonoBeta0_Type.__name__ = "DisplayString"
_GpsAlmanacIonoBeta0_Object = MibScalar
gpsAlmanacIonoBeta0 = _GpsAlmanacIonoBeta0_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 61),
    _GpsAlmanacIonoBeta0_Type()
)
gpsAlmanacIonoBeta0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacIonoBeta0.setStatus("current")


class _GpsAlmanacIonoBeta1_Type(DisplayString):
    """Custom type gpsAlmanacIonoBeta1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsAlmanacIonoBeta1_Type.__name__ = "DisplayString"
_GpsAlmanacIonoBeta1_Object = MibScalar
gpsAlmanacIonoBeta1 = _GpsAlmanacIonoBeta1_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 62),
    _GpsAlmanacIonoBeta1_Type()
)
gpsAlmanacIonoBeta1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacIonoBeta1.setStatus("current")


class _GpsAlmanacIonoBeta2_Type(DisplayString):
    """Custom type gpsAlmanacIonoBeta2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsAlmanacIonoBeta2_Type.__name__ = "DisplayString"
_GpsAlmanacIonoBeta2_Object = MibScalar
gpsAlmanacIonoBeta2 = _GpsAlmanacIonoBeta2_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 63),
    _GpsAlmanacIonoBeta2_Type()
)
gpsAlmanacIonoBeta2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacIonoBeta2.setStatus("current")


class _GpsAlmanacIonoBeta3_Type(DisplayString):
    """Custom type gpsAlmanacIonoBeta3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsAlmanacIonoBeta3_Type.__name__ = "DisplayString"
_GpsAlmanacIonoBeta3_Object = MibScalar
gpsAlmanacIonoBeta3 = _GpsAlmanacIonoBeta3_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 64),
    _GpsAlmanacIonoBeta3_Type()
)
gpsAlmanacIonoBeta3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacIonoBeta3.setStatus("current")
_GpsAlmanacIonoWNa_Type = Integer32
_GpsAlmanacIonoWNa_Object = MibScalar
gpsAlmanacIonoWNa = _GpsAlmanacIonoWNa_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 65),
    _GpsAlmanacIonoWNa_Type()
)
gpsAlmanacIonoWNa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacIonoWNa.setStatus("current")
_GpsAlmanacIonotoa_Type = Integer32
_GpsAlmanacIonotoa_Object = MibScalar
gpsAlmanacIonotoa = _GpsAlmanacIonotoa_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 66),
    _GpsAlmanacIonotoa_Type()
)
gpsAlmanacIonotoa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAlmanacIonotoa.setStatus("current")


class _GpsRTICMode_Type(Integer32):
    """Custom type gpsRTICMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("gpsRTICModeOFF", 0),
          ("gpsRTICModeON", 1))
    )


_GpsRTICMode_Type.__name__ = "Integer32"
_GpsRTICMode_Object = MibScalar
gpsRTICMode = _GpsRTICMode_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 67),
    _GpsRTICMode_Type()
)
gpsRTICMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsRTICMode.setStatus("current")


class _GpsRTICValid_Type(Integer32):
    """Custom type gpsRTICValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("gpsRTICValidFALSE", 0),
          ("gpsRTICValidTRUE", 1))
    )


_GpsRTICValid_Type.__name__ = "Integer32"
_GpsRTICValid_Object = MibScalar
gpsRTICValid = _GpsRTICValid_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 68),
    _GpsRTICValid_Type()
)
gpsRTICValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsRTICValid.setStatus("current")


class _GpsKlobucharEnsembleDelay_Type(DisplayString):
    """Custom type gpsKlobucharEnsembleDelay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsKlobucharEnsembleDelay_Type.__name__ = "DisplayString"
_GpsKlobucharEnsembleDelay_Object = MibScalar
gpsKlobucharEnsembleDelay = _GpsKlobucharEnsembleDelay_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 69),
    _GpsKlobucharEnsembleDelay_Type()
)
gpsKlobucharEnsembleDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsKlobucharEnsembleDelay.setStatus("current")


class _GpsRTICEnsembleDelay_Type(DisplayString):
    """Custom type gpsRTICEnsembleDelay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsRTICEnsembleDelay_Type.__name__ = "DisplayString"
_GpsRTICEnsembleDelay_Object = MibScalar
gpsRTICEnsembleDelay = _GpsRTICEnsembleDelay_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 70),
    _GpsRTICEnsembleDelay_Type()
)
gpsRTICEnsembleDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsRTICEnsembleDelay.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 71),
    _GpsFaultNibble0Status_Type()
)
gpsFaultNibble0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsFaultNibble0Status.setStatus("current")


class _GpsFaultNibble1Status_Type(Bits):
    """Custom type gpsFaultNibble1Status based on Bits"""
    namedValues = NamedValues(
        *(("gpsReceiverFlt", 0),
          ("gpsNTPNotPolling", 1),
          ("gpsRefTimeFlt", 2),
          ("gpsReceiverCommFlt", 3))
    )

_GpsFaultNibble1Status_Type.__name__ = "Bits"
_GpsFaultNibble1Status_Object = MibScalar
gpsFaultNibble1Status = _GpsFaultNibble1Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 72),
    _GpsFaultNibble1Status_Type()
)
gpsFaultNibble1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsFaultNibble1Status.setStatus("current")


class _GpsFaultNibble2Status_Type(Bits):
    """Custom type gpsFaultNibble2Status based on Bits"""
    namedValues = NamedValues(
        *(("gpsAntennaFlt", 0),
          ("gpsOscPLLFlt", 1),
          ("gpsSecPwrSplyFlt", 2),
          ("gpsPriPwrSplyFlt", 3))
    )

_GpsFaultNibble2Status_Type.__name__ = "Bits"
_GpsFaultNibble2Status_Object = MibScalar
gpsFaultNibble2Status = _GpsFaultNibble2Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 73),
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
          ("gpsHP5071a", 2),
          ("gpsPlugInOpts", 3))
    )

_GpsFaultNibble3Status_Type.__name__ = "Bits"
_GpsFaultNibble3Status_Object = MibScalar
gpsFaultNibble3Status = _GpsFaultNibble3Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 74),
    _GpsFaultNibble3Status_Type()
)
gpsFaultNibble3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsFaultNibble3Status.setStatus("current")


class _GpsHP5071AOperNibble0Status_Type(Bits):
    """Custom type gpsHP5071AOperNibble0Status based on Bits"""
    namedValues = NamedValues(
        *(("csNotUsed0", 0),
          ("csNotUsed1", 1),
          ("csNotUsed2", 2),
          ("csCalibrating", 3))
    )

_GpsHP5071AOperNibble0Status_Type.__name__ = "Bits"
_GpsHP5071AOperNibble0Status_Object = MibScalar
gpsHP5071AOperNibble0Status = _GpsHP5071AOperNibble0Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 75),
    _GpsHP5071AOperNibble0Status_Type()
)
gpsHP5071AOperNibble0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHP5071AOperNibble0Status.setStatus("current")


class _GpsHP5071AOperNibble2Status_Type(Bits):
    """Custom type gpsHP5071AOperNibble2Status based on Bits"""
    namedValues = NamedValues(
        *(("csFatal", 0),
          ("csNormal", 1),
          ("csOnBattery", 2),
          ("csStandby", 3))
    )

_GpsHP5071AOperNibble2Status_Type.__name__ = "Bits"
_GpsHP5071AOperNibble2Status_Object = MibScalar
gpsHP5071AOperNibble2Status = _GpsHP5071AOperNibble2Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 76),
    _GpsHP5071AOperNibble2Status_Type()
)
gpsHP5071AOperNibble2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHP5071AOperNibble2Status.setStatus("current")


class _GpsHP5071AOperNibble3Status_Type(Bits):
    """Custom type gpsHP5071AOperNibble3Status based on Bits"""
    namedValues = NamedValues(
        *(("csNotUsed0", 0),
          ("csNotUsed1", 1),
          ("csNotUsed2", 2),
          ("csSteered", 3))
    )

_GpsHP5071AOperNibble3Status_Type.__name__ = "Bits"
_GpsHP5071AOperNibble3Status_Object = MibScalar
gpsHP5071AOperNibble3Status = _GpsHP5071AOperNibble3Status_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 77),
    _GpsHP5071AOperNibble3Status_Type()
)
gpsHP5071AOperNibble3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHP5071AOperNibble3Status.setStatus("current")


class _GpsHP5071AQuesNibble0Data_Type(Bits):
    """Custom type gpsHP5071AQuesNibble0Data based on Bits"""
    namedValues = NamedValues(
        *(("csNotUsed0", 0),
          ("csTime", 1),
          ("csNotUsed2", 2),
          ("csNotUsed3", 3))
    )

_GpsHP5071AQuesNibble0Data_Type.__name__ = "Bits"
_GpsHP5071AQuesNibble0Data_Object = MibScalar
gpsHP5071AQuesNibble0Data = _GpsHP5071AQuesNibble0Data_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 78),
    _GpsHP5071AQuesNibble0Data_Type()
)
gpsHP5071AQuesNibble0Data.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHP5071AQuesNibble0Data.setStatus("current")


class _GpsHP5071AQuesNibble1Data_Type(Bits):
    """Custom type gpsHP5071AQuesNibble1Data based on Bits"""
    namedValues = NamedValues(
        *(("csNotUsed0", 0),
          ("csPhase", 1),
          ("csFrequency", 2),
          ("csNotUsed3", 3))
    )

_GpsHP5071AQuesNibble1Data_Type.__name__ = "Bits"
_GpsHP5071AQuesNibble1Data_Object = MibScalar
gpsHP5071AQuesNibble1Data = _GpsHP5071AQuesNibble1Data_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 79),
    _GpsHP5071AQuesNibble1Data_Type()
)
gpsHP5071AQuesNibble1Data.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHP5071AQuesNibble1Data.setStatus("current")


class _GpsHP5071ACsBeamI_Type(DisplayString):
    """Custom type gpsHP5071ACsBeamI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GpsHP5071ACsBeamI_Type.__name__ = "DisplayString"
_GpsHP5071ACsBeamI_Object = MibScalar
gpsHP5071ACsBeamI = _GpsHP5071ACsBeamI_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 80),
    _GpsHP5071ACsBeamI_Type()
)
gpsHP5071ACsBeamI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHP5071ACsBeamI.setStatus("current")


class _GpsHP5071ACFieldI_Type(DisplayString):
    """Custom type gpsHP5071ACFieldI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GpsHP5071ACFieldI_Type.__name__ = "DisplayString"
_GpsHP5071ACFieldI_Object = MibScalar
gpsHP5071ACFieldI = _GpsHP5071ACFieldI_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 81),
    _GpsHP5071ACFieldI_Type()
)
gpsHP5071ACFieldI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHP5071ACFieldI.setStatus("current")


class _GpsHP5071AIonPumpI_Type(DisplayString):
    """Custom type gpsHP5071AIonPumpI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GpsHP5071AIonPumpI_Type.__name__ = "DisplayString"
_GpsHP5071AIonPumpI_Object = MibScalar
gpsHP5071AIonPumpI = _GpsHP5071AIonPumpI_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 82),
    _GpsHP5071AIonPumpI_Type()
)
gpsHP5071AIonPumpI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHP5071AIonPumpI.setStatus("current")


class _GpsHP5071AEMultiplierV_Type(DisplayString):
    """Custom type gpsHP5071AEMultiplierV based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GpsHP5071AEMultiplierV_Type.__name__ = "DisplayString"
_GpsHP5071AEMultiplierV_Object = MibScalar
gpsHP5071AEMultiplierV = _GpsHP5071AEMultiplierV_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 83),
    _GpsHP5071AEMultiplierV_Type()
)
gpsHP5071AEMultiplierV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHP5071AEMultiplierV.setStatus("current")


class _GpsHP5071ACsOvenV_Type(DisplayString):
    """Custom type gpsHP5071ACsOvenV based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GpsHP5071ACsOvenV_Type.__name__ = "DisplayString"
_GpsHP5071ACsOvenV_Object = MibScalar
gpsHP5071ACsOvenV = _GpsHP5071ACsOvenV_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 84),
    _GpsHP5071ACsOvenV_Type()
)
gpsHP5071ACsOvenV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHP5071ACsOvenV.setStatus("current")


class _GpsHP5071ASignalGainPerCent_Type(DisplayString):
    """Custom type gpsHP5071ASignalGainPerCent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GpsHP5071ASignalGainPerCent_Type.__name__ = "DisplayString"
_GpsHP5071ASignalGainPerCent_Object = MibScalar
gpsHP5071ASignalGainPerCent = _GpsHP5071ASignalGainPerCent_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 85),
    _GpsHP5071ASignalGainPerCent_Type()
)
gpsHP5071ASignalGainPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHP5071ASignalGainPerCent.setStatus("current")


class _GpsHP5071ARFAmplitude1PerCent_Type(DisplayString):
    """Custom type gpsHP5071ARFAmplitude1PerCent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GpsHP5071ARFAmplitude1PerCent_Type.__name__ = "DisplayString"
_GpsHP5071ARFAmplitude1PerCent_Object = MibScalar
gpsHP5071ARFAmplitude1PerCent = _GpsHP5071ARFAmplitude1PerCent_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 86),
    _GpsHP5071ARFAmplitude1PerCent_Type()
)
gpsHP5071ARFAmplitude1PerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHP5071ARFAmplitude1PerCent.setStatus("current")


class _GpsHP5071ARFAmplitude2PerCent_Type(DisplayString):
    """Custom type gpsHP5071ARFAmplitude2PerCent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GpsHP5071ARFAmplitude2PerCent_Type.__name__ = "DisplayString"
_GpsHP5071ARFAmplitude2PerCent_Object = MibScalar
gpsHP5071ARFAmplitude2PerCent = _GpsHP5071ARFAmplitude2PerCent_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 87),
    _GpsHP5071ARFAmplitude2PerCent_Type()
)
gpsHP5071ARFAmplitude2PerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHP5071ARFAmplitude2PerCent.setStatus("current")


class _GpsHP5071AOscillatorOvenV_Type(DisplayString):
    """Custom type gpsHP5071AOscillatorOvenV based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GpsHP5071AOscillatorOvenV_Type.__name__ = "DisplayString"
_GpsHP5071AOscillatorOvenV_Object = MibScalar
gpsHP5071AOscillatorOvenV = _GpsHP5071AOscillatorOvenV_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 88),
    _GpsHP5071AOscillatorOvenV_Type()
)
gpsHP5071AOscillatorOvenV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHP5071AOscillatorOvenV.setStatus("current")


class _GpsHP5071AOscillatorControlPerCent_Type(DisplayString):
    """Custom type gpsHP5071AOscillatorControlPerCent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GpsHP5071AOscillatorControlPerCent_Type.__name__ = "DisplayString"
_GpsHP5071AOscillatorControlPerCent_Object = MibScalar
gpsHP5071AOscillatorControlPerCent = _GpsHP5071AOscillatorControlPerCent_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 89),
    _GpsHP5071AOscillatorControlPerCent_Type()
)
gpsHP5071AOscillatorControlPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHP5071AOscillatorControlPerCent.setStatus("current")
_GCPUIO_ObjectIdentity = ObjectIdentity
gCPUIO = _GCPUIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 14, 3)
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 3, 3),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 3, 4),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 3, 5),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 3, 6),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 3, 7),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 3, 8),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 3, 9),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 3, 10),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 3, 11),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 3, 12),
    _GcpuioConnC_Type()
)
gcpuioConnC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gcpuioConnC.setStatus("current")
_GPlugInOptions_ObjectIdentity = ObjectIdentity
gPlugInOptions = _GPlugInOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4)
)
_GoptSlot1_ObjectIdentity = ObjectIdentity
goptSlot1 = _GoptSlot1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 1)
)


class _GoptSlot1Desc_Type(DisplayString):
    """Custom type goptSlot1Desc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot1Desc_Type.__name__ = "DisplayString"
_GoptSlot1Desc_Object = MibScalar
goptSlot1Desc = _GoptSlot1Desc_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 1, 1),
    _GoptSlot1Desc_Type()
)
goptSlot1Desc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot1Desc.setStatus("current")


class _GoptSlot1A_Type(DisplayString):
    """Custom type goptSlot1A based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot1A_Type.__name__ = "DisplayString"
_GoptSlot1A_Object = MibScalar
goptSlot1A = _GoptSlot1A_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 1, 2),
    _GoptSlot1A_Type()
)
goptSlot1A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot1A.setStatus("current")


class _GoptSlot1B_Type(DisplayString):
    """Custom type goptSlot1B based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot1B_Type.__name__ = "DisplayString"
_GoptSlot1B_Object = MibScalar
goptSlot1B = _GoptSlot1B_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 1, 3),
    _GoptSlot1B_Type()
)
goptSlot1B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot1B.setStatus("current")


class _GoptSlot1C_Type(DisplayString):
    """Custom type goptSlot1C based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot1C_Type.__name__ = "DisplayString"
_GoptSlot1C_Object = MibScalar
goptSlot1C = _GoptSlot1C_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 1, 4),
    _GoptSlot1C_Type()
)
goptSlot1C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot1C.setStatus("current")


class _GoptSlot1D_Type(DisplayString):
    """Custom type goptSlot1D based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot1D_Type.__name__ = "DisplayString"
_GoptSlot1D_Object = MibScalar
goptSlot1D = _GoptSlot1D_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 1, 5),
    _GoptSlot1D_Type()
)
goptSlot1D.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot1D.setStatus("current")


class _GoptSlot1E_Type(DisplayString):
    """Custom type goptSlot1E based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot1E_Type.__name__ = "DisplayString"
_GoptSlot1E_Object = MibScalar
goptSlot1E = _GoptSlot1E_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 1, 6),
    _GoptSlot1E_Type()
)
goptSlot1E.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot1E.setStatus("current")


class _GoptSlot1F_Type(DisplayString):
    """Custom type goptSlot1F based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot1F_Type.__name__ = "DisplayString"
_GoptSlot1F_Object = MibScalar
goptSlot1F = _GoptSlot1F_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 1, 7),
    _GoptSlot1F_Type()
)
goptSlot1F.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot1F.setStatus("current")
_GoptSlot2_ObjectIdentity = ObjectIdentity
goptSlot2 = _GoptSlot2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 2)
)


class _GoptSlot2Desc_Type(DisplayString):
    """Custom type goptSlot2Desc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot2Desc_Type.__name__ = "DisplayString"
_GoptSlot2Desc_Object = MibScalar
goptSlot2Desc = _GoptSlot2Desc_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 2, 1),
    _GoptSlot2Desc_Type()
)
goptSlot2Desc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot2Desc.setStatus("current")


class _GoptSlot2A_Type(DisplayString):
    """Custom type goptSlot2A based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot2A_Type.__name__ = "DisplayString"
_GoptSlot2A_Object = MibScalar
goptSlot2A = _GoptSlot2A_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 2, 2),
    _GoptSlot2A_Type()
)
goptSlot2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot2A.setStatus("current")


class _GoptSlot2B_Type(DisplayString):
    """Custom type goptSlot2B based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot2B_Type.__name__ = "DisplayString"
_GoptSlot2B_Object = MibScalar
goptSlot2B = _GoptSlot2B_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 2, 3),
    _GoptSlot2B_Type()
)
goptSlot2B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot2B.setStatus("current")


class _GoptSlot2C_Type(DisplayString):
    """Custom type goptSlot2C based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot2C_Type.__name__ = "DisplayString"
_GoptSlot2C_Object = MibScalar
goptSlot2C = _GoptSlot2C_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 2, 4),
    _GoptSlot2C_Type()
)
goptSlot2C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot2C.setStatus("current")


class _GoptSlot2D_Type(DisplayString):
    """Custom type goptSlot2D based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot2D_Type.__name__ = "DisplayString"
_GoptSlot2D_Object = MibScalar
goptSlot2D = _GoptSlot2D_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 2, 5),
    _GoptSlot2D_Type()
)
goptSlot2D.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot2D.setStatus("current")


class _GoptSlot2E_Type(DisplayString):
    """Custom type goptSlot2E based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot2E_Type.__name__ = "DisplayString"
_GoptSlot2E_Object = MibScalar
goptSlot2E = _GoptSlot2E_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 2, 6),
    _GoptSlot2E_Type()
)
goptSlot2E.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot2E.setStatus("current")


class _GoptSlot2F_Type(DisplayString):
    """Custom type goptSlot2F based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot2F_Type.__name__ = "DisplayString"
_GoptSlot2F_Object = MibScalar
goptSlot2F = _GoptSlot2F_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 2, 7),
    _GoptSlot2F_Type()
)
goptSlot2F.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot2F.setStatus("current")
_GoptSlot3_ObjectIdentity = ObjectIdentity
goptSlot3 = _GoptSlot3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 3)
)


class _GoptSlot3Desc_Type(DisplayString):
    """Custom type goptSlot3Desc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot3Desc_Type.__name__ = "DisplayString"
_GoptSlot3Desc_Object = MibScalar
goptSlot3Desc = _GoptSlot3Desc_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 3, 1),
    _GoptSlot3Desc_Type()
)
goptSlot3Desc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot3Desc.setStatus("current")


class _GoptSlot3A_Type(DisplayString):
    """Custom type goptSlot3A based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot3A_Type.__name__ = "DisplayString"
_GoptSlot3A_Object = MibScalar
goptSlot3A = _GoptSlot3A_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 3, 2),
    _GoptSlot3A_Type()
)
goptSlot3A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot3A.setStatus("current")


class _GoptSlot3B_Type(DisplayString):
    """Custom type goptSlot3B based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot3B_Type.__name__ = "DisplayString"
_GoptSlot3B_Object = MibScalar
goptSlot3B = _GoptSlot3B_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 3, 3),
    _GoptSlot3B_Type()
)
goptSlot3B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot3B.setStatus("current")


class _GoptSlot3C_Type(DisplayString):
    """Custom type goptSlot3C based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot3C_Type.__name__ = "DisplayString"
_GoptSlot3C_Object = MibScalar
goptSlot3C = _GoptSlot3C_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 3, 4),
    _GoptSlot3C_Type()
)
goptSlot3C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot3C.setStatus("current")


class _GoptSlot3D_Type(DisplayString):
    """Custom type goptSlot3D based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot3D_Type.__name__ = "DisplayString"
_GoptSlot3D_Object = MibScalar
goptSlot3D = _GoptSlot3D_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 3, 5),
    _GoptSlot3D_Type()
)
goptSlot3D.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot3D.setStatus("current")


class _GoptSlot3E_Type(DisplayString):
    """Custom type goptSlot3E based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot3E_Type.__name__ = "DisplayString"
_GoptSlot3E_Object = MibScalar
goptSlot3E = _GoptSlot3E_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 3, 6),
    _GoptSlot3E_Type()
)
goptSlot3E.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot3E.setStatus("current")


class _GoptSlot3F_Type(DisplayString):
    """Custom type goptSlot3F based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot3F_Type.__name__ = "DisplayString"
_GoptSlot3F_Object = MibScalar
goptSlot3F = _GoptSlot3F_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 3, 7),
    _GoptSlot3F_Type()
)
goptSlot3F.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot3F.setStatus("current")
_GoptSlot4_ObjectIdentity = ObjectIdentity
goptSlot4 = _GoptSlot4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 4)
)


class _GoptSlot4Desc_Type(DisplayString):
    """Custom type goptSlot4Desc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot4Desc_Type.__name__ = "DisplayString"
_GoptSlot4Desc_Object = MibScalar
goptSlot4Desc = _GoptSlot4Desc_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 4, 1),
    _GoptSlot4Desc_Type()
)
goptSlot4Desc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot4Desc.setStatus("current")


class _GoptSlot4A_Type(DisplayString):
    """Custom type goptSlot4A based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot4A_Type.__name__ = "DisplayString"
_GoptSlot4A_Object = MibScalar
goptSlot4A = _GoptSlot4A_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 4, 2),
    _GoptSlot4A_Type()
)
goptSlot4A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot4A.setStatus("current")


class _GoptSlot4B_Type(DisplayString):
    """Custom type goptSlot4B based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot4B_Type.__name__ = "DisplayString"
_GoptSlot4B_Object = MibScalar
goptSlot4B = _GoptSlot4B_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 4, 3),
    _GoptSlot4B_Type()
)
goptSlot4B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot4B.setStatus("current")


class _GoptSlot4C_Type(DisplayString):
    """Custom type goptSlot4C based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot4C_Type.__name__ = "DisplayString"
_GoptSlot4C_Object = MibScalar
goptSlot4C = _GoptSlot4C_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 4, 4),
    _GoptSlot4C_Type()
)
goptSlot4C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot4C.setStatus("current")


class _GoptSlot4D_Type(DisplayString):
    """Custom type goptSlot4D based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot4D_Type.__name__ = "DisplayString"
_GoptSlot4D_Object = MibScalar
goptSlot4D = _GoptSlot4D_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 4, 5),
    _GoptSlot4D_Type()
)
goptSlot4D.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot4D.setStatus("current")


class _GoptSlot4E_Type(DisplayString):
    """Custom type goptSlot4E based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot4E_Type.__name__ = "DisplayString"
_GoptSlot4E_Object = MibScalar
goptSlot4E = _GoptSlot4E_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 4, 6),
    _GoptSlot4E_Type()
)
goptSlot4E.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot4E.setStatus("current")


class _GoptSlot4F_Type(DisplayString):
    """Custom type goptSlot4F based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot4F_Type.__name__ = "DisplayString"
_GoptSlot4F_Object = MibScalar
goptSlot4F = _GoptSlot4F_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 4, 7),
    _GoptSlot4F_Type()
)
goptSlot4F.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot4F.setStatus("current")
_GoptSlot5_ObjectIdentity = ObjectIdentity
goptSlot5 = _GoptSlot5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 5)
)


class _GoptSlot5Desc_Type(DisplayString):
    """Custom type goptSlot5Desc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot5Desc_Type.__name__ = "DisplayString"
_GoptSlot5Desc_Object = MibScalar
goptSlot5Desc = _GoptSlot5Desc_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 5, 1),
    _GoptSlot5Desc_Type()
)
goptSlot5Desc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot5Desc.setStatus("current")


class _GoptSlot5A_Type(DisplayString):
    """Custom type goptSlot5A based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot5A_Type.__name__ = "DisplayString"
_GoptSlot5A_Object = MibScalar
goptSlot5A = _GoptSlot5A_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 5, 2),
    _GoptSlot5A_Type()
)
goptSlot5A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot5A.setStatus("current")


class _GoptSlot5B_Type(DisplayString):
    """Custom type goptSlot5B based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot5B_Type.__name__ = "DisplayString"
_GoptSlot5B_Object = MibScalar
goptSlot5B = _GoptSlot5B_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 5, 3),
    _GoptSlot5B_Type()
)
goptSlot5B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot5B.setStatus("current")


class _GoptSlot5C_Type(DisplayString):
    """Custom type goptSlot5C based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot5C_Type.__name__ = "DisplayString"
_GoptSlot5C_Object = MibScalar
goptSlot5C = _GoptSlot5C_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 5, 4),
    _GoptSlot5C_Type()
)
goptSlot5C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot5C.setStatus("current")


class _GoptSlot5D_Type(DisplayString):
    """Custom type goptSlot5D based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot5D_Type.__name__ = "DisplayString"
_GoptSlot5D_Object = MibScalar
goptSlot5D = _GoptSlot5D_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 5, 5),
    _GoptSlot5D_Type()
)
goptSlot5D.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot5D.setStatus("current")


class _GoptSlot5E_Type(DisplayString):
    """Custom type goptSlot5E based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot5E_Type.__name__ = "DisplayString"
_GoptSlot5E_Object = MibScalar
goptSlot5E = _GoptSlot5E_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 5, 6),
    _GoptSlot5E_Type()
)
goptSlot5E.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot5E.setStatus("current")


class _GoptSlot5F_Type(DisplayString):
    """Custom type goptSlot5F based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GoptSlot5F_Type.__name__ = "DisplayString"
_GoptSlot5F_Object = MibScalar
goptSlot5F = _GoptSlot5F_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 4, 5, 7),
    _GoptSlot5F_Type()
)
goptSlot5F.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSlot5F.setStatus("current")
_Gptp0_ObjectIdentity = ObjectIdentity
gptp0 = _Gptp0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 14, 5)
)
_Gptp0Version_Type = Integer32
_Gptp0Version_Object = MibScalar
gptp0Version = _Gptp0Version_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 1),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 2),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 3),
    _Gptp0AnnounceInterval_Type()
)
gptp0AnnounceInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0AnnounceInterval.setStatus("current")
_Gptp0Priority1_Type = Integer32
_Gptp0Priority1_Object = MibScalar
gptp0Priority1 = _Gptp0Priority1_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 4),
    _Gptp0Priority1_Type()
)
gptp0Priority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0Priority1.setStatus("current")
_Gptp0Priority2_Type = Integer32
_Gptp0Priority2_Object = MibScalar
gptp0Priority2 = _Gptp0Priority2_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 5),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 6),
    _Gptp0DelayMechanism_Type()
)
gptp0DelayMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0DelayMechanism.setStatus("current")
_Gptp0Domain_Type = Integer32
_Gptp0Domain_Object = MibScalar
gptp0Domain = _Gptp0Domain_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 7),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 8),
    _Gptp0TimeMode_Type()
)
gptp0TimeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0TimeMode.setStatus("current")
_Gptp0TTL_Type = Integer32
_Gptp0TTL_Object = MibScalar
gptp0TTL = _Gptp0TTL_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 9),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 10),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 11),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 12),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 13),
    _Gptp0TimeSource_Type()
)
gptp0TimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0TimeSource.setStatus("current")
_Gptp0UTCOffset_Type = Integer32
_Gptp0UTCOffset_Object = MibScalar
gptp0UTCOffset = _Gptp0UTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 14),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 15),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 16),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 17),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 18),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 19),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 5, 20),
    _Gptp0FreqTraceable_Type()
)
gptp0FreqTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp0FreqTraceable.setStatus("current")
_Gptp1_ObjectIdentity = ObjectIdentity
gptp1 = _Gptp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 14, 6)
)
_Gptp1Version_Type = Integer32
_Gptp1Version_Object = MibScalar
gptp1Version = _Gptp1Version_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 1),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 2),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 3),
    _Gptp1AnnounceInterval_Type()
)
gptp1AnnounceInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1AnnounceInterval.setStatus("current")
_Gptp1Priority1_Type = Integer32
_Gptp1Priority1_Object = MibScalar
gptp1Priority1 = _Gptp1Priority1_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 4),
    _Gptp1Priority1_Type()
)
gptp1Priority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1Priority1.setStatus("current")
_Gptp1Priority2_Type = Integer32
_Gptp1Priority2_Object = MibScalar
gptp1Priority2 = _Gptp1Priority2_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 5),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 6),
    _Gptp1DelayMechanism_Type()
)
gptp1DelayMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1DelayMechanism.setStatus("current")
_Gptp1Domain_Type = Integer32
_Gptp1Domain_Object = MibScalar
gptp1Domain = _Gptp1Domain_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 7),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 8),
    _Gptp1TimeMode_Type()
)
gptp1TimeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1TimeMode.setStatus("current")
_Gptp1TTL_Type = Integer32
_Gptp1TTL_Object = MibScalar
gptp1TTL = _Gptp1TTL_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 9),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 10),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 11),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 12),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 13),
    _Gptp1TimeSource_Type()
)
gptp1TimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1TimeSource.setStatus("current")
_Gptp1UTCOffset_Type = Integer32
_Gptp1UTCOffset_Object = MibScalar
gptp1UTCOffset = _Gptp1UTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 14),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 15),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 16),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 17),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 18),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 19),
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
    (1, 3, 6, 1, 4, 1, 13827, 14, 6, 20),
    _Gptp1FreqTraceable_Type()
)
gptp1FreqTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gptp1FreqTraceable.setStatus("current")

# Managed Objects groups


# Notification objects

gntpTrapLeapIndBitsChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 0, 1)
)
gntpTrapLeapIndBitsChange.setObjects(
    ("MERIDIAN2-MIB", "gntpLeapIndBits")
)
if mibBuilder.loadTexts:
    gntpTrapLeapIndBitsChange.setStatus(
        "current"
    )

gntpTrapStratumChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 14, 1, 0, 2)
)
gntpTrapStratumChange.setObjects(
    ("MERIDIAN2-MIB", "gntpStratum")
)
if mibBuilder.loadTexts:
    gntpTrapStratumChange.setStatus(
        "current"
    )

gpsTrapFaultStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 0, 1)
)
gpsTrapFaultStatusChange.setObjects(
    ("MERIDIAN2-MIB", "gpsFaultStatus")
)
if mibBuilder.loadTexts:
    gpsTrapFaultStatusChange.setStatus(
        "current"
    )

gpsTrapFault2StatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 0, 2)
)
gpsTrapFault2StatusChange.setObjects(
    ("MERIDIAN2-MIB", "gpsFault2Status")
)
if mibBuilder.loadTexts:
    gpsTrapFault2StatusChange.setStatus(
        "current"
    )

gpsTrapTimeFigureOfMeritChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 14, 2, 0, 3)
)
gpsTrapTimeFigureOfMeritChange.setObjects(
    ("MERIDIAN2-MIB", "gpsTimeFigureOfMerit")
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
    "MERIDIAN2-MIB",
    **{"endRunTechnologiesMIB": endRunTechnologiesMIB,
       "endRunTechnologies": endRunTechnologies,
       "meridian2GPS": meridian2GPS,
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
       "gpsReceiverFaultNibble0Status": gpsReceiverFaultNibble0Status,
       "gpsReceiverFaultNibble1Status": gpsReceiverFaultNibble1Status,
       "gpsReceiverFaultNibble2Status": gpsReceiverFaultNibble2Status,
       "gpsReceiverFaultNibble3Status": gpsReceiverFaultNibble3Status,
       "gpsTimeFigureOfMerit": gpsTimeFigureOfMerit,
       "gpsSigProcState": gpsSigProcState,
       "gpsReceiverSigProcState": gpsReceiverSigProcState,
       "gpsNumTrackSats": gpsNumTrackSats,
       "gpsAGC": gpsAGC,
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
       "gpsGPSminusUTCOffsetPicoSecs": gpsGPSminusUTCOffsetPicoSecs,
       "gpsSubsystemVersion": gpsSubsystemVersion,
       "gpsReceiverVersion": gpsReceiverVersion,
       "gpsDynamicMode": gpsDynamicMode,
       "gpsCalibrationDelayNanoSecs": gpsCalibrationDelayNanoSecs,
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
       "gpsTimeFigureOfMeritFaultLevel": gpsTimeFigureOfMeritFaultLevel,
       "gpsInhibitOutputsMode": gpsInhibitOutputsMode,
       "gpsAlmanacIonoAlpha0": gpsAlmanacIonoAlpha0,
       "gpsAlmanacIonoAlpha1": gpsAlmanacIonoAlpha1,
       "gpsAlmanacIonoAlpha2": gpsAlmanacIonoAlpha2,
       "gpsAlmanacIonoAlpha3": gpsAlmanacIonoAlpha3,
       "gpsAlmanacIonoBeta0": gpsAlmanacIonoBeta0,
       "gpsAlmanacIonoBeta1": gpsAlmanacIonoBeta1,
       "gpsAlmanacIonoBeta2": gpsAlmanacIonoBeta2,
       "gpsAlmanacIonoBeta3": gpsAlmanacIonoBeta3,
       "gpsAlmanacIonoWNa": gpsAlmanacIonoWNa,
       "gpsAlmanacIonotoa": gpsAlmanacIonotoa,
       "gpsRTICMode": gpsRTICMode,
       "gpsRTICValid": gpsRTICValid,
       "gpsKlobucharEnsembleDelay": gpsKlobucharEnsembleDelay,
       "gpsRTICEnsembleDelay": gpsRTICEnsembleDelay,
       "gpsFaultNibble0Status": gpsFaultNibble0Status,
       "gpsFaultNibble1Status": gpsFaultNibble1Status,
       "gpsFaultNibble2Status": gpsFaultNibble2Status,
       "gpsFaultNibble3Status": gpsFaultNibble3Status,
       "gpsHP5071AOperNibble0Status": gpsHP5071AOperNibble0Status,
       "gpsHP5071AOperNibble2Status": gpsHP5071AOperNibble2Status,
       "gpsHP5071AOperNibble3Status": gpsHP5071AOperNibble3Status,
       "gpsHP5071AQuesNibble0Data": gpsHP5071AQuesNibble0Data,
       "gpsHP5071AQuesNibble1Data": gpsHP5071AQuesNibble1Data,
       "gpsHP5071ACsBeamI": gpsHP5071ACsBeamI,
       "gpsHP5071ACFieldI": gpsHP5071ACFieldI,
       "gpsHP5071AIonPumpI": gpsHP5071AIonPumpI,
       "gpsHP5071AEMultiplierV": gpsHP5071AEMultiplierV,
       "gpsHP5071ACsOvenV": gpsHP5071ACsOvenV,
       "gpsHP5071ASignalGainPerCent": gpsHP5071ASignalGainPerCent,
       "gpsHP5071ARFAmplitude1PerCent": gpsHP5071ARFAmplitude1PerCent,
       "gpsHP5071ARFAmplitude2PerCent": gpsHP5071ARFAmplitude2PerCent,
       "gpsHP5071AOscillatorOvenV": gpsHP5071AOscillatorOvenV,
       "gpsHP5071AOscillatorControlPerCent": gpsHP5071AOscillatorControlPerCent,
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
       "gPlugInOptions": gPlugInOptions,
       "goptSlot1": goptSlot1,
       "goptSlot1Desc": goptSlot1Desc,
       "goptSlot1A": goptSlot1A,
       "goptSlot1B": goptSlot1B,
       "goptSlot1C": goptSlot1C,
       "goptSlot1D": goptSlot1D,
       "goptSlot1E": goptSlot1E,
       "goptSlot1F": goptSlot1F,
       "goptSlot2": goptSlot2,
       "goptSlot2Desc": goptSlot2Desc,
       "goptSlot2A": goptSlot2A,
       "goptSlot2B": goptSlot2B,
       "goptSlot2C": goptSlot2C,
       "goptSlot2D": goptSlot2D,
       "goptSlot2E": goptSlot2E,
       "goptSlot2F": goptSlot2F,
       "goptSlot3": goptSlot3,
       "goptSlot3Desc": goptSlot3Desc,
       "goptSlot3A": goptSlot3A,
       "goptSlot3B": goptSlot3B,
       "goptSlot3C": goptSlot3C,
       "goptSlot3D": goptSlot3D,
       "goptSlot3E": goptSlot3E,
       "goptSlot3F": goptSlot3F,
       "goptSlot4": goptSlot4,
       "goptSlot4Desc": goptSlot4Desc,
       "goptSlot4A": goptSlot4A,
       "goptSlot4B": goptSlot4B,
       "goptSlot4C": goptSlot4C,
       "goptSlot4D": goptSlot4D,
       "goptSlot4E": goptSlot4E,
       "goptSlot4F": goptSlot4F,
       "goptSlot5": goptSlot5,
       "goptSlot5Desc": goptSlot5Desc,
       "goptSlot5A": goptSlot5A,
       "goptSlot5B": goptSlot5B,
       "goptSlot5C": goptSlot5C,
       "goptSlot5D": goptSlot5D,
       "goptSlot5E": goptSlot5E,
       "goptSlot5F": goptSlot5F,
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
