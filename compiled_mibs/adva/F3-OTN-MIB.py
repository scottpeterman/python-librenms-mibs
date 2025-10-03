# SNMP MIB module (F3-OTN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-OTN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:16:29 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(CmPmIntervalType,
 PerfCounter64) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "CmPmIntervalType",
    "PerfCounter64")

(cmEthernetNetPortEntry,) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "cmEthernetNetPortEntry")

(cmEthernetNetPortHistoryEntry,
 cmEthernetNetPortStatsEntry) = mibBuilder.importSymbols(
    "CM-PERFORMANCE-MIB",
    "cmEthernetNetPortHistoryEntry",
    "cmEthernetNetPortStatsEntry")

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
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3OtnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34)
)
if mibBuilder.loadTexts:
    f3OtnMIB.setRevisions(
        ("2014-07-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OtnFacilityType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("otu2e-eth", 1)
    )



class OtnFecType(TextualConvention, Integer32):
    status = "current"
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
        *(("nofec", 1),
          ("gfec", 2),
          ("efec-1", 3),
          ("efec-2", 4))
    )



class TimDetectMode(TextualConvention, Integer32):
    status = "current"
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
        *(("off", 1),
          ("sapi", 2),
          ("dapi", 3),
          ("sapi-dapi", 4))
    )



# MIB Managed Objects in the order of their OIDs

_F3OtnConfigObjects_ObjectIdentity = ObjectIdentity
f3OtnConfigObjects = _F3OtnConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1)
)
_F3OtnNetPortExtTable_Object = MibTable
f3OtnNetPortExtTable = _F3OtnNetPortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1)
)
if mibBuilder.loadTexts:
    f3OtnNetPortExtTable.setStatus("current")
_F3OtnNetPortEntry_Object = MibTableRow
f3OtnNetPortEntry = _F3OtnNetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1)
)
if mibBuilder.loadTexts:
    f3OtnNetPortEntry.setStatus("current")
_F3OtnNetPortPayloadType_Type = Unsigned32
_F3OtnNetPortPayloadType_Object = MibTableColumn
f3OtnNetPortPayloadType = _F3OtnNetPortPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 1),
    _F3OtnNetPortPayloadType_Type()
)
f3OtnNetPortPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OtnNetPortPayloadType.setStatus("current")
_F3OtnNetPortFacilityType_Type = OtnFacilityType
_F3OtnNetPortFacilityType_Object = MibTableColumn
f3OtnNetPortFacilityType = _F3OtnNetPortFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 2),
    _F3OtnNetPortFacilityType_Type()
)
f3OtnNetPortFacilityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OtnNetPortFacilityType.setStatus("current")
_F3OtnNetPortFec_Type = OtnFecType
_F3OtnNetPortFec_Object = MibTableColumn
f3OtnNetPortFec = _F3OtnNetPortFec_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 3),
    _F3OtnNetPortFec_Type()
)
f3OtnNetPortFec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OtnNetPortFec.setStatus("current")
_F3OtnNetPortTimDetectModeOtu_Type = TimDetectMode
_F3OtnNetPortTimDetectModeOtu_Object = MibTableColumn
f3OtnNetPortTimDetectModeOtu = _F3OtnNetPortTimDetectModeOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 4),
    _F3OtnNetPortTimDetectModeOtu_Type()
)
f3OtnNetPortTimDetectModeOtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OtnNetPortTimDetectModeOtu.setStatus("current")
_F3OtnNetPortTimAisInsertOtuEnabled_Type = TruthValue
_F3OtnNetPortTimAisInsertOtuEnabled_Object = MibTableColumn
f3OtnNetPortTimAisInsertOtuEnabled = _F3OtnNetPortTimAisInsertOtuEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 5),
    _F3OtnNetPortTimAisInsertOtuEnabled_Type()
)
f3OtnNetPortTimAisInsertOtuEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OtnNetPortTimAisInsertOtuEnabled.setStatus("current")
_F3OtnNetPortTtiActualRxHexOtu_Type = OctetString
_F3OtnNetPortTtiActualRxHexOtu_Object = MibTableColumn
f3OtnNetPortTtiActualRxHexOtu = _F3OtnNetPortTtiActualRxHexOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 6),
    _F3OtnNetPortTtiActualRxHexOtu_Type()
)
f3OtnNetPortTtiActualRxHexOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortTtiActualRxHexOtu.setStatus("current")
_F3OtnNetPortTtiSapiActualRxOtu_Type = DisplayString
_F3OtnNetPortTtiSapiActualRxOtu_Object = MibTableColumn
f3OtnNetPortTtiSapiActualRxOtu = _F3OtnNetPortTtiSapiActualRxOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 7),
    _F3OtnNetPortTtiSapiActualRxOtu_Type()
)
f3OtnNetPortTtiSapiActualRxOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortTtiSapiActualRxOtu.setStatus("current")
_F3OtnNetPortTtiDapiActualRxOtu_Type = DisplayString
_F3OtnNetPortTtiDapiActualRxOtu_Object = MibTableColumn
f3OtnNetPortTtiDapiActualRxOtu = _F3OtnNetPortTtiDapiActualRxOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 8),
    _F3OtnNetPortTtiDapiActualRxOtu_Type()
)
f3OtnNetPortTtiDapiActualRxOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortTtiDapiActualRxOtu.setStatus("current")
_F3OtnNetPortTtiOpSpActualRxOtu_Type = DisplayString
_F3OtnNetPortTtiOpSpActualRxOtu_Object = MibTableColumn
f3OtnNetPortTtiOpSpActualRxOtu = _F3OtnNetPortTtiOpSpActualRxOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 9),
    _F3OtnNetPortTtiOpSpActualRxOtu_Type()
)
f3OtnNetPortTtiOpSpActualRxOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortTtiOpSpActualRxOtu.setStatus("current")


class _F3OtnNetPortTtiSapiExpectedRxOtu_Type(DisplayString):
    """Custom type f3OtnNetPortTtiSapiExpectedRxOtu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_F3OtnNetPortTtiSapiExpectedRxOtu_Type.__name__ = "DisplayString"
_F3OtnNetPortTtiSapiExpectedRxOtu_Object = MibTableColumn
f3OtnNetPortTtiSapiExpectedRxOtu = _F3OtnNetPortTtiSapiExpectedRxOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 10),
    _F3OtnNetPortTtiSapiExpectedRxOtu_Type()
)
f3OtnNetPortTtiSapiExpectedRxOtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OtnNetPortTtiSapiExpectedRxOtu.setStatus("current")


class _F3OtnNetPortTtiSapiTxOtu_Type(DisplayString):
    """Custom type f3OtnNetPortTtiSapiTxOtu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_F3OtnNetPortTtiSapiTxOtu_Type.__name__ = "DisplayString"
_F3OtnNetPortTtiSapiTxOtu_Object = MibTableColumn
f3OtnNetPortTtiSapiTxOtu = _F3OtnNetPortTtiSapiTxOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 11),
    _F3OtnNetPortTtiSapiTxOtu_Type()
)
f3OtnNetPortTtiSapiTxOtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OtnNetPortTtiSapiTxOtu.setStatus("current")


class _F3OtnNetPortTtiDapiTxOtu_Type(DisplayString):
    """Custom type f3OtnNetPortTtiDapiTxOtu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_F3OtnNetPortTtiDapiTxOtu_Type.__name__ = "DisplayString"
_F3OtnNetPortTtiDapiTxOtu_Object = MibTableColumn
f3OtnNetPortTtiDapiTxOtu = _F3OtnNetPortTtiDapiTxOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 12),
    _F3OtnNetPortTtiDapiTxOtu_Type()
)
f3OtnNetPortTtiDapiTxOtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OtnNetPortTtiDapiTxOtu.setStatus("current")


class _F3OtnNetPortTtiOpSpTxOtu_Type(DisplayString):
    """Custom type f3OtnNetPortTtiOpSpTxOtu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_F3OtnNetPortTtiOpSpTxOtu_Type.__name__ = "DisplayString"
_F3OtnNetPortTtiOpSpTxOtu_Object = MibTableColumn
f3OtnNetPortTtiOpSpTxOtu = _F3OtnNetPortTtiOpSpTxOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 13),
    _F3OtnNetPortTtiOpSpTxOtu_Type()
)
f3OtnNetPortTtiOpSpTxOtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OtnNetPortTtiOpSpTxOtu.setStatus("current")
_F3OtnNetPortTimDetectModeOdu_Type = TimDetectMode
_F3OtnNetPortTimDetectModeOdu_Object = MibTableColumn
f3OtnNetPortTimDetectModeOdu = _F3OtnNetPortTimDetectModeOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 14),
    _F3OtnNetPortTimDetectModeOdu_Type()
)
f3OtnNetPortTimDetectModeOdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OtnNetPortTimDetectModeOdu.setStatus("current")
_F3OtnNetPortTimAisInsertOduEnabled_Type = TruthValue
_F3OtnNetPortTimAisInsertOduEnabled_Object = MibTableColumn
f3OtnNetPortTimAisInsertOduEnabled = _F3OtnNetPortTimAisInsertOduEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 15),
    _F3OtnNetPortTimAisInsertOduEnabled_Type()
)
f3OtnNetPortTimAisInsertOduEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OtnNetPortTimAisInsertOduEnabled.setStatus("current")
_F3OtnNetPortTtiActualRxHexOdu_Type = OctetString
_F3OtnNetPortTtiActualRxHexOdu_Object = MibTableColumn
f3OtnNetPortTtiActualRxHexOdu = _F3OtnNetPortTtiActualRxHexOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 16),
    _F3OtnNetPortTtiActualRxHexOdu_Type()
)
f3OtnNetPortTtiActualRxHexOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortTtiActualRxHexOdu.setStatus("current")
_F3OtnNetPortTtiSapiActualRxOdu_Type = DisplayString
_F3OtnNetPortTtiSapiActualRxOdu_Object = MibTableColumn
f3OtnNetPortTtiSapiActualRxOdu = _F3OtnNetPortTtiSapiActualRxOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 17),
    _F3OtnNetPortTtiSapiActualRxOdu_Type()
)
f3OtnNetPortTtiSapiActualRxOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortTtiSapiActualRxOdu.setStatus("current")
_F3OtnNetPortTtiDapiActualRxOdu_Type = DisplayString
_F3OtnNetPortTtiDapiActualRxOdu_Object = MibTableColumn
f3OtnNetPortTtiDapiActualRxOdu = _F3OtnNetPortTtiDapiActualRxOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 18),
    _F3OtnNetPortTtiDapiActualRxOdu_Type()
)
f3OtnNetPortTtiDapiActualRxOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortTtiDapiActualRxOdu.setStatus("current")
_F3OtnNetPortTtiOpSpActualRxOdu_Type = DisplayString
_F3OtnNetPortTtiOpSpActualRxOdu_Object = MibTableColumn
f3OtnNetPortTtiOpSpActualRxOdu = _F3OtnNetPortTtiOpSpActualRxOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 19),
    _F3OtnNetPortTtiOpSpActualRxOdu_Type()
)
f3OtnNetPortTtiOpSpActualRxOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortTtiOpSpActualRxOdu.setStatus("current")


class _F3OtnNetPortTtiSapiExpectedRxOdu_Type(DisplayString):
    """Custom type f3OtnNetPortTtiSapiExpectedRxOdu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_F3OtnNetPortTtiSapiExpectedRxOdu_Type.__name__ = "DisplayString"
_F3OtnNetPortTtiSapiExpectedRxOdu_Object = MibTableColumn
f3OtnNetPortTtiSapiExpectedRxOdu = _F3OtnNetPortTtiSapiExpectedRxOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 20),
    _F3OtnNetPortTtiSapiExpectedRxOdu_Type()
)
f3OtnNetPortTtiSapiExpectedRxOdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OtnNetPortTtiSapiExpectedRxOdu.setStatus("current")


class _F3OtnNetPortTtiSapiTxOdu_Type(DisplayString):
    """Custom type f3OtnNetPortTtiSapiTxOdu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_F3OtnNetPortTtiSapiTxOdu_Type.__name__ = "DisplayString"
_F3OtnNetPortTtiSapiTxOdu_Object = MibTableColumn
f3OtnNetPortTtiSapiTxOdu = _F3OtnNetPortTtiSapiTxOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 21),
    _F3OtnNetPortTtiSapiTxOdu_Type()
)
f3OtnNetPortTtiSapiTxOdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OtnNetPortTtiSapiTxOdu.setStatus("current")


class _F3OtnNetPortTtiDapiTxOdu_Type(DisplayString):
    """Custom type f3OtnNetPortTtiDapiTxOdu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_F3OtnNetPortTtiDapiTxOdu_Type.__name__ = "DisplayString"
_F3OtnNetPortTtiDapiTxOdu_Object = MibTableColumn
f3OtnNetPortTtiDapiTxOdu = _F3OtnNetPortTtiDapiTxOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 22),
    _F3OtnNetPortTtiDapiTxOdu_Type()
)
f3OtnNetPortTtiDapiTxOdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OtnNetPortTtiDapiTxOdu.setStatus("current")


class _F3OtnNetPortTtiOpSpTxOdu_Type(DisplayString):
    """Custom type f3OtnNetPortTtiOpSpTxOdu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_F3OtnNetPortTtiOpSpTxOdu_Type.__name__ = "DisplayString"
_F3OtnNetPortTtiOpSpTxOdu_Object = MibTableColumn
f3OtnNetPortTtiOpSpTxOdu = _F3OtnNetPortTtiOpSpTxOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 23),
    _F3OtnNetPortTtiOpSpTxOdu_Type()
)
f3OtnNetPortTtiOpSpTxOdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OtnNetPortTtiOpSpTxOdu.setStatus("current")
_F3OtnPerfObjects_ObjectIdentity = ObjectIdentity
f3OtnPerfObjects = _F3OtnPerfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2)
)
_F3OtnNetPortStatsExtTable_Object = MibTable
f3OtnNetPortStatsExtTable = _F3OtnNetPortStatsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1)
)
if mibBuilder.loadTexts:
    f3OtnNetPortStatsExtTable.setStatus("current")
_F3OtnNetPortStatsExtEntry_Object = MibTableRow
f3OtnNetPortStatsExtEntry = _F3OtnNetPortStatsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1)
)
if mibBuilder.loadTexts:
    f3OtnNetPortStatsExtEntry.setStatus("current")
_F3OtnNetPortStatsExtBerBeforeCorr_Type = PerfCounter64
_F3OtnNetPortStatsExtBerBeforeCorr_Object = MibTableColumn
f3OtnNetPortStatsExtBerBeforeCorr = _F3OtnNetPortStatsExtBerBeforeCorr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 1),
    _F3OtnNetPortStatsExtBerBeforeCorr_Type()
)
f3OtnNetPortStatsExtBerBeforeCorr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortStatsExtBerBeforeCorr.setStatus("current")
_F3OtnNetPortStatsExtFecErrSec_Type = Integer32
_F3OtnNetPortStatsExtFecErrSec_Object = MibTableColumn
f3OtnNetPortStatsExtFecErrSec = _F3OtnNetPortStatsExtFecErrSec_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 2),
    _F3OtnNetPortStatsExtFecErrSec_Type()
)
f3OtnNetPortStatsExtFecErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortStatsExtFecErrSec.setStatus("current")
_F3OtnNetPortStatsExtFecSES_Type = Integer32
_F3OtnNetPortStatsExtFecSES_Object = MibTableColumn
f3OtnNetPortStatsExtFecSES = _F3OtnNetPortStatsExtFecSES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 3),
    _F3OtnNetPortStatsExtFecSES_Type()
)
f3OtnNetPortStatsExtFecSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortStatsExtFecSES.setStatus("current")
_F3OtnNetPortStatsExtFecCorrErr_Type = PerfCounter64
_F3OtnNetPortStatsExtFecCorrErr_Object = MibTableColumn
f3OtnNetPortStatsExtFecCorrErr = _F3OtnNetPortStatsExtFecCorrErr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 4),
    _F3OtnNetPortStatsExtFecCorrErr_Type()
)
f3OtnNetPortStatsExtFecCorrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortStatsExtFecCorrErr.setStatus("current")
_F3OtnNetPortStatsExtFecUncorrBlockErr_Type = PerfCounter64
_F3OtnNetPortStatsExtFecUncorrBlockErr_Object = MibTableColumn
f3OtnNetPortStatsExtFecUncorrBlockErr = _F3OtnNetPortStatsExtFecUncorrBlockErr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 5),
    _F3OtnNetPortStatsExtFecUncorrBlockErr_Type()
)
f3OtnNetPortStatsExtFecUncorrBlockErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortStatsExtFecUncorrBlockErr.setStatus("current")
_F3OtnNetPortStatsExtOtuErrSec_Type = Integer32
_F3OtnNetPortStatsExtOtuErrSec_Object = MibTableColumn
f3OtnNetPortStatsExtOtuErrSec = _F3OtnNetPortStatsExtOtuErrSec_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 6),
    _F3OtnNetPortStatsExtOtuErrSec_Type()
)
f3OtnNetPortStatsExtOtuErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortStatsExtOtuErrSec.setStatus("current")
_F3OtnNetPortStatsExtOtuSES_Type = Integer32
_F3OtnNetPortStatsExtOtuSES_Object = MibTableColumn
f3OtnNetPortStatsExtOtuSES = _F3OtnNetPortStatsExtOtuSES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 7),
    _F3OtnNetPortStatsExtOtuSES_Type()
)
f3OtnNetPortStatsExtOtuSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortStatsExtOtuSES.setStatus("current")
_F3OtnNetPortStatsExtOtuBBE_Type = PerfCounter64
_F3OtnNetPortStatsExtOtuBBE_Object = MibTableColumn
f3OtnNetPortStatsExtOtuBBE = _F3OtnNetPortStatsExtOtuBBE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 8),
    _F3OtnNetPortStatsExtOtuBBE_Type()
)
f3OtnNetPortStatsExtOtuBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortStatsExtOtuBBE.setStatus("current")
_F3OtnNetPortStatsExtOtuUAS_Type = Integer32
_F3OtnNetPortStatsExtOtuUAS_Object = MibTableColumn
f3OtnNetPortStatsExtOtuUAS = _F3OtnNetPortStatsExtOtuUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 9),
    _F3OtnNetPortStatsExtOtuUAS_Type()
)
f3OtnNetPortStatsExtOtuUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortStatsExtOtuUAS.setStatus("current")
_F3OtnNetPortStatsExtOduErrSec_Type = Integer32
_F3OtnNetPortStatsExtOduErrSec_Object = MibTableColumn
f3OtnNetPortStatsExtOduErrSec = _F3OtnNetPortStatsExtOduErrSec_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 10),
    _F3OtnNetPortStatsExtOduErrSec_Type()
)
f3OtnNetPortStatsExtOduErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortStatsExtOduErrSec.setStatus("current")
_F3OtnNetPortStatsExtOduSES_Type = Integer32
_F3OtnNetPortStatsExtOduSES_Object = MibTableColumn
f3OtnNetPortStatsExtOduSES = _F3OtnNetPortStatsExtOduSES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 11),
    _F3OtnNetPortStatsExtOduSES_Type()
)
f3OtnNetPortStatsExtOduSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortStatsExtOduSES.setStatus("current")
_F3OtnNetPortStatsExtOduBBE_Type = PerfCounter64
_F3OtnNetPortStatsExtOduBBE_Object = MibTableColumn
f3OtnNetPortStatsExtOduBBE = _F3OtnNetPortStatsExtOduBBE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 12),
    _F3OtnNetPortStatsExtOduBBE_Type()
)
f3OtnNetPortStatsExtOduBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortStatsExtOduBBE.setStatus("current")
_F3OtnNetPortStatsExtOduUAS_Type = Integer32
_F3OtnNetPortStatsExtOduUAS_Object = MibTableColumn
f3OtnNetPortStatsExtOduUAS = _F3OtnNetPortStatsExtOduUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 13),
    _F3OtnNetPortStatsExtOduUAS_Type()
)
f3OtnNetPortStatsExtOduUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortStatsExtOduUAS.setStatus("current")
_F3OtnNetPortHistoryExtTable_Object = MibTable
f3OtnNetPortHistoryExtTable = _F3OtnNetPortHistoryExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2)
)
if mibBuilder.loadTexts:
    f3OtnNetPortHistoryExtTable.setStatus("current")
_F3OtnNetPortHistoryExtEntry_Object = MibTableRow
f3OtnNetPortHistoryExtEntry = _F3OtnNetPortHistoryExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1)
)
if mibBuilder.loadTexts:
    f3OtnNetPortHistoryExtEntry.setStatus("current")
_F3OtnNetPortHistoryExtBerBeforeCorr_Type = PerfCounter64
_F3OtnNetPortHistoryExtBerBeforeCorr_Object = MibTableColumn
f3OtnNetPortHistoryExtBerBeforeCorr = _F3OtnNetPortHistoryExtBerBeforeCorr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 1),
    _F3OtnNetPortHistoryExtBerBeforeCorr_Type()
)
f3OtnNetPortHistoryExtBerBeforeCorr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortHistoryExtBerBeforeCorr.setStatus("current")
_F3OtnNetPortHistoryExtFecErrSec_Type = Integer32
_F3OtnNetPortHistoryExtFecErrSec_Object = MibTableColumn
f3OtnNetPortHistoryExtFecErrSec = _F3OtnNetPortHistoryExtFecErrSec_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 2),
    _F3OtnNetPortHistoryExtFecErrSec_Type()
)
f3OtnNetPortHistoryExtFecErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortHistoryExtFecErrSec.setStatus("current")
_F3OtnNetPortHistoryExtFecSES_Type = Integer32
_F3OtnNetPortHistoryExtFecSES_Object = MibTableColumn
f3OtnNetPortHistoryExtFecSES = _F3OtnNetPortHistoryExtFecSES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 3),
    _F3OtnNetPortHistoryExtFecSES_Type()
)
f3OtnNetPortHistoryExtFecSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortHistoryExtFecSES.setStatus("current")
_F3OtnNetPortHistoryExtFecCorrErr_Type = PerfCounter64
_F3OtnNetPortHistoryExtFecCorrErr_Object = MibTableColumn
f3OtnNetPortHistoryExtFecCorrErr = _F3OtnNetPortHistoryExtFecCorrErr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 4),
    _F3OtnNetPortHistoryExtFecCorrErr_Type()
)
f3OtnNetPortHistoryExtFecCorrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortHistoryExtFecCorrErr.setStatus("current")
_F3OtnNetPortHistoryExtFecUncorrBlockErr_Type = PerfCounter64
_F3OtnNetPortHistoryExtFecUncorrBlockErr_Object = MibTableColumn
f3OtnNetPortHistoryExtFecUncorrBlockErr = _F3OtnNetPortHistoryExtFecUncorrBlockErr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 5),
    _F3OtnNetPortHistoryExtFecUncorrBlockErr_Type()
)
f3OtnNetPortHistoryExtFecUncorrBlockErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortHistoryExtFecUncorrBlockErr.setStatus("current")
_F3OtnNetPortHistoryExtOtuErrSec_Type = Integer32
_F3OtnNetPortHistoryExtOtuErrSec_Object = MibTableColumn
f3OtnNetPortHistoryExtOtuErrSec = _F3OtnNetPortHistoryExtOtuErrSec_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 6),
    _F3OtnNetPortHistoryExtOtuErrSec_Type()
)
f3OtnNetPortHistoryExtOtuErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortHistoryExtOtuErrSec.setStatus("current")
_F3OtnNetPortHistoryExtOtuSES_Type = Integer32
_F3OtnNetPortHistoryExtOtuSES_Object = MibTableColumn
f3OtnNetPortHistoryExtOtuSES = _F3OtnNetPortHistoryExtOtuSES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 7),
    _F3OtnNetPortHistoryExtOtuSES_Type()
)
f3OtnNetPortHistoryExtOtuSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortHistoryExtOtuSES.setStatus("current")
_F3OtnNetPortHistoryExtOtuBBE_Type = PerfCounter64
_F3OtnNetPortHistoryExtOtuBBE_Object = MibTableColumn
f3OtnNetPortHistoryExtOtuBBE = _F3OtnNetPortHistoryExtOtuBBE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 8),
    _F3OtnNetPortHistoryExtOtuBBE_Type()
)
f3OtnNetPortHistoryExtOtuBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortHistoryExtOtuBBE.setStatus("current")
_F3OtnNetPortHistoryExtOtuUAS_Type = Integer32
_F3OtnNetPortHistoryExtOtuUAS_Object = MibTableColumn
f3OtnNetPortHistoryExtOtuUAS = _F3OtnNetPortHistoryExtOtuUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 9),
    _F3OtnNetPortHistoryExtOtuUAS_Type()
)
f3OtnNetPortHistoryExtOtuUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortHistoryExtOtuUAS.setStatus("current")
_F3OtnNetPortHistoryExtOduErrSec_Type = Integer32
_F3OtnNetPortHistoryExtOduErrSec_Object = MibTableColumn
f3OtnNetPortHistoryExtOduErrSec = _F3OtnNetPortHistoryExtOduErrSec_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 10),
    _F3OtnNetPortHistoryExtOduErrSec_Type()
)
f3OtnNetPortHistoryExtOduErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortHistoryExtOduErrSec.setStatus("current")
_F3OtnNetPortHistoryExtOduSES_Type = Integer32
_F3OtnNetPortHistoryExtOduSES_Object = MibTableColumn
f3OtnNetPortHistoryExtOduSES = _F3OtnNetPortHistoryExtOduSES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 11),
    _F3OtnNetPortHistoryExtOduSES_Type()
)
f3OtnNetPortHistoryExtOduSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortHistoryExtOduSES.setStatus("current")
_F3OtnNetPortHistoryExtOduBBE_Type = PerfCounter64
_F3OtnNetPortHistoryExtOduBBE_Object = MibTableColumn
f3OtnNetPortHistoryExtOduBBE = _F3OtnNetPortHistoryExtOduBBE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 12),
    _F3OtnNetPortHistoryExtOduBBE_Type()
)
f3OtnNetPortHistoryExtOduBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortHistoryExtOduBBE.setStatus("current")
_F3OtnNetPortHistoryExtOduUAS_Type = Integer32
_F3OtnNetPortHistoryExtOduUAS_Object = MibTableColumn
f3OtnNetPortHistoryExtOduUAS = _F3OtnNetPortHistoryExtOduUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 13),
    _F3OtnNetPortHistoryExtOduUAS_Type()
)
f3OtnNetPortHistoryExtOduUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OtnNetPortHistoryExtOduUAS.setStatus("current")
_F3OtnConformance_ObjectIdentity = ObjectIdentity
f3OtnConformance = _F3OtnConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 3)
)
_F3OtnCompliances_ObjectIdentity = ObjectIdentity
f3OtnCompliances = _F3OtnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 3, 1)
)
_F3OtnGroups_ObjectIdentity = ObjectIdentity
f3OtnGroups = _F3OtnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 3, 2)
)
cmEthernetNetPortEntry.registerAugmentions(
    ("F3-OTN-MIB",
     "f3OtnNetPortEntry")
)
f3OtnNetPortEntry.setIndexNames(*cmEthernetNetPortEntry.getIndexNames())
cmEthernetNetPortStatsEntry.registerAugmentions(
    ("F3-OTN-MIB",
     "f3OtnNetPortStatsExtEntry")
)
f3OtnNetPortStatsExtEntry.setIndexNames(*cmEthernetNetPortStatsEntry.getIndexNames())
cmEthernetNetPortHistoryEntry.registerAugmentions(
    ("F3-OTN-MIB",
     "f3OtnNetPortHistoryExtEntry")
)
f3OtnNetPortHistoryExtEntry.setIndexNames(*cmEthernetNetPortHistoryEntry.getIndexNames())

# Managed Objects groups

f3OtnConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 3, 2, 1)
)
f3OtnConfigGroup.setObjects(
      *(("F3-OTN-MIB", "f3OtnNetPortPayloadType"),
        ("F3-OTN-MIB", "f3OtnNetPortFacilityType"),
        ("F3-OTN-MIB", "f3OtnNetPortFec"),
        ("F3-OTN-MIB", "f3OtnNetPortTimDetectModeOtu"),
        ("F3-OTN-MIB", "f3OtnNetPortTimAisInsertOtuEnabled"),
        ("F3-OTN-MIB", "f3OtnNetPortTtiActualRxHexOtu"),
        ("F3-OTN-MIB", "f3OtnNetPortTtiSapiActualRxOtu"),
        ("F3-OTN-MIB", "f3OtnNetPortTtiDapiActualRxOtu"),
        ("F3-OTN-MIB", "f3OtnNetPortTtiOpSpActualRxOtu"),
        ("F3-OTN-MIB", "f3OtnNetPortTtiSapiExpectedRxOtu"),
        ("F3-OTN-MIB", "f3OtnNetPortTtiSapiTxOtu"),
        ("F3-OTN-MIB", "f3OtnNetPortTtiDapiTxOtu"),
        ("F3-OTN-MIB", "f3OtnNetPortTtiOpSpTxOtu"),
        ("F3-OTN-MIB", "f3OtnNetPortTimDetectModeOdu"),
        ("F3-OTN-MIB", "f3OtnNetPortTimAisInsertOduEnabled"),
        ("F3-OTN-MIB", "f3OtnNetPortTtiActualRxHexOdu"),
        ("F3-OTN-MIB", "f3OtnNetPortTtiSapiActualRxOdu"),
        ("F3-OTN-MIB", "f3OtnNetPortTtiDapiActualRxOdu"),
        ("F3-OTN-MIB", "f3OtnNetPortTtiOpSpActualRxOdu"),
        ("F3-OTN-MIB", "f3OtnNetPortTtiSapiExpectedRxOdu"),
        ("F3-OTN-MIB", "f3OtnNetPortTtiSapiTxOdu"),
        ("F3-OTN-MIB", "f3OtnNetPortTtiDapiTxOdu"),
        ("F3-OTN-MIB", "f3OtnNetPortTtiOpSpTxOdu"))
)
if mibBuilder.loadTexts:
    f3OtnConfigGroup.setStatus("current")

f3OtnPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 3, 2, 2)
)
f3OtnPerfGroup.setObjects(
      *(("F3-OTN-MIB", "f3OtnNetPortStatsExtBerBeforeCorr"),
        ("F3-OTN-MIB", "f3OtnNetPortStatsExtFecErrSec"),
        ("F3-OTN-MIB", "f3OtnNetPortStatsExtFecSES"),
        ("F3-OTN-MIB", "f3OtnNetPortStatsExtFecCorrErr"),
        ("F3-OTN-MIB", "f3OtnNetPortStatsExtFecUncorrBlockErr"),
        ("F3-OTN-MIB", "f3OtnNetPortStatsExtOtuErrSec"),
        ("F3-OTN-MIB", "f3OtnNetPortStatsExtOtuSES"),
        ("F3-OTN-MIB", "f3OtnNetPortStatsExtOtuBBE"),
        ("F3-OTN-MIB", "f3OtnNetPortStatsExtOtuUAS"),
        ("F3-OTN-MIB", "f3OtnNetPortStatsExtOduErrSec"),
        ("F3-OTN-MIB", "f3OtnNetPortStatsExtOduSES"),
        ("F3-OTN-MIB", "f3OtnNetPortStatsExtOduBBE"),
        ("F3-OTN-MIB", "f3OtnNetPortStatsExtOduUAS"),
        ("F3-OTN-MIB", "f3OtnNetPortHistoryExtBerBeforeCorr"),
        ("F3-OTN-MIB", "f3OtnNetPortHistoryExtFecErrSec"),
        ("F3-OTN-MIB", "f3OtnNetPortHistoryExtFecSES"),
        ("F3-OTN-MIB", "f3OtnNetPortHistoryExtFecCorrErr"),
        ("F3-OTN-MIB", "f3OtnNetPortHistoryExtFecUncorrBlockErr"),
        ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOtuErrSec"),
        ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOtuSES"),
        ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOtuBBE"),
        ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOtuUAS"),
        ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOduErrSec"),
        ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOduSES"),
        ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOduBBE"),
        ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOduUAS"))
)
if mibBuilder.loadTexts:
    f3OtnPerfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f3OtnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 3, 1, 1)
)
f3OtnCompliance.setObjects(
      *(("F3-OTN-MIB", "f3OtnConfigGroup"),
        ("F3-OTN-MIB", "f3OtnPerfGroup"))
)
if mibBuilder.loadTexts:
    f3OtnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-OTN-MIB",
    **{"OtnFacilityType": OtnFacilityType,
       "OtnFecType": OtnFecType,
       "TimDetectMode": TimDetectMode,
       "f3OtnMIB": f3OtnMIB,
       "f3OtnConfigObjects": f3OtnConfigObjects,
       "f3OtnNetPortExtTable": f3OtnNetPortExtTable,
       "f3OtnNetPortEntry": f3OtnNetPortEntry,
       "f3OtnNetPortPayloadType": f3OtnNetPortPayloadType,
       "f3OtnNetPortFacilityType": f3OtnNetPortFacilityType,
       "f3OtnNetPortFec": f3OtnNetPortFec,
       "f3OtnNetPortTimDetectModeOtu": f3OtnNetPortTimDetectModeOtu,
       "f3OtnNetPortTimAisInsertOtuEnabled": f3OtnNetPortTimAisInsertOtuEnabled,
       "f3OtnNetPortTtiActualRxHexOtu": f3OtnNetPortTtiActualRxHexOtu,
       "f3OtnNetPortTtiSapiActualRxOtu": f3OtnNetPortTtiSapiActualRxOtu,
       "f3OtnNetPortTtiDapiActualRxOtu": f3OtnNetPortTtiDapiActualRxOtu,
       "f3OtnNetPortTtiOpSpActualRxOtu": f3OtnNetPortTtiOpSpActualRxOtu,
       "f3OtnNetPortTtiSapiExpectedRxOtu": f3OtnNetPortTtiSapiExpectedRxOtu,
       "f3OtnNetPortTtiSapiTxOtu": f3OtnNetPortTtiSapiTxOtu,
       "f3OtnNetPortTtiDapiTxOtu": f3OtnNetPortTtiDapiTxOtu,
       "f3OtnNetPortTtiOpSpTxOtu": f3OtnNetPortTtiOpSpTxOtu,
       "f3OtnNetPortTimDetectModeOdu": f3OtnNetPortTimDetectModeOdu,
       "f3OtnNetPortTimAisInsertOduEnabled": f3OtnNetPortTimAisInsertOduEnabled,
       "f3OtnNetPortTtiActualRxHexOdu": f3OtnNetPortTtiActualRxHexOdu,
       "f3OtnNetPortTtiSapiActualRxOdu": f3OtnNetPortTtiSapiActualRxOdu,
       "f3OtnNetPortTtiDapiActualRxOdu": f3OtnNetPortTtiDapiActualRxOdu,
       "f3OtnNetPortTtiOpSpActualRxOdu": f3OtnNetPortTtiOpSpActualRxOdu,
       "f3OtnNetPortTtiSapiExpectedRxOdu": f3OtnNetPortTtiSapiExpectedRxOdu,
       "f3OtnNetPortTtiSapiTxOdu": f3OtnNetPortTtiSapiTxOdu,
       "f3OtnNetPortTtiDapiTxOdu": f3OtnNetPortTtiDapiTxOdu,
       "f3OtnNetPortTtiOpSpTxOdu": f3OtnNetPortTtiOpSpTxOdu,
       "f3OtnPerfObjects": f3OtnPerfObjects,
       "f3OtnNetPortStatsExtTable": f3OtnNetPortStatsExtTable,
       "f3OtnNetPortStatsExtEntry": f3OtnNetPortStatsExtEntry,
       "f3OtnNetPortStatsExtBerBeforeCorr": f3OtnNetPortStatsExtBerBeforeCorr,
       "f3OtnNetPortStatsExtFecErrSec": f3OtnNetPortStatsExtFecErrSec,
       "f3OtnNetPortStatsExtFecSES": f3OtnNetPortStatsExtFecSES,
       "f3OtnNetPortStatsExtFecCorrErr": f3OtnNetPortStatsExtFecCorrErr,
       "f3OtnNetPortStatsExtFecUncorrBlockErr": f3OtnNetPortStatsExtFecUncorrBlockErr,
       "f3OtnNetPortStatsExtOtuErrSec": f3OtnNetPortStatsExtOtuErrSec,
       "f3OtnNetPortStatsExtOtuSES": f3OtnNetPortStatsExtOtuSES,
       "f3OtnNetPortStatsExtOtuBBE": f3OtnNetPortStatsExtOtuBBE,
       "f3OtnNetPortStatsExtOtuUAS": f3OtnNetPortStatsExtOtuUAS,
       "f3OtnNetPortStatsExtOduErrSec": f3OtnNetPortStatsExtOduErrSec,
       "f3OtnNetPortStatsExtOduSES": f3OtnNetPortStatsExtOduSES,
       "f3OtnNetPortStatsExtOduBBE": f3OtnNetPortStatsExtOduBBE,
       "f3OtnNetPortStatsExtOduUAS": f3OtnNetPortStatsExtOduUAS,
       "f3OtnNetPortHistoryExtTable": f3OtnNetPortHistoryExtTable,
       "f3OtnNetPortHistoryExtEntry": f3OtnNetPortHistoryExtEntry,
       "f3OtnNetPortHistoryExtBerBeforeCorr": f3OtnNetPortHistoryExtBerBeforeCorr,
       "f3OtnNetPortHistoryExtFecErrSec": f3OtnNetPortHistoryExtFecErrSec,
       "f3OtnNetPortHistoryExtFecSES": f3OtnNetPortHistoryExtFecSES,
       "f3OtnNetPortHistoryExtFecCorrErr": f3OtnNetPortHistoryExtFecCorrErr,
       "f3OtnNetPortHistoryExtFecUncorrBlockErr": f3OtnNetPortHistoryExtFecUncorrBlockErr,
       "f3OtnNetPortHistoryExtOtuErrSec": f3OtnNetPortHistoryExtOtuErrSec,
       "f3OtnNetPortHistoryExtOtuSES": f3OtnNetPortHistoryExtOtuSES,
       "f3OtnNetPortHistoryExtOtuBBE": f3OtnNetPortHistoryExtOtuBBE,
       "f3OtnNetPortHistoryExtOtuUAS": f3OtnNetPortHistoryExtOtuUAS,
       "f3OtnNetPortHistoryExtOduErrSec": f3OtnNetPortHistoryExtOduErrSec,
       "f3OtnNetPortHistoryExtOduSES": f3OtnNetPortHistoryExtOduSES,
       "f3OtnNetPortHistoryExtOduBBE": f3OtnNetPortHistoryExtOduBBE,
       "f3OtnNetPortHistoryExtOduUAS": f3OtnNetPortHistoryExtOduUAS,
       "f3OtnConformance": f3OtnConformance,
       "f3OtnCompliances": f3OtnCompliances,
       "f3OtnCompliance": f3OtnCompliance,
       "f3OtnGroups": f3OtnGroups,
       "f3OtnConfigGroup": f3OtnConfigGroup,
       "f3OtnPerfGroup": f3OtnPerfGroup}
)
