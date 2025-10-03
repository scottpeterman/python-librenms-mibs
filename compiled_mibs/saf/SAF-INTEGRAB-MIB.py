# SNMP MIB module (SAF-INTEGRAB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\saf\SAF-INTEGRAB-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:24:42 2025
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

integraB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    integraB.setRevisions(
        ("2015-09-17 00:00",
         "2015-09-15 00:00",
         "2015-08-12 00:00",
         "2015-07-20 00:00",
         "2015-05-20 00:00",
         "2015-04-14 00:00",
         "2015-03-24 00:00",
         "2015-02-10 00:00",
         "2015-02-04 00:00",
         "2015-01-12 00:00",
         "2015-01-08 00:00",
         "2015-01-06 00:00",
         "2014-12-18 00:00",
         "2014-12-12 00:00",
         "2014-12-10 00:00",
         "2014-12-09 00:00",
         "2014-11-22 00:00",
         "2014-10-29 00:00",
         "2014-09-04 00:00",
         "2014-08-01 00:00",
         "2014-06-11 00:00",
         "2014-04-16 00:00",
         "2014-02-12 00:00",
         "2014-02-11 00:00",
         "2014-01-30 00:00",
         "2014-01-29 00:00",
         "2013-12-18 00:00",
         "2013-12-09 00:00",
         "2013-12-05 00:00",
         "2013-09-27 00:00",
         "2013-09-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IntegraBtimestamp_Type = DateAndTime
_IntegraBtimestamp_Object = MibScalar
integraBtimestamp = _IntegraBtimestamp_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 1),
    _IntegraBtimestamp_Type()
)
integraBtimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBtimestamp.setStatus("current")
_IntegraBradio_ObjectIdentity = ObjectIdentity
integraBradio = _IntegraBradio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 2)
)
_IntegraBradioTxPower_Type = Integer32
_IntegraBradioTxPower_Object = MibScalar
integraBradioTxPower = _IntegraBradioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 2, 1),
    _IntegraBradioTxPower_Type()
)
integraBradioTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraBradioTxPower.setStatus("current")
if mibBuilder.loadTexts:
    integraBradioTxPower.setUnits("dBm")
_IntegraBradioTxFrequency_Type = Integer32
_IntegraBradioTxFrequency_Object = MibScalar
integraBradioTxFrequency = _IntegraBradioTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 2, 2),
    _IntegraBradioTxFrequency_Type()
)
integraBradioTxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraBradioTxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    integraBradioTxFrequency.setUnits("kHz")
_IntegraBradioRxLevel_Type = Integer32
_IntegraBradioRxLevel_Object = MibScalar
integraBradioRxLevel = _IntegraBradioRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 2, 3),
    _IntegraBradioRxLevel_Type()
)
integraBradioRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBradioRxLevel.setStatus("current")
if mibBuilder.loadTexts:
    integraBradioRxLevel.setUnits("dBm")


class _IntegraBradioSide_Type(Integer32):
    """Custom type integraBradioSide based on Integer32"""
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


_IntegraBradioSide_Type.__name__ = "Integer32"
_IntegraBradioSide_Object = MibScalar
integraBradioSide = _IntegraBradioSide_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 2, 4),
    _IntegraBradioSide_Type()
)
integraBradioSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBradioSide.setStatus("current")


class _IntegraBradioTxMute_Type(Integer32):
    """Custom type integraBradioTxMute based on Integer32"""
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


_IntegraBradioTxMute_Type.__name__ = "Integer32"
_IntegraBradioTxMute_Object = MibScalar
integraBradioTxMute = _IntegraBradioTxMute_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 2, 5),
    _IntegraBradioTxMute_Type()
)
integraBradioTxMute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBradioTxMute.setStatus("current")
_IntegraBradioDuplexShift_Type = Integer32
_IntegraBradioDuplexShift_Object = MibScalar
integraBradioDuplexShift = _IntegraBradioDuplexShift_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 2, 6),
    _IntegraBradioDuplexShift_Type()
)
integraBradioDuplexShift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBradioDuplexShift.setStatus("current")
if mibBuilder.loadTexts:
    integraBradioDuplexShift.setUnits("kHz")
_IntegraBradioRxFrequency_Type = Integer32
_IntegraBradioRxFrequency_Object = MibScalar
integraBradioRxFrequency = _IntegraBradioRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 2, 7),
    _IntegraBradioRxFrequency_Type()
)
integraBradioRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBradioRxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    integraBradioRxFrequency.setUnits("kHz")
_IntegraBradioTemperature_Type = Integer32
_IntegraBradioTemperature_Object = MibScalar
integraBradioTemperature = _IntegraBradioTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 2, 8),
    _IntegraBradioTemperature_Type()
)
integraBradioTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBradioTemperature.setStatus("current")
if mibBuilder.loadTexts:
    integraBradioTemperature.setUnits("C")


class _IntegraBradioTxMuteDuration_Type(Integer32):
    """Custom type integraBradioTxMuteDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214748364),
    )


_IntegraBradioTxMuteDuration_Type.__name__ = "Integer32"
_IntegraBradioTxMuteDuration_Object = MibScalar
integraBradioTxMuteDuration = _IntegraBradioTxMuteDuration_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 2, 9),
    _IntegraBradioTxMuteDuration_Type()
)
integraBradioTxMuteDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraBradioTxMuteDuration.setStatus("current")
if mibBuilder.loadTexts:
    integraBradioTxMuteDuration.setUnits("s")
_IntegraBradioRangesTable_Object = MibTable
integraBradioRangesTable = _IntegraBradioRangesTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 2, 10)
)
if mibBuilder.loadTexts:
    integraBradioRangesTable.setStatus("current")
_IntegraBradioRangeEntry_Object = MibTableRow
integraBradioRangeEntry = _IntegraBradioRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 2, 10, 1)
)
integraBradioRangeEntry.setIndexNames(
    (0, "SAF-INTEGRAB-MIB", "integraBradioRangeEntryIndex"),
)
if mibBuilder.loadTexts:
    integraBradioRangeEntry.setStatus("current")


class _IntegraBradioRangeEntryIndex_Type(Integer32):
    """Custom type integraBradioRangeEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IntegraBradioRangeEntryIndex_Type.__name__ = "Integer32"
_IntegraBradioRangeEntryIndex_Object = MibTableColumn
integraBradioRangeEntryIndex = _IntegraBradioRangeEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 2, 10, 1, 1),
    _IntegraBradioRangeEntryIndex_Type()
)
integraBradioRangeEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBradioRangeEntryIndex.setStatus("current")


class _IntegraBradioRangeDescr_Type(DisplayString):
    """Custom type integraBradioRangeDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntegraBradioRangeDescr_Type.__name__ = "DisplayString"
_IntegraBradioRangeDescr_Object = MibTableColumn
integraBradioRangeDescr = _IntegraBradioRangeDescr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 2, 10, 1, 2),
    _IntegraBradioRangeDescr_Type()
)
integraBradioRangeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBradioRangeDescr.setStatus("current")
_IntegraBradioRangeTxPower_Type = Integer32
_IntegraBradioRangeTxPower_Object = MibTableColumn
integraBradioRangeTxPower = _IntegraBradioRangeTxPower_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 2, 10, 1, 3),
    _IntegraBradioRangeTxPower_Type()
)
integraBradioRangeTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBradioRangeTxPower.setStatus("current")
if mibBuilder.loadTexts:
    integraBradioRangeTxPower.setUnits("dBm")
_IntegraBradioRangeTxFrequency_Type = Integer32
_IntegraBradioRangeTxFrequency_Object = MibTableColumn
integraBradioRangeTxFrequency = _IntegraBradioRangeTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 2, 10, 1, 4),
    _IntegraBradioRangeTxFrequency_Type()
)
integraBradioRangeTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBradioRangeTxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    integraBradioRangeTxFrequency.setUnits("kHz")


class _IntegraBradioPLL_Type(Integer32):
    """Custom type integraBradioPLL based on Integer32"""
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


_IntegraBradioPLL_Type.__name__ = "Integer32"
_IntegraBradioPLL_Object = MibScalar
integraBradioPLL = _IntegraBradioPLL_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 2, 11),
    _IntegraBradioPLL_Type()
)
integraBradioPLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBradioPLL.setStatus("current")
_IntegraBmodem_ObjectIdentity = ObjectIdentity
integraBmodem = _IntegraBmodem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 3)
)


class _IntegraBmodemAcquireStatus_Type(Integer32):
    """Custom type integraBmodemAcquireStatus based on Integer32"""
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


_IntegraBmodemAcquireStatus_Type.__name__ = "Integer32"
_IntegraBmodemAcquireStatus_Object = MibScalar
integraBmodemAcquireStatus = _IntegraBmodemAcquireStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 3, 1),
    _IntegraBmodemAcquireStatus_Type()
)
integraBmodemAcquireStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBmodemAcquireStatus.setStatus("current")
_IntegraBmodemRadialMse_Type = Integer32
_IntegraBmodemRadialMse_Object = MibScalar
integraBmodemRadialMse = _IntegraBmodemRadialMse_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 3, 2),
    _IntegraBmodemRadialMse_Type()
)
integraBmodemRadialMse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBmodemRadialMse.setStatus("current")
if mibBuilder.loadTexts:
    integraBmodemRadialMse.setUnits("dB")
_IntegraBmodemFECload_Type = DisplayString
_IntegraBmodemFECload_Object = MibScalar
integraBmodemFECload = _IntegraBmodemFECload_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 3, 3),
    _IntegraBmodemFECload_Type()
)
integraBmodemFECload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBmodemFECload.setStatus("current")


class _IntegraBmodemAcquireLastStatusDetails_Type(Integer32):
    """Custom type integraBmodemAcquireLastStatusDetails based on Integer32"""
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


_IntegraBmodemAcquireLastStatusDetails_Type.__name__ = "Integer32"
_IntegraBmodemAcquireLastStatusDetails_Object = MibScalar
integraBmodemAcquireLastStatusDetails = _IntegraBmodemAcquireLastStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 3, 4),
    _IntegraBmodemAcquireLastStatusDetails_Type()
)
integraBmodemAcquireLastStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBmodemAcquireLastStatusDetails.setStatus("current")
_IntegraBmodemTemperature_Type = Integer32
_IntegraBmodemTemperature_Object = MibScalar
integraBmodemTemperature = _IntegraBmodemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 3, 5),
    _IntegraBmodemTemperature_Type()
)
integraBmodemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBmodemTemperature.setStatus("current")
if mibBuilder.loadTexts:
    integraBmodemTemperature.setUnits("C")
_IntegraBmodemBandwidth_Type = Integer32
_IntegraBmodemBandwidth_Object = MibScalar
integraBmodemBandwidth = _IntegraBmodemBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 3, 6),
    _IntegraBmodemBandwidth_Type()
)
integraBmodemBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBmodemBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    integraBmodemBandwidth.setUnits("kHz")
_IntegraBmodemModulation_Type = DisplayString
_IntegraBmodemModulation_Object = MibScalar
integraBmodemModulation = _IntegraBmodemModulation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 3, 7),
    _IntegraBmodemModulation_Type()
)
integraBmodemModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBmodemModulation.setStatus("current")
_IntegraBmodemRxModulation_Type = DisplayString
_IntegraBmodemRxModulation_Object = MibScalar
integraBmodemRxModulation = _IntegraBmodemRxModulation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 3, 8),
    _IntegraBmodemRxModulation_Type()
)
integraBmodemRxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBmodemRxModulation.setStatus("current")
_IntegraBmodemTxModulation_Type = DisplayString
_IntegraBmodemTxModulation_Object = MibScalar
integraBmodemTxModulation = _IntegraBmodemTxModulation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 3, 9),
    _IntegraBmodemTxModulation_Type()
)
integraBmodemTxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBmodemTxModulation.setStatus("current")
_IntegraBmodemRxCapacity_Type = Integer32
_IntegraBmodemRxCapacity_Object = MibScalar
integraBmodemRxCapacity = _IntegraBmodemRxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 3, 10),
    _IntegraBmodemRxCapacity_Type()
)
integraBmodemRxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBmodemRxCapacity.setStatus("current")
if mibBuilder.loadTexts:
    integraBmodemRxCapacity.setUnits("kb/s")
_IntegraBmodemTxCapacity_Type = Integer32
_IntegraBmodemTxCapacity_Object = MibScalar
integraBmodemTxCapacity = _IntegraBmodemTxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 3, 11),
    _IntegraBmodemTxCapacity_Type()
)
integraBmodemTxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBmodemTxCapacity.setStatus("current")
if mibBuilder.loadTexts:
    integraBmodemTxCapacity.setUnits("kb/s")


class _IntegraBmodemACMengine_Type(Integer32):
    """Custom type integraBmodemACMengine based on Integer32"""
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


_IntegraBmodemACMengine_Type.__name__ = "Integer32"
_IntegraBmodemACMengine_Object = MibScalar
integraBmodemACMengine = _IntegraBmodemACMengine_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 3, 12),
    _IntegraBmodemACMengine_Type()
)
integraBmodemACMengine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBmodemACMengine.setStatus("current")
_IntegraBmodemCarrierOffset_Type = Integer32
_IntegraBmodemCarrierOffset_Object = MibScalar
integraBmodemCarrierOffset = _IntegraBmodemCarrierOffset_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 3, 13),
    _IntegraBmodemCarrierOffset_Type()
)
integraBmodemCarrierOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBmodemCarrierOffset.setStatus("current")
if mibBuilder.loadTexts:
    integraBmodemCarrierOffset.setUnits("Hz")
_IntegraBsystem_ObjectIdentity = ObjectIdentity
integraBsystem = _IntegraBsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 4)
)
_IntegraBsysCPUtemperature_Type = Integer32
_IntegraBsysCPUtemperature_Object = MibScalar
integraBsysCPUtemperature = _IntegraBsysCPUtemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 4, 2),
    _IntegraBsysCPUtemperature_Type()
)
integraBsysCPUtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBsysCPUtemperature.setStatus("current")
if mibBuilder.loadTexts:
    integraBsysCPUtemperature.setUnits("C")
_IntegraBsysLicenseExpire_Type = Gauge32
_IntegraBsysLicenseExpire_Object = MibScalar
integraBsysLicenseExpire = _IntegraBsysLicenseExpire_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 4, 3),
    _IntegraBsysLicenseExpire_Type()
)
integraBsysLicenseExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBsysLicenseExpire.setStatus("current")
if mibBuilder.loadTexts:
    integraBsysLicenseExpire.setUnits("s")


class _IntegraBsysLicenseGenStatus_Type(Integer32):
    """Custom type integraBsysLicenseGenStatus based on Integer32"""
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


_IntegraBsysLicenseGenStatus_Type.__name__ = "Integer32"
_IntegraBsysLicenseGenStatus_Object = MibScalar
integraBsysLicenseGenStatus = _IntegraBsysLicenseGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 4, 4),
    _IntegraBsysLicenseGenStatus_Type()
)
integraBsysLicenseGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBsysLicenseGenStatus.setStatus("current")
_IntegraBsysPSUvoltage_Type = Integer32
_IntegraBsysPSUvoltage_Object = MibScalar
integraBsysPSUvoltage = _IntegraBsysPSUvoltage_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 4, 5),
    _IntegraBsysPSUvoltage_Type()
)
integraBsysPSUvoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBsysPSUvoltage.setStatus("current")
if mibBuilder.loadTexts:
    integraBsysPSUvoltage.setUnits("mV")
_IntegraBsysPSUcurrent_Type = Integer32
_IntegraBsysPSUcurrent_Object = MibScalar
integraBsysPSUcurrent = _IntegraBsysPSUcurrent_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 4, 6),
    _IntegraBsysPSUcurrent_Type()
)
integraBsysPSUcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBsysPSUcurrent.setStatus("current")
if mibBuilder.loadTexts:
    integraBsysPSUcurrent.setUnits("mA")
_IntegraBsysPSUpower_Type = Integer32
_IntegraBsysPSUpower_Object = MibScalar
integraBsysPSUpower = _IntegraBsysPSUpower_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 4, 7),
    _IntegraBsysPSUpower_Type()
)
integraBsysPSUpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBsysPSUpower.setStatus("current")
if mibBuilder.loadTexts:
    integraBsysPSUpower.setUnits("mW")
_IntegraBsysBoardTemperature_Type = Integer32
_IntegraBsysBoardTemperature_Object = MibScalar
integraBsysBoardTemperature = _IntegraBsysBoardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 4, 8),
    _IntegraBsysBoardTemperature_Type()
)
integraBsysBoardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBsysBoardTemperature.setStatus("current")
if mibBuilder.loadTexts:
    integraBsysBoardTemperature.setUnits("C")
_IntegraBsysFreeMemory_Type = Integer32
_IntegraBsysFreeMemory_Object = MibScalar
integraBsysFreeMemory = _IntegraBsysFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 4, 9),
    _IntegraBsysFreeMemory_Type()
)
integraBsysFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBsysFreeMemory.setStatus("current")
if mibBuilder.loadTexts:
    integraBsysFreeMemory.setUnits("%")
_IntegraBsysCPUidle_Type = Integer32
_IntegraBsysCPUidle_Object = MibScalar
integraBsysCPUidle = _IntegraBsysCPUidle_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 4, 10),
    _IntegraBsysCPUidle_Type()
)
integraBsysCPUidle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBsysCPUidle.setStatus("current")
if mibBuilder.loadTexts:
    integraBsysCPUidle.setUnits("%")
_IntegraBethernet_ObjectIdentity = ObjectIdentity
integraBethernet = _IntegraBethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5)
)
_IntegraBifStatusTable_Object = MibTable
integraBifStatusTable = _IntegraBifStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 1)
)
if mibBuilder.loadTexts:
    integraBifStatusTable.setStatus("current")
_IntegraBifPortEntry_Object = MibTableRow
integraBifPortEntry = _IntegraBifPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 1, 1)
)
integraBifPortEntry.setIndexNames(
    (0, "SAF-INTEGRAB-MIB", "integraBifPortStatIndex"),
)
if mibBuilder.loadTexts:
    integraBifPortEntry.setStatus("current")


class _IntegraBifPortStatIndex_Type(Integer32):
    """Custom type integraBifPortStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IntegraBifPortStatIndex_Type.__name__ = "Integer32"
_IntegraBifPortStatIndex_Object = MibTableColumn
integraBifPortStatIndex = _IntegraBifPortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 1, 1, 1),
    _IntegraBifPortStatIndex_Type()
)
integraBifPortStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPortStatIndex.setStatus("current")


class _IntegraBifPortStatDescr_Type(DisplayString):
    """Custom type integraBifPortStatDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntegraBifPortStatDescr_Type.__name__ = "DisplayString"
_IntegraBifPortStatDescr_Object = MibTableColumn
integraBifPortStatDescr = _IntegraBifPortStatDescr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 1, 1, 2),
    _IntegraBifPortStatDescr_Type()
)
integraBifPortStatDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPortStatDescr.setStatus("current")
_IntegraBifPortType_Type = IANAifType
_IntegraBifPortType_Object = MibTableColumn
integraBifPortType = _IntegraBifPortType_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 1, 1, 3),
    _IntegraBifPortType_Type()
)
integraBifPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPortType.setStatus("current")
_IntegraBifPortMtu_Type = Integer32
_IntegraBifPortMtu_Object = MibTableColumn
integraBifPortMtu = _IntegraBifPortMtu_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 1, 1, 4),
    _IntegraBifPortMtu_Type()
)
integraBifPortMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPortMtu.setStatus("current")
if mibBuilder.loadTexts:
    integraBifPortMtu.setUnits("B")
_IntegraBifPortSpeed_Type = Gauge32
_IntegraBifPortSpeed_Object = MibTableColumn
integraBifPortSpeed = _IntegraBifPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 1, 1, 5),
    _IntegraBifPortSpeed_Type()
)
integraBifPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPortSpeed.setStatus("current")
if mibBuilder.loadTexts:
    integraBifPortSpeed.setUnits("bps")
_IntegraBifPortPhysAddress_Type = PhysAddress
_IntegraBifPortPhysAddress_Object = MibTableColumn
integraBifPortPhysAddress = _IntegraBifPortPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 1, 1, 6),
    _IntegraBifPortPhysAddress_Type()
)
integraBifPortPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPortPhysAddress.setStatus("current")


class _IntegraBifPortAdminStatus_Type(Integer32):
    """Custom type integraBifPortAdminStatus based on Integer32"""
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


_IntegraBifPortAdminStatus_Type.__name__ = "Integer32"
_IntegraBifPortAdminStatus_Object = MibTableColumn
integraBifPortAdminStatus = _IntegraBifPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 1, 1, 7),
    _IntegraBifPortAdminStatus_Type()
)
integraBifPortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPortAdminStatus.setStatus("current")


class _IntegraBifPortOperStatus_Type(Integer32):
    """Custom type integraBifPortOperStatus based on Integer32"""
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


_IntegraBifPortOperStatus_Type.__name__ = "Integer32"
_IntegraBifPortOperStatus_Object = MibTableColumn
integraBifPortOperStatus = _IntegraBifPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 1, 1, 8),
    _IntegraBifPortOperStatus_Type()
)
integraBifPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPortOperStatus.setStatus("current")
_IntegraBifPortLastChange_Type = TimeTicks
_IntegraBifPortLastChange_Object = MibTableColumn
integraBifPortLastChange = _IntegraBifPortLastChange_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 1, 1, 9),
    _IntegraBifPortLastChange_Type()
)
integraBifPortLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPortLastChange.setStatus("current")


class _IntegraBifPortAutoneg_Type(Integer32):
    """Custom type integraBifPortAutoneg based on Integer32"""
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


_IntegraBifPortAutoneg_Type.__name__ = "Integer32"
_IntegraBifPortAutoneg_Object = MibTableColumn
integraBifPortAutoneg = _IntegraBifPortAutoneg_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 1, 1, 10),
    _IntegraBifPortAutoneg_Type()
)
integraBifPortAutoneg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPortAutoneg.setStatus("current")


class _IntegraBifPortDuplex_Type(Integer32):
    """Custom type integraBifPortDuplex based on Integer32"""
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


_IntegraBifPortDuplex_Type.__name__ = "Integer32"
_IntegraBifPortDuplex_Object = MibTableColumn
integraBifPortDuplex = _IntegraBifPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 1, 1, 11),
    _IntegraBifPortDuplex_Type()
)
integraBifPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPortDuplex.setStatus("current")


class _IntegraBifPortSyncEthActive_Type(Integer32):
    """Custom type integraBifPortSyncEthActive based on Integer32"""
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


_IntegraBifPortSyncEthActive_Type.__name__ = "Integer32"
_IntegraBifPortSyncEthActive_Object = MibTableColumn
integraBifPortSyncEthActive = _IntegraBifPortSyncEthActive_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 1, 1, 12),
    _IntegraBifPortSyncEthActive_Type()
)
integraBifPortSyncEthActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPortSyncEthActive.setStatus("current")
_IntegraBifPortSyncEthPrio_Type = Integer32
_IntegraBifPortSyncEthPrio_Object = MibTableColumn
integraBifPortSyncEthPrio = _IntegraBifPortSyncEthPrio_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 1, 1, 13),
    _IntegraBifPortSyncEthPrio_Type()
)
integraBifPortSyncEthPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPortSyncEthPrio.setStatus("current")


class _IntegraBifPortFlowControl_Type(Integer32):
    """Custom type integraBifPortFlowControl based on Integer32"""
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


_IntegraBifPortFlowControl_Type.__name__ = "Integer32"
_IntegraBifPortFlowControl_Object = MibTableColumn
integraBifPortFlowControl = _IntegraBifPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 1, 1, 14),
    _IntegraBifPortFlowControl_Type()
)
integraBifPortFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPortFlowControl.setStatus("current")
_IntegraBifStatisticsTable_Object = MibTable
integraBifStatisticsTable = _IntegraBifStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2)
)
if mibBuilder.loadTexts:
    integraBifStatisticsTable.setStatus("current")
_IntegraBifPortStcEntry_Object = MibTableRow
integraBifPortStcEntry = _IntegraBifPortStcEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1)
)
integraBifPortStcEntry.setIndexNames(
    (0, "SAF-INTEGRAB-MIB", "integraBifPortStcIndex"),
)
if mibBuilder.loadTexts:
    integraBifPortStcEntry.setStatus("current")


class _IntegraBifPortStcIndex_Type(Integer32):
    """Custom type integraBifPortStcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IntegraBifPortStcIndex_Type.__name__ = "Integer32"
_IntegraBifPortStcIndex_Object = MibTableColumn
integraBifPortStcIndex = _IntegraBifPortStcIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 1),
    _IntegraBifPortStcIndex_Type()
)
integraBifPortStcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPortStcIndex.setStatus("current")


class _IntegraBifPortStcDescr_Type(DisplayString):
    """Custom type integraBifPortStcDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntegraBifPortStcDescr_Type.__name__ = "DisplayString"
_IntegraBifPortStcDescr_Object = MibTableColumn
integraBifPortStcDescr = _IntegraBifPortStcDescr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 2),
    _IntegraBifPortStcDescr_Type()
)
integraBifPortStcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPortStcDescr.setStatus("current")
_IntegraBifTimePassed_Type = TimeTicks
_IntegraBifTimePassed_Object = MibTableColumn
integraBifTimePassed = _IntegraBifTimePassed_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 3),
    _IntegraBifTimePassed_Type()
)
integraBifTimePassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifTimePassed.setStatus("current")
if mibBuilder.loadTexts:
    integraBifTimePassed.setUnits("s/100")
_IntegraBifIngressPackets_Type = Counter64
_IntegraBifIngressPackets_Object = MibTableColumn
integraBifIngressPackets = _IntegraBifIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 4),
    _IntegraBifIngressPackets_Type()
)
integraBifIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifIngressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifIngressPackets.setUnits("packet")
_IntegraBifIngressBytes_Type = Counter64
_IntegraBifIngressBytes_Object = MibTableColumn
integraBifIngressBytes = _IntegraBifIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 5),
    _IntegraBifIngressBytes_Type()
)
integraBifIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifIngressBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraBifIngressBytes.setUnits("B")
_IntegraBifEgressPackets_Type = Counter64
_IntegraBifEgressPackets_Object = MibTableColumn
integraBifEgressPackets = _IntegraBifEgressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 6),
    _IntegraBifEgressPackets_Type()
)
integraBifEgressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEgressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEgressPackets.setUnits("packet")
_IntegraBifEgressBytes_Type = Counter64
_IntegraBifEgressBytes_Object = MibTableColumn
integraBifEgressBytes = _IntegraBifEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 7),
    _IntegraBifEgressBytes_Type()
)
integraBifEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEgressBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEgressBytes.setUnits("B")
_IntegraBifEtherStatsMulticastPkts_Type = Counter64
_IntegraBifEtherStatsMulticastPkts_Object = MibTableColumn
integraBifEtherStatsMulticastPkts = _IntegraBifEtherStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 8),
    _IntegraBifEtherStatsMulticastPkts_Type()
)
integraBifEtherStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherStatsMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherStatsMulticastPkts.setUnits("packet")
_IntegraBifEtherStatsBroadcastPkts_Type = Counter64
_IntegraBifEtherStatsBroadcastPkts_Object = MibTableColumn
integraBifEtherStatsBroadcastPkts = _IntegraBifEtherStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 9),
    _IntegraBifEtherStatsBroadcastPkts_Type()
)
integraBifEtherStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherStatsBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherStatsBroadcastPkts.setUnits("packet")
_IntegraBifEtherStatsPkts64Octets_Type = Counter64
_IntegraBifEtherStatsPkts64Octets_Object = MibTableColumn
integraBifEtherStatsPkts64Octets = _IntegraBifEtherStatsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 10),
    _IntegraBifEtherStatsPkts64Octets_Type()
)
integraBifEtherStatsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherStatsPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherStatsPkts64Octets.setUnits("packet")
_IntegraBifEtherStatsPkts65to127Octets_Type = Counter64
_IntegraBifEtherStatsPkts65to127Octets_Object = MibTableColumn
integraBifEtherStatsPkts65to127Octets = _IntegraBifEtherStatsPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 11),
    _IntegraBifEtherStatsPkts65to127Octets_Type()
)
integraBifEtherStatsPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherStatsPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherStatsPkts65to127Octets.setUnits("packet")
_IntegraBifEtherStatsPkts128to255Octets_Type = Counter64
_IntegraBifEtherStatsPkts128to255Octets_Object = MibTableColumn
integraBifEtherStatsPkts128to255Octets = _IntegraBifEtherStatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 12),
    _IntegraBifEtherStatsPkts128to255Octets_Type()
)
integraBifEtherStatsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherStatsPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherStatsPkts128to255Octets.setUnits("packet")
_IntegraBifEtherStatsPkts256to511Octets_Type = Counter64
_IntegraBifEtherStatsPkts256to511Octets_Object = MibTableColumn
integraBifEtherStatsPkts256to511Octets = _IntegraBifEtherStatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 13),
    _IntegraBifEtherStatsPkts256to511Octets_Type()
)
integraBifEtherStatsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherStatsPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherStatsPkts256to511Octets.setUnits("packet")
_IntegraBifEtherStatsPkts512to1023Octets_Type = Counter64
_IntegraBifEtherStatsPkts512to1023Octets_Object = MibTableColumn
integraBifEtherStatsPkts512to1023Octets = _IntegraBifEtherStatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 14),
    _IntegraBifEtherStatsPkts512to1023Octets_Type()
)
integraBifEtherStatsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherStatsPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherStatsPkts512to1023Octets.setUnits("packet")
_IntegraBifEtherStatsPkts1024to1518Octets_Type = Counter64
_IntegraBifEtherStatsPkts1024to1518Octets_Object = MibTableColumn
integraBifEtherStatsPkts1024to1518Octets = _IntegraBifEtherStatsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 15),
    _IntegraBifEtherStatsPkts1024to1518Octets_Type()
)
integraBifEtherStatsPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherStatsPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherStatsPkts1024to1518Octets.setUnits("packet")
_IntegraBifEtherStatsOversizePkts_Type = Counter64
_IntegraBifEtherStatsOversizePkts_Object = MibTableColumn
integraBifEtherStatsOversizePkts = _IntegraBifEtherStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 16),
    _IntegraBifEtherStatsOversizePkts_Type()
)
integraBifEtherStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherStatsOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherStatsOversizePkts.setUnits("packet")
_IntegraBifEtherRxOversizePkts_Type = Counter64
_IntegraBifEtherRxOversizePkts_Object = MibTableColumn
integraBifEtherRxOversizePkts = _IntegraBifEtherRxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 17),
    _IntegraBifEtherRxOversizePkts_Type()
)
integraBifEtherRxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherRxOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherRxOversizePkts.setUnits("packet")
_IntegraBifEtherTxOversizePkts_Type = Counter64
_IntegraBifEtherTxOversizePkts_Object = MibTableColumn
integraBifEtherTxOversizePkts = _IntegraBifEtherTxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 18),
    _IntegraBifEtherTxOversizePkts_Type()
)
integraBifEtherTxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherTxOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherTxOversizePkts.setUnits("packet")
_IntegraBifEtherStatsOctets_Type = Counter64
_IntegraBifEtherStatsOctets_Object = MibTableColumn
integraBifEtherStatsOctets = _IntegraBifEtherStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 19),
    _IntegraBifEtherStatsOctets_Type()
)
integraBifEtherStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherStatsOctets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherStatsOctets.setUnits("packet")
_IntegraBifEtherStatsPkts_Type = Counter64
_IntegraBifEtherStatsPkts_Object = MibTableColumn
integraBifEtherStatsPkts = _IntegraBifEtherStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 20),
    _IntegraBifEtherStatsPkts_Type()
)
integraBifEtherStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherStatsPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherStatsPkts.setUnits("packet")
_IntegraBifEtherStatsTXNoErrors_Type = Counter64
_IntegraBifEtherStatsTXNoErrors_Object = MibTableColumn
integraBifEtherStatsTXNoErrors = _IntegraBifEtherStatsTXNoErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 21),
    _IntegraBifEtherStatsTXNoErrors_Type()
)
integraBifEtherStatsTXNoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherStatsTXNoErrors.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherStatsTXNoErrors.setUnits("packet")
_IntegraBifEtherStatsRXNoErrors_Type = Counter64
_IntegraBifEtherStatsRXNoErrors_Object = MibTableColumn
integraBifEtherStatsRXNoErrors = _IntegraBifEtherStatsRXNoErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 22),
    _IntegraBifEtherStatsRXNoErrors_Type()
)
integraBifEtherStatsRXNoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherStatsRXNoErrors.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherStatsRXNoErrors.setUnits("packet")
_IntegraBifEtherStatsPkts1519to1522Octets_Type = Counter64
_IntegraBifEtherStatsPkts1519to1522Octets_Object = MibTableColumn
integraBifEtherStatsPkts1519to1522Octets = _IntegraBifEtherStatsPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 23),
    _IntegraBifEtherStatsPkts1519to1522Octets_Type()
)
integraBifEtherStatsPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherStatsPkts1519to1522Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherStatsPkts1519to1522Octets.setUnits("packet")
_IntegraBifIfInOctets_Type = Counter64
_IntegraBifIfInOctets_Object = MibTableColumn
integraBifIfInOctets = _IntegraBifIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 24),
    _IntegraBifIfInOctets_Type()
)
integraBifIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifIfInOctets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifIfInOctets.setUnits("octet")
_IntegraBifIfOutOctets_Type = Counter64
_IntegraBifIfOutOctets_Object = MibTableColumn
integraBifIfOutOctets = _IntegraBifIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 25),
    _IntegraBifIfOutOctets_Type()
)
integraBifIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifIfOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifIfOutOctets.setUnits("octet")
_IntegraBifDot1dTpPortInFrames_Type = Counter64
_IntegraBifDot1dTpPortInFrames_Object = MibTableColumn
integraBifDot1dTpPortInFrames = _IntegraBifDot1dTpPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 26),
    _IntegraBifDot1dTpPortInFrames_Type()
)
integraBifDot1dTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifDot1dTpPortInFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraBifDot1dTpPortInFrames.setUnits("frame")
_IntegraBifDot1dTpPortOutFrames_Type = Counter64
_IntegraBifDot1dTpPortOutFrames_Object = MibTableColumn
integraBifDot1dTpPortOutFrames = _IntegraBifDot1dTpPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 27),
    _IntegraBifDot1dTpPortOutFrames_Type()
)
integraBifDot1dTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifDot1dTpPortOutFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraBifDot1dTpPortOutFrames.setUnits("frame")
_IntegraBifReceivedPkts64Octets_Type = Counter64
_IntegraBifReceivedPkts64Octets_Object = MibTableColumn
integraBifReceivedPkts64Octets = _IntegraBifReceivedPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 28),
    _IntegraBifReceivedPkts64Octets_Type()
)
integraBifReceivedPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifReceivedPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifReceivedPkts64Octets.setUnits("packet")
_IntegraBifTransmittedPkts64Octets_Type = Counter64
_IntegraBifTransmittedPkts64Octets_Object = MibTableColumn
integraBifTransmittedPkts64Octets = _IntegraBifTransmittedPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 29),
    _IntegraBifTransmittedPkts64Octets_Type()
)
integraBifTransmittedPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifTransmittedPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifTransmittedPkts64Octets.setUnits("packet")
_IntegraBifReceivedPkts65to127Octets_Type = Counter64
_IntegraBifReceivedPkts65to127Octets_Object = MibTableColumn
integraBifReceivedPkts65to127Octets = _IntegraBifReceivedPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 30),
    _IntegraBifReceivedPkts65to127Octets_Type()
)
integraBifReceivedPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifReceivedPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifReceivedPkts65to127Octets.setUnits("packet")
_IntegraBifTransmittedPkts65to127Octets_Type = Counter64
_IntegraBifTransmittedPkts65to127Octets_Object = MibTableColumn
integraBifTransmittedPkts65to127Octets = _IntegraBifTransmittedPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 31),
    _IntegraBifTransmittedPkts65to127Octets_Type()
)
integraBifTransmittedPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifTransmittedPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifTransmittedPkts65to127Octets.setUnits("packet")
_IntegraBifReceivedPkts128to255Octets_Type = Counter64
_IntegraBifReceivedPkts128to255Octets_Object = MibTableColumn
integraBifReceivedPkts128to255Octets = _IntegraBifReceivedPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 32),
    _IntegraBifReceivedPkts128to255Octets_Type()
)
integraBifReceivedPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifReceivedPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifReceivedPkts128to255Octets.setUnits("packet")
_IntegraBifTransmittedPkts128to255Octets_Type = Counter64
_IntegraBifTransmittedPkts128to255Octets_Object = MibTableColumn
integraBifTransmittedPkts128to255Octets = _IntegraBifTransmittedPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 33),
    _IntegraBifTransmittedPkts128to255Octets_Type()
)
integraBifTransmittedPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifTransmittedPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifTransmittedPkts128to255Octets.setUnits("packet")
_IntegraBifReceivedPkts256to511Octets_Type = Counter64
_IntegraBifReceivedPkts256to511Octets_Object = MibTableColumn
integraBifReceivedPkts256to511Octets = _IntegraBifReceivedPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 34),
    _IntegraBifReceivedPkts256to511Octets_Type()
)
integraBifReceivedPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifReceivedPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifReceivedPkts256to511Octets.setUnits("packet")
_IntegraBifTransmittedPkts256to511Octets_Type = Counter64
_IntegraBifTransmittedPkts256to511Octets_Object = MibTableColumn
integraBifTransmittedPkts256to511Octets = _IntegraBifTransmittedPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 35),
    _IntegraBifTransmittedPkts256to511Octets_Type()
)
integraBifTransmittedPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifTransmittedPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifTransmittedPkts256to511Octets.setUnits("packet")
_IntegraBifReceivedPkts512to1023Octets_Type = Counter64
_IntegraBifReceivedPkts512to1023Octets_Object = MibTableColumn
integraBifReceivedPkts512to1023Octets = _IntegraBifReceivedPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 36),
    _IntegraBifReceivedPkts512to1023Octets_Type()
)
integraBifReceivedPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifReceivedPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifReceivedPkts512to1023Octets.setUnits("packet")
_IntegraBifTransmittedPkts512to1023Octets_Type = Counter64
_IntegraBifTransmittedPkts512to1023Octets_Object = MibTableColumn
integraBifTransmittedPkts512to1023Octets = _IntegraBifTransmittedPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 37),
    _IntegraBifTransmittedPkts512to1023Octets_Type()
)
integraBifTransmittedPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifTransmittedPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifTransmittedPkts512to1023Octets.setUnits("packet")
_IntegraBifReceivedPkts1024to1518Octets_Type = Counter64
_IntegraBifReceivedPkts1024to1518Octets_Object = MibTableColumn
integraBifReceivedPkts1024to1518Octets = _IntegraBifReceivedPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 38),
    _IntegraBifReceivedPkts1024to1518Octets_Type()
)
integraBifReceivedPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifReceivedPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifReceivedPkts1024to1518Octets.setUnits("packet")
_IntegraBifTransmittedPkts1024to1518Octets_Type = Counter64
_IntegraBifTransmittedPkts1024to1518Octets_Object = MibTableColumn
integraBifTransmittedPkts1024to1518Octets = _IntegraBifTransmittedPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 39),
    _IntegraBifTransmittedPkts1024to1518Octets_Type()
)
integraBifTransmittedPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifTransmittedPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifTransmittedPkts1024to1518Octets.setUnits("packet")
_IntegraBifIfInBroadcastPkts_Type = Counter64
_IntegraBifIfInBroadcastPkts_Object = MibTableColumn
integraBifIfInBroadcastPkts = _IntegraBifIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 40),
    _IntegraBifIfInBroadcastPkts_Type()
)
integraBifIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifIfInBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraBifIfInBroadcastPkts.setUnits("packet")
_IntegraBifIfOutBroadcastPkts_Type = Counter64
_IntegraBifIfOutBroadcastPkts_Object = MibTableColumn
integraBifIfOutBroadcastPkts = _IntegraBifIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 41),
    _IntegraBifIfOutBroadcastPkts_Type()
)
integraBifIfOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifIfOutBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraBifIfOutBroadcastPkts.setUnits("packet")
_IntegraBifIfInMulticastPkts_Type = Counter64
_IntegraBifIfInMulticastPkts_Object = MibTableColumn
integraBifIfInMulticastPkts = _IntegraBifIfInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 42),
    _IntegraBifIfInMulticastPkts_Type()
)
integraBifIfInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifIfInMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraBifIfInMulticastPkts.setUnits("packet")
_IntegraBifIfOutMulticastPkts_Type = Counter64
_IntegraBifIfOutMulticastPkts_Object = MibTableColumn
integraBifIfOutMulticastPkts = _IntegraBifIfOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 43),
    _IntegraBifIfOutMulticastPkts_Type()
)
integraBifIfOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifIfOutMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraBifIfOutMulticastPkts.setUnits("packet")
_IntegraBifDot3InPauseFrames_Type = Counter64
_IntegraBifDot3InPauseFrames_Object = MibTableColumn
integraBifDot3InPauseFrames = _IntegraBifDot3InPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 44),
    _IntegraBifDot3InPauseFrames_Type()
)
integraBifDot3InPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifDot3InPauseFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraBifDot3InPauseFrames.setUnits("frame")
_IntegraBifDot3OutPauseFrames_Type = Counter64
_IntegraBifDot3OutPauseFrames_Object = MibTableColumn
integraBifDot3OutPauseFrames = _IntegraBifDot3OutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 45),
    _IntegraBifDot3OutPauseFrames_Type()
)
integraBifDot3OutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifDot3OutPauseFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraBifDot3OutPauseFrames.setUnits("frame")
_IntegraBifEtherStatsUndersizePkts_Type = Counter64
_IntegraBifEtherStatsUndersizePkts_Object = MibTableColumn
integraBifEtherStatsUndersizePkts = _IntegraBifEtherStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 46),
    _IntegraBifEtherStatsUndersizePkts_Type()
)
integraBifEtherStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherStatsUndersizePkts.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherStatsUndersizePkts.setUnits("packet")
_IntegraBifEtherStatsFragments_Type = Counter64
_IntegraBifEtherStatsFragments_Object = MibTableColumn
integraBifEtherStatsFragments = _IntegraBifEtherStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 47),
    _IntegraBifEtherStatsFragments_Type()
)
integraBifEtherStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherStatsFragments.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherStatsFragments.setUnits("packet")
_IntegraBifEtherStatsCRCAlignErrors_Type = Counter64
_IntegraBifEtherStatsCRCAlignErrors_Object = MibTableColumn
integraBifEtherStatsCRCAlignErrors = _IntegraBifEtherStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 48),
    _IntegraBifEtherStatsCRCAlignErrors_Type()
)
integraBifEtherStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherStatsCRCAlignErrors.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherStatsCRCAlignErrors.setUnits("packet")
_IntegraBifEtherStatsJabbers_Type = Counter64
_IntegraBifEtherStatsJabbers_Object = MibTableColumn
integraBifEtherStatsJabbers = _IntegraBifEtherStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 49),
    _IntegraBifEtherStatsJabbers_Type()
)
integraBifEtherStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEtherStatsJabbers.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEtherStatsJabbers.setUnits("packet")
_IntegraBifIngressBPS_Type = Integer32
_IntegraBifIngressBPS_Object = MibTableColumn
integraBifIngressBPS = _IntegraBifIngressBPS_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 50),
    _IntegraBifIngressBPS_Type()
)
integraBifIngressBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifIngressBPS.setStatus("current")
if mibBuilder.loadTexts:
    integraBifIngressBPS.setUnits("Bps")
_IntegraBifIngressPPS_Type = Integer32
_IntegraBifIngressPPS_Object = MibTableColumn
integraBifIngressPPS = _IntegraBifIngressPPS_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 51),
    _IntegraBifIngressPPS_Type()
)
integraBifIngressPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifIngressPPS.setStatus("current")
if mibBuilder.loadTexts:
    integraBifIngressPPS.setUnits("pps")
_IntegraBifEgressBPS_Type = Integer32
_IntegraBifEgressBPS_Object = MibTableColumn
integraBifEgressBPS = _IntegraBifEgressBPS_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 52),
    _IntegraBifEgressBPS_Type()
)
integraBifEgressBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEgressBPS.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEgressBPS.setUnits("Bps")
_IntegraBifEgressPPS_Type = Integer32
_IntegraBifEgressPPS_Object = MibTableColumn
integraBifEgressPPS = _IntegraBifEgressPPS_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 53),
    _IntegraBifEgressPPS_Type()
)
integraBifEgressPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEgressPPS.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEgressPPS.setUnits("pps")
_IntegraBifMAClearnLimitDropIngressPackets_Type = Counter64
_IntegraBifMAClearnLimitDropIngressPackets_Object = MibTableColumn
integraBifMAClearnLimitDropIngressPackets = _IntegraBifMAClearnLimitDropIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 54),
    _IntegraBifMAClearnLimitDropIngressPackets_Type()
)
integraBifMAClearnLimitDropIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifMAClearnLimitDropIngressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifMAClearnLimitDropIngressPackets.setUnits("packet")
_IntegraBifL2cacheDropIngressPackets_Type = Counter64
_IntegraBifL2cacheDropIngressPackets_Object = MibTableColumn
integraBifL2cacheDropIngressPackets = _IntegraBifL2cacheDropIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 55),
    _IntegraBifL2cacheDropIngressPackets_Type()
)
integraBifL2cacheDropIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifL2cacheDropIngressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifL2cacheDropIngressPackets.setUnits("packet")
_IntegraBifEFMdropIngressPackets_Type = Counter64
_IntegraBifEFMdropIngressPackets_Object = MibTableColumn
integraBifEFMdropIngressPackets = _IntegraBifEFMdropIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 56),
    _IntegraBifEFMdropIngressPackets_Type()
)
integraBifEFMdropIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEFMdropIngressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEFMdropIngressPackets.setUnits("packet")
_IntegraBifEFMdropEgressPackets_Type = Counter64
_IntegraBifEFMdropEgressPackets_Object = MibTableColumn
integraBifEFMdropEgressPackets = _IntegraBifEFMdropEgressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 57),
    _IntegraBifEFMdropEgressPackets_Type()
)
integraBifEFMdropEgressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifEFMdropEgressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifEFMdropEgressPackets.setUnits("packet")
_IntegraBifSTPdropIngressPackets_Type = Counter64
_IntegraBifSTPdropIngressPackets_Object = MibTableColumn
integraBifSTPdropIngressPackets = _IntegraBifSTPdropIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 58),
    _IntegraBifSTPdropIngressPackets_Type()
)
integraBifSTPdropIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifSTPdropIngressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifSTPdropIngressPackets.setUnits("packet")
_IntegraBifSTPdropEgressPackets_Type = Counter64
_IntegraBifSTPdropEgressPackets_Object = MibTableColumn
integraBifSTPdropEgressPackets = _IntegraBifSTPdropEgressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 59),
    _IntegraBifSTPdropEgressPackets_Type()
)
integraBifSTPdropEgressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifSTPdropEgressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifSTPdropEgressPackets.setUnits("packet")
_IntegraBifMRUdropIngressPackets_Type = Counter64
_IntegraBifMRUdropIngressPackets_Object = MibTableColumn
integraBifMRUdropIngressPackets = _IntegraBifMRUdropIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 60),
    _IntegraBifMRUdropIngressPackets_Type()
)
integraBifMRUdropIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifMRUdropIngressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifMRUdropIngressPackets.setUnits("packet")
_IntegraBifMRUdropEgressPackets_Type = Counter64
_IntegraBifMRUdropEgressPackets_Object = MibTableColumn
integraBifMRUdropEgressPackets = _IntegraBifMRUdropEgressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 61),
    _IntegraBifMRUdropEgressPackets_Type()
)
integraBifMRUdropEgressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifMRUdropEgressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifMRUdropEgressPackets.setUnits("packet")
_IntegraBifFilterDropIngressPackets_Type = Counter64
_IntegraBifFilterDropIngressPackets_Object = MibTableColumn
integraBifFilterDropIngressPackets = _IntegraBifFilterDropIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 62),
    _IntegraBifFilterDropIngressPackets_Type()
)
integraBifFilterDropIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifFilterDropIngressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifFilterDropIngressPackets.setUnits("packet")
_IntegraBifFlowClassifierDropIngressPackets_Type = Counter64
_IntegraBifFlowClassifierDropIngressPackets_Object = MibTableColumn
integraBifFlowClassifierDropIngressPackets = _IntegraBifFlowClassifierDropIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 63),
    _IntegraBifFlowClassifierDropIngressPackets_Type()
)
integraBifFlowClassifierDropIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifFlowClassifierDropIngressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifFlowClassifierDropIngressPackets.setUnits("packet")
_IntegraBifFlowClassifierDropEgressPackets_Type = Counter64
_IntegraBifFlowClassifierDropEgressPackets_Object = MibTableColumn
integraBifFlowClassifierDropEgressPackets = _IntegraBifFlowClassifierDropEgressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 64),
    _IntegraBifFlowClassifierDropEgressPackets_Type()
)
integraBifFlowClassifierDropEgressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifFlowClassifierDropEgressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifFlowClassifierDropEgressPackets.setUnits("packet")
_IntegraBifIllegalSAdropIngressPackets_Type = Counter64
_IntegraBifIllegalSAdropIngressPackets_Object = MibTableColumn
integraBifIllegalSAdropIngressPackets = _IntegraBifIllegalSAdropIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 65),
    _IntegraBifIllegalSAdropIngressPackets_Type()
)
integraBifIllegalSAdropIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifIllegalSAdropIngressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifIllegalSAdropIngressPackets.setUnits("packet")
_IntegraBifPortRateLimitDropIngressPackets_Type = Counter64
_IntegraBifPortRateLimitDropIngressPackets_Object = MibTableColumn
integraBifPortRateLimitDropIngressPackets = _IntegraBifPortRateLimitDropIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 66),
    _IntegraBifPortRateLimitDropIngressPackets_Type()
)
integraBifPortRateLimitDropIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPortRateLimitDropIngressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifPortRateLimitDropIngressPackets.setUnits("packet")
_IntegraBifPortRateLimitDropIngressBytes_Type = Counter64
_IntegraBifPortRateLimitDropIngressBytes_Object = MibTableColumn
integraBifPortRateLimitDropIngressBytes = _IntegraBifPortRateLimitDropIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 67),
    _IntegraBifPortRateLimitDropIngressBytes_Type()
)
integraBifPortRateLimitDropIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPortRateLimitDropIngressBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraBifPortRateLimitDropIngressBytes.setUnits("packet")
_IntegraBifPausePFCframesGeneratedIngressPackets_Type = Counter64
_IntegraBifPausePFCframesGeneratedIngressPackets_Object = MibTableColumn
integraBifPausePFCframesGeneratedIngressPackets = _IntegraBifPausePFCframesGeneratedIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 68),
    _IntegraBifPausePFCframesGeneratedIngressPackets_Type()
)
integraBifPausePFCframesGeneratedIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPausePFCframesGeneratedIngressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifPausePFCframesGeneratedIngressPackets.setUnits("packet")
_IntegraBifPausePFCframesGeneratedEgressPackets_Type = Counter64
_IntegraBifPausePFCframesGeneratedEgressPackets_Object = MibTableColumn
integraBifPausePFCframesGeneratedEgressPackets = _IntegraBifPausePFCframesGeneratedEgressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 69),
    _IntegraBifPausePFCframesGeneratedEgressPackets_Type()
)
integraBifPausePFCframesGeneratedEgressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifPausePFCframesGeneratedEgressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifPausePFCframesGeneratedEgressPackets.setUnits("packet")
_IntegraBifRateLimitDropForUnknownUnicastIngressPackets_Type = Counter64
_IntegraBifRateLimitDropForUnknownUnicastIngressPackets_Object = MibTableColumn
integraBifRateLimitDropForUnknownUnicastIngressPackets = _IntegraBifRateLimitDropForUnknownUnicastIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 70),
    _IntegraBifRateLimitDropForUnknownUnicastIngressPackets_Type()
)
integraBifRateLimitDropForUnknownUnicastIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifRateLimitDropForUnknownUnicastIngressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifRateLimitDropForUnknownUnicastIngressPackets.setUnits("packet")
_IntegraBifRateLimitDropForUnknownUnicastIngressBytes_Type = Counter64
_IntegraBifRateLimitDropForUnknownUnicastIngressBytes_Object = MibTableColumn
integraBifRateLimitDropForUnknownUnicastIngressBytes = _IntegraBifRateLimitDropForUnknownUnicastIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 71),
    _IntegraBifRateLimitDropForUnknownUnicastIngressBytes_Type()
)
integraBifRateLimitDropForUnknownUnicastIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifRateLimitDropForUnknownUnicastIngressBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraBifRateLimitDropForUnknownUnicastIngressBytes.setUnits("B")
_IntegraBifRateLimitDropForBroadcastIngressPackets_Type = Counter64
_IntegraBifRateLimitDropForBroadcastIngressPackets_Object = MibTableColumn
integraBifRateLimitDropForBroadcastIngressPackets = _IntegraBifRateLimitDropForBroadcastIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 72),
    _IntegraBifRateLimitDropForBroadcastIngressPackets_Type()
)
integraBifRateLimitDropForBroadcastIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifRateLimitDropForBroadcastIngressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifRateLimitDropForBroadcastIngressPackets.setUnits("packet")
_IntegraBifRateLimitDropForBroadcastIngressBytes_Type = Counter64
_IntegraBifRateLimitDropForBroadcastIngressBytes_Object = MibTableColumn
integraBifRateLimitDropForBroadcastIngressBytes = _IntegraBifRateLimitDropForBroadcastIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 73),
    _IntegraBifRateLimitDropForBroadcastIngressBytes_Type()
)
integraBifRateLimitDropForBroadcastIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifRateLimitDropForBroadcastIngressBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraBifRateLimitDropForBroadcastIngressBytes.setUnits("B")
_IntegraBifRateLimitDropForKnownMulticastIngressPackets_Type = Counter64
_IntegraBifRateLimitDropForKnownMulticastIngressPackets_Object = MibTableColumn
integraBifRateLimitDropForKnownMulticastIngressPackets = _IntegraBifRateLimitDropForKnownMulticastIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 74),
    _IntegraBifRateLimitDropForKnownMulticastIngressPackets_Type()
)
integraBifRateLimitDropForKnownMulticastIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifRateLimitDropForKnownMulticastIngressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifRateLimitDropForKnownMulticastIngressPackets.setUnits("packet")
_IntegraBifRateLimitDropForKnownMulticastIngressBytes_Type = Counter64
_IntegraBifRateLimitDropForKnownMulticastIngressBytes_Object = MibTableColumn
integraBifRateLimitDropForKnownMulticastIngressBytes = _IntegraBifRateLimitDropForKnownMulticastIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 75),
    _IntegraBifRateLimitDropForKnownMulticastIngressBytes_Type()
)
integraBifRateLimitDropForKnownMulticastIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifRateLimitDropForKnownMulticastIngressBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraBifRateLimitDropForKnownMulticastIngressBytes.setUnits("B")
_IntegraBifRateLimitDropForUnknownMulticastIngressPackets_Type = Counter64
_IntegraBifRateLimitDropForUnknownMulticastIngressPackets_Object = MibTableColumn
integraBifRateLimitDropForUnknownMulticastIngressPackets = _IntegraBifRateLimitDropForUnknownMulticastIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 76),
    _IntegraBifRateLimitDropForUnknownMulticastIngressPackets_Type()
)
integraBifRateLimitDropForUnknownMulticastIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifRateLimitDropForUnknownMulticastIngressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifRateLimitDropForUnknownMulticastIngressPackets.setUnits("packet")
_IntegraBifRateLimitDropForUnknownMulticastIngressBytes_Type = Counter64
_IntegraBifRateLimitDropForUnknownMulticastIngressBytes_Object = MibTableColumn
integraBifRateLimitDropForUnknownMulticastIngressBytes = _IntegraBifRateLimitDropForUnknownMulticastIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 77),
    _IntegraBifRateLimitDropForUnknownMulticastIngressBytes_Type()
)
integraBifRateLimitDropForUnknownMulticastIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifRateLimitDropForUnknownMulticastIngressBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraBifRateLimitDropForUnknownMulticastIngressBytes.setUnits("B")
_IntegraBifAllCoSQoutPackets_Type = Counter64
_IntegraBifAllCoSQoutPackets_Object = MibTableColumn
integraBifAllCoSQoutPackets = _IntegraBifAllCoSQoutPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 78),
    _IntegraBifAllCoSQoutPackets_Type()
)
integraBifAllCoSQoutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifAllCoSQoutPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifAllCoSQoutPackets.setUnits("packet")
_IntegraBifAllCoSQoutBytes_Type = Counter64
_IntegraBifAllCoSQoutBytes_Object = MibTableColumn
integraBifAllCoSQoutBytes = _IntegraBifAllCoSQoutBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 79),
    _IntegraBifAllCoSQoutBytes_Type()
)
integraBifAllCoSQoutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifAllCoSQoutBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraBifAllCoSQoutBytes.setUnits("B")
_IntegraBifAllCoSQdroppedPackets_Type = Counter64
_IntegraBifAllCoSQdroppedPackets_Object = MibTableColumn
integraBifAllCoSQdroppedPackets = _IntegraBifAllCoSQdroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 80),
    _IntegraBifAllCoSQdroppedPackets_Type()
)
integraBifAllCoSQdroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifAllCoSQdroppedPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifAllCoSQdroppedPackets.setUnits("packet")
_IntegraBifAllCoSQdroppedBytes_Type = Counter64
_IntegraBifAllCoSQdroppedBytes_Object = MibTableColumn
integraBifAllCoSQdroppedBytes = _IntegraBifAllCoSQdroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 81),
    _IntegraBifAllCoSQdroppedBytes_Type()
)
integraBifAllCoSQdroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifAllCoSQdroppedBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraBifAllCoSQdroppedBytes.setUnits("B")
_IntegraBifProcessedRxPackets_Type = Counter64
_IntegraBifProcessedRxPackets_Object = MibTableColumn
integraBifProcessedRxPackets = _IntegraBifProcessedRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 82),
    _IntegraBifProcessedRxPackets_Type()
)
integraBifProcessedRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifProcessedRxPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraBifProcessedRxPackets.setUnits("packet")
_IntegraBifProcessedRxBytes_Type = Counter64
_IntegraBifProcessedRxBytes_Object = MibTableColumn
integraBifProcessedRxBytes = _IntegraBifProcessedRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 2, 1, 83),
    _IntegraBifProcessedRxBytes_Type()
)
integraBifProcessedRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifProcessedRxBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraBifProcessedRxBytes.setUnits("B")
_IntegraBifQosStatisticsTable_Object = MibTable
integraBifQosStatisticsTable = _IntegraBifQosStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3)
)
if mibBuilder.loadTexts:
    integraBifQosStatisticsTable.setStatus("current")
_IntegraBifCosqEntry_Object = MibTableRow
integraBifCosqEntry = _IntegraBifCosqEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1)
)
integraBifCosqEntry.setIndexNames(
    (0, "SAF-INTEGRAB-MIB", "integraBifCosqIfaceIndex"),
)
if mibBuilder.loadTexts:
    integraBifCosqEntry.setStatus("current")


class _IntegraBifCosqIfaceIndex_Type(Integer32):
    """Custom type integraBifCosqIfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IntegraBifCosqIfaceIndex_Type.__name__ = "Integer32"
_IntegraBifCosqIfaceIndex_Object = MibTableColumn
integraBifCosqIfaceIndex = _IntegraBifCosqIfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 1),
    _IntegraBifCosqIfaceIndex_Type()
)
integraBifCosqIfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqIfaceIndex.setStatus("current")


class _IntegraBifCosqIfaceDescr_Type(DisplayString):
    """Custom type integraBifCosqIfaceDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntegraBifCosqIfaceDescr_Type.__name__ = "DisplayString"
_IntegraBifCosqIfaceDescr_Object = MibTableColumn
integraBifCosqIfaceDescr = _IntegraBifCosqIfaceDescr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 2),
    _IntegraBifCosqIfaceDescr_Type()
)
integraBifCosqIfaceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqIfaceDescr.setStatus("current")
_IntegraBifCosqStatDroppedPacketsCoSQ0_Type = Counter64
_IntegraBifCosqStatDroppedPacketsCoSQ0_Object = MibTableColumn
integraBifCosqStatDroppedPacketsCoSQ0 = _IntegraBifCosqStatDroppedPacketsCoSQ0_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 3),
    _IntegraBifCosqStatDroppedPacketsCoSQ0_Type()
)
integraBifCosqStatDroppedPacketsCoSQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedPacketsCoSQ0.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedPacketsCoSQ0.setUnits("packet")
_IntegraBifCosqStatDroppedBytesCoSQ0_Type = Counter64
_IntegraBifCosqStatDroppedBytesCoSQ0_Object = MibTableColumn
integraBifCosqStatDroppedBytesCoSQ0 = _IntegraBifCosqStatDroppedBytesCoSQ0_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 4),
    _IntegraBifCosqStatDroppedBytesCoSQ0_Type()
)
integraBifCosqStatDroppedBytesCoSQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedBytesCoSQ0.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedBytesCoSQ0.setUnits("B")
_IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ0_Type = Counter64
_IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ0_Object = MibTableColumn
integraBifCosqStatGreenDiscardDroppedPacketsCoSQ0 = _IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ0_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 5),
    _IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ0_Type()
)
integraBifCosqStatGreenDiscardDroppedPacketsCoSQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatGreenDiscardDroppedPacketsCoSQ0.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatGreenDiscardDroppedPacketsCoSQ0.setUnits("packet")
_IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ0_Type = Counter64
_IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ0_Object = MibTableColumn
integraBifCosqStatYellowDiscardDroppedPacketsCoSQ0 = _IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ0_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 6),
    _IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ0_Type()
)
integraBifCosqStatYellowDiscardDroppedPacketsCoSQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatYellowDiscardDroppedPacketsCoSQ0.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatYellowDiscardDroppedPacketsCoSQ0.setUnits("packet")
_IntegraBifCosqStatOutPacketsCoSQ0_Type = Counter64
_IntegraBifCosqStatOutPacketsCoSQ0_Object = MibTableColumn
integraBifCosqStatOutPacketsCoSQ0 = _IntegraBifCosqStatOutPacketsCoSQ0_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 7),
    _IntegraBifCosqStatOutPacketsCoSQ0_Type()
)
integraBifCosqStatOutPacketsCoSQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatOutPacketsCoSQ0.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatOutPacketsCoSQ0.setUnits("packet")
_IntegraBifCosqStatOutBytesCoSQ0_Type = Counter64
_IntegraBifCosqStatOutBytesCoSQ0_Object = MibTableColumn
integraBifCosqStatOutBytesCoSQ0 = _IntegraBifCosqStatOutBytesCoSQ0_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 8),
    _IntegraBifCosqStatOutBytesCoSQ0_Type()
)
integraBifCosqStatOutBytesCoSQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatOutBytesCoSQ0.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatOutBytesCoSQ0.setUnits("B")
_IntegraBifCosqStatDroppedPacketsCoSQ1_Type = Counter64
_IntegraBifCosqStatDroppedPacketsCoSQ1_Object = MibTableColumn
integraBifCosqStatDroppedPacketsCoSQ1 = _IntegraBifCosqStatDroppedPacketsCoSQ1_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 9),
    _IntegraBifCosqStatDroppedPacketsCoSQ1_Type()
)
integraBifCosqStatDroppedPacketsCoSQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedPacketsCoSQ1.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedPacketsCoSQ1.setUnits("packet")
_IntegraBifCosqStatDroppedBytesCoSQ1_Type = Counter64
_IntegraBifCosqStatDroppedBytesCoSQ1_Object = MibTableColumn
integraBifCosqStatDroppedBytesCoSQ1 = _IntegraBifCosqStatDroppedBytesCoSQ1_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 10),
    _IntegraBifCosqStatDroppedBytesCoSQ1_Type()
)
integraBifCosqStatDroppedBytesCoSQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedBytesCoSQ1.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedBytesCoSQ1.setUnits("B")
_IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ1_Type = Counter64
_IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ1_Object = MibTableColumn
integraBifCosqStatGreenDiscardDroppedPacketsCoSQ1 = _IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ1_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 11),
    _IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ1_Type()
)
integraBifCosqStatGreenDiscardDroppedPacketsCoSQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatGreenDiscardDroppedPacketsCoSQ1.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatGreenDiscardDroppedPacketsCoSQ1.setUnits("packet")
_IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ1_Type = Counter64
_IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ1_Object = MibTableColumn
integraBifCosqStatYellowDiscardDroppedPacketsCoSQ1 = _IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ1_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 12),
    _IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ1_Type()
)
integraBifCosqStatYellowDiscardDroppedPacketsCoSQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatYellowDiscardDroppedPacketsCoSQ1.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatYellowDiscardDroppedPacketsCoSQ1.setUnits("packet")
_IntegraBifCosqStatOutPacketsCoSQ1_Type = Counter64
_IntegraBifCosqStatOutPacketsCoSQ1_Object = MibTableColumn
integraBifCosqStatOutPacketsCoSQ1 = _IntegraBifCosqStatOutPacketsCoSQ1_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 13),
    _IntegraBifCosqStatOutPacketsCoSQ1_Type()
)
integraBifCosqStatOutPacketsCoSQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatOutPacketsCoSQ1.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatOutPacketsCoSQ1.setUnits("packet")
_IntegraBifCosqStatOutBytesCoSQ1_Type = Counter64
_IntegraBifCosqStatOutBytesCoSQ1_Object = MibTableColumn
integraBifCosqStatOutBytesCoSQ1 = _IntegraBifCosqStatOutBytesCoSQ1_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 14),
    _IntegraBifCosqStatOutBytesCoSQ1_Type()
)
integraBifCosqStatOutBytesCoSQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatOutBytesCoSQ1.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatOutBytesCoSQ1.setUnits("B")
_IntegraBifCosqStatDroppedPacketsCoSQ2_Type = Counter64
_IntegraBifCosqStatDroppedPacketsCoSQ2_Object = MibTableColumn
integraBifCosqStatDroppedPacketsCoSQ2 = _IntegraBifCosqStatDroppedPacketsCoSQ2_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 15),
    _IntegraBifCosqStatDroppedPacketsCoSQ2_Type()
)
integraBifCosqStatDroppedPacketsCoSQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedPacketsCoSQ2.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedPacketsCoSQ2.setUnits("packet")
_IntegraBifCosqStatDroppedBytesCoSQ2_Type = Counter64
_IntegraBifCosqStatDroppedBytesCoSQ2_Object = MibTableColumn
integraBifCosqStatDroppedBytesCoSQ2 = _IntegraBifCosqStatDroppedBytesCoSQ2_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 16),
    _IntegraBifCosqStatDroppedBytesCoSQ2_Type()
)
integraBifCosqStatDroppedBytesCoSQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedBytesCoSQ2.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedBytesCoSQ2.setUnits("B")
_IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ2_Type = Counter64
_IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ2_Object = MibTableColumn
integraBifCosqStatGreenDiscardDroppedPacketsCoSQ2 = _IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ2_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 17),
    _IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ2_Type()
)
integraBifCosqStatGreenDiscardDroppedPacketsCoSQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatGreenDiscardDroppedPacketsCoSQ2.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatGreenDiscardDroppedPacketsCoSQ2.setUnits("packet")
_IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ2_Type = Counter64
_IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ2_Object = MibTableColumn
integraBifCosqStatYellowDiscardDroppedPacketsCoSQ2 = _IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ2_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 18),
    _IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ2_Type()
)
integraBifCosqStatYellowDiscardDroppedPacketsCoSQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatYellowDiscardDroppedPacketsCoSQ2.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatYellowDiscardDroppedPacketsCoSQ2.setUnits("packet")
_IntegraBifCosqStatOutPacketsCoSQ2_Type = Counter64
_IntegraBifCosqStatOutPacketsCoSQ2_Object = MibTableColumn
integraBifCosqStatOutPacketsCoSQ2 = _IntegraBifCosqStatOutPacketsCoSQ2_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 19),
    _IntegraBifCosqStatOutPacketsCoSQ2_Type()
)
integraBifCosqStatOutPacketsCoSQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatOutPacketsCoSQ2.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatOutPacketsCoSQ2.setUnits("packet")
_IntegraBifCosqStatOutBytesCoSQ2_Type = Counter64
_IntegraBifCosqStatOutBytesCoSQ2_Object = MibTableColumn
integraBifCosqStatOutBytesCoSQ2 = _IntegraBifCosqStatOutBytesCoSQ2_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 20),
    _IntegraBifCosqStatOutBytesCoSQ2_Type()
)
integraBifCosqStatOutBytesCoSQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatOutBytesCoSQ2.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatOutBytesCoSQ2.setUnits("B")
_IntegraBifCosqStatDroppedPacketsCoSQ3_Type = Counter64
_IntegraBifCosqStatDroppedPacketsCoSQ3_Object = MibTableColumn
integraBifCosqStatDroppedPacketsCoSQ3 = _IntegraBifCosqStatDroppedPacketsCoSQ3_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 21),
    _IntegraBifCosqStatDroppedPacketsCoSQ3_Type()
)
integraBifCosqStatDroppedPacketsCoSQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedPacketsCoSQ3.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedPacketsCoSQ3.setUnits("packet")
_IntegraBifCosqStatDroppedBytesCoSQ3_Type = Counter64
_IntegraBifCosqStatDroppedBytesCoSQ3_Object = MibTableColumn
integraBifCosqStatDroppedBytesCoSQ3 = _IntegraBifCosqStatDroppedBytesCoSQ3_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 22),
    _IntegraBifCosqStatDroppedBytesCoSQ3_Type()
)
integraBifCosqStatDroppedBytesCoSQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedBytesCoSQ3.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedBytesCoSQ3.setUnits("B")
_IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ3_Type = Counter64
_IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ3_Object = MibTableColumn
integraBifCosqStatGreenDiscardDroppedPacketsCoSQ3 = _IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ3_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 23),
    _IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ3_Type()
)
integraBifCosqStatGreenDiscardDroppedPacketsCoSQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatGreenDiscardDroppedPacketsCoSQ3.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatGreenDiscardDroppedPacketsCoSQ3.setUnits("packet")
_IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ3_Type = Counter64
_IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ3_Object = MibTableColumn
integraBifCosqStatYellowDiscardDroppedPacketsCoSQ3 = _IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ3_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 24),
    _IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ3_Type()
)
integraBifCosqStatYellowDiscardDroppedPacketsCoSQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatYellowDiscardDroppedPacketsCoSQ3.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatYellowDiscardDroppedPacketsCoSQ3.setUnits("packet")
_IntegraBifCosqStatOutPacketsCoSQ3_Type = Counter64
_IntegraBifCosqStatOutPacketsCoSQ3_Object = MibTableColumn
integraBifCosqStatOutPacketsCoSQ3 = _IntegraBifCosqStatOutPacketsCoSQ3_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 25),
    _IntegraBifCosqStatOutPacketsCoSQ3_Type()
)
integraBifCosqStatOutPacketsCoSQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatOutPacketsCoSQ3.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatOutPacketsCoSQ3.setUnits("packet")
_IntegraBifCosqStatOutBytesCoSQ3_Type = Counter64
_IntegraBifCosqStatOutBytesCoSQ3_Object = MibTableColumn
integraBifCosqStatOutBytesCoSQ3 = _IntegraBifCosqStatOutBytesCoSQ3_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 26),
    _IntegraBifCosqStatOutBytesCoSQ3_Type()
)
integraBifCosqStatOutBytesCoSQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatOutBytesCoSQ3.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatOutBytesCoSQ3.setUnits("B")
_IntegraBifCosqStatDroppedPacketsCoSQ4_Type = Counter64
_IntegraBifCosqStatDroppedPacketsCoSQ4_Object = MibTableColumn
integraBifCosqStatDroppedPacketsCoSQ4 = _IntegraBifCosqStatDroppedPacketsCoSQ4_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 27),
    _IntegraBifCosqStatDroppedPacketsCoSQ4_Type()
)
integraBifCosqStatDroppedPacketsCoSQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedPacketsCoSQ4.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedPacketsCoSQ4.setUnits("packet")
_IntegraBifCosqStatDroppedBytesCoSQ4_Type = Counter64
_IntegraBifCosqStatDroppedBytesCoSQ4_Object = MibTableColumn
integraBifCosqStatDroppedBytesCoSQ4 = _IntegraBifCosqStatDroppedBytesCoSQ4_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 28),
    _IntegraBifCosqStatDroppedBytesCoSQ4_Type()
)
integraBifCosqStatDroppedBytesCoSQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedBytesCoSQ4.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedBytesCoSQ4.setUnits("B")
_IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ4_Type = Counter64
_IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ4_Object = MibTableColumn
integraBifCosqStatGreenDiscardDroppedPacketsCoSQ4 = _IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ4_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 29),
    _IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ4_Type()
)
integraBifCosqStatGreenDiscardDroppedPacketsCoSQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatGreenDiscardDroppedPacketsCoSQ4.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatGreenDiscardDroppedPacketsCoSQ4.setUnits("packet")
_IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ4_Type = Counter64
_IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ4_Object = MibTableColumn
integraBifCosqStatYellowDiscardDroppedPacketsCoSQ4 = _IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ4_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 30),
    _IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ4_Type()
)
integraBifCosqStatYellowDiscardDroppedPacketsCoSQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatYellowDiscardDroppedPacketsCoSQ4.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatYellowDiscardDroppedPacketsCoSQ4.setUnits("packet")
_IntegraBifCosqStatOutPacketsCoSQ4_Type = Counter64
_IntegraBifCosqStatOutPacketsCoSQ4_Object = MibTableColumn
integraBifCosqStatOutPacketsCoSQ4 = _IntegraBifCosqStatOutPacketsCoSQ4_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 31),
    _IntegraBifCosqStatOutPacketsCoSQ4_Type()
)
integraBifCosqStatOutPacketsCoSQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatOutPacketsCoSQ4.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatOutPacketsCoSQ4.setUnits("packet")
_IntegraBifCosqStatOutBytesCoSQ4_Type = Counter64
_IntegraBifCosqStatOutBytesCoSQ4_Object = MibTableColumn
integraBifCosqStatOutBytesCoSQ4 = _IntegraBifCosqStatOutBytesCoSQ4_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 32),
    _IntegraBifCosqStatOutBytesCoSQ4_Type()
)
integraBifCosqStatOutBytesCoSQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatOutBytesCoSQ4.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatOutBytesCoSQ4.setUnits("B")
_IntegraBifCosqStatDroppedPacketsCoSQ5_Type = Counter64
_IntegraBifCosqStatDroppedPacketsCoSQ5_Object = MibTableColumn
integraBifCosqStatDroppedPacketsCoSQ5 = _IntegraBifCosqStatDroppedPacketsCoSQ5_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 33),
    _IntegraBifCosqStatDroppedPacketsCoSQ5_Type()
)
integraBifCosqStatDroppedPacketsCoSQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedPacketsCoSQ5.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedPacketsCoSQ5.setUnits("packet")
_IntegraBifCosqStatDroppedBytesCoSQ5_Type = Counter64
_IntegraBifCosqStatDroppedBytesCoSQ5_Object = MibTableColumn
integraBifCosqStatDroppedBytesCoSQ5 = _IntegraBifCosqStatDroppedBytesCoSQ5_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 34),
    _IntegraBifCosqStatDroppedBytesCoSQ5_Type()
)
integraBifCosqStatDroppedBytesCoSQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedBytesCoSQ5.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedBytesCoSQ5.setUnits("B")
_IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ5_Type = Counter64
_IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ5_Object = MibTableColumn
integraBifCosqStatGreenDiscardDroppedPacketsCoSQ5 = _IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ5_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 35),
    _IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ5_Type()
)
integraBifCosqStatGreenDiscardDroppedPacketsCoSQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatGreenDiscardDroppedPacketsCoSQ5.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatGreenDiscardDroppedPacketsCoSQ5.setUnits("packet")
_IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ5_Type = Counter64
_IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ5_Object = MibTableColumn
integraBifCosqStatYellowDiscardDroppedPacketsCoSQ5 = _IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ5_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 36),
    _IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ5_Type()
)
integraBifCosqStatYellowDiscardDroppedPacketsCoSQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatYellowDiscardDroppedPacketsCoSQ5.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatYellowDiscardDroppedPacketsCoSQ5.setUnits("packet")
_IntegraBifCosqStatOutPacketsCoSQ5_Type = Counter64
_IntegraBifCosqStatOutPacketsCoSQ5_Object = MibTableColumn
integraBifCosqStatOutPacketsCoSQ5 = _IntegraBifCosqStatOutPacketsCoSQ5_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 37),
    _IntegraBifCosqStatOutPacketsCoSQ5_Type()
)
integraBifCosqStatOutPacketsCoSQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatOutPacketsCoSQ5.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatOutPacketsCoSQ5.setUnits("packet")
_IntegraBifCosqStatOutBytesCoSQ5_Type = Counter64
_IntegraBifCosqStatOutBytesCoSQ5_Object = MibTableColumn
integraBifCosqStatOutBytesCoSQ5 = _IntegraBifCosqStatOutBytesCoSQ5_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 38),
    _IntegraBifCosqStatOutBytesCoSQ5_Type()
)
integraBifCosqStatOutBytesCoSQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatOutBytesCoSQ5.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatOutBytesCoSQ5.setUnits("B")
_IntegraBifCosqStatDroppedPacketsCoSQ6_Type = Counter64
_IntegraBifCosqStatDroppedPacketsCoSQ6_Object = MibTableColumn
integraBifCosqStatDroppedPacketsCoSQ6 = _IntegraBifCosqStatDroppedPacketsCoSQ6_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 39),
    _IntegraBifCosqStatDroppedPacketsCoSQ6_Type()
)
integraBifCosqStatDroppedPacketsCoSQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedPacketsCoSQ6.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedPacketsCoSQ6.setUnits("packet")
_IntegraBifCosqStatDroppedBytesCoSQ6_Type = Counter64
_IntegraBifCosqStatDroppedBytesCoSQ6_Object = MibTableColumn
integraBifCosqStatDroppedBytesCoSQ6 = _IntegraBifCosqStatDroppedBytesCoSQ6_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 40),
    _IntegraBifCosqStatDroppedBytesCoSQ6_Type()
)
integraBifCosqStatDroppedBytesCoSQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedBytesCoSQ6.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedBytesCoSQ6.setUnits("B")
_IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ6_Type = Counter64
_IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ6_Object = MibTableColumn
integraBifCosqStatGreenDiscardDroppedPacketsCoSQ6 = _IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ6_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 41),
    _IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ6_Type()
)
integraBifCosqStatGreenDiscardDroppedPacketsCoSQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatGreenDiscardDroppedPacketsCoSQ6.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatGreenDiscardDroppedPacketsCoSQ6.setUnits("packet")
_IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ6_Type = Counter64
_IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ6_Object = MibTableColumn
integraBifCosqStatYellowDiscardDroppedPacketsCoSQ6 = _IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ6_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 42),
    _IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ6_Type()
)
integraBifCosqStatYellowDiscardDroppedPacketsCoSQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatYellowDiscardDroppedPacketsCoSQ6.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatYellowDiscardDroppedPacketsCoSQ6.setUnits("packet")
_IntegraBifCosqStatOutPacketsCoSQ6_Type = Counter64
_IntegraBifCosqStatOutPacketsCoSQ6_Object = MibTableColumn
integraBifCosqStatOutPacketsCoSQ6 = _IntegraBifCosqStatOutPacketsCoSQ6_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 43),
    _IntegraBifCosqStatOutPacketsCoSQ6_Type()
)
integraBifCosqStatOutPacketsCoSQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatOutPacketsCoSQ6.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatOutPacketsCoSQ6.setUnits("packet")
_IntegraBifCosqStatOutBytesCoSQ6_Type = Counter64
_IntegraBifCosqStatOutBytesCoSQ6_Object = MibTableColumn
integraBifCosqStatOutBytesCoSQ6 = _IntegraBifCosqStatOutBytesCoSQ6_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 44),
    _IntegraBifCosqStatOutBytesCoSQ6_Type()
)
integraBifCosqStatOutBytesCoSQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatOutBytesCoSQ6.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatOutBytesCoSQ6.setUnits("B")
_IntegraBifCosqStatDroppedPacketsCoSQ7_Type = Counter64
_IntegraBifCosqStatDroppedPacketsCoSQ7_Object = MibTableColumn
integraBifCosqStatDroppedPacketsCoSQ7 = _IntegraBifCosqStatDroppedPacketsCoSQ7_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 45),
    _IntegraBifCosqStatDroppedPacketsCoSQ7_Type()
)
integraBifCosqStatDroppedPacketsCoSQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedPacketsCoSQ7.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedPacketsCoSQ7.setUnits("packet")
_IntegraBifCosqStatDroppedBytesCoSQ7_Type = Counter64
_IntegraBifCosqStatDroppedBytesCoSQ7_Object = MibTableColumn
integraBifCosqStatDroppedBytesCoSQ7 = _IntegraBifCosqStatDroppedBytesCoSQ7_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 46),
    _IntegraBifCosqStatDroppedBytesCoSQ7_Type()
)
integraBifCosqStatDroppedBytesCoSQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedBytesCoSQ7.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatDroppedBytesCoSQ7.setUnits("B")
_IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ7_Type = Counter64
_IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ7_Object = MibTableColumn
integraBifCosqStatGreenDiscardDroppedPacketsCoSQ7 = _IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ7_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 47),
    _IntegraBifCosqStatGreenDiscardDroppedPacketsCoSQ7_Type()
)
integraBifCosqStatGreenDiscardDroppedPacketsCoSQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatGreenDiscardDroppedPacketsCoSQ7.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatGreenDiscardDroppedPacketsCoSQ7.setUnits("packet")
_IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ7_Type = Counter64
_IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ7_Object = MibTableColumn
integraBifCosqStatYellowDiscardDroppedPacketsCoSQ7 = _IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ7_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 48),
    _IntegraBifCosqStatYellowDiscardDroppedPacketsCoSQ7_Type()
)
integraBifCosqStatYellowDiscardDroppedPacketsCoSQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatYellowDiscardDroppedPacketsCoSQ7.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatYellowDiscardDroppedPacketsCoSQ7.setUnits("packet")
_IntegraBifCosqStatOutPacketsCoSQ7_Type = Counter64
_IntegraBifCosqStatOutPacketsCoSQ7_Object = MibTableColumn
integraBifCosqStatOutPacketsCoSQ7 = _IntegraBifCosqStatOutPacketsCoSQ7_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 49),
    _IntegraBifCosqStatOutPacketsCoSQ7_Type()
)
integraBifCosqStatOutPacketsCoSQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatOutPacketsCoSQ7.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatOutPacketsCoSQ7.setUnits("packet")
_IntegraBifCosqStatOutBytesCoSQ7_Type = Counter64
_IntegraBifCosqStatOutBytesCoSQ7_Object = MibTableColumn
integraBifCosqStatOutBytesCoSQ7 = _IntegraBifCosqStatOutBytesCoSQ7_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 5, 3, 1, 50),
    _IntegraBifCosqStatOutBytesCoSQ7_Type()
)
integraBifCosqStatOutBytesCoSQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBifCosqStatOutBytesCoSQ7.setStatus("current")
if mibBuilder.loadTexts:
    integraBifCosqStatOutBytesCoSQ7.setUnits("B")


class _IntegraBexecuteConfig_Type(Integer32):
    """Custom type integraBexecuteConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_IntegraBexecuteConfig_Type.__name__ = "Integer32"
_IntegraBexecuteConfig_Object = MibScalar
integraBexecuteConfig = _IntegraBexecuteConfig_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 6),
    _IntegraBexecuteConfig_Type()
)
integraBexecuteConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraBexecuteConfig.setStatus("current")


class _IntegraBneedStore_Type(Integer32):
    """Custom type integraBneedStore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("no", 0)
    )


_IntegraBneedStore_Type.__name__ = "Integer32"
_IntegraBneedStore_Object = MibScalar
integraBneedStore = _IntegraBneedStore_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 7),
    _IntegraBneedStore_Type()
)
integraBneedStore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBneedStore.setStatus("current")


class _IntegraBstoreConfig_Type(Integer32):
    """Custom type integraBstoreConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("store", 1)
    )


_IntegraBstoreConfig_Type.__name__ = "Integer32"
_IntegraBstoreConfig_Object = MibScalar
integraBstoreConfig = _IntegraBstoreConfig_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 8),
    _IntegraBstoreConfig_Type()
)
integraBstoreConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraBstoreConfig.setStatus("current")
_IntegraBnetCfg_ObjectIdentity = ObjectIdentity
integraBnetCfg = _IntegraBnetCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 9)
)
_IntegraBnetCfgIPaddress_Type = IpAddress
_IntegraBnetCfgIPaddress_Object = MibScalar
integraBnetCfgIPaddress = _IntegraBnetCfgIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 9, 1),
    _IntegraBnetCfgIPaddress_Type()
)
integraBnetCfgIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraBnetCfgIPaddress.setStatus("current")
_IntegraBnetCfgIPmask_Type = IpAddress
_IntegraBnetCfgIPmask_Object = MibScalar
integraBnetCfgIPmask = _IntegraBnetCfgIPmask_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 9, 2),
    _IntegraBnetCfgIPmask_Type()
)
integraBnetCfgIPmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraBnetCfgIPmask.setStatus("current")
_IntegraBnetCfgIPgateway_Type = IpAddress
_IntegraBnetCfgIPgateway_Object = MibScalar
integraBnetCfgIPgateway = _IntegraBnetCfgIPgateway_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 9, 3),
    _IntegraBnetCfgIPgateway_Type()
)
integraBnetCfgIPgateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraBnetCfgIPgateway.setStatus("current")
_IntegraBnetCfgRemoteIPaddress_Type = IpAddress
_IntegraBnetCfgRemoteIPaddress_Object = MibScalar
integraBnetCfgRemoteIPaddress = _IntegraBnetCfgRemoteIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 9, 4),
    _IntegraBnetCfgRemoteIPaddress_Type()
)
integraBnetCfgRemoteIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraBnetCfgRemoteIPaddress.setStatus("current")
_IntegraBConformance_ObjectIdentity = ObjectIdentity
integraBConformance = _IntegraBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 10)
)
_IntegraBCompliances_ObjectIdentity = ObjectIdentity
integraBCompliances = _IntegraBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 10, 1)
)
_IntegraBGroups_ObjectIdentity = ObjectIdentity
integraBGroups = _IntegraBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 10, 2)
)

# Managed Objects groups

integraBMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 10, 2, 1)
)
integraBMiscGroup.setObjects(
    ("SAF-INTEGRAB-MIB", "integraBtimestamp")
)
if mibBuilder.loadTexts:
    integraBMiscGroup.setStatus("current")

integraBRadioGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 10, 2, 2)
)
integraBRadioGroup.setObjects(
      *(("SAF-INTEGRAB-MIB", "integraBradioTxPower"),
        ("SAF-INTEGRAB-MIB", "integraBradioTxFrequency"),
        ("SAF-INTEGRAB-MIB", "integraBradioRxLevel"),
        ("SAF-INTEGRAB-MIB", "integraBradioSide"),
        ("SAF-INTEGRAB-MIB", "integraBradioTxMute"),
        ("SAF-INTEGRAB-MIB", "integraBradioDuplexShift"),
        ("SAF-INTEGRAB-MIB", "integraBradioRxFrequency"),
        ("SAF-INTEGRAB-MIB", "integraBradioTemperature"),
        ("SAF-INTEGRAB-MIB", "integraBradioTxMuteDuration"),
        ("SAF-INTEGRAB-MIB", "integraBradioRangeEntryIndex"),
        ("SAF-INTEGRAB-MIB", "integraBradioRangeDescr"),
        ("SAF-INTEGRAB-MIB", "integraBradioRangeTxPower"),
        ("SAF-INTEGRAB-MIB", "integraBradioRangeTxFrequency"),
        ("SAF-INTEGRAB-MIB", "integraBradioPLL"))
)
if mibBuilder.loadTexts:
    integraBRadioGroup.setStatus("current")

integraBModemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 10, 2, 3)
)
integraBModemGroup.setObjects(
      *(("SAF-INTEGRAB-MIB", "integraBmodemAcquireStatus"),
        ("SAF-INTEGRAB-MIB", "integraBmodemRadialMse"),
        ("SAF-INTEGRAB-MIB", "integraBmodemFECload"),
        ("SAF-INTEGRAB-MIB", "integraBmodemAcquireLastStatusDetails"),
        ("SAF-INTEGRAB-MIB", "integraBmodemTemperature"),
        ("SAF-INTEGRAB-MIB", "integraBmodemBandwidth"),
        ("SAF-INTEGRAB-MIB", "integraBmodemModulation"),
        ("SAF-INTEGRAB-MIB", "integraBmodemRxModulation"),
        ("SAF-INTEGRAB-MIB", "integraBmodemTxModulation"),
        ("SAF-INTEGRAB-MIB", "integraBmodemRxCapacity"),
        ("SAF-INTEGRAB-MIB", "integraBmodemTxCapacity"),
        ("SAF-INTEGRAB-MIB", "integraBmodemACMengine"),
        ("SAF-INTEGRAB-MIB", "integraBmodemCarrierOffset"))
)
if mibBuilder.loadTexts:
    integraBModemGroup.setStatus("current")

integraBSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 10, 2, 4)
)
integraBSystemGroup.setObjects(
      *(("SAF-INTEGRAB-MIB", "integraBsysCPUtemperature"),
        ("SAF-INTEGRAB-MIB", "integraBsysLicenseExpire"),
        ("SAF-INTEGRAB-MIB", "integraBsysLicenseGenStatus"),
        ("SAF-INTEGRAB-MIB", "integraBsysPSUvoltage"),
        ("SAF-INTEGRAB-MIB", "integraBsysPSUcurrent"),
        ("SAF-INTEGRAB-MIB", "integraBsysPSUpower"),
        ("SAF-INTEGRAB-MIB", "integraBsysBoardTemperature"),
        ("SAF-INTEGRAB-MIB", "integraBsysFreeMemory"),
        ("SAF-INTEGRAB-MIB", "integraBsysCPUidle"),
        ("SAF-INTEGRAB-MIB", "integraBexecuteConfig"),
        ("SAF-INTEGRAB-MIB", "integraBneedStore"),
        ("SAF-INTEGRAB-MIB", "integraBstoreConfig"))
)
if mibBuilder.loadTexts:
    integraBSystemGroup.setStatus("current")

integraBEthernetGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 10, 2, 5)
)
integraBEthernetGeneralGroup.setObjects(
      *(("SAF-INTEGRAB-MIB", "integraBifPortStatIndex"),
        ("SAF-INTEGRAB-MIB", "integraBifPortStatDescr"),
        ("SAF-INTEGRAB-MIB", "integraBifPortType"),
        ("SAF-INTEGRAB-MIB", "integraBifPortMtu"),
        ("SAF-INTEGRAB-MIB", "integraBifPortSpeed"),
        ("SAF-INTEGRAB-MIB", "integraBifPortPhysAddress"),
        ("SAF-INTEGRAB-MIB", "integraBifPortAdminStatus"),
        ("SAF-INTEGRAB-MIB", "integraBifPortOperStatus"),
        ("SAF-INTEGRAB-MIB", "integraBifPortLastChange"),
        ("SAF-INTEGRAB-MIB", "integraBifPortAutoneg"),
        ("SAF-INTEGRAB-MIB", "integraBifPortDuplex"),
        ("SAF-INTEGRAB-MIB", "integraBifPortSyncEthActive"),
        ("SAF-INTEGRAB-MIB", "integraBifPortSyncEthPrio"),
        ("SAF-INTEGRAB-MIB", "integraBifPortFlowControl"),
        ("SAF-INTEGRAB-MIB", "integraBifPortStcIndex"),
        ("SAF-INTEGRAB-MIB", "integraBifPortStcDescr"),
        ("SAF-INTEGRAB-MIB", "integraBifTimePassed"),
        ("SAF-INTEGRAB-MIB", "integraBifIngressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifIngressBytes"),
        ("SAF-INTEGRAB-MIB", "integraBifEgressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifEgressBytes"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherRxOversizePkts"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherTxOversizePkts"),
        ("SAF-INTEGRAB-MIB", "integraBifReceivedPkts64Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifTransmittedPkts64Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifReceivedPkts65to127Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifTransmittedPkts65to127Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifReceivedPkts128to255Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifTransmittedPkts128to255Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifReceivedPkts256to511Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifTransmittedPkts256to511Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifReceivedPkts512to1023Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifTransmittedPkts512to1023Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifReceivedPkts1024to1518Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifTransmittedPkts1024to1518Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifIfInBroadcastPkts"),
        ("SAF-INTEGRAB-MIB", "integraBifIfOutBroadcastPkts"),
        ("SAF-INTEGRAB-MIB", "integraBifIfInMulticastPkts"),
        ("SAF-INTEGRAB-MIB", "integraBifIfOutMulticastPkts"),
        ("SAF-INTEGRAB-MIB", "integraBifIngressBPS"),
        ("SAF-INTEGRAB-MIB", "integraBifIngressPPS"),
        ("SAF-INTEGRAB-MIB", "integraBifEgressBPS"),
        ("SAF-INTEGRAB-MIB", "integraBifEgressPPS"),
        ("SAF-INTEGRAB-MIB", "integraBifMAClearnLimitDropIngressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifL2cacheDropIngressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifEFMdropIngressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifEFMdropEgressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifSTPdropIngressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifSTPdropEgressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifMRUdropIngressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifMRUdropEgressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifFilterDropIngressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifFlowClassifierDropIngressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifFlowClassifierDropEgressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifIllegalSAdropIngressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifPortRateLimitDropIngressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifPortRateLimitDropIngressBytes"),
        ("SAF-INTEGRAB-MIB", "integraBifPausePFCframesGeneratedIngressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifPausePFCframesGeneratedEgressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifRateLimitDropForUnknownUnicastIngressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifRateLimitDropForUnknownUnicastIngressBytes"),
        ("SAF-INTEGRAB-MIB", "integraBifRateLimitDropForBroadcastIngressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifRateLimitDropForBroadcastIngressBytes"),
        ("SAF-INTEGRAB-MIB", "integraBifRateLimitDropForKnownMulticastIngressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifRateLimitDropForKnownMulticastIngressBytes"),
        ("SAF-INTEGRAB-MIB", "integraBifRateLimitDropForUnknownMulticastIngressPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifRateLimitDropForUnknownMulticastIngressBytes"),
        ("SAF-INTEGRAB-MIB", "integraBifAllCoSQoutPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifAllCoSQoutBytes"),
        ("SAF-INTEGRAB-MIB", "integraBifAllCoSQdroppedPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifAllCoSQdroppedBytes"),
        ("SAF-INTEGRAB-MIB", "integraBifProcessedRxPackets"),
        ("SAF-INTEGRAB-MIB", "integraBifProcessedRxBytes"),
        ("SAF-INTEGRAB-MIB", "integraBnetCfgIPaddress"),
        ("SAF-INTEGRAB-MIB", "integraBnetCfgIPmask"),
        ("SAF-INTEGRAB-MIB", "integraBnetCfgIPgateway"),
        ("SAF-INTEGRAB-MIB", "integraBnetCfgRemoteIPaddress"))
)
if mibBuilder.loadTexts:
    integraBEthernetGeneralGroup.setStatus("current")

integraBEthernetMiiPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 10, 2, 6)
)
integraBEthernetMiiPortGroup.setObjects(
      *(("SAF-INTEGRAB-MIB", "integraBifEtherStatsMulticastPkts"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherStatsBroadcastPkts"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherStatsPkts64Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherStatsPkts65to127Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherStatsPkts128to255Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherStatsPkts256to511Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherStatsPkts512to1023Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherStatsPkts1024to1518Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherStatsOversizePkts"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherStatsOctets"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherStatsPkts"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherStatsTXNoErrors"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherStatsRXNoErrors"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherStatsPkts1519to1522Octets"),
        ("SAF-INTEGRAB-MIB", "integraBifIfInOctets"),
        ("SAF-INTEGRAB-MIB", "integraBifIfOutOctets"),
        ("SAF-INTEGRAB-MIB", "integraBifDot1dTpPortInFrames"),
        ("SAF-INTEGRAB-MIB", "integraBifDot1dTpPortOutFrames"),
        ("SAF-INTEGRAB-MIB", "integraBifDot3InPauseFrames"),
        ("SAF-INTEGRAB-MIB", "integraBifDot3OutPauseFrames"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherStatsUndersizePkts"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherStatsFragments"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherStatsCRCAlignErrors"),
        ("SAF-INTEGRAB-MIB", "integraBifEtherStatsJabbers"))
)
if mibBuilder.loadTexts:
    integraBEthernetMiiPortGroup.setStatus("current")

integraBEthernetQosQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 10, 2, 7)
)
integraBEthernetQosQueueGroup.setObjects(
      *(("SAF-INTEGRAB-MIB", "integraBifCosqIfaceIndex"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqIfaceDescr"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatDroppedPacketsCoSQ0"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatDroppedBytesCoSQ0"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatGreenDiscardDroppedPacketsCoSQ0"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatYellowDiscardDroppedPacketsCoSQ0"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatOutPacketsCoSQ0"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatOutBytesCoSQ0"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatDroppedPacketsCoSQ1"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatDroppedBytesCoSQ1"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatGreenDiscardDroppedPacketsCoSQ1"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatYellowDiscardDroppedPacketsCoSQ1"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatOutPacketsCoSQ1"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatOutBytesCoSQ1"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatDroppedPacketsCoSQ2"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatDroppedBytesCoSQ2"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatGreenDiscardDroppedPacketsCoSQ2"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatYellowDiscardDroppedPacketsCoSQ2"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatOutPacketsCoSQ2"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatOutBytesCoSQ2"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatDroppedPacketsCoSQ3"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatDroppedBytesCoSQ3"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatGreenDiscardDroppedPacketsCoSQ3"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatYellowDiscardDroppedPacketsCoSQ3"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatOutPacketsCoSQ3"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatOutBytesCoSQ3"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatDroppedPacketsCoSQ4"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatDroppedBytesCoSQ4"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatGreenDiscardDroppedPacketsCoSQ4"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatYellowDiscardDroppedPacketsCoSQ4"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatOutPacketsCoSQ4"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatOutBytesCoSQ4"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatDroppedPacketsCoSQ5"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatDroppedBytesCoSQ5"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatGreenDiscardDroppedPacketsCoSQ5"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatYellowDiscardDroppedPacketsCoSQ5"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatOutPacketsCoSQ5"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatOutBytesCoSQ5"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatDroppedPacketsCoSQ6"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatDroppedBytesCoSQ6"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatGreenDiscardDroppedPacketsCoSQ6"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatYellowDiscardDroppedPacketsCoSQ6"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatOutPacketsCoSQ6"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatOutBytesCoSQ6"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatDroppedPacketsCoSQ7"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatDroppedBytesCoSQ7"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatGreenDiscardDroppedPacketsCoSQ7"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatYellowDiscardDroppedPacketsCoSQ7"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatOutPacketsCoSQ7"),
        ("SAF-INTEGRAB-MIB", "integraBifCosqStatOutBytesCoSQ7"))
)
if mibBuilder.loadTexts:
    integraBEthernetQosQueueGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

integraBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 1, 10, 1, 1)
)
integraBCompliance.setObjects(
      *(("SAF-INTEGRAB-MIB", "integraBMiscGroup"),
        ("SAF-INTEGRAB-MIB", "integraBRadioGroup"),
        ("SAF-INTEGRAB-MIB", "integraBModemGroup"),
        ("SAF-INTEGRAB-MIB", "integraBSystemGroup"),
        ("SAF-INTEGRAB-MIB", "integraBEthernetGeneralGroup"),
        ("SAF-INTEGRAB-MIB", "integraBEthernetMiiPortGroup"),
        ("SAF-INTEGRAB-MIB", "integraBEthernetQosQueueGroup"))
)
if mibBuilder.loadTexts:
    integraBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAF-INTEGRAB-MIB",
    **{"integraB": integraB,
       "integraBtimestamp": integraBtimestamp,
       "integraBradio": integraBradio,
       "integraBradioTxPower": integraBradioTxPower,
       "integraBradioTxFrequency": integraBradioTxFrequency,
       "integraBradioRxLevel": integraBradioRxLevel,
       "integraBradioSide": integraBradioSide,
       "integraBradioTxMute": integraBradioTxMute,
       "integraBradioDuplexShift": integraBradioDuplexShift,
       "integraBradioRxFrequency": integraBradioRxFrequency,
       "integraBradioTemperature": integraBradioTemperature,
       "integraBradioTxMuteDuration": integraBradioTxMuteDuration,
       "integraBradioRangesTable": integraBradioRangesTable,
       "integraBradioRangeEntry": integraBradioRangeEntry,
       "integraBradioRangeEntryIndex": integraBradioRangeEntryIndex,
       "integraBradioRangeDescr": integraBradioRangeDescr,
       "integraBradioRangeTxPower": integraBradioRangeTxPower,
       "integraBradioRangeTxFrequency": integraBradioRangeTxFrequency,
       "integraBradioPLL": integraBradioPLL,
       "integraBmodem": integraBmodem,
       "integraBmodemAcquireStatus": integraBmodemAcquireStatus,
       "integraBmodemRadialMse": integraBmodemRadialMse,
       "integraBmodemFECload": integraBmodemFECload,
       "integraBmodemAcquireLastStatusDetails": integraBmodemAcquireLastStatusDetails,
       "integraBmodemTemperature": integraBmodemTemperature,
       "integraBmodemBandwidth": integraBmodemBandwidth,
       "integraBmodemModulation": integraBmodemModulation,
       "integraBmodemRxModulation": integraBmodemRxModulation,
       "integraBmodemTxModulation": integraBmodemTxModulation,
       "integraBmodemRxCapacity": integraBmodemRxCapacity,
       "integraBmodemTxCapacity": integraBmodemTxCapacity,
       "integraBmodemACMengine": integraBmodemACMengine,
       "integraBmodemCarrierOffset": integraBmodemCarrierOffset,
       "integraBsystem": integraBsystem,
       "integraBsysCPUtemperature": integraBsysCPUtemperature,
       "integraBsysLicenseExpire": integraBsysLicenseExpire,
       "integraBsysLicenseGenStatus": integraBsysLicenseGenStatus,
       "integraBsysPSUvoltage": integraBsysPSUvoltage,
       "integraBsysPSUcurrent": integraBsysPSUcurrent,
       "integraBsysPSUpower": integraBsysPSUpower,
       "integraBsysBoardTemperature": integraBsysBoardTemperature,
       "integraBsysFreeMemory": integraBsysFreeMemory,
       "integraBsysCPUidle": integraBsysCPUidle,
       "integraBethernet": integraBethernet,
       "integraBifStatusTable": integraBifStatusTable,
       "integraBifPortEntry": integraBifPortEntry,
       "integraBifPortStatIndex": integraBifPortStatIndex,
       "integraBifPortStatDescr": integraBifPortStatDescr,
       "integraBifPortType": integraBifPortType,
       "integraBifPortMtu": integraBifPortMtu,
       "integraBifPortSpeed": integraBifPortSpeed,
       "integraBifPortPhysAddress": integraBifPortPhysAddress,
       "integraBifPortAdminStatus": integraBifPortAdminStatus,
       "integraBifPortOperStatus": integraBifPortOperStatus,
       "integraBifPortLastChange": integraBifPortLastChange,
       "integraBifPortAutoneg": integraBifPortAutoneg,
       "integraBifPortDuplex": integraBifPortDuplex,
       "integraBifPortSyncEthActive": integraBifPortSyncEthActive,
       "integraBifPortSyncEthPrio": integraBifPortSyncEthPrio,
       "integraBifPortFlowControl": integraBifPortFlowControl,
       "integraBifStatisticsTable": integraBifStatisticsTable,
       "integraBifPortStcEntry": integraBifPortStcEntry,
       "integraBifPortStcIndex": integraBifPortStcIndex,
       "integraBifPortStcDescr": integraBifPortStcDescr,
       "integraBifTimePassed": integraBifTimePassed,
       "integraBifIngressPackets": integraBifIngressPackets,
       "integraBifIngressBytes": integraBifIngressBytes,
       "integraBifEgressPackets": integraBifEgressPackets,
       "integraBifEgressBytes": integraBifEgressBytes,
       "integraBifEtherStatsMulticastPkts": integraBifEtherStatsMulticastPkts,
       "integraBifEtherStatsBroadcastPkts": integraBifEtherStatsBroadcastPkts,
       "integraBifEtherStatsPkts64Octets": integraBifEtherStatsPkts64Octets,
       "integraBifEtherStatsPkts65to127Octets": integraBifEtherStatsPkts65to127Octets,
       "integraBifEtherStatsPkts128to255Octets": integraBifEtherStatsPkts128to255Octets,
       "integraBifEtherStatsPkts256to511Octets": integraBifEtherStatsPkts256to511Octets,
       "integraBifEtherStatsPkts512to1023Octets": integraBifEtherStatsPkts512to1023Octets,
       "integraBifEtherStatsPkts1024to1518Octets": integraBifEtherStatsPkts1024to1518Octets,
       "integraBifEtherStatsOversizePkts": integraBifEtherStatsOversizePkts,
       "integraBifEtherRxOversizePkts": integraBifEtherRxOversizePkts,
       "integraBifEtherTxOversizePkts": integraBifEtherTxOversizePkts,
       "integraBifEtherStatsOctets": integraBifEtherStatsOctets,
       "integraBifEtherStatsPkts": integraBifEtherStatsPkts,
       "integraBifEtherStatsTXNoErrors": integraBifEtherStatsTXNoErrors,
       "integraBifEtherStatsRXNoErrors": integraBifEtherStatsRXNoErrors,
       "integraBifEtherStatsPkts1519to1522Octets": integraBifEtherStatsPkts1519to1522Octets,
       "integraBifIfInOctets": integraBifIfInOctets,
       "integraBifIfOutOctets": integraBifIfOutOctets,
       "integraBifDot1dTpPortInFrames": integraBifDot1dTpPortInFrames,
       "integraBifDot1dTpPortOutFrames": integraBifDot1dTpPortOutFrames,
       "integraBifReceivedPkts64Octets": integraBifReceivedPkts64Octets,
       "integraBifTransmittedPkts64Octets": integraBifTransmittedPkts64Octets,
       "integraBifReceivedPkts65to127Octets": integraBifReceivedPkts65to127Octets,
       "integraBifTransmittedPkts65to127Octets": integraBifTransmittedPkts65to127Octets,
       "integraBifReceivedPkts128to255Octets": integraBifReceivedPkts128to255Octets,
       "integraBifTransmittedPkts128to255Octets": integraBifTransmittedPkts128to255Octets,
       "integraBifReceivedPkts256to511Octets": integraBifReceivedPkts256to511Octets,
       "integraBifTransmittedPkts256to511Octets": integraBifTransmittedPkts256to511Octets,
       "integraBifReceivedPkts512to1023Octets": integraBifReceivedPkts512to1023Octets,
       "integraBifTransmittedPkts512to1023Octets": integraBifTransmittedPkts512to1023Octets,
       "integraBifReceivedPkts1024to1518Octets": integraBifReceivedPkts1024to1518Octets,
       "integraBifTransmittedPkts1024to1518Octets": integraBifTransmittedPkts1024to1518Octets,
       "integraBifIfInBroadcastPkts": integraBifIfInBroadcastPkts,
       "integraBifIfOutBroadcastPkts": integraBifIfOutBroadcastPkts,
       "integraBifIfInMulticastPkts": integraBifIfInMulticastPkts,
       "integraBifIfOutMulticastPkts": integraBifIfOutMulticastPkts,
       "integraBifDot3InPauseFrames": integraBifDot3InPauseFrames,
       "integraBifDot3OutPauseFrames": integraBifDot3OutPauseFrames,
       "integraBifEtherStatsUndersizePkts": integraBifEtherStatsUndersizePkts,
       "integraBifEtherStatsFragments": integraBifEtherStatsFragments,
       "integraBifEtherStatsCRCAlignErrors": integraBifEtherStatsCRCAlignErrors,
       "integraBifEtherStatsJabbers": integraBifEtherStatsJabbers,
       "integraBifIngressBPS": integraBifIngressBPS,
       "integraBifIngressPPS": integraBifIngressPPS,
       "integraBifEgressBPS": integraBifEgressBPS,
       "integraBifEgressPPS": integraBifEgressPPS,
       "integraBifMAClearnLimitDropIngressPackets": integraBifMAClearnLimitDropIngressPackets,
       "integraBifL2cacheDropIngressPackets": integraBifL2cacheDropIngressPackets,
       "integraBifEFMdropIngressPackets": integraBifEFMdropIngressPackets,
       "integraBifEFMdropEgressPackets": integraBifEFMdropEgressPackets,
       "integraBifSTPdropIngressPackets": integraBifSTPdropIngressPackets,
       "integraBifSTPdropEgressPackets": integraBifSTPdropEgressPackets,
       "integraBifMRUdropIngressPackets": integraBifMRUdropIngressPackets,
       "integraBifMRUdropEgressPackets": integraBifMRUdropEgressPackets,
       "integraBifFilterDropIngressPackets": integraBifFilterDropIngressPackets,
       "integraBifFlowClassifierDropIngressPackets": integraBifFlowClassifierDropIngressPackets,
       "integraBifFlowClassifierDropEgressPackets": integraBifFlowClassifierDropEgressPackets,
       "integraBifIllegalSAdropIngressPackets": integraBifIllegalSAdropIngressPackets,
       "integraBifPortRateLimitDropIngressPackets": integraBifPortRateLimitDropIngressPackets,
       "integraBifPortRateLimitDropIngressBytes": integraBifPortRateLimitDropIngressBytes,
       "integraBifPausePFCframesGeneratedIngressPackets": integraBifPausePFCframesGeneratedIngressPackets,
       "integraBifPausePFCframesGeneratedEgressPackets": integraBifPausePFCframesGeneratedEgressPackets,
       "integraBifRateLimitDropForUnknownUnicastIngressPackets": integraBifRateLimitDropForUnknownUnicastIngressPackets,
       "integraBifRateLimitDropForUnknownUnicastIngressBytes": integraBifRateLimitDropForUnknownUnicastIngressBytes,
       "integraBifRateLimitDropForBroadcastIngressPackets": integraBifRateLimitDropForBroadcastIngressPackets,
       "integraBifRateLimitDropForBroadcastIngressBytes": integraBifRateLimitDropForBroadcastIngressBytes,
       "integraBifRateLimitDropForKnownMulticastIngressPackets": integraBifRateLimitDropForKnownMulticastIngressPackets,
       "integraBifRateLimitDropForKnownMulticastIngressBytes": integraBifRateLimitDropForKnownMulticastIngressBytes,
       "integraBifRateLimitDropForUnknownMulticastIngressPackets": integraBifRateLimitDropForUnknownMulticastIngressPackets,
       "integraBifRateLimitDropForUnknownMulticastIngressBytes": integraBifRateLimitDropForUnknownMulticastIngressBytes,
       "integraBifAllCoSQoutPackets": integraBifAllCoSQoutPackets,
       "integraBifAllCoSQoutBytes": integraBifAllCoSQoutBytes,
       "integraBifAllCoSQdroppedPackets": integraBifAllCoSQdroppedPackets,
       "integraBifAllCoSQdroppedBytes": integraBifAllCoSQdroppedBytes,
       "integraBifProcessedRxPackets": integraBifProcessedRxPackets,
       "integraBifProcessedRxBytes": integraBifProcessedRxBytes,
       "integraBifQosStatisticsTable": integraBifQosStatisticsTable,
       "integraBifCosqEntry": integraBifCosqEntry,
       "integraBifCosqIfaceIndex": integraBifCosqIfaceIndex,
       "integraBifCosqIfaceDescr": integraBifCosqIfaceDescr,
       "integraBifCosqStatDroppedPacketsCoSQ0": integraBifCosqStatDroppedPacketsCoSQ0,
       "integraBifCosqStatDroppedBytesCoSQ0": integraBifCosqStatDroppedBytesCoSQ0,
       "integraBifCosqStatGreenDiscardDroppedPacketsCoSQ0": integraBifCosqStatGreenDiscardDroppedPacketsCoSQ0,
       "integraBifCosqStatYellowDiscardDroppedPacketsCoSQ0": integraBifCosqStatYellowDiscardDroppedPacketsCoSQ0,
       "integraBifCosqStatOutPacketsCoSQ0": integraBifCosqStatOutPacketsCoSQ0,
       "integraBifCosqStatOutBytesCoSQ0": integraBifCosqStatOutBytesCoSQ0,
       "integraBifCosqStatDroppedPacketsCoSQ1": integraBifCosqStatDroppedPacketsCoSQ1,
       "integraBifCosqStatDroppedBytesCoSQ1": integraBifCosqStatDroppedBytesCoSQ1,
       "integraBifCosqStatGreenDiscardDroppedPacketsCoSQ1": integraBifCosqStatGreenDiscardDroppedPacketsCoSQ1,
       "integraBifCosqStatYellowDiscardDroppedPacketsCoSQ1": integraBifCosqStatYellowDiscardDroppedPacketsCoSQ1,
       "integraBifCosqStatOutPacketsCoSQ1": integraBifCosqStatOutPacketsCoSQ1,
       "integraBifCosqStatOutBytesCoSQ1": integraBifCosqStatOutBytesCoSQ1,
       "integraBifCosqStatDroppedPacketsCoSQ2": integraBifCosqStatDroppedPacketsCoSQ2,
       "integraBifCosqStatDroppedBytesCoSQ2": integraBifCosqStatDroppedBytesCoSQ2,
       "integraBifCosqStatGreenDiscardDroppedPacketsCoSQ2": integraBifCosqStatGreenDiscardDroppedPacketsCoSQ2,
       "integraBifCosqStatYellowDiscardDroppedPacketsCoSQ2": integraBifCosqStatYellowDiscardDroppedPacketsCoSQ2,
       "integraBifCosqStatOutPacketsCoSQ2": integraBifCosqStatOutPacketsCoSQ2,
       "integraBifCosqStatOutBytesCoSQ2": integraBifCosqStatOutBytesCoSQ2,
       "integraBifCosqStatDroppedPacketsCoSQ3": integraBifCosqStatDroppedPacketsCoSQ3,
       "integraBifCosqStatDroppedBytesCoSQ3": integraBifCosqStatDroppedBytesCoSQ3,
       "integraBifCosqStatGreenDiscardDroppedPacketsCoSQ3": integraBifCosqStatGreenDiscardDroppedPacketsCoSQ3,
       "integraBifCosqStatYellowDiscardDroppedPacketsCoSQ3": integraBifCosqStatYellowDiscardDroppedPacketsCoSQ3,
       "integraBifCosqStatOutPacketsCoSQ3": integraBifCosqStatOutPacketsCoSQ3,
       "integraBifCosqStatOutBytesCoSQ3": integraBifCosqStatOutBytesCoSQ3,
       "integraBifCosqStatDroppedPacketsCoSQ4": integraBifCosqStatDroppedPacketsCoSQ4,
       "integraBifCosqStatDroppedBytesCoSQ4": integraBifCosqStatDroppedBytesCoSQ4,
       "integraBifCosqStatGreenDiscardDroppedPacketsCoSQ4": integraBifCosqStatGreenDiscardDroppedPacketsCoSQ4,
       "integraBifCosqStatYellowDiscardDroppedPacketsCoSQ4": integraBifCosqStatYellowDiscardDroppedPacketsCoSQ4,
       "integraBifCosqStatOutPacketsCoSQ4": integraBifCosqStatOutPacketsCoSQ4,
       "integraBifCosqStatOutBytesCoSQ4": integraBifCosqStatOutBytesCoSQ4,
       "integraBifCosqStatDroppedPacketsCoSQ5": integraBifCosqStatDroppedPacketsCoSQ5,
       "integraBifCosqStatDroppedBytesCoSQ5": integraBifCosqStatDroppedBytesCoSQ5,
       "integraBifCosqStatGreenDiscardDroppedPacketsCoSQ5": integraBifCosqStatGreenDiscardDroppedPacketsCoSQ5,
       "integraBifCosqStatYellowDiscardDroppedPacketsCoSQ5": integraBifCosqStatYellowDiscardDroppedPacketsCoSQ5,
       "integraBifCosqStatOutPacketsCoSQ5": integraBifCosqStatOutPacketsCoSQ5,
       "integraBifCosqStatOutBytesCoSQ5": integraBifCosqStatOutBytesCoSQ5,
       "integraBifCosqStatDroppedPacketsCoSQ6": integraBifCosqStatDroppedPacketsCoSQ6,
       "integraBifCosqStatDroppedBytesCoSQ6": integraBifCosqStatDroppedBytesCoSQ6,
       "integraBifCosqStatGreenDiscardDroppedPacketsCoSQ6": integraBifCosqStatGreenDiscardDroppedPacketsCoSQ6,
       "integraBifCosqStatYellowDiscardDroppedPacketsCoSQ6": integraBifCosqStatYellowDiscardDroppedPacketsCoSQ6,
       "integraBifCosqStatOutPacketsCoSQ6": integraBifCosqStatOutPacketsCoSQ6,
       "integraBifCosqStatOutBytesCoSQ6": integraBifCosqStatOutBytesCoSQ6,
       "integraBifCosqStatDroppedPacketsCoSQ7": integraBifCosqStatDroppedPacketsCoSQ7,
       "integraBifCosqStatDroppedBytesCoSQ7": integraBifCosqStatDroppedBytesCoSQ7,
       "integraBifCosqStatGreenDiscardDroppedPacketsCoSQ7": integraBifCosqStatGreenDiscardDroppedPacketsCoSQ7,
       "integraBifCosqStatYellowDiscardDroppedPacketsCoSQ7": integraBifCosqStatYellowDiscardDroppedPacketsCoSQ7,
       "integraBifCosqStatOutPacketsCoSQ7": integraBifCosqStatOutPacketsCoSQ7,
       "integraBifCosqStatOutBytesCoSQ7": integraBifCosqStatOutBytesCoSQ7,
       "integraBexecuteConfig": integraBexecuteConfig,
       "integraBneedStore": integraBneedStore,
       "integraBstoreConfig": integraBstoreConfig,
       "integraBnetCfg": integraBnetCfg,
       "integraBnetCfgIPaddress": integraBnetCfgIPaddress,
       "integraBnetCfgIPmask": integraBnetCfgIPmask,
       "integraBnetCfgIPgateway": integraBnetCfgIPgateway,
       "integraBnetCfgRemoteIPaddress": integraBnetCfgRemoteIPaddress,
       "integraBConformance": integraBConformance,
       "integraBCompliances": integraBCompliances,
       "integraBCompliance": integraBCompliance,
       "integraBGroups": integraBGroups,
       "integraBMiscGroup": integraBMiscGroup,
       "integraBRadioGroup": integraBRadioGroup,
       "integraBModemGroup": integraBModemGroup,
       "integraBSystemGroup": integraBSystemGroup,
       "integraBEthernetGeneralGroup": integraBEthernetGeneralGroup,
       "integraBEthernetMiiPortGroup": integraBEthernetMiiPortGroup,
       "integraBEthernetQosQueueGroup": integraBEthernetQosQueueGroup}
)
