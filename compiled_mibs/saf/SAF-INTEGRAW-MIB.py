# SNMP MIB module (SAF-INTEGRAW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\saf\SAF-INTEGRAW-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:24:47 2025
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

integraW = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    integraW.setRevisions(
        ("2016-05-11 00:00",
         "2015-09-17 00:00",
         "2015-09-15 00:00",
         "2015-08-12 00:00",
         "2015-07-29 00:00",
         "2015-05-29 00:00",
         "2015-05-20 00:00",
         "2015-04-21 00:00",
         "2015-04-14 00:00",
         "2015-03-24 00:00",
         "2015-02-04 00:00",
         "2015-01-20 00:00",
         "2015-01-08 00:00",
         "2015-01-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IntegraWtimestamp_Type = DateAndTime
_IntegraWtimestamp_Object = MibScalar
integraWtimestamp = _IntegraWtimestamp_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 1),
    _IntegraWtimestamp_Type()
)
integraWtimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtimestamp.setStatus("current")
_IntegraWradio_ObjectIdentity = ObjectIdentity
integraWradio = _IntegraWradio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 2)
)
_IntegraWradioTxPower_Type = Integer32
_IntegraWradioTxPower_Object = MibScalar
integraWradioTxPower = _IntegraWradioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 2, 1),
    _IntegraWradioTxPower_Type()
)
integraWradioTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraWradioTxPower.setStatus("current")
if mibBuilder.loadTexts:
    integraWradioTxPower.setUnits("dBm")
_IntegraWradioTxFrequency_Type = Integer32
_IntegraWradioTxFrequency_Object = MibScalar
integraWradioTxFrequency = _IntegraWradioTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 2, 2),
    _IntegraWradioTxFrequency_Type()
)
integraWradioTxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraWradioTxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    integraWradioTxFrequency.setUnits("kHz")
_IntegraWradioRxLevel_Type = Integer32
_IntegraWradioRxLevel_Object = MibScalar
integraWradioRxLevel = _IntegraWradioRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 2, 3),
    _IntegraWradioRxLevel_Type()
)
integraWradioRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWradioRxLevel.setStatus("current")
if mibBuilder.loadTexts:
    integraWradioRxLevel.setUnits("dBm")


class _IntegraWradioSide_Type(Integer32):
    """Custom type integraWradioSide based on Integer32"""
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


_IntegraWradioSide_Type.__name__ = "Integer32"
_IntegraWradioSide_Object = MibScalar
integraWradioSide = _IntegraWradioSide_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 2, 4),
    _IntegraWradioSide_Type()
)
integraWradioSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWradioSide.setStatus("current")


class _IntegraWradioTxMute_Type(Integer32):
    """Custom type integraWradioTxMute based on Integer32"""
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


_IntegraWradioTxMute_Type.__name__ = "Integer32"
_IntegraWradioTxMute_Object = MibScalar
integraWradioTxMute = _IntegraWradioTxMute_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 2, 5),
    _IntegraWradioTxMute_Type()
)
integraWradioTxMute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWradioTxMute.setStatus("current")
_IntegraWradioDuplexShift_Type = Integer32
_IntegraWradioDuplexShift_Object = MibScalar
integraWradioDuplexShift = _IntegraWradioDuplexShift_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 2, 6),
    _IntegraWradioDuplexShift_Type()
)
integraWradioDuplexShift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWradioDuplexShift.setStatus("current")
if mibBuilder.loadTexts:
    integraWradioDuplexShift.setUnits("kHz")
_IntegraWradioRxFrequency_Type = Integer32
_IntegraWradioRxFrequency_Object = MibScalar
integraWradioRxFrequency = _IntegraWradioRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 2, 7),
    _IntegraWradioRxFrequency_Type()
)
integraWradioRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWradioRxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    integraWradioRxFrequency.setUnits("kHz")
_IntegraWradioTemperature_Type = Integer32
_IntegraWradioTemperature_Object = MibScalar
integraWradioTemperature = _IntegraWradioTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 2, 8),
    _IntegraWradioTemperature_Type()
)
integraWradioTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWradioTemperature.setStatus("current")
if mibBuilder.loadTexts:
    integraWradioTemperature.setUnits("C")


class _IntegraWradioTxMuteDuration_Type(Integer32):
    """Custom type integraWradioTxMuteDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214748364),
    )


_IntegraWradioTxMuteDuration_Type.__name__ = "Integer32"
_IntegraWradioTxMuteDuration_Object = MibScalar
integraWradioTxMuteDuration = _IntegraWradioTxMuteDuration_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 2, 9),
    _IntegraWradioTxMuteDuration_Type()
)
integraWradioTxMuteDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraWradioTxMuteDuration.setStatus("current")
if mibBuilder.loadTexts:
    integraWradioTxMuteDuration.setUnits("s")
_IntegraWradioRangesTable_Object = MibTable
integraWradioRangesTable = _IntegraWradioRangesTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 2, 10)
)
if mibBuilder.loadTexts:
    integraWradioRangesTable.setStatus("current")
_IntegraWradioRangeEntry_Object = MibTableRow
integraWradioRangeEntry = _IntegraWradioRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 2, 10, 1)
)
integraWradioRangeEntry.setIndexNames(
    (0, "SAF-INTEGRAW-MIB", "integraWradioRangeEntryIndex"),
)
if mibBuilder.loadTexts:
    integraWradioRangeEntry.setStatus("current")


class _IntegraWradioRangeEntryIndex_Type(Integer32):
    """Custom type integraWradioRangeEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IntegraWradioRangeEntryIndex_Type.__name__ = "Integer32"
_IntegraWradioRangeEntryIndex_Object = MibTableColumn
integraWradioRangeEntryIndex = _IntegraWradioRangeEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 2, 10, 1, 1),
    _IntegraWradioRangeEntryIndex_Type()
)
integraWradioRangeEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWradioRangeEntryIndex.setStatus("current")


class _IntegraWradioRangeDescr_Type(DisplayString):
    """Custom type integraWradioRangeDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntegraWradioRangeDescr_Type.__name__ = "DisplayString"
_IntegraWradioRangeDescr_Object = MibTableColumn
integraWradioRangeDescr = _IntegraWradioRangeDescr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 2, 10, 1, 2),
    _IntegraWradioRangeDescr_Type()
)
integraWradioRangeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWradioRangeDescr.setStatus("current")
_IntegraWradioRangeTxPower_Type = Integer32
_IntegraWradioRangeTxPower_Object = MibTableColumn
integraWradioRangeTxPower = _IntegraWradioRangeTxPower_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 2, 10, 1, 3),
    _IntegraWradioRangeTxPower_Type()
)
integraWradioRangeTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWradioRangeTxPower.setStatus("current")
if mibBuilder.loadTexts:
    integraWradioRangeTxPower.setUnits("dBm")
_IntegraWradioRangeTxFrequency_Type = Integer32
_IntegraWradioRangeTxFrequency_Object = MibTableColumn
integraWradioRangeTxFrequency = _IntegraWradioRangeTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 2, 10, 1, 4),
    _IntegraWradioRangeTxFrequency_Type()
)
integraWradioRangeTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWradioRangeTxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    integraWradioRangeTxFrequency.setUnits("kHz")


class _IntegraWradioPLL_Type(Integer32):
    """Custom type integraWradioPLL based on Integer32"""
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


_IntegraWradioPLL_Type.__name__ = "Integer32"
_IntegraWradioPLL_Object = MibScalar
integraWradioPLL = _IntegraWradioPLL_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 2, 11),
    _IntegraWradioPLL_Type()
)
integraWradioPLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWradioPLL.setStatus("current")


class _IntegraWradioRxLevelState_Type(Integer32):
    """Custom type integraWradioRxLevelState based on Integer32"""
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


_IntegraWradioRxLevelState_Type.__name__ = "Integer32"
_IntegraWradioRxLevelState_Object = MibScalar
integraWradioRxLevelState = _IntegraWradioRxLevelState_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 2, 12),
    _IntegraWradioRxLevelState_Type()
)
integraWradioRxLevelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWradioRxLevelState.setStatus("current")
_IntegraWmodem_ObjectIdentity = ObjectIdentity
integraWmodem = _IntegraWmodem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 3)
)


class _IntegraWmodemAcquireStatus_Type(Integer32):
    """Custom type integraWmodemAcquireStatus based on Integer32"""
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


_IntegraWmodemAcquireStatus_Type.__name__ = "Integer32"
_IntegraWmodemAcquireStatus_Object = MibScalar
integraWmodemAcquireStatus = _IntegraWmodemAcquireStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 3, 1),
    _IntegraWmodemAcquireStatus_Type()
)
integraWmodemAcquireStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWmodemAcquireStatus.setStatus("current")
_IntegraWmodemMse_Type = Integer32
_IntegraWmodemMse_Object = MibScalar
integraWmodemMse = _IntegraWmodemMse_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 3, 2),
    _IntegraWmodemMse_Type()
)
integraWmodemMse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWmodemMse.setStatus("current")
if mibBuilder.loadTexts:
    integraWmodemMse.setUnits("dB")
_IntegraWmodemFecLoad_Type = DisplayString
_IntegraWmodemFecLoad_Object = MibScalar
integraWmodemFecLoad = _IntegraWmodemFecLoad_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 3, 3),
    _IntegraWmodemFecLoad_Type()
)
integraWmodemFecLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWmodemFecLoad.setStatus("current")


class _IntegraWmodemSyncLoss_Type(Integer32):
    """Custom type integraWmodemSyncLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2),
          ("unknown", 3))
    )


_IntegraWmodemSyncLoss_Type.__name__ = "Integer32"
_IntegraWmodemSyncLoss_Object = MibScalar
integraWmodemSyncLoss = _IntegraWmodemSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 3, 4),
    _IntegraWmodemSyncLoss_Type()
)
integraWmodemSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWmodemSyncLoss.setStatus("current")
_IntegraWmodemBandwidth_Type = Integer32
_IntegraWmodemBandwidth_Object = MibScalar
integraWmodemBandwidth = _IntegraWmodemBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 3, 6),
    _IntegraWmodemBandwidth_Type()
)
integraWmodemBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWmodemBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    integraWmodemBandwidth.setUnits("kHz")
_IntegraWmodemModulation_Type = DisplayString
_IntegraWmodemModulation_Object = MibScalar
integraWmodemModulation = _IntegraWmodemModulation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 3, 7),
    _IntegraWmodemModulation_Type()
)
integraWmodemModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWmodemModulation.setStatus("current")
_IntegraWmodemRxModulation_Type = DisplayString
_IntegraWmodemRxModulation_Object = MibScalar
integraWmodemRxModulation = _IntegraWmodemRxModulation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 3, 8),
    _IntegraWmodemRxModulation_Type()
)
integraWmodemRxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWmodemRxModulation.setStatus("current")
_IntegraWmodemTxModulation_Type = DisplayString
_IntegraWmodemTxModulation_Object = MibScalar
integraWmodemTxModulation = _IntegraWmodemTxModulation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 3, 9),
    _IntegraWmodemTxModulation_Type()
)
integraWmodemTxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWmodemTxModulation.setStatus("current")
_IntegraWmodemRxCapacity_Type = Integer32
_IntegraWmodemRxCapacity_Object = MibScalar
integraWmodemRxCapacity = _IntegraWmodemRxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 3, 10),
    _IntegraWmodemRxCapacity_Type()
)
integraWmodemRxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWmodemRxCapacity.setStatus("current")
if mibBuilder.loadTexts:
    integraWmodemRxCapacity.setUnits("kb/s")
_IntegraWmodemTxCapacity_Type = Integer32
_IntegraWmodemTxCapacity_Object = MibScalar
integraWmodemTxCapacity = _IntegraWmodemTxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 3, 11),
    _IntegraWmodemTxCapacity_Type()
)
integraWmodemTxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWmodemTxCapacity.setStatus("current")
if mibBuilder.loadTexts:
    integraWmodemTxCapacity.setUnits("kb/s")


class _IntegraWmodemAcmEngine_Type(Integer32):
    """Custom type integraWmodemAcmEngine based on Integer32"""
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


_IntegraWmodemAcmEngine_Type.__name__ = "Integer32"
_IntegraWmodemAcmEngine_Object = MibScalar
integraWmodemAcmEngine = _IntegraWmodemAcmEngine_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 3, 12),
    _IntegraWmodemAcmEngine_Type()
)
integraWmodemAcmEngine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWmodemAcmEngine.setStatus("current")
_IntegraWmodemSignalQuality_Type = Integer32
_IntegraWmodemSignalQuality_Object = MibScalar
integraWmodemSignalQuality = _IntegraWmodemSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 3, 14),
    _IntegraWmodemSignalQuality_Type()
)
integraWmodemSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWmodemSignalQuality.setStatus("current")
if mibBuilder.loadTexts:
    integraWmodemSignalQuality.setUnits("%")
_IntegraWsystem_ObjectIdentity = ObjectIdentity
integraWsystem = _IntegraWsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 4)
)
_IntegraWsysCPUtemperature_Type = Integer32
_IntegraWsysCPUtemperature_Object = MibScalar
integraWsysCPUtemperature = _IntegraWsysCPUtemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 4, 2),
    _IntegraWsysCPUtemperature_Type()
)
integraWsysCPUtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWsysCPUtemperature.setStatus("current")
if mibBuilder.loadTexts:
    integraWsysCPUtemperature.setUnits("C")
_IntegraWsysLicenseExpire_Type = Gauge32
_IntegraWsysLicenseExpire_Object = MibScalar
integraWsysLicenseExpire = _IntegraWsysLicenseExpire_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 4, 3),
    _IntegraWsysLicenseExpire_Type()
)
integraWsysLicenseExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWsysLicenseExpire.setStatus("current")
if mibBuilder.loadTexts:
    integraWsysLicenseExpire.setUnits("s")


class _IntegraWsysLicenseGenStatus_Type(Integer32):
    """Custom type integraWsysLicenseGenStatus based on Integer32"""
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


_IntegraWsysLicenseGenStatus_Type.__name__ = "Integer32"
_IntegraWsysLicenseGenStatus_Object = MibScalar
integraWsysLicenseGenStatus = _IntegraWsysLicenseGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 4, 4),
    _IntegraWsysLicenseGenStatus_Type()
)
integraWsysLicenseGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWsysLicenseGenStatus.setStatus("current")
_IntegraWsysPSUvoltage_Type = Integer32
_IntegraWsysPSUvoltage_Object = MibScalar
integraWsysPSUvoltage = _IntegraWsysPSUvoltage_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 4, 5),
    _IntegraWsysPSUvoltage_Type()
)
integraWsysPSUvoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWsysPSUvoltage.setStatus("current")
if mibBuilder.loadTexts:
    integraWsysPSUvoltage.setUnits("mV")
_IntegraWsysPSUcurrent_Type = Integer32
_IntegraWsysPSUcurrent_Object = MibScalar
integraWsysPSUcurrent = _IntegraWsysPSUcurrent_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 4, 6),
    _IntegraWsysPSUcurrent_Type()
)
integraWsysPSUcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWsysPSUcurrent.setStatus("current")
if mibBuilder.loadTexts:
    integraWsysPSUcurrent.setUnits("mA")
_IntegraWsysPSUpower_Type = Integer32
_IntegraWsysPSUpower_Object = MibScalar
integraWsysPSUpower = _IntegraWsysPSUpower_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 4, 7),
    _IntegraWsysPSUpower_Type()
)
integraWsysPSUpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWsysPSUpower.setStatus("current")
if mibBuilder.loadTexts:
    integraWsysPSUpower.setUnits("mW")
_IntegraWsysBoardTemperature_Type = Integer32
_IntegraWsysBoardTemperature_Object = MibScalar
integraWsysBoardTemperature = _IntegraWsysBoardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 4, 8),
    _IntegraWsysBoardTemperature_Type()
)
integraWsysBoardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWsysBoardTemperature.setStatus("current")
if mibBuilder.loadTexts:
    integraWsysBoardTemperature.setUnits("C")
_IntegraWsysFreeMemory_Type = Integer32
_IntegraWsysFreeMemory_Object = MibScalar
integraWsysFreeMemory = _IntegraWsysFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 4, 9),
    _IntegraWsysFreeMemory_Type()
)
integraWsysFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWsysFreeMemory.setStatus("current")
if mibBuilder.loadTexts:
    integraWsysFreeMemory.setUnits("%")
_IntegraWsysCPUidle_Type = Integer32
_IntegraWsysCPUidle_Object = MibScalar
integraWsysCPUidle = _IntegraWsysCPUidle_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 4, 10),
    _IntegraWsysCPUidle_Type()
)
integraWsysCPUidle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWsysCPUidle.setStatus("current")
if mibBuilder.loadTexts:
    integraWsysCPUidle.setUnits("%")
_IntegraWethernet_ObjectIdentity = ObjectIdentity
integraWethernet = _IntegraWethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5)
)
_IntegraWifStatusTable_Object = MibTable
integraWifStatusTable = _IntegraWifStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 1)
)
if mibBuilder.loadTexts:
    integraWifStatusTable.setStatus("current")
_IntegraWifPortEntry_Object = MibTableRow
integraWifPortEntry = _IntegraWifPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 1, 1)
)
integraWifPortEntry.setIndexNames(
    (0, "SAF-INTEGRAW-MIB", "integraWifPortStatIndex"),
)
if mibBuilder.loadTexts:
    integraWifPortEntry.setStatus("current")


class _IntegraWifPortStatIndex_Type(Integer32):
    """Custom type integraWifPortStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IntegraWifPortStatIndex_Type.__name__ = "Integer32"
_IntegraWifPortStatIndex_Object = MibTableColumn
integraWifPortStatIndex = _IntegraWifPortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 1, 1, 1),
    _IntegraWifPortStatIndex_Type()
)
integraWifPortStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWifPortStatIndex.setStatus("current")


class _IntegraWifPortStatDescr_Type(DisplayString):
    """Custom type integraWifPortStatDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntegraWifPortStatDescr_Type.__name__ = "DisplayString"
_IntegraWifPortStatDescr_Object = MibTableColumn
integraWifPortStatDescr = _IntegraWifPortStatDescr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 1, 1, 2),
    _IntegraWifPortStatDescr_Type()
)
integraWifPortStatDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWifPortStatDescr.setStatus("current")
_IntegraWifPortType_Type = IANAifType
_IntegraWifPortType_Object = MibTableColumn
integraWifPortType = _IntegraWifPortType_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 1, 1, 3),
    _IntegraWifPortType_Type()
)
integraWifPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWifPortType.setStatus("current")
_IntegraWifPortMtu_Type = Integer32
_IntegraWifPortMtu_Object = MibTableColumn
integraWifPortMtu = _IntegraWifPortMtu_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 1, 1, 4),
    _IntegraWifPortMtu_Type()
)
integraWifPortMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWifPortMtu.setStatus("current")
if mibBuilder.loadTexts:
    integraWifPortMtu.setUnits("B")
_IntegraWifPortSpeed_Type = Gauge32
_IntegraWifPortSpeed_Object = MibTableColumn
integraWifPortSpeed = _IntegraWifPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 1, 1, 5),
    _IntegraWifPortSpeed_Type()
)
integraWifPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWifPortSpeed.setStatus("current")
if mibBuilder.loadTexts:
    integraWifPortSpeed.setUnits("bps")
_IntegraWifPortPhysAddress_Type = PhysAddress
_IntegraWifPortPhysAddress_Object = MibTableColumn
integraWifPortPhysAddress = _IntegraWifPortPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 1, 1, 6),
    _IntegraWifPortPhysAddress_Type()
)
integraWifPortPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWifPortPhysAddress.setStatus("current")


class _IntegraWifPortAdminStatus_Type(Integer32):
    """Custom type integraWifPortAdminStatus based on Integer32"""
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


_IntegraWifPortAdminStatus_Type.__name__ = "Integer32"
_IntegraWifPortAdminStatus_Object = MibTableColumn
integraWifPortAdminStatus = _IntegraWifPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 1, 1, 7),
    _IntegraWifPortAdminStatus_Type()
)
integraWifPortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWifPortAdminStatus.setStatus("current")


class _IntegraWifPortOperStatus_Type(Integer32):
    """Custom type integraWifPortOperStatus based on Integer32"""
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


_IntegraWifPortOperStatus_Type.__name__ = "Integer32"
_IntegraWifPortOperStatus_Object = MibTableColumn
integraWifPortOperStatus = _IntegraWifPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 1, 1, 8),
    _IntegraWifPortOperStatus_Type()
)
integraWifPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWifPortOperStatus.setStatus("current")
_IntegraWifPortLastChange_Type = TimeTicks
_IntegraWifPortLastChange_Object = MibTableColumn
integraWifPortLastChange = _IntegraWifPortLastChange_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 1, 1, 9),
    _IntegraWifPortLastChange_Type()
)
integraWifPortLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWifPortLastChange.setStatus("current")


class _IntegraWifPortAutoneg_Type(Integer32):
    """Custom type integraWifPortAutoneg based on Integer32"""
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


_IntegraWifPortAutoneg_Type.__name__ = "Integer32"
_IntegraWifPortAutoneg_Object = MibTableColumn
integraWifPortAutoneg = _IntegraWifPortAutoneg_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 1, 1, 10),
    _IntegraWifPortAutoneg_Type()
)
integraWifPortAutoneg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWifPortAutoneg.setStatus("current")


class _IntegraWifPortDuplex_Type(Integer32):
    """Custom type integraWifPortDuplex based on Integer32"""
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


_IntegraWifPortDuplex_Type.__name__ = "Integer32"
_IntegraWifPortDuplex_Object = MibTableColumn
integraWifPortDuplex = _IntegraWifPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 1, 1, 11),
    _IntegraWifPortDuplex_Type()
)
integraWifPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWifPortDuplex.setStatus("current")


class _IntegraWifPortSyncEthActive_Type(Integer32):
    """Custom type integraWifPortSyncEthActive based on Integer32"""
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


_IntegraWifPortSyncEthActive_Type.__name__ = "Integer32"
_IntegraWifPortSyncEthActive_Object = MibTableColumn
integraWifPortSyncEthActive = _IntegraWifPortSyncEthActive_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 1, 1, 12),
    _IntegraWifPortSyncEthActive_Type()
)
integraWifPortSyncEthActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWifPortSyncEthActive.setStatus("current")
_IntegraWifPortSyncEthPrio_Type = Integer32
_IntegraWifPortSyncEthPrio_Object = MibTableColumn
integraWifPortSyncEthPrio = _IntegraWifPortSyncEthPrio_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 1, 1, 13),
    _IntegraWifPortSyncEthPrio_Type()
)
integraWifPortSyncEthPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWifPortSyncEthPrio.setStatus("current")


class _IntegraWifPortFlowControl_Type(Integer32):
    """Custom type integraWifPortFlowControl based on Integer32"""
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


_IntegraWifPortFlowControl_Type.__name__ = "Integer32"
_IntegraWifPortFlowControl_Object = MibTableColumn
integraWifPortFlowControl = _IntegraWifPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 1, 1, 14),
    _IntegraWifPortFlowControl_Type()
)
integraWifPortFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWifPortFlowControl.setStatus("current")
_IntegraWifStatisticsTable_Object = MibTable
integraWifStatisticsTable = _IntegraWifStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2)
)
if mibBuilder.loadTexts:
    integraWifStatisticsTable.setStatus("current")
_IntegraWifPortStcEntry_Object = MibTableRow
integraWifPortStcEntry = _IntegraWifPortStcEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1)
)
integraWifPortStcEntry.setIndexNames(
    (0, "SAF-INTEGRAW-MIB", "integraWifPortStcIndex"),
)
if mibBuilder.loadTexts:
    integraWifPortStcEntry.setStatus("current")


class _IntegraWifPortStcIndex_Type(Integer32):
    """Custom type integraWifPortStcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IntegraWifPortStcIndex_Type.__name__ = "Integer32"
_IntegraWifPortStcIndex_Object = MibTableColumn
integraWifPortStcIndex = _IntegraWifPortStcIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 1),
    _IntegraWifPortStcIndex_Type()
)
integraWifPortStcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWifPortStcIndex.setStatus("current")


class _IntegraWifPortStcDescr_Type(DisplayString):
    """Custom type integraWifPortStcDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntegraWifPortStcDescr_Type.__name__ = "DisplayString"
_IntegraWifPortStcDescr_Object = MibTableColumn
integraWifPortStcDescr = _IntegraWifPortStcDescr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 2),
    _IntegraWifPortStcDescr_Type()
)
integraWifPortStcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWifPortStcDescr.setStatus("current")
_IntegraWifTimePassed_Type = TimeTicks
_IntegraWifTimePassed_Object = MibTableColumn
integraWifTimePassed = _IntegraWifTimePassed_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 3),
    _IntegraWifTimePassed_Type()
)
integraWifTimePassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWifTimePassed.setStatus("current")
if mibBuilder.loadTexts:
    integraWifTimePassed.setUnits("s/100")
_IntegraWrxDetected_Type = Counter64
_IntegraWrxDetected_Object = MibTableColumn
integraWrxDetected = _IntegraWrxDetected_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 4),
    _IntegraWrxDetected_Type()
)
integraWrxDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrxDetected.setStatus("current")
if mibBuilder.loadTexts:
    integraWrxDetected.setUnits("packet")
_IntegraWrxDropped_Type = Counter64
_IntegraWrxDropped_Object = MibTableColumn
integraWrxDropped = _IntegraWrxDropped_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 5),
    _IntegraWrxDropped_Type()
)
integraWrxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrxDropped.setStatus("current")
if mibBuilder.loadTexts:
    integraWrxDropped.setUnits("packet")
_IntegraWtxDetected_Type = Counter64
_IntegraWtxDetected_Object = MibTableColumn
integraWtxDetected = _IntegraWtxDetected_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 6),
    _IntegraWtxDetected_Type()
)
integraWtxDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxDetected.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxDetected.setUnits("packet")
_IntegraWtxDropped_Type = Counter64
_IntegraWtxDropped_Object = MibTableColumn
integraWtxDropped = _IntegraWtxDropped_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 7),
    _IntegraWtxDropped_Type()
)
integraWtxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxDropped.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxDropped.setUnits("packet")
_IntegraWrxBytes_Type = Counter64
_IntegraWrxBytes_Object = MibTableColumn
integraWrxBytes = _IntegraWrxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 8),
    _IntegraWrxBytes_Type()
)
integraWrxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrxBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraWrxBytes.setUnits("B")
_IntegraWtxBytes_Type = Counter64
_IntegraWtxBytes_Object = MibTableColumn
integraWtxBytes = _IntegraWtxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 9),
    _IntegraWtxBytes_Type()
)
integraWtxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxBytes.setUnits("B")
_IntegraWrx64Frames_Type = Counter64
_IntegraWrx64Frames_Object = MibTableColumn
integraWrx64Frames = _IntegraWrx64Frames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 10),
    _IntegraWrx64Frames_Type()
)
integraWrx64Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrx64Frames.setStatus("current")
if mibBuilder.loadTexts:
    integraWrx64Frames.setUnits("frame")
_IntegraWrx65to127Frames_Type = Counter64
_IntegraWrx65to127Frames_Object = MibTableColumn
integraWrx65to127Frames = _IntegraWrx65to127Frames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 11),
    _IntegraWrx65to127Frames_Type()
)
integraWrx65to127Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrx65to127Frames.setStatus("current")
if mibBuilder.loadTexts:
    integraWrx65to127Frames.setUnits("frame")
_IntegraWrx128to255Frames_Type = Counter64
_IntegraWrx128to255Frames_Object = MibTableColumn
integraWrx128to255Frames = _IntegraWrx128to255Frames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 12),
    _IntegraWrx128to255Frames_Type()
)
integraWrx128to255Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrx128to255Frames.setStatus("current")
if mibBuilder.loadTexts:
    integraWrx128to255Frames.setUnits("frame")
_IntegraWrx256to511Frames_Type = Counter64
_IntegraWrx256to511Frames_Object = MibTableColumn
integraWrx256to511Frames = _IntegraWrx256to511Frames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 13),
    _IntegraWrx256to511Frames_Type()
)
integraWrx256to511Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrx256to511Frames.setStatus("current")
if mibBuilder.loadTexts:
    integraWrx256to511Frames.setUnits("frame")
_IntegraWrx512to1023Frames_Type = Counter64
_IntegraWrx512to1023Frames_Object = MibTableColumn
integraWrx512to1023Frames = _IntegraWrx512to1023Frames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 14),
    _IntegraWrx512to1023Frames_Type()
)
integraWrx512to1023Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrx512to1023Frames.setStatus("current")
if mibBuilder.loadTexts:
    integraWrx512to1023Frames.setUnits("frame")
_IntegraWrx1024toMaxFrames_Type = Counter64
_IntegraWrx1024toMaxFrames_Object = MibTableColumn
integraWrx1024toMaxFrames = _IntegraWrx1024toMaxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 15),
    _IntegraWrx1024toMaxFrames_Type()
)
integraWrx1024toMaxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrx1024toMaxFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraWrx1024toMaxFrames.setUnits("frame")
_IntegraWrxUsizeFrames_Type = Counter64
_IntegraWrxUsizeFrames_Object = MibTableColumn
integraWrxUsizeFrames = _IntegraWrxUsizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 16),
    _IntegraWrxUsizeFrames_Type()
)
integraWrxUsizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrxUsizeFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraWrxUsizeFrames.setUnits("frame")
_IntegraWrxOsizeFrames_Type = Counter64
_IntegraWrxOsizeFrames_Object = MibTableColumn
integraWrxOsizeFrames = _IntegraWrxOsizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 17),
    _IntegraWrxOsizeFrames_Type()
)
integraWrxOsizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrxOsizeFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraWrxOsizeFrames.setUnits("frame")
_IntegraWtx64Frames_Type = Counter64
_IntegraWtx64Frames_Object = MibTableColumn
integraWtx64Frames = _IntegraWtx64Frames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 18),
    _IntegraWtx64Frames_Type()
)
integraWtx64Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtx64Frames.setStatus("current")
if mibBuilder.loadTexts:
    integraWtx64Frames.setUnits("frame")
_IntegraWtx65to127Frames_Type = Counter64
_IntegraWtx65to127Frames_Object = MibTableColumn
integraWtx65to127Frames = _IntegraWtx65to127Frames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 19),
    _IntegraWtx65to127Frames_Type()
)
integraWtx65to127Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtx65to127Frames.setStatus("current")
if mibBuilder.loadTexts:
    integraWtx65to127Frames.setUnits("frame")
_IntegraWtx128to255Frames_Type = Counter64
_IntegraWtx128to255Frames_Object = MibTableColumn
integraWtx128to255Frames = _IntegraWtx128to255Frames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 20),
    _IntegraWtx128to255Frames_Type()
)
integraWtx128to255Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtx128to255Frames.setStatus("current")
if mibBuilder.loadTexts:
    integraWtx128to255Frames.setUnits("frame")
_IntegraWtx256to511Frames_Type = Counter64
_IntegraWtx256to511Frames_Object = MibTableColumn
integraWtx256to511Frames = _IntegraWtx256to511Frames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 21),
    _IntegraWtx256to511Frames_Type()
)
integraWtx256to511Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtx256to511Frames.setStatus("current")
if mibBuilder.loadTexts:
    integraWtx256to511Frames.setUnits("frame")
_IntegraWtx512to1023Frames_Type = Counter64
_IntegraWtx512to1023Frames_Object = MibTableColumn
integraWtx512to1023Frames = _IntegraWtx512to1023Frames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 22),
    _IntegraWtx512to1023Frames_Type()
)
integraWtx512to1023Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtx512to1023Frames.setStatus("current")
if mibBuilder.loadTexts:
    integraWtx512to1023Frames.setUnits("frame")
_IntegraWtx1024toMaxFrames_Type = Counter64
_IntegraWtx1024toMaxFrames_Object = MibTableColumn
integraWtx1024toMaxFrames = _IntegraWtx1024toMaxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 23),
    _IntegraWtx1024toMaxFrames_Type()
)
integraWtx1024toMaxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtx1024toMaxFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraWtx1024toMaxFrames.setUnits("frame")
_IntegraWtxUsizeFrames_Type = Counter64
_IntegraWtxUsizeFrames_Object = MibTableColumn
integraWtxUsizeFrames = _IntegraWtxUsizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 24),
    _IntegraWtxUsizeFrames_Type()
)
integraWtxUsizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxUsizeFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxUsizeFrames.setUnits("frame")
_IntegraWtxOsizeFrames_Type = Counter64
_IntegraWtxOsizeFrames_Object = MibTableColumn
integraWtxOsizeFrames = _IntegraWtxOsizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 25),
    _IntegraWtxOsizeFrames_Type()
)
integraWtxOsizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxOsizeFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxOsizeFrames.setUnits("frame")
_IntegraWrxGoodFrames_Type = Counter64
_IntegraWrxGoodFrames_Object = MibTableColumn
integraWrxGoodFrames = _IntegraWrxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 26),
    _IntegraWrxGoodFrames_Type()
)
integraWrxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrxGoodFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraWrxGoodFrames.setUnits("frame")
_IntegraWrxErrors_Type = Counter64
_IntegraWrxErrors_Object = MibTableColumn
integraWrxErrors = _IntegraWrxErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 27),
    _IntegraWrxErrors_Type()
)
integraWrxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrxErrors.setStatus("current")
if mibBuilder.loadTexts:
    integraWrxErrors.setUnits("packet")
_IntegraWrxFifoErr_Type = Counter64
_IntegraWrxFifoErr_Object = MibTableColumn
integraWrxFifoErr = _IntegraWrxFifoErr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 28),
    _IntegraWrxFifoErr_Type()
)
integraWrxFifoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrxFifoErr.setStatus("current")
if mibBuilder.loadTexts:
    integraWrxFifoErr.setUnits("packet")
_IntegraWrxCRCErrors_Type = Counter64
_IntegraWrxCRCErrors_Object = MibTableColumn
integraWrxCRCErrors = _IntegraWrxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 29),
    _IntegraWrxCRCErrors_Type()
)
integraWrxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrxCRCErrors.setStatus("current")
if mibBuilder.loadTexts:
    integraWrxCRCErrors.setUnits("packet")
_IntegraWrxBcastFrames_Type = Counter64
_IntegraWrxBcastFrames_Object = MibTableColumn
integraWrxBcastFrames = _IntegraWrxBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 30),
    _IntegraWrxBcastFrames_Type()
)
integraWrxBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrxBcastFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraWrxBcastFrames.setUnits("frame")
_IntegraWrxMcastFrames_Type = Counter64
_IntegraWrxMcastFrames_Object = MibTableColumn
integraWrxMcastFrames = _IntegraWrxMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 31),
    _IntegraWrxMcastFrames_Type()
)
integraWrxMcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrxMcastFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraWrxMcastFrames.setUnits("frame")
_IntegraWrxCntrlFrames_Type = Counter64
_IntegraWrxCntrlFrames_Object = MibTableColumn
integraWrxCntrlFrames = _IntegraWrxCntrlFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 32),
    _IntegraWrxCntrlFrames_Type()
)
integraWrxCntrlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrxCntrlFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraWrxCntrlFrames.setUnits("frame")
_IntegraWrxLenErrors_Type = Counter64
_IntegraWrxLenErrors_Object = MibTableColumn
integraWrxLenErrors = _IntegraWrxLenErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 33),
    _IntegraWrxLenErrors_Type()
)
integraWrxLenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrxLenErrors.setStatus("current")
if mibBuilder.loadTexts:
    integraWrxLenErrors.setUnits("packet")
_IntegraWrxVlanFrames_Type = Counter64
_IntegraWrxVlanFrames_Object = MibTableColumn
integraWrxVlanFrames = _IntegraWrxVlanFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 34),
    _IntegraWrxVlanFrames_Type()
)
integraWrxVlanFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrxVlanFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraWrxVlanFrames.setUnits("frame")
_IntegraWrxPauseFrames_Type = Counter64
_IntegraWrxPauseFrames_Object = MibTableColumn
integraWrxPauseFrames = _IntegraWrxPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 35),
    _IntegraWrxPauseFrames_Type()
)
integraWrxPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrxPauseFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraWrxPauseFrames.setUnits("frame")
_IntegraWrxOpErrors_Type = Counter64
_IntegraWrxOpErrors_Object = MibTableColumn
integraWrxOpErrors = _IntegraWrxOpErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 36),
    _IntegraWrxOpErrors_Type()
)
integraWrxOpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrxOpErrors.setStatus("current")
if mibBuilder.loadTexts:
    integraWrxOpErrors.setUnits("packet")
_IntegraWrxFrameErrors_Type = Counter64
_IntegraWrxFrameErrors_Object = MibTableColumn
integraWrxFrameErrors = _IntegraWrxFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 37),
    _IntegraWrxFrameErrors_Type()
)
integraWrxFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWrxFrameErrors.setStatus("current")
if mibBuilder.loadTexts:
    integraWrxFrameErrors.setUnits("frame")
_IntegraWtxGoodFrames_Type = Counter64
_IntegraWtxGoodFrames_Object = MibTableColumn
integraWtxGoodFrames = _IntegraWtxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 38),
    _IntegraWtxGoodFrames_Type()
)
integraWtxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxGoodFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxGoodFrames.setUnits("frame")
_IntegraWtxErrors_Type = Counter64
_IntegraWtxErrors_Object = MibTableColumn
integraWtxErrors = _IntegraWtxErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 39),
    _IntegraWtxErrors_Type()
)
integraWtxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxErrors.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxErrors.setUnits("packet")
_IntegraWtxFifoErr_Type = Counter64
_IntegraWtxFifoErr_Object = MibTableColumn
integraWtxFifoErr = _IntegraWtxFifoErr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 40),
    _IntegraWtxFifoErr_Type()
)
integraWtxFifoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxFifoErr.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxFifoErr.setUnits("packet")
_IntegraWtxBcastFrames_Type = Counter64
_IntegraWtxBcastFrames_Object = MibTableColumn
integraWtxBcastFrames = _IntegraWtxBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 41),
    _IntegraWtxBcastFrames_Type()
)
integraWtxBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxBcastFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxBcastFrames.setUnits("frame")
_IntegraWtxMcastFrames_Type = Counter64
_IntegraWtxMcastFrames_Object = MibTableColumn
integraWtxMcastFrames = _IntegraWtxMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 42),
    _IntegraWtxMcastFrames_Type()
)
integraWtxMcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxMcastFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxMcastFrames.setUnits("frame")
_IntegraWtxUrunErrors_Type = Counter64
_IntegraWtxUrunErrors_Object = MibTableColumn
integraWtxUrunErrors = _IntegraWtxUrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 43),
    _IntegraWtxUrunErrors_Type()
)
integraWtxUrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxUrunErrors.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxUrunErrors.setUnits("packet")
_IntegraWtxCntrlFrames_Type = Counter64
_IntegraWtxCntrlFrames_Object = MibTableColumn
integraWtxCntrlFrames = _IntegraWtxCntrlFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 44),
    _IntegraWtxCntrlFrames_Type()
)
integraWtxCntrlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxCntrlFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxCntrlFrames.setUnits("frame")
_IntegraWtxVlanFrames_Type = Counter64
_IntegraWtxVlanFrames_Object = MibTableColumn
integraWtxVlanFrames = _IntegraWtxVlanFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 45),
    _IntegraWtxVlanFrames_Type()
)
integraWtxVlanFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxVlanFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxVlanFrames.setUnits("frame")
_IntegraWtxPauseFrames_Type = Counter64
_IntegraWtxPauseFrames_Object = MibTableColumn
integraWtxPauseFrames = _IntegraWtxPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 46),
    _IntegraWtxPauseFrames_Type()
)
integraWtxPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxPauseFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxPauseFrames.setUnits("frame")
_IntegraWtxSingleCollisions_Type = Counter64
_IntegraWtxSingleCollisions_Object = MibTableColumn
integraWtxSingleCollisions = _IntegraWtxSingleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 47),
    _IntegraWtxSingleCollisions_Type()
)
integraWtxSingleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxSingleCollisions.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxSingleCollisions.setUnits("packet")
_IntegraWtxMultiCollisions_Type = Counter64
_IntegraWtxMultiCollisions_Object = MibTableColumn
integraWtxMultiCollisions = _IntegraWtxMultiCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 48),
    _IntegraWtxMultiCollisions_Type()
)
integraWtxMultiCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxMultiCollisions.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxMultiCollisions.setUnits("packet")
_IntegraWtxDeferred_Type = Counter64
_IntegraWtxDeferred_Object = MibTableColumn
integraWtxDeferred = _IntegraWtxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 49),
    _IntegraWtxDeferred_Type()
)
integraWtxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxDeferred.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxDeferred.setUnits("packet")
_IntegraWtxLateCollisions_Type = Counter64
_IntegraWtxLateCollisions_Object = MibTableColumn
integraWtxLateCollisions = _IntegraWtxLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 50),
    _IntegraWtxLateCollisions_Type()
)
integraWtxLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxLateCollisions.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxLateCollisions.setUnits("packet")
_IntegraWtxExcessCollisions_Type = Counter64
_IntegraWtxExcessCollisions_Object = MibTableColumn
integraWtxExcessCollisions = _IntegraWtxExcessCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 51),
    _IntegraWtxExcessCollisions_Type()
)
integraWtxExcessCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxExcessCollisions.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxExcessCollisions.setUnits("packet")
_IntegraWtxExcessDeferral_Type = Counter64
_IntegraWtxExcessDeferral_Object = MibTableColumn
integraWtxExcessDeferral = _IntegraWtxExcessDeferral_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 52),
    _IntegraWtxExcessDeferral_Type()
)
integraWtxExcessDeferral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxExcessDeferral.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxExcessDeferral.setUnits("packet")
_IntegraWtxAlignErrors_Type = Counter64
_IntegraWtxAlignErrors_Object = MibTableColumn
integraWtxAlignErrors = _IntegraWtxAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 53),
    _IntegraWtxAlignErrors_Type()
)
integraWtxAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxAlignErrors.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxAlignErrors.setUnits("packet")
_IntegraWtxCarrierErrors_Type = Counter64
_IntegraWtxCarrierErrors_Object = MibTableColumn
integraWtxCarrierErrors = _IntegraWtxCarrierErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 54),
    _IntegraWtxCarrierErrors_Type()
)
integraWtxCarrierErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxCarrierErrors.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxCarrierErrors.setUnits("packet")
_IntegraWtxCollisions_Type = Counter64
_IntegraWtxCollisions_Object = MibTableColumn
integraWtxCollisions = _IntegraWtxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 5, 2, 1, 55),
    _IntegraWtxCollisions_Type()
)
integraWtxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWtxCollisions.setStatus("current")
if mibBuilder.loadTexts:
    integraWtxCollisions.setUnits("packet")


class _IntegraWexecuteConfig_Type(Integer32):
    """Custom type integraWexecuteConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_IntegraWexecuteConfig_Type.__name__ = "Integer32"
_IntegraWexecuteConfig_Object = MibScalar
integraWexecuteConfig = _IntegraWexecuteConfig_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 6),
    _IntegraWexecuteConfig_Type()
)
integraWexecuteConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraWexecuteConfig.setStatus("current")


class _IntegraWneedStore_Type(Integer32):
    """Custom type integraWneedStore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("no", 0)
    )


_IntegraWneedStore_Type.__name__ = "Integer32"
_IntegraWneedStore_Object = MibScalar
integraWneedStore = _IntegraWneedStore_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 7),
    _IntegraWneedStore_Type()
)
integraWneedStore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWneedStore.setStatus("current")


class _IntegraWstoreConfig_Type(Integer32):
    """Custom type integraWstoreConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("store", 1)
    )


_IntegraWstoreConfig_Type.__name__ = "Integer32"
_IntegraWstoreConfig_Object = MibScalar
integraWstoreConfig = _IntegraWstoreConfig_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 8),
    _IntegraWstoreConfig_Type()
)
integraWstoreConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraWstoreConfig.setStatus("current")
_IntegraWnetCfg_ObjectIdentity = ObjectIdentity
integraWnetCfg = _IntegraWnetCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 9)
)
_IntegraWnetCfgIPaddress_Type = IpAddress
_IntegraWnetCfgIPaddress_Object = MibScalar
integraWnetCfgIPaddress = _IntegraWnetCfgIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 9, 1),
    _IntegraWnetCfgIPaddress_Type()
)
integraWnetCfgIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraWnetCfgIPaddress.setStatus("current")
_IntegraWnetCfgIPmask_Type = IpAddress
_IntegraWnetCfgIPmask_Object = MibScalar
integraWnetCfgIPmask = _IntegraWnetCfgIPmask_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 9, 2),
    _IntegraWnetCfgIPmask_Type()
)
integraWnetCfgIPmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraWnetCfgIPmask.setStatus("current")
_IntegraWnetCfgIPgateway_Type = IpAddress
_IntegraWnetCfgIPgateway_Object = MibScalar
integraWnetCfgIPgateway = _IntegraWnetCfgIPgateway_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 9, 3),
    _IntegraWnetCfgIPgateway_Type()
)
integraWnetCfgIPgateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraWnetCfgIPgateway.setStatus("current")
_IntegraWnetCfgRemoteIPaddress_Type = IpAddress
_IntegraWnetCfgRemoteIPaddress_Object = MibScalar
integraWnetCfgRemoteIPaddress = _IntegraWnetCfgRemoteIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 9, 4),
    _IntegraWnetCfgRemoteIPaddress_Type()
)
integraWnetCfgRemoteIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraWnetCfgRemoteIPaddress.setStatus("current")
_IntegraWConformance_ObjectIdentity = ObjectIdentity
integraWConformance = _IntegraWConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 10)
)
_IntegraWCompliances_ObjectIdentity = ObjectIdentity
integraWCompliances = _IntegraWCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 10, 1)
)
_IntegraWGroups_ObjectIdentity = ObjectIdentity
integraWGroups = _IntegraWGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 10, 2)
)

# Managed Objects groups

integraWMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 10, 2, 1)
)
integraWMiscGroup.setObjects(
    ("SAF-INTEGRAW-MIB", "integraWtimestamp")
)
if mibBuilder.loadTexts:
    integraWMiscGroup.setStatus("current")

integraWRadioGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 10, 2, 2)
)
integraWRadioGroup.setObjects(
      *(("SAF-INTEGRAW-MIB", "integraWradioTxPower"),
        ("SAF-INTEGRAW-MIB", "integraWradioTxFrequency"),
        ("SAF-INTEGRAW-MIB", "integraWradioRxLevel"),
        ("SAF-INTEGRAW-MIB", "integraWradioSide"),
        ("SAF-INTEGRAW-MIB", "integraWradioTxMute"),
        ("SAF-INTEGRAW-MIB", "integraWradioDuplexShift"),
        ("SAF-INTEGRAW-MIB", "integraWradioRxFrequency"),
        ("SAF-INTEGRAW-MIB", "integraWradioTemperature"),
        ("SAF-INTEGRAW-MIB", "integraWradioTxMuteDuration"),
        ("SAF-INTEGRAW-MIB", "integraWradioRangeEntryIndex"),
        ("SAF-INTEGRAW-MIB", "integraWradioRangeDescr"),
        ("SAF-INTEGRAW-MIB", "integraWradioRangeTxPower"),
        ("SAF-INTEGRAW-MIB", "integraWradioRangeTxFrequency"),
        ("SAF-INTEGRAW-MIB", "integraWradioPLL"))
)
if mibBuilder.loadTexts:
    integraWRadioGroup.setStatus("current")

integraWModemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 10, 2, 3)
)
integraWModemGroup.setObjects(
      *(("SAF-INTEGRAW-MIB", "integraWmodemAcquireStatus"),
        ("SAF-INTEGRAW-MIB", "integraWmodemMse"),
        ("SAF-INTEGRAW-MIB", "integraWmodemFecLoad"),
        ("SAF-INTEGRAW-MIB", "integraWmodemSyncLoss"),
        ("SAF-INTEGRAW-MIB", "integraWmodemBandwidth"),
        ("SAF-INTEGRAW-MIB", "integraWmodemModulation"),
        ("SAF-INTEGRAW-MIB", "integraWmodemRxModulation"),
        ("SAF-INTEGRAW-MIB", "integraWmodemTxModulation"),
        ("SAF-INTEGRAW-MIB", "integraWmodemRxCapacity"),
        ("SAF-INTEGRAW-MIB", "integraWmodemTxCapacity"),
        ("SAF-INTEGRAW-MIB", "integraWmodemAcmEngine"),
        ("SAF-INTEGRAW-MIB", "integraWmodemSignalQuality"))
)
if mibBuilder.loadTexts:
    integraWModemGroup.setStatus("current")

integraWSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 10, 2, 4)
)
integraWSystemGroup.setObjects(
      *(("SAF-INTEGRAW-MIB", "integraWsysCPUtemperature"),
        ("SAF-INTEGRAW-MIB", "integraWsysLicenseExpire"),
        ("SAF-INTEGRAW-MIB", "integraWsysLicenseGenStatus"),
        ("SAF-INTEGRAW-MIB", "integraWsysPSUvoltage"),
        ("SAF-INTEGRAW-MIB", "integraWsysPSUcurrent"),
        ("SAF-INTEGRAW-MIB", "integraWsysPSUpower"),
        ("SAF-INTEGRAW-MIB", "integraWsysBoardTemperature"),
        ("SAF-INTEGRAW-MIB", "integraWsysFreeMemory"),
        ("SAF-INTEGRAW-MIB", "integraWsysCPUidle"),
        ("SAF-INTEGRAW-MIB", "integraWexecuteConfig"),
        ("SAF-INTEGRAW-MIB", "integraWneedStore"),
        ("SAF-INTEGRAW-MIB", "integraWstoreConfig"))
)
if mibBuilder.loadTexts:
    integraWSystemGroup.setStatus("current")

integraWEthernetGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 10, 2, 5)
)
integraWEthernetGeneralGroup.setObjects(
      *(("SAF-INTEGRAW-MIB", "integraWifPortStatIndex"),
        ("SAF-INTEGRAW-MIB", "integraWifPortStatDescr"),
        ("SAF-INTEGRAW-MIB", "integraWifPortType"),
        ("SAF-INTEGRAW-MIB", "integraWifPortMtu"),
        ("SAF-INTEGRAW-MIB", "integraWifPortSpeed"),
        ("SAF-INTEGRAW-MIB", "integraWifPortPhysAddress"),
        ("SAF-INTEGRAW-MIB", "integraWifPortAdminStatus"),
        ("SAF-INTEGRAW-MIB", "integraWifPortOperStatus"),
        ("SAF-INTEGRAW-MIB", "integraWifPortLastChange"),
        ("SAF-INTEGRAW-MIB", "integraWifPortAutoneg"),
        ("SAF-INTEGRAW-MIB", "integraWifPortDuplex"),
        ("SAF-INTEGRAW-MIB", "integraWifPortSyncEthActive"),
        ("SAF-INTEGRAW-MIB", "integraWifPortSyncEthPrio"),
        ("SAF-INTEGRAW-MIB", "integraWifPortFlowControl"),
        ("SAF-INTEGRAW-MIB", "integraWifPortStcIndex"),
        ("SAF-INTEGRAW-MIB", "integraWifPortStcDescr"),
        ("SAF-INTEGRAW-MIB", "integraWifTimePassed"),
        ("SAF-INTEGRAW-MIB", "integraWnetCfgIPaddress"),
        ("SAF-INTEGRAW-MIB", "integraWnetCfgIPmask"),
        ("SAF-INTEGRAW-MIB", "integraWnetCfgIPgateway"),
        ("SAF-INTEGRAW-MIB", "integraWnetCfgRemoteIPaddress"))
)
if mibBuilder.loadTexts:
    integraWEthernetGeneralGroup.setStatus("current")

integraWEthernetMiiPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 10, 2, 6)
)
integraWEthernetMiiPortGroup.setObjects(
      *(("SAF-INTEGRAW-MIB", "integraWrxDetected"),
        ("SAF-INTEGRAW-MIB", "integraWrxDropped"),
        ("SAF-INTEGRAW-MIB", "integraWtxDetected"),
        ("SAF-INTEGRAW-MIB", "integraWtxDropped"),
        ("SAF-INTEGRAW-MIB", "integraWrxBytes"),
        ("SAF-INTEGRAW-MIB", "integraWtxBytes"),
        ("SAF-INTEGRAW-MIB", "integraWrx64Frames"),
        ("SAF-INTEGRAW-MIB", "integraWrx65to127Frames"),
        ("SAF-INTEGRAW-MIB", "integraWrx128to255Frames"),
        ("SAF-INTEGRAW-MIB", "integraWrx256to511Frames"),
        ("SAF-INTEGRAW-MIB", "integraWrx512to1023Frames"),
        ("SAF-INTEGRAW-MIB", "integraWrx1024toMaxFrames"),
        ("SAF-INTEGRAW-MIB", "integraWrxUsizeFrames"),
        ("SAF-INTEGRAW-MIB", "integraWrxOsizeFrames"),
        ("SAF-INTEGRAW-MIB", "integraWtx64Frames"),
        ("SAF-INTEGRAW-MIB", "integraWtx65to127Frames"),
        ("SAF-INTEGRAW-MIB", "integraWtx128to255Frames"),
        ("SAF-INTEGRAW-MIB", "integraWtx256to511Frames"),
        ("SAF-INTEGRAW-MIB", "integraWtx512to1023Frames"),
        ("SAF-INTEGRAW-MIB", "integraWtx1024toMaxFrames"),
        ("SAF-INTEGRAW-MIB", "integraWtxUsizeFrames"),
        ("SAF-INTEGRAW-MIB", "integraWtxOsizeFrames"),
        ("SAF-INTEGRAW-MIB", "integraWrxGoodFrames"),
        ("SAF-INTEGRAW-MIB", "integraWrxErrors"),
        ("SAF-INTEGRAW-MIB", "integraWrxFifoErr"),
        ("SAF-INTEGRAW-MIB", "integraWrxCRCErrors"),
        ("SAF-INTEGRAW-MIB", "integraWrxBcastFrames"),
        ("SAF-INTEGRAW-MIB", "integraWrxMcastFrames"),
        ("SAF-INTEGRAW-MIB", "integraWrxCntrlFrames"),
        ("SAF-INTEGRAW-MIB", "integraWrxLenErrors"),
        ("SAF-INTEGRAW-MIB", "integraWrxVlanFrames"),
        ("SAF-INTEGRAW-MIB", "integraWrxPauseFrames"),
        ("SAF-INTEGRAW-MIB", "integraWrxOpErrors"),
        ("SAF-INTEGRAW-MIB", "integraWrxFrameErrors"),
        ("SAF-INTEGRAW-MIB", "integraWtxGoodFrames"),
        ("SAF-INTEGRAW-MIB", "integraWtxErrors"),
        ("SAF-INTEGRAW-MIB", "integraWtxFifoErr"),
        ("SAF-INTEGRAW-MIB", "integraWtxBcastFrames"),
        ("SAF-INTEGRAW-MIB", "integraWtxMcastFrames"),
        ("SAF-INTEGRAW-MIB", "integraWtxUrunErrors"),
        ("SAF-INTEGRAW-MIB", "integraWtxCntrlFrames"),
        ("SAF-INTEGRAW-MIB", "integraWtxVlanFrames"),
        ("SAF-INTEGRAW-MIB", "integraWtxPauseFrames"),
        ("SAF-INTEGRAW-MIB", "integraWtxSingleCollisions"),
        ("SAF-INTEGRAW-MIB", "integraWtxMultiCollisions"),
        ("SAF-INTEGRAW-MIB", "integraWtxDeferred"),
        ("SAF-INTEGRAW-MIB", "integraWtxLateCollisions"),
        ("SAF-INTEGRAW-MIB", "integraWtxExcessCollisions"),
        ("SAF-INTEGRAW-MIB", "integraWtxExcessDeferral"),
        ("SAF-INTEGRAW-MIB", "integraWtxAlignErrors"),
        ("SAF-INTEGRAW-MIB", "integraWtxCarrierErrors"),
        ("SAF-INTEGRAW-MIB", "integraWtxCollisions"))
)
if mibBuilder.loadTexts:
    integraWEthernetMiiPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

integraWCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 2, 10, 1, 1)
)
integraWCompliance.setObjects(
      *(("SAF-INTEGRAW-MIB", "integraWMiscGroup"),
        ("SAF-INTEGRAW-MIB", "integraWRadioGroup"),
        ("SAF-INTEGRAW-MIB", "integraWModemGroup"),
        ("SAF-INTEGRAW-MIB", "integraWSystemGroup"),
        ("SAF-INTEGRAW-MIB", "integraWEthernetGeneralGroup"),
        ("SAF-INTEGRAW-MIB", "integraWEthernetMiiPortGroup"))
)
if mibBuilder.loadTexts:
    integraWCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAF-INTEGRAW-MIB",
    **{"integraW": integraW,
       "integraWtimestamp": integraWtimestamp,
       "integraWradio": integraWradio,
       "integraWradioTxPower": integraWradioTxPower,
       "integraWradioTxFrequency": integraWradioTxFrequency,
       "integraWradioRxLevel": integraWradioRxLevel,
       "integraWradioSide": integraWradioSide,
       "integraWradioTxMute": integraWradioTxMute,
       "integraWradioDuplexShift": integraWradioDuplexShift,
       "integraWradioRxFrequency": integraWradioRxFrequency,
       "integraWradioTemperature": integraWradioTemperature,
       "integraWradioTxMuteDuration": integraWradioTxMuteDuration,
       "integraWradioRangesTable": integraWradioRangesTable,
       "integraWradioRangeEntry": integraWradioRangeEntry,
       "integraWradioRangeEntryIndex": integraWradioRangeEntryIndex,
       "integraWradioRangeDescr": integraWradioRangeDescr,
       "integraWradioRangeTxPower": integraWradioRangeTxPower,
       "integraWradioRangeTxFrequency": integraWradioRangeTxFrequency,
       "integraWradioPLL": integraWradioPLL,
       "integraWradioRxLevelState": integraWradioRxLevelState,
       "integraWmodem": integraWmodem,
       "integraWmodemAcquireStatus": integraWmodemAcquireStatus,
       "integraWmodemMse": integraWmodemMse,
       "integraWmodemFecLoad": integraWmodemFecLoad,
       "integraWmodemSyncLoss": integraWmodemSyncLoss,
       "integraWmodemBandwidth": integraWmodemBandwidth,
       "integraWmodemModulation": integraWmodemModulation,
       "integraWmodemRxModulation": integraWmodemRxModulation,
       "integraWmodemTxModulation": integraWmodemTxModulation,
       "integraWmodemRxCapacity": integraWmodemRxCapacity,
       "integraWmodemTxCapacity": integraWmodemTxCapacity,
       "integraWmodemAcmEngine": integraWmodemAcmEngine,
       "integraWmodemSignalQuality": integraWmodemSignalQuality,
       "integraWsystem": integraWsystem,
       "integraWsysCPUtemperature": integraWsysCPUtemperature,
       "integraWsysLicenseExpire": integraWsysLicenseExpire,
       "integraWsysLicenseGenStatus": integraWsysLicenseGenStatus,
       "integraWsysPSUvoltage": integraWsysPSUvoltage,
       "integraWsysPSUcurrent": integraWsysPSUcurrent,
       "integraWsysPSUpower": integraWsysPSUpower,
       "integraWsysBoardTemperature": integraWsysBoardTemperature,
       "integraWsysFreeMemory": integraWsysFreeMemory,
       "integraWsysCPUidle": integraWsysCPUidle,
       "integraWethernet": integraWethernet,
       "integraWifStatusTable": integraWifStatusTable,
       "integraWifPortEntry": integraWifPortEntry,
       "integraWifPortStatIndex": integraWifPortStatIndex,
       "integraWifPortStatDescr": integraWifPortStatDescr,
       "integraWifPortType": integraWifPortType,
       "integraWifPortMtu": integraWifPortMtu,
       "integraWifPortSpeed": integraWifPortSpeed,
       "integraWifPortPhysAddress": integraWifPortPhysAddress,
       "integraWifPortAdminStatus": integraWifPortAdminStatus,
       "integraWifPortOperStatus": integraWifPortOperStatus,
       "integraWifPortLastChange": integraWifPortLastChange,
       "integraWifPortAutoneg": integraWifPortAutoneg,
       "integraWifPortDuplex": integraWifPortDuplex,
       "integraWifPortSyncEthActive": integraWifPortSyncEthActive,
       "integraWifPortSyncEthPrio": integraWifPortSyncEthPrio,
       "integraWifPortFlowControl": integraWifPortFlowControl,
       "integraWifStatisticsTable": integraWifStatisticsTable,
       "integraWifPortStcEntry": integraWifPortStcEntry,
       "integraWifPortStcIndex": integraWifPortStcIndex,
       "integraWifPortStcDescr": integraWifPortStcDescr,
       "integraWifTimePassed": integraWifTimePassed,
       "integraWrxDetected": integraWrxDetected,
       "integraWrxDropped": integraWrxDropped,
       "integraWtxDetected": integraWtxDetected,
       "integraWtxDropped": integraWtxDropped,
       "integraWrxBytes": integraWrxBytes,
       "integraWtxBytes": integraWtxBytes,
       "integraWrx64Frames": integraWrx64Frames,
       "integraWrx65to127Frames": integraWrx65to127Frames,
       "integraWrx128to255Frames": integraWrx128to255Frames,
       "integraWrx256to511Frames": integraWrx256to511Frames,
       "integraWrx512to1023Frames": integraWrx512to1023Frames,
       "integraWrx1024toMaxFrames": integraWrx1024toMaxFrames,
       "integraWrxUsizeFrames": integraWrxUsizeFrames,
       "integraWrxOsizeFrames": integraWrxOsizeFrames,
       "integraWtx64Frames": integraWtx64Frames,
       "integraWtx65to127Frames": integraWtx65to127Frames,
       "integraWtx128to255Frames": integraWtx128to255Frames,
       "integraWtx256to511Frames": integraWtx256to511Frames,
       "integraWtx512to1023Frames": integraWtx512to1023Frames,
       "integraWtx1024toMaxFrames": integraWtx1024toMaxFrames,
       "integraWtxUsizeFrames": integraWtxUsizeFrames,
       "integraWtxOsizeFrames": integraWtxOsizeFrames,
       "integraWrxGoodFrames": integraWrxGoodFrames,
       "integraWrxErrors": integraWrxErrors,
       "integraWrxFifoErr": integraWrxFifoErr,
       "integraWrxCRCErrors": integraWrxCRCErrors,
       "integraWrxBcastFrames": integraWrxBcastFrames,
       "integraWrxMcastFrames": integraWrxMcastFrames,
       "integraWrxCntrlFrames": integraWrxCntrlFrames,
       "integraWrxLenErrors": integraWrxLenErrors,
       "integraWrxVlanFrames": integraWrxVlanFrames,
       "integraWrxPauseFrames": integraWrxPauseFrames,
       "integraWrxOpErrors": integraWrxOpErrors,
       "integraWrxFrameErrors": integraWrxFrameErrors,
       "integraWtxGoodFrames": integraWtxGoodFrames,
       "integraWtxErrors": integraWtxErrors,
       "integraWtxFifoErr": integraWtxFifoErr,
       "integraWtxBcastFrames": integraWtxBcastFrames,
       "integraWtxMcastFrames": integraWtxMcastFrames,
       "integraWtxUrunErrors": integraWtxUrunErrors,
       "integraWtxCntrlFrames": integraWtxCntrlFrames,
       "integraWtxVlanFrames": integraWtxVlanFrames,
       "integraWtxPauseFrames": integraWtxPauseFrames,
       "integraWtxSingleCollisions": integraWtxSingleCollisions,
       "integraWtxMultiCollisions": integraWtxMultiCollisions,
       "integraWtxDeferred": integraWtxDeferred,
       "integraWtxLateCollisions": integraWtxLateCollisions,
       "integraWtxExcessCollisions": integraWtxExcessCollisions,
       "integraWtxExcessDeferral": integraWtxExcessDeferral,
       "integraWtxAlignErrors": integraWtxAlignErrors,
       "integraWtxCarrierErrors": integraWtxCarrierErrors,
       "integraWtxCollisions": integraWtxCollisions,
       "integraWexecuteConfig": integraWexecuteConfig,
       "integraWneedStore": integraWneedStore,
       "integraWstoreConfig": integraWstoreConfig,
       "integraWnetCfg": integraWnetCfg,
       "integraWnetCfgIPaddress": integraWnetCfgIPaddress,
       "integraWnetCfgIPmask": integraWnetCfgIPmask,
       "integraWnetCfgIPgateway": integraWnetCfgIPgateway,
       "integraWnetCfgRemoteIPaddress": integraWnetCfgRemoteIPaddress,
       "integraWConformance": integraWConformance,
       "integraWCompliances": integraWCompliances,
       "integraWCompliance": integraWCompliance,
       "integraWGroups": integraWGroups,
       "integraWMiscGroup": integraWMiscGroup,
       "integraWRadioGroup": integraWRadioGroup,
       "integraWModemGroup": integraWModemGroup,
       "integraWSystemGroup": integraWSystemGroup,
       "integraWEthernetGeneralGroup": integraWEthernetGeneralGroup,
       "integraWEthernetMiiPortGroup": integraWEthernetMiiPortGroup}
)
