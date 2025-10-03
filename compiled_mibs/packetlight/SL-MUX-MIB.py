# SNMP MIB module (SL-MUX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-MUX-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:55 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(CleiCode,) = mibBuilder.importSymbols(
    "SL-ENTITY-MIB",
    "CleiCode")

(sitelight,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "sitelight")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

slMux = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MuxIfTable_Object = MibTable
muxIfTable = _MuxIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 5, 1)
)
if mibBuilder.loadTexts:
    muxIfTable.setStatus("current")
_MuxIfEntry_Object = MibTableRow
muxIfEntry = _MuxIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 5, 1, 1)
)
muxIfEntry.setIndexNames(
    (0, "SL-MUX-MIB", "muxIfIndex"),
)
if mibBuilder.loadTexts:
    muxIfEntry.setStatus("current")
_MuxIfIndex_Type = InterfaceIndex
_MuxIfIndex_Object = MibTableColumn
muxIfIndex = _MuxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 5, 1, 1, 1),
    _MuxIfIndex_Type()
)
muxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfIndex.setStatus("current")
_MuxIfType_Type = Integer32
_MuxIfType_Object = MibTableColumn
muxIfType = _MuxIfType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 5, 1, 1, 2),
    _MuxIfType_Type()
)
muxIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfType.setStatus("current")


class _MuxIfWaveSpacing_Type(Integer32):
    """Custom type muxIfWaveSpacing based on Integer32"""
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
        *(("ghzNone", 0),
          ("ghz400", 1),
          ("ghz200", 2),
          ("ghz100", 3),
          ("ghz50", 4),
          ("ghz2500", 5))
    )


_MuxIfWaveSpacing_Type.__name__ = "Integer32"
_MuxIfWaveSpacing_Object = MibTableColumn
muxIfWaveSpacing = _MuxIfWaveSpacing_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 5, 1, 1, 3),
    _MuxIfWaveSpacing_Type()
)
muxIfWaveSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfWaveSpacing.setStatus("current")
_MuxIfWaveLengthNm_Type = Integer32
_MuxIfWaveLengthNm_Object = MibTableColumn
muxIfWaveLengthNm = _MuxIfWaveLengthNm_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 5, 1, 1, 4),
    _MuxIfWaveLengthNm_Type()
)
muxIfWaveLengthNm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfWaveLengthNm.setStatus("current")
_MuxIfOscWaveLengthNm_Type = Integer32
_MuxIfOscWaveLengthNm_Object = MibTableColumn
muxIfOscWaveLengthNm = _MuxIfOscWaveLengthNm_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 5, 1, 1, 5),
    _MuxIfOscWaveLengthNm_Type()
)
muxIfOscWaveLengthNm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxIfOscWaveLengthNm.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-MUX-MIB",
    **{"slMux": slMux,
       "muxIfTable": muxIfTable,
       "muxIfEntry": muxIfEntry,
       "muxIfIndex": muxIfIndex,
       "muxIfType": muxIfType,
       "muxIfWaveSpacing": muxIfWaveSpacing,
       "muxIfWaveLengthNm": muxIfWaveLengthNm,
       "muxIfOscWaveLengthNm": muxIfOscWaveLengthNm}
)
