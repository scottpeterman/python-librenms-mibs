# SNMP MIB module (HH3C-VLANTERM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-VLANTERM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:14 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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


# MODULE-IDENTITY

hh3cVlanTerm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 193)
)
if mibBuilder.loadTexts:
    hh3cVlanTerm.setRevisions(
        ("2020-09-01 16:38",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cVlanTermObjects_ObjectIdentity = ObjectIdentity
hh3cVlanTermObjects = _Hh3cVlanTermObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 193, 1)
)
_Hh3cVlanTermDot1qTable_Object = MibTable
hh3cVlanTermDot1qTable = _Hh3cVlanTermDot1qTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 193, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cVlanTermDot1qTable.setStatus("current")
_Hh3cVlanTermDot1qEntry_Object = MibTableRow
hh3cVlanTermDot1qEntry = _Hh3cVlanTermDot1qEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 193, 1, 1, 1)
)
hh3cVlanTermDot1qEntry.setIndexNames(
    (0, "HH3C-VLANTERM-MIB", "hh3cVlanTermDot1qIfIndex"),
    (0, "HH3C-VLANTERM-MIB", "hh3cVlanTermDot1qVidStart"),
)
if mibBuilder.loadTexts:
    hh3cVlanTermDot1qEntry.setStatus("current")
_Hh3cVlanTermDot1qIfIndex_Type = InterfaceIndex
_Hh3cVlanTermDot1qIfIndex_Object = MibTableColumn
hh3cVlanTermDot1qIfIndex = _Hh3cVlanTermDot1qIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 193, 1, 1, 1, 1),
    _Hh3cVlanTermDot1qIfIndex_Type()
)
hh3cVlanTermDot1qIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVlanTermDot1qIfIndex.setStatus("current")


class _Hh3cVlanTermDot1qVidStart_Type(Unsigned32):
    """Custom type hh3cVlanTermDot1qVidStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cVlanTermDot1qVidStart_Type.__name__ = "Unsigned32"
_Hh3cVlanTermDot1qVidStart_Object = MibTableColumn
hh3cVlanTermDot1qVidStart = _Hh3cVlanTermDot1qVidStart_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 193, 1, 1, 1, 2),
    _Hh3cVlanTermDot1qVidStart_Type()
)
hh3cVlanTermDot1qVidStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVlanTermDot1qVidStart.setStatus("current")


class _Hh3cVlanTermDot1qVidEnd_Type(Unsigned32):
    """Custom type hh3cVlanTermDot1qVidEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cVlanTermDot1qVidEnd_Type.__name__ = "Unsigned32"
_Hh3cVlanTermDot1qVidEnd_Object = MibTableColumn
hh3cVlanTermDot1qVidEnd = _Hh3cVlanTermDot1qVidEnd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 193, 1, 1, 1, 3),
    _Hh3cVlanTermDot1qVidEnd_Type()
)
hh3cVlanTermDot1qVidEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVlanTermDot1qVidEnd.setStatus("current")


class _Hh3cVlanTermDot1qEncapFlag_Type(Integer32):
    """Custom type hh3cVlanTermDot1qEncapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("strict", 0),
          ("loose", 1))
    )


_Hh3cVlanTermDot1qEncapFlag_Type.__name__ = "Integer32"
_Hh3cVlanTermDot1qEncapFlag_Object = MibTableColumn
hh3cVlanTermDot1qEncapFlag = _Hh3cVlanTermDot1qEncapFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 193, 1, 1, 1, 4),
    _Hh3cVlanTermDot1qEncapFlag_Type()
)
hh3cVlanTermDot1qEncapFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVlanTermDot1qEncapFlag.setStatus("current")
_Hh3cVlanTermDot1qIsUserVlanMode_Type = TruthValue
_Hh3cVlanTermDot1qIsUserVlanMode_Object = MibTableColumn
hh3cVlanTermDot1qIsUserVlanMode = _Hh3cVlanTermDot1qIsUserVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 193, 1, 1, 1, 5),
    _Hh3cVlanTermDot1qIsUserVlanMode_Type()
)
hh3cVlanTermDot1qIsUserVlanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVlanTermDot1qIsUserVlanMode.setStatus("current")
_Hh3cVlanTermQinqTable_Object = MibTable
hh3cVlanTermQinqTable = _Hh3cVlanTermQinqTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 193, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cVlanTermQinqTable.setStatus("current")
_Hh3cVlanTermQinqEntry_Object = MibTableRow
hh3cVlanTermQinqEntry = _Hh3cVlanTermQinqEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 193, 1, 2, 1)
)
hh3cVlanTermQinqEntry.setIndexNames(
    (0, "HH3C-VLANTERM-MIB", "hh3cVlanTermQinQIfIndex"),
    (0, "HH3C-VLANTERM-MIB", "hh3cVlanTermQinQFirstVlan"),
    (0, "HH3C-VLANTERM-MIB", "hh3cVlanTermQinQSecondVlanStart"),
)
if mibBuilder.loadTexts:
    hh3cVlanTermQinqEntry.setStatus("current")
_Hh3cVlanTermQinQIfIndex_Type = InterfaceIndex
_Hh3cVlanTermQinQIfIndex_Object = MibTableColumn
hh3cVlanTermQinQIfIndex = _Hh3cVlanTermQinQIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 193, 1, 2, 1, 1),
    _Hh3cVlanTermQinQIfIndex_Type()
)
hh3cVlanTermQinQIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVlanTermQinQIfIndex.setStatus("current")


class _Hh3cVlanTermQinQFirstVlan_Type(Unsigned32):
    """Custom type hh3cVlanTermQinQFirstVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cVlanTermQinQFirstVlan_Type.__name__ = "Unsigned32"
_Hh3cVlanTermQinQFirstVlan_Object = MibTableColumn
hh3cVlanTermQinQFirstVlan = _Hh3cVlanTermQinQFirstVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 193, 1, 2, 1, 2),
    _Hh3cVlanTermQinQFirstVlan_Type()
)
hh3cVlanTermQinQFirstVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVlanTermQinQFirstVlan.setStatus("current")


class _Hh3cVlanTermQinQSecondVlanStart_Type(Unsigned32):
    """Custom type hh3cVlanTermQinQSecondVlanStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Hh3cVlanTermQinQSecondVlanStart_Type.__name__ = "Unsigned32"
_Hh3cVlanTermQinQSecondVlanStart_Object = MibTableColumn
hh3cVlanTermQinQSecondVlanStart = _Hh3cVlanTermQinQSecondVlanStart_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 193, 1, 2, 1, 3),
    _Hh3cVlanTermQinQSecondVlanStart_Type()
)
hh3cVlanTermQinQSecondVlanStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVlanTermQinQSecondVlanStart.setStatus("current")


class _Hh3cVlanTermQinQSecondVlanEnd_Type(Unsigned32):
    """Custom type hh3cVlanTermQinQSecondVlanEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Hh3cVlanTermQinQSecondVlanEnd_Type.__name__ = "Unsigned32"
_Hh3cVlanTermQinQSecondVlanEnd_Object = MibTableColumn
hh3cVlanTermQinQSecondVlanEnd = _Hh3cVlanTermQinQSecondVlanEnd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 193, 1, 2, 1, 4),
    _Hh3cVlanTermQinQSecondVlanEnd_Type()
)
hh3cVlanTermQinQSecondVlanEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVlanTermQinQSecondVlanEnd.setStatus("current")
_Hh3cVlanTermQinQQinqAny_Type = TruthValue
_Hh3cVlanTermQinQQinqAny_Object = MibTableColumn
hh3cVlanTermQinQQinqAny = _Hh3cVlanTermQinQQinqAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 193, 1, 2, 1, 5),
    _Hh3cVlanTermQinQQinqAny_Type()
)
hh3cVlanTermQinQQinqAny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVlanTermQinQQinqAny.setStatus("current")


class _Hh3cVlanTermQinQEncapFlag_Type(Integer32):
    """Custom type hh3cVlanTermQinQEncapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("strict", 0),
          ("loose", 1))
    )


_Hh3cVlanTermQinQEncapFlag_Type.__name__ = "Integer32"
_Hh3cVlanTermQinQEncapFlag_Object = MibTableColumn
hh3cVlanTermQinQEncapFlag = _Hh3cVlanTermQinQEncapFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 193, 1, 2, 1, 6),
    _Hh3cVlanTermQinQEncapFlag_Type()
)
hh3cVlanTermQinQEncapFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVlanTermQinQEncapFlag.setStatus("current")
_Hh3cVlanTermQinQIsUserVlanMode_Type = TruthValue
_Hh3cVlanTermQinQIsUserVlanMode_Object = MibTableColumn
hh3cVlanTermQinQIsUserVlanMode = _Hh3cVlanTermQinQIsUserVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 193, 1, 2, 1, 7),
    _Hh3cVlanTermQinQIsUserVlanMode_Type()
)
hh3cVlanTermQinQIsUserVlanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVlanTermQinQIsUserVlanMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-VLANTERM-MIB",
    **{"hh3cVlanTerm": hh3cVlanTerm,
       "hh3cVlanTermObjects": hh3cVlanTermObjects,
       "hh3cVlanTermDot1qTable": hh3cVlanTermDot1qTable,
       "hh3cVlanTermDot1qEntry": hh3cVlanTermDot1qEntry,
       "hh3cVlanTermDot1qIfIndex": hh3cVlanTermDot1qIfIndex,
       "hh3cVlanTermDot1qVidStart": hh3cVlanTermDot1qVidStart,
       "hh3cVlanTermDot1qVidEnd": hh3cVlanTermDot1qVidEnd,
       "hh3cVlanTermDot1qEncapFlag": hh3cVlanTermDot1qEncapFlag,
       "hh3cVlanTermDot1qIsUserVlanMode": hh3cVlanTermDot1qIsUserVlanMode,
       "hh3cVlanTermQinqTable": hh3cVlanTermQinqTable,
       "hh3cVlanTermQinqEntry": hh3cVlanTermQinqEntry,
       "hh3cVlanTermQinQIfIndex": hh3cVlanTermQinQIfIndex,
       "hh3cVlanTermQinQFirstVlan": hh3cVlanTermQinQFirstVlan,
       "hh3cVlanTermQinQSecondVlanStart": hh3cVlanTermQinQSecondVlanStart,
       "hh3cVlanTermQinQSecondVlanEnd": hh3cVlanTermQinQSecondVlanEnd,
       "hh3cVlanTermQinQQinqAny": hh3cVlanTermQinQQinqAny,
       "hh3cVlanTermQinQEncapFlag": hh3cVlanTermQinQEncapFlag,
       "hh3cVlanTermQinQIsUserVlanMode": hh3cVlanTermQinQIsUserVlanMode}
)
