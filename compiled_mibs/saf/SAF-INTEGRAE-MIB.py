# SNMP MIB module (SAF-INTEGRAE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\saf\SAF-INTEGRAE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:24:44 2025
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(pointToPoint,) = mibBuilder.importSymbols(
    "SAF-ENTERPRISE",
    "pointToPoint")

(safIntegra,) = mibBuilder.importSymbols(
    "SAF-INTEGRA-MIB",
    "safIntegra")

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

integraE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9)
)
if mibBuilder.loadTexts:
    integraE.setRevisions(
        ("2020-04-25 00:00",
         "2020-04-22 00:00",
         "2020-01-14 00:00",
         "2019-11-21 00:00",
         "2019-06-11 00:00",
         "2019-04-23 00:00",
         "2019-03-12 00:00",
         "2019-02-04 00:00",
         "2018-11-15 00:00",
         "2018-11-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FixedDiv20(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"


class FixedDiv10(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


# MIB Managed Objects in the order of their OIDs

_IntegraEtimestamp_Type = DateAndTime
_IntegraEtimestamp_Object = MibScalar
integraEtimestamp = _IntegraEtimestamp_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 1),
    _IntegraEtimestamp_Type()
)
integraEtimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEtimestamp.setStatus("current")
_IntegraEradio_ObjectIdentity = ObjectIdentity
integraEradio = _IntegraEradio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2)
)
_IntegraEradioTxPower_Type = Integer32
_IntegraEradioTxPower_Object = MibScalar
integraEradioTxPower = _IntegraEradioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 1),
    _IntegraEradioTxPower_Type()
)
integraEradioTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraEradioTxPower.setStatus("current")
if mibBuilder.loadTexts:
    integraEradioTxPower.setUnits("dBm")
_IntegraEradioTxFrequency_Type = Integer32
_IntegraEradioTxFrequency_Object = MibScalar
integraEradioTxFrequency = _IntegraEradioTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 2),
    _IntegraEradioTxFrequency_Type()
)
integraEradioTxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraEradioTxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    integraEradioTxFrequency.setUnits("kHz")
_IntegraEradioRxLevel_Type = Integer32
_IntegraEradioRxLevel_Object = MibScalar
integraEradioRxLevel = _IntegraEradioRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 3),
    _IntegraEradioRxLevel_Type()
)
integraEradioRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEradioRxLevel.setStatus("current")
if mibBuilder.loadTexts:
    integraEradioRxLevel.setUnits("dBm")


class _IntegraEradioSide_Type(Integer32):
    """Custom type integraEradioSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2),
          ("error", 3))
    )


_IntegraEradioSide_Type.__name__ = "Integer32"
_IntegraEradioSide_Object = MibScalar
integraEradioSide = _IntegraEradioSide_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 4),
    _IntegraEradioSide_Type()
)
integraEradioSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEradioSide.setStatus("current")


class _IntegraEradioTxMute_Type(Integer32):
    """Custom type integraEradioTxMute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("error", 3))
    )


_IntegraEradioTxMute_Type.__name__ = "Integer32"
_IntegraEradioTxMute_Object = MibScalar
integraEradioTxMute = _IntegraEradioTxMute_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 5),
    _IntegraEradioTxMute_Type()
)
integraEradioTxMute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEradioTxMute.setStatus("current")
_IntegraEradioDuplexShift_Type = Integer32
_IntegraEradioDuplexShift_Object = MibScalar
integraEradioDuplexShift = _IntegraEradioDuplexShift_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 6),
    _IntegraEradioDuplexShift_Type()
)
integraEradioDuplexShift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEradioDuplexShift.setStatus("current")
if mibBuilder.loadTexts:
    integraEradioDuplexShift.setUnits("kHz")
_IntegraEradioRxFrequency_Type = Integer32
_IntegraEradioRxFrequency_Object = MibScalar
integraEradioRxFrequency = _IntegraEradioRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 7),
    _IntegraEradioRxFrequency_Type()
)
integraEradioRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEradioRxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    integraEradioRxFrequency.setUnits("kHz")
_IntegraEradioTemperature_Type = FixedDiv10
_IntegraEradioTemperature_Object = MibScalar
integraEradioTemperature = _IntegraEradioTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 8),
    _IntegraEradioTemperature_Type()
)
integraEradioTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEradioTemperature.setStatus("current")
if mibBuilder.loadTexts:
    integraEradioTemperature.setUnits("C")


class _IntegraEradioTxMuteDuration_Type(Integer32):
    """Custom type integraEradioTxMuteDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214748364),
    )


_IntegraEradioTxMuteDuration_Type.__name__ = "Integer32"
_IntegraEradioTxMuteDuration_Object = MibScalar
integraEradioTxMuteDuration = _IntegraEradioTxMuteDuration_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 9),
    _IntegraEradioTxMuteDuration_Type()
)
integraEradioTxMuteDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraEradioTxMuteDuration.setStatus("current")
if mibBuilder.loadTexts:
    integraEradioTxMuteDuration.setUnits("s")
_IntegraEradioRangesTable_Object = MibTable
integraEradioRangesTable = _IntegraEradioRangesTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 10)
)
if mibBuilder.loadTexts:
    integraEradioRangesTable.setStatus("current")
_IntegraEradioRangeEntry_Object = MibTableRow
integraEradioRangeEntry = _IntegraEradioRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 10, 1)
)
integraEradioRangeEntry.setIndexNames(
    (0, "SAF-INTEGRAE-MIB", "integraEradioRangeEntryIndex"),
)
if mibBuilder.loadTexts:
    integraEradioRangeEntry.setStatus("current")


class _IntegraEradioRangeEntryIndex_Type(Integer32):
    """Custom type integraEradioRangeEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IntegraEradioRangeEntryIndex_Type.__name__ = "Integer32"
_IntegraEradioRangeEntryIndex_Object = MibTableColumn
integraEradioRangeEntryIndex = _IntegraEradioRangeEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 10, 1, 1),
    _IntegraEradioRangeEntryIndex_Type()
)
integraEradioRangeEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEradioRangeEntryIndex.setStatus("current")


class _IntegraEradioRangeDescr_Type(DisplayString):
    """Custom type integraEradioRangeDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntegraEradioRangeDescr_Type.__name__ = "DisplayString"
_IntegraEradioRangeDescr_Object = MibTableColumn
integraEradioRangeDescr = _IntegraEradioRangeDescr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 10, 1, 2),
    _IntegraEradioRangeDescr_Type()
)
integraEradioRangeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEradioRangeDescr.setStatus("current")
_IntegraEradioRangeTxPower_Type = Integer32
_IntegraEradioRangeTxPower_Object = MibTableColumn
integraEradioRangeTxPower = _IntegraEradioRangeTxPower_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 10, 1, 3),
    _IntegraEradioRangeTxPower_Type()
)
integraEradioRangeTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEradioRangeTxPower.setStatus("current")
if mibBuilder.loadTexts:
    integraEradioRangeTxPower.setUnits("dBm")
_IntegraEradioRangeTxFrequency_Type = Integer32
_IntegraEradioRangeTxFrequency_Object = MibTableColumn
integraEradioRangeTxFrequency = _IntegraEradioRangeTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 10, 1, 4),
    _IntegraEradioRangeTxFrequency_Type()
)
integraEradioRangeTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEradioRangeTxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    integraEradioRangeTxFrequency.setUnits("kHz")


class _IntegraEradioPLL_Type(Integer32):
    """Custom type integraEradioPLL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ok", 2))
    )


_IntegraEradioPLL_Type.__name__ = "Integer32"
_IntegraEradioPLL_Object = MibScalar
integraEradioPLL = _IntegraEradioPLL_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 11),
    _IntegraEradioPLL_Type()
)
integraEradioPLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEradioPLL.setStatus("current")


class _IntegraEradioRxLevelState_Type(Integer32):
    """Custom type integraEradioRxLevelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("low", 2),
          ("high", 3),
          ("error", 4))
    )


_IntegraEradioRxLevelState_Type.__name__ = "Integer32"
_IntegraEradioRxLevelState_Object = MibScalar
integraEradioRxLevelState = _IntegraEradioRxLevelState_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 12),
    _IntegraEradioRxLevelState_Type()
)
integraEradioRxLevelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEradioRxLevelState.setStatus("current")


class _IntegraEradioAtpcState_Type(Integer32):
    """Custom type integraEradioAtpcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("unknown", 3))
    )


_IntegraEradioAtpcState_Type.__name__ = "Integer32"
_IntegraEradioAtpcState_Object = MibScalar
integraEradioAtpcState = _IntegraEradioAtpcState_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 13),
    _IntegraEradioAtpcState_Type()
)
integraEradioAtpcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEradioAtpcState.setStatus("current")


class _IntegraEradioAtpcUpdatePeriod_Type(Integer32):
    """Custom type integraEradioAtpcUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214748364),
    )


_IntegraEradioAtpcUpdatePeriod_Type.__name__ = "Integer32"
_IntegraEradioAtpcUpdatePeriod_Object = MibScalar
integraEradioAtpcUpdatePeriod = _IntegraEradioAtpcUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 14),
    _IntegraEradioAtpcUpdatePeriod_Type()
)
integraEradioAtpcUpdatePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEradioAtpcUpdatePeriod.setStatus("current")
if mibBuilder.loadTexts:
    integraEradioAtpcUpdatePeriod.setUnits("s")
_IntegraEradioAtpcRxLevelMin_Type = Integer32
_IntegraEradioAtpcRxLevelMin_Object = MibScalar
integraEradioAtpcRxLevelMin = _IntegraEradioAtpcRxLevelMin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 15),
    _IntegraEradioAtpcRxLevelMin_Type()
)
integraEradioAtpcRxLevelMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEradioAtpcRxLevelMin.setStatus("current")
if mibBuilder.loadTexts:
    integraEradioAtpcRxLevelMin.setUnits("dBm")
_IntegraEradioAtpcRxLevelMax_Type = Integer32
_IntegraEradioAtpcRxLevelMax_Object = MibScalar
integraEradioAtpcRxLevelMax = _IntegraEradioAtpcRxLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 2, 16),
    _IntegraEradioAtpcRxLevelMax_Type()
)
integraEradioAtpcRxLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEradioAtpcRxLevelMax.setStatus("current")
if mibBuilder.loadTexts:
    integraEradioAtpcRxLevelMax.setUnits("dBm")
_IntegraEmodem_ObjectIdentity = ObjectIdentity
integraEmodem = _IntegraEmodem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3)
)


class _IntegraEmodemAcquireStatus_Type(Integer32):
    """Custom type integraEmodemAcquireStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acquireInProgress", 1),
          ("acquireLocked", 2),
          ("acquireFailed", 3))
    )


_IntegraEmodemAcquireStatus_Type.__name__ = "Integer32"
_IntegraEmodemAcquireStatus_Object = MibScalar
integraEmodemAcquireStatus = _IntegraEmodemAcquireStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 1),
    _IntegraEmodemAcquireStatus_Type()
)
integraEmodemAcquireStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemAcquireStatus.setStatus("current")
_IntegraEmodemNormalizedMse_Type = FixedDiv10
_IntegraEmodemNormalizedMse_Object = MibScalar
integraEmodemNormalizedMse = _IntegraEmodemNormalizedMse_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 2),
    _IntegraEmodemNormalizedMse_Type()
)
integraEmodemNormalizedMse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemNormalizedMse.setStatus("current")
if mibBuilder.loadTexts:
    integraEmodemNormalizedMse.setUnits("dB")
_IntegraEmodemFECload_Type = FixedDiv10
_IntegraEmodemFECload_Object = MibScalar
integraEmodemFECload = _IntegraEmodemFECload_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 3),
    _IntegraEmodemFECload_Type()
)
integraEmodemFECload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemFECload.setStatus("current")
if mibBuilder.loadTexts:
    integraEmodemFECload.setUnits("dB")


class _IntegraEmodemFEClocked_Type(Integer32):
    """Custom type integraEmodemFEClocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2),
          ("unknown", 3))
    )


_IntegraEmodemFEClocked_Type.__name__ = "Integer32"
_IntegraEmodemFEClocked_Object = MibScalar
integraEmodemFEClocked = _IntegraEmodemFEClocked_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 4),
    _IntegraEmodemFEClocked_Type()
)
integraEmodemFEClocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemFEClocked.setStatus("current")


class _IntegraEmodemAcquireLastStatusDetails_Type(Integer32):
    """Custom type integraEmodemAcquireLastStatusDetails based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("acquireLocked", 1),
          ("acquireSweep", 4),
          ("acquireMSEerror", 5),
          ("acquireBITerror", 6),
          ("acquireStopped", 12),
          ("acquireSMerror", 13))
    )


_IntegraEmodemAcquireLastStatusDetails_Type.__name__ = "Integer32"
_IntegraEmodemAcquireLastStatusDetails_Object = MibScalar
integraEmodemAcquireLastStatusDetails = _IntegraEmodemAcquireLastStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 5),
    _IntegraEmodemAcquireLastStatusDetails_Type()
)
integraEmodemAcquireLastStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemAcquireLastStatusDetails.setStatus("current")
_IntegraEmodemTemperature_Type = FixedDiv10
_IntegraEmodemTemperature_Object = MibScalar
integraEmodemTemperature = _IntegraEmodemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 6),
    _IntegraEmodemTemperature_Type()
)
integraEmodemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemTemperature.setStatus("current")
if mibBuilder.loadTexts:
    integraEmodemTemperature.setUnits("C")
_IntegraEmodemBandwidth_Type = Integer32
_IntegraEmodemBandwidth_Object = MibScalar
integraEmodemBandwidth = _IntegraEmodemBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 7),
    _IntegraEmodemBandwidth_Type()
)
integraEmodemBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    integraEmodemBandwidth.setUnits("kHz")
_IntegraEmodemModulation_Type = DisplayString
_IntegraEmodemModulation_Object = MibScalar
integraEmodemModulation = _IntegraEmodemModulation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 8),
    _IntegraEmodemModulation_Type()
)
integraEmodemModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemModulation.setStatus("current")
_IntegraEmodemRxModulation_Type = DisplayString
_IntegraEmodemRxModulation_Object = MibScalar
integraEmodemRxModulation = _IntegraEmodemRxModulation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 9),
    _IntegraEmodemRxModulation_Type()
)
integraEmodemRxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemRxModulation.setStatus("current")
_IntegraEmodemTxModulation_Type = DisplayString
_IntegraEmodemTxModulation_Object = MibScalar
integraEmodemTxModulation = _IntegraEmodemTxModulation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 10),
    _IntegraEmodemTxModulation_Type()
)
integraEmodemTxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemTxModulation.setStatus("current")
_IntegraEmodemRxCapacity_Type = Integer32
_IntegraEmodemRxCapacity_Object = MibScalar
integraEmodemRxCapacity = _IntegraEmodemRxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 11),
    _IntegraEmodemRxCapacity_Type()
)
integraEmodemRxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemRxCapacity.setStatus("current")
if mibBuilder.loadTexts:
    integraEmodemRxCapacity.setUnits("kb/s")
_IntegraEmodemTxCapacity_Type = Integer32
_IntegraEmodemTxCapacity_Object = MibScalar
integraEmodemTxCapacity = _IntegraEmodemTxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 12),
    _IntegraEmodemTxCapacity_Type()
)
integraEmodemTxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemTxCapacity.setStatus("current")
if mibBuilder.loadTexts:
    integraEmodemTxCapacity.setUnits("kb/s")


class _IntegraEmodemACMBengine_Type(Integer32):
    """Custom type integraEmodemACMBengine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("error", 3))
    )


_IntegraEmodemACMBengine_Type.__name__ = "Integer32"
_IntegraEmodemACMBengine_Object = MibScalar
integraEmodemACMBengine = _IntegraEmodemACMBengine_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 13),
    _IntegraEmodemACMBengine_Type()
)
integraEmodemACMBengine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemACMBengine.setStatus("current")
_IntegraEmodemCarrierOffset_Type = Integer32
_IntegraEmodemCarrierOffset_Object = MibScalar
integraEmodemCarrierOffset = _IntegraEmodemCarrierOffset_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 14),
    _IntegraEmodemCarrierOffset_Type()
)
integraEmodemCarrierOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemCarrierOffset.setStatus("current")
if mibBuilder.loadTexts:
    integraEmodemCarrierOffset.setUnits("Hz")
_IntegraEmodemCountTime_Type = Counter64
_IntegraEmodemCountTime_Object = MibScalar
integraEmodemCountTime = _IntegraEmodemCountTime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 15),
    _IntegraEmodemCountTime_Type()
)
integraEmodemCountTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemCountTime.setStatus("current")
if mibBuilder.loadTexts:
    integraEmodemCountTime.setUnits("s")
_IntegraEmodemErroredBlock_Type = Counter64
_IntegraEmodemErroredBlock_Object = MibScalar
integraEmodemErroredBlock = _IntegraEmodemErroredBlock_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 16),
    _IntegraEmodemErroredBlock_Type()
)
integraEmodemErroredBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemErroredBlock.setStatus("current")
_IntegraEmodemErroredSecond_Type = Counter64
_IntegraEmodemErroredSecond_Object = MibScalar
integraEmodemErroredSecond = _IntegraEmodemErroredSecond_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 17),
    _IntegraEmodemErroredSecond_Type()
)
integraEmodemErroredSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemErroredSecond.setStatus("current")
if mibBuilder.loadTexts:
    integraEmodemErroredSecond.setUnits("s")
_IntegraEmodemSeverelyErroredSecond_Type = Counter64
_IntegraEmodemSeverelyErroredSecond_Object = MibScalar
integraEmodemSeverelyErroredSecond = _IntegraEmodemSeverelyErroredSecond_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 18),
    _IntegraEmodemSeverelyErroredSecond_Type()
)
integraEmodemSeverelyErroredSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemSeverelyErroredSecond.setStatus("current")
if mibBuilder.loadTexts:
    integraEmodemSeverelyErroredSecond.setUnits("s")
_IntegraEmodemBackgroundBlockError_Type = Counter64
_IntegraEmodemBackgroundBlockError_Object = MibScalar
integraEmodemBackgroundBlockError = _IntegraEmodemBackgroundBlockError_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 19),
    _IntegraEmodemBackgroundBlockError_Type()
)
integraEmodemBackgroundBlockError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemBackgroundBlockError.setStatus("current")
_IntegraEmodemTotalBlockNumber_Type = Counter64
_IntegraEmodemTotalBlockNumber_Object = MibScalar
integraEmodemTotalBlockNumber = _IntegraEmodemTotalBlockNumber_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 20),
    _IntegraEmodemTotalBlockNumber_Type()
)
integraEmodemTotalBlockNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemTotalBlockNumber.setStatus("current")
_IntegraEmodemErroredSecondRatio_Type = DisplayString
_IntegraEmodemErroredSecondRatio_Object = MibScalar
integraEmodemErroredSecondRatio = _IntegraEmodemErroredSecondRatio_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 21),
    _IntegraEmodemErroredSecondRatio_Type()
)
integraEmodemErroredSecondRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemErroredSecondRatio.setStatus("current")
_IntegraEmodemSeverelyErroredSecondRatio_Type = DisplayString
_IntegraEmodemSeverelyErroredSecondRatio_Object = MibScalar
integraEmodemSeverelyErroredSecondRatio = _IntegraEmodemSeverelyErroredSecondRatio_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 22),
    _IntegraEmodemSeverelyErroredSecondRatio_Type()
)
integraEmodemSeverelyErroredSecondRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemSeverelyErroredSecondRatio.setStatus("current")
_IntegraEmodemBackgroundBlockErrorRatio_Type = DisplayString
_IntegraEmodemBackgroundBlockErrorRatio_Object = MibScalar
integraEmodemBackgroundBlockErrorRatio = _IntegraEmodemBackgroundBlockErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 23),
    _IntegraEmodemBackgroundBlockErrorRatio_Type()
)
integraEmodemBackgroundBlockErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemBackgroundBlockErrorRatio.setStatus("current")
_IntegraEmodemUptime_Type = Counter64
_IntegraEmodemUptime_Object = MibScalar
integraEmodemUptime = _IntegraEmodemUptime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 24),
    _IntegraEmodemUptime_Type()
)
integraEmodemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemUptime.setStatus("current")
if mibBuilder.loadTexts:
    integraEmodemUptime.setUnits("s")
_IntegraEmodemUnavailtime_Type = Counter64
_IntegraEmodemUnavailtime_Object = MibScalar
integraEmodemUnavailtime = _IntegraEmodemUnavailtime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 25),
    _IntegraEmodemUnavailtime_Type()
)
integraEmodemUnavailtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemUnavailtime.setStatus("current")
if mibBuilder.loadTexts:
    integraEmodemUnavailtime.setUnits("s")
_IntegraEmodemModulationACMBmin_Type = DisplayString
_IntegraEmodemModulationACMBmin_Object = MibScalar
integraEmodemModulationACMBmin = _IntegraEmodemModulationACMBmin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 26),
    _IntegraEmodemModulationACMBmin_Type()
)
integraEmodemModulationACMBmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemModulationACMBmin.setStatus("current")
_IntegraEmodemModulationACMBmax_Type = DisplayString
_IntegraEmodemModulationACMBmax_Object = MibScalar
integraEmodemModulationACMBmax = _IntegraEmodemModulationACMBmax_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 3, 27),
    _IntegraEmodemModulationACMBmax_Type()
)
integraEmodemModulationACMBmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEmodemModulationACMBmax.setStatus("current")
_IntegraEsystem_ObjectIdentity = ObjectIdentity
integraEsystem = _IntegraEsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4)
)
_IntegraEsysCPUtemperature_Type = FixedDiv10
_IntegraEsysCPUtemperature_Object = MibScalar
integraEsysCPUtemperature = _IntegraEsysCPUtemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 2),
    _IntegraEsysCPUtemperature_Type()
)
integraEsysCPUtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysCPUtemperature.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysCPUtemperature.setUnits("C")
_IntegraEsysLicenseExpire_Type = Gauge32
_IntegraEsysLicenseExpire_Object = MibScalar
integraEsysLicenseExpire = _IntegraEsysLicenseExpire_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 3),
    _IntegraEsysLicenseExpire_Type()
)
integraEsysLicenseExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysLicenseExpire.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysLicenseExpire.setUnits("s")


class _IntegraEsysLicenseGenStatus_Type(Integer32):
    """Custom type integraEsysLicenseGenStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("expired", 2),
          ("unknown", 3),
          ("unlimitedTime", 4))
    )


_IntegraEsysLicenseGenStatus_Type.__name__ = "Integer32"
_IntegraEsysLicenseGenStatus_Object = MibScalar
integraEsysLicenseGenStatus = _IntegraEsysLicenseGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 4),
    _IntegraEsysLicenseGenStatus_Type()
)
integraEsysLicenseGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysLicenseGenStatus.setStatus("current")
_IntegraEsysPSUvoltage_Type = Integer32
_IntegraEsysPSUvoltage_Object = MibScalar
integraEsysPSUvoltage = _IntegraEsysPSUvoltage_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 5),
    _IntegraEsysPSUvoltage_Type()
)
integraEsysPSUvoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysPSUvoltage.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysPSUvoltage.setUnits("mV")
_IntegraEsysPSUcurrent_Type = Integer32
_IntegraEsysPSUcurrent_Object = MibScalar
integraEsysPSUcurrent = _IntegraEsysPSUcurrent_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 6),
    _IntegraEsysPSUcurrent_Type()
)
integraEsysPSUcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysPSUcurrent.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysPSUcurrent.setUnits("mA")
_IntegraEsysPSUpower_Type = Integer32
_IntegraEsysPSUpower_Object = MibScalar
integraEsysPSUpower = _IntegraEsysPSUpower_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 7),
    _IntegraEsysPSUpower_Type()
)
integraEsysPSUpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysPSUpower.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysPSUpower.setUnits("mW")
_IntegraEsysBoardTemperature_Type = FixedDiv10
_IntegraEsysBoardTemperature_Object = MibScalar
integraEsysBoardTemperature = _IntegraEsysBoardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 8),
    _IntegraEsysBoardTemperature_Type()
)
integraEsysBoardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysBoardTemperature.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysBoardTemperature.setUnits("C")
_IntegraEsysFreeMemory_Type = FixedDiv10
_IntegraEsysFreeMemory_Object = MibScalar
integraEsysFreeMemory = _IntegraEsysFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 9),
    _IntegraEsysFreeMemory_Type()
)
integraEsysFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysFreeMemory.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysFreeMemory.setUnits("%")
_IntegraEsysCPUidle_Type = FixedDiv10
_IntegraEsysCPUidle_Object = MibScalar
integraEsysCPUidle = _IntegraEsysCPUidle_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 10),
    _IntegraEsysCPUidle_Type()
)
integraEsysCPUidle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysCPUidle.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysCPUidle.setUnits("%")
_IntegraEsysDeviceType_Type = DisplayString
_IntegraEsysDeviceType_Object = MibScalar
integraEsysDeviceType = _IntegraEsysDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 11),
    _IntegraEsysDeviceType_Type()
)
integraEsysDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysDeviceType.setStatus("current")
_IntegraEsysDeviceSerial_Type = DisplayString
_IntegraEsysDeviceSerial_Object = MibScalar
integraEsysDeviceSerial = _IntegraEsysDeviceSerial_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 12),
    _IntegraEsysDeviceSerial_Type()
)
integraEsysDeviceSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysDeviceSerial.setStatus("current")
_IntegraEsysDeviceProductModel_Type = DisplayString
_IntegraEsysDeviceProductModel_Object = MibScalar
integraEsysDeviceProductModel = _IntegraEsysDeviceProductModel_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 13),
    _IntegraEsysDeviceProductModel_Type()
)
integraEsysDeviceProductModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysDeviceProductModel.setStatus("current")


class _IntegraEsysFanError_Type(Bits):
    """Custom type integraEsysFanError based on Bits"""
    namedValues = NamedValues(
        *(("no", 0),
          ("fan1", 1),
          ("unknown", 3))
    )

_IntegraEsysFanError_Type.__name__ = "Bits"
_IntegraEsysFanError_Object = MibScalar
integraEsysFanError = _IntegraEsysFanError_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 14),
    _IntegraEsysFanError_Type()
)
integraEsysFanError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysFanError.setStatus("current")
_IntegraEsysXADCtemperature_Type = FixedDiv10
_IntegraEsysXADCtemperature_Object = MibScalar
integraEsysXADCtemperature = _IntegraEsysXADCtemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 15),
    _IntegraEsysXADCtemperature_Type()
)
integraEsysXADCtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysXADCtemperature.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysXADCtemperature.setUnits("C")
_IntegraEsysVCCint_Type = FixedDiv20
_IntegraEsysVCCint_Object = MibScalar
integraEsysVCCint = _IntegraEsysVCCint_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 16),
    _IntegraEsysVCCint_Type()
)
integraEsysVCCint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysVCCint.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysVCCint.setUnits("V")
_IntegraEsysVCCaux_Type = FixedDiv20
_IntegraEsysVCCaux_Object = MibScalar
integraEsysVCCaux = _IntegraEsysVCCaux_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 17),
    _IntegraEsysVCCaux_Type()
)
integraEsysVCCaux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysVCCaux.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysVCCaux.setUnits("V")
_IntegraEsysVCCbram_Type = FixedDiv20
_IntegraEsysVCCbram_Object = MibScalar
integraEsysVCCbram = _IntegraEsysVCCbram_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 18),
    _IntegraEsysVCCbram_Type()
)
integraEsysVCCbram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysVCCbram.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysVCCbram.setUnits("V")
_IntegraEsysVCCpint_Type = FixedDiv20
_IntegraEsysVCCpint_Object = MibScalar
integraEsysVCCpint = _IntegraEsysVCCpint_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 19),
    _IntegraEsysVCCpint_Type()
)
integraEsysVCCpint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysVCCpint.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysVCCpint.setUnits("V")
_IntegraEsysVCCpaux_Type = FixedDiv20
_IntegraEsysVCCpaux_Object = MibScalar
integraEsysVCCpaux = _IntegraEsysVCCpaux_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 20),
    _IntegraEsysVCCpaux_Type()
)
integraEsysVCCpaux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysVCCpaux.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysVCCpaux.setUnits("V")
_IntegraEsysVCCoddr_Type = FixedDiv20
_IntegraEsysVCCoddr_Object = MibScalar
integraEsysVCCoddr = _IntegraEsysVCCoddr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 21),
    _IntegraEsysVCCoddr_Type()
)
integraEsysVCCoddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysVCCoddr.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysVCCoddr.setUnits("V")
_IntegraEsysXadc6v0AvddMdmAna_Type = FixedDiv20
_IntegraEsysXadc6v0AvddMdmAna_Object = MibScalar
integraEsysXadc6v0AvddMdmAna = _IntegraEsysXadc6v0AvddMdmAna_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 22),
    _IntegraEsysXadc6v0AvddMdmAna_Type()
)
integraEsysXadc6v0AvddMdmAna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysXadc6v0AvddMdmAna.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysXadc6v0AvddMdmAna.setUnits("V")
_IntegraEsysXadc1v0AvddSwAna_Type = FixedDiv20
_IntegraEsysXadc1v0AvddSwAna_Object = MibScalar
integraEsysXadc1v0AvddSwAna = _IntegraEsysXadc1v0AvddSwAna_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 23),
    _IntegraEsysXadc1v0AvddSwAna_Type()
)
integraEsysXadc1v0AvddSwAna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysXadc1v0AvddSwAna.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysXadc1v0AvddSwAna.setUnits("V")
_IntegraEsysXadc1v0AvddMdmAna_Type = FixedDiv20
_IntegraEsysXadc1v0AvddMdmAna_Object = MibScalar
integraEsysXadc1v0AvddMdmAna = _IntegraEsysXadc1v0AvddMdmAna_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 24),
    _IntegraEsysXadc1v0AvddMdmAna_Type()
)
integraEsysXadc1v0AvddMdmAna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysXadc1v0AvddMdmAna.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysXadc1v0AvddMdmAna.setUnits("V")
_IntegraEsysXadc1v0DvddMdmDig_Type = FixedDiv20
_IntegraEsysXadc1v0DvddMdmDig_Object = MibScalar
integraEsysXadc1v0DvddMdmDig = _IntegraEsysXadc1v0DvddMdmDig_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 25),
    _IntegraEsysXadc1v0DvddMdmDig_Type()
)
integraEsysXadc1v0DvddMdmDig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysXadc1v0DvddMdmDig.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysXadc1v0DvddMdmDig.setUnits("V")
_IntegraEsysXadc1v0CoreMdmDig_Type = FixedDiv20
_IntegraEsysXadc1v0CoreMdmDig_Object = MibScalar
integraEsysXadc1v0CoreMdmDig = _IntegraEsysXadc1v0CoreMdmDig_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 26),
    _IntegraEsysXadc1v0CoreMdmDig_Type()
)
integraEsysXadc1v0CoreMdmDig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysXadc1v0CoreMdmDig.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysXadc1v0CoreMdmDig.setUnits("V")
_IntegraEsysXadc2v5EnvAdcAvddMdmAna_Type = FixedDiv20
_IntegraEsysXadc2v5EnvAdcAvddMdmAna_Object = MibScalar
integraEsysXadc2v5EnvAdcAvddMdmAna = _IntegraEsysXadc2v5EnvAdcAvddMdmAna_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 27),
    _IntegraEsysXadc2v5EnvAdcAvddMdmAna_Type()
)
integraEsysXadc2v5EnvAdcAvddMdmAna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysXadc2v5EnvAdcAvddMdmAna.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysXadc2v5EnvAdcAvddMdmAna.setUnits("V")
_IntegraEsysXadc1v0CoreSwDig_Type = FixedDiv20
_IntegraEsysXadc1v0CoreSwDig_Object = MibScalar
integraEsysXadc1v0CoreSwDig = _IntegraEsysXadc1v0CoreSwDig_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 28),
    _IntegraEsysXadc1v0CoreSwDig_Type()
)
integraEsysXadc1v0CoreSwDig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysXadc1v0CoreSwDig.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysXadc1v0CoreSwDig.setUnits("V")
_IntegraEsysXadc5v0IqAvddMdmAna_Type = FixedDiv20
_IntegraEsysXadc5v0IqAvddMdmAna_Object = MibScalar
integraEsysXadc5v0IqAvddMdmAna = _IntegraEsysXadc5v0IqAvddMdmAna_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 29),
    _IntegraEsysXadc5v0IqAvddMdmAna_Type()
)
integraEsysXadc5v0IqAvddMdmAna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysXadc5v0IqAvddMdmAna.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysXadc5v0IqAvddMdmAna.setUnits("V")
_IntegraEsysXadc2v5WbDacClAvddMdmAna_Type = FixedDiv20
_IntegraEsysXadc2v5WbDacClAvddMdmAna_Object = MibScalar
integraEsysXadc2v5WbDacClAvddMdmAna = _IntegraEsysXadc2v5WbDacClAvddMdmAna_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 30),
    _IntegraEsysXadc2v5WbDacClAvddMdmAna_Type()
)
integraEsysXadc2v5WbDacClAvddMdmAna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysXadc2v5WbDacClAvddMdmAna.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysXadc2v5WbDacClAvddMdmAna.setUnits("V")
_IntegraEsysXadc1v2VccPhyDig_Type = FixedDiv20
_IntegraEsysXadc1v2VccPhyDig_Object = MibScalar
integraEsysXadc1v2VccPhyDig = _IntegraEsysXadc1v2VccPhyDig_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 31),
    _IntegraEsysXadc1v2VccPhyDig_Type()
)
integraEsysXadc1v2VccPhyDig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysXadc1v2VccPhyDig.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysXadc1v2VccPhyDig.setUnits("V")
_IntegraEsysXadc4v6AfeDacAvddMdmAna_Type = FixedDiv20
_IntegraEsysXadc4v6AfeDacAvddMdmAna_Object = MibScalar
integraEsysXadc4v6AfeDacAvddMdmAna = _IntegraEsysXadc4v6AfeDacAvddMdmAna_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 32),
    _IntegraEsysXadc4v6AfeDacAvddMdmAna_Type()
)
integraEsysXadc4v6AfeDacAvddMdmAna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysXadc4v6AfeDacAvddMdmAna.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysXadc4v6AfeDacAvddMdmAna.setUnits("V")
_IntegraEsysXadc2v5WbDacAvddMdmAna_Type = FixedDiv20
_IntegraEsysXadc2v5WbDacAvddMdmAna_Object = MibScalar
integraEsysXadc2v5WbDacAvddMdmAna = _IntegraEsysXadc2v5WbDacAvddMdmAna_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 33),
    _IntegraEsysXadc2v5WbDacAvddMdmAna_Type()
)
integraEsysXadc2v5WbDacAvddMdmAna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysXadc2v5WbDacAvddMdmAna.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysXadc2v5WbDacAvddMdmAna.setUnits("V")
_IntegraEsysXadc2v5VccSysDig_Type = FixedDiv20
_IntegraEsysXadc2v5VccSysDig_Object = MibScalar
integraEsysXadc2v5VccSysDig = _IntegraEsysXadc2v5VccSysDig_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 34),
    _IntegraEsysXadc2v5VccSysDig_Type()
)
integraEsysXadc2v5VccSysDig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysXadc2v5VccSysDig.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysXadc2v5VccSysDig.setUnits("V")
_IntegraEsysXadc3v3VccSysDig_Type = FixedDiv20
_IntegraEsysXadc3v3VccSysDig_Object = MibScalar
integraEsysXadc3v3VccSysDig = _IntegraEsysXadc3v3VccSysDig_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 35),
    _IntegraEsysXadc3v3VccSysDig_Type()
)
integraEsysXadc3v3VccSysDig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysXadc3v3VccSysDig.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysXadc3v3VccSysDig.setUnits("V")
_IntegraEsysXadc1v5Ddr3Sw_Type = FixedDiv20
_IntegraEsysXadc1v5Ddr3Sw_Object = MibScalar
integraEsysXadc1v5Ddr3Sw = _IntegraEsysXadc1v5Ddr3Sw_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 36),
    _IntegraEsysXadc1v5Ddr3Sw_Type()
)
integraEsysXadc1v5Ddr3Sw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysXadc1v5Ddr3Sw.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysXadc1v5Ddr3Sw.setUnits("V")
_IntegraEsysXadc2v5WbAdcAvddMdmAna_Type = FixedDiv20
_IntegraEsysXadc2v5WbAdcAvddMdmAna_Object = MibScalar
integraEsysXadc2v5WbAdcAvddMdmAna = _IntegraEsysXadc2v5WbAdcAvddMdmAna_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 37),
    _IntegraEsysXadc2v5WbAdcAvddMdmAna_Type()
)
integraEsysXadc2v5WbAdcAvddMdmAna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysXadc2v5WbAdcAvddMdmAna.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysXadc2v5WbAdcAvddMdmAna.setUnits("V")
_IntegraEsysXadc2v5WbDacPllAvddMdmAna_Type = FixedDiv20
_IntegraEsysXadc2v5WbDacPllAvddMdmAna_Object = MibScalar
integraEsysXadc2v5WbDacPllAvddMdmAna = _IntegraEsysXadc2v5WbDacPllAvddMdmAna_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 4, 38),
    _IntegraEsysXadc2v5WbDacPllAvddMdmAna_Type()
)
integraEsysXadc2v5WbDacPllAvddMdmAna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEsysXadc2v5WbDacPllAvddMdmAna.setStatus("current")
if mibBuilder.loadTexts:
    integraEsysXadc2v5WbDacPllAvddMdmAna.setUnits("V")
_IntegraEethernet_ObjectIdentity = ObjectIdentity
integraEethernet = _IntegraEethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5)
)
_IntegraEifStatusTable_Object = MibTable
integraEifStatusTable = _IntegraEifStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 1)
)
if mibBuilder.loadTexts:
    integraEifStatusTable.setStatus("current")
_IntegraEifPortEntry_Object = MibTableRow
integraEifPortEntry = _IntegraEifPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 1, 1)
)
integraEifPortEntry.setIndexNames(
    (0, "SAF-INTEGRAE-MIB", "integraEifPortStatIndex"),
)
if mibBuilder.loadTexts:
    integraEifPortEntry.setStatus("current")


class _IntegraEifPortStatIndex_Type(Integer32):
    """Custom type integraEifPortStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IntegraEifPortStatIndex_Type.__name__ = "Integer32"
_IntegraEifPortStatIndex_Object = MibTableColumn
integraEifPortStatIndex = _IntegraEifPortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 1, 1, 1),
    _IntegraEifPortStatIndex_Type()
)
integraEifPortStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifPortStatIndex.setStatus("current")


class _IntegraEifPortStatDescr_Type(DisplayString):
    """Custom type integraEifPortStatDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntegraEifPortStatDescr_Type.__name__ = "DisplayString"
_IntegraEifPortStatDescr_Object = MibTableColumn
integraEifPortStatDescr = _IntegraEifPortStatDescr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 1, 1, 2),
    _IntegraEifPortStatDescr_Type()
)
integraEifPortStatDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifPortStatDescr.setStatus("current")
_IntegraEifPortType_Type = IANAifType
_IntegraEifPortType_Object = MibTableColumn
integraEifPortType = _IntegraEifPortType_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 1, 1, 3),
    _IntegraEifPortType_Type()
)
integraEifPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifPortType.setStatus("current")
_IntegraEifPortMtu_Type = Integer32
_IntegraEifPortMtu_Object = MibTableColumn
integraEifPortMtu = _IntegraEifPortMtu_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 1, 1, 4),
    _IntegraEifPortMtu_Type()
)
integraEifPortMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifPortMtu.setStatus("current")
if mibBuilder.loadTexts:
    integraEifPortMtu.setUnits("B")
_IntegraEifPortHighSpeed_Type = Gauge32
_IntegraEifPortHighSpeed_Object = MibTableColumn
integraEifPortHighSpeed = _IntegraEifPortHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 1, 1, 5),
    _IntegraEifPortHighSpeed_Type()
)
integraEifPortHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifPortHighSpeed.setStatus("current")
if mibBuilder.loadTexts:
    integraEifPortHighSpeed.setUnits("Mbps")
_IntegraEifPortPhysAddress_Type = PhysAddress
_IntegraEifPortPhysAddress_Object = MibTableColumn
integraEifPortPhysAddress = _IntegraEifPortPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 1, 1, 6),
    _IntegraEifPortPhysAddress_Type()
)
integraEifPortPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifPortPhysAddress.setStatus("current")


class _IntegraEifPortAdminStatus_Type(Integer32):
    """Custom type integraEifPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("unknown", 3))
    )


_IntegraEifPortAdminStatus_Type.__name__ = "Integer32"
_IntegraEifPortAdminStatus_Object = MibTableColumn
integraEifPortAdminStatus = _IntegraEifPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 1, 1, 7),
    _IntegraEifPortAdminStatus_Type()
)
integraEifPortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifPortAdminStatus.setStatus("current")


class _IntegraEifPortOperStatus_Type(Integer32):
    """Custom type integraEifPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_IntegraEifPortOperStatus_Type.__name__ = "Integer32"
_IntegraEifPortOperStatus_Object = MibTableColumn
integraEifPortOperStatus = _IntegraEifPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 1, 1, 8),
    _IntegraEifPortOperStatus_Type()
)
integraEifPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifPortOperStatus.setStatus("current")
_IntegraEifPortLastChange_Type = TimeTicks
_IntegraEifPortLastChange_Object = MibTableColumn
integraEifPortLastChange = _IntegraEifPortLastChange_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 1, 1, 9),
    _IntegraEifPortLastChange_Type()
)
integraEifPortLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifPortLastChange.setStatus("current")


class _IntegraEifPortAutoneg_Type(Integer32):
    """Custom type integraEifPortAutoneg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("unknown", 3))
    )


_IntegraEifPortAutoneg_Type.__name__ = "Integer32"
_IntegraEifPortAutoneg_Object = MibTableColumn
integraEifPortAutoneg = _IntegraEifPortAutoneg_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 1, 1, 10),
    _IntegraEifPortAutoneg_Type()
)
integraEifPortAutoneg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifPortAutoneg.setStatus("current")


class _IntegraEifPortDuplex_Type(Integer32):
    """Custom type integraEifPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("unknown", 3))
    )


_IntegraEifPortDuplex_Type.__name__ = "Integer32"
_IntegraEifPortDuplex_Object = MibTableColumn
integraEifPortDuplex = _IntegraEifPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 1, 1, 11),
    _IntegraEifPortDuplex_Type()
)
integraEifPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifPortDuplex.setStatus("current")


class _IntegraEifPortSyncEthActive_Type(Integer32):
    """Custom type integraEifPortSyncEthActive based on Integer32"""
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


_IntegraEifPortSyncEthActive_Type.__name__ = "Integer32"
_IntegraEifPortSyncEthActive_Object = MibTableColumn
integraEifPortSyncEthActive = _IntegraEifPortSyncEthActive_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 1, 1, 12),
    _IntegraEifPortSyncEthActive_Type()
)
integraEifPortSyncEthActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifPortSyncEthActive.setStatus("current")
_IntegraEifPortSyncEthPrio_Type = Integer32
_IntegraEifPortSyncEthPrio_Object = MibTableColumn
integraEifPortSyncEthPrio = _IntegraEifPortSyncEthPrio_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 1, 1, 13),
    _IntegraEifPortSyncEthPrio_Type()
)
integraEifPortSyncEthPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifPortSyncEthPrio.setStatus("current")


class _IntegraEifPortFlowControl_Type(Integer32):
    """Custom type integraEifPortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("unknown", 3))
    )


_IntegraEifPortFlowControl_Type.__name__ = "Integer32"
_IntegraEifPortFlowControl_Object = MibTableColumn
integraEifPortFlowControl = _IntegraEifPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 1, 1, 14),
    _IntegraEifPortFlowControl_Type()
)
integraEifPortFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifPortFlowControl.setStatus("current")
_IntegraEifStatisticsTable_Object = MibTable
integraEifStatisticsTable = _IntegraEifStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2)
)
if mibBuilder.loadTexts:
    integraEifStatisticsTable.setStatus("current")
_IntegraEifPortStcEntry_Object = MibTableRow
integraEifPortStcEntry = _IntegraEifPortStcEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1)
)
integraEifPortStcEntry.setIndexNames(
    (0, "SAF-INTEGRAE-MIB", "integraEifPortStcIndex"),
)
if mibBuilder.loadTexts:
    integraEifPortStcEntry.setStatus("current")


class _IntegraEifPortStcIndex_Type(Integer32):
    """Custom type integraEifPortStcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IntegraEifPortStcIndex_Type.__name__ = "Integer32"
_IntegraEifPortStcIndex_Object = MibTableColumn
integraEifPortStcIndex = _IntegraEifPortStcIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 1),
    _IntegraEifPortStcIndex_Type()
)
integraEifPortStcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifPortStcIndex.setStatus("current")


class _IntegraEifPortStcDescr_Type(DisplayString):
    """Custom type integraEifPortStcDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntegraEifPortStcDescr_Type.__name__ = "DisplayString"
_IntegraEifPortStcDescr_Object = MibTableColumn
integraEifPortStcDescr = _IntegraEifPortStcDescr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 2),
    _IntegraEifPortStcDescr_Type()
)
integraEifPortStcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifPortStcDescr.setStatus("current")
_IntegraEifTimePassed_Type = TimeTicks
_IntegraEifTimePassed_Object = MibTableColumn
integraEifTimePassed = _IntegraEifTimePassed_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 3),
    _IntegraEifTimePassed_Type()
)
integraEifTimePassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifTimePassed.setStatus("current")
if mibBuilder.loadTexts:
    integraEifTimePassed.setUnits("s/100")
_IntegraEifIngressPackets_Type = Counter64
_IntegraEifIngressPackets_Object = MibTableColumn
integraEifIngressPackets = _IntegraEifIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 4),
    _IntegraEifIngressPackets_Type()
)
integraEifIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifIngressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifIngressPackets.setUnits("packet")
_IntegraEifIngressBytes_Type = Counter64
_IntegraEifIngressBytes_Object = MibTableColumn
integraEifIngressBytes = _IntegraEifIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 5),
    _IntegraEifIngressBytes_Type()
)
integraEifIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifIngressBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraEifIngressBytes.setUnits("B")
_IntegraEifEgressPackets_Type = Counter64
_IntegraEifEgressPackets_Object = MibTableColumn
integraEifEgressPackets = _IntegraEifEgressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 6),
    _IntegraEifEgressPackets_Type()
)
integraEifEgressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEgressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEgressPackets.setUnits("packet")
_IntegraEifEgressBytes_Type = Counter64
_IntegraEifEgressBytes_Object = MibTableColumn
integraEifEgressBytes = _IntegraEifEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 7),
    _IntegraEifEgressBytes_Type()
)
integraEifEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEgressBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEgressBytes.setUnits("B")
_IntegraEifEtherStatsMulticastPkts_Type = Counter64
_IntegraEifEtherStatsMulticastPkts_Object = MibTableColumn
integraEifEtherStatsMulticastPkts = _IntegraEifEtherStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 8),
    _IntegraEifEtherStatsMulticastPkts_Type()
)
integraEifEtherStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherStatsMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherStatsMulticastPkts.setUnits("packet")
_IntegraEifEtherStatsBroadcastPkts_Type = Counter64
_IntegraEifEtherStatsBroadcastPkts_Object = MibTableColumn
integraEifEtherStatsBroadcastPkts = _IntegraEifEtherStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 9),
    _IntegraEifEtherStatsBroadcastPkts_Type()
)
integraEifEtherStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherStatsBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherStatsBroadcastPkts.setUnits("packet")
_IntegraEifEtherStatsPkts64Octets_Type = Counter64
_IntegraEifEtherStatsPkts64Octets_Object = MibTableColumn
integraEifEtherStatsPkts64Octets = _IntegraEifEtherStatsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 10),
    _IntegraEifEtherStatsPkts64Octets_Type()
)
integraEifEtherStatsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherStatsPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherStatsPkts64Octets.setUnits("packet")
_IntegraEifEtherStatsPkts65to127Octets_Type = Counter64
_IntegraEifEtherStatsPkts65to127Octets_Object = MibTableColumn
integraEifEtherStatsPkts65to127Octets = _IntegraEifEtherStatsPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 11),
    _IntegraEifEtherStatsPkts65to127Octets_Type()
)
integraEifEtherStatsPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherStatsPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherStatsPkts65to127Octets.setUnits("packet")
_IntegraEifEtherStatsPkts128to255Octets_Type = Counter64
_IntegraEifEtherStatsPkts128to255Octets_Object = MibTableColumn
integraEifEtherStatsPkts128to255Octets = _IntegraEifEtherStatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 12),
    _IntegraEifEtherStatsPkts128to255Octets_Type()
)
integraEifEtherStatsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherStatsPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherStatsPkts128to255Octets.setUnits("packet")
_IntegraEifEtherStatsPkts256to511Octets_Type = Counter64
_IntegraEifEtherStatsPkts256to511Octets_Object = MibTableColumn
integraEifEtherStatsPkts256to511Octets = _IntegraEifEtherStatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 13),
    _IntegraEifEtherStatsPkts256to511Octets_Type()
)
integraEifEtherStatsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherStatsPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherStatsPkts256to511Octets.setUnits("packet")
_IntegraEifEtherStatsPkts512to1023Octets_Type = Counter64
_IntegraEifEtherStatsPkts512to1023Octets_Object = MibTableColumn
integraEifEtherStatsPkts512to1023Octets = _IntegraEifEtherStatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 14),
    _IntegraEifEtherStatsPkts512to1023Octets_Type()
)
integraEifEtherStatsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherStatsPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherStatsPkts512to1023Octets.setUnits("packet")
_IntegraEifEtherStatsPkts1024to1518Octets_Type = Counter64
_IntegraEifEtherStatsPkts1024to1518Octets_Object = MibTableColumn
integraEifEtherStatsPkts1024to1518Octets = _IntegraEifEtherStatsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 15),
    _IntegraEifEtherStatsPkts1024to1518Octets_Type()
)
integraEifEtherStatsPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherStatsPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherStatsPkts1024to1518Octets.setUnits("packet")
_IntegraEifEtherStatsOversizePkts_Type = Counter64
_IntegraEifEtherStatsOversizePkts_Object = MibTableColumn
integraEifEtherStatsOversizePkts = _IntegraEifEtherStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 16),
    _IntegraEifEtherStatsOversizePkts_Type()
)
integraEifEtherStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherStatsOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherStatsOversizePkts.setUnits("packet")
_IntegraEifEtherRxOversizePkts_Type = Counter64
_IntegraEifEtherRxOversizePkts_Object = MibTableColumn
integraEifEtherRxOversizePkts = _IntegraEifEtherRxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 17),
    _IntegraEifEtherRxOversizePkts_Type()
)
integraEifEtherRxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherRxOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherRxOversizePkts.setUnits("packet")
_IntegraEifEtherTxOversizePkts_Type = Counter64
_IntegraEifEtherTxOversizePkts_Object = MibTableColumn
integraEifEtherTxOversizePkts = _IntegraEifEtherTxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 18),
    _IntegraEifEtherTxOversizePkts_Type()
)
integraEifEtherTxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherTxOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherTxOversizePkts.setUnits("packet")
_IntegraEifEtherStatsOctets_Type = Counter64
_IntegraEifEtherStatsOctets_Object = MibTableColumn
integraEifEtherStatsOctets = _IntegraEifEtherStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 19),
    _IntegraEifEtherStatsOctets_Type()
)
integraEifEtherStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherStatsOctets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherStatsOctets.setUnits("packet")
_IntegraEifEtherStatsPkts_Type = Counter64
_IntegraEifEtherStatsPkts_Object = MibTableColumn
integraEifEtherStatsPkts = _IntegraEifEtherStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 20),
    _IntegraEifEtherStatsPkts_Type()
)
integraEifEtherStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherStatsPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherStatsPkts.setUnits("packet")
_IntegraEifEtherStatsTXNoErrors_Type = Counter64
_IntegraEifEtherStatsTXNoErrors_Object = MibTableColumn
integraEifEtherStatsTXNoErrors = _IntegraEifEtherStatsTXNoErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 21),
    _IntegraEifEtherStatsTXNoErrors_Type()
)
integraEifEtherStatsTXNoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherStatsTXNoErrors.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherStatsTXNoErrors.setUnits("packet")
_IntegraEifEtherStatsRXNoErrors_Type = Counter64
_IntegraEifEtherStatsRXNoErrors_Object = MibTableColumn
integraEifEtherStatsRXNoErrors = _IntegraEifEtherStatsRXNoErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 22),
    _IntegraEifEtherStatsRXNoErrors_Type()
)
integraEifEtherStatsRXNoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherStatsRXNoErrors.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherStatsRXNoErrors.setUnits("packet")
_IntegraEifEtherStatsPkts1519to1522Octets_Type = Counter64
_IntegraEifEtherStatsPkts1519to1522Octets_Object = MibTableColumn
integraEifEtherStatsPkts1519to1522Octets = _IntegraEifEtherStatsPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 23),
    _IntegraEifEtherStatsPkts1519to1522Octets_Type()
)
integraEifEtherStatsPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherStatsPkts1519to1522Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherStatsPkts1519to1522Octets.setUnits("packet")
_IntegraEifIfInOctets_Type = Counter64
_IntegraEifIfInOctets_Object = MibTableColumn
integraEifIfInOctets = _IntegraEifIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 24),
    _IntegraEifIfInOctets_Type()
)
integraEifIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifIfInOctets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifIfInOctets.setUnits("octet")
_IntegraEifIfOutOctets_Type = Counter64
_IntegraEifIfOutOctets_Object = MibTableColumn
integraEifIfOutOctets = _IntegraEifIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 25),
    _IntegraEifIfOutOctets_Type()
)
integraEifIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifIfOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifIfOutOctets.setUnits("octet")
_IntegraEifDot1dTpPortInFrames_Type = Counter64
_IntegraEifDot1dTpPortInFrames_Object = MibTableColumn
integraEifDot1dTpPortInFrames = _IntegraEifDot1dTpPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 26),
    _IntegraEifDot1dTpPortInFrames_Type()
)
integraEifDot1dTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifDot1dTpPortInFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraEifDot1dTpPortInFrames.setUnits("frame")
_IntegraEifDot1dTpPortOutFrames_Type = Counter64
_IntegraEifDot1dTpPortOutFrames_Object = MibTableColumn
integraEifDot1dTpPortOutFrames = _IntegraEifDot1dTpPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 27),
    _IntegraEifDot1dTpPortOutFrames_Type()
)
integraEifDot1dTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifDot1dTpPortOutFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraEifDot1dTpPortOutFrames.setUnits("frame")
_IntegraEifReceivedPkts64Octets_Type = Counter64
_IntegraEifReceivedPkts64Octets_Object = MibTableColumn
integraEifReceivedPkts64Octets = _IntegraEifReceivedPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 28),
    _IntegraEifReceivedPkts64Octets_Type()
)
integraEifReceivedPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifReceivedPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifReceivedPkts64Octets.setUnits("packet")
_IntegraEifTransmittedPkts64Octets_Type = Counter64
_IntegraEifTransmittedPkts64Octets_Object = MibTableColumn
integraEifTransmittedPkts64Octets = _IntegraEifTransmittedPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 29),
    _IntegraEifTransmittedPkts64Octets_Type()
)
integraEifTransmittedPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifTransmittedPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifTransmittedPkts64Octets.setUnits("packet")
_IntegraEifReceivedPkts65to127Octets_Type = Counter64
_IntegraEifReceivedPkts65to127Octets_Object = MibTableColumn
integraEifReceivedPkts65to127Octets = _IntegraEifReceivedPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 30),
    _IntegraEifReceivedPkts65to127Octets_Type()
)
integraEifReceivedPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifReceivedPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifReceivedPkts65to127Octets.setUnits("packet")
_IntegraEifTransmittedPkts65to127Octets_Type = Counter64
_IntegraEifTransmittedPkts65to127Octets_Object = MibTableColumn
integraEifTransmittedPkts65to127Octets = _IntegraEifTransmittedPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 31),
    _IntegraEifTransmittedPkts65to127Octets_Type()
)
integraEifTransmittedPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifTransmittedPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifTransmittedPkts65to127Octets.setUnits("packet")
_IntegraEifReceivedPkts128to255Octets_Type = Counter64
_IntegraEifReceivedPkts128to255Octets_Object = MibTableColumn
integraEifReceivedPkts128to255Octets = _IntegraEifReceivedPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 32),
    _IntegraEifReceivedPkts128to255Octets_Type()
)
integraEifReceivedPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifReceivedPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifReceivedPkts128to255Octets.setUnits("packet")
_IntegraEifTransmittedPkts128to255Octets_Type = Counter64
_IntegraEifTransmittedPkts128to255Octets_Object = MibTableColumn
integraEifTransmittedPkts128to255Octets = _IntegraEifTransmittedPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 33),
    _IntegraEifTransmittedPkts128to255Octets_Type()
)
integraEifTransmittedPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifTransmittedPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifTransmittedPkts128to255Octets.setUnits("packet")
_IntegraEifReceivedPkts256to511Octets_Type = Counter64
_IntegraEifReceivedPkts256to511Octets_Object = MibTableColumn
integraEifReceivedPkts256to511Octets = _IntegraEifReceivedPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 34),
    _IntegraEifReceivedPkts256to511Octets_Type()
)
integraEifReceivedPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifReceivedPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifReceivedPkts256to511Octets.setUnits("packet")
_IntegraEifTransmittedPkts256to511Octets_Type = Counter64
_IntegraEifTransmittedPkts256to511Octets_Object = MibTableColumn
integraEifTransmittedPkts256to511Octets = _IntegraEifTransmittedPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 35),
    _IntegraEifTransmittedPkts256to511Octets_Type()
)
integraEifTransmittedPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifTransmittedPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifTransmittedPkts256to511Octets.setUnits("packet")
_IntegraEifReceivedPkts512to1023Octets_Type = Counter64
_IntegraEifReceivedPkts512to1023Octets_Object = MibTableColumn
integraEifReceivedPkts512to1023Octets = _IntegraEifReceivedPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 36),
    _IntegraEifReceivedPkts512to1023Octets_Type()
)
integraEifReceivedPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifReceivedPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifReceivedPkts512to1023Octets.setUnits("packet")
_IntegraEifTransmittedPkts512to1023Octets_Type = Counter64
_IntegraEifTransmittedPkts512to1023Octets_Object = MibTableColumn
integraEifTransmittedPkts512to1023Octets = _IntegraEifTransmittedPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 37),
    _IntegraEifTransmittedPkts512to1023Octets_Type()
)
integraEifTransmittedPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifTransmittedPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifTransmittedPkts512to1023Octets.setUnits("packet")
_IntegraEifReceivedPkts1024to1518Octets_Type = Counter64
_IntegraEifReceivedPkts1024to1518Octets_Object = MibTableColumn
integraEifReceivedPkts1024to1518Octets = _IntegraEifReceivedPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 38),
    _IntegraEifReceivedPkts1024to1518Octets_Type()
)
integraEifReceivedPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifReceivedPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifReceivedPkts1024to1518Octets.setUnits("packet")
_IntegraEifTransmittedPkts1024to1518Octets_Type = Counter64
_IntegraEifTransmittedPkts1024to1518Octets_Object = MibTableColumn
integraEifTransmittedPkts1024to1518Octets = _IntegraEifTransmittedPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 39),
    _IntegraEifTransmittedPkts1024to1518Octets_Type()
)
integraEifTransmittedPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifTransmittedPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifTransmittedPkts1024to1518Octets.setUnits("packet")
_IntegraEifIfInBroadcastPkts_Type = Counter64
_IntegraEifIfInBroadcastPkts_Object = MibTableColumn
integraEifIfInBroadcastPkts = _IntegraEifIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 40),
    _IntegraEifIfInBroadcastPkts_Type()
)
integraEifIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifIfInBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraEifIfInBroadcastPkts.setUnits("packet")
_IntegraEifIfOutBroadcastPkts_Type = Counter64
_IntegraEifIfOutBroadcastPkts_Object = MibTableColumn
integraEifIfOutBroadcastPkts = _IntegraEifIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 41),
    _IntegraEifIfOutBroadcastPkts_Type()
)
integraEifIfOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifIfOutBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraEifIfOutBroadcastPkts.setUnits("packet")
_IntegraEifIfInMulticastPkts_Type = Counter64
_IntegraEifIfInMulticastPkts_Object = MibTableColumn
integraEifIfInMulticastPkts = _IntegraEifIfInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 42),
    _IntegraEifIfInMulticastPkts_Type()
)
integraEifIfInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifIfInMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraEifIfInMulticastPkts.setUnits("packet")
_IntegraEifIfOutMulticastPkts_Type = Counter64
_IntegraEifIfOutMulticastPkts_Object = MibTableColumn
integraEifIfOutMulticastPkts = _IntegraEifIfOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 43),
    _IntegraEifIfOutMulticastPkts_Type()
)
integraEifIfOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifIfOutMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraEifIfOutMulticastPkts.setUnits("packet")
_IntegraEifDot3InPauseFrames_Type = Counter64
_IntegraEifDot3InPauseFrames_Object = MibTableColumn
integraEifDot3InPauseFrames = _IntegraEifDot3InPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 44),
    _IntegraEifDot3InPauseFrames_Type()
)
integraEifDot3InPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifDot3InPauseFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraEifDot3InPauseFrames.setUnits("frame")
_IntegraEifDot3OutPauseFrames_Type = Counter64
_IntegraEifDot3OutPauseFrames_Object = MibTableColumn
integraEifDot3OutPauseFrames = _IntegraEifDot3OutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 45),
    _IntegraEifDot3OutPauseFrames_Type()
)
integraEifDot3OutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifDot3OutPauseFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraEifDot3OutPauseFrames.setUnits("frame")
_IntegraEifEtherStatsUndersizePkts_Type = Counter64
_IntegraEifEtherStatsUndersizePkts_Object = MibTableColumn
integraEifEtherStatsUndersizePkts = _IntegraEifEtherStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 46),
    _IntegraEifEtherStatsUndersizePkts_Type()
)
integraEifEtherStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherStatsUndersizePkts.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherStatsUndersizePkts.setUnits("packet")
_IntegraEifEtherStatsFragments_Type = Counter64
_IntegraEifEtherStatsFragments_Object = MibTableColumn
integraEifEtherStatsFragments = _IntegraEifEtherStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 47),
    _IntegraEifEtherStatsFragments_Type()
)
integraEifEtherStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherStatsFragments.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherStatsFragments.setUnits("packet")
_IntegraEifEtherStatsCRCAlignErrors_Type = Counter64
_IntegraEifEtherStatsCRCAlignErrors_Object = MibTableColumn
integraEifEtherStatsCRCAlignErrors = _IntegraEifEtherStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 48),
    _IntegraEifEtherStatsCRCAlignErrors_Type()
)
integraEifEtherStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherStatsCRCAlignErrors.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherStatsCRCAlignErrors.setUnits("packet")
_IntegraEifEtherStatsJabbers_Type = Counter64
_IntegraEifEtherStatsJabbers_Object = MibTableColumn
integraEifEtherStatsJabbers = _IntegraEifEtherStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 49),
    _IntegraEifEtherStatsJabbers_Type()
)
integraEifEtherStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEtherStatsJabbers.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEtherStatsJabbers.setUnits("packet")
_IntegraEifIngressBPS_Type = Integer32
_IntegraEifIngressBPS_Object = MibTableColumn
integraEifIngressBPS = _IntegraEifIngressBPS_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 50),
    _IntegraEifIngressBPS_Type()
)
integraEifIngressBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifIngressBPS.setStatus("current")
if mibBuilder.loadTexts:
    integraEifIngressBPS.setUnits("Bps")
_IntegraEifIngressPPS_Type = Integer32
_IntegraEifIngressPPS_Object = MibTableColumn
integraEifIngressPPS = _IntegraEifIngressPPS_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 51),
    _IntegraEifIngressPPS_Type()
)
integraEifIngressPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifIngressPPS.setStatus("current")
if mibBuilder.loadTexts:
    integraEifIngressPPS.setUnits("pps")
_IntegraEifEgressBPS_Type = Integer32
_IntegraEifEgressBPS_Object = MibTableColumn
integraEifEgressBPS = _IntegraEifEgressBPS_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 52),
    _IntegraEifEgressBPS_Type()
)
integraEifEgressBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEgressBPS.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEgressBPS.setUnits("Bps")
_IntegraEifEgressPPS_Type = Integer32
_IntegraEifEgressPPS_Object = MibTableColumn
integraEifEgressPPS = _IntegraEifEgressPPS_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 53),
    _IntegraEifEgressPPS_Type()
)
integraEifEgressPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifEgressPPS.setStatus("current")
if mibBuilder.loadTexts:
    integraEifEgressPPS.setUnits("pps")
_IntegraEifAllCoSQoutPackets_Type = Counter64
_IntegraEifAllCoSQoutPackets_Object = MibTableColumn
integraEifAllCoSQoutPackets = _IntegraEifAllCoSQoutPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 54),
    _IntegraEifAllCoSQoutPackets_Type()
)
integraEifAllCoSQoutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifAllCoSQoutPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifAllCoSQoutPackets.setUnits("packet")
_IntegraEifAllCoSQoutBytes_Type = Counter64
_IntegraEifAllCoSQoutBytes_Object = MibTableColumn
integraEifAllCoSQoutBytes = _IntegraEifAllCoSQoutBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 55),
    _IntegraEifAllCoSQoutBytes_Type()
)
integraEifAllCoSQoutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifAllCoSQoutBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraEifAllCoSQoutBytes.setUnits("B")
_IntegraEifAllCoSQdroppedPackets_Type = Counter64
_IntegraEifAllCoSQdroppedPackets_Object = MibTableColumn
integraEifAllCoSQdroppedPackets = _IntegraEifAllCoSQdroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 56),
    _IntegraEifAllCoSQdroppedPackets_Type()
)
integraEifAllCoSQdroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifAllCoSQdroppedPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifAllCoSQdroppedPackets.setUnits("packet")
_IntegraEifAllCoSQdroppedBytes_Type = Counter64
_IntegraEifAllCoSQdroppedBytes_Object = MibTableColumn
integraEifAllCoSQdroppedBytes = _IntegraEifAllCoSQdroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 57),
    _IntegraEifAllCoSQdroppedBytes_Type()
)
integraEifAllCoSQdroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifAllCoSQdroppedBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraEifAllCoSQdroppedBytes.setUnits("B")
_IntegraEifProcessedRxPackets_Type = Counter64
_IntegraEifProcessedRxPackets_Object = MibTableColumn
integraEifProcessedRxPackets = _IntegraEifProcessedRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 58),
    _IntegraEifProcessedRxPackets_Type()
)
integraEifProcessedRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifProcessedRxPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraEifProcessedRxPackets.setUnits("packet")
_IntegraEifProcessedRxBytes_Type = Counter64
_IntegraEifProcessedRxBytes_Object = MibTableColumn
integraEifProcessedRxBytes = _IntegraEifProcessedRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 2, 1, 59),
    _IntegraEifProcessedRxBytes_Type()
)
integraEifProcessedRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifProcessedRxBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraEifProcessedRxBytes.setUnits("B")


class _IntegraEifLspPortAdminState_Type(Integer32):
    """Custom type integraEifLspPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("lsp", 2),
          ("backup", 3),
          ("unknown", 4))
    )


_IntegraEifLspPortAdminState_Type.__name__ = "Integer32"
_IntegraEifLspPortAdminState_Object = MibScalar
integraEifLspPortAdminState = _IntegraEifLspPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 3),
    _IntegraEifLspPortAdminState_Type()
)
integraEifLspPortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifLspPortAdminState.setStatus("current")


class _IntegraEifLspPortList_Type(Bits):
    """Custom type integraEifLspPortList based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("lan1", 1),
          ("lan2", 2),
          ("lan3", 3))
    )

_IntegraEifLspPortList_Type.__name__ = "Bits"
_IntegraEifLspPortList_Object = MibScalar
integraEifLspPortList = _IntegraEifLspPortList_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 4),
    _IntegraEifLspPortList_Type()
)
integraEifLspPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifLspPortList.setStatus("current")


class _IntegraEifLspPortStatus_Type(Integer32):
    """Custom type integraEifLspPortStatus based on Integer32"""
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
        *(("lspPortOK", 1),
          ("lspPortDownBlockedByLSP", 2),
          ("backupNoLink", 3),
          ("backupLinkActive", 4),
          ("backupLinkReady", 5),
          ("unknown", 6))
    )


_IntegraEifLspPortStatus_Type.__name__ = "Integer32"
_IntegraEifLspPortStatus_Object = MibScalar
integraEifLspPortStatus = _IntegraEifLspPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 5, 5),
    _IntegraEifLspPortStatus_Type()
)
integraEifLspPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEifLspPortStatus.setStatus("current")


class _IntegraEexecuteConfig_Type(Integer32):
    """Custom type integraEexecuteConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_IntegraEexecuteConfig_Type.__name__ = "Integer32"
_IntegraEexecuteConfig_Object = MibScalar
integraEexecuteConfig = _IntegraEexecuteConfig_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 6),
    _IntegraEexecuteConfig_Type()
)
integraEexecuteConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraEexecuteConfig.setStatus("current")


class _IntegraEneedStore_Type(Integer32):
    """Custom type integraEneedStore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("no", 0)
    )


_IntegraEneedStore_Type.__name__ = "Integer32"
_IntegraEneedStore_Object = MibScalar
integraEneedStore = _IntegraEneedStore_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 7),
    _IntegraEneedStore_Type()
)
integraEneedStore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEneedStore.setStatus("current")


class _IntegraEstoreConfig_Type(Integer32):
    """Custom type integraEstoreConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("store", 1)
    )


_IntegraEstoreConfig_Type.__name__ = "Integer32"
_IntegraEstoreConfig_Object = MibScalar
integraEstoreConfig = _IntegraEstoreConfig_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 8),
    _IntegraEstoreConfig_Type()
)
integraEstoreConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraEstoreConfig.setStatus("current")
_IntegraEnetCfg_ObjectIdentity = ObjectIdentity
integraEnetCfg = _IntegraEnetCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 9)
)
_IntegraEnetCfgIPaddress_Type = DisplayString
_IntegraEnetCfgIPaddress_Object = MibScalar
integraEnetCfgIPaddress = _IntegraEnetCfgIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 9, 1),
    _IntegraEnetCfgIPaddress_Type()
)
integraEnetCfgIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraEnetCfgIPaddress.setStatus("current")
_IntegraEnetCfgIPmask_Type = DisplayString
_IntegraEnetCfgIPmask_Object = MibScalar
integraEnetCfgIPmask = _IntegraEnetCfgIPmask_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 9, 2),
    _IntegraEnetCfgIPmask_Type()
)
integraEnetCfgIPmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraEnetCfgIPmask.setStatus("current")
_IntegraEnetCfgIPgateway_Type = DisplayString
_IntegraEnetCfgIPgateway_Object = MibScalar
integraEnetCfgIPgateway = _IntegraEnetCfgIPgateway_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 9, 3),
    _IntegraEnetCfgIPgateway_Type()
)
integraEnetCfgIPgateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraEnetCfgIPgateway.setStatus("current")
_IntegraEnetCfgRemoteIPaddress_Type = DisplayString
_IntegraEnetCfgRemoteIPaddress_Object = MibScalar
integraEnetCfgRemoteIPaddress = _IntegraEnetCfgRemoteIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 9, 4),
    _IntegraEnetCfgRemoteIPaddress_Type()
)
integraEnetCfgRemoteIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraEnetCfgRemoteIPaddress.setStatus("current")
_IntegraEConformance_ObjectIdentity = ObjectIdentity
integraEConformance = _IntegraEConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 10)
)
_IntegraECompliances_ObjectIdentity = ObjectIdentity
integraECompliances = _IntegraECompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 10, 1)
)
_IntegraEGroups_ObjectIdentity = ObjectIdentity
integraEGroups = _IntegraEGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 10, 2)
)

# Managed Objects groups

integraEMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 10, 2, 1)
)
integraEMiscGroup.setObjects(
    ("SAF-INTEGRAE-MIB", "integraEtimestamp")
)
if mibBuilder.loadTexts:
    integraEMiscGroup.setStatus("current")

integraERadioGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 10, 2, 2)
)
integraERadioGroup.setObjects(
      *(("SAF-INTEGRAE-MIB", "integraEradioTxPower"),
        ("SAF-INTEGRAE-MIB", "integraEradioTxFrequency"),
        ("SAF-INTEGRAE-MIB", "integraEradioRxLevel"),
        ("SAF-INTEGRAE-MIB", "integraEradioSide"),
        ("SAF-INTEGRAE-MIB", "integraEradioTxMute"),
        ("SAF-INTEGRAE-MIB", "integraEradioDuplexShift"),
        ("SAF-INTEGRAE-MIB", "integraEradioRxFrequency"),
        ("SAF-INTEGRAE-MIB", "integraEradioTemperature"),
        ("SAF-INTEGRAE-MIB", "integraEradioTxMuteDuration"),
        ("SAF-INTEGRAE-MIB", "integraEradioRangeEntryIndex"),
        ("SAF-INTEGRAE-MIB", "integraEradioRangeDescr"),
        ("SAF-INTEGRAE-MIB", "integraEradioRangeTxPower"),
        ("SAF-INTEGRAE-MIB", "integraEradioRangeTxFrequency"),
        ("SAF-INTEGRAE-MIB", "integraEradioPLL"),
        ("SAF-INTEGRAE-MIB", "integraEradioRxLevelState"),
        ("SAF-INTEGRAE-MIB", "integraEradioAtpcState"),
        ("SAF-INTEGRAE-MIB", "integraEradioAtpcUpdatePeriod"),
        ("SAF-INTEGRAE-MIB", "integraEradioAtpcRxLevelMin"),
        ("SAF-INTEGRAE-MIB", "integraEradioAtpcRxLevelMax"))
)
if mibBuilder.loadTexts:
    integraERadioGroup.setStatus("current")

integraEModemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 10, 2, 3)
)
integraEModemGroup.setObjects(
      *(("SAF-INTEGRAE-MIB", "integraEmodemAcquireStatus"),
        ("SAF-INTEGRAE-MIB", "integraEmodemNormalizedMse"),
        ("SAF-INTEGRAE-MIB", "integraEmodemFECload"),
        ("SAF-INTEGRAE-MIB", "integraEmodemFEClocked"),
        ("SAF-INTEGRAE-MIB", "integraEmodemAcquireLastStatusDetails"),
        ("SAF-INTEGRAE-MIB", "integraEmodemTemperature"),
        ("SAF-INTEGRAE-MIB", "integraEmodemBandwidth"),
        ("SAF-INTEGRAE-MIB", "integraEmodemModulation"),
        ("SAF-INTEGRAE-MIB", "integraEmodemRxModulation"),
        ("SAF-INTEGRAE-MIB", "integraEmodemTxModulation"),
        ("SAF-INTEGRAE-MIB", "integraEmodemRxCapacity"),
        ("SAF-INTEGRAE-MIB", "integraEmodemTxCapacity"),
        ("SAF-INTEGRAE-MIB", "integraEmodemACMBengine"),
        ("SAF-INTEGRAE-MIB", "integraEmodemCarrierOffset"),
        ("SAF-INTEGRAE-MIB", "integraEmodemCountTime"),
        ("SAF-INTEGRAE-MIB", "integraEmodemErroredBlock"),
        ("SAF-INTEGRAE-MIB", "integraEmodemErroredSecond"),
        ("SAF-INTEGRAE-MIB", "integraEmodemSeverelyErroredSecond"),
        ("SAF-INTEGRAE-MIB", "integraEmodemBackgroundBlockError"),
        ("SAF-INTEGRAE-MIB", "integraEmodemTotalBlockNumber"),
        ("SAF-INTEGRAE-MIB", "integraEmodemErroredSecondRatio"),
        ("SAF-INTEGRAE-MIB", "integraEmodemSeverelyErroredSecondRatio"),
        ("SAF-INTEGRAE-MIB", "integraEmodemBackgroundBlockErrorRatio"),
        ("SAF-INTEGRAE-MIB", "integraEmodemUptime"),
        ("SAF-INTEGRAE-MIB", "integraEmodemUnavailtime"),
        ("SAF-INTEGRAE-MIB", "integraEmodemModulationACMBmin"),
        ("SAF-INTEGRAE-MIB", "integraEmodemModulationACMBmax"))
)
if mibBuilder.loadTexts:
    integraEModemGroup.setStatus("current")

integraESystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 10, 2, 4)
)
integraESystemGroup.setObjects(
      *(("SAF-INTEGRAE-MIB", "integraEsysCPUtemperature"),
        ("SAF-INTEGRAE-MIB", "integraEsysLicenseExpire"),
        ("SAF-INTEGRAE-MIB", "integraEsysLicenseGenStatus"),
        ("SAF-INTEGRAE-MIB", "integraEsysPSUvoltage"),
        ("SAF-INTEGRAE-MIB", "integraEsysPSUcurrent"),
        ("SAF-INTEGRAE-MIB", "integraEsysPSUpower"),
        ("SAF-INTEGRAE-MIB", "integraEsysBoardTemperature"),
        ("SAF-INTEGRAE-MIB", "integraEsysFreeMemory"),
        ("SAF-INTEGRAE-MIB", "integraEsysCPUidle"),
        ("SAF-INTEGRAE-MIB", "integraEsysDeviceType"),
        ("SAF-INTEGRAE-MIB", "integraEsysDeviceSerial"),
        ("SAF-INTEGRAE-MIB", "integraEsysDeviceProductModel"),
        ("SAF-INTEGRAE-MIB", "integraEsysFanError"),
        ("SAF-INTEGRAE-MIB", "integraEexecuteConfig"),
        ("SAF-INTEGRAE-MIB", "integraEneedStore"),
        ("SAF-INTEGRAE-MIB", "integraEstoreConfig"),
        ("SAF-INTEGRAE-MIB", "integraEsysXADCtemperature"),
        ("SAF-INTEGRAE-MIB", "integraEsysVCCint"),
        ("SAF-INTEGRAE-MIB", "integraEsysVCCaux"),
        ("SAF-INTEGRAE-MIB", "integraEsysVCCbram"),
        ("SAF-INTEGRAE-MIB", "integraEsysVCCpint"),
        ("SAF-INTEGRAE-MIB", "integraEsysVCCpaux"),
        ("SAF-INTEGRAE-MIB", "integraEsysVCCoddr"),
        ("SAF-INTEGRAE-MIB", "integraEsysXadc6v0AvddMdmAna"),
        ("SAF-INTEGRAE-MIB", "integraEsysXadc1v0AvddSwAna"),
        ("SAF-INTEGRAE-MIB", "integraEsysXadc1v0AvddMdmAna"),
        ("SAF-INTEGRAE-MIB", "integraEsysXadc1v0DvddMdmDig"),
        ("SAF-INTEGRAE-MIB", "integraEsysXadc1v0CoreMdmDig"),
        ("SAF-INTEGRAE-MIB", "integraEsysXadc2v5EnvAdcAvddMdmAna"),
        ("SAF-INTEGRAE-MIB", "integraEsysXadc1v0CoreSwDig"),
        ("SAF-INTEGRAE-MIB", "integraEsysXadc5v0IqAvddMdmAna"),
        ("SAF-INTEGRAE-MIB", "integraEsysXadc2v5WbDacClAvddMdmAna"),
        ("SAF-INTEGRAE-MIB", "integraEsysXadc1v2VccPhyDig"),
        ("SAF-INTEGRAE-MIB", "integraEsysXadc4v6AfeDacAvddMdmAna"),
        ("SAF-INTEGRAE-MIB", "integraEsysXadc2v5WbDacAvddMdmAna"),
        ("SAF-INTEGRAE-MIB", "integraEsysXadc2v5VccSysDig"),
        ("SAF-INTEGRAE-MIB", "integraEsysXadc3v3VccSysDig"),
        ("SAF-INTEGRAE-MIB", "integraEsysXadc1v5Ddr3Sw"),
        ("SAF-INTEGRAE-MIB", "integraEsysXadc2v5WbAdcAvddMdmAna"),
        ("SAF-INTEGRAE-MIB", "integraEsysXadc2v5WbDacPllAvddMdmAna"))
)
if mibBuilder.loadTexts:
    integraESystemGroup.setStatus("current")

integraEEthernetGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 10, 2, 5)
)
integraEEthernetGeneralGroup.setObjects(
      *(("SAF-INTEGRAE-MIB", "integraEifPortStatIndex"),
        ("SAF-INTEGRAE-MIB", "integraEifPortStatDescr"),
        ("SAF-INTEGRAE-MIB", "integraEifPortType"),
        ("SAF-INTEGRAE-MIB", "integraEifPortMtu"),
        ("SAF-INTEGRAE-MIB", "integraEifPortHighSpeed"),
        ("SAF-INTEGRAE-MIB", "integraEifPortPhysAddress"),
        ("SAF-INTEGRAE-MIB", "integraEifPortAdminStatus"),
        ("SAF-INTEGRAE-MIB", "integraEifPortOperStatus"),
        ("SAF-INTEGRAE-MIB", "integraEifPortLastChange"),
        ("SAF-INTEGRAE-MIB", "integraEifPortAutoneg"),
        ("SAF-INTEGRAE-MIB", "integraEifPortDuplex"),
        ("SAF-INTEGRAE-MIB", "integraEifPortSyncEthActive"),
        ("SAF-INTEGRAE-MIB", "integraEifPortSyncEthPrio"),
        ("SAF-INTEGRAE-MIB", "integraEifPortFlowControl"),
        ("SAF-INTEGRAE-MIB", "integraEifPortStcIndex"),
        ("SAF-INTEGRAE-MIB", "integraEifPortStcDescr"),
        ("SAF-INTEGRAE-MIB", "integraEifTimePassed"),
        ("SAF-INTEGRAE-MIB", "integraEifIngressPackets"),
        ("SAF-INTEGRAE-MIB", "integraEifIngressBytes"),
        ("SAF-INTEGRAE-MIB", "integraEifEgressPackets"),
        ("SAF-INTEGRAE-MIB", "integraEifEgressBytes"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherRxOversizePkts"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherTxOversizePkts"),
        ("SAF-INTEGRAE-MIB", "integraEifReceivedPkts64Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifTransmittedPkts64Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifReceivedPkts65to127Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifTransmittedPkts65to127Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifReceivedPkts128to255Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifTransmittedPkts128to255Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifReceivedPkts256to511Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifTransmittedPkts256to511Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifReceivedPkts512to1023Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifTransmittedPkts512to1023Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifReceivedPkts1024to1518Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifTransmittedPkts1024to1518Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifIfInBroadcastPkts"),
        ("SAF-INTEGRAE-MIB", "integraEifIfOutBroadcastPkts"),
        ("SAF-INTEGRAE-MIB", "integraEifIfInMulticastPkts"),
        ("SAF-INTEGRAE-MIB", "integraEifIfOutMulticastPkts"),
        ("SAF-INTEGRAE-MIB", "integraEifIngressBPS"),
        ("SAF-INTEGRAE-MIB", "integraEifIngressPPS"),
        ("SAF-INTEGRAE-MIB", "integraEifEgressBPS"),
        ("SAF-INTEGRAE-MIB", "integraEifEgressPPS"),
        ("SAF-INTEGRAE-MIB", "integraEifAllCoSQoutPackets"),
        ("SAF-INTEGRAE-MIB", "integraEifAllCoSQoutBytes"),
        ("SAF-INTEGRAE-MIB", "integraEifAllCoSQdroppedPackets"),
        ("SAF-INTEGRAE-MIB", "integraEifAllCoSQdroppedBytes"),
        ("SAF-INTEGRAE-MIB", "integraEifProcessedRxPackets"),
        ("SAF-INTEGRAE-MIB", "integraEifProcessedRxBytes"),
        ("SAF-INTEGRAE-MIB", "integraEnetCfgIPaddress"),
        ("SAF-INTEGRAE-MIB", "integraEnetCfgIPmask"),
        ("SAF-INTEGRAE-MIB", "integraEnetCfgIPgateway"),
        ("SAF-INTEGRAE-MIB", "integraEnetCfgRemoteIPaddress"),
        ("SAF-INTEGRAE-MIB", "integraEifLspPortAdminState"),
        ("SAF-INTEGRAE-MIB", "integraEifLspPortList"),
        ("SAF-INTEGRAE-MIB", "integraEifLspPortStatus"))
)
if mibBuilder.loadTexts:
    integraEEthernetGeneralGroup.setStatus("current")

integraEEthernetMiiPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 10, 2, 6)
)
integraEEthernetMiiPortGroup.setObjects(
      *(("SAF-INTEGRAE-MIB", "integraEifEtherStatsMulticastPkts"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherStatsBroadcastPkts"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherStatsPkts64Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherStatsPkts65to127Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherStatsPkts128to255Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherStatsPkts256to511Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherStatsPkts512to1023Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherStatsPkts1024to1518Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherStatsOversizePkts"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherStatsOctets"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherStatsPkts"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherStatsTXNoErrors"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherStatsRXNoErrors"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherStatsPkts1519to1522Octets"),
        ("SAF-INTEGRAE-MIB", "integraEifIfInOctets"),
        ("SAF-INTEGRAE-MIB", "integraEifIfOutOctets"),
        ("SAF-INTEGRAE-MIB", "integraEifDot1dTpPortInFrames"),
        ("SAF-INTEGRAE-MIB", "integraEifDot1dTpPortOutFrames"),
        ("SAF-INTEGRAE-MIB", "integraEifDot3InPauseFrames"),
        ("SAF-INTEGRAE-MIB", "integraEifDot3OutPauseFrames"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherStatsUndersizePkts"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherStatsFragments"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherStatsCRCAlignErrors"),
        ("SAF-INTEGRAE-MIB", "integraEifEtherStatsJabbers"))
)
if mibBuilder.loadTexts:
    integraEEthernetMiiPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

integraECompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 9, 10, 1, 1)
)
integraECompliance.setObjects(
      *(("SAF-INTEGRAE-MIB", "integraEMiscGroup"),
        ("SAF-INTEGRAE-MIB", "integraERadioGroup"),
        ("SAF-INTEGRAE-MIB", "integraEModemGroup"),
        ("SAF-INTEGRAE-MIB", "integraESystemGroup"),
        ("SAF-INTEGRAE-MIB", "integraEEthernetGeneralGroup"),
        ("SAF-INTEGRAE-MIB", "integraEEthernetMiiPortGroup"))
)
if mibBuilder.loadTexts:
    integraECompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAF-INTEGRAE-MIB",
    **{"FixedDiv20": FixedDiv20,
       "FixedDiv10": FixedDiv10,
       "integraE": integraE,
       "integraEtimestamp": integraEtimestamp,
       "integraEradio": integraEradio,
       "integraEradioTxPower": integraEradioTxPower,
       "integraEradioTxFrequency": integraEradioTxFrequency,
       "integraEradioRxLevel": integraEradioRxLevel,
       "integraEradioSide": integraEradioSide,
       "integraEradioTxMute": integraEradioTxMute,
       "integraEradioDuplexShift": integraEradioDuplexShift,
       "integraEradioRxFrequency": integraEradioRxFrequency,
       "integraEradioTemperature": integraEradioTemperature,
       "integraEradioTxMuteDuration": integraEradioTxMuteDuration,
       "integraEradioRangesTable": integraEradioRangesTable,
       "integraEradioRangeEntry": integraEradioRangeEntry,
       "integraEradioRangeEntryIndex": integraEradioRangeEntryIndex,
       "integraEradioRangeDescr": integraEradioRangeDescr,
       "integraEradioRangeTxPower": integraEradioRangeTxPower,
       "integraEradioRangeTxFrequency": integraEradioRangeTxFrequency,
       "integraEradioPLL": integraEradioPLL,
       "integraEradioRxLevelState": integraEradioRxLevelState,
       "integraEradioAtpcState": integraEradioAtpcState,
       "integraEradioAtpcUpdatePeriod": integraEradioAtpcUpdatePeriod,
       "integraEradioAtpcRxLevelMin": integraEradioAtpcRxLevelMin,
       "integraEradioAtpcRxLevelMax": integraEradioAtpcRxLevelMax,
       "integraEmodem": integraEmodem,
       "integraEmodemAcquireStatus": integraEmodemAcquireStatus,
       "integraEmodemNormalizedMse": integraEmodemNormalizedMse,
       "integraEmodemFECload": integraEmodemFECload,
       "integraEmodemFEClocked": integraEmodemFEClocked,
       "integraEmodemAcquireLastStatusDetails": integraEmodemAcquireLastStatusDetails,
       "integraEmodemTemperature": integraEmodemTemperature,
       "integraEmodemBandwidth": integraEmodemBandwidth,
       "integraEmodemModulation": integraEmodemModulation,
       "integraEmodemRxModulation": integraEmodemRxModulation,
       "integraEmodemTxModulation": integraEmodemTxModulation,
       "integraEmodemRxCapacity": integraEmodemRxCapacity,
       "integraEmodemTxCapacity": integraEmodemTxCapacity,
       "integraEmodemACMBengine": integraEmodemACMBengine,
       "integraEmodemCarrierOffset": integraEmodemCarrierOffset,
       "integraEmodemCountTime": integraEmodemCountTime,
       "integraEmodemErroredBlock": integraEmodemErroredBlock,
       "integraEmodemErroredSecond": integraEmodemErroredSecond,
       "integraEmodemSeverelyErroredSecond": integraEmodemSeverelyErroredSecond,
       "integraEmodemBackgroundBlockError": integraEmodemBackgroundBlockError,
       "integraEmodemTotalBlockNumber": integraEmodemTotalBlockNumber,
       "integraEmodemErroredSecondRatio": integraEmodemErroredSecondRatio,
       "integraEmodemSeverelyErroredSecondRatio": integraEmodemSeverelyErroredSecondRatio,
       "integraEmodemBackgroundBlockErrorRatio": integraEmodemBackgroundBlockErrorRatio,
       "integraEmodemUptime": integraEmodemUptime,
       "integraEmodemUnavailtime": integraEmodemUnavailtime,
       "integraEmodemModulationACMBmin": integraEmodemModulationACMBmin,
       "integraEmodemModulationACMBmax": integraEmodemModulationACMBmax,
       "integraEsystem": integraEsystem,
       "integraEsysCPUtemperature": integraEsysCPUtemperature,
       "integraEsysLicenseExpire": integraEsysLicenseExpire,
       "integraEsysLicenseGenStatus": integraEsysLicenseGenStatus,
       "integraEsysPSUvoltage": integraEsysPSUvoltage,
       "integraEsysPSUcurrent": integraEsysPSUcurrent,
       "integraEsysPSUpower": integraEsysPSUpower,
       "integraEsysBoardTemperature": integraEsysBoardTemperature,
       "integraEsysFreeMemory": integraEsysFreeMemory,
       "integraEsysCPUidle": integraEsysCPUidle,
       "integraEsysDeviceType": integraEsysDeviceType,
       "integraEsysDeviceSerial": integraEsysDeviceSerial,
       "integraEsysDeviceProductModel": integraEsysDeviceProductModel,
       "integraEsysFanError": integraEsysFanError,
       "integraEsysXADCtemperature": integraEsysXADCtemperature,
       "integraEsysVCCint": integraEsysVCCint,
       "integraEsysVCCaux": integraEsysVCCaux,
       "integraEsysVCCbram": integraEsysVCCbram,
       "integraEsysVCCpint": integraEsysVCCpint,
       "integraEsysVCCpaux": integraEsysVCCpaux,
       "integraEsysVCCoddr": integraEsysVCCoddr,
       "integraEsysXadc6v0AvddMdmAna": integraEsysXadc6v0AvddMdmAna,
       "integraEsysXadc1v0AvddSwAna": integraEsysXadc1v0AvddSwAna,
       "integraEsysXadc1v0AvddMdmAna": integraEsysXadc1v0AvddMdmAna,
       "integraEsysXadc1v0DvddMdmDig": integraEsysXadc1v0DvddMdmDig,
       "integraEsysXadc1v0CoreMdmDig": integraEsysXadc1v0CoreMdmDig,
       "integraEsysXadc2v5EnvAdcAvddMdmAna": integraEsysXadc2v5EnvAdcAvddMdmAna,
       "integraEsysXadc1v0CoreSwDig": integraEsysXadc1v0CoreSwDig,
       "integraEsysXadc5v0IqAvddMdmAna": integraEsysXadc5v0IqAvddMdmAna,
       "integraEsysXadc2v5WbDacClAvddMdmAna": integraEsysXadc2v5WbDacClAvddMdmAna,
       "integraEsysXadc1v2VccPhyDig": integraEsysXadc1v2VccPhyDig,
       "integraEsysXadc4v6AfeDacAvddMdmAna": integraEsysXadc4v6AfeDacAvddMdmAna,
       "integraEsysXadc2v5WbDacAvddMdmAna": integraEsysXadc2v5WbDacAvddMdmAna,
       "integraEsysXadc2v5VccSysDig": integraEsysXadc2v5VccSysDig,
       "integraEsysXadc3v3VccSysDig": integraEsysXadc3v3VccSysDig,
       "integraEsysXadc1v5Ddr3Sw": integraEsysXadc1v5Ddr3Sw,
       "integraEsysXadc2v5WbAdcAvddMdmAna": integraEsysXadc2v5WbAdcAvddMdmAna,
       "integraEsysXadc2v5WbDacPllAvddMdmAna": integraEsysXadc2v5WbDacPllAvddMdmAna,
       "integraEethernet": integraEethernet,
       "integraEifStatusTable": integraEifStatusTable,
       "integraEifPortEntry": integraEifPortEntry,
       "integraEifPortStatIndex": integraEifPortStatIndex,
       "integraEifPortStatDescr": integraEifPortStatDescr,
       "integraEifPortType": integraEifPortType,
       "integraEifPortMtu": integraEifPortMtu,
       "integraEifPortHighSpeed": integraEifPortHighSpeed,
       "integraEifPortPhysAddress": integraEifPortPhysAddress,
       "integraEifPortAdminStatus": integraEifPortAdminStatus,
       "integraEifPortOperStatus": integraEifPortOperStatus,
       "integraEifPortLastChange": integraEifPortLastChange,
       "integraEifPortAutoneg": integraEifPortAutoneg,
       "integraEifPortDuplex": integraEifPortDuplex,
       "integraEifPortSyncEthActive": integraEifPortSyncEthActive,
       "integraEifPortSyncEthPrio": integraEifPortSyncEthPrio,
       "integraEifPortFlowControl": integraEifPortFlowControl,
       "integraEifStatisticsTable": integraEifStatisticsTable,
       "integraEifPortStcEntry": integraEifPortStcEntry,
       "integraEifPortStcIndex": integraEifPortStcIndex,
       "integraEifPortStcDescr": integraEifPortStcDescr,
       "integraEifTimePassed": integraEifTimePassed,
       "integraEifIngressPackets": integraEifIngressPackets,
       "integraEifIngressBytes": integraEifIngressBytes,
       "integraEifEgressPackets": integraEifEgressPackets,
       "integraEifEgressBytes": integraEifEgressBytes,
       "integraEifEtherStatsMulticastPkts": integraEifEtherStatsMulticastPkts,
       "integraEifEtherStatsBroadcastPkts": integraEifEtherStatsBroadcastPkts,
       "integraEifEtherStatsPkts64Octets": integraEifEtherStatsPkts64Octets,
       "integraEifEtherStatsPkts65to127Octets": integraEifEtherStatsPkts65to127Octets,
       "integraEifEtherStatsPkts128to255Octets": integraEifEtherStatsPkts128to255Octets,
       "integraEifEtherStatsPkts256to511Octets": integraEifEtherStatsPkts256to511Octets,
       "integraEifEtherStatsPkts512to1023Octets": integraEifEtherStatsPkts512to1023Octets,
       "integraEifEtherStatsPkts1024to1518Octets": integraEifEtherStatsPkts1024to1518Octets,
       "integraEifEtherStatsOversizePkts": integraEifEtherStatsOversizePkts,
       "integraEifEtherRxOversizePkts": integraEifEtherRxOversizePkts,
       "integraEifEtherTxOversizePkts": integraEifEtherTxOversizePkts,
       "integraEifEtherStatsOctets": integraEifEtherStatsOctets,
       "integraEifEtherStatsPkts": integraEifEtherStatsPkts,
       "integraEifEtherStatsTXNoErrors": integraEifEtherStatsTXNoErrors,
       "integraEifEtherStatsRXNoErrors": integraEifEtherStatsRXNoErrors,
       "integraEifEtherStatsPkts1519to1522Octets": integraEifEtherStatsPkts1519to1522Octets,
       "integraEifIfInOctets": integraEifIfInOctets,
       "integraEifIfOutOctets": integraEifIfOutOctets,
       "integraEifDot1dTpPortInFrames": integraEifDot1dTpPortInFrames,
       "integraEifDot1dTpPortOutFrames": integraEifDot1dTpPortOutFrames,
       "integraEifReceivedPkts64Octets": integraEifReceivedPkts64Octets,
       "integraEifTransmittedPkts64Octets": integraEifTransmittedPkts64Octets,
       "integraEifReceivedPkts65to127Octets": integraEifReceivedPkts65to127Octets,
       "integraEifTransmittedPkts65to127Octets": integraEifTransmittedPkts65to127Octets,
       "integraEifReceivedPkts128to255Octets": integraEifReceivedPkts128to255Octets,
       "integraEifTransmittedPkts128to255Octets": integraEifTransmittedPkts128to255Octets,
       "integraEifReceivedPkts256to511Octets": integraEifReceivedPkts256to511Octets,
       "integraEifTransmittedPkts256to511Octets": integraEifTransmittedPkts256to511Octets,
       "integraEifReceivedPkts512to1023Octets": integraEifReceivedPkts512to1023Octets,
       "integraEifTransmittedPkts512to1023Octets": integraEifTransmittedPkts512to1023Octets,
       "integraEifReceivedPkts1024to1518Octets": integraEifReceivedPkts1024to1518Octets,
       "integraEifTransmittedPkts1024to1518Octets": integraEifTransmittedPkts1024to1518Octets,
       "integraEifIfInBroadcastPkts": integraEifIfInBroadcastPkts,
       "integraEifIfOutBroadcastPkts": integraEifIfOutBroadcastPkts,
       "integraEifIfInMulticastPkts": integraEifIfInMulticastPkts,
       "integraEifIfOutMulticastPkts": integraEifIfOutMulticastPkts,
       "integraEifDot3InPauseFrames": integraEifDot3InPauseFrames,
       "integraEifDot3OutPauseFrames": integraEifDot3OutPauseFrames,
       "integraEifEtherStatsUndersizePkts": integraEifEtherStatsUndersizePkts,
       "integraEifEtherStatsFragments": integraEifEtherStatsFragments,
       "integraEifEtherStatsCRCAlignErrors": integraEifEtherStatsCRCAlignErrors,
       "integraEifEtherStatsJabbers": integraEifEtherStatsJabbers,
       "integraEifIngressBPS": integraEifIngressBPS,
       "integraEifIngressPPS": integraEifIngressPPS,
       "integraEifEgressBPS": integraEifEgressBPS,
       "integraEifEgressPPS": integraEifEgressPPS,
       "integraEifAllCoSQoutPackets": integraEifAllCoSQoutPackets,
       "integraEifAllCoSQoutBytes": integraEifAllCoSQoutBytes,
       "integraEifAllCoSQdroppedPackets": integraEifAllCoSQdroppedPackets,
       "integraEifAllCoSQdroppedBytes": integraEifAllCoSQdroppedBytes,
       "integraEifProcessedRxPackets": integraEifProcessedRxPackets,
       "integraEifProcessedRxBytes": integraEifProcessedRxBytes,
       "integraEifLspPortAdminState": integraEifLspPortAdminState,
       "integraEifLspPortList": integraEifLspPortList,
       "integraEifLspPortStatus": integraEifLspPortStatus,
       "integraEexecuteConfig": integraEexecuteConfig,
       "integraEneedStore": integraEneedStore,
       "integraEstoreConfig": integraEstoreConfig,
       "integraEnetCfg": integraEnetCfg,
       "integraEnetCfgIPaddress": integraEnetCfgIPaddress,
       "integraEnetCfgIPmask": integraEnetCfgIPmask,
       "integraEnetCfgIPgateway": integraEnetCfgIPgateway,
       "integraEnetCfgRemoteIPaddress": integraEnetCfgRemoteIPaddress,
       "integraEConformance": integraEConformance,
       "integraECompliances": integraECompliances,
       "integraECompliance": integraECompliance,
       "integraEGroups": integraEGroups,
       "integraEMiscGroup": integraEMiscGroup,
       "integraERadioGroup": integraERadioGroup,
       "integraEModemGroup": integraEModemGroup,
       "integraESystemGroup": integraESystemGroup,
       "integraEEthernetGeneralGroup": integraEEthernetGeneralGroup,
       "integraEEthernetMiiPortGroup": integraEEthernetMiiPortGroup}
)
