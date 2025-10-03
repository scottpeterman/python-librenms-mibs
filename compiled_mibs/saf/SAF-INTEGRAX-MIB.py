# SNMP MIB module (SAF-INTEGRAX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\saf\SAF-INTEGRAX-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:24:49 2025
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

integraX = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10)
)
if mibBuilder.loadTexts:
    integraX.setRevisions(
        ("2020-06-26 00:00",
         "2020-05-19 00:00",
         "2020-05-08 00:00",
         "2020-01-14 00:00",
         "2019-11-27 00:00",
         "2019-06-11 00:00",
         "2019-04-23 00:00",
         "2019-03-07 00:00",
         "2019-03-06 00:00",
         "2019-02-17 00:00")
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

_IntegraXtimestamp_Type = DateAndTime
_IntegraXtimestamp_Object = MibScalar
integraXtimestamp = _IntegraXtimestamp_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 1),
    _IntegraXtimestamp_Type()
)
integraXtimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXtimestamp.setStatus("current")
_IntegraXradio_ObjectIdentity = ObjectIdentity
integraXradio = _IntegraXradio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2)
)
_IntegraXradioA_ObjectIdentity = ObjectIdentity
integraXradioA = _IntegraXradioA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 1)
)
_IntegraXradioAtxPower_Type = Integer32
_IntegraXradioAtxPower_Object = MibScalar
integraXradioAtxPower = _IntegraXradioAtxPower_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 1, 1),
    _IntegraXradioAtxPower_Type()
)
integraXradioAtxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioAtxPower.setStatus("current")
if mibBuilder.loadTexts:
    integraXradioAtxPower.setUnits("dBm")
_IntegraXradioAtxFrequency_Type = Integer32
_IntegraXradioAtxFrequency_Object = MibScalar
integraXradioAtxFrequency = _IntegraXradioAtxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 1, 2),
    _IntegraXradioAtxFrequency_Type()
)
integraXradioAtxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioAtxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    integraXradioAtxFrequency.setUnits("kHz")
_IntegraXradioArxLevel_Type = Integer32
_IntegraXradioArxLevel_Object = MibScalar
integraXradioArxLevel = _IntegraXradioArxLevel_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 1, 3),
    _IntegraXradioArxLevel_Type()
)
integraXradioArxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioArxLevel.setStatus("current")
if mibBuilder.loadTexts:
    integraXradioArxLevel.setUnits("dBm")


class _IntegraXradioArxLevelState_Type(Integer32):
    """Custom type integraXradioArxLevelState based on Integer32"""
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


_IntegraXradioArxLevelState_Type.__name__ = "Integer32"
_IntegraXradioArxLevelState_Object = MibScalar
integraXradioArxLevelState = _IntegraXradioArxLevelState_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 1, 4),
    _IntegraXradioArxLevelState_Type()
)
integraXradioArxLevelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioArxLevelState.setStatus("current")


class _IntegraXradioAside_Type(Integer32):
    """Custom type integraXradioAside based on Integer32"""
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


_IntegraXradioAside_Type.__name__ = "Integer32"
_IntegraXradioAside_Object = MibScalar
integraXradioAside = _IntegraXradioAside_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 1, 5),
    _IntegraXradioAside_Type()
)
integraXradioAside.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioAside.setStatus("current")


class _IntegraXradioAtxMute_Type(Integer32):
    """Custom type integraXradioAtxMute based on Integer32"""
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


_IntegraXradioAtxMute_Type.__name__ = "Integer32"
_IntegraXradioAtxMute_Object = MibScalar
integraXradioAtxMute = _IntegraXradioAtxMute_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 1, 6),
    _IntegraXradioAtxMute_Type()
)
integraXradioAtxMute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioAtxMute.setStatus("current")


class _IntegraXradioAtxMuteDuration_Type(Integer32):
    """Custom type integraXradioAtxMuteDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214748364),
    )


_IntegraXradioAtxMuteDuration_Type.__name__ = "Integer32"
_IntegraXradioAtxMuteDuration_Object = MibScalar
integraXradioAtxMuteDuration = _IntegraXradioAtxMuteDuration_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 1, 7),
    _IntegraXradioAtxMuteDuration_Type()
)
integraXradioAtxMuteDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioAtxMuteDuration.setStatus("current")
if mibBuilder.loadTexts:
    integraXradioAtxMuteDuration.setUnits("s")
_IntegraXradioAduplexShift_Type = Integer32
_IntegraXradioAduplexShift_Object = MibScalar
integraXradioAduplexShift = _IntegraXradioAduplexShift_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 1, 8),
    _IntegraXradioAduplexShift_Type()
)
integraXradioAduplexShift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioAduplexShift.setStatus("current")
if mibBuilder.loadTexts:
    integraXradioAduplexShift.setUnits("kHz")
_IntegraXradioArxFrequency_Type = Integer32
_IntegraXradioArxFrequency_Object = MibScalar
integraXradioArxFrequency = _IntegraXradioArxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 1, 9),
    _IntegraXradioArxFrequency_Type()
)
integraXradioArxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioArxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    integraXradioArxFrequency.setUnits("kHz")
_IntegraXradioAtemperature_Type = FixedDiv10
_IntegraXradioAtemperature_Object = MibScalar
integraXradioAtemperature = _IntegraXradioAtemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 1, 10),
    _IntegraXradioAtemperature_Type()
)
integraXradioAtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioAtemperature.setStatus("current")
if mibBuilder.loadTexts:
    integraXradioAtemperature.setUnits("C")


class _IntegraXradioApll_Type(Integer32):
    """Custom type integraXradioApll based on Integer32"""
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


_IntegraXradioApll_Type.__name__ = "Integer32"
_IntegraXradioApll_Object = MibScalar
integraXradioApll = _IntegraXradioApll_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 1, 11),
    _IntegraXradioApll_Type()
)
integraXradioApll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioApll.setStatus("current")
_IntegraXradioArangesTable_Object = MibTable
integraXradioArangesTable = _IntegraXradioArangesTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 1, 12)
)
if mibBuilder.loadTexts:
    integraXradioArangesTable.setStatus("current")
_IntegraXradioArangeEntry_Object = MibTableRow
integraXradioArangeEntry = _IntegraXradioArangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 1, 12, 1)
)
integraXradioArangeEntry.setIndexNames(
    (0, "SAF-INTEGRAX-MIB", "integraXradioArangeEntryIndex"),
)
if mibBuilder.loadTexts:
    integraXradioArangeEntry.setStatus("current")


class _IntegraXradioArangeEntryIndex_Type(Integer32):
    """Custom type integraXradioArangeEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IntegraXradioArangeEntryIndex_Type.__name__ = "Integer32"
_IntegraXradioArangeEntryIndex_Object = MibTableColumn
integraXradioArangeEntryIndex = _IntegraXradioArangeEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 1, 12, 1, 1),
    _IntegraXradioArangeEntryIndex_Type()
)
integraXradioArangeEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioArangeEntryIndex.setStatus("current")


class _IntegraXradioArangeDescr_Type(DisplayString):
    """Custom type integraXradioArangeDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntegraXradioArangeDescr_Type.__name__ = "DisplayString"
_IntegraXradioArangeDescr_Object = MibTableColumn
integraXradioArangeDescr = _IntegraXradioArangeDescr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 1, 12, 1, 2),
    _IntegraXradioArangeDescr_Type()
)
integraXradioArangeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioArangeDescr.setStatus("current")
_IntegraXradioArangeTxPower_Type = Integer32
_IntegraXradioArangeTxPower_Object = MibTableColumn
integraXradioArangeTxPower = _IntegraXradioArangeTxPower_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 1, 12, 1, 3),
    _IntegraXradioArangeTxPower_Type()
)
integraXradioArangeTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioArangeTxPower.setStatus("current")
if mibBuilder.loadTexts:
    integraXradioArangeTxPower.setUnits("dBm")
_IntegraXradioArangeTxFrequency_Type = Integer32
_IntegraXradioArangeTxFrequency_Object = MibTableColumn
integraXradioArangeTxFrequency = _IntegraXradioArangeTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 1, 12, 1, 4),
    _IntegraXradioArangeTxFrequency_Type()
)
integraXradioArangeTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioArangeTxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    integraXradioArangeTxFrequency.setUnits("kHz")
_IntegraXradioB_ObjectIdentity = ObjectIdentity
integraXradioB = _IntegraXradioB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 2)
)
_IntegraXradioBtxPower_Type = Integer32
_IntegraXradioBtxPower_Object = MibScalar
integraXradioBtxPower = _IntegraXradioBtxPower_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 2, 1),
    _IntegraXradioBtxPower_Type()
)
integraXradioBtxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioBtxPower.setStatus("current")
if mibBuilder.loadTexts:
    integraXradioBtxPower.setUnits("dBm")
_IntegraXradioBtxFrequency_Type = Integer32
_IntegraXradioBtxFrequency_Object = MibScalar
integraXradioBtxFrequency = _IntegraXradioBtxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 2, 2),
    _IntegraXradioBtxFrequency_Type()
)
integraXradioBtxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioBtxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    integraXradioBtxFrequency.setUnits("kHz")
_IntegraXradioBrxLevel_Type = Integer32
_IntegraXradioBrxLevel_Object = MibScalar
integraXradioBrxLevel = _IntegraXradioBrxLevel_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 2, 3),
    _IntegraXradioBrxLevel_Type()
)
integraXradioBrxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioBrxLevel.setStatus("current")
if mibBuilder.loadTexts:
    integraXradioBrxLevel.setUnits("dBm")


class _IntegraXradioBrxLevelState_Type(Integer32):
    """Custom type integraXradioBrxLevelState based on Integer32"""
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


_IntegraXradioBrxLevelState_Type.__name__ = "Integer32"
_IntegraXradioBrxLevelState_Object = MibScalar
integraXradioBrxLevelState = _IntegraXradioBrxLevelState_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 2, 4),
    _IntegraXradioBrxLevelState_Type()
)
integraXradioBrxLevelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioBrxLevelState.setStatus("current")


class _IntegraXradioBside_Type(Integer32):
    """Custom type integraXradioBside based on Integer32"""
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


_IntegraXradioBside_Type.__name__ = "Integer32"
_IntegraXradioBside_Object = MibScalar
integraXradioBside = _IntegraXradioBside_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 2, 5),
    _IntegraXradioBside_Type()
)
integraXradioBside.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioBside.setStatus("current")


class _IntegraXradioBtxMute_Type(Integer32):
    """Custom type integraXradioBtxMute based on Integer32"""
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


_IntegraXradioBtxMute_Type.__name__ = "Integer32"
_IntegraXradioBtxMute_Object = MibScalar
integraXradioBtxMute = _IntegraXradioBtxMute_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 2, 6),
    _IntegraXradioBtxMute_Type()
)
integraXradioBtxMute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioBtxMute.setStatus("current")


class _IntegraXradioBtxMuteDuration_Type(Integer32):
    """Custom type integraXradioBtxMuteDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214748364),
    )


_IntegraXradioBtxMuteDuration_Type.__name__ = "Integer32"
_IntegraXradioBtxMuteDuration_Object = MibScalar
integraXradioBtxMuteDuration = _IntegraXradioBtxMuteDuration_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 2, 7),
    _IntegraXradioBtxMuteDuration_Type()
)
integraXradioBtxMuteDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioBtxMuteDuration.setStatus("current")
if mibBuilder.loadTexts:
    integraXradioBtxMuteDuration.setUnits("s")
_IntegraXradioBduplexShift_Type = Integer32
_IntegraXradioBduplexShift_Object = MibScalar
integraXradioBduplexShift = _IntegraXradioBduplexShift_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 2, 8),
    _IntegraXradioBduplexShift_Type()
)
integraXradioBduplexShift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioBduplexShift.setStatus("current")
if mibBuilder.loadTexts:
    integraXradioBduplexShift.setUnits("kHz")
_IntegraXradioBrxFrequency_Type = Integer32
_IntegraXradioBrxFrequency_Object = MibScalar
integraXradioBrxFrequency = _IntegraXradioBrxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 2, 9),
    _IntegraXradioBrxFrequency_Type()
)
integraXradioBrxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioBrxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    integraXradioBrxFrequency.setUnits("kHz")
_IntegraXradioBtemperature_Type = FixedDiv10
_IntegraXradioBtemperature_Object = MibScalar
integraXradioBtemperature = _IntegraXradioBtemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 2, 10),
    _IntegraXradioBtemperature_Type()
)
integraXradioBtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioBtemperature.setStatus("current")
if mibBuilder.loadTexts:
    integraXradioBtemperature.setUnits("C")


class _IntegraXradioBpll_Type(Integer32):
    """Custom type integraXradioBpll based on Integer32"""
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


_IntegraXradioBpll_Type.__name__ = "Integer32"
_IntegraXradioBpll_Object = MibScalar
integraXradioBpll = _IntegraXradioBpll_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 2, 11),
    _IntegraXradioBpll_Type()
)
integraXradioBpll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioBpll.setStatus("current")
_IntegraXradioBrangesTable_Object = MibTable
integraXradioBrangesTable = _IntegraXradioBrangesTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 2, 12)
)
if mibBuilder.loadTexts:
    integraXradioBrangesTable.setStatus("current")
_IntegraXradioBrangeEntry_Object = MibTableRow
integraXradioBrangeEntry = _IntegraXradioBrangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 2, 12, 1)
)
integraXradioBrangeEntry.setIndexNames(
    (0, "SAF-INTEGRAX-MIB", "integraXradioBrangeEntryIndex"),
)
if mibBuilder.loadTexts:
    integraXradioBrangeEntry.setStatus("current")


class _IntegraXradioBrangeEntryIndex_Type(Integer32):
    """Custom type integraXradioBrangeEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IntegraXradioBrangeEntryIndex_Type.__name__ = "Integer32"
_IntegraXradioBrangeEntryIndex_Object = MibTableColumn
integraXradioBrangeEntryIndex = _IntegraXradioBrangeEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 2, 12, 1, 1),
    _IntegraXradioBrangeEntryIndex_Type()
)
integraXradioBrangeEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioBrangeEntryIndex.setStatus("current")


class _IntegraXradioBrangeDescr_Type(DisplayString):
    """Custom type integraXradioBrangeDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntegraXradioBrangeDescr_Type.__name__ = "DisplayString"
_IntegraXradioBrangeDescr_Object = MibTableColumn
integraXradioBrangeDescr = _IntegraXradioBrangeDescr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 2, 12, 1, 2),
    _IntegraXradioBrangeDescr_Type()
)
integraXradioBrangeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioBrangeDescr.setStatus("current")
_IntegraXradioBrangeTxPower_Type = Integer32
_IntegraXradioBrangeTxPower_Object = MibTableColumn
integraXradioBrangeTxPower = _IntegraXradioBrangeTxPower_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 2, 12, 1, 3),
    _IntegraXradioBrangeTxPower_Type()
)
integraXradioBrangeTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioBrangeTxPower.setStatus("current")
if mibBuilder.loadTexts:
    integraXradioBrangeTxPower.setUnits("dBm")
_IntegraXradioBrangeTxFrequency_Type = Integer32
_IntegraXradioBrangeTxFrequency_Object = MibTableColumn
integraXradioBrangeTxFrequency = _IntegraXradioBrangeTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 2, 2, 12, 1, 4),
    _IntegraXradioBrangeTxFrequency_Type()
)
integraXradioBrangeTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXradioBrangeTxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    integraXradioBrangeTxFrequency.setUnits("kHz")
_IntegraXmodem_ObjectIdentity = ObjectIdentity
integraXmodem = _IntegraXmodem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3)
)
_IntegraXmodemA_ObjectIdentity = ObjectIdentity
integraXmodemA = _IntegraXmodemA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1)
)


class _IntegraXmodemAacquireStatus_Type(Integer32):
    """Custom type integraXmodemAacquireStatus based on Integer32"""
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


_IntegraXmodemAacquireStatus_Type.__name__ = "Integer32"
_IntegraXmodemAacquireStatus_Object = MibScalar
integraXmodemAacquireStatus = _IntegraXmodemAacquireStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 1),
    _IntegraXmodemAacquireStatus_Type()
)
integraXmodemAacquireStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAacquireStatus.setStatus("current")
_IntegraXmodemAnormalizedMse_Type = Integer32
_IntegraXmodemAnormalizedMse_Object = MibScalar
integraXmodemAnormalizedMse = _IntegraXmodemAnormalizedMse_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 2),
    _IntegraXmodemAnormalizedMse_Type()
)
integraXmodemAnormalizedMse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAnormalizedMse.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemAnormalizedMse.setUnits("dB")
_IntegraXmodemAfecLoad_Type = DisplayString
_IntegraXmodemAfecLoad_Object = MibScalar
integraXmodemAfecLoad = _IntegraXmodemAfecLoad_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 3),
    _IntegraXmodemAfecLoad_Type()
)
integraXmodemAfecLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAfecLoad.setStatus("current")
_IntegraXmodemAxpdEst_Type = Integer32
_IntegraXmodemAxpdEst_Object = MibScalar
integraXmodemAxpdEst = _IntegraXmodemAxpdEst_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 4),
    _IntegraXmodemAxpdEst_Type()
)
integraXmodemAxpdEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAxpdEst.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemAxpdEst.setUnits("dB")


class _IntegraXmodemAacquireLastStatusDetails_Type(Integer32):
    """Custom type integraXmodemAacquireLastStatusDetails based on Integer32"""
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


_IntegraXmodemAacquireLastStatusDetails_Type.__name__ = "Integer32"
_IntegraXmodemAacquireLastStatusDetails_Object = MibScalar
integraXmodemAacquireLastStatusDetails = _IntegraXmodemAacquireLastStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 5),
    _IntegraXmodemAacquireLastStatusDetails_Type()
)
integraXmodemAacquireLastStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAacquireLastStatusDetails.setStatus("current")
_IntegraXmodemAtemperature_Type = FixedDiv10
_IntegraXmodemAtemperature_Object = MibScalar
integraXmodemAtemperature = _IntegraXmodemAtemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 6),
    _IntegraXmodemAtemperature_Type()
)
integraXmodemAtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAtemperature.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemAtemperature.setUnits("C")
_IntegraXmodemArxModulation_Type = DisplayString
_IntegraXmodemArxModulation_Object = MibScalar
integraXmodemArxModulation = _IntegraXmodemArxModulation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 7),
    _IntegraXmodemArxModulation_Type()
)
integraXmodemArxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemArxModulation.setStatus("current")
_IntegraXmodemAtxModulation_Type = DisplayString
_IntegraXmodemAtxModulation_Object = MibScalar
integraXmodemAtxModulation = _IntegraXmodemAtxModulation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 8),
    _IntegraXmodemAtxModulation_Type()
)
integraXmodemAtxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAtxModulation.setStatus("current")
_IntegraXmodemArxCapacity_Type = Integer32
_IntegraXmodemArxCapacity_Object = MibScalar
integraXmodemArxCapacity = _IntegraXmodemArxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 9),
    _IntegraXmodemArxCapacity_Type()
)
integraXmodemArxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemArxCapacity.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemArxCapacity.setUnits("kb/s")
_IntegraXmodemAtxCapacity_Type = Integer32
_IntegraXmodemAtxCapacity_Object = MibScalar
integraXmodemAtxCapacity = _IntegraXmodemAtxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 10),
    _IntegraXmodemAtxCapacity_Type()
)
integraXmodemAtxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAtxCapacity.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemAtxCapacity.setUnits("kb/s")


class _IntegraXmodemAacmEngine_Type(Integer32):
    """Custom type integraXmodemAacmEngine based on Integer32"""
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


_IntegraXmodemAacmEngine_Type.__name__ = "Integer32"
_IntegraXmodemAacmEngine_Object = MibScalar
integraXmodemAacmEngine = _IntegraXmodemAacmEngine_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 11),
    _IntegraXmodemAacmEngine_Type()
)
integraXmodemAacmEngine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAacmEngine.setStatus("current")
_IntegraXmodemAcarrierOffset_Type = Integer32
_IntegraXmodemAcarrierOffset_Object = MibScalar
integraXmodemAcarrierOffset = _IntegraXmodemAcarrierOffset_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 12),
    _IntegraXmodemAcarrierOffset_Type()
)
integraXmodemAcarrierOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAcarrierOffset.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemAcarrierOffset.setUnits("Hz")
_IntegraXmodemAcountTime_Type = Counter64
_IntegraXmodemAcountTime_Object = MibScalar
integraXmodemAcountTime = _IntegraXmodemAcountTime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 13),
    _IntegraXmodemAcountTime_Type()
)
integraXmodemAcountTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAcountTime.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemAcountTime.setUnits("s")
_IntegraXmodemAerroredBlock_Type = Counter64
_IntegraXmodemAerroredBlock_Object = MibScalar
integraXmodemAerroredBlock = _IntegraXmodemAerroredBlock_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 14),
    _IntegraXmodemAerroredBlock_Type()
)
integraXmodemAerroredBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAerroredBlock.setStatus("current")
_IntegraXmodemAerroredSecond_Type = Counter64
_IntegraXmodemAerroredSecond_Object = MibScalar
integraXmodemAerroredSecond = _IntegraXmodemAerroredSecond_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 15),
    _IntegraXmodemAerroredSecond_Type()
)
integraXmodemAerroredSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAerroredSecond.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemAerroredSecond.setUnits("s")
_IntegraXmodemAseverelyErroredSecond_Type = Counter64
_IntegraXmodemAseverelyErroredSecond_Object = MibScalar
integraXmodemAseverelyErroredSecond = _IntegraXmodemAseverelyErroredSecond_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 16),
    _IntegraXmodemAseverelyErroredSecond_Type()
)
integraXmodemAseverelyErroredSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAseverelyErroredSecond.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemAseverelyErroredSecond.setUnits("s")
_IntegraXmodemAbackgroundBlockError_Type = Counter64
_IntegraXmodemAbackgroundBlockError_Object = MibScalar
integraXmodemAbackgroundBlockError = _IntegraXmodemAbackgroundBlockError_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 17),
    _IntegraXmodemAbackgroundBlockError_Type()
)
integraXmodemAbackgroundBlockError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAbackgroundBlockError.setStatus("current")
_IntegraXmodemAtotalBlockNumber_Type = Counter64
_IntegraXmodemAtotalBlockNumber_Object = MibScalar
integraXmodemAtotalBlockNumber = _IntegraXmodemAtotalBlockNumber_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 18),
    _IntegraXmodemAtotalBlockNumber_Type()
)
integraXmodemAtotalBlockNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAtotalBlockNumber.setStatus("current")
_IntegraXmodemAerroredSecondRatio_Type = DisplayString
_IntegraXmodemAerroredSecondRatio_Object = MibScalar
integraXmodemAerroredSecondRatio = _IntegraXmodemAerroredSecondRatio_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 19),
    _IntegraXmodemAerroredSecondRatio_Type()
)
integraXmodemAerroredSecondRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAerroredSecondRatio.setStatus("current")
_IntegraXmodemAseverelyErroredSecondRatio_Type = DisplayString
_IntegraXmodemAseverelyErroredSecondRatio_Object = MibScalar
integraXmodemAseverelyErroredSecondRatio = _IntegraXmodemAseverelyErroredSecondRatio_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 20),
    _IntegraXmodemAseverelyErroredSecondRatio_Type()
)
integraXmodemAseverelyErroredSecondRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAseverelyErroredSecondRatio.setStatus("current")
_IntegraXmodemAbackgroundBlockErrorRatio_Type = DisplayString
_IntegraXmodemAbackgroundBlockErrorRatio_Object = MibScalar
integraXmodemAbackgroundBlockErrorRatio = _IntegraXmodemAbackgroundBlockErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 21),
    _IntegraXmodemAbackgroundBlockErrorRatio_Type()
)
integraXmodemAbackgroundBlockErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAbackgroundBlockErrorRatio.setStatus("current")
_IntegraXmodemAuptime_Type = Counter64
_IntegraXmodemAuptime_Object = MibScalar
integraXmodemAuptime = _IntegraXmodemAuptime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 22),
    _IntegraXmodemAuptime_Type()
)
integraXmodemAuptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAuptime.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemAuptime.setUnits("s")
_IntegraXmodemAunavailtime_Type = Counter64
_IntegraXmodemAunavailtime_Object = MibScalar
integraXmodemAunavailtime = _IntegraXmodemAunavailtime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 23),
    _IntegraXmodemAunavailtime_Type()
)
integraXmodemAunavailtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAunavailtime.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemAunavailtime.setUnits("s")
_IntegraXmodemAfecLdpcBlockCounter_Type = Counter64
_IntegraXmodemAfecLdpcBlockCounter_Object = MibScalar
integraXmodemAfecLdpcBlockCounter = _IntegraXmodemAfecLdpcBlockCounter_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 24),
    _IntegraXmodemAfecLdpcBlockCounter_Type()
)
integraXmodemAfecLdpcBlockCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAfecLdpcBlockCounter.setStatus("current")
_IntegraXmodemAfecLdpcUncorrectedBlockCounter_Type = Counter64
_IntegraXmodemAfecLdpcUncorrectedBlockCounter_Object = MibScalar
integraXmodemAfecLdpcUncorrectedBlockCounter = _IntegraXmodemAfecLdpcUncorrectedBlockCounter_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 25),
    _IntegraXmodemAfecLdpcUncorrectedBlockCounter_Type()
)
integraXmodemAfecLdpcUncorrectedBlockCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAfecLdpcUncorrectedBlockCounter.setStatus("current")
_IntegraXmodemAfecLdpcUncorrectedPercent_Type = Integer32
_IntegraXmodemAfecLdpcUncorrectedPercent_Object = MibScalar
integraXmodemAfecLdpcUncorrectedPercent = _IntegraXmodemAfecLdpcUncorrectedPercent_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 26),
    _IntegraXmodemAfecLdpcUncorrectedPercent_Type()
)
integraXmodemAfecLdpcUncorrectedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAfecLdpcUncorrectedPercent.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemAfecLdpcUncorrectedPercent.setUnits("%")
_IntegraXmodemAfecRsBlockCounter_Type = Counter64
_IntegraXmodemAfecRsBlockCounter_Object = MibScalar
integraXmodemAfecRsBlockCounter = _IntegraXmodemAfecRsBlockCounter_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 27),
    _IntegraXmodemAfecRsBlockCounter_Type()
)
integraXmodemAfecRsBlockCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAfecRsBlockCounter.setStatus("current")
_IntegraXmodemAfecRsUncorrectedBlockCounter_Type = Counter64
_IntegraXmodemAfecRsUncorrectedBlockCounter_Object = MibScalar
integraXmodemAfecRsUncorrectedBlockCounter = _IntegraXmodemAfecRsUncorrectedBlockCounter_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 28),
    _IntegraXmodemAfecRsUncorrectedBlockCounter_Type()
)
integraXmodemAfecRsUncorrectedBlockCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAfecRsUncorrectedBlockCounter.setStatus("current")
_IntegraXmodemAmodulationACMmin_Type = DisplayString
_IntegraXmodemAmodulationACMmin_Object = MibScalar
integraXmodemAmodulationACMmin = _IntegraXmodemAmodulationACMmin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 29),
    _IntegraXmodemAmodulationACMmin_Type()
)
integraXmodemAmodulationACMmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAmodulationACMmin.setStatus("current")
_IntegraXmodemAmodulationACMmax_Type = DisplayString
_IntegraXmodemAmodulationACMmax_Object = MibScalar
integraXmodemAmodulationACMmax = _IntegraXmodemAmodulationACMmax_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 1, 30),
    _IntegraXmodemAmodulationACMmax_Type()
)
integraXmodemAmodulationACMmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemAmodulationACMmax.setStatus("current")
_IntegraXmodemB_ObjectIdentity = ObjectIdentity
integraXmodemB = _IntegraXmodemB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2)
)


class _IntegraXmodemBacquireStatus_Type(Integer32):
    """Custom type integraXmodemBacquireStatus based on Integer32"""
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


_IntegraXmodemBacquireStatus_Type.__name__ = "Integer32"
_IntegraXmodemBacquireStatus_Object = MibScalar
integraXmodemBacquireStatus = _IntegraXmodemBacquireStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 1),
    _IntegraXmodemBacquireStatus_Type()
)
integraXmodemBacquireStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBacquireStatus.setStatus("current")
_IntegraXmodemBnormalizedMse_Type = Integer32
_IntegraXmodemBnormalizedMse_Object = MibScalar
integraXmodemBnormalizedMse = _IntegraXmodemBnormalizedMse_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 2),
    _IntegraXmodemBnormalizedMse_Type()
)
integraXmodemBnormalizedMse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBnormalizedMse.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemBnormalizedMse.setUnits("dB")
_IntegraXmodemBfecLoad_Type = DisplayString
_IntegraXmodemBfecLoad_Object = MibScalar
integraXmodemBfecLoad = _IntegraXmodemBfecLoad_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 3),
    _IntegraXmodemBfecLoad_Type()
)
integraXmodemBfecLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBfecLoad.setStatus("current")
_IntegraXmodemBxpdEst_Type = Integer32
_IntegraXmodemBxpdEst_Object = MibScalar
integraXmodemBxpdEst = _IntegraXmodemBxpdEst_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 4),
    _IntegraXmodemBxpdEst_Type()
)
integraXmodemBxpdEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBxpdEst.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemBxpdEst.setUnits("dB")


class _IntegraXmodemBacquireLastStatusDetails_Type(Integer32):
    """Custom type integraXmodemBacquireLastStatusDetails based on Integer32"""
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


_IntegraXmodemBacquireLastStatusDetails_Type.__name__ = "Integer32"
_IntegraXmodemBacquireLastStatusDetails_Object = MibScalar
integraXmodemBacquireLastStatusDetails = _IntegraXmodemBacquireLastStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 5),
    _IntegraXmodemBacquireLastStatusDetails_Type()
)
integraXmodemBacquireLastStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBacquireLastStatusDetails.setStatus("current")
_IntegraXmodemBtemperature_Type = FixedDiv10
_IntegraXmodemBtemperature_Object = MibScalar
integraXmodemBtemperature = _IntegraXmodemBtemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 6),
    _IntegraXmodemBtemperature_Type()
)
integraXmodemBtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBtemperature.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemBtemperature.setUnits("C")
_IntegraXmodemBrxModulation_Type = DisplayString
_IntegraXmodemBrxModulation_Object = MibScalar
integraXmodemBrxModulation = _IntegraXmodemBrxModulation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 7),
    _IntegraXmodemBrxModulation_Type()
)
integraXmodemBrxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBrxModulation.setStatus("current")
_IntegraXmodemBtxModulation_Type = DisplayString
_IntegraXmodemBtxModulation_Object = MibScalar
integraXmodemBtxModulation = _IntegraXmodemBtxModulation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 8),
    _IntegraXmodemBtxModulation_Type()
)
integraXmodemBtxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBtxModulation.setStatus("current")
_IntegraXmodemBrxCapacity_Type = Integer32
_IntegraXmodemBrxCapacity_Object = MibScalar
integraXmodemBrxCapacity = _IntegraXmodemBrxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 9),
    _IntegraXmodemBrxCapacity_Type()
)
integraXmodemBrxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBrxCapacity.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemBrxCapacity.setUnits("kb/s")
_IntegraXmodemBtxCapacity_Type = Integer32
_IntegraXmodemBtxCapacity_Object = MibScalar
integraXmodemBtxCapacity = _IntegraXmodemBtxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 10),
    _IntegraXmodemBtxCapacity_Type()
)
integraXmodemBtxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBtxCapacity.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemBtxCapacity.setUnits("kb/s")


class _IntegraXmodemBacmEngine_Type(Integer32):
    """Custom type integraXmodemBacmEngine based on Integer32"""
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


_IntegraXmodemBacmEngine_Type.__name__ = "Integer32"
_IntegraXmodemBacmEngine_Object = MibScalar
integraXmodemBacmEngine = _IntegraXmodemBacmEngine_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 11),
    _IntegraXmodemBacmEngine_Type()
)
integraXmodemBacmEngine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBacmEngine.setStatus("current")
_IntegraXmodemBcarrierOffset_Type = Integer32
_IntegraXmodemBcarrierOffset_Object = MibScalar
integraXmodemBcarrierOffset = _IntegraXmodemBcarrierOffset_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 12),
    _IntegraXmodemBcarrierOffset_Type()
)
integraXmodemBcarrierOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBcarrierOffset.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemBcarrierOffset.setUnits("Hz")
_IntegraXmodemBcountTime_Type = Counter64
_IntegraXmodemBcountTime_Object = MibScalar
integraXmodemBcountTime = _IntegraXmodemBcountTime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 13),
    _IntegraXmodemBcountTime_Type()
)
integraXmodemBcountTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBcountTime.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemBcountTime.setUnits("s")
_IntegraXmodemBerroredBlock_Type = Counter64
_IntegraXmodemBerroredBlock_Object = MibScalar
integraXmodemBerroredBlock = _IntegraXmodemBerroredBlock_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 14),
    _IntegraXmodemBerroredBlock_Type()
)
integraXmodemBerroredBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBerroredBlock.setStatus("current")
_IntegraXmodemBerroredSecond_Type = Counter64
_IntegraXmodemBerroredSecond_Object = MibScalar
integraXmodemBerroredSecond = _IntegraXmodemBerroredSecond_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 15),
    _IntegraXmodemBerroredSecond_Type()
)
integraXmodemBerroredSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBerroredSecond.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemBerroredSecond.setUnits("s")
_IntegraXmodemBseverelyErroredSecond_Type = Counter64
_IntegraXmodemBseverelyErroredSecond_Object = MibScalar
integraXmodemBseverelyErroredSecond = _IntegraXmodemBseverelyErroredSecond_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 16),
    _IntegraXmodemBseverelyErroredSecond_Type()
)
integraXmodemBseverelyErroredSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBseverelyErroredSecond.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemBseverelyErroredSecond.setUnits("s")
_IntegraXmodemBbackgroundBlockError_Type = Counter64
_IntegraXmodemBbackgroundBlockError_Object = MibScalar
integraXmodemBbackgroundBlockError = _IntegraXmodemBbackgroundBlockError_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 17),
    _IntegraXmodemBbackgroundBlockError_Type()
)
integraXmodemBbackgroundBlockError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBbackgroundBlockError.setStatus("current")
_IntegraXmodemBtotalBlockNumber_Type = Counter64
_IntegraXmodemBtotalBlockNumber_Object = MibScalar
integraXmodemBtotalBlockNumber = _IntegraXmodemBtotalBlockNumber_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 18),
    _IntegraXmodemBtotalBlockNumber_Type()
)
integraXmodemBtotalBlockNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBtotalBlockNumber.setStatus("current")
_IntegraXmodemBerroredSecondRatio_Type = DisplayString
_IntegraXmodemBerroredSecondRatio_Object = MibScalar
integraXmodemBerroredSecondRatio = _IntegraXmodemBerroredSecondRatio_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 19),
    _IntegraXmodemBerroredSecondRatio_Type()
)
integraXmodemBerroredSecondRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBerroredSecondRatio.setStatus("current")
_IntegraXmodemBseverelyErroredSecondRatio_Type = DisplayString
_IntegraXmodemBseverelyErroredSecondRatio_Object = MibScalar
integraXmodemBseverelyErroredSecondRatio = _IntegraXmodemBseverelyErroredSecondRatio_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 20),
    _IntegraXmodemBseverelyErroredSecondRatio_Type()
)
integraXmodemBseverelyErroredSecondRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBseverelyErroredSecondRatio.setStatus("current")
_IntegraXmodemBbackgroundBlockErrorRatio_Type = DisplayString
_IntegraXmodemBbackgroundBlockErrorRatio_Object = MibScalar
integraXmodemBbackgroundBlockErrorRatio = _IntegraXmodemBbackgroundBlockErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 21),
    _IntegraXmodemBbackgroundBlockErrorRatio_Type()
)
integraXmodemBbackgroundBlockErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBbackgroundBlockErrorRatio.setStatus("current")
_IntegraXmodemBuptime_Type = Counter64
_IntegraXmodemBuptime_Object = MibScalar
integraXmodemBuptime = _IntegraXmodemBuptime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 22),
    _IntegraXmodemBuptime_Type()
)
integraXmodemBuptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBuptime.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemBuptime.setUnits("s")
_IntegraXmodemBunavailtime_Type = Counter64
_IntegraXmodemBunavailtime_Object = MibScalar
integraXmodemBunavailtime = _IntegraXmodemBunavailtime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 23),
    _IntegraXmodemBunavailtime_Type()
)
integraXmodemBunavailtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBunavailtime.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemBunavailtime.setUnits("s")
_IntegraXmodemBfecLdpcBlockCounter_Type = Counter64
_IntegraXmodemBfecLdpcBlockCounter_Object = MibScalar
integraXmodemBfecLdpcBlockCounter = _IntegraXmodemBfecLdpcBlockCounter_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 24),
    _IntegraXmodemBfecLdpcBlockCounter_Type()
)
integraXmodemBfecLdpcBlockCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBfecLdpcBlockCounter.setStatus("current")
_IntegraXmodemBfecLdpcUncorrectedBlockCounter_Type = Counter64
_IntegraXmodemBfecLdpcUncorrectedBlockCounter_Object = MibScalar
integraXmodemBfecLdpcUncorrectedBlockCounter = _IntegraXmodemBfecLdpcUncorrectedBlockCounter_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 25),
    _IntegraXmodemBfecLdpcUncorrectedBlockCounter_Type()
)
integraXmodemBfecLdpcUncorrectedBlockCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBfecLdpcUncorrectedBlockCounter.setStatus("current")
_IntegraXmodemBfecLdpcUncorrectedPercent_Type = Integer32
_IntegraXmodemBfecLdpcUncorrectedPercent_Object = MibScalar
integraXmodemBfecLdpcUncorrectedPercent = _IntegraXmodemBfecLdpcUncorrectedPercent_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 26),
    _IntegraXmodemBfecLdpcUncorrectedPercent_Type()
)
integraXmodemBfecLdpcUncorrectedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBfecLdpcUncorrectedPercent.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemBfecLdpcUncorrectedPercent.setUnits("%")
_IntegraXmodemBfecRsBlockCounter_Type = Counter64
_IntegraXmodemBfecRsBlockCounter_Object = MibScalar
integraXmodemBfecRsBlockCounter = _IntegraXmodemBfecRsBlockCounter_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 27),
    _IntegraXmodemBfecRsBlockCounter_Type()
)
integraXmodemBfecRsBlockCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBfecRsBlockCounter.setStatus("current")
_IntegraXmodemBfecRsUncorrectedBlockCounter_Type = Counter64
_IntegraXmodemBfecRsUncorrectedBlockCounter_Object = MibScalar
integraXmodemBfecRsUncorrectedBlockCounter = _IntegraXmodemBfecRsUncorrectedBlockCounter_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 28),
    _IntegraXmodemBfecRsUncorrectedBlockCounter_Type()
)
integraXmodemBfecRsUncorrectedBlockCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBfecRsUncorrectedBlockCounter.setStatus("current")
_IntegraXmodemBmodulationACMmin_Type = DisplayString
_IntegraXmodemBmodulationACMmin_Object = MibScalar
integraXmodemBmodulationACMmin = _IntegraXmodemBmodulationACMmin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 29),
    _IntegraXmodemBmodulationACMmin_Type()
)
integraXmodemBmodulationACMmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBmodulationACMmin.setStatus("current")
_IntegraXmodemBmodulationACMmax_Type = DisplayString
_IntegraXmodemBmodulationACMmax_Object = MibScalar
integraXmodemBmodulationACMmax = _IntegraXmodemBmodulationACMmax_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 2, 30),
    _IntegraXmodemBmodulationACMmax_Type()
)
integraXmodemBmodulationACMmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBmodulationACMmax.setStatus("current")
_IntegraXmodemBandwidth_Type = Integer32
_IntegraXmodemBandwidth_Object = MibScalar
integraXmodemBandwidth = _IntegraXmodemBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 3),
    _IntegraXmodemBandwidth_Type()
)
integraXmodemBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    integraXmodemBandwidth.setUnits("kHz")
_IntegraXmodemModulation_Type = DisplayString
_IntegraXmodemModulation_Object = MibScalar
integraXmodemModulation = _IntegraXmodemModulation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 3, 4),
    _IntegraXmodemModulation_Type()
)
integraXmodemModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXmodemModulation.setStatus("current")
_IntegraXsystem_ObjectIdentity = ObjectIdentity
integraXsystem = _IntegraXsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4)
)
_IntegraXsysCPUtemperature_Type = FixedDiv10
_IntegraXsysCPUtemperature_Object = MibScalar
integraXsysCPUtemperature = _IntegraXsysCPUtemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 2),
    _IntegraXsysCPUtemperature_Type()
)
integraXsysCPUtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysCPUtemperature.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysCPUtemperature.setUnits("C")
_IntegraXsysLicenseExpire_Type = Gauge32
_IntegraXsysLicenseExpire_Object = MibScalar
integraXsysLicenseExpire = _IntegraXsysLicenseExpire_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 3),
    _IntegraXsysLicenseExpire_Type()
)
integraXsysLicenseExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysLicenseExpire.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysLicenseExpire.setUnits("s")


class _IntegraXsysLicenseGenStatus_Type(Integer32):
    """Custom type integraXsysLicenseGenStatus based on Integer32"""
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


_IntegraXsysLicenseGenStatus_Type.__name__ = "Integer32"
_IntegraXsysLicenseGenStatus_Object = MibScalar
integraXsysLicenseGenStatus = _IntegraXsysLicenseGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 4),
    _IntegraXsysLicenseGenStatus_Type()
)
integraXsysLicenseGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysLicenseGenStatus.setStatus("current")
_IntegraXsysPSUvoltage_Type = Integer32
_IntegraXsysPSUvoltage_Object = MibScalar
integraXsysPSUvoltage = _IntegraXsysPSUvoltage_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 5),
    _IntegraXsysPSUvoltage_Type()
)
integraXsysPSUvoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysPSUvoltage.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysPSUvoltage.setUnits("mV")
_IntegraXsysPSUcurrent_Type = Integer32
_IntegraXsysPSUcurrent_Object = MibScalar
integraXsysPSUcurrent = _IntegraXsysPSUcurrent_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 6),
    _IntegraXsysPSUcurrent_Type()
)
integraXsysPSUcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysPSUcurrent.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysPSUcurrent.setUnits("mA")
_IntegraXsysPSUpower_Type = Integer32
_IntegraXsysPSUpower_Object = MibScalar
integraXsysPSUpower = _IntegraXsysPSUpower_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 7),
    _IntegraXsysPSUpower_Type()
)
integraXsysPSUpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysPSUpower.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysPSUpower.setUnits("mW")
_IntegraXsysBoardTemperature_Type = FixedDiv10
_IntegraXsysBoardTemperature_Object = MibScalar
integraXsysBoardTemperature = _IntegraXsysBoardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 8),
    _IntegraXsysBoardTemperature_Type()
)
integraXsysBoardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysBoardTemperature.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysBoardTemperature.setUnits("C")
_IntegraXsysFreeMemory_Type = FixedDiv10
_IntegraXsysFreeMemory_Object = MibScalar
integraXsysFreeMemory = _IntegraXsysFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 9),
    _IntegraXsysFreeMemory_Type()
)
integraXsysFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysFreeMemory.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysFreeMemory.setUnits("%")
_IntegraXsysCPUidle_Type = FixedDiv10
_IntegraXsysCPUidle_Object = MibScalar
integraXsysCPUidle = _IntegraXsysCPUidle_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 10),
    _IntegraXsysCPUidle_Type()
)
integraXsysCPUidle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysCPUidle.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysCPUidle.setUnits("%")
_IntegraXsysDeviceType_Type = DisplayString
_IntegraXsysDeviceType_Object = MibScalar
integraXsysDeviceType = _IntegraXsysDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 11),
    _IntegraXsysDeviceType_Type()
)
integraXsysDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysDeviceType.setStatus("current")
_IntegraXsysDeviceSerial_Type = DisplayString
_IntegraXsysDeviceSerial_Object = MibScalar
integraXsysDeviceSerial = _IntegraXsysDeviceSerial_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 12),
    _IntegraXsysDeviceSerial_Type()
)
integraXsysDeviceSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysDeviceSerial.setStatus("current")
_IntegraXsysDeviceProductModel_Type = DisplayString
_IntegraXsysDeviceProductModel_Object = MibScalar
integraXsysDeviceProductModel = _IntegraXsysDeviceProductModel_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 13),
    _IntegraXsysDeviceProductModel_Type()
)
integraXsysDeviceProductModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysDeviceProductModel.setStatus("current")


class _IntegraXsysFanError_Type(Bits):
    """Custom type integraXsysFanError based on Bits"""
    namedValues = NamedValues(
        *(("no", 0),
          ("fan1", 1),
          ("fan2", 2),
          ("unknown", 3))
    )

_IntegraXsysFanError_Type.__name__ = "Bits"
_IntegraXsysFanError_Object = MibScalar
integraXsysFanError = _IntegraXsysFanError_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 14),
    _IntegraXsysFanError_Type()
)
integraXsysFanError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysFanError.setStatus("current")
_IntegraXsysSw1v0core_Type = FixedDiv20
_IntegraXsysSw1v0core_Object = MibScalar
integraXsysSw1v0core = _IntegraXsysSw1v0core_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 15),
    _IntegraXsysSw1v0core_Type()
)
integraXsysSw1v0core.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysSw1v0core.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysSw1v0core.setUnits("V")
_IntegraXsysSw1v0avdd_Type = FixedDiv20
_IntegraXsysSw1v0avdd_Object = MibScalar
integraXsysSw1v0avdd = _IntegraXsysSw1v0avdd_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 16),
    _IntegraXsysSw1v0avdd_Type()
)
integraXsysSw1v0avdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysSw1v0avdd.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysSw1v0avdd.setUnits("V")
_IntegraXsysSw1v2a_Type = FixedDiv20
_IntegraXsysSw1v2a_Object = MibScalar
integraXsysSw1v2a = _IntegraXsysSw1v2a_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 17),
    _IntegraXsysSw1v2a_Type()
)
integraXsysSw1v2a.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysSw1v2a.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysSw1v2a.setUnits("V")
_IntegraXsysSw1v5ddr_Type = FixedDiv20
_IntegraXsysSw1v5ddr_Object = MibScalar
integraXsysSw1v5ddr = _IntegraXsysSw1v5ddr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 18),
    _IntegraXsysSw1v5ddr_Type()
)
integraXsysSw1v5ddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysSw1v5ddr.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysSw1v5ddr.setUnits("V")
_IntegraXsysSw1v8_Type = FixedDiv20
_IntegraXsysSw1v8_Object = MibScalar
integraXsysSw1v8 = _IntegraXsysSw1v8_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 19),
    _IntegraXsysSw1v8_Type()
)
integraXsysSw1v8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysSw1v8.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysSw1v8.setUnits("V")
_IntegraXsysSw2v5_Type = FixedDiv20
_IntegraXsysSw2v5_Object = MibScalar
integraXsysSw2v5 = _IntegraXsysSw2v5_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 20),
    _IntegraXsysSw2v5_Type()
)
integraXsysSw2v5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysSw2v5.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysSw2v5.setUnits("V")
_IntegraXsysSw3v3_Type = FixedDiv20
_IntegraXsysSw3v3_Object = MibScalar
integraXsysSw3v3 = _IntegraXsysSw3v3_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 21),
    _IntegraXsysSw3v3_Type()
)
integraXsysSw3v3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysSw3v3.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysSw3v3.setUnits("V")
_IntegraXsysVttrefPs_Type = FixedDiv20
_IntegraXsysVttrefPs_Object = MibScalar
integraXsysVttrefPs = _IntegraXsysVttrefPs_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 22),
    _IntegraXsysVttrefPs_Type()
)
integraXsysVttrefPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysVttrefPs.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysVttrefPs.setUnits("V")
_IntegraXsysVttddrPs_Type = FixedDiv20
_IntegraXsysVttddrPs_Object = MibScalar
integraXsysVttddrPs = _IntegraXsysVttddrPs_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 23),
    _IntegraXsysVttddrPs_Type()
)
integraXsysVttddrPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysVttddrPs.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysVttddrPs.setUnits("V")
_IntegraXsysZq1v0_Type = FixedDiv20
_IntegraXsysZq1v0_Object = MibScalar
integraXsysZq1v0 = _IntegraXsysZq1v0_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 24),
    _IntegraXsysZq1v0_Type()
)
integraXsysZq1v0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysZq1v0.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysZq1v0.setUnits("V")
_IntegraXsysZq1v5_Type = FixedDiv20
_IntegraXsysZq1v5_Object = MibScalar
integraXsysZq1v5 = _IntegraXsysZq1v5_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 25),
    _IntegraXsysZq1v5_Type()
)
integraXsysZq1v5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysZq1v5.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysZq1v5.setUnits("V")
_IntegraXsysZq1v8_Type = FixedDiv20
_IntegraXsysZq1v8_Object = MibScalar
integraXsysZq1v8 = _IntegraXsysZq1v8_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 26),
    _IntegraXsysZq1v8_Type()
)
integraXsysZq1v8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysZq1v8.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysZq1v8.setUnits("V")
_IntegraXsysZq2v5_Type = FixedDiv20
_IntegraXsysZq2v5_Object = MibScalar
integraXsysZq2v5 = _IntegraXsysZq2v5_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 27),
    _IntegraXsysZq2v5_Type()
)
integraXsysZq2v5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysZq2v5.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysZq2v5.setUnits("V")
_IntegraXsysZq3v3_Type = FixedDiv20
_IntegraXsysZq3v3_Object = MibScalar
integraXsysZq3v3 = _IntegraXsysZq3v3_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 28),
    _IntegraXsysZq3v3_Type()
)
integraXsysZq3v3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysZq3v3.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysZq3v3.setUnits("V")
_IntegraXsys5v0d_Type = FixedDiv20
_IntegraXsys5v0d_Object = MibScalar
integraXsys5v0d = _IntegraXsys5v0d_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 29),
    _IntegraXsys5v0d_Type()
)
integraXsys5v0d.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsys5v0d.setStatus("current")
if mibBuilder.loadTexts:
    integraXsys5v0d.setUnits("V")
_IntegraXsysSw1v2_Type = FixedDiv20
_IntegraXsysSw1v2_Object = MibScalar
integraXsysSw1v2 = _IntegraXsysSw1v2_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 30),
    _IntegraXsysSw1v2_Type()
)
integraXsysSw1v2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysSw1v2.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysSw1v2.setUnits("V")
_IntegraXsysMdmVddcAvs_Type = FixedDiv20
_IntegraXsysMdmVddcAvs_Object = MibScalar
integraXsysMdmVddcAvs = _IntegraXsysMdmVddcAvs_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 31),
    _IntegraXsysMdmVddcAvs_Type()
)
integraXsysMdmVddcAvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysMdmVddcAvs.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysMdmVddcAvs.setUnits("V")
_IntegraXsysMdm3v3_Type = FixedDiv20
_IntegraXsysMdm3v3_Object = MibScalar
integraXsysMdm3v3 = _IntegraXsysMdm3v3_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 32),
    _IntegraXsysMdm3v3_Type()
)
integraXsysMdm3v3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysMdm3v3.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysMdm3v3.setUnits("V")
_IntegraXsysMdm1v0aPm_Type = FixedDiv20
_IntegraXsysMdm1v0aPm_Object = MibScalar
integraXsysMdm1v0aPm = _IntegraXsysMdm1v0aPm_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 33),
    _IntegraXsysMdm1v0aPm_Type()
)
integraXsysMdm1v0aPm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysMdm1v0aPm.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysMdm1v0aPm.setUnits("V")
_IntegraXsysMdm1v0a_Type = FixedDiv20
_IntegraXsysMdm1v0a_Object = MibScalar
integraXsysMdm1v0a = _IntegraXsysMdm1v0a_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 34),
    _IntegraXsysMdm1v0a_Type()
)
integraXsysMdm1v0a.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysMdm1v0a.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysMdm1v0a.setUnits("V")
_IntegraXsysMdm1v8a_Type = FixedDiv20
_IntegraXsysMdm1v8a_Object = MibScalar
integraXsysMdm1v8a = _IntegraXsysMdm1v8a_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 35),
    _IntegraXsysMdm1v8a_Type()
)
integraXsysMdm1v8a.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysMdm1v8a.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysMdm1v8a.setUnits("V")
_IntegraXsysMdmDAC02v5a_Type = FixedDiv20
_IntegraXsysMdmDAC02v5a_Object = MibScalar
integraXsysMdmDAC02v5a = _IntegraXsysMdmDAC02v5a_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 36),
    _IntegraXsysMdmDAC02v5a_Type()
)
integraXsysMdmDAC02v5a.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysMdmDAC02v5a.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysMdmDAC02v5a.setUnits("V")
_IntegraXsysMdmDAC12v5_Type = FixedDiv20
_IntegraXsysMdmDAC12v5_Object = MibScalar
integraXsysMdmDAC12v5 = _IntegraXsysMdmDAC12v5_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 37),
    _IntegraXsysMdmDAC12v5_Type()
)
integraXsysMdmDAC12v5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysMdmDAC12v5.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysMdmDAC12v5.setUnits("V")
_IntegraXsysMdmDAC22v5_Type = FixedDiv20
_IntegraXsysMdmDAC22v5_Object = MibScalar
integraXsysMdmDAC22v5 = _IntegraXsysMdmDAC22v5_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 38),
    _IntegraXsysMdmDAC22v5_Type()
)
integraXsysMdmDAC22v5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysMdmDAC22v5.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysMdmDAC22v5.setUnits("V")
_IntegraXsysMdm1v8io_Type = FixedDiv20
_IntegraXsysMdm1v8io_Object = MibScalar
integraXsysMdm1v8io = _IntegraXsysMdm1v8io_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 39),
    _IntegraXsysMdm1v8io_Type()
)
integraXsysMdm1v8io.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysMdm1v8io.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysMdm1v8io.setUnits("V")
_IntegraXsysMdm3v3io_Type = FixedDiv20
_IntegraXsysMdm3v3io_Object = MibScalar
integraXsysMdm3v3io = _IntegraXsysMdm3v3io_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 40),
    _IntegraXsysMdm3v3io_Type()
)
integraXsysMdm3v3io.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysMdm3v3io.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysMdm3v3io.setUnits("V")
_IntegraXsys3v3Radio_Type = FixedDiv20
_IntegraXsys3v3Radio_Object = MibScalar
integraXsys3v3Radio = _IntegraXsys3v3Radio_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 41),
    _IntegraXsys3v3Radio_Type()
)
integraXsys3v3Radio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsys3v3Radio.setStatus("current")
if mibBuilder.loadTexts:
    integraXsys3v3Radio.setUnits("V")
_IntegraXsysMdm4v0_Type = FixedDiv20
_IntegraXsysMdm4v0_Object = MibScalar
integraXsysMdm4v0 = _IntegraXsysMdm4v0_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 42),
    _IntegraXsysMdm4v0_Type()
)
integraXsysMdm4v0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysMdm4v0.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysMdm4v0.setUnits("V")
_IntegraXsys5v0nRadio_Type = FixedDiv20
_IntegraXsys5v0nRadio_Object = MibScalar
integraXsys5v0nRadio = _IntegraXsys5v0nRadio_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 43),
    _IntegraXsys5v0nRadio_Type()
)
integraXsys5v0nRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsys5v0nRadio.setStatus("current")
if mibBuilder.loadTexts:
    integraXsys5v0nRadio.setUnits("V")
_IntegraXsysCoreVddSns_Type = FixedDiv20
_IntegraXsysCoreVddSns_Object = MibScalar
integraXsysCoreVddSns = _IntegraXsysCoreVddSns_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 44),
    _IntegraXsysCoreVddSns_Type()
)
integraXsysCoreVddSns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysCoreVddSns.setStatus("current")
if mibBuilder.loadTexts:
    integraXsysCoreVddSns.setUnits("V")
_IntegraXsys40v0RadioSns_Type = FixedDiv20
_IntegraXsys40v0RadioSns_Object = MibScalar
integraXsys40v0RadioSns = _IntegraXsys40v0RadioSns_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 45),
    _IntegraXsys40v0RadioSns_Type()
)
integraXsys40v0RadioSns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsys40v0RadioSns.setStatus("current")
if mibBuilder.loadTexts:
    integraXsys40v0RadioSns.setUnits("V")
_IntegraXsysServices_ObjectIdentity = ObjectIdentity
integraXsysServices = _IntegraXsysServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 46)
)


class _IntegraXsysServicesReboot_Type(Integer32):
    """Custom type integraXsysServicesReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_IntegraXsysServicesReboot_Type.__name__ = "Integer32"
_IntegraXsysServicesReboot_Object = MibScalar
integraXsysServicesReboot = _IntegraXsysServicesReboot_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 46, 1),
    _IntegraXsysServicesReboot_Type()
)
integraXsysServicesReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraXsysServicesReboot.setStatus("current")


class _IntegraXsysServicesFtpSwitch_Type(Integer32):
    """Custom type integraXsysServicesFtpSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("unknown", 3))
    )


_IntegraXsysServicesFtpSwitch_Type.__name__ = "Integer32"
_IntegraXsysServicesFtpSwitch_Object = MibScalar
integraXsysServicesFtpSwitch = _IntegraXsysServicesFtpSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 46, 2),
    _IntegraXsysServicesFtpSwitch_Type()
)
integraXsysServicesFtpSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraXsysServicesFtpSwitch.setStatus("current")


class _IntegraXsysServicesFwCurrInfo_Type(DisplayString):
    """Custom type integraXsysServicesFwCurrInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntegraXsysServicesFwCurrInfo_Type.__name__ = "DisplayString"
_IntegraXsysServicesFwCurrInfo_Object = MibScalar
integraXsysServicesFwCurrInfo = _IntegraXsysServicesFwCurrInfo_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 46, 3),
    _IntegraXsysServicesFwCurrInfo_Type()
)
integraXsysServicesFwCurrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysServicesFwCurrInfo.setStatus("current")
_IntegraXsysServicesFwAvailView_Type = DisplayString
_IntegraXsysServicesFwAvailView_Object = MibScalar
integraXsysServicesFwAvailView = _IntegraXsysServicesFwAvailView_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 46, 4),
    _IntegraXsysServicesFwAvailView_Type()
)
integraXsysServicesFwAvailView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysServicesFwAvailView.setStatus("current")


class _IntegraXsysServicesFwRemove_Type(Integer32):
    """Custom type integraXsysServicesFwRemove based on Integer32"""
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
        *(("candfw1", 1),
          ("candfw2", 2),
          ("candfw3", 3),
          ("candfw4", 4),
          ("candfw5", 5))
    )


_IntegraXsysServicesFwRemove_Type.__name__ = "Integer32"
_IntegraXsysServicesFwRemove_Object = MibScalar
integraXsysServicesFwRemove = _IntegraXsysServicesFwRemove_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 46, 5),
    _IntegraXsysServicesFwRemove_Type()
)
integraXsysServicesFwRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraXsysServicesFwRemove.setStatus("current")


class _IntegraXsysServicesFwRemoveAll_Type(Integer32):
    """Custom type integraXsysServicesFwRemoveAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("removeAllCandfw", 1)
    )


_IntegraXsysServicesFwRemoveAll_Type.__name__ = "Integer32"
_IntegraXsysServicesFwRemoveAll_Object = MibScalar
integraXsysServicesFwRemoveAll = _IntegraXsysServicesFwRemoveAll_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 46, 6),
    _IntegraXsysServicesFwRemoveAll_Type()
)
integraXsysServicesFwRemoveAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraXsysServicesFwRemoveAll.setStatus("current")


class _IntegraXsysServicesFwUpload_Type(Integer32):
    """Custom type integraXsysServicesFwUpload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("upload", 1)
    )


_IntegraXsysServicesFwUpload_Type.__name__ = "Integer32"
_IntegraXsysServicesFwUpload_Object = MibScalar
integraXsysServicesFwUpload = _IntegraXsysServicesFwUpload_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 46, 7),
    _IntegraXsysServicesFwUpload_Type()
)
integraXsysServicesFwUpload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraXsysServicesFwUpload.setStatus("current")


class _IntegraXsysServicesFwInst_Type(Integer32):
    """Custom type integraXsysServicesFwInst based on Integer32"""
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
        *(("candfw1", 1),
          ("candfw2", 2),
          ("candfw3", 3),
          ("candfw4", 4),
          ("candfw5", 5))
    )


_IntegraXsysServicesFwInst_Type.__name__ = "Integer32"
_IntegraXsysServicesFwInst_Object = MibScalar
integraXsysServicesFwInst = _IntegraXsysServicesFwInst_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 46, 8),
    _IntegraXsysServicesFwInst_Type()
)
integraXsysServicesFwInst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraXsysServicesFwInst.setStatus("current")


class _IntegraXsysServicesFwSwitchRunning_Type(Integer32):
    """Custom type integraXsysServicesFwSwitchRunning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fw1", 1),
          ("fw2", 2))
    )


_IntegraXsysServicesFwSwitchRunning_Type.__name__ = "Integer32"
_IntegraXsysServicesFwSwitchRunning_Object = MibScalar
integraXsysServicesFwSwitchRunning = _IntegraXsysServicesFwSwitchRunning_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 46, 9),
    _IntegraXsysServicesFwSwitchRunning_Type()
)
integraXsysServicesFwSwitchRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXsysServicesFwSwitchRunning.setStatus("current")


class _IntegraXsysServicesFwSwitchNext_Type(Integer32):
    """Custom type integraXsysServicesFwSwitchNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fw1", 1),
          ("fw2", 2))
    )


_IntegraXsysServicesFwSwitchNext_Type.__name__ = "Integer32"
_IntegraXsysServicesFwSwitchNext_Object = MibScalar
integraXsysServicesFwSwitchNext = _IntegraXsysServicesFwSwitchNext_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 4, 46, 10),
    _IntegraXsysServicesFwSwitchNext_Type()
)
integraXsysServicesFwSwitchNext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraXsysServicesFwSwitchNext.setStatus("current")
_IntegraXethernet_ObjectIdentity = ObjectIdentity
integraXethernet = _IntegraXethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5)
)
_IntegraXifStatusTable_Object = MibTable
integraXifStatusTable = _IntegraXifStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 1)
)
if mibBuilder.loadTexts:
    integraXifStatusTable.setStatus("current")
_IntegraXifPortEntry_Object = MibTableRow
integraXifPortEntry = _IntegraXifPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 1, 1)
)
integraXifPortEntry.setIndexNames(
    (0, "SAF-INTEGRAX-MIB", "integraXifPortStatIndex"),
)
if mibBuilder.loadTexts:
    integraXifPortEntry.setStatus("current")


class _IntegraXifPortStatIndex_Type(Integer32):
    """Custom type integraXifPortStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IntegraXifPortStatIndex_Type.__name__ = "Integer32"
_IntegraXifPortStatIndex_Object = MibTableColumn
integraXifPortStatIndex = _IntegraXifPortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 1, 1, 1),
    _IntegraXifPortStatIndex_Type()
)
integraXifPortStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifPortStatIndex.setStatus("current")


class _IntegraXifPortStatDescr_Type(DisplayString):
    """Custom type integraXifPortStatDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntegraXifPortStatDescr_Type.__name__ = "DisplayString"
_IntegraXifPortStatDescr_Object = MibTableColumn
integraXifPortStatDescr = _IntegraXifPortStatDescr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 1, 1, 2),
    _IntegraXifPortStatDescr_Type()
)
integraXifPortStatDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifPortStatDescr.setStatus("current")
_IntegraXifPortType_Type = IANAifType
_IntegraXifPortType_Object = MibTableColumn
integraXifPortType = _IntegraXifPortType_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 1, 1, 3),
    _IntegraXifPortType_Type()
)
integraXifPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifPortType.setStatus("current")
_IntegraXifPortMtu_Type = Integer32
_IntegraXifPortMtu_Object = MibTableColumn
integraXifPortMtu = _IntegraXifPortMtu_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 1, 1, 4),
    _IntegraXifPortMtu_Type()
)
integraXifPortMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifPortMtu.setStatus("current")
if mibBuilder.loadTexts:
    integraXifPortMtu.setUnits("B")
_IntegraXifPortHighSpeed_Type = Gauge32
_IntegraXifPortHighSpeed_Object = MibTableColumn
integraXifPortHighSpeed = _IntegraXifPortHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 1, 1, 5),
    _IntegraXifPortHighSpeed_Type()
)
integraXifPortHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifPortHighSpeed.setStatus("current")
if mibBuilder.loadTexts:
    integraXifPortHighSpeed.setUnits("Mbps")
_IntegraXifPortPhysAddress_Type = PhysAddress
_IntegraXifPortPhysAddress_Object = MibTableColumn
integraXifPortPhysAddress = _IntegraXifPortPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 1, 1, 6),
    _IntegraXifPortPhysAddress_Type()
)
integraXifPortPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifPortPhysAddress.setStatus("current")


class _IntegraXifPortAdminStatus_Type(Integer32):
    """Custom type integraXifPortAdminStatus based on Integer32"""
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


_IntegraXifPortAdminStatus_Type.__name__ = "Integer32"
_IntegraXifPortAdminStatus_Object = MibTableColumn
integraXifPortAdminStatus = _IntegraXifPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 1, 1, 7),
    _IntegraXifPortAdminStatus_Type()
)
integraXifPortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifPortAdminStatus.setStatus("current")


class _IntegraXifPortOperStatus_Type(Integer32):
    """Custom type integraXifPortOperStatus based on Integer32"""
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


_IntegraXifPortOperStatus_Type.__name__ = "Integer32"
_IntegraXifPortOperStatus_Object = MibTableColumn
integraXifPortOperStatus = _IntegraXifPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 1, 1, 8),
    _IntegraXifPortOperStatus_Type()
)
integraXifPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifPortOperStatus.setStatus("current")
_IntegraXifPortLastChange_Type = TimeTicks
_IntegraXifPortLastChange_Object = MibTableColumn
integraXifPortLastChange = _IntegraXifPortLastChange_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 1, 1, 9),
    _IntegraXifPortLastChange_Type()
)
integraXifPortLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifPortLastChange.setStatus("current")


class _IntegraXifPortAutoneg_Type(Integer32):
    """Custom type integraXifPortAutoneg based on Integer32"""
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


_IntegraXifPortAutoneg_Type.__name__ = "Integer32"
_IntegraXifPortAutoneg_Object = MibTableColumn
integraXifPortAutoneg = _IntegraXifPortAutoneg_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 1, 1, 10),
    _IntegraXifPortAutoneg_Type()
)
integraXifPortAutoneg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifPortAutoneg.setStatus("current")


class _IntegraXifPortDuplex_Type(Integer32):
    """Custom type integraXifPortDuplex based on Integer32"""
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


_IntegraXifPortDuplex_Type.__name__ = "Integer32"
_IntegraXifPortDuplex_Object = MibTableColumn
integraXifPortDuplex = _IntegraXifPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 1, 1, 11),
    _IntegraXifPortDuplex_Type()
)
integraXifPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifPortDuplex.setStatus("current")


class _IntegraXifPortSyncEthActive_Type(Integer32):
    """Custom type integraXifPortSyncEthActive based on Integer32"""
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


_IntegraXifPortSyncEthActive_Type.__name__ = "Integer32"
_IntegraXifPortSyncEthActive_Object = MibTableColumn
integraXifPortSyncEthActive = _IntegraXifPortSyncEthActive_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 1, 1, 12),
    _IntegraXifPortSyncEthActive_Type()
)
integraXifPortSyncEthActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifPortSyncEthActive.setStatus("current")
_IntegraXifPortSyncEthPrio_Type = Integer32
_IntegraXifPortSyncEthPrio_Object = MibTableColumn
integraXifPortSyncEthPrio = _IntegraXifPortSyncEthPrio_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 1, 1, 13),
    _IntegraXifPortSyncEthPrio_Type()
)
integraXifPortSyncEthPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifPortSyncEthPrio.setStatus("current")


class _IntegraXifPortFlowControl_Type(Integer32):
    """Custom type integraXifPortFlowControl based on Integer32"""
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


_IntegraXifPortFlowControl_Type.__name__ = "Integer32"
_IntegraXifPortFlowControl_Object = MibTableColumn
integraXifPortFlowControl = _IntegraXifPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 1, 1, 14),
    _IntegraXifPortFlowControl_Type()
)
integraXifPortFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifPortFlowControl.setStatus("current")
_IntegraXifStatisticsTable_Object = MibTable
integraXifStatisticsTable = _IntegraXifStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2)
)
if mibBuilder.loadTexts:
    integraXifStatisticsTable.setStatus("current")
_IntegraXifPortStcEntry_Object = MibTableRow
integraXifPortStcEntry = _IntegraXifPortStcEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1)
)
integraXifPortStcEntry.setIndexNames(
    (0, "SAF-INTEGRAX-MIB", "integraXifPortStcIndex"),
)
if mibBuilder.loadTexts:
    integraXifPortStcEntry.setStatus("current")


class _IntegraXifPortStcIndex_Type(Integer32):
    """Custom type integraXifPortStcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IntegraXifPortStcIndex_Type.__name__ = "Integer32"
_IntegraXifPortStcIndex_Object = MibTableColumn
integraXifPortStcIndex = _IntegraXifPortStcIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 1),
    _IntegraXifPortStcIndex_Type()
)
integraXifPortStcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifPortStcIndex.setStatus("current")


class _IntegraXifPortStcDescr_Type(DisplayString):
    """Custom type integraXifPortStcDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntegraXifPortStcDescr_Type.__name__ = "DisplayString"
_IntegraXifPortStcDescr_Object = MibTableColumn
integraXifPortStcDescr = _IntegraXifPortStcDescr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 2),
    _IntegraXifPortStcDescr_Type()
)
integraXifPortStcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifPortStcDescr.setStatus("current")
_IntegraXifTimePassed_Type = TimeTicks
_IntegraXifTimePassed_Object = MibTableColumn
integraXifTimePassed = _IntegraXifTimePassed_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 3),
    _IntegraXifTimePassed_Type()
)
integraXifTimePassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifTimePassed.setStatus("current")
if mibBuilder.loadTexts:
    integraXifTimePassed.setUnits("s/100")
_IntegraXifIngressPackets_Type = Counter64
_IntegraXifIngressPackets_Object = MibTableColumn
integraXifIngressPackets = _IntegraXifIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 4),
    _IntegraXifIngressPackets_Type()
)
integraXifIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifIngressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifIngressPackets.setUnits("packet")
_IntegraXifIngressBytes_Type = Counter64
_IntegraXifIngressBytes_Object = MibTableColumn
integraXifIngressBytes = _IntegraXifIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 5),
    _IntegraXifIngressBytes_Type()
)
integraXifIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifIngressBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraXifIngressBytes.setUnits("B")
_IntegraXifEgressPackets_Type = Counter64
_IntegraXifEgressPackets_Object = MibTableColumn
integraXifEgressPackets = _IntegraXifEgressPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 6),
    _IntegraXifEgressPackets_Type()
)
integraXifEgressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEgressPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEgressPackets.setUnits("packet")
_IntegraXifEgressBytes_Type = Counter64
_IntegraXifEgressBytes_Object = MibTableColumn
integraXifEgressBytes = _IntegraXifEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 7),
    _IntegraXifEgressBytes_Type()
)
integraXifEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEgressBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEgressBytes.setUnits("B")
_IntegraXifEtherStatsMulticastPkts_Type = Counter64
_IntegraXifEtherStatsMulticastPkts_Object = MibTableColumn
integraXifEtherStatsMulticastPkts = _IntegraXifEtherStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 8),
    _IntegraXifEtherStatsMulticastPkts_Type()
)
integraXifEtherStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherStatsMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherStatsMulticastPkts.setUnits("packet")
_IntegraXifEtherStatsBroadcastPkts_Type = Counter64
_IntegraXifEtherStatsBroadcastPkts_Object = MibTableColumn
integraXifEtherStatsBroadcastPkts = _IntegraXifEtherStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 9),
    _IntegraXifEtherStatsBroadcastPkts_Type()
)
integraXifEtherStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherStatsBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherStatsBroadcastPkts.setUnits("packet")
_IntegraXifEtherStatsPkts64Octets_Type = Counter64
_IntegraXifEtherStatsPkts64Octets_Object = MibTableColumn
integraXifEtherStatsPkts64Octets = _IntegraXifEtherStatsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 10),
    _IntegraXifEtherStatsPkts64Octets_Type()
)
integraXifEtherStatsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherStatsPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherStatsPkts64Octets.setUnits("packet")
_IntegraXifEtherStatsPkts65to127Octets_Type = Counter64
_IntegraXifEtherStatsPkts65to127Octets_Object = MibTableColumn
integraXifEtherStatsPkts65to127Octets = _IntegraXifEtherStatsPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 11),
    _IntegraXifEtherStatsPkts65to127Octets_Type()
)
integraXifEtherStatsPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherStatsPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherStatsPkts65to127Octets.setUnits("packet")
_IntegraXifEtherStatsPkts128to255Octets_Type = Counter64
_IntegraXifEtherStatsPkts128to255Octets_Object = MibTableColumn
integraXifEtherStatsPkts128to255Octets = _IntegraXifEtherStatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 12),
    _IntegraXifEtherStatsPkts128to255Octets_Type()
)
integraXifEtherStatsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherStatsPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherStatsPkts128to255Octets.setUnits("packet")
_IntegraXifEtherStatsPkts256to511Octets_Type = Counter64
_IntegraXifEtherStatsPkts256to511Octets_Object = MibTableColumn
integraXifEtherStatsPkts256to511Octets = _IntegraXifEtherStatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 13),
    _IntegraXifEtherStatsPkts256to511Octets_Type()
)
integraXifEtherStatsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherStatsPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherStatsPkts256to511Octets.setUnits("packet")
_IntegraXifEtherStatsPkts512to1023Octets_Type = Counter64
_IntegraXifEtherStatsPkts512to1023Octets_Object = MibTableColumn
integraXifEtherStatsPkts512to1023Octets = _IntegraXifEtherStatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 14),
    _IntegraXifEtherStatsPkts512to1023Octets_Type()
)
integraXifEtherStatsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherStatsPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherStatsPkts512to1023Octets.setUnits("packet")
_IntegraXifEtherStatsPkts1024to1518Octets_Type = Counter64
_IntegraXifEtherStatsPkts1024to1518Octets_Object = MibTableColumn
integraXifEtherStatsPkts1024to1518Octets = _IntegraXifEtherStatsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 15),
    _IntegraXifEtherStatsPkts1024to1518Octets_Type()
)
integraXifEtherStatsPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherStatsPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherStatsPkts1024to1518Octets.setUnits("packet")
_IntegraXifEtherStatsOversizePkts_Type = Counter64
_IntegraXifEtherStatsOversizePkts_Object = MibTableColumn
integraXifEtherStatsOversizePkts = _IntegraXifEtherStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 16),
    _IntegraXifEtherStatsOversizePkts_Type()
)
integraXifEtherStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherStatsOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherStatsOversizePkts.setUnits("packet")
_IntegraXifEtherRxOversizePkts_Type = Counter64
_IntegraXifEtherRxOversizePkts_Object = MibTableColumn
integraXifEtherRxOversizePkts = _IntegraXifEtherRxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 17),
    _IntegraXifEtherRxOversizePkts_Type()
)
integraXifEtherRxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherRxOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherRxOversizePkts.setUnits("packet")
_IntegraXifEtherTxOversizePkts_Type = Counter64
_IntegraXifEtherTxOversizePkts_Object = MibTableColumn
integraXifEtherTxOversizePkts = _IntegraXifEtherTxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 18),
    _IntegraXifEtherTxOversizePkts_Type()
)
integraXifEtherTxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherTxOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherTxOversizePkts.setUnits("packet")
_IntegraXifEtherStatsOctets_Type = Counter64
_IntegraXifEtherStatsOctets_Object = MibTableColumn
integraXifEtherStatsOctets = _IntegraXifEtherStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 19),
    _IntegraXifEtherStatsOctets_Type()
)
integraXifEtherStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherStatsOctets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherStatsOctets.setUnits("packet")
_IntegraXifEtherStatsPkts_Type = Counter64
_IntegraXifEtherStatsPkts_Object = MibTableColumn
integraXifEtherStatsPkts = _IntegraXifEtherStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 20),
    _IntegraXifEtherStatsPkts_Type()
)
integraXifEtherStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherStatsPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherStatsPkts.setUnits("packet")
_IntegraXifEtherStatsTXNoErrors_Type = Counter64
_IntegraXifEtherStatsTXNoErrors_Object = MibTableColumn
integraXifEtherStatsTXNoErrors = _IntegraXifEtherStatsTXNoErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 21),
    _IntegraXifEtherStatsTXNoErrors_Type()
)
integraXifEtherStatsTXNoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherStatsTXNoErrors.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherStatsTXNoErrors.setUnits("packet")
_IntegraXifEtherStatsRXNoErrors_Type = Counter64
_IntegraXifEtherStatsRXNoErrors_Object = MibTableColumn
integraXifEtherStatsRXNoErrors = _IntegraXifEtherStatsRXNoErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 22),
    _IntegraXifEtherStatsRXNoErrors_Type()
)
integraXifEtherStatsRXNoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherStatsRXNoErrors.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherStatsRXNoErrors.setUnits("packet")
_IntegraXifEtherStatsPkts1519to1522Octets_Type = Counter64
_IntegraXifEtherStatsPkts1519to1522Octets_Object = MibTableColumn
integraXifEtherStatsPkts1519to1522Octets = _IntegraXifEtherStatsPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 23),
    _IntegraXifEtherStatsPkts1519to1522Octets_Type()
)
integraXifEtherStatsPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherStatsPkts1519to1522Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherStatsPkts1519to1522Octets.setUnits("packet")
_IntegraXifIfInOctets_Type = Counter64
_IntegraXifIfInOctets_Object = MibTableColumn
integraXifIfInOctets = _IntegraXifIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 24),
    _IntegraXifIfInOctets_Type()
)
integraXifIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifIfInOctets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifIfInOctets.setUnits("octet")
_IntegraXifIfOutOctets_Type = Counter64
_IntegraXifIfOutOctets_Object = MibTableColumn
integraXifIfOutOctets = _IntegraXifIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 25),
    _IntegraXifIfOutOctets_Type()
)
integraXifIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifIfOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifIfOutOctets.setUnits("octet")
_IntegraXifDot1dTpPortInFrames_Type = Counter64
_IntegraXifDot1dTpPortInFrames_Object = MibTableColumn
integraXifDot1dTpPortInFrames = _IntegraXifDot1dTpPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 26),
    _IntegraXifDot1dTpPortInFrames_Type()
)
integraXifDot1dTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifDot1dTpPortInFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraXifDot1dTpPortInFrames.setUnits("frame")
_IntegraXifDot1dTpPortOutFrames_Type = Counter64
_IntegraXifDot1dTpPortOutFrames_Object = MibTableColumn
integraXifDot1dTpPortOutFrames = _IntegraXifDot1dTpPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 27),
    _IntegraXifDot1dTpPortOutFrames_Type()
)
integraXifDot1dTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifDot1dTpPortOutFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraXifDot1dTpPortOutFrames.setUnits("frame")
_IntegraXifReceivedPkts64Octets_Type = Counter64
_IntegraXifReceivedPkts64Octets_Object = MibTableColumn
integraXifReceivedPkts64Octets = _IntegraXifReceivedPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 28),
    _IntegraXifReceivedPkts64Octets_Type()
)
integraXifReceivedPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifReceivedPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifReceivedPkts64Octets.setUnits("packet")
_IntegraXifTransmittedPkts64Octets_Type = Counter64
_IntegraXifTransmittedPkts64Octets_Object = MibTableColumn
integraXifTransmittedPkts64Octets = _IntegraXifTransmittedPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 29),
    _IntegraXifTransmittedPkts64Octets_Type()
)
integraXifTransmittedPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifTransmittedPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifTransmittedPkts64Octets.setUnits("packet")
_IntegraXifReceivedPkts65to127Octets_Type = Counter64
_IntegraXifReceivedPkts65to127Octets_Object = MibTableColumn
integraXifReceivedPkts65to127Octets = _IntegraXifReceivedPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 30),
    _IntegraXifReceivedPkts65to127Octets_Type()
)
integraXifReceivedPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifReceivedPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifReceivedPkts65to127Octets.setUnits("packet")
_IntegraXifTransmittedPkts65to127Octets_Type = Counter64
_IntegraXifTransmittedPkts65to127Octets_Object = MibTableColumn
integraXifTransmittedPkts65to127Octets = _IntegraXifTransmittedPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 31),
    _IntegraXifTransmittedPkts65to127Octets_Type()
)
integraXifTransmittedPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifTransmittedPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifTransmittedPkts65to127Octets.setUnits("packet")
_IntegraXifReceivedPkts128to255Octets_Type = Counter64
_IntegraXifReceivedPkts128to255Octets_Object = MibTableColumn
integraXifReceivedPkts128to255Octets = _IntegraXifReceivedPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 32),
    _IntegraXifReceivedPkts128to255Octets_Type()
)
integraXifReceivedPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifReceivedPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifReceivedPkts128to255Octets.setUnits("packet")
_IntegraXifTransmittedPkts128to255Octets_Type = Counter64
_IntegraXifTransmittedPkts128to255Octets_Object = MibTableColumn
integraXifTransmittedPkts128to255Octets = _IntegraXifTransmittedPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 33),
    _IntegraXifTransmittedPkts128to255Octets_Type()
)
integraXifTransmittedPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifTransmittedPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifTransmittedPkts128to255Octets.setUnits("packet")
_IntegraXifReceivedPkts256to511Octets_Type = Counter64
_IntegraXifReceivedPkts256to511Octets_Object = MibTableColumn
integraXifReceivedPkts256to511Octets = _IntegraXifReceivedPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 34),
    _IntegraXifReceivedPkts256to511Octets_Type()
)
integraXifReceivedPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifReceivedPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifReceivedPkts256to511Octets.setUnits("packet")
_IntegraXifTransmittedPkts256to511Octets_Type = Counter64
_IntegraXifTransmittedPkts256to511Octets_Object = MibTableColumn
integraXifTransmittedPkts256to511Octets = _IntegraXifTransmittedPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 35),
    _IntegraXifTransmittedPkts256to511Octets_Type()
)
integraXifTransmittedPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifTransmittedPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifTransmittedPkts256to511Octets.setUnits("packet")
_IntegraXifReceivedPkts512to1023Octets_Type = Counter64
_IntegraXifReceivedPkts512to1023Octets_Object = MibTableColumn
integraXifReceivedPkts512to1023Octets = _IntegraXifReceivedPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 36),
    _IntegraXifReceivedPkts512to1023Octets_Type()
)
integraXifReceivedPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifReceivedPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifReceivedPkts512to1023Octets.setUnits("packet")
_IntegraXifTransmittedPkts512to1023Octets_Type = Counter64
_IntegraXifTransmittedPkts512to1023Octets_Object = MibTableColumn
integraXifTransmittedPkts512to1023Octets = _IntegraXifTransmittedPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 37),
    _IntegraXifTransmittedPkts512to1023Octets_Type()
)
integraXifTransmittedPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifTransmittedPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifTransmittedPkts512to1023Octets.setUnits("packet")
_IntegraXifReceivedPkts1024to1518Octets_Type = Counter64
_IntegraXifReceivedPkts1024to1518Octets_Object = MibTableColumn
integraXifReceivedPkts1024to1518Octets = _IntegraXifReceivedPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 38),
    _IntegraXifReceivedPkts1024to1518Octets_Type()
)
integraXifReceivedPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifReceivedPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifReceivedPkts1024to1518Octets.setUnits("packet")
_IntegraXifTransmittedPkts1024to1518Octets_Type = Counter64
_IntegraXifTransmittedPkts1024to1518Octets_Object = MibTableColumn
integraXifTransmittedPkts1024to1518Octets = _IntegraXifTransmittedPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 39),
    _IntegraXifTransmittedPkts1024to1518Octets_Type()
)
integraXifTransmittedPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifTransmittedPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifTransmittedPkts1024to1518Octets.setUnits("packet")
_IntegraXifIfInBroadcastPkts_Type = Counter64
_IntegraXifIfInBroadcastPkts_Object = MibTableColumn
integraXifIfInBroadcastPkts = _IntegraXifIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 40),
    _IntegraXifIfInBroadcastPkts_Type()
)
integraXifIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifIfInBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraXifIfInBroadcastPkts.setUnits("packet")
_IntegraXifIfOutBroadcastPkts_Type = Counter64
_IntegraXifIfOutBroadcastPkts_Object = MibTableColumn
integraXifIfOutBroadcastPkts = _IntegraXifIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 41),
    _IntegraXifIfOutBroadcastPkts_Type()
)
integraXifIfOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifIfOutBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraXifIfOutBroadcastPkts.setUnits("packet")
_IntegraXifIfInMulticastPkts_Type = Counter64
_IntegraXifIfInMulticastPkts_Object = MibTableColumn
integraXifIfInMulticastPkts = _IntegraXifIfInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 42),
    _IntegraXifIfInMulticastPkts_Type()
)
integraXifIfInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifIfInMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraXifIfInMulticastPkts.setUnits("packet")
_IntegraXifIfOutMulticastPkts_Type = Counter64
_IntegraXifIfOutMulticastPkts_Object = MibTableColumn
integraXifIfOutMulticastPkts = _IntegraXifIfOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 43),
    _IntegraXifIfOutMulticastPkts_Type()
)
integraXifIfOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifIfOutMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    integraXifIfOutMulticastPkts.setUnits("packet")
_IntegraXifDot3InPauseFrames_Type = Counter64
_IntegraXifDot3InPauseFrames_Object = MibTableColumn
integraXifDot3InPauseFrames = _IntegraXifDot3InPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 44),
    _IntegraXifDot3InPauseFrames_Type()
)
integraXifDot3InPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifDot3InPauseFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraXifDot3InPauseFrames.setUnits("frame")
_IntegraXifDot3OutPauseFrames_Type = Counter64
_IntegraXifDot3OutPauseFrames_Object = MibTableColumn
integraXifDot3OutPauseFrames = _IntegraXifDot3OutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 45),
    _IntegraXifDot3OutPauseFrames_Type()
)
integraXifDot3OutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifDot3OutPauseFrames.setStatus("current")
if mibBuilder.loadTexts:
    integraXifDot3OutPauseFrames.setUnits("frame")
_IntegraXifEtherStatsUndersizePkts_Type = Counter64
_IntegraXifEtherStatsUndersizePkts_Object = MibTableColumn
integraXifEtherStatsUndersizePkts = _IntegraXifEtherStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 46),
    _IntegraXifEtherStatsUndersizePkts_Type()
)
integraXifEtherStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherStatsUndersizePkts.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherStatsUndersizePkts.setUnits("packet")
_IntegraXifEtherStatsFragments_Type = Counter64
_IntegraXifEtherStatsFragments_Object = MibTableColumn
integraXifEtherStatsFragments = _IntegraXifEtherStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 47),
    _IntegraXifEtherStatsFragments_Type()
)
integraXifEtherStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherStatsFragments.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherStatsFragments.setUnits("packet")
_IntegraXifEtherStatsCRCAlignErrors_Type = Counter64
_IntegraXifEtherStatsCRCAlignErrors_Object = MibTableColumn
integraXifEtherStatsCRCAlignErrors = _IntegraXifEtherStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 48),
    _IntegraXifEtherStatsCRCAlignErrors_Type()
)
integraXifEtherStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherStatsCRCAlignErrors.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherStatsCRCAlignErrors.setUnits("packet")
_IntegraXifEtherStatsJabbers_Type = Counter64
_IntegraXifEtherStatsJabbers_Object = MibTableColumn
integraXifEtherStatsJabbers = _IntegraXifEtherStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 49),
    _IntegraXifEtherStatsJabbers_Type()
)
integraXifEtherStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEtherStatsJabbers.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEtherStatsJabbers.setUnits("packet")
_IntegraXifIngressBPS_Type = Integer32
_IntegraXifIngressBPS_Object = MibTableColumn
integraXifIngressBPS = _IntegraXifIngressBPS_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 50),
    _IntegraXifIngressBPS_Type()
)
integraXifIngressBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifIngressBPS.setStatus("current")
if mibBuilder.loadTexts:
    integraXifIngressBPS.setUnits("Bps")
_IntegraXifIngressPPS_Type = Integer32
_IntegraXifIngressPPS_Object = MibTableColumn
integraXifIngressPPS = _IntegraXifIngressPPS_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 51),
    _IntegraXifIngressPPS_Type()
)
integraXifIngressPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifIngressPPS.setStatus("current")
if mibBuilder.loadTexts:
    integraXifIngressPPS.setUnits("pps")
_IntegraXifEgressBPS_Type = Integer32
_IntegraXifEgressBPS_Object = MibTableColumn
integraXifEgressBPS = _IntegraXifEgressBPS_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 52),
    _IntegraXifEgressBPS_Type()
)
integraXifEgressBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEgressBPS.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEgressBPS.setUnits("Bps")
_IntegraXifEgressPPS_Type = Integer32
_IntegraXifEgressPPS_Object = MibTableColumn
integraXifEgressPPS = _IntegraXifEgressPPS_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 53),
    _IntegraXifEgressPPS_Type()
)
integraXifEgressPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifEgressPPS.setStatus("current")
if mibBuilder.loadTexts:
    integraXifEgressPPS.setUnits("pps")
_IntegraXifAllCoSQoutPackets_Type = Counter64
_IntegraXifAllCoSQoutPackets_Object = MibTableColumn
integraXifAllCoSQoutPackets = _IntegraXifAllCoSQoutPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 54),
    _IntegraXifAllCoSQoutPackets_Type()
)
integraXifAllCoSQoutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifAllCoSQoutPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifAllCoSQoutPackets.setUnits("packet")
_IntegraXifAllCoSQoutBytes_Type = Counter64
_IntegraXifAllCoSQoutBytes_Object = MibTableColumn
integraXifAllCoSQoutBytes = _IntegraXifAllCoSQoutBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 55),
    _IntegraXifAllCoSQoutBytes_Type()
)
integraXifAllCoSQoutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifAllCoSQoutBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraXifAllCoSQoutBytes.setUnits("B")
_IntegraXifAllCoSQdroppedPackets_Type = Counter64
_IntegraXifAllCoSQdroppedPackets_Object = MibTableColumn
integraXifAllCoSQdroppedPackets = _IntegraXifAllCoSQdroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 56),
    _IntegraXifAllCoSQdroppedPackets_Type()
)
integraXifAllCoSQdroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifAllCoSQdroppedPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifAllCoSQdroppedPackets.setUnits("packet")
_IntegraXifAllCoSQdroppedBytes_Type = Counter64
_IntegraXifAllCoSQdroppedBytes_Object = MibTableColumn
integraXifAllCoSQdroppedBytes = _IntegraXifAllCoSQdroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 57),
    _IntegraXifAllCoSQdroppedBytes_Type()
)
integraXifAllCoSQdroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifAllCoSQdroppedBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraXifAllCoSQdroppedBytes.setUnits("B")
_IntegraXifProcessedRxPackets_Type = Counter64
_IntegraXifProcessedRxPackets_Object = MibTableColumn
integraXifProcessedRxPackets = _IntegraXifProcessedRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 58),
    _IntegraXifProcessedRxPackets_Type()
)
integraXifProcessedRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifProcessedRxPackets.setStatus("current")
if mibBuilder.loadTexts:
    integraXifProcessedRxPackets.setUnits("packet")
_IntegraXifProcessedRxBytes_Type = Counter64
_IntegraXifProcessedRxBytes_Object = MibTableColumn
integraXifProcessedRxBytes = _IntegraXifProcessedRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 2, 1, 59),
    _IntegraXifProcessedRxBytes_Type()
)
integraXifProcessedRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifProcessedRxBytes.setStatus("current")
if mibBuilder.loadTexts:
    integraXifProcessedRxBytes.setUnits("B")


class _IntegraXifLspPortAdminState_Type(Integer32):
    """Custom type integraXifLspPortAdminState based on Integer32"""
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


_IntegraXifLspPortAdminState_Type.__name__ = "Integer32"
_IntegraXifLspPortAdminState_Object = MibScalar
integraXifLspPortAdminState = _IntegraXifLspPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 3),
    _IntegraXifLspPortAdminState_Type()
)
integraXifLspPortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifLspPortAdminState.setStatus("current")


class _IntegraXifLspPortList_Type(Bits):
    """Custom type integraXifLspPortList based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("lan1", 1),
          ("lan2", 2),
          ("lan3", 3))
    )

_IntegraXifLspPortList_Type.__name__ = "Bits"
_IntegraXifLspPortList_Object = MibScalar
integraXifLspPortList = _IntegraXifLspPortList_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 4),
    _IntegraXifLspPortList_Type()
)
integraXifLspPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifLspPortList.setStatus("current")


class _IntegraXifLspPortStatus_Type(Integer32):
    """Custom type integraXifLspPortStatus based on Integer32"""
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


_IntegraXifLspPortStatus_Type.__name__ = "Integer32"
_IntegraXifLspPortStatus_Object = MibScalar
integraXifLspPortStatus = _IntegraXifLspPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 5, 5),
    _IntegraXifLspPortStatus_Type()
)
integraXifLspPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXifLspPortStatus.setStatus("current")


class _IntegraXexecuteConfig_Type(Integer32):
    """Custom type integraXexecuteConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_IntegraXexecuteConfig_Type.__name__ = "Integer32"
_IntegraXexecuteConfig_Object = MibScalar
integraXexecuteConfig = _IntegraXexecuteConfig_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 6),
    _IntegraXexecuteConfig_Type()
)
integraXexecuteConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraXexecuteConfig.setStatus("current")


class _IntegraXneedStore_Type(Integer32):
    """Custom type integraXneedStore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("no", 0)
    )


_IntegraXneedStore_Type.__name__ = "Integer32"
_IntegraXneedStore_Object = MibScalar
integraXneedStore = _IntegraXneedStore_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 7),
    _IntegraXneedStore_Type()
)
integraXneedStore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXneedStore.setStatus("current")


class _IntegraXstoreConfig_Type(Integer32):
    """Custom type integraXstoreConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("store", 1)
    )


_IntegraXstoreConfig_Type.__name__ = "Integer32"
_IntegraXstoreConfig_Object = MibScalar
integraXstoreConfig = _IntegraXstoreConfig_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 8),
    _IntegraXstoreConfig_Type()
)
integraXstoreConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraXstoreConfig.setStatus("current")
_IntegraXnetCfg_ObjectIdentity = ObjectIdentity
integraXnetCfg = _IntegraXnetCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 9)
)
_IntegraXnetCfgIPaddress_Type = DisplayString
_IntegraXnetCfgIPaddress_Object = MibScalar
integraXnetCfgIPaddress = _IntegraXnetCfgIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 9, 1),
    _IntegraXnetCfgIPaddress_Type()
)
integraXnetCfgIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraXnetCfgIPaddress.setStatus("current")
_IntegraXnetCfgIPmask_Type = DisplayString
_IntegraXnetCfgIPmask_Object = MibScalar
integraXnetCfgIPmask = _IntegraXnetCfgIPmask_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 9, 2),
    _IntegraXnetCfgIPmask_Type()
)
integraXnetCfgIPmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraXnetCfgIPmask.setStatus("current")
_IntegraXnetCfgIPgateway_Type = DisplayString
_IntegraXnetCfgIPgateway_Object = MibScalar
integraXnetCfgIPgateway = _IntegraXnetCfgIPgateway_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 9, 3),
    _IntegraXnetCfgIPgateway_Type()
)
integraXnetCfgIPgateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integraXnetCfgIPgateway.setStatus("current")
_IntegraXnetCfgRemoteIPaddress_Type = DisplayString
_IntegraXnetCfgRemoteIPaddress_Object = MibScalar
integraXnetCfgRemoteIPaddress = _IntegraXnetCfgRemoteIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 9, 4),
    _IntegraXnetCfgRemoteIPaddress_Type()
)
integraXnetCfgRemoteIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integraXnetCfgRemoteIPaddress.setStatus("current")
_IntegraXConformance_ObjectIdentity = ObjectIdentity
integraXConformance = _IntegraXConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 10)
)
_IntegraXCompliances_ObjectIdentity = ObjectIdentity
integraXCompliances = _IntegraXCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 10, 1)
)
_IntegraXGroups_ObjectIdentity = ObjectIdentity
integraXGroups = _IntegraXGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 10, 2)
)

# Managed Objects groups

integraXMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 10, 2, 1)
)
integraXMiscGroup.setObjects(
    ("SAF-INTEGRAX-MIB", "integraXtimestamp")
)
if mibBuilder.loadTexts:
    integraXMiscGroup.setStatus("current")

integraXRadioGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 10, 2, 2)
)
integraXRadioGroup.setObjects(
      *(("SAF-INTEGRAX-MIB", "integraXradioAtxPower"),
        ("SAF-INTEGRAX-MIB", "integraXradioAtxFrequency"),
        ("SAF-INTEGRAX-MIB", "integraXradioArxLevel"),
        ("SAF-INTEGRAX-MIB", "integraXradioArxLevelState"),
        ("SAF-INTEGRAX-MIB", "integraXradioAside"),
        ("SAF-INTEGRAX-MIB", "integraXradioAtxMute"),
        ("SAF-INTEGRAX-MIB", "integraXradioAtxMuteDuration"),
        ("SAF-INTEGRAX-MIB", "integraXradioAduplexShift"),
        ("SAF-INTEGRAX-MIB", "integraXradioArxFrequency"),
        ("SAF-INTEGRAX-MIB", "integraXradioAtemperature"),
        ("SAF-INTEGRAX-MIB", "integraXradioApll"),
        ("SAF-INTEGRAX-MIB", "integraXradioArangeEntryIndex"),
        ("SAF-INTEGRAX-MIB", "integraXradioArangeDescr"),
        ("SAF-INTEGRAX-MIB", "integraXradioArangeTxPower"),
        ("SAF-INTEGRAX-MIB", "integraXradioArangeTxFrequency"),
        ("SAF-INTEGRAX-MIB", "integraXradioBtxPower"),
        ("SAF-INTEGRAX-MIB", "integraXradioBtxFrequency"),
        ("SAF-INTEGRAX-MIB", "integraXradioBrxLevel"),
        ("SAF-INTEGRAX-MIB", "integraXradioBrxLevelState"),
        ("SAF-INTEGRAX-MIB", "integraXradioBside"),
        ("SAF-INTEGRAX-MIB", "integraXradioBtxMute"),
        ("SAF-INTEGRAX-MIB", "integraXradioBtxMuteDuration"),
        ("SAF-INTEGRAX-MIB", "integraXradioBduplexShift"),
        ("SAF-INTEGRAX-MIB", "integraXradioBrxFrequency"),
        ("SAF-INTEGRAX-MIB", "integraXradioBtemperature"),
        ("SAF-INTEGRAX-MIB", "integraXradioBpll"),
        ("SAF-INTEGRAX-MIB", "integraXradioBrangeEntryIndex"),
        ("SAF-INTEGRAX-MIB", "integraXradioBrangeDescr"),
        ("SAF-INTEGRAX-MIB", "integraXradioBrangeTxPower"),
        ("SAF-INTEGRAX-MIB", "integraXradioBrangeTxFrequency"))
)
if mibBuilder.loadTexts:
    integraXRadioGroup.setStatus("current")

integraXModemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 10, 2, 3)
)
integraXModemGroup.setObjects(
      *(("SAF-INTEGRAX-MIB", "integraXmodemAacquireStatus"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAnormalizedMse"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAfecLoad"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAxpdEst"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAacquireLastStatusDetails"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAtemperature"),
        ("SAF-INTEGRAX-MIB", "integraXmodemArxModulation"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAtxModulation"),
        ("SAF-INTEGRAX-MIB", "integraXmodemArxCapacity"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAtxCapacity"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAacmEngine"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAcarrierOffset"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAcountTime"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAerroredBlock"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAerroredSecond"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAseverelyErroredSecond"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAbackgroundBlockError"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAtotalBlockNumber"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAerroredSecondRatio"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAseverelyErroredSecondRatio"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAbackgroundBlockErrorRatio"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAuptime"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAunavailtime"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAfecLdpcBlockCounter"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAfecLdpcUncorrectedBlockCounter"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAfecLdpcUncorrectedPercent"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAfecRsBlockCounter"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAfecRsUncorrectedBlockCounter"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBacquireStatus"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBnormalizedMse"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBfecLoad"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBxpdEst"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBacquireLastStatusDetails"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBtemperature"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBrxModulation"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBtxModulation"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBrxCapacity"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBtxCapacity"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBacmEngine"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBcarrierOffset"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBcountTime"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBerroredBlock"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBerroredSecond"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBseverelyErroredSecond"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBbackgroundBlockError"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBtotalBlockNumber"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBerroredSecondRatio"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBseverelyErroredSecondRatio"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBbackgroundBlockErrorRatio"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBuptime"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBunavailtime"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBfecLdpcBlockCounter"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBfecLdpcUncorrectedBlockCounter"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBfecLdpcUncorrectedPercent"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBfecRsBlockCounter"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBfecRsUncorrectedBlockCounter"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBandwidth"),
        ("SAF-INTEGRAX-MIB", "integraXmodemModulation"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAmodulationACMmin"),
        ("SAF-INTEGRAX-MIB", "integraXmodemAmodulationACMmax"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBmodulationACMmin"),
        ("SAF-INTEGRAX-MIB", "integraXmodemBmodulationACMmax"))
)
if mibBuilder.loadTexts:
    integraXModemGroup.setStatus("current")

integraXSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 10, 2, 4)
)
integraXSystemGroup.setObjects(
      *(("SAF-INTEGRAX-MIB", "integraXsysCPUtemperature"),
        ("SAF-INTEGRAX-MIB", "integraXsysLicenseExpire"),
        ("SAF-INTEGRAX-MIB", "integraXsysLicenseGenStatus"),
        ("SAF-INTEGRAX-MIB", "integraXsysPSUvoltage"),
        ("SAF-INTEGRAX-MIB", "integraXsysPSUcurrent"),
        ("SAF-INTEGRAX-MIB", "integraXsysPSUpower"),
        ("SAF-INTEGRAX-MIB", "integraXsysBoardTemperature"),
        ("SAF-INTEGRAX-MIB", "integraXsysFreeMemory"),
        ("SAF-INTEGRAX-MIB", "integraXsysCPUidle"),
        ("SAF-INTEGRAX-MIB", "integraXsysDeviceType"),
        ("SAF-INTEGRAX-MIB", "integraXsysDeviceSerial"),
        ("SAF-INTEGRAX-MIB", "integraXsysDeviceProductModel"),
        ("SAF-INTEGRAX-MIB", "integraXsysFanError"),
        ("SAF-INTEGRAX-MIB", "integraXexecuteConfig"),
        ("SAF-INTEGRAX-MIB", "integraXneedStore"),
        ("SAF-INTEGRAX-MIB", "integraXstoreConfig"),
        ("SAF-INTEGRAX-MIB", "integraXsysSw1v0core"),
        ("SAF-INTEGRAX-MIB", "integraXsysSw1v0avdd"),
        ("SAF-INTEGRAX-MIB", "integraXsysSw1v2a"),
        ("SAF-INTEGRAX-MIB", "integraXsysSw1v5ddr"),
        ("SAF-INTEGRAX-MIB", "integraXsysSw1v8"),
        ("SAF-INTEGRAX-MIB", "integraXsysSw2v5"),
        ("SAF-INTEGRAX-MIB", "integraXsysSw3v3"),
        ("SAF-INTEGRAX-MIB", "integraXsysVttrefPs"),
        ("SAF-INTEGRAX-MIB", "integraXsysVttddrPs"),
        ("SAF-INTEGRAX-MIB", "integraXsysZq1v0"),
        ("SAF-INTEGRAX-MIB", "integraXsysZq1v5"),
        ("SAF-INTEGRAX-MIB", "integraXsysZq1v8"),
        ("SAF-INTEGRAX-MIB", "integraXsysZq2v5"),
        ("SAF-INTEGRAX-MIB", "integraXsysZq3v3"),
        ("SAF-INTEGRAX-MIB", "integraXsys5v0d"),
        ("SAF-INTEGRAX-MIB", "integraXsysSw1v2"),
        ("SAF-INTEGRAX-MIB", "integraXsysMdmVddcAvs"),
        ("SAF-INTEGRAX-MIB", "integraXsysMdm3v3"),
        ("SAF-INTEGRAX-MIB", "integraXsysMdm1v0aPm"),
        ("SAF-INTEGRAX-MIB", "integraXsysMdm1v0a"),
        ("SAF-INTEGRAX-MIB", "integraXsysMdm1v8a"),
        ("SAF-INTEGRAX-MIB", "integraXsysMdmDAC02v5a"),
        ("SAF-INTEGRAX-MIB", "integraXsysMdmDAC12v5"),
        ("SAF-INTEGRAX-MIB", "integraXsysMdmDAC22v5"),
        ("SAF-INTEGRAX-MIB", "integraXsysMdm1v8io"),
        ("SAF-INTEGRAX-MIB", "integraXsysMdm3v3io"),
        ("SAF-INTEGRAX-MIB", "integraXsys3v3Radio"),
        ("SAF-INTEGRAX-MIB", "integraXsysMdm4v0"),
        ("SAF-INTEGRAX-MIB", "integraXsys5v0nRadio"),
        ("SAF-INTEGRAX-MIB", "integraXsysCoreVddSns"),
        ("SAF-INTEGRAX-MIB", "integraXsys40v0RadioSns"),
        ("SAF-INTEGRAX-MIB", "integraXsysServicesReboot"),
        ("SAF-INTEGRAX-MIB", "integraXsysServicesFtpSwitch"),
        ("SAF-INTEGRAX-MIB", "integraXsysServicesFwCurrInfo"),
        ("SAF-INTEGRAX-MIB", "integraXsysServicesFwAvailView"),
        ("SAF-INTEGRAX-MIB", "integraXsysServicesFwRemove"),
        ("SAF-INTEGRAX-MIB", "integraXsysServicesFwRemoveAll"),
        ("SAF-INTEGRAX-MIB", "integraXsysServicesFwUpload"),
        ("SAF-INTEGRAX-MIB", "integraXsysServicesFwInst"),
        ("SAF-INTEGRAX-MIB", "integraXsysServicesFwSwitchRunning"),
        ("SAF-INTEGRAX-MIB", "integraXsysServicesFwSwitchNext"))
)
if mibBuilder.loadTexts:
    integraXSystemGroup.setStatus("current")

integraXEthernetGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 10, 2, 5)
)
integraXEthernetGeneralGroup.setObjects(
      *(("SAF-INTEGRAX-MIB", "integraXifPortStatIndex"),
        ("SAF-INTEGRAX-MIB", "integraXifPortStatDescr"),
        ("SAF-INTEGRAX-MIB", "integraXifPortType"),
        ("SAF-INTEGRAX-MIB", "integraXifPortMtu"),
        ("SAF-INTEGRAX-MIB", "integraXifPortHighSpeed"),
        ("SAF-INTEGRAX-MIB", "integraXifPortPhysAddress"),
        ("SAF-INTEGRAX-MIB", "integraXifPortAdminStatus"),
        ("SAF-INTEGRAX-MIB", "integraXifPortOperStatus"),
        ("SAF-INTEGRAX-MIB", "integraXifPortLastChange"),
        ("SAF-INTEGRAX-MIB", "integraXifPortAutoneg"),
        ("SAF-INTEGRAX-MIB", "integraXifPortDuplex"),
        ("SAF-INTEGRAX-MIB", "integraXifPortSyncEthActive"),
        ("SAF-INTEGRAX-MIB", "integraXifPortSyncEthPrio"),
        ("SAF-INTEGRAX-MIB", "integraXifPortFlowControl"),
        ("SAF-INTEGRAX-MIB", "integraXifPortStcIndex"),
        ("SAF-INTEGRAX-MIB", "integraXifPortStcDescr"),
        ("SAF-INTEGRAX-MIB", "integraXifTimePassed"),
        ("SAF-INTEGRAX-MIB", "integraXifIngressPackets"),
        ("SAF-INTEGRAX-MIB", "integraXifIngressBytes"),
        ("SAF-INTEGRAX-MIB", "integraXifEgressPackets"),
        ("SAF-INTEGRAX-MIB", "integraXifEgressBytes"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherRxOversizePkts"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherTxOversizePkts"),
        ("SAF-INTEGRAX-MIB", "integraXifReceivedPkts64Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifTransmittedPkts64Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifReceivedPkts65to127Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifTransmittedPkts65to127Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifReceivedPkts128to255Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifTransmittedPkts128to255Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifReceivedPkts256to511Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifTransmittedPkts256to511Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifReceivedPkts512to1023Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifTransmittedPkts512to1023Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifReceivedPkts1024to1518Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifTransmittedPkts1024to1518Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifIfInBroadcastPkts"),
        ("SAF-INTEGRAX-MIB", "integraXifIfOutBroadcastPkts"),
        ("SAF-INTEGRAX-MIB", "integraXifIfInMulticastPkts"),
        ("SAF-INTEGRAX-MIB", "integraXifIfOutMulticastPkts"),
        ("SAF-INTEGRAX-MIB", "integraXifIngressBPS"),
        ("SAF-INTEGRAX-MIB", "integraXifIngressPPS"),
        ("SAF-INTEGRAX-MIB", "integraXifEgressBPS"),
        ("SAF-INTEGRAX-MIB", "integraXifEgressPPS"),
        ("SAF-INTEGRAX-MIB", "integraXifAllCoSQoutPackets"),
        ("SAF-INTEGRAX-MIB", "integraXifAllCoSQoutBytes"),
        ("SAF-INTEGRAX-MIB", "integraXifAllCoSQdroppedPackets"),
        ("SAF-INTEGRAX-MIB", "integraXifAllCoSQdroppedBytes"),
        ("SAF-INTEGRAX-MIB", "integraXifProcessedRxPackets"),
        ("SAF-INTEGRAX-MIB", "integraXifProcessedRxBytes"),
        ("SAF-INTEGRAX-MIB", "integraXnetCfgIPaddress"),
        ("SAF-INTEGRAX-MIB", "integraXnetCfgIPmask"),
        ("SAF-INTEGRAX-MIB", "integraXnetCfgIPgateway"),
        ("SAF-INTEGRAX-MIB", "integraXnetCfgRemoteIPaddress"),
        ("SAF-INTEGRAX-MIB", "integraXifLspPortAdminState"),
        ("SAF-INTEGRAX-MIB", "integraXifLspPortList"),
        ("SAF-INTEGRAX-MIB", "integraXifLspPortStatus"))
)
if mibBuilder.loadTexts:
    integraXEthernetGeneralGroup.setStatus("current")

integraXEthernetMiiPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 10, 2, 6)
)
integraXEthernetMiiPortGroup.setObjects(
      *(("SAF-INTEGRAX-MIB", "integraXifEtherStatsMulticastPkts"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherStatsBroadcastPkts"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherStatsPkts64Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherStatsPkts65to127Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherStatsPkts128to255Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherStatsPkts256to511Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherStatsPkts512to1023Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherStatsPkts1024to1518Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherStatsOversizePkts"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherStatsOctets"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherStatsPkts"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherStatsTXNoErrors"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherStatsRXNoErrors"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherStatsPkts1519to1522Octets"),
        ("SAF-INTEGRAX-MIB", "integraXifIfInOctets"),
        ("SAF-INTEGRAX-MIB", "integraXifIfOutOctets"),
        ("SAF-INTEGRAX-MIB", "integraXifDot1dTpPortInFrames"),
        ("SAF-INTEGRAX-MIB", "integraXifDot1dTpPortOutFrames"),
        ("SAF-INTEGRAX-MIB", "integraXifDot3InPauseFrames"),
        ("SAF-INTEGRAX-MIB", "integraXifDot3OutPauseFrames"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherStatsUndersizePkts"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherStatsFragments"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherStatsCRCAlignErrors"),
        ("SAF-INTEGRAX-MIB", "integraXifEtherStatsJabbers"))
)
if mibBuilder.loadTexts:
    integraXEthernetMiiPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

integraXCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7, 10, 10, 1, 1)
)
integraXCompliance.setObjects(
      *(("SAF-INTEGRAX-MIB", "integraXMiscGroup"),
        ("SAF-INTEGRAX-MIB", "integraXRadioGroup"),
        ("SAF-INTEGRAX-MIB", "integraXModemGroup"),
        ("SAF-INTEGRAX-MIB", "integraXSystemGroup"),
        ("SAF-INTEGRAX-MIB", "integraXEthernetGeneralGroup"),
        ("SAF-INTEGRAX-MIB", "integraXEthernetMiiPortGroup"))
)
if mibBuilder.loadTexts:
    integraXCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAF-INTEGRAX-MIB",
    **{"FixedDiv20": FixedDiv20,
       "FixedDiv10": FixedDiv10,
       "integraX": integraX,
       "integraXtimestamp": integraXtimestamp,
       "integraXradio": integraXradio,
       "integraXradioA": integraXradioA,
       "integraXradioAtxPower": integraXradioAtxPower,
       "integraXradioAtxFrequency": integraXradioAtxFrequency,
       "integraXradioArxLevel": integraXradioArxLevel,
       "integraXradioArxLevelState": integraXradioArxLevelState,
       "integraXradioAside": integraXradioAside,
       "integraXradioAtxMute": integraXradioAtxMute,
       "integraXradioAtxMuteDuration": integraXradioAtxMuteDuration,
       "integraXradioAduplexShift": integraXradioAduplexShift,
       "integraXradioArxFrequency": integraXradioArxFrequency,
       "integraXradioAtemperature": integraXradioAtemperature,
       "integraXradioApll": integraXradioApll,
       "integraXradioArangesTable": integraXradioArangesTable,
       "integraXradioArangeEntry": integraXradioArangeEntry,
       "integraXradioArangeEntryIndex": integraXradioArangeEntryIndex,
       "integraXradioArangeDescr": integraXradioArangeDescr,
       "integraXradioArangeTxPower": integraXradioArangeTxPower,
       "integraXradioArangeTxFrequency": integraXradioArangeTxFrequency,
       "integraXradioB": integraXradioB,
       "integraXradioBtxPower": integraXradioBtxPower,
       "integraXradioBtxFrequency": integraXradioBtxFrequency,
       "integraXradioBrxLevel": integraXradioBrxLevel,
       "integraXradioBrxLevelState": integraXradioBrxLevelState,
       "integraXradioBside": integraXradioBside,
       "integraXradioBtxMute": integraXradioBtxMute,
       "integraXradioBtxMuteDuration": integraXradioBtxMuteDuration,
       "integraXradioBduplexShift": integraXradioBduplexShift,
       "integraXradioBrxFrequency": integraXradioBrxFrequency,
       "integraXradioBtemperature": integraXradioBtemperature,
       "integraXradioBpll": integraXradioBpll,
       "integraXradioBrangesTable": integraXradioBrangesTable,
       "integraXradioBrangeEntry": integraXradioBrangeEntry,
       "integraXradioBrangeEntryIndex": integraXradioBrangeEntryIndex,
       "integraXradioBrangeDescr": integraXradioBrangeDescr,
       "integraXradioBrangeTxPower": integraXradioBrangeTxPower,
       "integraXradioBrangeTxFrequency": integraXradioBrangeTxFrequency,
       "integraXmodem": integraXmodem,
       "integraXmodemA": integraXmodemA,
       "integraXmodemAacquireStatus": integraXmodemAacquireStatus,
       "integraXmodemAnormalizedMse": integraXmodemAnormalizedMse,
       "integraXmodemAfecLoad": integraXmodemAfecLoad,
       "integraXmodemAxpdEst": integraXmodemAxpdEst,
       "integraXmodemAacquireLastStatusDetails": integraXmodemAacquireLastStatusDetails,
       "integraXmodemAtemperature": integraXmodemAtemperature,
       "integraXmodemArxModulation": integraXmodemArxModulation,
       "integraXmodemAtxModulation": integraXmodemAtxModulation,
       "integraXmodemArxCapacity": integraXmodemArxCapacity,
       "integraXmodemAtxCapacity": integraXmodemAtxCapacity,
       "integraXmodemAacmEngine": integraXmodemAacmEngine,
       "integraXmodemAcarrierOffset": integraXmodemAcarrierOffset,
       "integraXmodemAcountTime": integraXmodemAcountTime,
       "integraXmodemAerroredBlock": integraXmodemAerroredBlock,
       "integraXmodemAerroredSecond": integraXmodemAerroredSecond,
       "integraXmodemAseverelyErroredSecond": integraXmodemAseverelyErroredSecond,
       "integraXmodemAbackgroundBlockError": integraXmodemAbackgroundBlockError,
       "integraXmodemAtotalBlockNumber": integraXmodemAtotalBlockNumber,
       "integraXmodemAerroredSecondRatio": integraXmodemAerroredSecondRatio,
       "integraXmodemAseverelyErroredSecondRatio": integraXmodemAseverelyErroredSecondRatio,
       "integraXmodemAbackgroundBlockErrorRatio": integraXmodemAbackgroundBlockErrorRatio,
       "integraXmodemAuptime": integraXmodemAuptime,
       "integraXmodemAunavailtime": integraXmodemAunavailtime,
       "integraXmodemAfecLdpcBlockCounter": integraXmodemAfecLdpcBlockCounter,
       "integraXmodemAfecLdpcUncorrectedBlockCounter": integraXmodemAfecLdpcUncorrectedBlockCounter,
       "integraXmodemAfecLdpcUncorrectedPercent": integraXmodemAfecLdpcUncorrectedPercent,
       "integraXmodemAfecRsBlockCounter": integraXmodemAfecRsBlockCounter,
       "integraXmodemAfecRsUncorrectedBlockCounter": integraXmodemAfecRsUncorrectedBlockCounter,
       "integraXmodemAmodulationACMmin": integraXmodemAmodulationACMmin,
       "integraXmodemAmodulationACMmax": integraXmodemAmodulationACMmax,
       "integraXmodemB": integraXmodemB,
       "integraXmodemBacquireStatus": integraXmodemBacquireStatus,
       "integraXmodemBnormalizedMse": integraXmodemBnormalizedMse,
       "integraXmodemBfecLoad": integraXmodemBfecLoad,
       "integraXmodemBxpdEst": integraXmodemBxpdEst,
       "integraXmodemBacquireLastStatusDetails": integraXmodemBacquireLastStatusDetails,
       "integraXmodemBtemperature": integraXmodemBtemperature,
       "integraXmodemBrxModulation": integraXmodemBrxModulation,
       "integraXmodemBtxModulation": integraXmodemBtxModulation,
       "integraXmodemBrxCapacity": integraXmodemBrxCapacity,
       "integraXmodemBtxCapacity": integraXmodemBtxCapacity,
       "integraXmodemBacmEngine": integraXmodemBacmEngine,
       "integraXmodemBcarrierOffset": integraXmodemBcarrierOffset,
       "integraXmodemBcountTime": integraXmodemBcountTime,
       "integraXmodemBerroredBlock": integraXmodemBerroredBlock,
       "integraXmodemBerroredSecond": integraXmodemBerroredSecond,
       "integraXmodemBseverelyErroredSecond": integraXmodemBseverelyErroredSecond,
       "integraXmodemBbackgroundBlockError": integraXmodemBbackgroundBlockError,
       "integraXmodemBtotalBlockNumber": integraXmodemBtotalBlockNumber,
       "integraXmodemBerroredSecondRatio": integraXmodemBerroredSecondRatio,
       "integraXmodemBseverelyErroredSecondRatio": integraXmodemBseverelyErroredSecondRatio,
       "integraXmodemBbackgroundBlockErrorRatio": integraXmodemBbackgroundBlockErrorRatio,
       "integraXmodemBuptime": integraXmodemBuptime,
       "integraXmodemBunavailtime": integraXmodemBunavailtime,
       "integraXmodemBfecLdpcBlockCounter": integraXmodemBfecLdpcBlockCounter,
       "integraXmodemBfecLdpcUncorrectedBlockCounter": integraXmodemBfecLdpcUncorrectedBlockCounter,
       "integraXmodemBfecLdpcUncorrectedPercent": integraXmodemBfecLdpcUncorrectedPercent,
       "integraXmodemBfecRsBlockCounter": integraXmodemBfecRsBlockCounter,
       "integraXmodemBfecRsUncorrectedBlockCounter": integraXmodemBfecRsUncorrectedBlockCounter,
       "integraXmodemBmodulationACMmin": integraXmodemBmodulationACMmin,
       "integraXmodemBmodulationACMmax": integraXmodemBmodulationACMmax,
       "integraXmodemBandwidth": integraXmodemBandwidth,
       "integraXmodemModulation": integraXmodemModulation,
       "integraXsystem": integraXsystem,
       "integraXsysCPUtemperature": integraXsysCPUtemperature,
       "integraXsysLicenseExpire": integraXsysLicenseExpire,
       "integraXsysLicenseGenStatus": integraXsysLicenseGenStatus,
       "integraXsysPSUvoltage": integraXsysPSUvoltage,
       "integraXsysPSUcurrent": integraXsysPSUcurrent,
       "integraXsysPSUpower": integraXsysPSUpower,
       "integraXsysBoardTemperature": integraXsysBoardTemperature,
       "integraXsysFreeMemory": integraXsysFreeMemory,
       "integraXsysCPUidle": integraXsysCPUidle,
       "integraXsysDeviceType": integraXsysDeviceType,
       "integraXsysDeviceSerial": integraXsysDeviceSerial,
       "integraXsysDeviceProductModel": integraXsysDeviceProductModel,
       "integraXsysFanError": integraXsysFanError,
       "integraXsysSw1v0core": integraXsysSw1v0core,
       "integraXsysSw1v0avdd": integraXsysSw1v0avdd,
       "integraXsysSw1v2a": integraXsysSw1v2a,
       "integraXsysSw1v5ddr": integraXsysSw1v5ddr,
       "integraXsysSw1v8": integraXsysSw1v8,
       "integraXsysSw2v5": integraXsysSw2v5,
       "integraXsysSw3v3": integraXsysSw3v3,
       "integraXsysVttrefPs": integraXsysVttrefPs,
       "integraXsysVttddrPs": integraXsysVttddrPs,
       "integraXsysZq1v0": integraXsysZq1v0,
       "integraXsysZq1v5": integraXsysZq1v5,
       "integraXsysZq1v8": integraXsysZq1v8,
       "integraXsysZq2v5": integraXsysZq2v5,
       "integraXsysZq3v3": integraXsysZq3v3,
       "integraXsys5v0d": integraXsys5v0d,
       "integraXsysSw1v2": integraXsysSw1v2,
       "integraXsysMdmVddcAvs": integraXsysMdmVddcAvs,
       "integraXsysMdm3v3": integraXsysMdm3v3,
       "integraXsysMdm1v0aPm": integraXsysMdm1v0aPm,
       "integraXsysMdm1v0a": integraXsysMdm1v0a,
       "integraXsysMdm1v8a": integraXsysMdm1v8a,
       "integraXsysMdmDAC02v5a": integraXsysMdmDAC02v5a,
       "integraXsysMdmDAC12v5": integraXsysMdmDAC12v5,
       "integraXsysMdmDAC22v5": integraXsysMdmDAC22v5,
       "integraXsysMdm1v8io": integraXsysMdm1v8io,
       "integraXsysMdm3v3io": integraXsysMdm3v3io,
       "integraXsys3v3Radio": integraXsys3v3Radio,
       "integraXsysMdm4v0": integraXsysMdm4v0,
       "integraXsys5v0nRadio": integraXsys5v0nRadio,
       "integraXsysCoreVddSns": integraXsysCoreVddSns,
       "integraXsys40v0RadioSns": integraXsys40v0RadioSns,
       "integraXsysServices": integraXsysServices,
       "integraXsysServicesReboot": integraXsysServicesReboot,
       "integraXsysServicesFtpSwitch": integraXsysServicesFtpSwitch,
       "integraXsysServicesFwCurrInfo": integraXsysServicesFwCurrInfo,
       "integraXsysServicesFwAvailView": integraXsysServicesFwAvailView,
       "integraXsysServicesFwRemove": integraXsysServicesFwRemove,
       "integraXsysServicesFwRemoveAll": integraXsysServicesFwRemoveAll,
       "integraXsysServicesFwUpload": integraXsysServicesFwUpload,
       "integraXsysServicesFwInst": integraXsysServicesFwInst,
       "integraXsysServicesFwSwitchRunning": integraXsysServicesFwSwitchRunning,
       "integraXsysServicesFwSwitchNext": integraXsysServicesFwSwitchNext,
       "integraXethernet": integraXethernet,
       "integraXifStatusTable": integraXifStatusTable,
       "integraXifPortEntry": integraXifPortEntry,
       "integraXifPortStatIndex": integraXifPortStatIndex,
       "integraXifPortStatDescr": integraXifPortStatDescr,
       "integraXifPortType": integraXifPortType,
       "integraXifPortMtu": integraXifPortMtu,
       "integraXifPortHighSpeed": integraXifPortHighSpeed,
       "integraXifPortPhysAddress": integraXifPortPhysAddress,
       "integraXifPortAdminStatus": integraXifPortAdminStatus,
       "integraXifPortOperStatus": integraXifPortOperStatus,
       "integraXifPortLastChange": integraXifPortLastChange,
       "integraXifPortAutoneg": integraXifPortAutoneg,
       "integraXifPortDuplex": integraXifPortDuplex,
       "integraXifPortSyncEthActive": integraXifPortSyncEthActive,
       "integraXifPortSyncEthPrio": integraXifPortSyncEthPrio,
       "integraXifPortFlowControl": integraXifPortFlowControl,
       "integraXifStatisticsTable": integraXifStatisticsTable,
       "integraXifPortStcEntry": integraXifPortStcEntry,
       "integraXifPortStcIndex": integraXifPortStcIndex,
       "integraXifPortStcDescr": integraXifPortStcDescr,
       "integraXifTimePassed": integraXifTimePassed,
       "integraXifIngressPackets": integraXifIngressPackets,
       "integraXifIngressBytes": integraXifIngressBytes,
       "integraXifEgressPackets": integraXifEgressPackets,
       "integraXifEgressBytes": integraXifEgressBytes,
       "integraXifEtherStatsMulticastPkts": integraXifEtherStatsMulticastPkts,
       "integraXifEtherStatsBroadcastPkts": integraXifEtherStatsBroadcastPkts,
       "integraXifEtherStatsPkts64Octets": integraXifEtherStatsPkts64Octets,
       "integraXifEtherStatsPkts65to127Octets": integraXifEtherStatsPkts65to127Octets,
       "integraXifEtherStatsPkts128to255Octets": integraXifEtherStatsPkts128to255Octets,
       "integraXifEtherStatsPkts256to511Octets": integraXifEtherStatsPkts256to511Octets,
       "integraXifEtherStatsPkts512to1023Octets": integraXifEtherStatsPkts512to1023Octets,
       "integraXifEtherStatsPkts1024to1518Octets": integraXifEtherStatsPkts1024to1518Octets,
       "integraXifEtherStatsOversizePkts": integraXifEtherStatsOversizePkts,
       "integraXifEtherRxOversizePkts": integraXifEtherRxOversizePkts,
       "integraXifEtherTxOversizePkts": integraXifEtherTxOversizePkts,
       "integraXifEtherStatsOctets": integraXifEtherStatsOctets,
       "integraXifEtherStatsPkts": integraXifEtherStatsPkts,
       "integraXifEtherStatsTXNoErrors": integraXifEtherStatsTXNoErrors,
       "integraXifEtherStatsRXNoErrors": integraXifEtherStatsRXNoErrors,
       "integraXifEtherStatsPkts1519to1522Octets": integraXifEtherStatsPkts1519to1522Octets,
       "integraXifIfInOctets": integraXifIfInOctets,
       "integraXifIfOutOctets": integraXifIfOutOctets,
       "integraXifDot1dTpPortInFrames": integraXifDot1dTpPortInFrames,
       "integraXifDot1dTpPortOutFrames": integraXifDot1dTpPortOutFrames,
       "integraXifReceivedPkts64Octets": integraXifReceivedPkts64Octets,
       "integraXifTransmittedPkts64Octets": integraXifTransmittedPkts64Octets,
       "integraXifReceivedPkts65to127Octets": integraXifReceivedPkts65to127Octets,
       "integraXifTransmittedPkts65to127Octets": integraXifTransmittedPkts65to127Octets,
       "integraXifReceivedPkts128to255Octets": integraXifReceivedPkts128to255Octets,
       "integraXifTransmittedPkts128to255Octets": integraXifTransmittedPkts128to255Octets,
       "integraXifReceivedPkts256to511Octets": integraXifReceivedPkts256to511Octets,
       "integraXifTransmittedPkts256to511Octets": integraXifTransmittedPkts256to511Octets,
       "integraXifReceivedPkts512to1023Octets": integraXifReceivedPkts512to1023Octets,
       "integraXifTransmittedPkts512to1023Octets": integraXifTransmittedPkts512to1023Octets,
       "integraXifReceivedPkts1024to1518Octets": integraXifReceivedPkts1024to1518Octets,
       "integraXifTransmittedPkts1024to1518Octets": integraXifTransmittedPkts1024to1518Octets,
       "integraXifIfInBroadcastPkts": integraXifIfInBroadcastPkts,
       "integraXifIfOutBroadcastPkts": integraXifIfOutBroadcastPkts,
       "integraXifIfInMulticastPkts": integraXifIfInMulticastPkts,
       "integraXifIfOutMulticastPkts": integraXifIfOutMulticastPkts,
       "integraXifDot3InPauseFrames": integraXifDot3InPauseFrames,
       "integraXifDot3OutPauseFrames": integraXifDot3OutPauseFrames,
       "integraXifEtherStatsUndersizePkts": integraXifEtherStatsUndersizePkts,
       "integraXifEtherStatsFragments": integraXifEtherStatsFragments,
       "integraXifEtherStatsCRCAlignErrors": integraXifEtherStatsCRCAlignErrors,
       "integraXifEtherStatsJabbers": integraXifEtherStatsJabbers,
       "integraXifIngressBPS": integraXifIngressBPS,
       "integraXifIngressPPS": integraXifIngressPPS,
       "integraXifEgressBPS": integraXifEgressBPS,
       "integraXifEgressPPS": integraXifEgressPPS,
       "integraXifAllCoSQoutPackets": integraXifAllCoSQoutPackets,
       "integraXifAllCoSQoutBytes": integraXifAllCoSQoutBytes,
       "integraXifAllCoSQdroppedPackets": integraXifAllCoSQdroppedPackets,
       "integraXifAllCoSQdroppedBytes": integraXifAllCoSQdroppedBytes,
       "integraXifProcessedRxPackets": integraXifProcessedRxPackets,
       "integraXifProcessedRxBytes": integraXifProcessedRxBytes,
       "integraXifLspPortAdminState": integraXifLspPortAdminState,
       "integraXifLspPortList": integraXifLspPortList,
       "integraXifLspPortStatus": integraXifLspPortStatus,
       "integraXexecuteConfig": integraXexecuteConfig,
       "integraXneedStore": integraXneedStore,
       "integraXstoreConfig": integraXstoreConfig,
       "integraXnetCfg": integraXnetCfg,
       "integraXnetCfgIPaddress": integraXnetCfgIPaddress,
       "integraXnetCfgIPmask": integraXnetCfgIPmask,
       "integraXnetCfgIPgateway": integraXnetCfgIPgateway,
       "integraXnetCfgRemoteIPaddress": integraXnetCfgRemoteIPaddress,
       "integraXConformance": integraXConformance,
       "integraXCompliances": integraXCompliances,
       "integraXCompliance": integraXCompliance,
       "integraXGroups": integraXGroups,
       "integraXMiscGroup": integraXMiscGroup,
       "integraXRadioGroup": integraXRadioGroup,
       "integraXModemGroup": integraXModemGroup,
       "integraXSystemGroup": integraXSystemGroup,
       "integraXEthernetGeneralGroup": integraXEthernetGeneralGroup,
       "integraXEthernetMiiPortGroup": integraXEthernetMiiPortGroup}
)
