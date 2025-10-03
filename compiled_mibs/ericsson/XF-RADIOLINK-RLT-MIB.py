# SNMP MIB module (XF-RADIOLINK-RLT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ericsson\XF-RADIOLINK-RLT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:50 2025
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

(entLogicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entLogicalIndex",
    "entPhysicalIndex")

(HCPerfCurrentCount,) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfCurrentCount")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(xfRadioLink,) = mibBuilder.importSymbols(
    "XF-TOP-MIB",
    "xfRadioLink")


# MODULE-IDENTITY

xfRadioLinkRltMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5)
)
if mibBuilder.loadTexts:
    xfRadioLinkRltMIB.setRevisions(
        ("2020-11-05 00:00",
         "2020-09-17 00:00",
         "2020-06-10 00:00",
         "2020-06-03 00:00",
         "2020-05-28 00:00",
         "2020-04-30 00:00",
         "2020-03-04 00:00",
         "2019-10-14 00:00",
         "2019-10-09 00:00",
         "2019-07-18 00:00",
         "2019-06-07 00:00",
         "2019-03-26 00:00",
         "2019-03-25 00:00",
         "2019-02-28 00:00",
         "2019-02-20 00:00",
         "2019-01-30 00:00",
         "2019-01-11 00:00",
         "2018-11-24 00:00",
         "2018-10-24 00:00",
         "2018-10-03 00:00",
         "2018-09-17 00:00",
         "2018-08-27 00:00",
         "2018-08-16 00:00",
         "2018-07-09 00:00",
         "2018-04-13 00:00",
         "2018-04-09 00:00",
         "2018-03-23 00:00",
         "2018-03-13 00:00",
         "2018-01-30 00:00",
         "2017-12-27 00:00",
         "2017-09-19 00:00",
         "2017-08-03 00:00",
         "2017-05-03 00:00",
         "2017-02-01 00:00",
         "2017-01-30 00:00",
         "2016-11-04 00:00",
         "2016-09-29 00:00",
         "2016-09-08 00:00",
         "2016-07-18 00:00",
         "2016-06-10 00:00",
         "2016-06-06 00:00",
         "2016-06-01 00:00",
         "2016-05-02 00:00",
         "2016-04-29 00:00",
         "2016-04-12 00:00",
         "2016-03-01 00:00",
         "2016-02-22 00:00",
         "2016-02-05 00:00",
         "2015-11-25 00:00",
         "2015-11-16 00:00",
         "2015-11-10 00:00",
         "2015-11-05 00:00",
         "2015-09-16 00:00",
         "2015-08-27 00:00",
         "2015-08-20 00:00",
         "2015-07-07 00:00",
         "2015-06-30 00:00",
         "2015-06-04 00:00",
         "2015-06-03 00:00",
         "2015-05-11 00:00",
         "2015-05-08 00:00",
         "2015-05-06 00:00",
         "2015-04-20 00:00",
         "2015-04-13 00:00",
         "2015-03-30 00:00",
         "2015-03-19 00:00",
         "2015-03-11 00:00",
         "2015-03-09 00:00",
         "2015-03-06 00:00",
         "2015-03-05 00:00",
         "2015-02-25 00:00",
         "2015-02-18 00:00",
         "2015-02-10 00:00",
         "2015-01-29 00:00",
         "2014-12-12 00:00",
         "2014-12-10 00:00",
         "2014-12-02 00:00",
         "2014-12-01 00:00",
         "2014-11-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CarrierTermACMIndex(TextualConvention, Integer32):
    status = "current"
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
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("acm4QAMStrong", 1),
          ("acm4QAMStd", 2),
          ("acm4QAMLight", 3),
          ("acm16QAMStrong", 4),
          ("acm16QAMStd", 5),
          ("acm16QAMLight", 6),
          ("acm32QAMStrong", 7),
          ("acm32QAMStd", 8),
          ("acm32QAMLight", 9),
          ("acm64QAMStrong", 10),
          ("acm64QAMStd", 11),
          ("acm64QAMLight", 12),
          ("acm128QAMStrong", 13),
          ("acm128QAMStd", 14),
          ("acm128QAMLight", 15),
          ("acm256QAMStrong", 16),
          ("acm256QAMStd", 17),
          ("acm256QAMLight", 18),
          ("acm512QAMStrong", 19),
          ("acm512QAMStd", 20),
          ("acm512QAMLight", 21),
          ("acm1024QAMStrong", 22),
          ("acm1024QAMStd", 23),
          ("acm1024QAMLight", 24),
          ("acm2048QAMStrong", 25),
          ("acm2048QAMStd", 26),
          ("acm2048QAMLight", 27),
          ("acm4096QAMStrong", 28),
          ("acm4096QAMStd", 29),
          ("acm4096QAMLight", 30),
          ("acm8192QAMStrong", 31),
          ("acm8192QAMStd", 32),
          ("acm8192QAMLight", 33),
          ("acm16384QAMStrong", 34),
          ("acm16384QAMStd", 35),
          ("acm16384QAMLight", 36))
    )



# MIB Managed Objects in the order of their OIDs

_XfRadioLinkRltObjects_ObjectIdentity = ObjectIdentity
xfRadioLinkRltObjects = _XfRadioLinkRltObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1)
)
_XfChannelGroupTable_Object = MibTable
xfChannelGroupTable = _XfChannelGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 1)
)
if mibBuilder.loadTexts:
    xfChannelGroupTable.setStatus("current")
_XfChannelGroupEntry_Object = MibTableRow
xfChannelGroupEntry = _XfChannelGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 1, 1)
)
xfChannelGroupEntry.setIndexNames(
    (0, "XF-RADIOLINK-RLT-MIB", "cgIfIndex"),
    (0, "XF-RADIOLINK-RLT-MIB", "cgTypeIndex"),
)
if mibBuilder.loadTexts:
    xfChannelGroupEntry.setStatus("current")


class _CgIfIndex_Type(Integer32):
    """Custom type cgIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CgIfIndex_Type.__name__ = "Integer32"
_CgIfIndex_Object = MibTableColumn
cgIfIndex = _CgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 1, 1, 1),
    _CgIfIndex_Type()
)
cgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgIfIndex.setStatus("current")


class _CgTypeIndex_Type(Integer32):
    """Custom type cgTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("bonding", 2),
          ("rlp", 3))
    )


_CgTypeIndex_Type.__name__ = "Integer32"
_CgTypeIndex_Object = MibTableColumn
cgTypeIndex = _CgTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 1, 1, 2),
    _CgTypeIndex_Type()
)
cgTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgTypeIndex.setStatus("current")


class _XfIfStatus_Type(Integer32):
    """Custom type xfIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ready", 2),
          ("notReady", 3))
    )


_XfIfStatus_Type.__name__ = "Integer32"
_XfIfStatus_Object = MibTableColumn
xfIfStatus = _XfIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 1, 1, 3),
    _XfIfStatus_Type()
)
xfIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfIfStatus.setStatus("current")
_XfLIMappingTable_Object = MibTable
xfLIMappingTable = _XfLIMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 2)
)
if mibBuilder.loadTexts:
    xfLIMappingTable.setStatus("current")
_XfLIMappingEntry_Object = MibTableRow
xfLIMappingEntry = _XfLIMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 2, 1)
)
xfLIMappingEntry.setIndexNames(
    (0, "XF-RADIOLINK-RLT-MIB", "liEntLogicalIndex"),
    (0, "XF-RADIOLINK-RLT-MIB", "liIfIndex"),
)
if mibBuilder.loadTexts:
    xfLIMappingEntry.setStatus("current")


class _LiEntLogicalIndex_Type(Integer32):
    """Custom type liEntLogicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LiEntLogicalIndex_Type.__name__ = "Integer32"
_LiEntLogicalIndex_Object = MibTableColumn
liEntLogicalIndex = _LiEntLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 2, 1, 1),
    _LiEntLogicalIndex_Type()
)
liEntLogicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liEntLogicalIndex.setStatus("current")


class _LiIfIndex_Type(Integer32):
    """Custom type liIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LiIfIndex_Type.__name__ = "Integer32"
_LiIfIndex_Object = MibTableColumn
liIfIndex = _LiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 2, 1, 2),
    _LiIfIndex_Type()
)
liIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liIfIndex.setStatus("current")


class _XfLIName_Type(DisplayString):
    """Custom type xfLIName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XfLIName_Type.__name__ = "DisplayString"
_XfLIName_Object = MibTableColumn
xfLIName = _XfLIName_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 2, 1, 3),
    _XfLIName_Type()
)
xfLIName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfLIName.setStatus("current")


class _XfLIIfDescr_Type(DisplayString):
    """Custom type xfLIIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XfLIIfDescr_Type.__name__ = "DisplayString"
_XfLIIfDescr_Object = MibTableColumn
xfLIIfDescr = _XfLIIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 2, 1, 4),
    _XfLIIfDescr_Type()
)
xfLIIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfLIIfDescr.setStatus("current")
_XfCarrierTerminationTable_Object = MibTable
xfCarrierTerminationTable = _XfCarrierTerminationTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3)
)
if mibBuilder.loadTexts:
    xfCarrierTerminationTable.setStatus("current")
_XfCarrierTerminationEntry_Object = MibTableRow
xfCarrierTerminationEntry = _XfCarrierTerminationEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1)
)
xfCarrierTerminationEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLogicalIndex"),
)
if mibBuilder.loadTexts:
    xfCarrierTerminationEntry.setStatus("current")


class _XfCarrierTermDistinguishedName_Type(DisplayString):
    """Custom type xfCarrierTermDistinguishedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XfCarrierTermDistinguishedName_Type.__name__ = "DisplayString"
_XfCarrierTermDistinguishedName_Object = MibTableColumn
xfCarrierTermDistinguishedName = _XfCarrierTermDistinguishedName_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 1),
    _XfCarrierTermDistinguishedName_Type()
)
xfCarrierTermDistinguishedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfCarrierTermDistinguishedName.setStatus("current")


class _XfCarrierTermLabel_Type(DisplayString):
    """Custom type xfCarrierTermLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XfCarrierTermLabel_Type.__name__ = "DisplayString"
_XfCarrierTermLabel_Object = MibTableColumn
xfCarrierTermLabel = _XfCarrierTermLabel_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 2),
    _XfCarrierTermLabel_Type()
)
xfCarrierTermLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfCarrierTermLabel.setStatus("current")


class _XfCarrierTermOperStatus_Type(Integer32):
    """Custom type xfCarrierTermOperStatus based on Integer32"""
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
        *(("other", 1),
          ("down", 2),
          ("up", 3),
          ("degraded", 4),
          ("testing", 5))
    )


_XfCarrierTermOperStatus_Type.__name__ = "Integer32"
_XfCarrierTermOperStatus_Object = MibTableColumn
xfCarrierTermOperStatus = _XfCarrierTermOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 3),
    _XfCarrierTermOperStatus_Type()
)
xfCarrierTermOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfCarrierTermOperStatus.setStatus("current")
_XfCarrierTermRadioFrameId_Type = Integer32
_XfCarrierTermRadioFrameId_Object = MibTableColumn
xfCarrierTermRadioFrameId = _XfCarrierTermRadioFrameId_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 4),
    _XfCarrierTermRadioFrameId_Type()
)
xfCarrierTermRadioFrameId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfCarrierTermRadioFrameId.setStatus("current")


class _XfCarrierTermPreamble_Type(Integer32):
    """Custom type xfCarrierTermPreamble based on Integer32"""
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
        *(("notSpecified", 1),
          ("preambleA", 2),
          ("preambleB", 3),
          ("preambleC", 4),
          ("preambleD", 5))
    )


_XfCarrierTermPreamble_Type.__name__ = "Integer32"
_XfCarrierTermPreamble_Object = MibTableColumn
xfCarrierTermPreamble = _XfCarrierTermPreamble_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 5),
    _XfCarrierTermPreamble_Type()
)
xfCarrierTermPreamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfCarrierTermPreamble.setStatus("current")
_XfCarrierTermSelectedMinACM_Type = CarrierTermACMIndex
_XfCarrierTermSelectedMinACM_Object = MibTableColumn
xfCarrierTermSelectedMinACM = _XfCarrierTermSelectedMinACM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 6),
    _XfCarrierTermSelectedMinACM_Type()
)
xfCarrierTermSelectedMinACM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfCarrierTermSelectedMinACM.setStatus("current")
_XfCarrierTermActualACM_Type = CarrierTermACMIndex
_XfCarrierTermActualACM_Object = MibTableColumn
xfCarrierTermActualACM = _XfCarrierTermActualACM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 7),
    _XfCarrierTermActualACM_Type()
)
xfCarrierTermActualACM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfCarrierTermActualACM.setStatus("current")
_XfCarrierTermSelectedMaxACM_Type = CarrierTermACMIndex
_XfCarrierTermSelectedMaxACM_Object = MibTableColumn
xfCarrierTermSelectedMaxACM = _XfCarrierTermSelectedMaxACM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 8),
    _XfCarrierTermSelectedMaxACM_Type()
)
xfCarrierTermSelectedMaxACM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfCarrierTermSelectedMaxACM.setStatus("current")
_XfCarrierTermCapabilitiesLastChange_Type = TimeTicks
_XfCarrierTermCapabilitiesLastChange_Object = MibTableColumn
xfCarrierTermCapabilitiesLastChange = _XfCarrierTermCapabilitiesLastChange_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 9),
    _XfCarrierTermCapabilitiesLastChange_Type()
)
xfCarrierTermCapabilitiesLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfCarrierTermCapabilitiesLastChange.setStatus("current")


class _XfCarrierTermReferenceSEC_Type(Integer32):
    """Custom type xfCarrierTermReferenceSEC based on Integer32"""
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
        *(("notSpecified", 1),
          ("sec2", 2),
          ("sec4L", 3),
          ("sec4H", 4),
          ("sec5LB", 5),
          ("sec5HB", 6),
          ("sec6LB", 7),
          ("sec6HB", 8),
          ("sec7B", 9))
    )


_XfCarrierTermReferenceSEC_Type.__name__ = "Integer32"
_XfCarrierTermReferenceSEC_Object = MibTableColumn
xfCarrierTermReferenceSEC = _XfCarrierTermReferenceSEC_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 10),
    _XfCarrierTermReferenceSEC_Type()
)
xfCarrierTermReferenceSEC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfCarrierTermReferenceSEC.setStatus("current")


class _XfCarrierTermWantedLicensedCapacity_Type(Integer32):
    """Custom type xfCarrierTermWantedLicensedCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XfCarrierTermWantedLicensedCapacity_Type.__name__ = "Integer32"
_XfCarrierTermWantedLicensedCapacity_Object = MibTableColumn
xfCarrierTermWantedLicensedCapacity = _XfCarrierTermWantedLicensedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 11),
    _XfCarrierTermWantedLicensedCapacity_Type()
)
xfCarrierTermWantedLicensedCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfCarrierTermWantedLicensedCapacity.setStatus("current")


class _XfCarrierTermActualLicensedCapacity_Type(Integer32):
    """Custom type xfCarrierTermActualLicensedCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XfCarrierTermActualLicensedCapacity_Type.__name__ = "Integer32"
_XfCarrierTermActualLicensedCapacity_Object = MibTableColumn
xfCarrierTermActualLicensedCapacity = _XfCarrierTermActualLicensedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 12),
    _XfCarrierTermActualLicensedCapacity_Type()
)
xfCarrierTermActualLicensedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfCarrierTermActualLicensedCapacity.setStatus("current")


class _XfCarrierTermActualCapacity_Type(Integer32):
    """Custom type xfCarrierTermActualCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XfCarrierTermActualCapacity_Type.__name__ = "Integer32"
_XfCarrierTermActualCapacity_Object = MibTableColumn
xfCarrierTermActualCapacity = _XfCarrierTermActualCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 13),
    _XfCarrierTermActualCapacity_Type()
)
xfCarrierTermActualCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfCarrierTermActualCapacity.setStatus("current")


class _XfCarrierTermPolarization_Type(Integer32):
    """Custom type xfCarrierTermPolarization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSpecified", 1),
          ("horizontal", 2),
          ("vertical", 3))
    )


_XfCarrierTermPolarization_Type.__name__ = "Integer32"
_XfCarrierTermPolarization_Object = MibTableColumn
xfCarrierTermPolarization = _XfCarrierTermPolarization_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 14),
    _XfCarrierTermPolarization_Type()
)
xfCarrierTermPolarization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfCarrierTermPolarization.setStatus("current")


class _XfCarrierTermXPICOperStatus_Type(Integer32):
    """Custom type xfCarrierTermXPICOperStatus based on Integer32"""
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
        *(("other", 1),
          ("locked", 2),
          ("unlocked", 3),
          ("mute", 4),
          ("notApplicable", 5))
    )


_XfCarrierTermXPICOperStatus_Type.__name__ = "Integer32"
_XfCarrierTermXPICOperStatus_Object = MibTableColumn
xfCarrierTermXPICOperStatus = _XfCarrierTermXPICOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 15),
    _XfCarrierTermXPICOperStatus_Type()
)
xfCarrierTermXPICOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfCarrierTermXPICOperStatus.setStatus("current")


class _XfCarrierTermMIMOOperStatus_Type(Integer32):
    """Custom type xfCarrierTermMIMOOperStatus based on Integer32"""
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
        *(("other", 1),
          ("locked", 2),
          ("unlocked", 3),
          ("mute", 4),
          ("notApplicable", 5))
    )


_XfCarrierTermMIMOOperStatus_Type.__name__ = "Integer32"
_XfCarrierTermMIMOOperStatus_Object = MibTableColumn
xfCarrierTermMIMOOperStatus = _XfCarrierTermMIMOOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 16),
    _XfCarrierTermMIMOOperStatus_Type()
)
xfCarrierTermMIMOOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfCarrierTermMIMOOperStatus.setStatus("current")
_XfCarrierTermSNIR_Type = Integer32
_XfCarrierTermSNIR_Object = MibTableColumn
xfCarrierTermSNIR = _XfCarrierTermSNIR_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 17),
    _XfCarrierTermSNIR_Type()
)
xfCarrierTermSNIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfCarrierTermSNIR.setStatus("current")
_XfCarrierTermXPI_Type = Integer32
_XfCarrierTermXPI_Object = MibTableColumn
xfCarrierTermXPI = _XfCarrierTermXPI_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 18),
    _XfCarrierTermXPI_Type()
)
xfCarrierTermXPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfCarrierTermXPI.setStatus("current")


class _XfCarrierTermReset_Type(Integer32):
    """Custom type xfCarrierTermReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("noReset", 2),
          ("reset", 3))
    )


_XfCarrierTermReset_Type.__name__ = "Integer32"
_XfCarrierTermReset_Object = MibTableColumn
xfCarrierTermReset = _XfCarrierTermReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 19),
    _XfCarrierTermReset_Type()
)
xfCarrierTermReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfCarrierTermReset.setStatus("current")


class _XfCarrierTermRestore_Type(Integer32):
    """Custom type xfCarrierTermRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("noRestore", 2),
          ("restore", 3))
    )


_XfCarrierTermRestore_Type.__name__ = "Integer32"
_XfCarrierTermRestore_Object = MibTableColumn
xfCarrierTermRestore = _XfCarrierTermRestore_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 20),
    _XfCarrierTermRestore_Type()
)
xfCarrierTermRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfCarrierTermRestore.setStatus("current")


class _XfCarrierTermAutoRemoveLoopEnable_Type(Integer32):
    """Custom type xfCarrierTermAutoRemoveLoopEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_XfCarrierTermAutoRemoveLoopEnable_Type.__name__ = "Integer32"
_XfCarrierTermAutoRemoveLoopEnable_Object = MibTableColumn
xfCarrierTermAutoRemoveLoopEnable = _XfCarrierTermAutoRemoveLoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 21),
    _XfCarrierTermAutoRemoveLoopEnable_Type()
)
xfCarrierTermAutoRemoveLoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfCarrierTermAutoRemoveLoopEnable.setStatus("current")


class _XfCarrierTermBerAlarmThreshold_Type(Integer32):
    """Custom type xfCarrierTermBerAlarmThreshold based on Integer32"""
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
        *(("other", 1),
          ("ber1e3", 2),
          ("ber1e4", 3),
          ("ber1e5", 4),
          ("ber1e6", 5))
    )


_XfCarrierTermBerAlarmThreshold_Type.__name__ = "Integer32"
_XfCarrierTermBerAlarmThreshold_Object = MibTableColumn
xfCarrierTermBerAlarmThreshold = _XfCarrierTermBerAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 22),
    _XfCarrierTermBerAlarmThreshold_Type()
)
xfCarrierTermBerAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfCarrierTermBerAlarmThreshold.setStatus("current")
_XfCarrierTermActualRxACM_Type = CarrierTermACMIndex
_XfCarrierTermActualRxACM_Object = MibTableColumn
xfCarrierTermActualRxACM = _XfCarrierTermActualRxACM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 23),
    _XfCarrierTermActualRxACM_Type()
)
xfCarrierTermActualRxACM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfCarrierTermActualRxACM.setStatus("current")


class _XfCarrierTermFeCTSeverity_Type(Bits):
    """Custom type xfCarrierTermFeCTSeverity based on Bits"""
    namedValues = NamedValues(
        *(("feCtSeverity0", 0),
          ("feCtSeverity1", 1),
          ("feCtSeverity2", 2))
    )

_XfCarrierTermFeCTSeverity_Type.__name__ = "Bits"
_XfCarrierTermFeCTSeverity_Object = MibTableColumn
xfCarrierTermFeCTSeverity = _XfCarrierTermFeCTSeverity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 3, 1, 24),
    _XfCarrierTermFeCTSeverity_Type()
)
xfCarrierTermFeCTSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfCarrierTermFeCTSeverity.setStatus("current")
_XfCarrierTerminationCapabilityTable_Object = MibTable
xfCarrierTerminationCapabilityTable = _XfCarrierTerminationCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 4)
)
if mibBuilder.loadTexts:
    xfCarrierTerminationCapabilityTable.setStatus("current")
_XfCarrierTerminationCapabilityEntry_Object = MibTableRow
xfCarrierTerminationCapabilityEntry = _XfCarrierTerminationCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 4, 1)
)
xfCarrierTerminationCapabilityEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLogicalIndex"),
    (0, "XF-RADIOLINK-RLT-MIB", "xfRadioFrameId"),
)
if mibBuilder.loadTexts:
    xfCarrierTerminationCapabilityEntry.setStatus("current")


class _XfRadioFrameId_Type(Integer32):
    """Custom type xfRadioFrameId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_XfRadioFrameId_Type.__name__ = "Integer32"
_XfRadioFrameId_Object = MibTableColumn
xfRadioFrameId = _XfRadioFrameId_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 4, 1, 1),
    _XfRadioFrameId_Type()
)
xfRadioFrameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRadioFrameId.setStatus("current")


class _XfChannelSpacing_Type(Integer32):
    """Custom type xfChannelSpacing based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("chspOther", 1),
          ("chsp3500kHz", 2),
          ("chsp7MHz", 3),
          ("chsp10MHz", 4),
          ("chsp14MHz", 5),
          ("chsp20MHz", 6),
          ("chsp28MHz", 7),
          ("chsp30MHz", 8),
          ("chsp40MHz", 9),
          ("chsp50MHz", 10),
          ("chsp56MHz", 11),
          ("chsp60MHz", 12),
          ("chsp80MHz", 13),
          ("chsp112MHz", 14))
    )


_XfChannelSpacing_Type.__name__ = "Integer32"
_XfChannelSpacing_Object = MibTableColumn
xfChannelSpacing = _XfChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 4, 1, 2),
    _XfChannelSpacing_Type()
)
xfChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfChannelSpacing.setStatus("current")


class _XfFrameFormatType_Type(Integer32):
    """Custom type xfFrameFormatType based on Integer32"""
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("standard", 2),
          ("xpic", 3),
          ("mimo", 4),
          ("longHaulStandard", 5),
          ("longHaulXpic", 6),
          ("xpic2boards", 7),
          ("longHaulXpic2boards", 8),
          ("mimo2boards", 9),
          ("sisoCA", 10),
          ("xpicCA", 11))
    )


_XfFrameFormatType_Type.__name__ = "Integer32"
_XfFrameFormatType_Object = MibTableColumn
xfFrameFormatType = _XfFrameFormatType_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 4, 1, 3),
    _XfFrameFormatType_Type()
)
xfFrameFormatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfFrameFormatType.setStatus("current")


class _XfMinACMCapacity_Type(Integer32):
    """Custom type xfMinACMCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_XfMinACMCapacity_Type.__name__ = "Integer32"
_XfMinACMCapacity_Object = MibTableColumn
xfMinACMCapacity = _XfMinACMCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 4, 1, 4),
    _XfMinACMCapacity_Type()
)
xfMinACMCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMinACMCapacity.setStatus("current")


class _XfMaxACMCapacity_Type(Integer32):
    """Custom type xfMaxACMCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_XfMaxACMCapacity_Type.__name__ = "Integer32"
_XfMaxACMCapacity_Object = MibTableColumn
xfMaxACMCapacity = _XfMaxACMCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 4, 1, 5),
    _XfMaxACMCapacity_Type()
)
xfMaxACMCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMaxACMCapacity.setStatus("current")


class _XfACMProfile_Type(Bits):
    """Custom type xfACMProfile based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("qam4Strong", 1),
          ("qam4Std", 2),
          ("qam4Light", 3),
          ("qam16Strong", 4),
          ("qam16Std", 5),
          ("qam16Light", 6),
          ("qam32Strong", 7),
          ("qam32Std", 8),
          ("qam32Light", 9),
          ("qam64Strong", 10),
          ("qam64Std", 11),
          ("qam64Light", 12),
          ("qam128Strong", 13),
          ("qam128Std", 14),
          ("qam128Light", 15),
          ("qam256Strong", 16),
          ("qam256Std", 17),
          ("qam256Light", 18),
          ("qam512Strong", 19),
          ("qam512Std", 20),
          ("qam512Light", 21),
          ("qam1024Strong", 22),
          ("qam1024Std", 23),
          ("qam1024Light", 24),
          ("qam2048Strong", 25),
          ("qam2048Std", 26),
          ("qam2048Light", 27),
          ("qam4096Strong", 28),
          ("qam4096Std", 29),
          ("qam4096Light", 30),
          ("qam8192Strong", 31),
          ("qam8192Std", 32),
          ("qam8192Light", 33),
          ("qam16384Strong", 34),
          ("qam16384Std", 35),
          ("qam16384Light", 36))
    )

_XfACMProfile_Type.__name__ = "Bits"
_XfACMProfile_Object = MibTableColumn
xfACMProfile = _XfACMProfile_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 4, 1, 6),
    _XfACMProfile_Type()
)
xfACMProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfACMProfile.setStatus("current")
_XfACMProfileCapacityTable_Object = MibTable
xfACMProfileCapacityTable = _XfACMProfileCapacityTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 5)
)
if mibBuilder.loadTexts:
    xfACMProfileCapacityTable.setStatus("current")
_XfACMProfileCapacityEntry_Object = MibTableRow
xfACMProfileCapacityEntry = _XfACMProfileCapacityEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 5, 1)
)
xfACMProfileCapacityEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLogicalIndex"),
    (0, "XF-RADIOLINK-RLT-MIB", "xfACMIndex"),
)
if mibBuilder.loadTexts:
    xfACMProfileCapacityEntry.setStatus("current")
_XfACMIndex_Type = CarrierTermACMIndex
_XfACMIndex_Object = MibTableColumn
xfACMIndex = _XfACMIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 5, 1, 1),
    _XfACMIndex_Type()
)
xfACMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfACMIndex.setStatus("current")


class _XfACMCapacity_Type(Integer32):
    """Custom type xfACMCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XfACMCapacity_Type.__name__ = "Integer32"
_XfACMCapacity_Object = MibTableColumn
xfACMCapacity = _XfACMCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 5, 1, 2),
    _XfACMCapacity_Type()
)
xfACMCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfACMCapacity.setStatus("current")
_XfRLTTable_Object = MibTable
xfRLTTable = _XfRLTTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6)
)
if mibBuilder.loadTexts:
    xfRLTTable.setStatus("current")
_XfRLTEntry_Object = MibTableRow
xfRLTEntry = _XfRLTEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1)
)
xfRLTEntry.setIndexNames(
    (0, "XF-RADIOLINK-RLT-MIB", "rltEntLogicalIndex"),
)
if mibBuilder.loadTexts:
    xfRLTEntry.setStatus("current")


class _RltEntLogicalIndex_Type(Integer32):
    """Custom type rltEntLogicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RltEntLogicalIndex_Type.__name__ = "Integer32"
_RltEntLogicalIndex_Object = MibTableColumn
rltEntLogicalIndex = _RltEntLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 1),
    _RltEntLogicalIndex_Type()
)
rltEntLogicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rltEntLogicalIndex.setStatus("current")


class _XfRLTDistinguishedName_Type(DisplayString):
    """Custom type xfRLTDistinguishedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XfRLTDistinguishedName_Type.__name__ = "DisplayString"
_XfRLTDistinguishedName_Object = MibTableColumn
xfRLTDistinguishedName = _XfRLTDistinguishedName_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 2),
    _XfRLTDistinguishedName_Type()
)
xfRLTDistinguishedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTDistinguishedName.setStatus("current")
_XfRLTIpAddress_Type = IpAddress
_XfRLTIpAddress_Object = MibTableColumn
xfRLTIpAddress = _XfRLTIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 3),
    _XfRLTIpAddress_Type()
)
xfRLTIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTIpAddress.setStatus("current")
_XfRLTIPv6Address_Type = InetAddressIPv6
_XfRLTIPv6Address_Object = MibTableColumn
xfRLTIPv6Address = _XfRLTIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 4),
    _XfRLTIPv6Address_Type()
)
xfRLTIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTIPv6Address.setStatus("current")


class _XfRLTNeName_Type(DisplayString):
    """Custom type xfRLTNeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XfRLTNeName_Type.__name__ = "DisplayString"
_XfRLTNeName_Object = MibTableColumn
xfRLTNeName = _XfRLTNeName_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 5),
    _XfRLTNeName_Type()
)
xfRLTNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTNeName.setStatus("current")


class _XfRLTNeType_Type(DisplayString):
    """Custom type xfRLTNeType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XfRLTNeType_Type.__name__ = "DisplayString"
_XfRLTNeType_Object = MibTableColumn
xfRLTNeType = _XfRLTNeType_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 6),
    _XfRLTNeType_Type()
)
xfRLTNeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTNeType.setStatus("current")


class _XfRLTId_Type(DisplayString):
    """Custom type xfRLTId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XfRLTId_Type.__name__ = "DisplayString"
_XfRLTId_Object = MibTableColumn
xfRLTId = _XfRLTId_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 7),
    _XfRLTId_Type()
)
xfRLTId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLTId.setStatus("current")


class _XfRLTExpectedFarEndId_Type(DisplayString):
    """Custom type xfRLTExpectedFarEndId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XfRLTExpectedFarEndId_Type.__name__ = "DisplayString"
_XfRLTExpectedFarEndId_Object = MibTableColumn
xfRLTExpectedFarEndId = _XfRLTExpectedFarEndId_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 8),
    _XfRLTExpectedFarEndId_Type()
)
xfRLTExpectedFarEndId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLTExpectedFarEndId.setStatus("current")


class _XfRLTFarEndIdCheck_Type(Integer32):
    """Custom type xfRLTFarEndIdCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enable", 2),
          ("disable", 3))
    )


_XfRLTFarEndIdCheck_Type.__name__ = "Integer32"
_XfRLTFarEndIdCheck_Object = MibTableColumn
xfRLTFarEndIdCheck = _XfRLTFarEndIdCheck_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 9),
    _XfRLTFarEndIdCheck_Type()
)
xfRLTFarEndIdCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLTFarEndIdCheck.setStatus("current")


class _XfRLTStatus_Type(Integer32):
    """Custom type xfRLTStatus based on Integer32"""
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
        *(("other", 1),
          ("down", 2),
          ("up", 3),
          ("degraded", 4),
          ("resourceUnavailable", 5))
    )


_XfRLTStatus_Type.__name__ = "Integer32"
_XfRLTStatus_Object = MibTableColumn
xfRLTStatus = _XfRLTStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 10),
    _XfRLTStatus_Type()
)
xfRLTStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTStatus.setStatus("current")


class _XfRLTMode_Type(Integer32):
    """Custom type xfRLTMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("onePlusZero", 2),
          ("onePlusOneRadioLinkProtection", 3),
          ("twoPlusZeroAdvancedRadioLinkBonding", 4),
          ("onePlusOneRadioLinkProtectionAndEquipmentProtection", 5),
          ("twoPlusZeroRadioLinkBondingAndEquipmentProtection", 6),
          ("twoPlusTwoRadioLinkProtectionAndEquipmentProtection", 7),
          ("fourPlusZeroRadioLinkBondingAndEquipmentProtection", 8))
    )


_XfRLTMode_Type.__name__ = "Integer32"
_XfRLTMode_Object = MibTableColumn
xfRLTMode = _XfRLTMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 11),
    _XfRLTMode_Type()
)
xfRLTMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLTMode.setStatus("current")
_XfRLTActualTXTotalCapacity_Type = Gauge32
_XfRLTActualTXTotalCapacity_Object = MibTableColumn
xfRLTActualTXTotalCapacity = _XfRLTActualTXTotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 12),
    _XfRLTActualTXTotalCapacity_Type()
)
xfRLTActualTXTotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTActualTXTotalCapacity.setStatus("current")
_XfRLTActualTXPacketCapacity_Type = Gauge32
_XfRLTActualTXPacketCapacity_Object = MibTableColumn
xfRLTActualTXPacketCapacity = _XfRLTActualTXPacketCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 13),
    _XfRLTActualTXPacketCapacity_Type()
)
xfRLTActualTXPacketCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTActualTXPacketCapacity.setStatus("current")
_XfRLTLimitedTotalCapacity_Type = Gauge32
_XfRLTLimitedTotalCapacity_Object = MibTableColumn
xfRLTLimitedTotalCapacity = _XfRLTLimitedTotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 14),
    _XfRLTLimitedTotalCapacity_Type()
)
xfRLTLimitedTotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTLimitedTotalCapacity.setStatus("current")


class _XfRLTRltSeverity_Type(Bits):
    """Custom type xfRLTRltSeverity based on Bits"""
    namedValues = NamedValues(
        *(("rltSeverity0", 0),
          ("rltSeverity1", 1),
          ("rltSeverity2", 2))
    )

_XfRLTRltSeverity_Type.__name__ = "Bits"
_XfRLTRltSeverity_Object = MibTableColumn
xfRLTRltSeverity = _XfRLTRltSeverity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 15),
    _XfRLTRltSeverity_Type()
)
xfRLTRltSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTRltSeverity.setStatus("current")


class _XfRLTCapability_Type(Bits):
    """Custom type xfRLTCapability based on Bits"""
    namedValues = NamedValues(
        *(("xpicCapability0", 0),
          ("capTDMWithEQP", 1),
          ("capCsPlurality", 2),
          ("capCtAutoSelection", 3),
          ("capOnePlusZero", 4),
          ("capOnePlusOneRadioLinkProtection", 5),
          ("capTwoPlusZeroAdvancedRadioLinkBonding", 6),
          ("capOnePlusOneRadioLinkProtectionWithEQP", 7),
          ("capTwoPlusZeroRadioLinkBondingWithEQP", 8),
          ("capTwoPlusTwoRadioLinkProtectionWithEQP", 9),
          ("capFourPlusZeroRadioLinkBondingWithEQP", 10),
          ("capXpicBetweenBoards", 11),
          ("capXpicMembersAutoSelection", 12),
          ("capManualEqpSwitch", 13),
          ("capEnhAcmMaxCapacity", 14),
          ("capEnhAcmMaxProtection", 15),
          ("capRLEncryption", 16),
          ("capMIMO", 17),
          ("capTXswoAndSSD", 18))
    )

_XfRLTCapability_Type.__name__ = "Bits"
_XfRLTCapability_Object = MibTableColumn
xfRLTCapability = _XfRLTCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 16),
    _XfRLTCapability_Type()
)
xfRLTCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTCapability.setStatus("current")
_XfRLTInventoryLastChange_Type = TimeTicks
_XfRLTInventoryLastChange_Object = MibTableColumn
xfRLTInventoryLastChange = _XfRLTInventoryLastChange_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 17),
    _XfRLTInventoryLastChange_Type()
)
xfRLTInventoryLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTInventoryLastChange.setStatus("current")
_XfRLTCpriMode_Type = Integer32
_XfRLTCpriMode_Object = MibTableColumn
xfRLTCpriMode = _XfRLTCpriMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 18),
    _XfRLTCpriMode_Type()
)
xfRLTCpriMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTCpriMode.setStatus("current")


class _XfRLTReset_Type(Integer32):
    """Custom type xfRLTReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("rltNoReset", 2),
          ("rltReset", 3))
    )


_XfRLTReset_Type.__name__ = "Integer32"
_XfRLTReset_Object = MibTableColumn
xfRLTReset = _XfRLTReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 19),
    _XfRLTReset_Type()
)
xfRLTReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLTReset.setStatus("current")
_XfRLTMeasuredHopLength_Type = Integer32
_XfRLTMeasuredHopLength_Object = MibTableColumn
xfRLTMeasuredHopLength = _XfRLTMeasuredHopLength_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 6, 1, 20),
    _XfRLTMeasuredHopLength_Type()
)
xfRLTMeasuredHopLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTMeasuredHopLength.setStatus("current")
_XfTrafficTable_Object = MibTable
xfTrafficTable = _XfTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 7)
)
if mibBuilder.loadTexts:
    xfTrafficTable.setStatus("current")
_XfTrafficEntry_Object = MibTableRow
xfTrafficEntry = _XfTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 7, 1)
)
xfTrafficEntry.setIndexNames(
    (0, "XF-RADIOLINK-RLT-MIB", "trEntLogicalIndex"),
)
if mibBuilder.loadTexts:
    xfTrafficEntry.setStatus("current")


class _TrEntLogicalIndex_Type(Integer32):
    """Custom type trEntLogicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrEntLogicalIndex_Type.__name__ = "Integer32"
_TrEntLogicalIndex_Object = MibTableColumn
trEntLogicalIndex = _TrEntLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 7, 1, 1),
    _TrEntLogicalIndex_Type()
)
trEntLogicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trEntLogicalIndex.setStatus("current")


class _XfTDMEnable_Type(Integer32):
    """Custom type xfTDMEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enable", 2),
          ("disable", 3))
    )


_XfTDMEnable_Type.__name__ = "Integer32"
_XfTDMEnable_Object = MibTableColumn
xfTDMEnable = _XfTDMEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 7, 1, 2),
    _XfTDMEnable_Type()
)
xfTDMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTDMEnable.setStatus("current")
_XfRLTDMIfTable_Object = MibTable
xfRLTDMIfTable = _XfRLTDMIfTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 8)
)
if mibBuilder.loadTexts:
    xfRLTDMIfTable.setStatus("current")
_XfRLTDMIfEntry_Object = MibTableRow
xfRLTDMIfEntry = _XfRLTDMIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 8, 1)
)
xfRLTDMIfEntry.setIndexNames(
    (0, "XF-RADIOLINK-RLT-MIB", "xfRLTDMIfIndex"),
)
if mibBuilder.loadTexts:
    xfRLTDMIfEntry.setStatus("current")


class _XfRLTDMIfIndex_Type(Integer32):
    """Custom type xfRLTDMIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_XfRLTDMIfIndex_Type.__name__ = "Integer32"
_XfRLTDMIfIndex_Object = MibTableColumn
xfRLTDMIfIndex = _XfRLTDMIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 8, 1, 1),
    _XfRLTDMIfIndex_Type()
)
xfRLTDMIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTDMIfIndex.setStatus("current")


class _XfActualTDMCapacity_Type(Integer32):
    """Custom type xfActualTDMCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XfActualTDMCapacity_Type.__name__ = "Integer32"
_XfActualTDMCapacity_Object = MibTableColumn
xfActualTDMCapacity = _XfActualTDMCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 8, 1, 2),
    _XfActualTDMCapacity_Type()
)
xfActualTDMCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfActualTDMCapacity.setStatus("current")


class _XfWantedTDMAllocation_Type(Bits):
    """Custom type xfWantedTDMAllocation based on Bits"""
    namedValues = NamedValues(
        ("firstE1", 0)
    )

_XfWantedTDMAllocation_Type.__name__ = "Bits"
_XfWantedTDMAllocation_Object = MibTableColumn
xfWantedTDMAllocation = _XfWantedTDMAllocation_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 8, 1, 3),
    _XfWantedTDMAllocation_Type()
)
xfWantedTDMAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfWantedTDMAllocation.setStatus("current")


class _XfActualTDMAllocation_Type(Bits):
    """Custom type xfActualTDMAllocation based on Bits"""
    namedValues = NamedValues(
        ("firstE1", 0)
    )

_XfActualTDMAllocation_Type.__name__ = "Bits"
_XfActualTDMAllocation_Object = MibTableColumn
xfActualTDMAllocation = _XfActualTDMAllocation_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 8, 1, 4),
    _XfActualTDMAllocation_Type()
)
xfActualTDMAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfActualTDMAllocation.setStatus("current")


class _XfTDMIfAlarms_Type(Bits):
    """Custom type xfTDMIfAlarms based on Bits"""
    namedValues = NamedValues(
        *(("ber0", 0),
          ("ber1", 1),
          ("ber2", 2))
    )

_XfTDMIfAlarms_Type.__name__ = "Bits"
_XfTDMIfAlarms_Object = MibTableColumn
xfTDMIfAlarms = _XfTDMIfAlarms_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 8, 1, 5),
    _XfTDMIfAlarms_Type()
)
xfTDMIfAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTDMIfAlarms.setStatus("current")


class _XfTDMRxLoop_Type(Integer32):
    """Custom type xfTDMRxLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enable", 2),
          ("disable", 3))
    )


_XfTDMRxLoop_Type.__name__ = "Integer32"
_XfTDMRxLoop_Object = MibTableColumn
xfTDMRxLoop = _XfTDMRxLoop_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 8, 1, 6),
    _XfTDMRxLoop_Type()
)
xfTDMRxLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTDMRxLoop.setStatus("current")


class _XfTDMDistinguishedName_Type(DisplayString):
    """Custom type xfTDMDistinguishedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XfTDMDistinguishedName_Type.__name__ = "DisplayString"
_XfTDMDistinguishedName_Object = MibTableColumn
xfTDMDistinguishedName = _XfTDMDistinguishedName_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 8, 1, 7),
    _XfTDMDistinguishedName_Type()
)
xfTDMDistinguishedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTDMDistinguishedName.setStatus("current")
_XfTDMMaxTributaries_Type = Integer32
_XfTDMMaxTributaries_Object = MibTableColumn
xfTDMMaxTributaries = _XfTDMMaxTributaries_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 8, 1, 8),
    _XfTDMMaxTributaries_Type()
)
xfTDMMaxTributaries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTDMMaxTributaries.setStatus("current")
_XfTDMHopLength_Type = Integer32
_XfTDMHopLength_Object = MibTableColumn
xfTDMHopLength = _XfTDMHopLength_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 8, 1, 9),
    _XfTDMHopLength_Type()
)
xfTDMHopLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTDMHopLength.setStatus("current")
_XfCGIfTable_Object = MibTable
xfCGIfTable = _XfCGIfTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 9)
)
if mibBuilder.loadTexts:
    xfCGIfTable.setStatus("current")
_XfCGIfEntry_Object = MibTableRow
xfCGIfEntry = _XfCGIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 9, 1)
)
xfCGIfEntry.setIndexNames(
    (0, "XF-RADIOLINK-RLT-MIB", "xfCGIfIndex"),
)
if mibBuilder.loadTexts:
    xfCGIfEntry.setStatus("current")


class _XfCGIfIndex_Type(Integer32):
    """Custom type xfCGIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_XfCGIfIndex_Type.__name__ = "Integer32"
_XfCGIfIndex_Object = MibTableColumn
xfCGIfIndex = _XfCGIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 9, 1, 1),
    _XfCGIfIndex_Type()
)
xfCGIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfCGIfIndex.setStatus("current")


class _XfCGIfMinSpeed_Type(Integer32):
    """Custom type xfCGIfMinSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_XfCGIfMinSpeed_Type.__name__ = "Integer32"
_XfCGIfMinSpeed_Object = MibTableColumn
xfCGIfMinSpeed = _XfCGIfMinSpeed_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 9, 1, 2),
    _XfCGIfMinSpeed_Type()
)
xfCGIfMinSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfCGIfMinSpeed.setStatus("current")
_XfCGIfMaxSpeed_Type = Gauge32
_XfCGIfMaxSpeed_Object = MibTableColumn
xfCGIfMaxSpeed = _XfCGIfMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 9, 1, 3),
    _XfCGIfMaxSpeed_Type()
)
xfCGIfMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfCGIfMaxSpeed.setStatus("current")


class _XfCGIfRCNum_Type(Integer32):
    """Custom type xfCGIfRCNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_XfCGIfRCNum_Type.__name__ = "Integer32"
_XfCGIfRCNum_Object = MibTableColumn
xfCGIfRCNum = _XfCGIfRCNum_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 9, 1, 4),
    _XfCGIfRCNum_Type()
)
xfCGIfRCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfCGIfRCNum.setStatus("current")


class _XfCGIfAlarms_Type(Bits):
    """Custom type xfCGIfAlarms based on Bits"""
    namedValues = NamedValues(
        *(("hccNe0", 0),
          ("hccNe1", 1),
          ("hccNe2", 2),
          ("rltId0", 3),
          ("rltId1", 4),
          ("rltId2", 5),
          ("txSwitchover0", 6),
          ("txSwitchover1", 7),
          ("txSwitchover2", 8),
          ("remoteTxSwitchOver0", 9),
          ("remoteTxSwitchOver1", 10),
          ("remoteTxSwitchOver2", 11),
          ("unableToProtect0", 12),
          ("unableToProtect1", 13),
          ("unableToProtect2", 14),
          ("rfInputThresholdProtection0", 15),
          ("rfInputThresholdProtection1", 16),
          ("rfInputThresholdProtection2", 17),
          ("unableToProtectEqp0", 18),
          ("unableToProtectEqp1", 19),
          ("unableToProtectEqp2", 20))
    )

_XfCGIfAlarms_Type.__name__ = "Bits"
_XfCGIfAlarms_Object = MibTableColumn
xfCGIfAlarms = _XfCGIfAlarms_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 9, 1, 5),
    _XfCGIfAlarms_Type()
)
xfCGIfAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfCGIfAlarms.setStatus("current")


class _XfCGIfHopViewStatus_Type(Integer32):
    """Custom type xfCGIfHopViewStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("down", 2),
          ("up", 3))
    )


_XfCGIfHopViewStatus_Type.__name__ = "Integer32"
_XfCGIfHopViewStatus_Object = MibTableColumn
xfCGIfHopViewStatus = _XfCGIfHopViewStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 9, 1, 6),
    _XfCGIfHopViewStatus_Type()
)
xfCGIfHopViewStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfCGIfHopViewStatus.setStatus("current")
_XfXPICPairTable_Object = MibTable
xfXPICPairTable = _XfXPICPairTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 10)
)
if mibBuilder.loadTexts:
    xfXPICPairTable.setStatus("current")
_XfXPICPairEntry_Object = MibTableRow
xfXPICPairEntry = _XfXPICPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 10, 1)
)
xfXPICPairEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLogicalIndex"),
    (0, "XF-RADIOLINK-RLT-MIB", "xfXpicPairIndex"),
)
if mibBuilder.loadTexts:
    xfXPICPairEntry.setStatus("current")


class _XpicPairEntLogicalIIndex_Type(Integer32):
    """Custom type xpicPairEntLogicalIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_XpicPairEntLogicalIIndex_Type.__name__ = "Integer32"
_XpicPairEntLogicalIIndex_Object = MibTableColumn
xpicPairEntLogicalIIndex = _XpicPairEntLogicalIIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 10, 1, 1),
    _XpicPairEntLogicalIIndex_Type()
)
xpicPairEntLogicalIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpicPairEntLogicalIIndex.setStatus("current")


class _XfXPICPairAdminStatus_Type(Integer32):
    """Custom type xfXPICPairAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enable", 2),
          ("disable", 3))
    )


_XfXPICPairAdminStatus_Type.__name__ = "Integer32"
_XfXPICPairAdminStatus_Object = MibTableColumn
xfXPICPairAdminStatus = _XfXPICPairAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 10, 1, 2),
    _XfXPICPairAdminStatus_Type()
)
xfXPICPairAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfXPICPairAdminStatus.setStatus("current")
_XfXPICPairNumber_Type = Integer32
_XfXPICPairNumber_Object = MibTableColumn
xfXPICPairNumber = _XfXPICPairNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 10, 1, 3),
    _XfXPICPairNumber_Type()
)
xfXPICPairNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfXPICPairNumber.setStatus("current")


class _XfXPICPairRecovery_Type(Integer32):
    """Custom type xfXPICPairRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enable", 2),
          ("disable", 3))
    )


_XfXPICPairRecovery_Type.__name__ = "Integer32"
_XfXPICPairRecovery_Object = MibTableColumn
xfXPICPairRecovery = _XfXPICPairRecovery_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 10, 1, 4),
    _XfXPICPairRecovery_Type()
)
xfXPICPairRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfXPICPairRecovery.setStatus("current")


class _XfXPICPairRestore_Type(Integer32):
    """Custom type xfXPICPairRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("xpicNoRestore", 2),
          ("xpicRestore", 3))
    )


_XfXPICPairRestore_Type.__name__ = "Integer32"
_XfXPICPairRestore_Object = MibTableColumn
xfXPICPairRestore = _XfXPICPairRestore_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 10, 1, 5),
    _XfXPICPairRestore_Type()
)
xfXPICPairRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfXPICPairRestore.setStatus("current")


class _XfXPICCTmember1_Type(DisplayString):
    """Custom type xfXPICCTmember1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XfXPICCTmember1_Type.__name__ = "DisplayString"
_XfXPICCTmember1_Object = MibTableColumn
xfXPICCTmember1 = _XfXPICCTmember1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 10, 1, 6),
    _XfXPICCTmember1_Type()
)
xfXPICCTmember1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfXPICCTmember1.setStatus("current")


class _XfXPICCTmember2_Type(DisplayString):
    """Custom type xfXPICCTmember2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XfXPICCTmember2_Type.__name__ = "DisplayString"
_XfXPICCTmember2_Object = MibTableColumn
xfXPICCTmember2 = _XfXPICCTmember2_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 10, 1, 7),
    _XfXPICCTmember2_Type()
)
xfXPICCTmember2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfXPICCTmember2.setStatus("current")


class _XfXPICAutoRestore_Type(Integer32):
    """Custom type xfXPICAutoRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enable", 2),
          ("disable", 3))
    )


_XfXPICAutoRestore_Type.__name__ = "Integer32"
_XfXPICAutoRestore_Object = MibTableColumn
xfXPICAutoRestore = _XfXPICAutoRestore_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 10, 1, 8),
    _XfXPICAutoRestore_Type()
)
xfXPICAutoRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfXPICAutoRestore.setStatus("current")


class _XfXpicPairIndex_Type(Integer32):
    """Custom type xfXpicPairIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_XfXpicPairIndex_Type.__name__ = "Integer32"
_XfXpicPairIndex_Object = MibTableColumn
xfXpicPairIndex = _XfXpicPairIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 10, 1, 9),
    _XfXpicPairIndex_Type()
)
xfXpicPairIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfXpicPairIndex.setStatus("current")
_XfMIMOGroupTable_Object = MibTable
xfMIMOGroupTable = _XfMIMOGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 11)
)
if mibBuilder.loadTexts:
    xfMIMOGroupTable.setStatus("current")
_XfMIMOGroupEntry_Object = MibTableRow
xfMIMOGroupEntry = _XfMIMOGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 11, 1)
)
xfMIMOGroupEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLogicalIndex"),
)
if mibBuilder.loadTexts:
    xfMIMOGroupEntry.setStatus("current")


class _MimoGroupEntLogicalIIndex_Type(Integer32):
    """Custom type mimoGroupEntLogicalIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MimoGroupEntLogicalIIndex_Type.__name__ = "Integer32"
_MimoGroupEntLogicalIIndex_Object = MibTableColumn
mimoGroupEntLogicalIIndex = _MimoGroupEntLogicalIIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 11, 1, 1),
    _MimoGroupEntLogicalIIndex_Type()
)
mimoGroupEntLogicalIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimoGroupEntLogicalIIndex.setStatus("current")


class _XfMIMOGroupAdminStatus_Type(Integer32):
    """Custom type xfMIMOGroupAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enable", 2),
          ("disable", 3))
    )


_XfMIMOGroupAdminStatus_Type.__name__ = "Integer32"
_XfMIMOGroupAdminStatus_Object = MibTableColumn
xfMIMOGroupAdminStatus = _XfMIMOGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 11, 1, 2),
    _XfMIMOGroupAdminStatus_Type()
)
xfMIMOGroupAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfMIMOGroupAdminStatus.setStatus("current")
_XfMIMOGroupNumber_Type = Integer32
_XfMIMOGroupNumber_Object = MibTableColumn
xfMIMOGroupNumber = _XfMIMOGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 11, 1, 3),
    _XfMIMOGroupNumber_Type()
)
xfMIMOGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfMIMOGroupNumber.setStatus("current")


class _XfMIMOGroupRecovery_Type(Integer32):
    """Custom type xfMIMOGroupRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enable", 2),
          ("disable", 3))
    )


_XfMIMOGroupRecovery_Type.__name__ = "Integer32"
_XfMIMOGroupRecovery_Object = MibTableColumn
xfMIMOGroupRecovery = _XfMIMOGroupRecovery_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 11, 1, 4),
    _XfMIMOGroupRecovery_Type()
)
xfMIMOGroupRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfMIMOGroupRecovery.setStatus("current")


class _XfMIMOGroupRestore_Type(Integer32):
    """Custom type xfMIMOGroupRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("mimoNoRestore", 2),
          ("mimoRestore", 3))
    )


_XfMIMOGroupRestore_Type.__name__ = "Integer32"
_XfMIMOGroupRestore_Object = MibTableColumn
xfMIMOGroupRestore = _XfMIMOGroupRestore_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 11, 1, 5),
    _XfMIMOGroupRestore_Type()
)
xfMIMOGroupRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfMIMOGroupRestore.setStatus("current")


class _XfMIMOCTmember1_Type(DisplayString):
    """Custom type xfMIMOCTmember1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XfMIMOCTmember1_Type.__name__ = "DisplayString"
_XfMIMOCTmember1_Object = MibTableColumn
xfMIMOCTmember1 = _XfMIMOCTmember1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 11, 1, 6),
    _XfMIMOCTmember1_Type()
)
xfMIMOCTmember1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMIMOCTmember1.setStatus("current")


class _XfMIMOCTmember2_Type(DisplayString):
    """Custom type xfMIMOCTmember2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XfMIMOCTmember2_Type.__name__ = "DisplayString"
_XfMIMOCTmember2_Object = MibTableColumn
xfMIMOCTmember2 = _XfMIMOCTmember2_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 11, 1, 7),
    _XfMIMOCTmember2_Type()
)
xfMIMOCTmember2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMIMOCTmember2.setStatus("current")


class _XfMIMOCTmember3_Type(DisplayString):
    """Custom type xfMIMOCTmember3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XfMIMOCTmember3_Type.__name__ = "DisplayString"
_XfMIMOCTmember3_Object = MibTableColumn
xfMIMOCTmember3 = _XfMIMOCTmember3_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 11, 1, 8),
    _XfMIMOCTmember3_Type()
)
xfMIMOCTmember3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMIMOCTmember3.setStatus("current")


class _XfMIMOCTmember4_Type(DisplayString):
    """Custom type xfMIMOCTmember4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XfMIMOCTmember4_Type.__name__ = "DisplayString"
_XfMIMOCTmember4_Object = MibTableColumn
xfMIMOCTmember4 = _XfMIMOCTmember4_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 11, 1, 9),
    _XfMIMOCTmember4_Type()
)
xfMIMOCTmember4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMIMOCTmember4.setStatus("current")
_XfRLWANIfTable_Object = MibTable
xfRLWANIfTable = _XfRLWANIfTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 12)
)
if mibBuilder.loadTexts:
    xfRLWANIfTable.setStatus("current")
_XfRLWANIfEntry_Object = MibTableRow
xfRLWANIfEntry = _XfRLWANIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 12, 1)
)
xfRLWANIfEntry.setIndexNames(
    (0, "XF-RADIOLINK-RLT-MIB", "xfRLWANIfIndex"),
)
if mibBuilder.loadTexts:
    xfRLWANIfEntry.setStatus("current")


class _XfRLWANIfIndex_Type(Integer32):
    """Custom type xfRLWANIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_XfRLWANIfIndex_Type.__name__ = "Integer32"
_XfRLWANIfIndex_Object = MibTableColumn
xfRLWANIfIndex = _XfRLWANIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 12, 1, 1),
    _XfRLWANIfIndex_Type()
)
xfRLWANIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLWANIfIndex.setStatus("current")


class _XfRLWANDistinguishedName_Type(DisplayString):
    """Custom type xfRLWANDistinguishedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XfRLWANDistinguishedName_Type.__name__ = "DisplayString"
_XfRLWANDistinguishedName_Object = MibTableColumn
xfRLWANDistinguishedName = _XfRLWANDistinguishedName_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 12, 1, 2),
    _XfRLWANDistinguishedName_Type()
)
xfRLWANDistinguishedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLWANDistinguishedName.setStatus("current")


class _XfRLWANCompAdminStatus_Type(Integer32):
    """Custom type xfRLWANCompAdminStatus based on Integer32"""
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
        *(("other", 1),
          ("down", 2),
          ("mlhcUp", 3),
          ("mlhcPlcUp", 4))
    )


_XfRLWANCompAdminStatus_Type.__name__ = "Integer32"
_XfRLWANCompAdminStatus_Object = MibTableColumn
xfRLWANCompAdminStatus = _XfRLWANCompAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 12, 1, 3),
    _XfRLWANCompAdminStatus_Type()
)
xfRLWANCompAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLWANCompAdminStatus.setStatus("current")


class _XfRLWANCompConnStatus_Type(Integer32):
    """Custom type xfRLWANCompConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disconnected", 2),
          ("connected", 3))
    )


_XfRLWANCompConnStatus_Type.__name__ = "Integer32"
_XfRLWANCompConnStatus_Object = MibTableColumn
xfRLWANCompConnStatus = _XfRLWANCompConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 12, 1, 4),
    _XfRLWANCompConnStatus_Type()
)
xfRLWANCompConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLWANCompConnStatus.setStatus("current")


class _XfRLWANMlhcMplsMode_Type(Integer32):
    """Custom type xfRLWANMlhcMplsMode based on Integer32"""
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
        *(("other", 1),
          ("mplsOnly", 2),
          ("controlWord", 3),
          ("l2", 4),
          ("l3", 5))
    )


_XfRLWANMlhcMplsMode_Type.__name__ = "Integer32"
_XfRLWANMlhcMplsMode_Object = MibTableColumn
xfRLWANMlhcMplsMode = _XfRLWANMlhcMplsMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 12, 1, 5),
    _XfRLWANMlhcMplsMode_Type()
)
xfRLWANMlhcMplsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLWANMlhcMplsMode.setStatus("current")


class _XfRLWANMlhcOperStatus_Type(Integer32):
    """Custom type xfRLWANMlhcOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("down", 2),
          ("up", 3))
    )


_XfRLWANMlhcOperStatus_Type.__name__ = "Integer32"
_XfRLWANMlhcOperStatus_Object = MibTableColumn
xfRLWANMlhcOperStatus = _XfRLWANMlhcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 12, 1, 6),
    _XfRLWANMlhcOperStatus_Type()
)
xfRLWANMlhcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLWANMlhcOperStatus.setStatus("current")


class _XfRLWANPlcOperStatus_Type(Integer32):
    """Custom type xfRLWANPlcOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("down", 2),
          ("up", 3))
    )


_XfRLWANPlcOperStatus_Type.__name__ = "Integer32"
_XfRLWANPlcOperStatus_Object = MibTableColumn
xfRLWANPlcOperStatus = _XfRLWANPlcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 12, 1, 7),
    _XfRLWANPlcOperStatus_Type()
)
xfRLWANPlcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLWANPlcOperStatus.setStatus("current")
_XfRLWANActualCapacity_Type = Gauge32
_XfRLWANActualCapacity_Object = MibTableColumn
xfRLWANActualCapacity = _XfRLWANActualCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 12, 1, 8),
    _XfRLWANActualCapacity_Type()
)
xfRLWANActualCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLWANActualCapacity.setStatus("current")
_XfRLWANLimitedCapacity_Type = Gauge32
_XfRLWANLimitedCapacity_Object = MibTableColumn
xfRLWANLimitedCapacity = _XfRLWANLimitedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 12, 1, 9),
    _XfRLWANLimitedCapacity_Type()
)
xfRLWANLimitedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLWANLimitedCapacity.setStatus("current")
_XfRLTHierarchyModuleTable_Object = MibTable
xfRLTHierarchyModuleTable = _XfRLTHierarchyModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 13)
)
if mibBuilder.loadTexts:
    xfRLTHierarchyModuleTable.setStatus("current")
_XfRLTHierarchyModuleEntry_Object = MibTableRow
xfRLTHierarchyModuleEntry = _XfRLTHierarchyModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 13, 1)
)
xfRLTHierarchyModuleEntry.setIndexNames(
    (0, "XF-RADIOLINK-RLT-MIB", "xfRLTMHIndex"),
    (0, "XF-RADIOLINK-RLT-MIB", "xfRLTModuleIndex"),
)
if mibBuilder.loadTexts:
    xfRLTHierarchyModuleEntry.setStatus("current")


class _XfRLTMHIndex_Type(Integer32):
    """Custom type xfRLTMHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_XfRLTMHIndex_Type.__name__ = "Integer32"
_XfRLTMHIndex_Object = MibTableColumn
xfRLTMHIndex = _XfRLTMHIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 13, 1, 1),
    _XfRLTMHIndex_Type()
)
xfRLTMHIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTMHIndex.setStatus("current")


class _XfRLTModuleIndex_Type(Integer32):
    """Custom type xfRLTModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_XfRLTModuleIndex_Type.__name__ = "Integer32"
_XfRLTModuleIndex_Object = MibTableColumn
xfRLTModuleIndex = _XfRLTModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 13, 1, 2),
    _XfRLTModuleIndex_Type()
)
xfRLTModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTModuleIndex.setStatus("current")
_XfRLTEntPhysicalIndex_Type = Integer32
_XfRLTEntPhysicalIndex_Object = MibTableColumn
xfRLTEntPhysicalIndex = _XfRLTEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 13, 1, 3),
    _XfRLTEntPhysicalIndex_Type()
)
xfRLTEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTEntPhysicalIndex.setStatus("current")
_XfRLTPhysicalCointainedIn_Type = Integer32
_XfRLTPhysicalCointainedIn_Object = MibTableColumn
xfRLTPhysicalCointainedIn = _XfRLTPhysicalCointainedIn_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 13, 1, 4),
    _XfRLTPhysicalCointainedIn_Type()
)
xfRLTPhysicalCointainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTPhysicalCointainedIn.setStatus("current")
_XfRLTPhysicalParentRelPos_Type = Integer32
_XfRLTPhysicalParentRelPos_Object = MibTableColumn
xfRLTPhysicalParentRelPos = _XfRLTPhysicalParentRelPos_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 13, 1, 5),
    _XfRLTPhysicalParentRelPos_Type()
)
xfRLTPhysicalParentRelPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTPhysicalParentRelPos.setStatus("current")
_XfRLTEntityPhysicalDescr_Type = DisplayString
_XfRLTEntityPhysicalDescr_Object = MibTableColumn
xfRLTEntityPhysicalDescr = _XfRLTEntityPhysicalDescr_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 13, 1, 6),
    _XfRLTEntityPhysicalDescr_Type()
)
xfRLTEntityPhysicalDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTEntityPhysicalDescr.setStatus("current")
_XfRLTModuleSlotPosition_Type = Integer32
_XfRLTModuleSlotPosition_Object = MibTableColumn
xfRLTModuleSlotPosition = _XfRLTModuleSlotPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 13, 1, 7),
    _XfRLTModuleSlotPosition_Type()
)
xfRLTModuleSlotPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTModuleSlotPosition.setStatus("current")
_XfRLTFEDistinguishedName_Type = DisplayString
_XfRLTFEDistinguishedName_Object = MibTableColumn
xfRLTFEDistinguishedName = _XfRLTFEDistinguishedName_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 13, 1, 8),
    _XfRLTFEDistinguishedName_Type()
)
xfRLTFEDistinguishedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTFEDistinguishedName.setStatus("current")
_XfRLTNEDistinguishedName_Type = DisplayString
_XfRLTNEDistinguishedName_Object = MibTableColumn
xfRLTNEDistinguishedName = _XfRLTNEDistinguishedName_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 13, 1, 9),
    _XfRLTNEDistinguishedName_Type()
)
xfRLTNEDistinguishedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTNEDistinguishedName.setStatus("current")
_XfRLTInterfaceIndex_Type = Integer32
_XfRLTInterfaceIndex_Object = MibTableColumn
xfRLTInterfaceIndex = _XfRLTInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 13, 1, 10),
    _XfRLTInterfaceIndex_Type()
)
xfRLTInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTInterfaceIndex.setStatus("current")


class _XfRLTHighestSeverityAlarm_Type(Integer32):
    """Custom type xfRLTHighestSeverityAlarm based on Integer32"""
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
        *(("critical", 0),
          ("major", 1),
          ("minor", 2),
          ("warning", 3),
          ("clear", 4))
    )


_XfRLTHighestSeverityAlarm_Type.__name__ = "Integer32"
_XfRLTHighestSeverityAlarm_Object = MibTableColumn
xfRLTHighestSeverityAlarm = _XfRLTHighestSeverityAlarm_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 13, 1, 11),
    _XfRLTHighestSeverityAlarm_Type()
)
xfRLTHighestSeverityAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTHighestSeverityAlarm.setStatus("current")
_XfRLTProtectionTable_Object = MibTable
xfRLTProtectionTable = _XfRLTProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 14)
)
if mibBuilder.loadTexts:
    xfRLTProtectionTable.setStatus("current")
_XfRLTProtectionEntry_Object = MibTableRow
xfRLTProtectionEntry = _XfRLTProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 14, 1)
)
xfRLTProtectionEntry.setIndexNames(
    (0, "XF-RADIOLINK-RLT-MIB", "xfRLTProtIndex"),
)
if mibBuilder.loadTexts:
    xfRLTProtectionEntry.setStatus("current")


class _XfRLTProtIndex_Type(Integer32):
    """Custom type xfRLTProtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_XfRLTProtIndex_Type.__name__ = "Integer32"
_XfRLTProtIndex_Object = MibTableColumn
xfRLTProtIndex = _XfRLTProtIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 14, 1, 1),
    _XfRLTProtIndex_Type()
)
xfRLTProtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTProtIndex.setStatus("current")


class _XfRLTProtectionSwitchMode_Type(Integer32):
    """Custom type xfRLTProtectionSwitchMode based on Integer32"""
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
        *(("other", 1),
          ("auto", 2),
          ("manual", 3),
          ("autoRevertive", 4),
          ("txSwitchDisable", 5))
    )


_XfRLTProtectionSwitchMode_Type.__name__ = "Integer32"
_XfRLTProtectionSwitchMode_Object = MibTableColumn
xfRLTProtectionSwitchMode = _XfRLTProtectionSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 14, 1, 2),
    _XfRLTProtectionSwitchMode_Type()
)
xfRLTProtectionSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLTProtectionSwitchMode.setStatus("current")


class _XfRLTProtectionStatus_Type(Integer32):
    """Custom type xfRLTProtectionStatus based on Integer32"""
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
        *(("other", 1),
          ("unprotected", 2),
          ("protected", 3),
          ("unableToProtect", 4))
    )


_XfRLTProtectionStatus_Type.__name__ = "Integer32"
_XfRLTProtectionStatus_Object = MibTableColumn
xfRLTProtectionStatus = _XfRLTProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 14, 1, 3),
    _XfRLTProtectionStatus_Type()
)
xfRLTProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTProtectionStatus.setStatus("current")


class _XfRLTRevertivePreferredTX_Type(DisplayString):
    """Custom type xfRLTRevertivePreferredTX based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XfRLTRevertivePreferredTX_Type.__name__ = "DisplayString"
_XfRLTRevertivePreferredTX_Object = MibTableColumn
xfRLTRevertivePreferredTX = _XfRLTRevertivePreferredTX_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 14, 1, 4),
    _XfRLTRevertivePreferredTX_Type()
)
xfRLTRevertivePreferredTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLTRevertivePreferredTX.setStatus("current")
_XfRLTProtectionWaitToRestoreTime_Type = Integer32
_XfRLTProtectionWaitToRestoreTime_Object = MibTableColumn
xfRLTProtectionWaitToRestoreTime = _XfRLTProtectionWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 14, 1, 5),
    _XfRLTProtectionWaitToRestoreTime_Type()
)
xfRLTProtectionWaitToRestoreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLTProtectionWaitToRestoreTime.setStatus("current")
_XfRLTFadeNotificationTimer_Type = Integer32
_XfRLTFadeNotificationTimer_Object = MibTableColumn
xfRLTFadeNotificationTimer = _XfRLTFadeNotificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 14, 1, 6),
    _XfRLTFadeNotificationTimer_Type()
)
xfRLTFadeNotificationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLTFadeNotificationTimer.setStatus("current")


class _XfRLTManualSwitchCommand_Type(Integer32):
    """Custom type xfRLTManualSwitchCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("txManualSwitch", 2),
          ("txManualNoSwitch", 3))
    )


_XfRLTManualSwitchCommand_Type.__name__ = "Integer32"
_XfRLTManualSwitchCommand_Object = MibTableColumn
xfRLTManualSwitchCommand = _XfRLTManualSwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 14, 1, 7),
    _XfRLTManualSwitchCommand_Type()
)
xfRLTManualSwitchCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLTManualSwitchCommand.setStatus("current")


class _XfRLTTxSwitchOverConfiguration_Type(Integer32):
    """Custom type xfRLTTxSwitchOverConfiguration based on Integer32"""
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
        *(("other", 1),
          ("notSupported", 2),
          ("enable", 3),
          ("disable", 4),
          ("enableLocal", 5))
    )


_XfRLTTxSwitchOverConfiguration_Type.__name__ = "Integer32"
_XfRLTTxSwitchOverConfiguration_Object = MibTableColumn
xfRLTTxSwitchOverConfiguration = _XfRLTTxSwitchOverConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 14, 1, 8),
    _XfRLTTxSwitchOverConfiguration_Type()
)
xfRLTTxSwitchOverConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLTTxSwitchOverConfiguration.setStatus("current")


class _XfRLTTxSwitchOverAlarmReset_Type(Integer32):
    """Custom type xfRLTTxSwitchOverAlarmReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("txSwitchOverAlarmNoReset", 2),
          ("txSwitchOverAlarmReset", 3))
    )


_XfRLTTxSwitchOverAlarmReset_Type.__name__ = "Integer32"
_XfRLTTxSwitchOverAlarmReset_Object = MibTableColumn
xfRLTTxSwitchOverAlarmReset = _XfRLTTxSwitchOverAlarmReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 14, 1, 9),
    _XfRLTTxSwitchOverAlarmReset_Type()
)
xfRLTTxSwitchOverAlarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLTTxSwitchOverAlarmReset.setStatus("current")


class _XfRLTNumOfRLPSwitch_Type(Integer32):
    """Custom type xfRLTNumOfRLPSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XfRLTNumOfRLPSwitch_Type.__name__ = "Integer32"
_XfRLTNumOfRLPSwitch_Object = MibTableColumn
xfRLTNumOfRLPSwitch = _XfRLTNumOfRLPSwitch_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 14, 1, 10),
    _XfRLTNumOfRLPSwitch_Type()
)
xfRLTNumOfRLPSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTNumOfRLPSwitch.setStatus("current")


class _XfRLTEnhancedACMProtectionMode_Type(Integer32):
    """Custom type xfRLTEnhancedACMProtectionMode based on Integer32"""
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
        *(("other", 1),
          ("activeTransmitter", 2),
          ("maximumCapacity", 3),
          ("maximumProtection", 4))
    )


_XfRLTEnhancedACMProtectionMode_Type.__name__ = "Integer32"
_XfRLTEnhancedACMProtectionMode_Object = MibTableColumn
xfRLTEnhancedACMProtectionMode = _XfRLTEnhancedACMProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 14, 1, 11),
    _XfRLTEnhancedACMProtectionMode_Type()
)
xfRLTEnhancedACMProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLTEnhancedACMProtectionMode.setStatus("current")


class _XfRLTEnhancedACMProtectionOperStatus_Type(Integer32):
    """Custom type xfRLTEnhancedACMProtectionOperStatus based on Integer32"""
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
        *(("other", 1),
          ("notApplicable", 2),
          ("enhAcmProtActive", 3),
          ("enhAcmProtNotActive", 4))
    )


_XfRLTEnhancedACMProtectionOperStatus_Type.__name__ = "Integer32"
_XfRLTEnhancedACMProtectionOperStatus_Object = MibTableColumn
xfRLTEnhancedACMProtectionOperStatus = _XfRLTEnhancedACMProtectionOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 14, 1, 12),
    _XfRLTEnhancedACMProtectionOperStatus_Type()
)
xfRLTEnhancedACMProtectionOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTEnhancedACMProtectionOperStatus.setStatus("current")
_XfRLTEncryptionTable_Object = MibTable
xfRLTEncryptionTable = _XfRLTEncryptionTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 15)
)
if mibBuilder.loadTexts:
    xfRLTEncryptionTable.setStatus("current")
_XfRLTEncryptionEntry_Object = MibTableRow
xfRLTEncryptionEntry = _XfRLTEncryptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 15, 1)
)
xfRLTEncryptionEntry.setIndexNames(
    (0, "XF-RADIOLINK-RLT-MIB", "xfRLTEncryptionIndex"),
)
if mibBuilder.loadTexts:
    xfRLTEncryptionEntry.setStatus("current")


class _XfRLTEncryptionIndex_Type(Integer32):
    """Custom type xfRLTEncryptionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_XfRLTEncryptionIndex_Type.__name__ = "Integer32"
_XfRLTEncryptionIndex_Object = MibTableColumn
xfRLTEncryptionIndex = _XfRLTEncryptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 15, 1, 1),
    _XfRLTEncryptionIndex_Type()
)
xfRLTEncryptionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTEncryptionIndex.setStatus("current")


class _XfRLTEncryptionAdminStatus_Type(Integer32):
    """Custom type xfRLTEncryptionAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enable", 2),
          ("disable", 3))
    )


_XfRLTEncryptionAdminStatus_Type.__name__ = "Integer32"
_XfRLTEncryptionAdminStatus_Object = MibTableColumn
xfRLTEncryptionAdminStatus = _XfRLTEncryptionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 15, 1, 2),
    _XfRLTEncryptionAdminStatus_Type()
)
xfRLTEncryptionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLTEncryptionAdminStatus.setStatus("current")


class _XfRLTEncryptionOperStatus_Type(Integer32):
    """Custom type xfRLTEncryptionOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("up", 2),
          ("down", 3))
    )


_XfRLTEncryptionOperStatus_Type.__name__ = "Integer32"
_XfRLTEncryptionOperStatus_Object = MibTableColumn
xfRLTEncryptionOperStatus = _XfRLTEncryptionOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 15, 1, 3),
    _XfRLTEncryptionOperStatus_Type()
)
xfRLTEncryptionOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLTEncryptionOperStatus.setStatus("current")


class _XfRLTEncryptionMasterKey_Type(DisplayString):
    """Custom type xfRLTEncryptionMasterKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_XfRLTEncryptionMasterKey_Type.__name__ = "DisplayString"
_XfRLTEncryptionMasterKey_Object = MibTableColumn
xfRLTEncryptionMasterKey = _XfRLTEncryptionMasterKey_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 1, 15, 1, 4),
    _XfRLTEncryptionMasterKey_Type()
)
xfRLTEncryptionMasterKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLTEncryptionMasterKey.setStatus("current")
_XfRadioLinkRltPmObjects_ObjectIdentity = ObjectIdentity
xfRadioLinkRltPmObjects = _XfRadioLinkRltPmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2)
)
_XfRLPMContinuousCounterTable_Object = MibTable
xfRLPMContinuousCounterTable = _XfRLPMContinuousCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 1)
)
if mibBuilder.loadTexts:
    xfRLPMContinuousCounterTable.setStatus("current")
_XfRLPMContinuousCounterEntry_Object = MibTableRow
xfRLPMContinuousCounterEntry = _XfRLPMContinuousCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 1, 1)
)
xfRLPMContinuousCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMContinuousCounterEntry.setStatus("current")
_XfPMTimeElapsed_Type = PerfIntervalCount
_XfPMTimeElapsed_Object = MibTableColumn
xfPMTimeElapsed = _XfPMTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 1, 1, 1),
    _XfPMTimeElapsed_Type()
)
xfPMTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMTimeElapsed.setStatus("current")
_XfPMCurrentES_Type = PerfCurrentCount
_XfPMCurrentES_Object = MibTableColumn
xfPMCurrentES = _XfPMCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 1, 1, 2),
    _XfPMCurrentES_Type()
)
xfPMCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrentES.setStatus("current")
_XfPMCurrentSES_Type = PerfCurrentCount
_XfPMCurrentSES_Object = MibTableColumn
xfPMCurrentSES = _XfPMCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 1, 1, 3),
    _XfPMCurrentSES_Type()
)
xfPMCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrentSES.setStatus("current")
_XfPMCurrentBBE_Type = HCPerfCurrentCount
_XfPMCurrentBBE_Object = MibTableColumn
xfPMCurrentBBE = _XfPMCurrentBBE_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 1, 1, 4),
    _XfPMCurrentBBE_Type()
)
xfPMCurrentBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrentBBE.setStatus("current")
_XfPMCurrentUAS_Type = PerfCurrentCount
_XfPMCurrentUAS_Object = MibTableColumn
xfPMCurrentUAS = _XfPMCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 1, 1, 5),
    _XfPMCurrentUAS_Type()
)
xfPMCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrentUAS.setStatus("current")
_XfPMCurrentBB_Type = HCPerfCurrentCount
_XfPMCurrentBB_Object = MibTableColumn
xfPMCurrentBB = _XfPMCurrentBB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 1, 1, 6),
    _XfPMCurrentBB_Type()
)
xfPMCurrentBB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrentBB.setStatus("current")


class _XfPMPerfReset_Type(Integer32):
    """Custom type xfPMPerfReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("noReset", 2),
          ("reset", 3))
    )


_XfPMPerfReset_Type.__name__ = "Integer32"
_XfPMPerfReset_Object = MibTableColumn
xfPMPerfReset = _XfPMPerfReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 1, 1, 7),
    _XfPMPerfReset_Type()
)
xfPMPerfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMPerfReset.setStatus("current")
_XfPMCurrentESR_Type = PerfCurrentCount
_XfPMCurrentESR_Object = MibTableColumn
xfPMCurrentESR = _XfPMCurrentESR_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 1, 1, 8),
    _XfPMCurrentESR_Type()
)
xfPMCurrentESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrentESR.setStatus("current")
_XfPMCurrentSESR_Type = PerfCurrentCount
_XfPMCurrentSESR_Object = MibTableColumn
xfPMCurrentSESR = _XfPMCurrentSESR_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 1, 1, 9),
    _XfPMCurrentSESR_Type()
)
xfPMCurrentSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrentSESR.setStatus("current")
_XfPMCurrentBBER_Type = HCPerfCurrentCount
_XfPMCurrentBBER_Object = MibTableColumn
xfPMCurrentBBER = _XfPMCurrentBBER_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 1, 1, 10),
    _XfPMCurrentBBER_Type()
)
xfPMCurrentBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrentBBER.setStatus("current")
_XfRLPMACMConfigTable_Object = MibTable
xfRLPMACMConfigTable = _XfRLPMACMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 2)
)
if mibBuilder.loadTexts:
    xfRLPMACMConfigTable.setStatus("current")
_XfRLPMACMConfigEntry_Object = MibTableRow
xfRLPMACMConfigEntry = _XfRLPMACMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 2, 1)
)
xfRLPMACMConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMACMConfigEntry.setStatus("current")
_XfPMACMSetThreshold15m_Type = Integer32
_XfPMACMSetThreshold15m_Object = MibTableColumn
xfPMACMSetThreshold15m = _XfPMACMSetThreshold15m_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 2, 1, 1),
    _XfPMACMSetThreshold15m_Type()
)
xfPMACMSetThreshold15m.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMACMSetThreshold15m.setStatus("current")
_XfPMACMSetThreshold24h_Type = Integer32
_XfPMACMSetThreshold24h_Object = MibTableColumn
xfPMACMSetThreshold24h = _XfPMACMSetThreshold24h_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 2, 1, 2),
    _XfPMACMSetThreshold24h_Type()
)
xfPMACMSetThreshold24h.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMACMSetThreshold24h.setStatus("current")
_XfPMACMResetThreshold15m_Type = Integer32
_XfPMACMResetThreshold15m_Object = MibTableColumn
xfPMACMResetThreshold15m = _XfPMACMResetThreshold15m_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 2, 1, 3),
    _XfPMACMResetThreshold15m_Type()
)
xfPMACMResetThreshold15m.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMACMResetThreshold15m.setStatus("current")


class _XfPMACMStatus_Type(Bits):
    """Custom type xfPMACMStatus based on Bits"""
    namedValues = NamedValues(
        *(("acm15m0", 0),
          ("acm15m1", 1),
          ("acm15m2", 2),
          ("acm24h0", 3),
          ("acm24h1", 4),
          ("acm24h2", 5))
    )

_XfPMACMStatus_Type.__name__ = "Bits"
_XfPMACMStatus_Object = MibTableColumn
xfPMACMStatus = _XfPMACMStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 2, 1, 4),
    _XfPMACMStatus_Type()
)
xfPMACMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMStatus.setStatus("current")


class _XfPMACMValidData_Type(Bits):
    """Custom type xfPMACMValidData based on Bits"""
    namedValues = NamedValues(
        *(("valid15m4QAMStrong", 0),
          ("valid15m4QAMStd", 1),
          ("valid15m4QAMLight", 2),
          ("valid15m16QAMStrong", 3),
          ("valid15m16QAMStd", 4),
          ("valid15m16QAMLight", 5),
          ("valid15m32QAMStrong", 6),
          ("valid15m32QAMStd", 7),
          ("valid15m32QAMLight", 8),
          ("valid15m64QAMStrong", 9),
          ("valid15m64QAMStd", 10),
          ("valid15m64QAMLight", 11),
          ("valid15m128QAMStrong", 12),
          ("valid15m128QAMStd", 13),
          ("valid15m128QAMLight", 14),
          ("valid15m256QAMStrong", 15),
          ("valid15m256QAMStd", 16),
          ("valid15m256QAMLight", 17),
          ("valid15m512QAMStrong", 18),
          ("valid15m512QAMStd", 19),
          ("valid15m512QAMLight", 20),
          ("valid15m1024QAMStrong", 21),
          ("valid15m1024QAMStd", 22),
          ("valid15m1024QAMLight", 23),
          ("valid15m2048QAMStrong", 24),
          ("valid15m2048QAMStd", 25),
          ("valid15m2048QAMLight", 26),
          ("valid15m4096QAMStrong", 27),
          ("valid15m4096QAMStd", 28),
          ("valid15m4096QAMLight", 29),
          ("valid15m8192QAMStrong", 30),
          ("valid15m8192QAMStd", 31),
          ("valid15m8192QAMLight", 32),
          ("valid15m16384QAMStrong", 33),
          ("valid15m16384QAMStd", 34),
          ("valid15m16384QAMLight", 35))
    )

_XfPMACMValidData_Type.__name__ = "Bits"
_XfPMACMValidData_Object = MibTableColumn
xfPMACMValidData = _XfPMACMValidData_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 2, 1, 5),
    _XfPMACMValidData_Type()
)
xfPMACMValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMValidData.setStatus("current")
_XfRLPMACMCurrent24hTable_Object = MibTable
xfRLPMACMCurrent24hTable = _XfRLPMACMCurrent24hTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3)
)
if mibBuilder.loadTexts:
    xfRLPMACMCurrent24hTable.setStatus("current")
_XfRLPMACMCurrent24hEntry_Object = MibTableRow
xfRLPMACMCurrent24hEntry = _XfRLPMACMCurrent24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1)
)
xfRLPMACMCurrent24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMACMCurrent24hEntry.setStatus("current")
_XfPMACMCurrent24h4QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent24h4QAMStrong_Object = MibTableColumn
xfPMACMCurrent24h4QAMStrong = _XfPMACMCurrent24h4QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 1),
    _XfPMACMCurrent24h4QAMStrong_Type()
)
xfPMACMCurrent24h4QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h4QAMStrong.setStatus("current")
_XfPMACMCurrent24h4QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent24h4QAMStd_Object = MibTableColumn
xfPMACMCurrent24h4QAMStd = _XfPMACMCurrent24h4QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 2),
    _XfPMACMCurrent24h4QAMStd_Type()
)
xfPMACMCurrent24h4QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h4QAMStd.setStatus("current")
_XfPMACMCurrent24h4QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent24h4QAMLight_Object = MibTableColumn
xfPMACMCurrent24h4QAMLight = _XfPMACMCurrent24h4QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 3),
    _XfPMACMCurrent24h4QAMLight_Type()
)
xfPMACMCurrent24h4QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h4QAMLight.setStatus("current")
_XfPMACMCurrent24h16QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent24h16QAMStrong_Object = MibTableColumn
xfPMACMCurrent24h16QAMStrong = _XfPMACMCurrent24h16QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 4),
    _XfPMACMCurrent24h16QAMStrong_Type()
)
xfPMACMCurrent24h16QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h16QAMStrong.setStatus("current")
_XfPMACMCurrent24h16QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent24h16QAMStd_Object = MibTableColumn
xfPMACMCurrent24h16QAMStd = _XfPMACMCurrent24h16QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 5),
    _XfPMACMCurrent24h16QAMStd_Type()
)
xfPMACMCurrent24h16QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h16QAMStd.setStatus("current")
_XfPMACMCurrent24h16QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent24h16QAMLight_Object = MibTableColumn
xfPMACMCurrent24h16QAMLight = _XfPMACMCurrent24h16QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 6),
    _XfPMACMCurrent24h16QAMLight_Type()
)
xfPMACMCurrent24h16QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h16QAMLight.setStatus("current")
_XfPMACMCurrent24h32QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent24h32QAMStrong_Object = MibTableColumn
xfPMACMCurrent24h32QAMStrong = _XfPMACMCurrent24h32QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 7),
    _XfPMACMCurrent24h32QAMStrong_Type()
)
xfPMACMCurrent24h32QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h32QAMStrong.setStatus("current")
_XfPMACMCurrent24h32QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent24h32QAMStd_Object = MibTableColumn
xfPMACMCurrent24h32QAMStd = _XfPMACMCurrent24h32QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 8),
    _XfPMACMCurrent24h32QAMStd_Type()
)
xfPMACMCurrent24h32QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h32QAMStd.setStatus("current")
_XfPMACMCurrent24h32QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent24h32QAMLight_Object = MibTableColumn
xfPMACMCurrent24h32QAMLight = _XfPMACMCurrent24h32QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 9),
    _XfPMACMCurrent24h32QAMLight_Type()
)
xfPMACMCurrent24h32QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h32QAMLight.setStatus("current")
_XfPMACMCurrent24h64QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent24h64QAMStrong_Object = MibTableColumn
xfPMACMCurrent24h64QAMStrong = _XfPMACMCurrent24h64QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 10),
    _XfPMACMCurrent24h64QAMStrong_Type()
)
xfPMACMCurrent24h64QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h64QAMStrong.setStatus("current")
_XfPMACMCurrent24h64QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent24h64QAMStd_Object = MibTableColumn
xfPMACMCurrent24h64QAMStd = _XfPMACMCurrent24h64QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 11),
    _XfPMACMCurrent24h64QAMStd_Type()
)
xfPMACMCurrent24h64QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h64QAMStd.setStatus("current")
_XfPMACMCurrent24h64QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent24h64QAMLight_Object = MibTableColumn
xfPMACMCurrent24h64QAMLight = _XfPMACMCurrent24h64QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 12),
    _XfPMACMCurrent24h64QAMLight_Type()
)
xfPMACMCurrent24h64QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h64QAMLight.setStatus("current")
_XfPMACMCurrent24h128QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent24h128QAMStrong_Object = MibTableColumn
xfPMACMCurrent24h128QAMStrong = _XfPMACMCurrent24h128QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 13),
    _XfPMACMCurrent24h128QAMStrong_Type()
)
xfPMACMCurrent24h128QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h128QAMStrong.setStatus("current")
_XfPMACMCurrent24h128QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent24h128QAMStd_Object = MibTableColumn
xfPMACMCurrent24h128QAMStd = _XfPMACMCurrent24h128QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 14),
    _XfPMACMCurrent24h128QAMStd_Type()
)
xfPMACMCurrent24h128QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h128QAMStd.setStatus("current")
_XfPMACMCurrent24h128QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent24h128QAMLight_Object = MibTableColumn
xfPMACMCurrent24h128QAMLight = _XfPMACMCurrent24h128QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 15),
    _XfPMACMCurrent24h128QAMLight_Type()
)
xfPMACMCurrent24h128QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h128QAMLight.setStatus("current")
_XfPMACMCurrent24h256QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent24h256QAMStrong_Object = MibTableColumn
xfPMACMCurrent24h256QAMStrong = _XfPMACMCurrent24h256QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 16),
    _XfPMACMCurrent24h256QAMStrong_Type()
)
xfPMACMCurrent24h256QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h256QAMStrong.setStatus("current")
_XfPMACMCurrent24h256QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent24h256QAMStd_Object = MibTableColumn
xfPMACMCurrent24h256QAMStd = _XfPMACMCurrent24h256QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 17),
    _XfPMACMCurrent24h256QAMStd_Type()
)
xfPMACMCurrent24h256QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h256QAMStd.setStatus("current")
_XfPMACMCurrent24h256QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent24h256QAMLight_Object = MibTableColumn
xfPMACMCurrent24h256QAMLight = _XfPMACMCurrent24h256QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 18),
    _XfPMACMCurrent24h256QAMLight_Type()
)
xfPMACMCurrent24h256QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h256QAMLight.setStatus("current")
_XfPMACMCurrent24h512QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent24h512QAMStrong_Object = MibTableColumn
xfPMACMCurrent24h512QAMStrong = _XfPMACMCurrent24h512QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 19),
    _XfPMACMCurrent24h512QAMStrong_Type()
)
xfPMACMCurrent24h512QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h512QAMStrong.setStatus("current")
_XfPMACMCurrent24h512QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent24h512QAMStd_Object = MibTableColumn
xfPMACMCurrent24h512QAMStd = _XfPMACMCurrent24h512QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 20),
    _XfPMACMCurrent24h512QAMStd_Type()
)
xfPMACMCurrent24h512QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h512QAMStd.setStatus("current")
_XfPMACMCurrent24h512QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent24h512QAMLight_Object = MibTableColumn
xfPMACMCurrent24h512QAMLight = _XfPMACMCurrent24h512QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 21),
    _XfPMACMCurrent24h512QAMLight_Type()
)
xfPMACMCurrent24h512QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h512QAMLight.setStatus("current")
_XfPMACMCurrent24h1024QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent24h1024QAMStrong_Object = MibTableColumn
xfPMACMCurrent24h1024QAMStrong = _XfPMACMCurrent24h1024QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 22),
    _XfPMACMCurrent24h1024QAMStrong_Type()
)
xfPMACMCurrent24h1024QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h1024QAMStrong.setStatus("current")
_XfPMACMCurrent24h1024QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent24h1024QAMStd_Object = MibTableColumn
xfPMACMCurrent24h1024QAMStd = _XfPMACMCurrent24h1024QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 23),
    _XfPMACMCurrent24h1024QAMStd_Type()
)
xfPMACMCurrent24h1024QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h1024QAMStd.setStatus("current")
_XfPMACMCurrent24h1024QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent24h1024QAMLight_Object = MibTableColumn
xfPMACMCurrent24h1024QAMLight = _XfPMACMCurrent24h1024QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 24),
    _XfPMACMCurrent24h1024QAMLight_Type()
)
xfPMACMCurrent24h1024QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h1024QAMLight.setStatus("current")
_XfPMACMCurrent24h2048QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent24h2048QAMStrong_Object = MibTableColumn
xfPMACMCurrent24h2048QAMStrong = _XfPMACMCurrent24h2048QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 25),
    _XfPMACMCurrent24h2048QAMStrong_Type()
)
xfPMACMCurrent24h2048QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h2048QAMStrong.setStatus("current")
_XfPMACMCurrent24h2048QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent24h2048QAMStd_Object = MibTableColumn
xfPMACMCurrent24h2048QAMStd = _XfPMACMCurrent24h2048QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 26),
    _XfPMACMCurrent24h2048QAMStd_Type()
)
xfPMACMCurrent24h2048QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h2048QAMStd.setStatus("current")
_XfPMACMCurrent24h2048QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent24h2048QAMLight_Object = MibTableColumn
xfPMACMCurrent24h2048QAMLight = _XfPMACMCurrent24h2048QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 27),
    _XfPMACMCurrent24h2048QAMLight_Type()
)
xfPMACMCurrent24h2048QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h2048QAMLight.setStatus("current")
_XfPMACMCurrent24h4096QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent24h4096QAMStrong_Object = MibTableColumn
xfPMACMCurrent24h4096QAMStrong = _XfPMACMCurrent24h4096QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 28),
    _XfPMACMCurrent24h4096QAMStrong_Type()
)
xfPMACMCurrent24h4096QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h4096QAMStrong.setStatus("current")
_XfPMACMCurrent24h4096QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent24h4096QAMStd_Object = MibTableColumn
xfPMACMCurrent24h4096QAMStd = _XfPMACMCurrent24h4096QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 29),
    _XfPMACMCurrent24h4096QAMStd_Type()
)
xfPMACMCurrent24h4096QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h4096QAMStd.setStatus("current")
_XfPMACMCurrent24h4096QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent24h4096QAMLight_Object = MibTableColumn
xfPMACMCurrent24h4096QAMLight = _XfPMACMCurrent24h4096QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 30),
    _XfPMACMCurrent24h4096QAMLight_Type()
)
xfPMACMCurrent24h4096QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h4096QAMLight.setStatus("current")
_XfPMACMCurrent24h8192QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent24h8192QAMStrong_Object = MibTableColumn
xfPMACMCurrent24h8192QAMStrong = _XfPMACMCurrent24h8192QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 31),
    _XfPMACMCurrent24h8192QAMStrong_Type()
)
xfPMACMCurrent24h8192QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h8192QAMStrong.setStatus("current")
_XfPMACMCurrent24h8192QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent24h8192QAMStd_Object = MibTableColumn
xfPMACMCurrent24h8192QAMStd = _XfPMACMCurrent24h8192QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 32),
    _XfPMACMCurrent24h8192QAMStd_Type()
)
xfPMACMCurrent24h8192QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h8192QAMStd.setStatus("current")
_XfPMACMCurrent24h8192QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent24h8192QAMLight_Object = MibTableColumn
xfPMACMCurrent24h8192QAMLight = _XfPMACMCurrent24h8192QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 33),
    _XfPMACMCurrent24h8192QAMLight_Type()
)
xfPMACMCurrent24h8192QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h8192QAMLight.setStatus("current")
_XfPMACMCurrent24h16384QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent24h16384QAMStrong_Object = MibTableColumn
xfPMACMCurrent24h16384QAMStrong = _XfPMACMCurrent24h16384QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 34),
    _XfPMACMCurrent24h16384QAMStrong_Type()
)
xfPMACMCurrent24h16384QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h16384QAMStrong.setStatus("current")
_XfPMACMCurrent24h16384QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent24h16384QAMStd_Object = MibTableColumn
xfPMACMCurrent24h16384QAMStd = _XfPMACMCurrent24h16384QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 35),
    _XfPMACMCurrent24h16384QAMStd_Type()
)
xfPMACMCurrent24h16384QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h16384QAMStd.setStatus("current")
_XfPMACMCurrent24h16384QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent24h16384QAMLight_Object = MibTableColumn
xfPMACMCurrent24h16384QAMLight = _XfPMACMCurrent24h16384QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 3, 1, 36),
    _XfPMACMCurrent24h16384QAMLight_Type()
)
xfPMACMCurrent24h16384QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent24h16384QAMLight.setStatus("current")
_XfRLPMACMInterval24hTable_Object = MibTable
xfRLPMACMInterval24hTable = _XfRLPMACMInterval24hTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4)
)
if mibBuilder.loadTexts:
    xfRLPMACMInterval24hTable.setStatus("current")
_XfRLPMACMInterval24hEntry_Object = MibTableRow
xfRLPMACMInterval24hEntry = _XfRLPMACMInterval24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1)
)
xfRLPMACMInterval24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMACMInterval24hEntry.setStatus("current")
_XfPMACMInterval24h4QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval24h4QAMStrong_Object = MibTableColumn
xfPMACMInterval24h4QAMStrong = _XfPMACMInterval24h4QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 1),
    _XfPMACMInterval24h4QAMStrong_Type()
)
xfPMACMInterval24h4QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h4QAMStrong.setStatus("current")
_XfPMACMInterval24h4QAMStd_Type = PerfIntervalCount
_XfPMACMInterval24h4QAMStd_Object = MibTableColumn
xfPMACMInterval24h4QAMStd = _XfPMACMInterval24h4QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 2),
    _XfPMACMInterval24h4QAMStd_Type()
)
xfPMACMInterval24h4QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h4QAMStd.setStatus("current")
_XfPMACMInterval24h4QAMLight_Type = PerfIntervalCount
_XfPMACMInterval24h4QAMLight_Object = MibTableColumn
xfPMACMInterval24h4QAMLight = _XfPMACMInterval24h4QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 3),
    _XfPMACMInterval24h4QAMLight_Type()
)
xfPMACMInterval24h4QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h4QAMLight.setStatus("current")
_XfPMACMInterval24h16QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval24h16QAMStrong_Object = MibTableColumn
xfPMACMInterval24h16QAMStrong = _XfPMACMInterval24h16QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 4),
    _XfPMACMInterval24h16QAMStrong_Type()
)
xfPMACMInterval24h16QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h16QAMStrong.setStatus("current")
_XfPMACMInterval24h16QAMStd_Type = PerfIntervalCount
_XfPMACMInterval24h16QAMStd_Object = MibTableColumn
xfPMACMInterval24h16QAMStd = _XfPMACMInterval24h16QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 5),
    _XfPMACMInterval24h16QAMStd_Type()
)
xfPMACMInterval24h16QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h16QAMStd.setStatus("current")
_XfPMACMInterval24h16QAMLight_Type = PerfIntervalCount
_XfPMACMInterval24h16QAMLight_Object = MibTableColumn
xfPMACMInterval24h16QAMLight = _XfPMACMInterval24h16QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 6),
    _XfPMACMInterval24h16QAMLight_Type()
)
xfPMACMInterval24h16QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h16QAMLight.setStatus("current")
_XfPMACMInterval24h32QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval24h32QAMStrong_Object = MibTableColumn
xfPMACMInterval24h32QAMStrong = _XfPMACMInterval24h32QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 7),
    _XfPMACMInterval24h32QAMStrong_Type()
)
xfPMACMInterval24h32QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h32QAMStrong.setStatus("current")
_XfPMACMInterval24h32QAMStd_Type = PerfIntervalCount
_XfPMACMInterval24h32QAMStd_Object = MibTableColumn
xfPMACMInterval24h32QAMStd = _XfPMACMInterval24h32QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 8),
    _XfPMACMInterval24h32QAMStd_Type()
)
xfPMACMInterval24h32QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h32QAMStd.setStatus("current")
_XfPMACMInterval24h32QAMLight_Type = PerfIntervalCount
_XfPMACMInterval24h32QAMLight_Object = MibTableColumn
xfPMACMInterval24h32QAMLight = _XfPMACMInterval24h32QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 9),
    _XfPMACMInterval24h32QAMLight_Type()
)
xfPMACMInterval24h32QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h32QAMLight.setStatus("current")
_XfPMACMInterval24h64QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval24h64QAMStrong_Object = MibTableColumn
xfPMACMInterval24h64QAMStrong = _XfPMACMInterval24h64QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 10),
    _XfPMACMInterval24h64QAMStrong_Type()
)
xfPMACMInterval24h64QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h64QAMStrong.setStatus("current")
_XfPMACMInterval24h64QAMStd_Type = PerfIntervalCount
_XfPMACMInterval24h64QAMStd_Object = MibTableColumn
xfPMACMInterval24h64QAMStd = _XfPMACMInterval24h64QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 11),
    _XfPMACMInterval24h64QAMStd_Type()
)
xfPMACMInterval24h64QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h64QAMStd.setStatus("current")
_XfPMACMInterval24h64QAMLight_Type = PerfIntervalCount
_XfPMACMInterval24h64QAMLight_Object = MibTableColumn
xfPMACMInterval24h64QAMLight = _XfPMACMInterval24h64QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 12),
    _XfPMACMInterval24h64QAMLight_Type()
)
xfPMACMInterval24h64QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h64QAMLight.setStatus("current")
_XfPMACMInterval24h128QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval24h128QAMStrong_Object = MibTableColumn
xfPMACMInterval24h128QAMStrong = _XfPMACMInterval24h128QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 13),
    _XfPMACMInterval24h128QAMStrong_Type()
)
xfPMACMInterval24h128QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h128QAMStrong.setStatus("current")
_XfPMACMInterval24h128QAMStd_Type = PerfIntervalCount
_XfPMACMInterval24h128QAMStd_Object = MibTableColumn
xfPMACMInterval24h128QAMStd = _XfPMACMInterval24h128QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 14),
    _XfPMACMInterval24h128QAMStd_Type()
)
xfPMACMInterval24h128QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h128QAMStd.setStatus("current")
_XfPMACMInterval24h128QAMLight_Type = PerfIntervalCount
_XfPMACMInterval24h128QAMLight_Object = MibTableColumn
xfPMACMInterval24h128QAMLight = _XfPMACMInterval24h128QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 15),
    _XfPMACMInterval24h128QAMLight_Type()
)
xfPMACMInterval24h128QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h128QAMLight.setStatus("current")
_XfPMACMInterval24h256QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval24h256QAMStrong_Object = MibTableColumn
xfPMACMInterval24h256QAMStrong = _XfPMACMInterval24h256QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 16),
    _XfPMACMInterval24h256QAMStrong_Type()
)
xfPMACMInterval24h256QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h256QAMStrong.setStatus("current")
_XfPMACMInterval24h256QAMStd_Type = PerfIntervalCount
_XfPMACMInterval24h256QAMStd_Object = MibTableColumn
xfPMACMInterval24h256QAMStd = _XfPMACMInterval24h256QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 17),
    _XfPMACMInterval24h256QAMStd_Type()
)
xfPMACMInterval24h256QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h256QAMStd.setStatus("current")
_XfPMACMInterval24h256QAMLight_Type = PerfIntervalCount
_XfPMACMInterval24h256QAMLight_Object = MibTableColumn
xfPMACMInterval24h256QAMLight = _XfPMACMInterval24h256QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 18),
    _XfPMACMInterval24h256QAMLight_Type()
)
xfPMACMInterval24h256QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h256QAMLight.setStatus("current")
_XfPMACMInterval24h512QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval24h512QAMStrong_Object = MibTableColumn
xfPMACMInterval24h512QAMStrong = _XfPMACMInterval24h512QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 19),
    _XfPMACMInterval24h512QAMStrong_Type()
)
xfPMACMInterval24h512QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h512QAMStrong.setStatus("current")
_XfPMACMInterval24h512QAMStd_Type = PerfIntervalCount
_XfPMACMInterval24h512QAMStd_Object = MibTableColumn
xfPMACMInterval24h512QAMStd = _XfPMACMInterval24h512QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 20),
    _XfPMACMInterval24h512QAMStd_Type()
)
xfPMACMInterval24h512QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h512QAMStd.setStatus("current")
_XfPMACMInterval24h512QAMLight_Type = PerfIntervalCount
_XfPMACMInterval24h512QAMLight_Object = MibTableColumn
xfPMACMInterval24h512QAMLight = _XfPMACMInterval24h512QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 21),
    _XfPMACMInterval24h512QAMLight_Type()
)
xfPMACMInterval24h512QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h512QAMLight.setStatus("current")
_XfPMACMInterval24h1024QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval24h1024QAMStrong_Object = MibTableColumn
xfPMACMInterval24h1024QAMStrong = _XfPMACMInterval24h1024QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 22),
    _XfPMACMInterval24h1024QAMStrong_Type()
)
xfPMACMInterval24h1024QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h1024QAMStrong.setStatus("current")
_XfPMACMInterval24h1024QAMStd_Type = PerfIntervalCount
_XfPMACMInterval24h1024QAMStd_Object = MibTableColumn
xfPMACMInterval24h1024QAMStd = _XfPMACMInterval24h1024QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 23),
    _XfPMACMInterval24h1024QAMStd_Type()
)
xfPMACMInterval24h1024QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h1024QAMStd.setStatus("current")
_XfPMACMInterval24h1024QAMLight_Type = PerfIntervalCount
_XfPMACMInterval24h1024QAMLight_Object = MibTableColumn
xfPMACMInterval24h1024QAMLight = _XfPMACMInterval24h1024QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 24),
    _XfPMACMInterval24h1024QAMLight_Type()
)
xfPMACMInterval24h1024QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h1024QAMLight.setStatus("current")
_XfPMACMInterval24h2048QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval24h2048QAMStrong_Object = MibTableColumn
xfPMACMInterval24h2048QAMStrong = _XfPMACMInterval24h2048QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 25),
    _XfPMACMInterval24h2048QAMStrong_Type()
)
xfPMACMInterval24h2048QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h2048QAMStrong.setStatus("current")
_XfPMACMInterval24h2048QAMStd_Type = PerfIntervalCount
_XfPMACMInterval24h2048QAMStd_Object = MibTableColumn
xfPMACMInterval24h2048QAMStd = _XfPMACMInterval24h2048QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 26),
    _XfPMACMInterval24h2048QAMStd_Type()
)
xfPMACMInterval24h2048QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h2048QAMStd.setStatus("current")
_XfPMACMInterval24h2048QAMLight_Type = PerfIntervalCount
_XfPMACMInterval24h2048QAMLight_Object = MibTableColumn
xfPMACMInterval24h2048QAMLight = _XfPMACMInterval24h2048QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 27),
    _XfPMACMInterval24h2048QAMLight_Type()
)
xfPMACMInterval24h2048QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h2048QAMLight.setStatus("current")
_XfPMACMInterval24h4096QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval24h4096QAMStrong_Object = MibTableColumn
xfPMACMInterval24h4096QAMStrong = _XfPMACMInterval24h4096QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 28),
    _XfPMACMInterval24h4096QAMStrong_Type()
)
xfPMACMInterval24h4096QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h4096QAMStrong.setStatus("current")
_XfPMACMInterval24h4096QAMStd_Type = PerfIntervalCount
_XfPMACMInterval24h4096QAMStd_Object = MibTableColumn
xfPMACMInterval24h4096QAMStd = _XfPMACMInterval24h4096QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 29),
    _XfPMACMInterval24h4096QAMStd_Type()
)
xfPMACMInterval24h4096QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h4096QAMStd.setStatus("current")
_XfPMACMInterval24h4096QAMLight_Type = PerfIntervalCount
_XfPMACMInterval24h4096QAMLight_Object = MibTableColumn
xfPMACMInterval24h4096QAMLight = _XfPMACMInterval24h4096QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 30),
    _XfPMACMInterval24h4096QAMLight_Type()
)
xfPMACMInterval24h4096QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h4096QAMLight.setStatus("current")
_XfPMACMInterval24hValidData_Type = TruthValue
_XfPMACMInterval24hValidData_Object = MibTableColumn
xfPMACMInterval24hValidData = _XfPMACMInterval24hValidData_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 31),
    _XfPMACMInterval24hValidData_Type()
)
xfPMACMInterval24hValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24hValidData.setStatus("current")
_XfPMACMInterval24h8192QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval24h8192QAMStrong_Object = MibTableColumn
xfPMACMInterval24h8192QAMStrong = _XfPMACMInterval24h8192QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 32),
    _XfPMACMInterval24h8192QAMStrong_Type()
)
xfPMACMInterval24h8192QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h8192QAMStrong.setStatus("current")
_XfPMACMInterval24h8192QAMStd_Type = PerfIntervalCount
_XfPMACMInterval24h8192QAMStd_Object = MibTableColumn
xfPMACMInterval24h8192QAMStd = _XfPMACMInterval24h8192QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 33),
    _XfPMACMInterval24h8192QAMStd_Type()
)
xfPMACMInterval24h8192QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h8192QAMStd.setStatus("current")
_XfPMACMInterval24h8192QAMLight_Type = PerfIntervalCount
_XfPMACMInterval24h8192QAMLight_Object = MibTableColumn
xfPMACMInterval24h8192QAMLight = _XfPMACMInterval24h8192QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 34),
    _XfPMACMInterval24h8192QAMLight_Type()
)
xfPMACMInterval24h8192QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h8192QAMLight.setStatus("current")
_XfPMACMInterval24h16384QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval24h16384QAMStrong_Object = MibTableColumn
xfPMACMInterval24h16384QAMStrong = _XfPMACMInterval24h16384QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 35),
    _XfPMACMInterval24h16384QAMStrong_Type()
)
xfPMACMInterval24h16384QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h16384QAMStrong.setStatus("current")
_XfPMACMInterval24h16384QAMStd_Type = PerfIntervalCount
_XfPMACMInterval24h16384QAMStd_Object = MibTableColumn
xfPMACMInterval24h16384QAMStd = _XfPMACMInterval24h16384QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 36),
    _XfPMACMInterval24h16384QAMStd_Type()
)
xfPMACMInterval24h16384QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h16384QAMStd.setStatus("current")
_XfPMACMInterval24h16384QAMLight_Type = PerfIntervalCount
_XfPMACMInterval24h16384QAMLight_Object = MibTableColumn
xfPMACMInterval24h16384QAMLight = _XfPMACMInterval24h16384QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 4, 1, 37),
    _XfPMACMInterval24h16384QAMLight_Type()
)
xfPMACMInterval24h16384QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval24h16384QAMLight.setStatus("current")
_XfRLPMACMCurrent15mTable_Object = MibTable
xfRLPMACMCurrent15mTable = _XfRLPMACMCurrent15mTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5)
)
if mibBuilder.loadTexts:
    xfRLPMACMCurrent15mTable.setStatus("current")
_XfRLPMACMCurrent15mEntry_Object = MibTableRow
xfRLPMACMCurrent15mEntry = _XfRLPMACMCurrent15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1)
)
xfRLPMACMCurrent15mEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMACMCurrent15mEntry.setStatus("current")
_XfPMACMCurrent15m4QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent15m4QAMStrong_Object = MibTableColumn
xfPMACMCurrent15m4QAMStrong = _XfPMACMCurrent15m4QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 1),
    _XfPMACMCurrent15m4QAMStrong_Type()
)
xfPMACMCurrent15m4QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m4QAMStrong.setStatus("current")
_XfPMACMCurrent15m4QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent15m4QAMStd_Object = MibTableColumn
xfPMACMCurrent15m4QAMStd = _XfPMACMCurrent15m4QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 2),
    _XfPMACMCurrent15m4QAMStd_Type()
)
xfPMACMCurrent15m4QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m4QAMStd.setStatus("current")
_XfPMACMCurrent15m4QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent15m4QAMLight_Object = MibTableColumn
xfPMACMCurrent15m4QAMLight = _XfPMACMCurrent15m4QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 3),
    _XfPMACMCurrent15m4QAMLight_Type()
)
xfPMACMCurrent15m4QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m4QAMLight.setStatus("current")
_XfPMACMCurrent15m16QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent15m16QAMStrong_Object = MibTableColumn
xfPMACMCurrent15m16QAMStrong = _XfPMACMCurrent15m16QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 4),
    _XfPMACMCurrent15m16QAMStrong_Type()
)
xfPMACMCurrent15m16QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m16QAMStrong.setStatus("current")
_XfPMACMCurrent15m16QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent15m16QAMStd_Object = MibTableColumn
xfPMACMCurrent15m16QAMStd = _XfPMACMCurrent15m16QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 5),
    _XfPMACMCurrent15m16QAMStd_Type()
)
xfPMACMCurrent15m16QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m16QAMStd.setStatus("current")
_XfPMACMCurrent15m16QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent15m16QAMLight_Object = MibTableColumn
xfPMACMCurrent15m16QAMLight = _XfPMACMCurrent15m16QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 6),
    _XfPMACMCurrent15m16QAMLight_Type()
)
xfPMACMCurrent15m16QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m16QAMLight.setStatus("current")
_XfPMACMCurrent15m32QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent15m32QAMStrong_Object = MibTableColumn
xfPMACMCurrent15m32QAMStrong = _XfPMACMCurrent15m32QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 7),
    _XfPMACMCurrent15m32QAMStrong_Type()
)
xfPMACMCurrent15m32QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m32QAMStrong.setStatus("current")
_XfPMACMCurrent15m32QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent15m32QAMStd_Object = MibTableColumn
xfPMACMCurrent15m32QAMStd = _XfPMACMCurrent15m32QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 8),
    _XfPMACMCurrent15m32QAMStd_Type()
)
xfPMACMCurrent15m32QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m32QAMStd.setStatus("current")
_XfPMACMCurrent15m32QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent15m32QAMLight_Object = MibTableColumn
xfPMACMCurrent15m32QAMLight = _XfPMACMCurrent15m32QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 9),
    _XfPMACMCurrent15m32QAMLight_Type()
)
xfPMACMCurrent15m32QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m32QAMLight.setStatus("current")
_XfPMACMCurrent15m64QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent15m64QAMStrong_Object = MibTableColumn
xfPMACMCurrent15m64QAMStrong = _XfPMACMCurrent15m64QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 10),
    _XfPMACMCurrent15m64QAMStrong_Type()
)
xfPMACMCurrent15m64QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m64QAMStrong.setStatus("current")
_XfPMACMCurrent15m64QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent15m64QAMStd_Object = MibTableColumn
xfPMACMCurrent15m64QAMStd = _XfPMACMCurrent15m64QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 11),
    _XfPMACMCurrent15m64QAMStd_Type()
)
xfPMACMCurrent15m64QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m64QAMStd.setStatus("current")
_XfPMACMCurrent15m64QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent15m64QAMLight_Object = MibTableColumn
xfPMACMCurrent15m64QAMLight = _XfPMACMCurrent15m64QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 12),
    _XfPMACMCurrent15m64QAMLight_Type()
)
xfPMACMCurrent15m64QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m64QAMLight.setStatus("current")
_XfPMACMCurrent15m128QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent15m128QAMStrong_Object = MibTableColumn
xfPMACMCurrent15m128QAMStrong = _XfPMACMCurrent15m128QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 13),
    _XfPMACMCurrent15m128QAMStrong_Type()
)
xfPMACMCurrent15m128QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m128QAMStrong.setStatus("current")
_XfPMACMCurrent15m128QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent15m128QAMStd_Object = MibTableColumn
xfPMACMCurrent15m128QAMStd = _XfPMACMCurrent15m128QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 14),
    _XfPMACMCurrent15m128QAMStd_Type()
)
xfPMACMCurrent15m128QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m128QAMStd.setStatus("current")
_XfPMACMCurrent15m128QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent15m128QAMLight_Object = MibTableColumn
xfPMACMCurrent15m128QAMLight = _XfPMACMCurrent15m128QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 15),
    _XfPMACMCurrent15m128QAMLight_Type()
)
xfPMACMCurrent15m128QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m128QAMLight.setStatus("current")
_XfPMACMCurrent15m256QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent15m256QAMStrong_Object = MibTableColumn
xfPMACMCurrent15m256QAMStrong = _XfPMACMCurrent15m256QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 16),
    _XfPMACMCurrent15m256QAMStrong_Type()
)
xfPMACMCurrent15m256QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m256QAMStrong.setStatus("current")
_XfPMACMCurrent15m256QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent15m256QAMStd_Object = MibTableColumn
xfPMACMCurrent15m256QAMStd = _XfPMACMCurrent15m256QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 17),
    _XfPMACMCurrent15m256QAMStd_Type()
)
xfPMACMCurrent15m256QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m256QAMStd.setStatus("current")
_XfPMACMCurrent15m256QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent15m256QAMLight_Object = MibTableColumn
xfPMACMCurrent15m256QAMLight = _XfPMACMCurrent15m256QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 18),
    _XfPMACMCurrent15m256QAMLight_Type()
)
xfPMACMCurrent15m256QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m256QAMLight.setStatus("current")
_XfPMACMCurrent15m512QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent15m512QAMStrong_Object = MibTableColumn
xfPMACMCurrent15m512QAMStrong = _XfPMACMCurrent15m512QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 19),
    _XfPMACMCurrent15m512QAMStrong_Type()
)
xfPMACMCurrent15m512QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m512QAMStrong.setStatus("current")
_XfPMACMCurrent15m512QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent15m512QAMStd_Object = MibTableColumn
xfPMACMCurrent15m512QAMStd = _XfPMACMCurrent15m512QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 20),
    _XfPMACMCurrent15m512QAMStd_Type()
)
xfPMACMCurrent15m512QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m512QAMStd.setStatus("current")
_XfPMACMCurrent15m512QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent15m512QAMLight_Object = MibTableColumn
xfPMACMCurrent15m512QAMLight = _XfPMACMCurrent15m512QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 21),
    _XfPMACMCurrent15m512QAMLight_Type()
)
xfPMACMCurrent15m512QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m512QAMLight.setStatus("current")
_XfPMACMCurrent15m1024QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent15m1024QAMStrong_Object = MibTableColumn
xfPMACMCurrent15m1024QAMStrong = _XfPMACMCurrent15m1024QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 22),
    _XfPMACMCurrent15m1024QAMStrong_Type()
)
xfPMACMCurrent15m1024QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m1024QAMStrong.setStatus("current")
_XfPMACMCurrent15m1024QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent15m1024QAMStd_Object = MibTableColumn
xfPMACMCurrent15m1024QAMStd = _XfPMACMCurrent15m1024QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 23),
    _XfPMACMCurrent15m1024QAMStd_Type()
)
xfPMACMCurrent15m1024QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m1024QAMStd.setStatus("current")
_XfPMACMCurrent15m1024QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent15m1024QAMLight_Object = MibTableColumn
xfPMACMCurrent15m1024QAMLight = _XfPMACMCurrent15m1024QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 24),
    _XfPMACMCurrent15m1024QAMLight_Type()
)
xfPMACMCurrent15m1024QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m1024QAMLight.setStatus("current")
_XfPMACMCurrent15m2048QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent15m2048QAMStrong_Object = MibTableColumn
xfPMACMCurrent15m2048QAMStrong = _XfPMACMCurrent15m2048QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 25),
    _XfPMACMCurrent15m2048QAMStrong_Type()
)
xfPMACMCurrent15m2048QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m2048QAMStrong.setStatus("current")
_XfPMACMCurrent15m2048QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent15m2048QAMStd_Object = MibTableColumn
xfPMACMCurrent15m2048QAMStd = _XfPMACMCurrent15m2048QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 26),
    _XfPMACMCurrent15m2048QAMStd_Type()
)
xfPMACMCurrent15m2048QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m2048QAMStd.setStatus("current")
_XfPMACMCurrent15m2048QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent15m2048QAMLight_Object = MibTableColumn
xfPMACMCurrent15m2048QAMLight = _XfPMACMCurrent15m2048QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 27),
    _XfPMACMCurrent15m2048QAMLight_Type()
)
xfPMACMCurrent15m2048QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m2048QAMLight.setStatus("current")
_XfPMACMCurrent15m4096QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent15m4096QAMStrong_Object = MibTableColumn
xfPMACMCurrent15m4096QAMStrong = _XfPMACMCurrent15m4096QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 28),
    _XfPMACMCurrent15m4096QAMStrong_Type()
)
xfPMACMCurrent15m4096QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m4096QAMStrong.setStatus("current")
_XfPMACMCurrent15m4096QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent15m4096QAMStd_Object = MibTableColumn
xfPMACMCurrent15m4096QAMStd = _XfPMACMCurrent15m4096QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 29),
    _XfPMACMCurrent15m4096QAMStd_Type()
)
xfPMACMCurrent15m4096QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m4096QAMStd.setStatus("current")
_XfPMACMCurrent15m4096QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent15m4096QAMLight_Object = MibTableColumn
xfPMACMCurrent15m4096QAMLight = _XfPMACMCurrent15m4096QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 30),
    _XfPMACMCurrent15m4096QAMLight_Type()
)
xfPMACMCurrent15m4096QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m4096QAMLight.setStatus("current")
_XfPMACMCurrent15m8192QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent15m8192QAMStrong_Object = MibTableColumn
xfPMACMCurrent15m8192QAMStrong = _XfPMACMCurrent15m8192QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 31),
    _XfPMACMCurrent15m8192QAMStrong_Type()
)
xfPMACMCurrent15m8192QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m8192QAMStrong.setStatus("current")
_XfPMACMCurrent15m8192QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent15m8192QAMStd_Object = MibTableColumn
xfPMACMCurrent15m8192QAMStd = _XfPMACMCurrent15m8192QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 32),
    _XfPMACMCurrent15m8192QAMStd_Type()
)
xfPMACMCurrent15m8192QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m8192QAMStd.setStatus("current")
_XfPMACMCurrent15m8192QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent15m8192QAMLight_Object = MibTableColumn
xfPMACMCurrent15m8192QAMLight = _XfPMACMCurrent15m8192QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 33),
    _XfPMACMCurrent15m8192QAMLight_Type()
)
xfPMACMCurrent15m8192QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m8192QAMLight.setStatus("current")
_XfPMACMCurrent15m16384QAMStrong_Type = PerfCurrentCount
_XfPMACMCurrent15m16384QAMStrong_Object = MibTableColumn
xfPMACMCurrent15m16384QAMStrong = _XfPMACMCurrent15m16384QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 34),
    _XfPMACMCurrent15m16384QAMStrong_Type()
)
xfPMACMCurrent15m16384QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m16384QAMStrong.setStatus("current")
_XfPMACMCurrent15m16384QAMStd_Type = PerfCurrentCount
_XfPMACMCurrent15m16384QAMStd_Object = MibTableColumn
xfPMACMCurrent15m16384QAMStd = _XfPMACMCurrent15m16384QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 35),
    _XfPMACMCurrent15m16384QAMStd_Type()
)
xfPMACMCurrent15m16384QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m16384QAMStd.setStatus("current")
_XfPMACMCurrent15m16384QAMLight_Type = PerfCurrentCount
_XfPMACMCurrent15m16384QAMLight_Object = MibTableColumn
xfPMACMCurrent15m16384QAMLight = _XfPMACMCurrent15m16384QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 5, 1, 36),
    _XfPMACMCurrent15m16384QAMLight_Type()
)
xfPMACMCurrent15m16384QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMCurrent15m16384QAMLight.setStatus("current")
_XfRLPMACMInterval15mTable_Object = MibTable
xfRLPMACMInterval15mTable = _XfRLPMACMInterval15mTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6)
)
if mibBuilder.loadTexts:
    xfRLPMACMInterval15mTable.setStatus("current")
_XfRLPMACMInterval15mEntry_Object = MibTableRow
xfRLPMACMInterval15mEntry = _XfRLPMACMInterval15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1)
)
xfRLPMACMInterval15mEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15mIntervalNumber"),
)
if mibBuilder.loadTexts:
    xfRLPMACMInterval15mEntry.setStatus("current")


class _XfPMACMInterval15mIntervalNumber_Type(Integer32):
    """Custom type xfPMACMInterval15mIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_XfPMACMInterval15mIntervalNumber_Type.__name__ = "Integer32"
_XfPMACMInterval15mIntervalNumber_Object = MibTableColumn
xfPMACMInterval15mIntervalNumber = _XfPMACMInterval15mIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 1),
    _XfPMACMInterval15mIntervalNumber_Type()
)
xfPMACMInterval15mIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15mIntervalNumber.setStatus("current")
_XfPMACMInterval15m4QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval15m4QAMStrong_Object = MibTableColumn
xfPMACMInterval15m4QAMStrong = _XfPMACMInterval15m4QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 2),
    _XfPMACMInterval15m4QAMStrong_Type()
)
xfPMACMInterval15m4QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m4QAMStrong.setStatus("current")
_XfPMACMInterval15m4QAMStd_Type = PerfIntervalCount
_XfPMACMInterval15m4QAMStd_Object = MibTableColumn
xfPMACMInterval15m4QAMStd = _XfPMACMInterval15m4QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 3),
    _XfPMACMInterval15m4QAMStd_Type()
)
xfPMACMInterval15m4QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m4QAMStd.setStatus("current")
_XfPMACMInterval15m4QAMLight_Type = PerfIntervalCount
_XfPMACMInterval15m4QAMLight_Object = MibTableColumn
xfPMACMInterval15m4QAMLight = _XfPMACMInterval15m4QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 4),
    _XfPMACMInterval15m4QAMLight_Type()
)
xfPMACMInterval15m4QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m4QAMLight.setStatus("current")
_XfPMACMInterval15m16QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval15m16QAMStrong_Object = MibTableColumn
xfPMACMInterval15m16QAMStrong = _XfPMACMInterval15m16QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 5),
    _XfPMACMInterval15m16QAMStrong_Type()
)
xfPMACMInterval15m16QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m16QAMStrong.setStatus("current")
_XfPMACMInterval15m16QAMStd_Type = PerfIntervalCount
_XfPMACMInterval15m16QAMStd_Object = MibTableColumn
xfPMACMInterval15m16QAMStd = _XfPMACMInterval15m16QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 6),
    _XfPMACMInterval15m16QAMStd_Type()
)
xfPMACMInterval15m16QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m16QAMStd.setStatus("current")
_XfPMACMInterval15m16QAMLight_Type = PerfIntervalCount
_XfPMACMInterval15m16QAMLight_Object = MibTableColumn
xfPMACMInterval15m16QAMLight = _XfPMACMInterval15m16QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 7),
    _XfPMACMInterval15m16QAMLight_Type()
)
xfPMACMInterval15m16QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m16QAMLight.setStatus("current")
_XfPMACMInterval15m32QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval15m32QAMStrong_Object = MibTableColumn
xfPMACMInterval15m32QAMStrong = _XfPMACMInterval15m32QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 8),
    _XfPMACMInterval15m32QAMStrong_Type()
)
xfPMACMInterval15m32QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m32QAMStrong.setStatus("current")
_XfPMACMInterval15m32QAMStd_Type = PerfIntervalCount
_XfPMACMInterval15m32QAMStd_Object = MibTableColumn
xfPMACMInterval15m32QAMStd = _XfPMACMInterval15m32QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 9),
    _XfPMACMInterval15m32QAMStd_Type()
)
xfPMACMInterval15m32QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m32QAMStd.setStatus("current")
_XfPMACMInterval15m32QAMLight_Type = PerfIntervalCount
_XfPMACMInterval15m32QAMLight_Object = MibTableColumn
xfPMACMInterval15m32QAMLight = _XfPMACMInterval15m32QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 10),
    _XfPMACMInterval15m32QAMLight_Type()
)
xfPMACMInterval15m32QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m32QAMLight.setStatus("current")
_XfPMACMInterval15m64QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval15m64QAMStrong_Object = MibTableColumn
xfPMACMInterval15m64QAMStrong = _XfPMACMInterval15m64QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 11),
    _XfPMACMInterval15m64QAMStrong_Type()
)
xfPMACMInterval15m64QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m64QAMStrong.setStatus("current")
_XfPMACMInterval15m64QAMStd_Type = PerfIntervalCount
_XfPMACMInterval15m64QAMStd_Object = MibTableColumn
xfPMACMInterval15m64QAMStd = _XfPMACMInterval15m64QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 12),
    _XfPMACMInterval15m64QAMStd_Type()
)
xfPMACMInterval15m64QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m64QAMStd.setStatus("current")
_XfPMACMInterval15m64QAMLight_Type = PerfIntervalCount
_XfPMACMInterval15m64QAMLight_Object = MibTableColumn
xfPMACMInterval15m64QAMLight = _XfPMACMInterval15m64QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 13),
    _XfPMACMInterval15m64QAMLight_Type()
)
xfPMACMInterval15m64QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m64QAMLight.setStatus("current")
_XfPMACMInterval15m128QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval15m128QAMStrong_Object = MibTableColumn
xfPMACMInterval15m128QAMStrong = _XfPMACMInterval15m128QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 14),
    _XfPMACMInterval15m128QAMStrong_Type()
)
xfPMACMInterval15m128QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m128QAMStrong.setStatus("current")
_XfPMACMInterval15m128QAMStd_Type = PerfIntervalCount
_XfPMACMInterval15m128QAMStd_Object = MibTableColumn
xfPMACMInterval15m128QAMStd = _XfPMACMInterval15m128QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 15),
    _XfPMACMInterval15m128QAMStd_Type()
)
xfPMACMInterval15m128QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m128QAMStd.setStatus("current")
_XfPMACMInterval15m128QAMLight_Type = PerfIntervalCount
_XfPMACMInterval15m128QAMLight_Object = MibTableColumn
xfPMACMInterval15m128QAMLight = _XfPMACMInterval15m128QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 16),
    _XfPMACMInterval15m128QAMLight_Type()
)
xfPMACMInterval15m128QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m128QAMLight.setStatus("current")
_XfPMACMInterval15m256QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval15m256QAMStrong_Object = MibTableColumn
xfPMACMInterval15m256QAMStrong = _XfPMACMInterval15m256QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 17),
    _XfPMACMInterval15m256QAMStrong_Type()
)
xfPMACMInterval15m256QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m256QAMStrong.setStatus("current")
_XfPMACMInterval15m256QAMStd_Type = PerfIntervalCount
_XfPMACMInterval15m256QAMStd_Object = MibTableColumn
xfPMACMInterval15m256QAMStd = _XfPMACMInterval15m256QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 18),
    _XfPMACMInterval15m256QAMStd_Type()
)
xfPMACMInterval15m256QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m256QAMStd.setStatus("current")
_XfPMACMInterval15m256QAMLight_Type = PerfIntervalCount
_XfPMACMInterval15m256QAMLight_Object = MibTableColumn
xfPMACMInterval15m256QAMLight = _XfPMACMInterval15m256QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 19),
    _XfPMACMInterval15m256QAMLight_Type()
)
xfPMACMInterval15m256QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m256QAMLight.setStatus("current")
_XfPMACMInterval15m512QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval15m512QAMStrong_Object = MibTableColumn
xfPMACMInterval15m512QAMStrong = _XfPMACMInterval15m512QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 20),
    _XfPMACMInterval15m512QAMStrong_Type()
)
xfPMACMInterval15m512QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m512QAMStrong.setStatus("current")
_XfPMACMInterval15m512QAMStd_Type = PerfIntervalCount
_XfPMACMInterval15m512QAMStd_Object = MibTableColumn
xfPMACMInterval15m512QAMStd = _XfPMACMInterval15m512QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 21),
    _XfPMACMInterval15m512QAMStd_Type()
)
xfPMACMInterval15m512QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m512QAMStd.setStatus("current")
_XfPMACMInterval15m512QAMLight_Type = PerfIntervalCount
_XfPMACMInterval15m512QAMLight_Object = MibTableColumn
xfPMACMInterval15m512QAMLight = _XfPMACMInterval15m512QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 22),
    _XfPMACMInterval15m512QAMLight_Type()
)
xfPMACMInterval15m512QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m512QAMLight.setStatus("current")
_XfPMACMInterval15m1024QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval15m1024QAMStrong_Object = MibTableColumn
xfPMACMInterval15m1024QAMStrong = _XfPMACMInterval15m1024QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 23),
    _XfPMACMInterval15m1024QAMStrong_Type()
)
xfPMACMInterval15m1024QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m1024QAMStrong.setStatus("current")
_XfPMACMInterval15m1024QAMStd_Type = PerfIntervalCount
_XfPMACMInterval15m1024QAMStd_Object = MibTableColumn
xfPMACMInterval15m1024QAMStd = _XfPMACMInterval15m1024QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 24),
    _XfPMACMInterval15m1024QAMStd_Type()
)
xfPMACMInterval15m1024QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m1024QAMStd.setStatus("current")
_XfPMACMInterval15m1024QAMLight_Type = PerfIntervalCount
_XfPMACMInterval15m1024QAMLight_Object = MibTableColumn
xfPMACMInterval15m1024QAMLight = _XfPMACMInterval15m1024QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 25),
    _XfPMACMInterval15m1024QAMLight_Type()
)
xfPMACMInterval15m1024QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m1024QAMLight.setStatus("current")
_XfPMACMInterval15m2048QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval15m2048QAMStrong_Object = MibTableColumn
xfPMACMInterval15m2048QAMStrong = _XfPMACMInterval15m2048QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 26),
    _XfPMACMInterval15m2048QAMStrong_Type()
)
xfPMACMInterval15m2048QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m2048QAMStrong.setStatus("current")
_XfPMACMInterval15m2048QAMStd_Type = PerfIntervalCount
_XfPMACMInterval15m2048QAMStd_Object = MibTableColumn
xfPMACMInterval15m2048QAMStd = _XfPMACMInterval15m2048QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 27),
    _XfPMACMInterval15m2048QAMStd_Type()
)
xfPMACMInterval15m2048QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m2048QAMStd.setStatus("current")
_XfPMACMInterval15m2048QAMLight_Type = PerfIntervalCount
_XfPMACMInterval15m2048QAMLight_Object = MibTableColumn
xfPMACMInterval15m2048QAMLight = _XfPMACMInterval15m2048QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 28),
    _XfPMACMInterval15m2048QAMLight_Type()
)
xfPMACMInterval15m2048QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m2048QAMLight.setStatus("current")
_XfPMACMInterval15m4096QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval15m4096QAMStrong_Object = MibTableColumn
xfPMACMInterval15m4096QAMStrong = _XfPMACMInterval15m4096QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 29),
    _XfPMACMInterval15m4096QAMStrong_Type()
)
xfPMACMInterval15m4096QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m4096QAMStrong.setStatus("current")
_XfPMACMInterval15m4096QAMStd_Type = PerfIntervalCount
_XfPMACMInterval15m4096QAMStd_Object = MibTableColumn
xfPMACMInterval15m4096QAMStd = _XfPMACMInterval15m4096QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 30),
    _XfPMACMInterval15m4096QAMStd_Type()
)
xfPMACMInterval15m4096QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m4096QAMStd.setStatus("current")
_XfPMACMInterval15m4096QAMLight_Type = PerfIntervalCount
_XfPMACMInterval15m4096QAMLight_Object = MibTableColumn
xfPMACMInterval15m4096QAMLight = _XfPMACMInterval15m4096QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 31),
    _XfPMACMInterval15m4096QAMLight_Type()
)
xfPMACMInterval15m4096QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m4096QAMLight.setStatus("current")
_XfPMACMInterval15mValidData_Type = TruthValue
_XfPMACMInterval15mValidData_Object = MibTableColumn
xfPMACMInterval15mValidData = _XfPMACMInterval15mValidData_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 32),
    _XfPMACMInterval15mValidData_Type()
)
xfPMACMInterval15mValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15mValidData.setStatus("current")
_XfPMACMInterval15m8192QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval15m8192QAMStrong_Object = MibTableColumn
xfPMACMInterval15m8192QAMStrong = _XfPMACMInterval15m8192QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 33),
    _XfPMACMInterval15m8192QAMStrong_Type()
)
xfPMACMInterval15m8192QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m8192QAMStrong.setStatus("current")
_XfPMACMInterval15m8192QAMStd_Type = PerfIntervalCount
_XfPMACMInterval15m8192QAMStd_Object = MibTableColumn
xfPMACMInterval15m8192QAMStd = _XfPMACMInterval15m8192QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 34),
    _XfPMACMInterval15m8192QAMStd_Type()
)
xfPMACMInterval15m8192QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m8192QAMStd.setStatus("current")
_XfPMACMInterval15m8192QAMLight_Type = PerfIntervalCount
_XfPMACMInterval15m8192QAMLight_Object = MibTableColumn
xfPMACMInterval15m8192QAMLight = _XfPMACMInterval15m8192QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 35),
    _XfPMACMInterval15m8192QAMLight_Type()
)
xfPMACMInterval15m8192QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m8192QAMLight.setStatus("current")
_XfPMACMInterval15m16384QAMStrong_Type = PerfIntervalCount
_XfPMACMInterval15m16384QAMStrong_Object = MibTableColumn
xfPMACMInterval15m16384QAMStrong = _XfPMACMInterval15m16384QAMStrong_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 36),
    _XfPMACMInterval15m16384QAMStrong_Type()
)
xfPMACMInterval15m16384QAMStrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m16384QAMStrong.setStatus("current")
_XfPMACMInterval15m16384QAMStd_Type = PerfIntervalCount
_XfPMACMInterval15m16384QAMStd_Object = MibTableColumn
xfPMACMInterval15m16384QAMStd = _XfPMACMInterval15m16384QAMStd_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 37),
    _XfPMACMInterval15m16384QAMStd_Type()
)
xfPMACMInterval15m16384QAMStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m16384QAMStd.setStatus("current")
_XfPMACMInterval15m16384QAMLight_Type = PerfIntervalCount
_XfPMACMInterval15m16384QAMLight_Object = MibTableColumn
xfPMACMInterval15m16384QAMLight = _XfPMACMInterval15m16384QAMLight_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 6, 1, 38),
    _XfPMACMInterval15m16384QAMLight_Type()
)
xfPMACMInterval15m16384QAMLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMACMInterval15m16384QAMLight.setStatus("current")
_XfRLPMMimoCurrentTable_Object = MibTable
xfRLPMMimoCurrentTable = _XfRLPMMimoCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 7)
)
if mibBuilder.loadTexts:
    xfRLPMMimoCurrentTable.setStatus("current")
_XfRLPMMimoCurrentEntry_Object = MibTableRow
xfRLPMMimoCurrentEntry = _XfRLPMMimoCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 7, 1)
)
xfRLPMMimoCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMMimoCurrentEntry.setStatus("current")
_XfPMPerfCurrentEta_Type = Integer32
_XfPMPerfCurrentEta_Object = MibTableColumn
xfPMPerfCurrentEta = _XfPMPerfCurrentEta_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 7, 1, 1),
    _XfPMPerfCurrentEta_Type()
)
xfPMPerfCurrentEta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMPerfCurrentEta.setStatus("current")
_XfPMPerfEtaMinLast7days_Type = Integer32
_XfPMPerfEtaMinLast7days_Object = MibTableColumn
xfPMPerfEtaMinLast7days = _XfPMPerfEtaMinLast7days_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 7, 1, 2),
    _XfPMPerfEtaMinLast7days_Type()
)
xfPMPerfEtaMinLast7days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMPerfEtaMinLast7days.setStatus("current")
_XfPMPerfEtaMaxLast7days_Type = Integer32
_XfPMPerfEtaMaxLast7days_Object = MibTableColumn
xfPMPerfEtaMaxLast7days = _XfPMPerfEtaMaxLast7days_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 7, 1, 3),
    _XfPMPerfEtaMaxLast7days_Type()
)
xfPMPerfEtaMaxLast7days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMPerfEtaMaxLast7days.setStatus("current")
_XfRLPMMimoCurrent24hTable_Object = MibTable
xfRLPMMimoCurrent24hTable = _XfRLPMMimoCurrent24hTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 8)
)
if mibBuilder.loadTexts:
    xfRLPMMimoCurrent24hTable.setStatus("current")
_XfRLPMMimoCurrent24hEntry_Object = MibTableRow
xfRLPMMimoCurrent24hEntry = _XfRLPMMimoCurrent24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 8, 1)
)
xfRLPMMimoCurrent24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMMimoCurrent24hEntry.setStatus("current")
_XfPMPerfCurrent24hElapsedTime_Type = Counter32
_XfPMPerfCurrent24hElapsedTime_Object = MibTableColumn
xfPMPerfCurrent24hElapsedTime = _XfPMPerfCurrent24hElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 8, 1, 1),
    _XfPMPerfCurrent24hElapsedTime_Type()
)
xfPMPerfCurrent24hElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMPerfCurrent24hElapsedTime.setStatus("current")
_XfPMPerfCurrent24hEtaMin_Type = Integer32
_XfPMPerfCurrent24hEtaMin_Object = MibTableColumn
xfPMPerfCurrent24hEtaMin = _XfPMPerfCurrent24hEtaMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 8, 1, 2),
    _XfPMPerfCurrent24hEtaMin_Type()
)
xfPMPerfCurrent24hEtaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMPerfCurrent24hEtaMin.setStatus("current")
_XfPMPerfCurrent24hEtaMax_Type = Integer32
_XfPMPerfCurrent24hEtaMax_Object = MibTableColumn
xfPMPerfCurrent24hEtaMax = _XfPMPerfCurrent24hEtaMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 8, 1, 3),
    _XfPMPerfCurrent24hEtaMax_Type()
)
xfPMPerfCurrent24hEtaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMPerfCurrent24hEtaMax.setStatus("current")
_XfRLPMMimoInterval24hTable_Object = MibTable
xfRLPMMimoInterval24hTable = _XfRLPMMimoInterval24hTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 9)
)
if mibBuilder.loadTexts:
    xfRLPMMimoInterval24hTable.setStatus("current")
_XfRLPMMimoInterval24hEntry_Object = MibTableRow
xfRLPMMimoInterval24hEntry = _XfRLPMMimoInterval24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 9, 1)
)
xfRLPMMimoInterval24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMMimoInterval24hEntry.setStatus("current")
_XfPMPerfInterval24hValidData_Type = Integer32
_XfPMPerfInterval24hValidData_Object = MibTableColumn
xfPMPerfInterval24hValidData = _XfPMPerfInterval24hValidData_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 9, 1, 1),
    _XfPMPerfInterval24hValidData_Type()
)
xfPMPerfInterval24hValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMPerfInterval24hValidData.setStatus("current")
_XfPMPerfInterval24hEtaMin_Type = Integer32
_XfPMPerfInterval24hEtaMin_Object = MibTableColumn
xfPMPerfInterval24hEtaMin = _XfPMPerfInterval24hEtaMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 9, 1, 2),
    _XfPMPerfInterval24hEtaMin_Type()
)
xfPMPerfInterval24hEtaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMPerfInterval24hEtaMin.setStatus("current")
_XfPMPerfInterval24hEtaMax_Type = Integer32
_XfPMPerfInterval24hEtaMax_Object = MibTableColumn
xfPMPerfInterval24hEtaMax = _XfPMPerfInterval24hEtaMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 9, 1, 3),
    _XfPMPerfInterval24hEtaMax_Type()
)
xfPMPerfInterval24hEtaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMPerfInterval24hEtaMax.setStatus("current")
_XfRLPMMimoCurrent15mTable_Object = MibTable
xfRLPMMimoCurrent15mTable = _XfRLPMMimoCurrent15mTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 10)
)
if mibBuilder.loadTexts:
    xfRLPMMimoCurrent15mTable.setStatus("current")
_XfRLPMMimoCurrent15mEntry_Object = MibTableRow
xfRLPMMimoCurrent15mEntry = _XfRLPMMimoCurrent15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 10, 1)
)
xfRLPMMimoCurrent15mEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMMimoCurrent15mEntry.setStatus("current")
_XfPMPerfCurrent15mElapsedTime_Type = Counter32
_XfPMPerfCurrent15mElapsedTime_Object = MibTableColumn
xfPMPerfCurrent15mElapsedTime = _XfPMPerfCurrent15mElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 10, 1, 1),
    _XfPMPerfCurrent15mElapsedTime_Type()
)
xfPMPerfCurrent15mElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMPerfCurrent15mElapsedTime.setStatus("current")
_XfPMPerfCurrent15mEtaMin_Type = Integer32
_XfPMPerfCurrent15mEtaMin_Object = MibTableColumn
xfPMPerfCurrent15mEtaMin = _XfPMPerfCurrent15mEtaMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 10, 1, 2),
    _XfPMPerfCurrent15mEtaMin_Type()
)
xfPMPerfCurrent15mEtaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMPerfCurrent15mEtaMin.setStatus("current")
_XfPMPerfCurrent15mEtaMax_Type = Integer32
_XfPMPerfCurrent15mEtaMax_Object = MibTableColumn
xfPMPerfCurrent15mEtaMax = _XfPMPerfCurrent15mEtaMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 10, 1, 3),
    _XfPMPerfCurrent15mEtaMax_Type()
)
xfPMPerfCurrent15mEtaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMPerfCurrent15mEtaMax.setStatus("current")
_XfRLPMMimoInterval15mTable_Object = MibTable
xfRLPMMimoInterval15mTable = _XfRLPMMimoInterval15mTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 11)
)
if mibBuilder.loadTexts:
    xfRLPMMimoInterval15mTable.setStatus("current")
_XfRLPMMimoInterval15mEntry_Object = MibTableRow
xfRLPMMimoInterval15mEntry = _XfRLPMMimoInterval15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 11, 1)
)
xfRLPMMimoInterval15mEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "XF-RADIOLINK-RLT-MIB", "xfPMPerfInterval15mIntervalNumber"),
)
if mibBuilder.loadTexts:
    xfRLPMMimoInterval15mEntry.setStatus("current")


class _XfPMPerfInterval15mIntervalNumber_Type(Integer32):
    """Custom type xfPMPerfInterval15mIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_XfPMPerfInterval15mIntervalNumber_Type.__name__ = "Integer32"
_XfPMPerfInterval15mIntervalNumber_Object = MibTableColumn
xfPMPerfInterval15mIntervalNumber = _XfPMPerfInterval15mIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 11, 1, 1),
    _XfPMPerfInterval15mIntervalNumber_Type()
)
xfPMPerfInterval15mIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMPerfInterval15mIntervalNumber.setStatus("current")
_XfPMPerfInterval15mEtaMin_Type = Integer32
_XfPMPerfInterval15mEtaMin_Object = MibTableColumn
xfPMPerfInterval15mEtaMin = _XfPMPerfInterval15mEtaMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 11, 1, 2),
    _XfPMPerfInterval15mEtaMin_Type()
)
xfPMPerfInterval15mEtaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMPerfInterval15mEtaMin.setStatus("current")
_XfPMPerfInterval15mEtaMax_Type = Integer32
_XfPMPerfInterval15mEtaMax_Object = MibTableColumn
xfPMPerfInterval15mEtaMax = _XfPMPerfInterval15mEtaMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 11, 1, 3),
    _XfPMPerfInterval15mEtaMax_Type()
)
xfPMPerfInterval15mEtaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMPerfInterval15mEtaMax.setStatus("current")
_XfPMPerfInterval15mValidData_Type = Integer32
_XfPMPerfInterval15mValidData_Object = MibTableColumn
xfPMPerfInterval15mValidData = _XfPMPerfInterval15mValidData_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 2, 11, 1, 4),
    _XfPMPerfInterval15mValidData_Type()
)
xfPMPerfInterval15mValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMPerfInterval15mValidData.setStatus("current")
_XfRadioLinkRltConformance_ObjectIdentity = ObjectIdentity
xfRadioLinkRltConformance = _XfRadioLinkRltConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 3)
)
_XfRadioLinkRltCompliances_ObjectIdentity = ObjectIdentity
xfRadioLinkRltCompliances = _XfRadioLinkRltCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 3, 1)
)
_XfRadioLinkRltGroups_ObjectIdentity = ObjectIdentity
xfRadioLinkRltGroups = _XfRadioLinkRltGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 3, 2)
)

# Managed Objects groups

xfRadioLinkRltCompleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 3, 2, 1)
)
xfRadioLinkRltCompleteGroup.setObjects(
      *(("XF-RADIOLINK-RLT-MIB", "cgIfIndex"),
        ("XF-RADIOLINK-RLT-MIB", "cgTypeIndex"),
        ("XF-RADIOLINK-RLT-MIB", "xfIfStatus"),
        ("XF-RADIOLINK-RLT-MIB", "liEntLogicalIndex"),
        ("XF-RADIOLINK-RLT-MIB", "liIfIndex"),
        ("XF-RADIOLINK-RLT-MIB", "xfLIName"),
        ("XF-RADIOLINK-RLT-MIB", "xfLIIfDescr"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermDistinguishedName"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermLabel"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermOperStatus"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermRadioFrameId"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermPreamble"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermSelectedMinACM"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermActualACM"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermSelectedMaxACM"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermCapabilitiesLastChange"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermReferenceSEC"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermWantedLicensedCapacity"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermActualLicensedCapacity"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermActualCapacity"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermPolarization"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermXPICOperStatus"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermMIMOOperStatus"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermSNIR"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermXPI"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermReset"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermRestore"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermAutoRemoveLoopEnable"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermBerAlarmThreshold"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermActualRxACM"),
        ("XF-RADIOLINK-RLT-MIB", "xfCarrierTermFeCTSeverity"),
        ("XF-RADIOLINK-RLT-MIB", "xfRadioFrameId"),
        ("XF-RADIOLINK-RLT-MIB", "xfChannelSpacing"),
        ("XF-RADIOLINK-RLT-MIB", "xfFrameFormatType"),
        ("XF-RADIOLINK-RLT-MIB", "xfMinACMCapacity"),
        ("XF-RADIOLINK-RLT-MIB", "xfMaxACMCapacity"),
        ("XF-RADIOLINK-RLT-MIB", "xfACMProfile"),
        ("XF-RADIOLINK-RLT-MIB", "xfACMIndex"),
        ("XF-RADIOLINK-RLT-MIB", "xfACMCapacity"),
        ("XF-RADIOLINK-RLT-MIB", "rltEntLogicalIndex"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTDistinguishedName"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTIpAddress"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTIPv6Address"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTNeName"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTNeType"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTId"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTExpectedFarEndId"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTFarEndIdCheck"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTStatus"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTMode"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTActualTXTotalCapacity"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTActualTXPacketCapacity"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTLimitedTotalCapacity"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTRltSeverity"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTCapability"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTInventoryLastChange"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTCpriMode"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTReset"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTMeasuredHopLength"),
        ("XF-RADIOLINK-RLT-MIB", "trEntLogicalIndex"),
        ("XF-RADIOLINK-RLT-MIB", "xfTDMEnable"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTDMIfIndex"),
        ("XF-RADIOLINK-RLT-MIB", "xfActualTDMCapacity"),
        ("XF-RADIOLINK-RLT-MIB", "xfWantedTDMAllocation"),
        ("XF-RADIOLINK-RLT-MIB", "xfActualTDMAllocation"),
        ("XF-RADIOLINK-RLT-MIB", "xfTDMIfAlarms"),
        ("XF-RADIOLINK-RLT-MIB", "xfTDMRxLoop"),
        ("XF-RADIOLINK-RLT-MIB", "xfTDMDistinguishedName"),
        ("XF-RADIOLINK-RLT-MIB", "xfTDMMaxTributaries"),
        ("XF-RADIOLINK-RLT-MIB", "xfTDMHopLength"),
        ("XF-RADIOLINK-RLT-MIB", "xfCGIfIndex"),
        ("XF-RADIOLINK-RLT-MIB", "xfCGIfMinSpeed"),
        ("XF-RADIOLINK-RLT-MIB", "xfCGIfMaxSpeed"),
        ("XF-RADIOLINK-RLT-MIB", "xfCGIfRCNum"),
        ("XF-RADIOLINK-RLT-MIB", "xfCGIfAlarms"),
        ("XF-RADIOLINK-RLT-MIB", "xfCGIfHopViewStatus"),
        ("XF-RADIOLINK-RLT-MIB", "xpicPairEntLogicalIIndex"),
        ("XF-RADIOLINK-RLT-MIB", "xfXPICPairAdminStatus"),
        ("XF-RADIOLINK-RLT-MIB", "xfXPICPairNumber"),
        ("XF-RADIOLINK-RLT-MIB", "xfXPICPairRecovery"),
        ("XF-RADIOLINK-RLT-MIB", "xfXPICPairRestore"),
        ("XF-RADIOLINK-RLT-MIB", "xfXPICCTmember1"),
        ("XF-RADIOLINK-RLT-MIB", "xfXPICCTmember2"),
        ("XF-RADIOLINK-RLT-MIB", "xfXPICAutoRestore"),
        ("XF-RADIOLINK-RLT-MIB", "xfXpicPairIndex"),
        ("XF-RADIOLINK-RLT-MIB", "mimoGroupEntLogicalIIndex"),
        ("XF-RADIOLINK-RLT-MIB", "xfMIMOGroupAdminStatus"),
        ("XF-RADIOLINK-RLT-MIB", "xfMIMOGroupNumber"),
        ("XF-RADIOLINK-RLT-MIB", "xfMIMOGroupRecovery"),
        ("XF-RADIOLINK-RLT-MIB", "xfMIMOGroupRestore"),
        ("XF-RADIOLINK-RLT-MIB", "xfMIMOCTmember1"),
        ("XF-RADIOLINK-RLT-MIB", "xfMIMOCTmember2"),
        ("XF-RADIOLINK-RLT-MIB", "xfMIMOCTmember3"),
        ("XF-RADIOLINK-RLT-MIB", "xfMIMOCTmember4"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMTimeElapsed"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMCurrentES"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMCurrentSES"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMCurrentBBE"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMCurrentUAS"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMCurrentBB"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMPerfReset"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMCurrentESR"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMCurrentSESR"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMCurrentBBER"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMSetThreshold15m"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMSetThreshold24h"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMResetThreshold15m"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMStatus"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMValidData"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h4QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h4QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h4QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h16QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h16QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h16QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h32QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h32QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h32QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h64QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h64QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h64QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h128QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h128QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h128QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h256QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h256QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h256QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h512QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h512QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h512QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h1024QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h1024QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h1024QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h2048QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h2048QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h2048QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h4096QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h4096QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h4096QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h8192QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h8192QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h8192QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h16384QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h16384QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent24h16384QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h4QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h4QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h4QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h16QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h16QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h16QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h32QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h32QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h32QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h64QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h64QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h64QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h128QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h128QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h128QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h256QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h256QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h256QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h512QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h512QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h512QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h1024QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h1024QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h1024QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h2048QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h2048QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h2048QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h4096QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h4096QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h4096QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24hValidData"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h8192QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h8192QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h8192QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h16384QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h16384QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval24h16384QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m4QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m4QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m4QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m16QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m16QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m16QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m32QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m32QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m32QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m64QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m64QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m64QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m128QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m128QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m128QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m256QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m256QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m256QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m512QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m512QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m512QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m1024QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m1024QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m1024QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m2048QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m2048QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m2048QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m4096QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m4096QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m4096QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m8192QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m8192QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m8192QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m16384QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m16384QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMCurrent15m16384QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15mIntervalNumber"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m4QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m4QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m4QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m16QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m16QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m16QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m32QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m32QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m32QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m64QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m64QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m64QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m128QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m128QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m128QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m256QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m256QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m256QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m512QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m512QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m512QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m1024QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m1024QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m1024QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m2048QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m2048QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m2048QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m4096QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m4096QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m4096QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15mValidData"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m8192QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m8192QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m8192QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m16384QAMStrong"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m16384QAMStd"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMACMInterval15m16384QAMLight"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLWANIfIndex"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLWANDistinguishedName"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLWANCompAdminStatus"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLWANCompConnStatus"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLWANMlhcMplsMode"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLWANMlhcOperStatus"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLWANPlcOperStatus"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLWANActualCapacity"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLWANLimitedCapacity"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTMHIndex"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTModuleIndex"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTEntPhysicalIndex"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTPhysicalCointainedIn"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTPhysicalParentRelPos"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTEntityPhysicalDescr"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTModuleSlotPosition"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTNEDistinguishedName"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTFEDistinguishedName"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTInterfaceIndex"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTHighestSeverityAlarm"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTProtIndex"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTProtectionSwitchMode"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTProtectionStatus"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTRevertivePreferredTX"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTProtectionWaitToRestoreTime"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTFadeNotificationTimer"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTManualSwitchCommand"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTTxSwitchOverConfiguration"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTTxSwitchOverAlarmReset"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTNumOfRLPSwitch"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTEnhancedACMProtectionMode"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTEnhancedACMProtectionOperStatus"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTEncryptionIndex"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTEncryptionAdminStatus"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTEncryptionOperStatus"),
        ("XF-RADIOLINK-RLT-MIB", "xfRLTEncryptionMasterKey"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMPerfCurrentEta"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMPerfEtaMinLast7days"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMPerfEtaMaxLast7days"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMPerfCurrent24hElapsedTime"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMPerfCurrent24hEtaMin"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMPerfCurrent24hEtaMax"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMPerfInterval24hValidData"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMPerfInterval24hEtaMin"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMPerfInterval24hEtaMax"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMPerfCurrent15mElapsedTime"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMPerfCurrent15mEtaMin"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMPerfCurrent15mEtaMax"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMPerfInterval15mIntervalNumber"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMPerfInterval15mEtaMin"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMPerfInterval15mEtaMax"),
        ("XF-RADIOLINK-RLT-MIB", "xfPMPerfInterval15mValidData"))
)
if mibBuilder.loadTexts:
    xfRadioLinkRltCompleteGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xfRadioLinkRltFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 5, 3, 1, 1)
)
xfRadioLinkRltFullCompliance.setObjects(
    ("XF-RADIOLINK-RLT-MIB", "xfRadioLinkRltCompleteGroup")
)
if mibBuilder.loadTexts:
    xfRadioLinkRltFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XF-RADIOLINK-RLT-MIB",
    **{"CarrierTermACMIndex": CarrierTermACMIndex,
       "xfRadioLinkRltMIB": xfRadioLinkRltMIB,
       "xfRadioLinkRltObjects": xfRadioLinkRltObjects,
       "xfChannelGroupTable": xfChannelGroupTable,
       "xfChannelGroupEntry": xfChannelGroupEntry,
       "cgIfIndex": cgIfIndex,
       "cgTypeIndex": cgTypeIndex,
       "xfIfStatus": xfIfStatus,
       "xfLIMappingTable": xfLIMappingTable,
       "xfLIMappingEntry": xfLIMappingEntry,
       "liEntLogicalIndex": liEntLogicalIndex,
       "liIfIndex": liIfIndex,
       "xfLIName": xfLIName,
       "xfLIIfDescr": xfLIIfDescr,
       "xfCarrierTerminationTable": xfCarrierTerminationTable,
       "xfCarrierTerminationEntry": xfCarrierTerminationEntry,
       "xfCarrierTermDistinguishedName": xfCarrierTermDistinguishedName,
       "xfCarrierTermLabel": xfCarrierTermLabel,
       "xfCarrierTermOperStatus": xfCarrierTermOperStatus,
       "xfCarrierTermRadioFrameId": xfCarrierTermRadioFrameId,
       "xfCarrierTermPreamble": xfCarrierTermPreamble,
       "xfCarrierTermSelectedMinACM": xfCarrierTermSelectedMinACM,
       "xfCarrierTermActualACM": xfCarrierTermActualACM,
       "xfCarrierTermSelectedMaxACM": xfCarrierTermSelectedMaxACM,
       "xfCarrierTermCapabilitiesLastChange": xfCarrierTermCapabilitiesLastChange,
       "xfCarrierTermReferenceSEC": xfCarrierTermReferenceSEC,
       "xfCarrierTermWantedLicensedCapacity": xfCarrierTermWantedLicensedCapacity,
       "xfCarrierTermActualLicensedCapacity": xfCarrierTermActualLicensedCapacity,
       "xfCarrierTermActualCapacity": xfCarrierTermActualCapacity,
       "xfCarrierTermPolarization": xfCarrierTermPolarization,
       "xfCarrierTermXPICOperStatus": xfCarrierTermXPICOperStatus,
       "xfCarrierTermMIMOOperStatus": xfCarrierTermMIMOOperStatus,
       "xfCarrierTermSNIR": xfCarrierTermSNIR,
       "xfCarrierTermXPI": xfCarrierTermXPI,
       "xfCarrierTermReset": xfCarrierTermReset,
       "xfCarrierTermRestore": xfCarrierTermRestore,
       "xfCarrierTermAutoRemoveLoopEnable": xfCarrierTermAutoRemoveLoopEnable,
       "xfCarrierTermBerAlarmThreshold": xfCarrierTermBerAlarmThreshold,
       "xfCarrierTermActualRxACM": xfCarrierTermActualRxACM,
       "xfCarrierTermFeCTSeverity": xfCarrierTermFeCTSeverity,
       "xfCarrierTerminationCapabilityTable": xfCarrierTerminationCapabilityTable,
       "xfCarrierTerminationCapabilityEntry": xfCarrierTerminationCapabilityEntry,
       "xfRadioFrameId": xfRadioFrameId,
       "xfChannelSpacing": xfChannelSpacing,
       "xfFrameFormatType": xfFrameFormatType,
       "xfMinACMCapacity": xfMinACMCapacity,
       "xfMaxACMCapacity": xfMaxACMCapacity,
       "xfACMProfile": xfACMProfile,
       "xfACMProfileCapacityTable": xfACMProfileCapacityTable,
       "xfACMProfileCapacityEntry": xfACMProfileCapacityEntry,
       "xfACMIndex": xfACMIndex,
       "xfACMCapacity": xfACMCapacity,
       "xfRLTTable": xfRLTTable,
       "xfRLTEntry": xfRLTEntry,
       "rltEntLogicalIndex": rltEntLogicalIndex,
       "xfRLTDistinguishedName": xfRLTDistinguishedName,
       "xfRLTIpAddress": xfRLTIpAddress,
       "xfRLTIPv6Address": xfRLTIPv6Address,
       "xfRLTNeName": xfRLTNeName,
       "xfRLTNeType": xfRLTNeType,
       "xfRLTId": xfRLTId,
       "xfRLTExpectedFarEndId": xfRLTExpectedFarEndId,
       "xfRLTFarEndIdCheck": xfRLTFarEndIdCheck,
       "xfRLTStatus": xfRLTStatus,
       "xfRLTMode": xfRLTMode,
       "xfRLTActualTXTotalCapacity": xfRLTActualTXTotalCapacity,
       "xfRLTActualTXPacketCapacity": xfRLTActualTXPacketCapacity,
       "xfRLTLimitedTotalCapacity": xfRLTLimitedTotalCapacity,
       "xfRLTRltSeverity": xfRLTRltSeverity,
       "xfRLTCapability": xfRLTCapability,
       "xfRLTInventoryLastChange": xfRLTInventoryLastChange,
       "xfRLTCpriMode": xfRLTCpriMode,
       "xfRLTReset": xfRLTReset,
       "xfRLTMeasuredHopLength": xfRLTMeasuredHopLength,
       "xfTrafficTable": xfTrafficTable,
       "xfTrafficEntry": xfTrafficEntry,
       "trEntLogicalIndex": trEntLogicalIndex,
       "xfTDMEnable": xfTDMEnable,
       "xfRLTDMIfTable": xfRLTDMIfTable,
       "xfRLTDMIfEntry": xfRLTDMIfEntry,
       "xfRLTDMIfIndex": xfRLTDMIfIndex,
       "xfActualTDMCapacity": xfActualTDMCapacity,
       "xfWantedTDMAllocation": xfWantedTDMAllocation,
       "xfActualTDMAllocation": xfActualTDMAllocation,
       "xfTDMIfAlarms": xfTDMIfAlarms,
       "xfTDMRxLoop": xfTDMRxLoop,
       "xfTDMDistinguishedName": xfTDMDistinguishedName,
       "xfTDMMaxTributaries": xfTDMMaxTributaries,
       "xfTDMHopLength": xfTDMHopLength,
       "xfCGIfTable": xfCGIfTable,
       "xfCGIfEntry": xfCGIfEntry,
       "xfCGIfIndex": xfCGIfIndex,
       "xfCGIfMinSpeed": xfCGIfMinSpeed,
       "xfCGIfMaxSpeed": xfCGIfMaxSpeed,
       "xfCGIfRCNum": xfCGIfRCNum,
       "xfCGIfAlarms": xfCGIfAlarms,
       "xfCGIfHopViewStatus": xfCGIfHopViewStatus,
       "xfXPICPairTable": xfXPICPairTable,
       "xfXPICPairEntry": xfXPICPairEntry,
       "xpicPairEntLogicalIIndex": xpicPairEntLogicalIIndex,
       "xfXPICPairAdminStatus": xfXPICPairAdminStatus,
       "xfXPICPairNumber": xfXPICPairNumber,
       "xfXPICPairRecovery": xfXPICPairRecovery,
       "xfXPICPairRestore": xfXPICPairRestore,
       "xfXPICCTmember1": xfXPICCTmember1,
       "xfXPICCTmember2": xfXPICCTmember2,
       "xfXPICAutoRestore": xfXPICAutoRestore,
       "xfXpicPairIndex": xfXpicPairIndex,
       "xfMIMOGroupTable": xfMIMOGroupTable,
       "xfMIMOGroupEntry": xfMIMOGroupEntry,
       "mimoGroupEntLogicalIIndex": mimoGroupEntLogicalIIndex,
       "xfMIMOGroupAdminStatus": xfMIMOGroupAdminStatus,
       "xfMIMOGroupNumber": xfMIMOGroupNumber,
       "xfMIMOGroupRecovery": xfMIMOGroupRecovery,
       "xfMIMOGroupRestore": xfMIMOGroupRestore,
       "xfMIMOCTmember1": xfMIMOCTmember1,
       "xfMIMOCTmember2": xfMIMOCTmember2,
       "xfMIMOCTmember3": xfMIMOCTmember3,
       "xfMIMOCTmember4": xfMIMOCTmember4,
       "xfRLWANIfTable": xfRLWANIfTable,
       "xfRLWANIfEntry": xfRLWANIfEntry,
       "xfRLWANIfIndex": xfRLWANIfIndex,
       "xfRLWANDistinguishedName": xfRLWANDistinguishedName,
       "xfRLWANCompAdminStatus": xfRLWANCompAdminStatus,
       "xfRLWANCompConnStatus": xfRLWANCompConnStatus,
       "xfRLWANMlhcMplsMode": xfRLWANMlhcMplsMode,
       "xfRLWANMlhcOperStatus": xfRLWANMlhcOperStatus,
       "xfRLWANPlcOperStatus": xfRLWANPlcOperStatus,
       "xfRLWANActualCapacity": xfRLWANActualCapacity,
       "xfRLWANLimitedCapacity": xfRLWANLimitedCapacity,
       "xfRLTHierarchyModuleTable": xfRLTHierarchyModuleTable,
       "xfRLTHierarchyModuleEntry": xfRLTHierarchyModuleEntry,
       "xfRLTMHIndex": xfRLTMHIndex,
       "xfRLTModuleIndex": xfRLTModuleIndex,
       "xfRLTEntPhysicalIndex": xfRLTEntPhysicalIndex,
       "xfRLTPhysicalCointainedIn": xfRLTPhysicalCointainedIn,
       "xfRLTPhysicalParentRelPos": xfRLTPhysicalParentRelPos,
       "xfRLTEntityPhysicalDescr": xfRLTEntityPhysicalDescr,
       "xfRLTModuleSlotPosition": xfRLTModuleSlotPosition,
       "xfRLTFEDistinguishedName": xfRLTFEDistinguishedName,
       "xfRLTNEDistinguishedName": xfRLTNEDistinguishedName,
       "xfRLTInterfaceIndex": xfRLTInterfaceIndex,
       "xfRLTHighestSeverityAlarm": xfRLTHighestSeverityAlarm,
       "xfRLTProtectionTable": xfRLTProtectionTable,
       "xfRLTProtectionEntry": xfRLTProtectionEntry,
       "xfRLTProtIndex": xfRLTProtIndex,
       "xfRLTProtectionSwitchMode": xfRLTProtectionSwitchMode,
       "xfRLTProtectionStatus": xfRLTProtectionStatus,
       "xfRLTRevertivePreferredTX": xfRLTRevertivePreferredTX,
       "xfRLTProtectionWaitToRestoreTime": xfRLTProtectionWaitToRestoreTime,
       "xfRLTFadeNotificationTimer": xfRLTFadeNotificationTimer,
       "xfRLTManualSwitchCommand": xfRLTManualSwitchCommand,
       "xfRLTTxSwitchOverConfiguration": xfRLTTxSwitchOverConfiguration,
       "xfRLTTxSwitchOverAlarmReset": xfRLTTxSwitchOverAlarmReset,
       "xfRLTNumOfRLPSwitch": xfRLTNumOfRLPSwitch,
       "xfRLTEnhancedACMProtectionMode": xfRLTEnhancedACMProtectionMode,
       "xfRLTEnhancedACMProtectionOperStatus": xfRLTEnhancedACMProtectionOperStatus,
       "xfRLTEncryptionTable": xfRLTEncryptionTable,
       "xfRLTEncryptionEntry": xfRLTEncryptionEntry,
       "xfRLTEncryptionIndex": xfRLTEncryptionIndex,
       "xfRLTEncryptionAdminStatus": xfRLTEncryptionAdminStatus,
       "xfRLTEncryptionOperStatus": xfRLTEncryptionOperStatus,
       "xfRLTEncryptionMasterKey": xfRLTEncryptionMasterKey,
       "xfRadioLinkRltPmObjects": xfRadioLinkRltPmObjects,
       "xfRLPMContinuousCounterTable": xfRLPMContinuousCounterTable,
       "xfRLPMContinuousCounterEntry": xfRLPMContinuousCounterEntry,
       "xfPMTimeElapsed": xfPMTimeElapsed,
       "xfPMCurrentES": xfPMCurrentES,
       "xfPMCurrentSES": xfPMCurrentSES,
       "xfPMCurrentBBE": xfPMCurrentBBE,
       "xfPMCurrentUAS": xfPMCurrentUAS,
       "xfPMCurrentBB": xfPMCurrentBB,
       "xfPMPerfReset": xfPMPerfReset,
       "xfPMCurrentESR": xfPMCurrentESR,
       "xfPMCurrentSESR": xfPMCurrentSESR,
       "xfPMCurrentBBER": xfPMCurrentBBER,
       "xfRLPMACMConfigTable": xfRLPMACMConfigTable,
       "xfRLPMACMConfigEntry": xfRLPMACMConfigEntry,
       "xfPMACMSetThreshold15m": xfPMACMSetThreshold15m,
       "xfPMACMSetThreshold24h": xfPMACMSetThreshold24h,
       "xfPMACMResetThreshold15m": xfPMACMResetThreshold15m,
       "xfPMACMStatus": xfPMACMStatus,
       "xfPMACMValidData": xfPMACMValidData,
       "xfRLPMACMCurrent24hTable": xfRLPMACMCurrent24hTable,
       "xfRLPMACMCurrent24hEntry": xfRLPMACMCurrent24hEntry,
       "xfPMACMCurrent24h4QAMStrong": xfPMACMCurrent24h4QAMStrong,
       "xfPMACMCurrent24h4QAMStd": xfPMACMCurrent24h4QAMStd,
       "xfPMACMCurrent24h4QAMLight": xfPMACMCurrent24h4QAMLight,
       "xfPMACMCurrent24h16QAMStrong": xfPMACMCurrent24h16QAMStrong,
       "xfPMACMCurrent24h16QAMStd": xfPMACMCurrent24h16QAMStd,
       "xfPMACMCurrent24h16QAMLight": xfPMACMCurrent24h16QAMLight,
       "xfPMACMCurrent24h32QAMStrong": xfPMACMCurrent24h32QAMStrong,
       "xfPMACMCurrent24h32QAMStd": xfPMACMCurrent24h32QAMStd,
       "xfPMACMCurrent24h32QAMLight": xfPMACMCurrent24h32QAMLight,
       "xfPMACMCurrent24h64QAMStrong": xfPMACMCurrent24h64QAMStrong,
       "xfPMACMCurrent24h64QAMStd": xfPMACMCurrent24h64QAMStd,
       "xfPMACMCurrent24h64QAMLight": xfPMACMCurrent24h64QAMLight,
       "xfPMACMCurrent24h128QAMStrong": xfPMACMCurrent24h128QAMStrong,
       "xfPMACMCurrent24h128QAMStd": xfPMACMCurrent24h128QAMStd,
       "xfPMACMCurrent24h128QAMLight": xfPMACMCurrent24h128QAMLight,
       "xfPMACMCurrent24h256QAMStrong": xfPMACMCurrent24h256QAMStrong,
       "xfPMACMCurrent24h256QAMStd": xfPMACMCurrent24h256QAMStd,
       "xfPMACMCurrent24h256QAMLight": xfPMACMCurrent24h256QAMLight,
       "xfPMACMCurrent24h512QAMStrong": xfPMACMCurrent24h512QAMStrong,
       "xfPMACMCurrent24h512QAMStd": xfPMACMCurrent24h512QAMStd,
       "xfPMACMCurrent24h512QAMLight": xfPMACMCurrent24h512QAMLight,
       "xfPMACMCurrent24h1024QAMStrong": xfPMACMCurrent24h1024QAMStrong,
       "xfPMACMCurrent24h1024QAMStd": xfPMACMCurrent24h1024QAMStd,
       "xfPMACMCurrent24h1024QAMLight": xfPMACMCurrent24h1024QAMLight,
       "xfPMACMCurrent24h2048QAMStrong": xfPMACMCurrent24h2048QAMStrong,
       "xfPMACMCurrent24h2048QAMStd": xfPMACMCurrent24h2048QAMStd,
       "xfPMACMCurrent24h2048QAMLight": xfPMACMCurrent24h2048QAMLight,
       "xfPMACMCurrent24h4096QAMStrong": xfPMACMCurrent24h4096QAMStrong,
       "xfPMACMCurrent24h4096QAMStd": xfPMACMCurrent24h4096QAMStd,
       "xfPMACMCurrent24h4096QAMLight": xfPMACMCurrent24h4096QAMLight,
       "xfPMACMCurrent24h8192QAMStrong": xfPMACMCurrent24h8192QAMStrong,
       "xfPMACMCurrent24h8192QAMStd": xfPMACMCurrent24h8192QAMStd,
       "xfPMACMCurrent24h8192QAMLight": xfPMACMCurrent24h8192QAMLight,
       "xfPMACMCurrent24h16384QAMStrong": xfPMACMCurrent24h16384QAMStrong,
       "xfPMACMCurrent24h16384QAMStd": xfPMACMCurrent24h16384QAMStd,
       "xfPMACMCurrent24h16384QAMLight": xfPMACMCurrent24h16384QAMLight,
       "xfRLPMACMInterval24hTable": xfRLPMACMInterval24hTable,
       "xfRLPMACMInterval24hEntry": xfRLPMACMInterval24hEntry,
       "xfPMACMInterval24h4QAMStrong": xfPMACMInterval24h4QAMStrong,
       "xfPMACMInterval24h4QAMStd": xfPMACMInterval24h4QAMStd,
       "xfPMACMInterval24h4QAMLight": xfPMACMInterval24h4QAMLight,
       "xfPMACMInterval24h16QAMStrong": xfPMACMInterval24h16QAMStrong,
       "xfPMACMInterval24h16QAMStd": xfPMACMInterval24h16QAMStd,
       "xfPMACMInterval24h16QAMLight": xfPMACMInterval24h16QAMLight,
       "xfPMACMInterval24h32QAMStrong": xfPMACMInterval24h32QAMStrong,
       "xfPMACMInterval24h32QAMStd": xfPMACMInterval24h32QAMStd,
       "xfPMACMInterval24h32QAMLight": xfPMACMInterval24h32QAMLight,
       "xfPMACMInterval24h64QAMStrong": xfPMACMInterval24h64QAMStrong,
       "xfPMACMInterval24h64QAMStd": xfPMACMInterval24h64QAMStd,
       "xfPMACMInterval24h64QAMLight": xfPMACMInterval24h64QAMLight,
       "xfPMACMInterval24h128QAMStrong": xfPMACMInterval24h128QAMStrong,
       "xfPMACMInterval24h128QAMStd": xfPMACMInterval24h128QAMStd,
       "xfPMACMInterval24h128QAMLight": xfPMACMInterval24h128QAMLight,
       "xfPMACMInterval24h256QAMStrong": xfPMACMInterval24h256QAMStrong,
       "xfPMACMInterval24h256QAMStd": xfPMACMInterval24h256QAMStd,
       "xfPMACMInterval24h256QAMLight": xfPMACMInterval24h256QAMLight,
       "xfPMACMInterval24h512QAMStrong": xfPMACMInterval24h512QAMStrong,
       "xfPMACMInterval24h512QAMStd": xfPMACMInterval24h512QAMStd,
       "xfPMACMInterval24h512QAMLight": xfPMACMInterval24h512QAMLight,
       "xfPMACMInterval24h1024QAMStrong": xfPMACMInterval24h1024QAMStrong,
       "xfPMACMInterval24h1024QAMStd": xfPMACMInterval24h1024QAMStd,
       "xfPMACMInterval24h1024QAMLight": xfPMACMInterval24h1024QAMLight,
       "xfPMACMInterval24h2048QAMStrong": xfPMACMInterval24h2048QAMStrong,
       "xfPMACMInterval24h2048QAMStd": xfPMACMInterval24h2048QAMStd,
       "xfPMACMInterval24h2048QAMLight": xfPMACMInterval24h2048QAMLight,
       "xfPMACMInterval24h4096QAMStrong": xfPMACMInterval24h4096QAMStrong,
       "xfPMACMInterval24h4096QAMStd": xfPMACMInterval24h4096QAMStd,
       "xfPMACMInterval24h4096QAMLight": xfPMACMInterval24h4096QAMLight,
       "xfPMACMInterval24hValidData": xfPMACMInterval24hValidData,
       "xfPMACMInterval24h8192QAMStrong": xfPMACMInterval24h8192QAMStrong,
       "xfPMACMInterval24h8192QAMStd": xfPMACMInterval24h8192QAMStd,
       "xfPMACMInterval24h8192QAMLight": xfPMACMInterval24h8192QAMLight,
       "xfPMACMInterval24h16384QAMStrong": xfPMACMInterval24h16384QAMStrong,
       "xfPMACMInterval24h16384QAMStd": xfPMACMInterval24h16384QAMStd,
       "xfPMACMInterval24h16384QAMLight": xfPMACMInterval24h16384QAMLight,
       "xfRLPMACMCurrent15mTable": xfRLPMACMCurrent15mTable,
       "xfRLPMACMCurrent15mEntry": xfRLPMACMCurrent15mEntry,
       "xfPMACMCurrent15m4QAMStrong": xfPMACMCurrent15m4QAMStrong,
       "xfPMACMCurrent15m4QAMStd": xfPMACMCurrent15m4QAMStd,
       "xfPMACMCurrent15m4QAMLight": xfPMACMCurrent15m4QAMLight,
       "xfPMACMCurrent15m16QAMStrong": xfPMACMCurrent15m16QAMStrong,
       "xfPMACMCurrent15m16QAMStd": xfPMACMCurrent15m16QAMStd,
       "xfPMACMCurrent15m16QAMLight": xfPMACMCurrent15m16QAMLight,
       "xfPMACMCurrent15m32QAMStrong": xfPMACMCurrent15m32QAMStrong,
       "xfPMACMCurrent15m32QAMStd": xfPMACMCurrent15m32QAMStd,
       "xfPMACMCurrent15m32QAMLight": xfPMACMCurrent15m32QAMLight,
       "xfPMACMCurrent15m64QAMStrong": xfPMACMCurrent15m64QAMStrong,
       "xfPMACMCurrent15m64QAMStd": xfPMACMCurrent15m64QAMStd,
       "xfPMACMCurrent15m64QAMLight": xfPMACMCurrent15m64QAMLight,
       "xfPMACMCurrent15m128QAMStrong": xfPMACMCurrent15m128QAMStrong,
       "xfPMACMCurrent15m128QAMStd": xfPMACMCurrent15m128QAMStd,
       "xfPMACMCurrent15m128QAMLight": xfPMACMCurrent15m128QAMLight,
       "xfPMACMCurrent15m256QAMStrong": xfPMACMCurrent15m256QAMStrong,
       "xfPMACMCurrent15m256QAMStd": xfPMACMCurrent15m256QAMStd,
       "xfPMACMCurrent15m256QAMLight": xfPMACMCurrent15m256QAMLight,
       "xfPMACMCurrent15m512QAMStrong": xfPMACMCurrent15m512QAMStrong,
       "xfPMACMCurrent15m512QAMStd": xfPMACMCurrent15m512QAMStd,
       "xfPMACMCurrent15m512QAMLight": xfPMACMCurrent15m512QAMLight,
       "xfPMACMCurrent15m1024QAMStrong": xfPMACMCurrent15m1024QAMStrong,
       "xfPMACMCurrent15m1024QAMStd": xfPMACMCurrent15m1024QAMStd,
       "xfPMACMCurrent15m1024QAMLight": xfPMACMCurrent15m1024QAMLight,
       "xfPMACMCurrent15m2048QAMStrong": xfPMACMCurrent15m2048QAMStrong,
       "xfPMACMCurrent15m2048QAMStd": xfPMACMCurrent15m2048QAMStd,
       "xfPMACMCurrent15m2048QAMLight": xfPMACMCurrent15m2048QAMLight,
       "xfPMACMCurrent15m4096QAMStrong": xfPMACMCurrent15m4096QAMStrong,
       "xfPMACMCurrent15m4096QAMStd": xfPMACMCurrent15m4096QAMStd,
       "xfPMACMCurrent15m4096QAMLight": xfPMACMCurrent15m4096QAMLight,
       "xfPMACMCurrent15m8192QAMStrong": xfPMACMCurrent15m8192QAMStrong,
       "xfPMACMCurrent15m8192QAMStd": xfPMACMCurrent15m8192QAMStd,
       "xfPMACMCurrent15m8192QAMLight": xfPMACMCurrent15m8192QAMLight,
       "xfPMACMCurrent15m16384QAMStrong": xfPMACMCurrent15m16384QAMStrong,
       "xfPMACMCurrent15m16384QAMStd": xfPMACMCurrent15m16384QAMStd,
       "xfPMACMCurrent15m16384QAMLight": xfPMACMCurrent15m16384QAMLight,
       "xfRLPMACMInterval15mTable": xfRLPMACMInterval15mTable,
       "xfRLPMACMInterval15mEntry": xfRLPMACMInterval15mEntry,
       "xfPMACMInterval15mIntervalNumber": xfPMACMInterval15mIntervalNumber,
       "xfPMACMInterval15m4QAMStrong": xfPMACMInterval15m4QAMStrong,
       "xfPMACMInterval15m4QAMStd": xfPMACMInterval15m4QAMStd,
       "xfPMACMInterval15m4QAMLight": xfPMACMInterval15m4QAMLight,
       "xfPMACMInterval15m16QAMStrong": xfPMACMInterval15m16QAMStrong,
       "xfPMACMInterval15m16QAMStd": xfPMACMInterval15m16QAMStd,
       "xfPMACMInterval15m16QAMLight": xfPMACMInterval15m16QAMLight,
       "xfPMACMInterval15m32QAMStrong": xfPMACMInterval15m32QAMStrong,
       "xfPMACMInterval15m32QAMStd": xfPMACMInterval15m32QAMStd,
       "xfPMACMInterval15m32QAMLight": xfPMACMInterval15m32QAMLight,
       "xfPMACMInterval15m64QAMStrong": xfPMACMInterval15m64QAMStrong,
       "xfPMACMInterval15m64QAMStd": xfPMACMInterval15m64QAMStd,
       "xfPMACMInterval15m64QAMLight": xfPMACMInterval15m64QAMLight,
       "xfPMACMInterval15m128QAMStrong": xfPMACMInterval15m128QAMStrong,
       "xfPMACMInterval15m128QAMStd": xfPMACMInterval15m128QAMStd,
       "xfPMACMInterval15m128QAMLight": xfPMACMInterval15m128QAMLight,
       "xfPMACMInterval15m256QAMStrong": xfPMACMInterval15m256QAMStrong,
       "xfPMACMInterval15m256QAMStd": xfPMACMInterval15m256QAMStd,
       "xfPMACMInterval15m256QAMLight": xfPMACMInterval15m256QAMLight,
       "xfPMACMInterval15m512QAMStrong": xfPMACMInterval15m512QAMStrong,
       "xfPMACMInterval15m512QAMStd": xfPMACMInterval15m512QAMStd,
       "xfPMACMInterval15m512QAMLight": xfPMACMInterval15m512QAMLight,
       "xfPMACMInterval15m1024QAMStrong": xfPMACMInterval15m1024QAMStrong,
       "xfPMACMInterval15m1024QAMStd": xfPMACMInterval15m1024QAMStd,
       "xfPMACMInterval15m1024QAMLight": xfPMACMInterval15m1024QAMLight,
       "xfPMACMInterval15m2048QAMStrong": xfPMACMInterval15m2048QAMStrong,
       "xfPMACMInterval15m2048QAMStd": xfPMACMInterval15m2048QAMStd,
       "xfPMACMInterval15m2048QAMLight": xfPMACMInterval15m2048QAMLight,
       "xfPMACMInterval15m4096QAMStrong": xfPMACMInterval15m4096QAMStrong,
       "xfPMACMInterval15m4096QAMStd": xfPMACMInterval15m4096QAMStd,
       "xfPMACMInterval15m4096QAMLight": xfPMACMInterval15m4096QAMLight,
       "xfPMACMInterval15mValidData": xfPMACMInterval15mValidData,
       "xfPMACMInterval15m8192QAMStrong": xfPMACMInterval15m8192QAMStrong,
       "xfPMACMInterval15m8192QAMStd": xfPMACMInterval15m8192QAMStd,
       "xfPMACMInterval15m8192QAMLight": xfPMACMInterval15m8192QAMLight,
       "xfPMACMInterval15m16384QAMStrong": xfPMACMInterval15m16384QAMStrong,
       "xfPMACMInterval15m16384QAMStd": xfPMACMInterval15m16384QAMStd,
       "xfPMACMInterval15m16384QAMLight": xfPMACMInterval15m16384QAMLight,
       "xfRLPMMimoCurrentTable": xfRLPMMimoCurrentTable,
       "xfRLPMMimoCurrentEntry": xfRLPMMimoCurrentEntry,
       "xfPMPerfCurrentEta": xfPMPerfCurrentEta,
       "xfPMPerfEtaMinLast7days": xfPMPerfEtaMinLast7days,
       "xfPMPerfEtaMaxLast7days": xfPMPerfEtaMaxLast7days,
       "xfRLPMMimoCurrent24hTable": xfRLPMMimoCurrent24hTable,
       "xfRLPMMimoCurrent24hEntry": xfRLPMMimoCurrent24hEntry,
       "xfPMPerfCurrent24hElapsedTime": xfPMPerfCurrent24hElapsedTime,
       "xfPMPerfCurrent24hEtaMin": xfPMPerfCurrent24hEtaMin,
       "xfPMPerfCurrent24hEtaMax": xfPMPerfCurrent24hEtaMax,
       "xfRLPMMimoInterval24hTable": xfRLPMMimoInterval24hTable,
       "xfRLPMMimoInterval24hEntry": xfRLPMMimoInterval24hEntry,
       "xfPMPerfInterval24hValidData": xfPMPerfInterval24hValidData,
       "xfPMPerfInterval24hEtaMin": xfPMPerfInterval24hEtaMin,
       "xfPMPerfInterval24hEtaMax": xfPMPerfInterval24hEtaMax,
       "xfRLPMMimoCurrent15mTable": xfRLPMMimoCurrent15mTable,
       "xfRLPMMimoCurrent15mEntry": xfRLPMMimoCurrent15mEntry,
       "xfPMPerfCurrent15mElapsedTime": xfPMPerfCurrent15mElapsedTime,
       "xfPMPerfCurrent15mEtaMin": xfPMPerfCurrent15mEtaMin,
       "xfPMPerfCurrent15mEtaMax": xfPMPerfCurrent15mEtaMax,
       "xfRLPMMimoInterval15mTable": xfRLPMMimoInterval15mTable,
       "xfRLPMMimoInterval15mEntry": xfRLPMMimoInterval15mEntry,
       "xfPMPerfInterval15mIntervalNumber": xfPMPerfInterval15mIntervalNumber,
       "xfPMPerfInterval15mEtaMin": xfPMPerfInterval15mEtaMin,
       "xfPMPerfInterval15mEtaMax": xfPMPerfInterval15mEtaMax,
       "xfPMPerfInterval15mValidData": xfPMPerfInterval15mValidData,
       "xfRadioLinkRltConformance": xfRadioLinkRltConformance,
       "xfRadioLinkRltCompliances": xfRadioLinkRltCompliances,
       "xfRadioLinkRltFullCompliance": xfRadioLinkRltFullCompliance,
       "xfRadioLinkRltGroups": xfRadioLinkRltGroups,
       "xfRadioLinkRltCompleteGroup": xfRadioLinkRltCompleteGroup}
)
