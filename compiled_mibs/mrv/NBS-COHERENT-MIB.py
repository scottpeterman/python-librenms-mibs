# SNMP MIB module (NBS-COHERENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mrv\NBS-COHERENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:11 2025
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

(nbs,) = mibBuilder.importSymbols(
    "NBS-MIB",
    "nbs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nbsCoherentMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 242)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsCoherentCfgGrp_ObjectIdentity = ObjectIdentity
nbsCoherentCfgGrp = _NbsCoherentCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 242, 10)
)
if mibBuilder.loadTexts:
    nbsCoherentCfgGrp.setStatus("current")
_NbsCoherentCfgTable_Object = MibTable
nbsCoherentCfgTable = _NbsCoherentCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 10, 2)
)
if mibBuilder.loadTexts:
    nbsCoherentCfgTable.setStatus("current")
_NbsCoherentCfgEntry_Object = MibTableRow
nbsCoherentCfgEntry = _NbsCoherentCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 10, 2, 1)
)
nbsCoherentCfgEntry.setIndexNames(
    (0, "NBS-COHERENT-MIB", "nbsCoherentCfgIfIndex"),
)
if mibBuilder.loadTexts:
    nbsCoherentCfgEntry.setStatus("current")
_NbsCoherentCfgIfIndex_Type = InterfaceIndex
_NbsCoherentCfgIfIndex_Object = MibTableColumn
nbsCoherentCfgIfIndex = _NbsCoherentCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 10, 2, 1, 1),
    _NbsCoherentCfgIfIndex_Type()
)
nbsCoherentCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentCfgIfIndex.setStatus("current")


class _NbsCoherentCfgCDmodeCaps_Type(OctetString):
    """Custom type nbsCoherentCfgCDmodeCaps based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_NbsCoherentCfgCDmodeCaps_Type.__name__ = "OctetString"
_NbsCoherentCfgCDmodeCaps_Object = MibTableColumn
nbsCoherentCfgCDmodeCaps = _NbsCoherentCfgCDmodeCaps_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 10, 2, 1, 3),
    _NbsCoherentCfgCDmodeCaps_Type()
)
nbsCoherentCfgCDmodeCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentCfgCDmodeCaps.setStatus("current")


class _NbsCoherentCfgCDmodeAdmin_Type(Integer32):
    """Custom type nbsCoherentCfgCDmodeAdmin based on Integer32"""
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
        *(("notSupported", 1),
          ("disable", 2),
          ("auto", 3),
          ("fixed", 4))
    )


_NbsCoherentCfgCDmodeAdmin_Type.__name__ = "Integer32"
_NbsCoherentCfgCDmodeAdmin_Object = MibTableColumn
nbsCoherentCfgCDmodeAdmin = _NbsCoherentCfgCDmodeAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 10, 2, 1, 12),
    _NbsCoherentCfgCDmodeAdmin_Type()
)
nbsCoherentCfgCDmodeAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCoherentCfgCDmodeAdmin.setStatus("current")


class _NbsCoherentCfgCDmodeOper_Type(Integer32):
    """Custom type nbsCoherentCfgCDmodeOper based on Integer32"""
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
        *(("notSupported", 1),
          ("disable", 2),
          ("auto", 3),
          ("fixed", 4))
    )


_NbsCoherentCfgCDmodeOper_Type.__name__ = "Integer32"
_NbsCoherentCfgCDmodeOper_Object = MibTableColumn
nbsCoherentCfgCDmodeOper = _NbsCoherentCfgCDmodeOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 10, 2, 1, 13),
    _NbsCoherentCfgCDmodeOper_Type()
)
nbsCoherentCfgCDmodeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentCfgCDmodeOper.setStatus("current")


class _NbsCoherentCfgCDautolAdmin_Type(Integer32):
    """Custom type nbsCoherentCfgCDautolAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsCoherentCfgCDautolAdmin_Type.__name__ = "Integer32"
_NbsCoherentCfgCDautolAdmin_Object = MibTableColumn
nbsCoherentCfgCDautolAdmin = _NbsCoherentCfgCDautolAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 10, 2, 1, 14),
    _NbsCoherentCfgCDautolAdmin_Type()
)
nbsCoherentCfgCDautolAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCoherentCfgCDautolAdmin.setStatus("current")


class _NbsCoherentCfgCDautolOper_Type(Integer32):
    """Custom type nbsCoherentCfgCDautolOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsCoherentCfgCDautolOper_Type.__name__ = "Integer32"
_NbsCoherentCfgCDautolOper_Object = MibTableColumn
nbsCoherentCfgCDautolOper = _NbsCoherentCfgCDautolOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 10, 2, 1, 15),
    _NbsCoherentCfgCDautolOper_Type()
)
nbsCoherentCfgCDautolOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentCfgCDautolOper.setStatus("current")


class _NbsCoherentCfgCDautohAdmin_Type(Integer32):
    """Custom type nbsCoherentCfgCDautohAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsCoherentCfgCDautohAdmin_Type.__name__ = "Integer32"
_NbsCoherentCfgCDautohAdmin_Object = MibTableColumn
nbsCoherentCfgCDautohAdmin = _NbsCoherentCfgCDautohAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 10, 2, 1, 16),
    _NbsCoherentCfgCDautohAdmin_Type()
)
nbsCoherentCfgCDautohAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCoherentCfgCDautohAdmin.setStatus("current")


class _NbsCoherentCfgCDautohOper_Type(Integer32):
    """Custom type nbsCoherentCfgCDautohOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsCoherentCfgCDautohOper_Type.__name__ = "Integer32"
_NbsCoherentCfgCDautohOper_Object = MibTableColumn
nbsCoherentCfgCDautohOper = _NbsCoherentCfgCDautohOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 10, 2, 1, 17),
    _NbsCoherentCfgCDautohOper_Type()
)
nbsCoherentCfgCDautohOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentCfgCDautohOper.setStatus("current")


class _NbsCoherentCfgCDfixedAdmin_Type(Integer32):
    """Custom type nbsCoherentCfgCDfixedAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsCoherentCfgCDfixedAdmin_Type.__name__ = "Integer32"
_NbsCoherentCfgCDfixedAdmin_Object = MibTableColumn
nbsCoherentCfgCDfixedAdmin = _NbsCoherentCfgCDfixedAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 10, 2, 1, 18),
    _NbsCoherentCfgCDfixedAdmin_Type()
)
nbsCoherentCfgCDfixedAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCoherentCfgCDfixedAdmin.setStatus("current")


class _NbsCoherentCfgCDfixedOper_Type(Integer32):
    """Custom type nbsCoherentCfgCDfixedOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsCoherentCfgCDfixedOper_Type.__name__ = "Integer32"
_NbsCoherentCfgCDfixedOper_Object = MibTableColumn
nbsCoherentCfgCDfixedOper = _NbsCoherentCfgCDfixedOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 10, 2, 1, 19),
    _NbsCoherentCfgCDfixedOper_Type()
)
nbsCoherentCfgCDfixedOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentCfgCDfixedOper.setStatus("current")


class _NbsCoherentCfgSOPmodeAdmin_Type(Integer32):
    """Custom type nbsCoherentCfgSOPmodeAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("standard", 2),
          ("enhanced", 3))
    )


_NbsCoherentCfgSOPmodeAdmin_Type.__name__ = "Integer32"
_NbsCoherentCfgSOPmodeAdmin_Object = MibTableColumn
nbsCoherentCfgSOPmodeAdmin = _NbsCoherentCfgSOPmodeAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 10, 2, 1, 22),
    _NbsCoherentCfgSOPmodeAdmin_Type()
)
nbsCoherentCfgSOPmodeAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCoherentCfgSOPmodeAdmin.setStatus("current")


class _NbsCoherentCfgSOPmodeOper_Type(Integer32):
    """Custom type nbsCoherentCfgSOPmodeOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("standard", 2),
          ("enhanced", 3))
    )


_NbsCoherentCfgSOPmodeOper_Type.__name__ = "Integer32"
_NbsCoherentCfgSOPmodeOper_Object = MibTableColumn
nbsCoherentCfgSOPmodeOper = _NbsCoherentCfgSOPmodeOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 10, 2, 1, 23),
    _NbsCoherentCfgSOPmodeOper_Type()
)
nbsCoherentCfgSOPmodeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentCfgSOPmodeOper.setStatus("current")
_NbsCohpmThresholdsGrp_ObjectIdentity = ObjectIdentity
nbsCohpmThresholdsGrp = _NbsCohpmThresholdsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 242, 21)
)
if mibBuilder.loadTexts:
    nbsCohpmThresholdsGrp.setStatus("current")
_NbsCohpmThresholdsTable_Object = MibTable
nbsCohpmThresholdsTable = _NbsCohpmThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1)
)
if mibBuilder.loadTexts:
    nbsCohpmThresholdsTable.setStatus("current")
_NbsCohpmThresholdsEntry_Object = MibTableRow
nbsCohpmThresholdsEntry = _NbsCohpmThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1)
)
nbsCohpmThresholdsEntry.setIndexNames(
    (0, "NBS-COHERENT-MIB", "nbsCohpmThresholdsIfIndex"),
    (0, "NBS-COHERENT-MIB", "nbsCohpmThresholdsInterval"),
)
if mibBuilder.loadTexts:
    nbsCohpmThresholdsEntry.setStatus("current")
_NbsCohpmThresholdsIfIndex_Type = InterfaceIndex
_NbsCohpmThresholdsIfIndex_Object = MibTableColumn
nbsCohpmThresholdsIfIndex = _NbsCohpmThresholdsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 1),
    _NbsCohpmThresholdsIfIndex_Type()
)
nbsCohpmThresholdsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsIfIndex.setStatus("current")


class _NbsCohpmThresholdsInterval_Type(Integer32):
    """Custom type nbsCohpmThresholdsInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("quarterHour", 1),
          ("twentyfourHour", 2))
    )


_NbsCohpmThresholdsInterval_Type.__name__ = "Integer32"
_NbsCohpmThresholdsInterval_Object = MibTableColumn
nbsCohpmThresholdsInterval = _NbsCohpmThresholdsInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 3),
    _NbsCohpmThresholdsInterval_Type()
)
nbsCohpmThresholdsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsInterval.setStatus("current")


class _NbsCohpmThresholdsAveNetBERsig_Type(Integer32):
    """Custom type nbsCohpmThresholdsAveNetBERsig based on Integer32"""
    defaultValue = 0


_NbsCohpmThresholdsAveNetBERsig_Type.__name__ = "Integer32"
_NbsCohpmThresholdsAveNetBERsig_Object = MibTableColumn
nbsCohpmThresholdsAveNetBERsig = _NbsCohpmThresholdsAveNetBERsig_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 11),
    _NbsCohpmThresholdsAveNetBERsig_Type()
)
nbsCohpmThresholdsAveNetBERsig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsAveNetBERsig.setStatus("current")


class _NbsCohpmThresholdsAveNetBERexp_Type(Integer32):
    """Custom type nbsCohpmThresholdsAveNetBERexp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmThresholdsAveNetBERexp_Type.__name__ = "Integer32"
_NbsCohpmThresholdsAveNetBERexp_Object = MibTableColumn
nbsCohpmThresholdsAveNetBERexp = _NbsCohpmThresholdsAveNetBERexp_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 12),
    _NbsCohpmThresholdsAveNetBERexp_Type()
)
nbsCohpmThresholdsAveNetBERexp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsAveNetBERexp.setStatus("current")


class _NbsCohpmThresholdsMinNetBERsig_Type(Integer32):
    """Custom type nbsCohpmThresholdsMinNetBERsig based on Integer32"""
    defaultValue = 0


_NbsCohpmThresholdsMinNetBERsig_Type.__name__ = "Integer32"
_NbsCohpmThresholdsMinNetBERsig_Object = MibTableColumn
nbsCohpmThresholdsMinNetBERsig = _NbsCohpmThresholdsMinNetBERsig_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 14),
    _NbsCohpmThresholdsMinNetBERsig_Type()
)
nbsCohpmThresholdsMinNetBERsig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMinNetBERsig.setStatus("current")


class _NbsCohpmThresholdsMinNetBERexp_Type(Integer32):
    """Custom type nbsCohpmThresholdsMinNetBERexp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmThresholdsMinNetBERexp_Type.__name__ = "Integer32"
_NbsCohpmThresholdsMinNetBERexp_Object = MibTableColumn
nbsCohpmThresholdsMinNetBERexp = _NbsCohpmThresholdsMinNetBERexp_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 15),
    _NbsCohpmThresholdsMinNetBERexp_Type()
)
nbsCohpmThresholdsMinNetBERexp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMinNetBERexp.setStatus("current")


class _NbsCohpmThresholdsMaxNetBERsig_Type(Integer32):
    """Custom type nbsCohpmThresholdsMaxNetBERsig based on Integer32"""
    defaultValue = 0


_NbsCohpmThresholdsMaxNetBERsig_Type.__name__ = "Integer32"
_NbsCohpmThresholdsMaxNetBERsig_Object = MibTableColumn
nbsCohpmThresholdsMaxNetBERsig = _NbsCohpmThresholdsMaxNetBERsig_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 17),
    _NbsCohpmThresholdsMaxNetBERsig_Type()
)
nbsCohpmThresholdsMaxNetBERsig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMaxNetBERsig.setStatus("current")


class _NbsCohpmThresholdsMaxNetBERexp_Type(Integer32):
    """Custom type nbsCohpmThresholdsMaxNetBERexp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmThresholdsMaxNetBERexp_Type.__name__ = "Integer32"
_NbsCohpmThresholdsMaxNetBERexp_Object = MibTableColumn
nbsCohpmThresholdsMaxNetBERexp = _NbsCohpmThresholdsMaxNetBERexp_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 18),
    _NbsCohpmThresholdsMaxNetBERexp_Type()
)
nbsCohpmThresholdsMaxNetBERexp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMaxNetBERexp.setStatus("current")


class _NbsCohpmThresholdsAveCD_Type(Integer32):
    """Custom type nbsCohpmThresholdsAveCD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmThresholdsAveCD_Type.__name__ = "Integer32"
_NbsCohpmThresholdsAveCD_Object = MibTableColumn
nbsCohpmThresholdsAveCD = _NbsCohpmThresholdsAveCD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 20),
    _NbsCohpmThresholdsAveCD_Type()
)
nbsCohpmThresholdsAveCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsAveCD.setStatus("current")


class _NbsCohpmThresholdsMinCD_Type(Integer32):
    """Custom type nbsCohpmThresholdsMinCD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmThresholdsMinCD_Type.__name__ = "Integer32"
_NbsCohpmThresholdsMinCD_Object = MibTableColumn
nbsCohpmThresholdsMinCD = _NbsCohpmThresholdsMinCD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 23),
    _NbsCohpmThresholdsMinCD_Type()
)
nbsCohpmThresholdsMinCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMinCD.setStatus("current")


class _NbsCohpmThresholdsMaxCD_Type(Integer32):
    """Custom type nbsCohpmThresholdsMaxCD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmThresholdsMaxCD_Type.__name__ = "Integer32"
_NbsCohpmThresholdsMaxCD_Object = MibTableColumn
nbsCohpmThresholdsMaxCD = _NbsCohpmThresholdsMaxCD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 26),
    _NbsCohpmThresholdsMaxCD_Type()
)
nbsCohpmThresholdsMaxCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMaxCD.setStatus("current")


class _NbsCohpmThresholdsAveDGD_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsAveDGD based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsAveDGD_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsAveDGD_Object = MibTableColumn
nbsCohpmThresholdsAveDGD = _NbsCohpmThresholdsAveDGD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 30),
    _NbsCohpmThresholdsAveDGD_Type()
)
nbsCohpmThresholdsAveDGD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsAveDGD.setStatus("current")


class _NbsCohpmThresholdsMinDGD_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsMinDGD based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsMinDGD_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsMinDGD_Object = MibTableColumn
nbsCohpmThresholdsMinDGD = _NbsCohpmThresholdsMinDGD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 33),
    _NbsCohpmThresholdsMinDGD_Type()
)
nbsCohpmThresholdsMinDGD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMinDGD.setStatus("current")


class _NbsCohpmThresholdsMaxDGD_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsMaxDGD based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsMaxDGD_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsMaxDGD_Object = MibTableColumn
nbsCohpmThresholdsMaxDGD = _NbsCohpmThresholdsMaxDGD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 36),
    _NbsCohpmThresholdsMaxDGD_Type()
)
nbsCohpmThresholdsMaxDGD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMaxDGD.setStatus("current")


class _NbsCohpmThresholdsAveQ_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsAveQ based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsAveQ_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsAveQ_Object = MibTableColumn
nbsCohpmThresholdsAveQ = _NbsCohpmThresholdsAveQ_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 40),
    _NbsCohpmThresholdsAveQ_Type()
)
nbsCohpmThresholdsAveQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsAveQ.setStatus("current")


class _NbsCohpmThresholdsMinQ_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsMinQ based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsMinQ_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsMinQ_Object = MibTableColumn
nbsCohpmThresholdsMinQ = _NbsCohpmThresholdsMinQ_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 43),
    _NbsCohpmThresholdsMinQ_Type()
)
nbsCohpmThresholdsMinQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMinQ.setStatus("current")


class _NbsCohpmThresholdsMaxQ_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsMaxQ based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsMaxQ_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsMaxQ_Object = MibTableColumn
nbsCohpmThresholdsMaxQ = _NbsCohpmThresholdsMaxQ_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 46),
    _NbsCohpmThresholdsMaxQ_Type()
)
nbsCohpmThresholdsMaxQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMaxQ.setStatus("current")


class _NbsCohpmThresholdsAveCFO_Type(Integer32):
    """Custom type nbsCohpmThresholdsAveCFO based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmThresholdsAveCFO_Type.__name__ = "Integer32"
_NbsCohpmThresholdsAveCFO_Object = MibTableColumn
nbsCohpmThresholdsAveCFO = _NbsCohpmThresholdsAveCFO_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 50),
    _NbsCohpmThresholdsAveCFO_Type()
)
nbsCohpmThresholdsAveCFO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsAveCFO.setStatus("current")


class _NbsCohpmThresholdsMinCFO_Type(Integer32):
    """Custom type nbsCohpmThresholdsMinCFO based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmThresholdsMinCFO_Type.__name__ = "Integer32"
_NbsCohpmThresholdsMinCFO_Object = MibTableColumn
nbsCohpmThresholdsMinCFO = _NbsCohpmThresholdsMinCFO_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 53),
    _NbsCohpmThresholdsMinCFO_Type()
)
nbsCohpmThresholdsMinCFO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMinCFO.setStatus("current")


class _NbsCohpmThresholdsMaxCFO_Type(Integer32):
    """Custom type nbsCohpmThresholdsMaxCFO based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmThresholdsMaxCFO_Type.__name__ = "Integer32"
_NbsCohpmThresholdsMaxCFO_Object = MibTableColumn
nbsCohpmThresholdsMaxCFO = _NbsCohpmThresholdsMaxCFO_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 56),
    _NbsCohpmThresholdsMaxCFO_Type()
)
nbsCohpmThresholdsMaxCFO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMaxCFO.setStatus("current")


class _NbsCohpmThresholdsAveOSNR_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsAveOSNR based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsAveOSNR_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsAveOSNR_Object = MibTableColumn
nbsCohpmThresholdsAveOSNR = _NbsCohpmThresholdsAveOSNR_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 60),
    _NbsCohpmThresholdsAveOSNR_Type()
)
nbsCohpmThresholdsAveOSNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsAveOSNR.setStatus("current")


class _NbsCohpmThresholdsMinOSNR_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsMinOSNR based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsMinOSNR_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsMinOSNR_Object = MibTableColumn
nbsCohpmThresholdsMinOSNR = _NbsCohpmThresholdsMinOSNR_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 63),
    _NbsCohpmThresholdsMinOSNR_Type()
)
nbsCohpmThresholdsMinOSNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMinOSNR.setStatus("current")


class _NbsCohpmThresholdsMaxOSNR_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsMaxOSNR based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsMaxOSNR_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsMaxOSNR_Object = MibTableColumn
nbsCohpmThresholdsMaxOSNR = _NbsCohpmThresholdsMaxOSNR_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 66),
    _NbsCohpmThresholdsMaxOSNR_Type()
)
nbsCohpmThresholdsMaxOSNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMaxOSNR.setStatus("current")


class _NbsCohpmThresholdsAveSNRx_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsAveSNRx based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsAveSNRx_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsAveSNRx_Object = MibTableColumn
nbsCohpmThresholdsAveSNRx = _NbsCohpmThresholdsAveSNRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 70),
    _NbsCohpmThresholdsAveSNRx_Type()
)
nbsCohpmThresholdsAveSNRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsAveSNRx.setStatus("current")


class _NbsCohpmThresholdsMinSNRx_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsMinSNRx based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsMinSNRx_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsMinSNRx_Object = MibTableColumn
nbsCohpmThresholdsMinSNRx = _NbsCohpmThresholdsMinSNRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 73),
    _NbsCohpmThresholdsMinSNRx_Type()
)
nbsCohpmThresholdsMinSNRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMinSNRx.setStatus("current")


class _NbsCohpmThresholdsMaxSNRx_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsMaxSNRx based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsMaxSNRx_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsMaxSNRx_Object = MibTableColumn
nbsCohpmThresholdsMaxSNRx = _NbsCohpmThresholdsMaxSNRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 76),
    _NbsCohpmThresholdsMaxSNRx_Type()
)
nbsCohpmThresholdsMaxSNRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMaxSNRx.setStatus("current")


class _NbsCohpmThresholdsAveSNRy_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsAveSNRy based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsAveSNRy_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsAveSNRy_Object = MibTableColumn
nbsCohpmThresholdsAveSNRy = _NbsCohpmThresholdsAveSNRy_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 80),
    _NbsCohpmThresholdsAveSNRy_Type()
)
nbsCohpmThresholdsAveSNRy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsAveSNRy.setStatus("current")


class _NbsCohpmThresholdsMinSNRy_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsMinSNRy based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsMinSNRy_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsMinSNRy_Object = MibTableColumn
nbsCohpmThresholdsMinSNRy = _NbsCohpmThresholdsMinSNRy_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 83),
    _NbsCohpmThresholdsMinSNRy_Type()
)
nbsCohpmThresholdsMinSNRy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMinSNRy.setStatus("current")


class _NbsCohpmThresholdsMaxSNRy_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsMaxSNRy based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsMaxSNRy_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsMaxSNRy_Object = MibTableColumn
nbsCohpmThresholdsMaxSNRy = _NbsCohpmThresholdsMaxSNRy_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 86),
    _NbsCohpmThresholdsMaxSNRy_Type()
)
nbsCohpmThresholdsMaxSNRy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMaxSNRy.setStatus("current")


class _NbsCohpmThresholdsAvePDL_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsAvePDL based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsAvePDL_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsAvePDL_Object = MibTableColumn
nbsCohpmThresholdsAvePDL = _NbsCohpmThresholdsAvePDL_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 90),
    _NbsCohpmThresholdsAvePDL_Type()
)
nbsCohpmThresholdsAvePDL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsAvePDL.setStatus("current")


class _NbsCohpmThresholdsMinPDL_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsMinPDL based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsMinPDL_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsMinPDL_Object = MibTableColumn
nbsCohpmThresholdsMinPDL = _NbsCohpmThresholdsMinPDL_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 93),
    _NbsCohpmThresholdsMinPDL_Type()
)
nbsCohpmThresholdsMinPDL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMinPDL.setStatus("current")


class _NbsCohpmThresholdsMaxPDL_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsMaxPDL based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsMaxPDL_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsMaxPDL_Object = MibTableColumn
nbsCohpmThresholdsMaxPDL = _NbsCohpmThresholdsMaxPDL_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 96),
    _NbsCohpmThresholdsMaxPDL_Type()
)
nbsCohpmThresholdsMaxPDL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMaxPDL.setStatus("current")


class _NbsCohpmThresholdsAveSOP_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsAveSOP based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsAveSOP_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsAveSOP_Object = MibTableColumn
nbsCohpmThresholdsAveSOP = _NbsCohpmThresholdsAveSOP_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 100),
    _NbsCohpmThresholdsAveSOP_Type()
)
nbsCohpmThresholdsAveSOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsAveSOP.setStatus("current")


class _NbsCohpmThresholdsMinSOP_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsMinSOP based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsMinSOP_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsMinSOP_Object = MibTableColumn
nbsCohpmThresholdsMinSOP = _NbsCohpmThresholdsMinSOP_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 103),
    _NbsCohpmThresholdsMinSOP_Type()
)
nbsCohpmThresholdsMinSOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMinSOP.setStatus("current")


class _NbsCohpmThresholdsMaxSOP_Type(Unsigned32):
    """Custom type nbsCohpmThresholdsMaxSOP based on Unsigned32"""
    defaultValue = 0


_NbsCohpmThresholdsMaxSOP_Type.__name__ = "Unsigned32"
_NbsCohpmThresholdsMaxSOP_Object = MibTableColumn
nbsCohpmThresholdsMaxSOP = _NbsCohpmThresholdsMaxSOP_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 21, 1, 1, 106),
    _NbsCohpmThresholdsMaxSOP_Type()
)
nbsCohpmThresholdsMaxSOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCohpmThresholdsMaxSOP.setStatus("current")
_NbsCohpmCurrentGrp_ObjectIdentity = ObjectIdentity
nbsCohpmCurrentGrp = _NbsCohpmCurrentGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 242, 22)
)
if mibBuilder.loadTexts:
    nbsCohpmCurrentGrp.setStatus("current")
_NbsCohpmCurrentTable_Object = MibTable
nbsCohpmCurrentTable = _NbsCohpmCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3)
)
if mibBuilder.loadTexts:
    nbsCohpmCurrentTable.setStatus("current")
_NbsCohpmCurrentEntry_Object = MibTableRow
nbsCohpmCurrentEntry = _NbsCohpmCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1)
)
nbsCohpmCurrentEntry.setIndexNames(
    (0, "NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
    (0, "NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
)
if mibBuilder.loadTexts:
    nbsCohpmCurrentEntry.setStatus("current")
_NbsCohpmCurrentIfIndex_Type = InterfaceIndex
_NbsCohpmCurrentIfIndex_Object = MibTableColumn
nbsCohpmCurrentIfIndex = _NbsCohpmCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 1),
    _NbsCohpmCurrentIfIndex_Type()
)
nbsCohpmCurrentIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentIfIndex.setStatus("current")


class _NbsCohpmCurrentInterval_Type(Integer32):
    """Custom type nbsCohpmCurrentInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("quarterHour", 1),
          ("twentyfourHour", 2))
    )


_NbsCohpmCurrentInterval_Type.__name__ = "Integer32"
_NbsCohpmCurrentInterval_Object = MibTableColumn
nbsCohpmCurrentInterval = _NbsCohpmCurrentInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 3),
    _NbsCohpmCurrentInterval_Type()
)
nbsCohpmCurrentInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentInterval.setStatus("current")
_NbsCohpmCurrentDate_Type = Integer32
_NbsCohpmCurrentDate_Object = MibTableColumn
nbsCohpmCurrentDate = _NbsCohpmCurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 5),
    _NbsCohpmCurrentDate_Type()
)
nbsCohpmCurrentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentDate.setStatus("current")
_NbsCohpmCurrentTime_Type = Integer32
_NbsCohpmCurrentTime_Object = MibTableColumn
nbsCohpmCurrentTime = _NbsCohpmCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 6),
    _NbsCohpmCurrentTime_Type()
)
nbsCohpmCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentTime.setStatus("current")


class _NbsCohpmCurrentAveNetBERsig_Type(Integer32):
    """Custom type nbsCohpmCurrentAveNetBERsig based on Integer32"""
    defaultValue = 0


_NbsCohpmCurrentAveNetBERsig_Type.__name__ = "Integer32"
_NbsCohpmCurrentAveNetBERsig_Object = MibTableColumn
nbsCohpmCurrentAveNetBERsig = _NbsCohpmCurrentAveNetBERsig_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 11),
    _NbsCohpmCurrentAveNetBERsig_Type()
)
nbsCohpmCurrentAveNetBERsig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentAveNetBERsig.setStatus("current")


class _NbsCohpmCurrentAveNetBERexp_Type(Integer32):
    """Custom type nbsCohpmCurrentAveNetBERexp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmCurrentAveNetBERexp_Type.__name__ = "Integer32"
_NbsCohpmCurrentAveNetBERexp_Object = MibTableColumn
nbsCohpmCurrentAveNetBERexp = _NbsCohpmCurrentAveNetBERexp_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 12),
    _NbsCohpmCurrentAveNetBERexp_Type()
)
nbsCohpmCurrentAveNetBERexp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentAveNetBERexp.setStatus("current")


class _NbsCohpmCurrentMinNetBERsig_Type(Integer32):
    """Custom type nbsCohpmCurrentMinNetBERsig based on Integer32"""
    defaultValue = 0


_NbsCohpmCurrentMinNetBERsig_Type.__name__ = "Integer32"
_NbsCohpmCurrentMinNetBERsig_Object = MibTableColumn
nbsCohpmCurrentMinNetBERsig = _NbsCohpmCurrentMinNetBERsig_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 14),
    _NbsCohpmCurrentMinNetBERsig_Type()
)
nbsCohpmCurrentMinNetBERsig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMinNetBERsig.setStatus("current")


class _NbsCohpmCurrentMinNetBERexp_Type(Integer32):
    """Custom type nbsCohpmCurrentMinNetBERexp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmCurrentMinNetBERexp_Type.__name__ = "Integer32"
_NbsCohpmCurrentMinNetBERexp_Object = MibTableColumn
nbsCohpmCurrentMinNetBERexp = _NbsCohpmCurrentMinNetBERexp_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 15),
    _NbsCohpmCurrentMinNetBERexp_Type()
)
nbsCohpmCurrentMinNetBERexp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMinNetBERexp.setStatus("current")


class _NbsCohpmCurrentMaxNetBERsig_Type(Integer32):
    """Custom type nbsCohpmCurrentMaxNetBERsig based on Integer32"""
    defaultValue = 0


_NbsCohpmCurrentMaxNetBERsig_Type.__name__ = "Integer32"
_NbsCohpmCurrentMaxNetBERsig_Object = MibTableColumn
nbsCohpmCurrentMaxNetBERsig = _NbsCohpmCurrentMaxNetBERsig_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 17),
    _NbsCohpmCurrentMaxNetBERsig_Type()
)
nbsCohpmCurrentMaxNetBERsig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMaxNetBERsig.setStatus("current")


class _NbsCohpmCurrentMaxNetBERexp_Type(Integer32):
    """Custom type nbsCohpmCurrentMaxNetBERexp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmCurrentMaxNetBERexp_Type.__name__ = "Integer32"
_NbsCohpmCurrentMaxNetBERexp_Object = MibTableColumn
nbsCohpmCurrentMaxNetBERexp = _NbsCohpmCurrentMaxNetBERexp_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 18),
    _NbsCohpmCurrentMaxNetBERexp_Type()
)
nbsCohpmCurrentMaxNetBERexp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMaxNetBERexp.setStatus("current")


class _NbsCohpmCurrentAveCD_Type(Integer32):
    """Custom type nbsCohpmCurrentAveCD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmCurrentAveCD_Type.__name__ = "Integer32"
_NbsCohpmCurrentAveCD_Object = MibTableColumn
nbsCohpmCurrentAveCD = _NbsCohpmCurrentAveCD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 20),
    _NbsCohpmCurrentAveCD_Type()
)
nbsCohpmCurrentAveCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentAveCD.setStatus("current")


class _NbsCohpmCurrentMinCD_Type(Integer32):
    """Custom type nbsCohpmCurrentMinCD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmCurrentMinCD_Type.__name__ = "Integer32"
_NbsCohpmCurrentMinCD_Object = MibTableColumn
nbsCohpmCurrentMinCD = _NbsCohpmCurrentMinCD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 23),
    _NbsCohpmCurrentMinCD_Type()
)
nbsCohpmCurrentMinCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMinCD.setStatus("current")


class _NbsCohpmCurrentMaxCD_Type(Integer32):
    """Custom type nbsCohpmCurrentMaxCD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmCurrentMaxCD_Type.__name__ = "Integer32"
_NbsCohpmCurrentMaxCD_Object = MibTableColumn
nbsCohpmCurrentMaxCD = _NbsCohpmCurrentMaxCD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 26),
    _NbsCohpmCurrentMaxCD_Type()
)
nbsCohpmCurrentMaxCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMaxCD.setStatus("current")


class _NbsCohpmCurrentAveDGD_Type(Unsigned32):
    """Custom type nbsCohpmCurrentAveDGD based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentAveDGD_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentAveDGD_Object = MibTableColumn
nbsCohpmCurrentAveDGD = _NbsCohpmCurrentAveDGD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 30),
    _NbsCohpmCurrentAveDGD_Type()
)
nbsCohpmCurrentAveDGD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentAveDGD.setStatus("current")


class _NbsCohpmCurrentMinDGD_Type(Unsigned32):
    """Custom type nbsCohpmCurrentMinDGD based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentMinDGD_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentMinDGD_Object = MibTableColumn
nbsCohpmCurrentMinDGD = _NbsCohpmCurrentMinDGD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 33),
    _NbsCohpmCurrentMinDGD_Type()
)
nbsCohpmCurrentMinDGD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMinDGD.setStatus("current")


class _NbsCohpmCurrentMaxDGD_Type(Unsigned32):
    """Custom type nbsCohpmCurrentMaxDGD based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentMaxDGD_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentMaxDGD_Object = MibTableColumn
nbsCohpmCurrentMaxDGD = _NbsCohpmCurrentMaxDGD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 36),
    _NbsCohpmCurrentMaxDGD_Type()
)
nbsCohpmCurrentMaxDGD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMaxDGD.setStatus("current")


class _NbsCohpmCurrentAveQ_Type(Unsigned32):
    """Custom type nbsCohpmCurrentAveQ based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentAveQ_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentAveQ_Object = MibTableColumn
nbsCohpmCurrentAveQ = _NbsCohpmCurrentAveQ_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 40),
    _NbsCohpmCurrentAveQ_Type()
)
nbsCohpmCurrentAveQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentAveQ.setStatus("current")


class _NbsCohpmCurrentMinQ_Type(Unsigned32):
    """Custom type nbsCohpmCurrentMinQ based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentMinQ_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentMinQ_Object = MibTableColumn
nbsCohpmCurrentMinQ = _NbsCohpmCurrentMinQ_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 43),
    _NbsCohpmCurrentMinQ_Type()
)
nbsCohpmCurrentMinQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMinQ.setStatus("current")


class _NbsCohpmCurrentMaxQ_Type(Unsigned32):
    """Custom type nbsCohpmCurrentMaxQ based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentMaxQ_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentMaxQ_Object = MibTableColumn
nbsCohpmCurrentMaxQ = _NbsCohpmCurrentMaxQ_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 46),
    _NbsCohpmCurrentMaxQ_Type()
)
nbsCohpmCurrentMaxQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMaxQ.setStatus("current")


class _NbsCohpmCurrentAveCFO_Type(Integer32):
    """Custom type nbsCohpmCurrentAveCFO based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmCurrentAveCFO_Type.__name__ = "Integer32"
_NbsCohpmCurrentAveCFO_Object = MibTableColumn
nbsCohpmCurrentAveCFO = _NbsCohpmCurrentAveCFO_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 50),
    _NbsCohpmCurrentAveCFO_Type()
)
nbsCohpmCurrentAveCFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentAveCFO.setStatus("current")


class _NbsCohpmCurrentMinCFO_Type(Integer32):
    """Custom type nbsCohpmCurrentMinCFO based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmCurrentMinCFO_Type.__name__ = "Integer32"
_NbsCohpmCurrentMinCFO_Object = MibTableColumn
nbsCohpmCurrentMinCFO = _NbsCohpmCurrentMinCFO_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 53),
    _NbsCohpmCurrentMinCFO_Type()
)
nbsCohpmCurrentMinCFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMinCFO.setStatus("current")


class _NbsCohpmCurrentMaxCFO_Type(Integer32):
    """Custom type nbsCohpmCurrentMaxCFO based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmCurrentMaxCFO_Type.__name__ = "Integer32"
_NbsCohpmCurrentMaxCFO_Object = MibTableColumn
nbsCohpmCurrentMaxCFO = _NbsCohpmCurrentMaxCFO_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 56),
    _NbsCohpmCurrentMaxCFO_Type()
)
nbsCohpmCurrentMaxCFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMaxCFO.setStatus("current")


class _NbsCohpmCurrentAveOSNR_Type(Unsigned32):
    """Custom type nbsCohpmCurrentAveOSNR based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentAveOSNR_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentAveOSNR_Object = MibTableColumn
nbsCohpmCurrentAveOSNR = _NbsCohpmCurrentAveOSNR_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 60),
    _NbsCohpmCurrentAveOSNR_Type()
)
nbsCohpmCurrentAveOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentAveOSNR.setStatus("current")


class _NbsCohpmCurrentMinOSNR_Type(Unsigned32):
    """Custom type nbsCohpmCurrentMinOSNR based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentMinOSNR_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentMinOSNR_Object = MibTableColumn
nbsCohpmCurrentMinOSNR = _NbsCohpmCurrentMinOSNR_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 63),
    _NbsCohpmCurrentMinOSNR_Type()
)
nbsCohpmCurrentMinOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMinOSNR.setStatus("current")


class _NbsCohpmCurrentMaxOSNR_Type(Unsigned32):
    """Custom type nbsCohpmCurrentMaxOSNR based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentMaxOSNR_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentMaxOSNR_Object = MibTableColumn
nbsCohpmCurrentMaxOSNR = _NbsCohpmCurrentMaxOSNR_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 66),
    _NbsCohpmCurrentMaxOSNR_Type()
)
nbsCohpmCurrentMaxOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMaxOSNR.setStatus("current")


class _NbsCohpmCurrentAveSNRx_Type(Unsigned32):
    """Custom type nbsCohpmCurrentAveSNRx based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentAveSNRx_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentAveSNRx_Object = MibTableColumn
nbsCohpmCurrentAveSNRx = _NbsCohpmCurrentAveSNRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 70),
    _NbsCohpmCurrentAveSNRx_Type()
)
nbsCohpmCurrentAveSNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentAveSNRx.setStatus("current")


class _NbsCohpmCurrentMinSNRx_Type(Unsigned32):
    """Custom type nbsCohpmCurrentMinSNRx based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentMinSNRx_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentMinSNRx_Object = MibTableColumn
nbsCohpmCurrentMinSNRx = _NbsCohpmCurrentMinSNRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 73),
    _NbsCohpmCurrentMinSNRx_Type()
)
nbsCohpmCurrentMinSNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMinSNRx.setStatus("current")


class _NbsCohpmCurrentMaxSNRx_Type(Unsigned32):
    """Custom type nbsCohpmCurrentMaxSNRx based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentMaxSNRx_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentMaxSNRx_Object = MibTableColumn
nbsCohpmCurrentMaxSNRx = _NbsCohpmCurrentMaxSNRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 76),
    _NbsCohpmCurrentMaxSNRx_Type()
)
nbsCohpmCurrentMaxSNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMaxSNRx.setStatus("current")


class _NbsCohpmCurrentAveSNRy_Type(Unsigned32):
    """Custom type nbsCohpmCurrentAveSNRy based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentAveSNRy_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentAveSNRy_Object = MibTableColumn
nbsCohpmCurrentAveSNRy = _NbsCohpmCurrentAveSNRy_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 80),
    _NbsCohpmCurrentAveSNRy_Type()
)
nbsCohpmCurrentAveSNRy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentAveSNRy.setStatus("current")


class _NbsCohpmCurrentMinSNRy_Type(Unsigned32):
    """Custom type nbsCohpmCurrentMinSNRy based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentMinSNRy_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentMinSNRy_Object = MibTableColumn
nbsCohpmCurrentMinSNRy = _NbsCohpmCurrentMinSNRy_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 83),
    _NbsCohpmCurrentMinSNRy_Type()
)
nbsCohpmCurrentMinSNRy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMinSNRy.setStatus("current")


class _NbsCohpmCurrentMaxSNRy_Type(Unsigned32):
    """Custom type nbsCohpmCurrentMaxSNRy based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentMaxSNRy_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentMaxSNRy_Object = MibTableColumn
nbsCohpmCurrentMaxSNRy = _NbsCohpmCurrentMaxSNRy_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 86),
    _NbsCohpmCurrentMaxSNRy_Type()
)
nbsCohpmCurrentMaxSNRy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMaxSNRy.setStatus("current")


class _NbsCohpmCurrentAvePDL_Type(Unsigned32):
    """Custom type nbsCohpmCurrentAvePDL based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentAvePDL_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentAvePDL_Object = MibTableColumn
nbsCohpmCurrentAvePDL = _NbsCohpmCurrentAvePDL_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 90),
    _NbsCohpmCurrentAvePDL_Type()
)
nbsCohpmCurrentAvePDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentAvePDL.setStatus("current")


class _NbsCohpmCurrentMinPDL_Type(Unsigned32):
    """Custom type nbsCohpmCurrentMinPDL based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentMinPDL_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentMinPDL_Object = MibTableColumn
nbsCohpmCurrentMinPDL = _NbsCohpmCurrentMinPDL_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 93),
    _NbsCohpmCurrentMinPDL_Type()
)
nbsCohpmCurrentMinPDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMinPDL.setStatus("current")


class _NbsCohpmCurrentMaxPDL_Type(Unsigned32):
    """Custom type nbsCohpmCurrentMaxPDL based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentMaxPDL_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentMaxPDL_Object = MibTableColumn
nbsCohpmCurrentMaxPDL = _NbsCohpmCurrentMaxPDL_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 96),
    _NbsCohpmCurrentMaxPDL_Type()
)
nbsCohpmCurrentMaxPDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMaxPDL.setStatus("current")


class _NbsCohpmCurrentAveSOP_Type(Unsigned32):
    """Custom type nbsCohpmCurrentAveSOP based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentAveSOP_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentAveSOP_Object = MibTableColumn
nbsCohpmCurrentAveSOP = _NbsCohpmCurrentAveSOP_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 100),
    _NbsCohpmCurrentAveSOP_Type()
)
nbsCohpmCurrentAveSOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentAveSOP.setStatus("current")


class _NbsCohpmCurrentMinSOP_Type(Unsigned32):
    """Custom type nbsCohpmCurrentMinSOP based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentMinSOP_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentMinSOP_Object = MibTableColumn
nbsCohpmCurrentMinSOP = _NbsCohpmCurrentMinSOP_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 103),
    _NbsCohpmCurrentMinSOP_Type()
)
nbsCohpmCurrentMinSOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMinSOP.setStatus("current")


class _NbsCohpmCurrentMaxSOP_Type(Unsigned32):
    """Custom type nbsCohpmCurrentMaxSOP based on Unsigned32"""
    defaultValue = 0


_NbsCohpmCurrentMaxSOP_Type.__name__ = "Unsigned32"
_NbsCohpmCurrentMaxSOP_Object = MibTableColumn
nbsCohpmCurrentMaxSOP = _NbsCohpmCurrentMaxSOP_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 22, 3, 1, 106),
    _NbsCohpmCurrentMaxSOP_Type()
)
nbsCohpmCurrentMaxSOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmCurrentMaxSOP.setStatus("current")
_NbsCohpmHistoricGrp_ObjectIdentity = ObjectIdentity
nbsCohpmHistoricGrp = _NbsCohpmHistoricGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 242, 23)
)
if mibBuilder.loadTexts:
    nbsCohpmHistoricGrp.setStatus("current")
_NbsCohpmHistoricTable_Object = MibTable
nbsCohpmHistoricTable = _NbsCohpmHistoricTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3)
)
if mibBuilder.loadTexts:
    nbsCohpmHistoricTable.setStatus("current")
_NbsCohpmHistoricEntry_Object = MibTableRow
nbsCohpmHistoricEntry = _NbsCohpmHistoricEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1)
)
nbsCohpmHistoricEntry.setIndexNames(
    (0, "NBS-COHERENT-MIB", "nbsCohpmHistoricIfIndex"),
    (0, "NBS-COHERENT-MIB", "nbsCohpmHistoricInterval"),
    (0, "NBS-COHERENT-MIB", "nbsCohpmHistoricSample"),
)
if mibBuilder.loadTexts:
    nbsCohpmHistoricEntry.setStatus("current")
_NbsCohpmHistoricIfIndex_Type = InterfaceIndex
_NbsCohpmHistoricIfIndex_Object = MibTableColumn
nbsCohpmHistoricIfIndex = _NbsCohpmHistoricIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 1),
    _NbsCohpmHistoricIfIndex_Type()
)
nbsCohpmHistoricIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricIfIndex.setStatus("current")


class _NbsCohpmHistoricInterval_Type(Integer32):
    """Custom type nbsCohpmHistoricInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("quarterHour", 1),
          ("twentyfourHour", 2))
    )


_NbsCohpmHistoricInterval_Type.__name__ = "Integer32"
_NbsCohpmHistoricInterval_Object = MibTableColumn
nbsCohpmHistoricInterval = _NbsCohpmHistoricInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 3),
    _NbsCohpmHistoricInterval_Type()
)
nbsCohpmHistoricInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsCohpmHistoricInterval.setStatus("current")
_NbsCohpmHistoricSample_Type = Integer32
_NbsCohpmHistoricSample_Object = MibTableColumn
nbsCohpmHistoricSample = _NbsCohpmHistoricSample_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 4),
    _NbsCohpmHistoricSample_Type()
)
nbsCohpmHistoricSample.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsCohpmHistoricSample.setStatus("current")
_NbsCohpmHistoricDate_Type = Integer32
_NbsCohpmHistoricDate_Object = MibTableColumn
nbsCohpmHistoricDate = _NbsCohpmHistoricDate_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 5),
    _NbsCohpmHistoricDate_Type()
)
nbsCohpmHistoricDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricDate.setStatus("current")
_NbsCohpmHistoricTime_Type = Integer32
_NbsCohpmHistoricTime_Object = MibTableColumn
nbsCohpmHistoricTime = _NbsCohpmHistoricTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 6),
    _NbsCohpmHistoricTime_Type()
)
nbsCohpmHistoricTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricTime.setStatus("current")


class _NbsCohpmHistoricAveNetBERsig_Type(Integer32):
    """Custom type nbsCohpmHistoricAveNetBERsig based on Integer32"""
    defaultValue = 0


_NbsCohpmHistoricAveNetBERsig_Type.__name__ = "Integer32"
_NbsCohpmHistoricAveNetBERsig_Object = MibTableColumn
nbsCohpmHistoricAveNetBERsig = _NbsCohpmHistoricAveNetBERsig_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 11),
    _NbsCohpmHistoricAveNetBERsig_Type()
)
nbsCohpmHistoricAveNetBERsig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricAveNetBERsig.setStatus("current")


class _NbsCohpmHistoricAveNetBERexp_Type(Integer32):
    """Custom type nbsCohpmHistoricAveNetBERexp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmHistoricAveNetBERexp_Type.__name__ = "Integer32"
_NbsCohpmHistoricAveNetBERexp_Object = MibTableColumn
nbsCohpmHistoricAveNetBERexp = _NbsCohpmHistoricAveNetBERexp_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 12),
    _NbsCohpmHistoricAveNetBERexp_Type()
)
nbsCohpmHistoricAveNetBERexp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricAveNetBERexp.setStatus("current")


class _NbsCohpmHistoricMinNetBERsig_Type(Integer32):
    """Custom type nbsCohpmHistoricMinNetBERsig based on Integer32"""
    defaultValue = 0


_NbsCohpmHistoricMinNetBERsig_Type.__name__ = "Integer32"
_NbsCohpmHistoricMinNetBERsig_Object = MibTableColumn
nbsCohpmHistoricMinNetBERsig = _NbsCohpmHistoricMinNetBERsig_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 14),
    _NbsCohpmHistoricMinNetBERsig_Type()
)
nbsCohpmHistoricMinNetBERsig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMinNetBERsig.setStatus("current")


class _NbsCohpmHistoricMinNetBERexp_Type(Integer32):
    """Custom type nbsCohpmHistoricMinNetBERexp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmHistoricMinNetBERexp_Type.__name__ = "Integer32"
_NbsCohpmHistoricMinNetBERexp_Object = MibTableColumn
nbsCohpmHistoricMinNetBERexp = _NbsCohpmHistoricMinNetBERexp_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 15),
    _NbsCohpmHistoricMinNetBERexp_Type()
)
nbsCohpmHistoricMinNetBERexp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMinNetBERexp.setStatus("current")


class _NbsCohpmHistoricMaxNetBERsig_Type(Integer32):
    """Custom type nbsCohpmHistoricMaxNetBERsig based on Integer32"""
    defaultValue = 0


_NbsCohpmHistoricMaxNetBERsig_Type.__name__ = "Integer32"
_NbsCohpmHistoricMaxNetBERsig_Object = MibTableColumn
nbsCohpmHistoricMaxNetBERsig = _NbsCohpmHistoricMaxNetBERsig_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 17),
    _NbsCohpmHistoricMaxNetBERsig_Type()
)
nbsCohpmHistoricMaxNetBERsig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMaxNetBERsig.setStatus("current")


class _NbsCohpmHistoricMaxNetBERexp_Type(Integer32):
    """Custom type nbsCohpmHistoricMaxNetBERexp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmHistoricMaxNetBERexp_Type.__name__ = "Integer32"
_NbsCohpmHistoricMaxNetBERexp_Object = MibTableColumn
nbsCohpmHistoricMaxNetBERexp = _NbsCohpmHistoricMaxNetBERexp_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 18),
    _NbsCohpmHistoricMaxNetBERexp_Type()
)
nbsCohpmHistoricMaxNetBERexp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMaxNetBERexp.setStatus("current")


class _NbsCohpmHistoricAveCD_Type(Integer32):
    """Custom type nbsCohpmHistoricAveCD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmHistoricAveCD_Type.__name__ = "Integer32"
_NbsCohpmHistoricAveCD_Object = MibTableColumn
nbsCohpmHistoricAveCD = _NbsCohpmHistoricAveCD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 20),
    _NbsCohpmHistoricAveCD_Type()
)
nbsCohpmHistoricAveCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricAveCD.setStatus("current")


class _NbsCohpmHistoricMinCD_Type(Integer32):
    """Custom type nbsCohpmHistoricMinCD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmHistoricMinCD_Type.__name__ = "Integer32"
_NbsCohpmHistoricMinCD_Object = MibTableColumn
nbsCohpmHistoricMinCD = _NbsCohpmHistoricMinCD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 23),
    _NbsCohpmHistoricMinCD_Type()
)
nbsCohpmHistoricMinCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMinCD.setStatus("current")


class _NbsCohpmHistoricMaxCD_Type(Integer32):
    """Custom type nbsCohpmHistoricMaxCD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmHistoricMaxCD_Type.__name__ = "Integer32"
_NbsCohpmHistoricMaxCD_Object = MibTableColumn
nbsCohpmHistoricMaxCD = _NbsCohpmHistoricMaxCD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 26),
    _NbsCohpmHistoricMaxCD_Type()
)
nbsCohpmHistoricMaxCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMaxCD.setStatus("current")


class _NbsCohpmHistoricAveDGD_Type(Unsigned32):
    """Custom type nbsCohpmHistoricAveDGD based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricAveDGD_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricAveDGD_Object = MibTableColumn
nbsCohpmHistoricAveDGD = _NbsCohpmHistoricAveDGD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 30),
    _NbsCohpmHistoricAveDGD_Type()
)
nbsCohpmHistoricAveDGD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricAveDGD.setStatus("current")


class _NbsCohpmHistoricMinDGD_Type(Unsigned32):
    """Custom type nbsCohpmHistoricMinDGD based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricMinDGD_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricMinDGD_Object = MibTableColumn
nbsCohpmHistoricMinDGD = _NbsCohpmHistoricMinDGD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 33),
    _NbsCohpmHistoricMinDGD_Type()
)
nbsCohpmHistoricMinDGD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMinDGD.setStatus("current")


class _NbsCohpmHistoricMaxDGD_Type(Unsigned32):
    """Custom type nbsCohpmHistoricMaxDGD based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricMaxDGD_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricMaxDGD_Object = MibTableColumn
nbsCohpmHistoricMaxDGD = _NbsCohpmHistoricMaxDGD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 36),
    _NbsCohpmHistoricMaxDGD_Type()
)
nbsCohpmHistoricMaxDGD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMaxDGD.setStatus("current")


class _NbsCohpmHistoricAveQ_Type(Unsigned32):
    """Custom type nbsCohpmHistoricAveQ based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricAveQ_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricAveQ_Object = MibTableColumn
nbsCohpmHistoricAveQ = _NbsCohpmHistoricAveQ_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 40),
    _NbsCohpmHistoricAveQ_Type()
)
nbsCohpmHistoricAveQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricAveQ.setStatus("current")


class _NbsCohpmHistoricMinQ_Type(Unsigned32):
    """Custom type nbsCohpmHistoricMinQ based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricMinQ_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricMinQ_Object = MibTableColumn
nbsCohpmHistoricMinQ = _NbsCohpmHistoricMinQ_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 43),
    _NbsCohpmHistoricMinQ_Type()
)
nbsCohpmHistoricMinQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMinQ.setStatus("current")


class _NbsCohpmHistoricMaxQ_Type(Unsigned32):
    """Custom type nbsCohpmHistoricMaxQ based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricMaxQ_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricMaxQ_Object = MibTableColumn
nbsCohpmHistoricMaxQ = _NbsCohpmHistoricMaxQ_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 46),
    _NbsCohpmHistoricMaxQ_Type()
)
nbsCohpmHistoricMaxQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMaxQ.setStatus("current")


class _NbsCohpmHistoricAveCFO_Type(Integer32):
    """Custom type nbsCohpmHistoricAveCFO based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmHistoricAveCFO_Type.__name__ = "Integer32"
_NbsCohpmHistoricAveCFO_Object = MibTableColumn
nbsCohpmHistoricAveCFO = _NbsCohpmHistoricAveCFO_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 50),
    _NbsCohpmHistoricAveCFO_Type()
)
nbsCohpmHistoricAveCFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricAveCFO.setStatus("current")


class _NbsCohpmHistoricMinCFO_Type(Integer32):
    """Custom type nbsCohpmHistoricMinCFO based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmHistoricMinCFO_Type.__name__ = "Integer32"
_NbsCohpmHistoricMinCFO_Object = MibTableColumn
nbsCohpmHistoricMinCFO = _NbsCohpmHistoricMinCFO_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 53),
    _NbsCohpmHistoricMinCFO_Type()
)
nbsCohpmHistoricMinCFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMinCFO.setStatus("current")


class _NbsCohpmHistoricMaxCFO_Type(Integer32):
    """Custom type nbsCohpmHistoricMaxCFO based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmHistoricMaxCFO_Type.__name__ = "Integer32"
_NbsCohpmHistoricMaxCFO_Object = MibTableColumn
nbsCohpmHistoricMaxCFO = _NbsCohpmHistoricMaxCFO_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 56),
    _NbsCohpmHistoricMaxCFO_Type()
)
nbsCohpmHistoricMaxCFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMaxCFO.setStatus("current")


class _NbsCohpmHistoricAveOSNR_Type(Unsigned32):
    """Custom type nbsCohpmHistoricAveOSNR based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricAveOSNR_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricAveOSNR_Object = MibTableColumn
nbsCohpmHistoricAveOSNR = _NbsCohpmHistoricAveOSNR_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 60),
    _NbsCohpmHistoricAveOSNR_Type()
)
nbsCohpmHistoricAveOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricAveOSNR.setStatus("current")


class _NbsCohpmHistoricMinOSNR_Type(Unsigned32):
    """Custom type nbsCohpmHistoricMinOSNR based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricMinOSNR_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricMinOSNR_Object = MibTableColumn
nbsCohpmHistoricMinOSNR = _NbsCohpmHistoricMinOSNR_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 63),
    _NbsCohpmHistoricMinOSNR_Type()
)
nbsCohpmHistoricMinOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMinOSNR.setStatus("current")


class _NbsCohpmHistoricMaxOSNR_Type(Unsigned32):
    """Custom type nbsCohpmHistoricMaxOSNR based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricMaxOSNR_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricMaxOSNR_Object = MibTableColumn
nbsCohpmHistoricMaxOSNR = _NbsCohpmHistoricMaxOSNR_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 66),
    _NbsCohpmHistoricMaxOSNR_Type()
)
nbsCohpmHistoricMaxOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMaxOSNR.setStatus("current")


class _NbsCohpmHistoricAveSNRx_Type(Unsigned32):
    """Custom type nbsCohpmHistoricAveSNRx based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricAveSNRx_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricAveSNRx_Object = MibTableColumn
nbsCohpmHistoricAveSNRx = _NbsCohpmHistoricAveSNRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 70),
    _NbsCohpmHistoricAveSNRx_Type()
)
nbsCohpmHistoricAveSNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricAveSNRx.setStatus("current")


class _NbsCohpmHistoricMinSNRx_Type(Unsigned32):
    """Custom type nbsCohpmHistoricMinSNRx based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricMinSNRx_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricMinSNRx_Object = MibTableColumn
nbsCohpmHistoricMinSNRx = _NbsCohpmHistoricMinSNRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 73),
    _NbsCohpmHistoricMinSNRx_Type()
)
nbsCohpmHistoricMinSNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMinSNRx.setStatus("current")


class _NbsCohpmHistoricMaxSNRx_Type(Unsigned32):
    """Custom type nbsCohpmHistoricMaxSNRx based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricMaxSNRx_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricMaxSNRx_Object = MibTableColumn
nbsCohpmHistoricMaxSNRx = _NbsCohpmHistoricMaxSNRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 76),
    _NbsCohpmHistoricMaxSNRx_Type()
)
nbsCohpmHistoricMaxSNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMaxSNRx.setStatus("current")


class _NbsCohpmHistoricAveSNRy_Type(Unsigned32):
    """Custom type nbsCohpmHistoricAveSNRy based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricAveSNRy_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricAveSNRy_Object = MibTableColumn
nbsCohpmHistoricAveSNRy = _NbsCohpmHistoricAveSNRy_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 80),
    _NbsCohpmHistoricAveSNRy_Type()
)
nbsCohpmHistoricAveSNRy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricAveSNRy.setStatus("current")


class _NbsCohpmHistoricMinSNRy_Type(Unsigned32):
    """Custom type nbsCohpmHistoricMinSNRy based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricMinSNRy_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricMinSNRy_Object = MibTableColumn
nbsCohpmHistoricMinSNRy = _NbsCohpmHistoricMinSNRy_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 83),
    _NbsCohpmHistoricMinSNRy_Type()
)
nbsCohpmHistoricMinSNRy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMinSNRy.setStatus("current")


class _NbsCohpmHistoricMaxSNRy_Type(Unsigned32):
    """Custom type nbsCohpmHistoricMaxSNRy based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricMaxSNRy_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricMaxSNRy_Object = MibTableColumn
nbsCohpmHistoricMaxSNRy = _NbsCohpmHistoricMaxSNRy_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 86),
    _NbsCohpmHistoricMaxSNRy_Type()
)
nbsCohpmHistoricMaxSNRy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMaxSNRy.setStatus("current")


class _NbsCohpmHistoricAvePDL_Type(Unsigned32):
    """Custom type nbsCohpmHistoricAvePDL based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricAvePDL_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricAvePDL_Object = MibTableColumn
nbsCohpmHistoricAvePDL = _NbsCohpmHistoricAvePDL_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 90),
    _NbsCohpmHistoricAvePDL_Type()
)
nbsCohpmHistoricAvePDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricAvePDL.setStatus("current")


class _NbsCohpmHistoricMinPDL_Type(Unsigned32):
    """Custom type nbsCohpmHistoricMinPDL based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricMinPDL_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricMinPDL_Object = MibTableColumn
nbsCohpmHistoricMinPDL = _NbsCohpmHistoricMinPDL_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 93),
    _NbsCohpmHistoricMinPDL_Type()
)
nbsCohpmHistoricMinPDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMinPDL.setStatus("current")


class _NbsCohpmHistoricMaxPDL_Type(Unsigned32):
    """Custom type nbsCohpmHistoricMaxPDL based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricMaxPDL_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricMaxPDL_Object = MibTableColumn
nbsCohpmHistoricMaxPDL = _NbsCohpmHistoricMaxPDL_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 96),
    _NbsCohpmHistoricMaxPDL_Type()
)
nbsCohpmHistoricMaxPDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMaxPDL.setStatus("current")


class _NbsCohpmHistoricAveSOP_Type(Unsigned32):
    """Custom type nbsCohpmHistoricAveSOP based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricAveSOP_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricAveSOP_Object = MibTableColumn
nbsCohpmHistoricAveSOP = _NbsCohpmHistoricAveSOP_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 100),
    _NbsCohpmHistoricAveSOP_Type()
)
nbsCohpmHistoricAveSOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricAveSOP.setStatus("current")


class _NbsCohpmHistoricMinSOP_Type(Unsigned32):
    """Custom type nbsCohpmHistoricMinSOP based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricMinSOP_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricMinSOP_Object = MibTableColumn
nbsCohpmHistoricMinSOP = _NbsCohpmHistoricMinSOP_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 103),
    _NbsCohpmHistoricMinSOP_Type()
)
nbsCohpmHistoricMinSOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMinSOP.setStatus("current")


class _NbsCohpmHistoricMaxSOP_Type(Unsigned32):
    """Custom type nbsCohpmHistoricMaxSOP based on Unsigned32"""
    defaultValue = 0


_NbsCohpmHistoricMaxSOP_Type.__name__ = "Unsigned32"
_NbsCohpmHistoricMaxSOP_Object = MibTableColumn
nbsCohpmHistoricMaxSOP = _NbsCohpmHistoricMaxSOP_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 23, 3, 1, 106),
    _NbsCohpmHistoricMaxSOP_Type()
)
nbsCohpmHistoricMaxSOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmHistoricMaxSOP.setStatus("current")
_NbsCohpmRunningGrp_ObjectIdentity = ObjectIdentity
nbsCohpmRunningGrp = _NbsCohpmRunningGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 242, 24)
)
if mibBuilder.loadTexts:
    nbsCohpmRunningGrp.setStatus("current")
_NbsCohpmRunningTable_Object = MibTable
nbsCohpmRunningTable = _NbsCohpmRunningTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3)
)
if mibBuilder.loadTexts:
    nbsCohpmRunningTable.setStatus("current")
_NbsCohpmRunningEntry_Object = MibTableRow
nbsCohpmRunningEntry = _NbsCohpmRunningEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1)
)
nbsCohpmRunningEntry.setIndexNames(
    (0, "NBS-COHERENT-MIB", "nbsCohpmRunningIfIndex"),
)
if mibBuilder.loadTexts:
    nbsCohpmRunningEntry.setStatus("current")
_NbsCohpmRunningIfIndex_Type = InterfaceIndex
_NbsCohpmRunningIfIndex_Object = MibTableColumn
nbsCohpmRunningIfIndex = _NbsCohpmRunningIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 1),
    _NbsCohpmRunningIfIndex_Type()
)
nbsCohpmRunningIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningIfIndex.setStatus("current")
_NbsCohpmRunningDate_Type = Integer32
_NbsCohpmRunningDate_Object = MibTableColumn
nbsCohpmRunningDate = _NbsCohpmRunningDate_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 5),
    _NbsCohpmRunningDate_Type()
)
nbsCohpmRunningDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningDate.setStatus("current")
_NbsCohpmRunningTime_Type = Integer32
_NbsCohpmRunningTime_Object = MibTableColumn
nbsCohpmRunningTime = _NbsCohpmRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 6),
    _NbsCohpmRunningTime_Type()
)
nbsCohpmRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningTime.setStatus("current")


class _NbsCohpmRunningAveNetBERsig_Type(Integer32):
    """Custom type nbsCohpmRunningAveNetBERsig based on Integer32"""
    defaultValue = 0


_NbsCohpmRunningAveNetBERsig_Type.__name__ = "Integer32"
_NbsCohpmRunningAveNetBERsig_Object = MibTableColumn
nbsCohpmRunningAveNetBERsig = _NbsCohpmRunningAveNetBERsig_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 11),
    _NbsCohpmRunningAveNetBERsig_Type()
)
nbsCohpmRunningAveNetBERsig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningAveNetBERsig.setStatus("current")


class _NbsCohpmRunningAveNetBERexp_Type(Integer32):
    """Custom type nbsCohpmRunningAveNetBERexp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmRunningAveNetBERexp_Type.__name__ = "Integer32"
_NbsCohpmRunningAveNetBERexp_Object = MibTableColumn
nbsCohpmRunningAveNetBERexp = _NbsCohpmRunningAveNetBERexp_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 12),
    _NbsCohpmRunningAveNetBERexp_Type()
)
nbsCohpmRunningAveNetBERexp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningAveNetBERexp.setStatus("current")


class _NbsCohpmRunningMinNetBERsig_Type(Integer32):
    """Custom type nbsCohpmRunningMinNetBERsig based on Integer32"""
    defaultValue = 0


_NbsCohpmRunningMinNetBERsig_Type.__name__ = "Integer32"
_NbsCohpmRunningMinNetBERsig_Object = MibTableColumn
nbsCohpmRunningMinNetBERsig = _NbsCohpmRunningMinNetBERsig_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 14),
    _NbsCohpmRunningMinNetBERsig_Type()
)
nbsCohpmRunningMinNetBERsig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMinNetBERsig.setStatus("current")


class _NbsCohpmRunningMinNetBERexp_Type(Integer32):
    """Custom type nbsCohpmRunningMinNetBERexp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmRunningMinNetBERexp_Type.__name__ = "Integer32"
_NbsCohpmRunningMinNetBERexp_Object = MibTableColumn
nbsCohpmRunningMinNetBERexp = _NbsCohpmRunningMinNetBERexp_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 15),
    _NbsCohpmRunningMinNetBERexp_Type()
)
nbsCohpmRunningMinNetBERexp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMinNetBERexp.setStatus("current")


class _NbsCohpmRunningMaxNetBERsig_Type(Integer32):
    """Custom type nbsCohpmRunningMaxNetBERsig based on Integer32"""
    defaultValue = 0


_NbsCohpmRunningMaxNetBERsig_Type.__name__ = "Integer32"
_NbsCohpmRunningMaxNetBERsig_Object = MibTableColumn
nbsCohpmRunningMaxNetBERsig = _NbsCohpmRunningMaxNetBERsig_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 17),
    _NbsCohpmRunningMaxNetBERsig_Type()
)
nbsCohpmRunningMaxNetBERsig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMaxNetBERsig.setStatus("current")


class _NbsCohpmRunningMaxNetBERexp_Type(Integer32):
    """Custom type nbsCohpmRunningMaxNetBERexp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmRunningMaxNetBERexp_Type.__name__ = "Integer32"
_NbsCohpmRunningMaxNetBERexp_Object = MibTableColumn
nbsCohpmRunningMaxNetBERexp = _NbsCohpmRunningMaxNetBERexp_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 18),
    _NbsCohpmRunningMaxNetBERexp_Type()
)
nbsCohpmRunningMaxNetBERexp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMaxNetBERexp.setStatus("current")


class _NbsCohpmRunningAveCD_Type(Integer32):
    """Custom type nbsCohpmRunningAveCD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmRunningAveCD_Type.__name__ = "Integer32"
_NbsCohpmRunningAveCD_Object = MibTableColumn
nbsCohpmRunningAveCD = _NbsCohpmRunningAveCD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 20),
    _NbsCohpmRunningAveCD_Type()
)
nbsCohpmRunningAveCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningAveCD.setStatus("current")


class _NbsCohpmRunningMinCD_Type(Integer32):
    """Custom type nbsCohpmRunningMinCD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmRunningMinCD_Type.__name__ = "Integer32"
_NbsCohpmRunningMinCD_Object = MibTableColumn
nbsCohpmRunningMinCD = _NbsCohpmRunningMinCD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 23),
    _NbsCohpmRunningMinCD_Type()
)
nbsCohpmRunningMinCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMinCD.setStatus("current")


class _NbsCohpmRunningMaxCD_Type(Integer32):
    """Custom type nbsCohpmRunningMaxCD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmRunningMaxCD_Type.__name__ = "Integer32"
_NbsCohpmRunningMaxCD_Object = MibTableColumn
nbsCohpmRunningMaxCD = _NbsCohpmRunningMaxCD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 26),
    _NbsCohpmRunningMaxCD_Type()
)
nbsCohpmRunningMaxCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMaxCD.setStatus("current")


class _NbsCohpmRunningAveDGD_Type(Unsigned32):
    """Custom type nbsCohpmRunningAveDGD based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningAveDGD_Type.__name__ = "Unsigned32"
_NbsCohpmRunningAveDGD_Object = MibTableColumn
nbsCohpmRunningAveDGD = _NbsCohpmRunningAveDGD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 30),
    _NbsCohpmRunningAveDGD_Type()
)
nbsCohpmRunningAveDGD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningAveDGD.setStatus("current")


class _NbsCohpmRunningMinDGD_Type(Unsigned32):
    """Custom type nbsCohpmRunningMinDGD based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningMinDGD_Type.__name__ = "Unsigned32"
_NbsCohpmRunningMinDGD_Object = MibTableColumn
nbsCohpmRunningMinDGD = _NbsCohpmRunningMinDGD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 33),
    _NbsCohpmRunningMinDGD_Type()
)
nbsCohpmRunningMinDGD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMinDGD.setStatus("current")


class _NbsCohpmRunningMaxDGD_Type(Unsigned32):
    """Custom type nbsCohpmRunningMaxDGD based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningMaxDGD_Type.__name__ = "Unsigned32"
_NbsCohpmRunningMaxDGD_Object = MibTableColumn
nbsCohpmRunningMaxDGD = _NbsCohpmRunningMaxDGD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 36),
    _NbsCohpmRunningMaxDGD_Type()
)
nbsCohpmRunningMaxDGD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMaxDGD.setStatus("current")


class _NbsCohpmRunningAveQ_Type(Unsigned32):
    """Custom type nbsCohpmRunningAveQ based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningAveQ_Type.__name__ = "Unsigned32"
_NbsCohpmRunningAveQ_Object = MibTableColumn
nbsCohpmRunningAveQ = _NbsCohpmRunningAveQ_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 40),
    _NbsCohpmRunningAveQ_Type()
)
nbsCohpmRunningAveQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningAveQ.setStatus("current")


class _NbsCohpmRunningMinQ_Type(Unsigned32):
    """Custom type nbsCohpmRunningMinQ based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningMinQ_Type.__name__ = "Unsigned32"
_NbsCohpmRunningMinQ_Object = MibTableColumn
nbsCohpmRunningMinQ = _NbsCohpmRunningMinQ_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 43),
    _NbsCohpmRunningMinQ_Type()
)
nbsCohpmRunningMinQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMinQ.setStatus("current")


class _NbsCohpmRunningMaxQ_Type(Unsigned32):
    """Custom type nbsCohpmRunningMaxQ based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningMaxQ_Type.__name__ = "Unsigned32"
_NbsCohpmRunningMaxQ_Object = MibTableColumn
nbsCohpmRunningMaxQ = _NbsCohpmRunningMaxQ_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 46),
    _NbsCohpmRunningMaxQ_Type()
)
nbsCohpmRunningMaxQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMaxQ.setStatus("current")


class _NbsCohpmRunningAveCFO_Type(Integer32):
    """Custom type nbsCohpmRunningAveCFO based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmRunningAveCFO_Type.__name__ = "Integer32"
_NbsCohpmRunningAveCFO_Object = MibTableColumn
nbsCohpmRunningAveCFO = _NbsCohpmRunningAveCFO_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 50),
    _NbsCohpmRunningAveCFO_Type()
)
nbsCohpmRunningAveCFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningAveCFO.setStatus("current")


class _NbsCohpmRunningMinCFO_Type(Integer32):
    """Custom type nbsCohpmRunningMinCFO based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmRunningMinCFO_Type.__name__ = "Integer32"
_NbsCohpmRunningMinCFO_Object = MibTableColumn
nbsCohpmRunningMinCFO = _NbsCohpmRunningMinCFO_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 53),
    _NbsCohpmRunningMinCFO_Type()
)
nbsCohpmRunningMinCFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMinCFO.setStatus("current")


class _NbsCohpmRunningMaxCFO_Type(Integer32):
    """Custom type nbsCohpmRunningMaxCFO based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCohpmRunningMaxCFO_Type.__name__ = "Integer32"
_NbsCohpmRunningMaxCFO_Object = MibTableColumn
nbsCohpmRunningMaxCFO = _NbsCohpmRunningMaxCFO_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 56),
    _NbsCohpmRunningMaxCFO_Type()
)
nbsCohpmRunningMaxCFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMaxCFO.setStatus("current")


class _NbsCohpmRunningAveOSNR_Type(Unsigned32):
    """Custom type nbsCohpmRunningAveOSNR based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningAveOSNR_Type.__name__ = "Unsigned32"
_NbsCohpmRunningAveOSNR_Object = MibTableColumn
nbsCohpmRunningAveOSNR = _NbsCohpmRunningAveOSNR_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 60),
    _NbsCohpmRunningAveOSNR_Type()
)
nbsCohpmRunningAveOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningAveOSNR.setStatus("current")


class _NbsCohpmRunningMinOSNR_Type(Unsigned32):
    """Custom type nbsCohpmRunningMinOSNR based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningMinOSNR_Type.__name__ = "Unsigned32"
_NbsCohpmRunningMinOSNR_Object = MibTableColumn
nbsCohpmRunningMinOSNR = _NbsCohpmRunningMinOSNR_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 63),
    _NbsCohpmRunningMinOSNR_Type()
)
nbsCohpmRunningMinOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMinOSNR.setStatus("current")


class _NbsCohpmRunningMaxOSNR_Type(Unsigned32):
    """Custom type nbsCohpmRunningMaxOSNR based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningMaxOSNR_Type.__name__ = "Unsigned32"
_NbsCohpmRunningMaxOSNR_Object = MibTableColumn
nbsCohpmRunningMaxOSNR = _NbsCohpmRunningMaxOSNR_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 66),
    _NbsCohpmRunningMaxOSNR_Type()
)
nbsCohpmRunningMaxOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMaxOSNR.setStatus("current")


class _NbsCohpmRunningAveSNRx_Type(Unsigned32):
    """Custom type nbsCohpmRunningAveSNRx based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningAveSNRx_Type.__name__ = "Unsigned32"
_NbsCohpmRunningAveSNRx_Object = MibTableColumn
nbsCohpmRunningAveSNRx = _NbsCohpmRunningAveSNRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 70),
    _NbsCohpmRunningAveSNRx_Type()
)
nbsCohpmRunningAveSNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningAveSNRx.setStatus("current")


class _NbsCohpmRunningMinSNRx_Type(Unsigned32):
    """Custom type nbsCohpmRunningMinSNRx based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningMinSNRx_Type.__name__ = "Unsigned32"
_NbsCohpmRunningMinSNRx_Object = MibTableColumn
nbsCohpmRunningMinSNRx = _NbsCohpmRunningMinSNRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 73),
    _NbsCohpmRunningMinSNRx_Type()
)
nbsCohpmRunningMinSNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMinSNRx.setStatus("current")


class _NbsCohpmRunningMaxSNRx_Type(Unsigned32):
    """Custom type nbsCohpmRunningMaxSNRx based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningMaxSNRx_Type.__name__ = "Unsigned32"
_NbsCohpmRunningMaxSNRx_Object = MibTableColumn
nbsCohpmRunningMaxSNRx = _NbsCohpmRunningMaxSNRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 76),
    _NbsCohpmRunningMaxSNRx_Type()
)
nbsCohpmRunningMaxSNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMaxSNRx.setStatus("current")


class _NbsCohpmRunningAveSNRy_Type(Unsigned32):
    """Custom type nbsCohpmRunningAveSNRy based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningAveSNRy_Type.__name__ = "Unsigned32"
_NbsCohpmRunningAveSNRy_Object = MibTableColumn
nbsCohpmRunningAveSNRy = _NbsCohpmRunningAveSNRy_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 80),
    _NbsCohpmRunningAveSNRy_Type()
)
nbsCohpmRunningAveSNRy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningAveSNRy.setStatus("current")


class _NbsCohpmRunningMinSNRy_Type(Unsigned32):
    """Custom type nbsCohpmRunningMinSNRy based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningMinSNRy_Type.__name__ = "Unsigned32"
_NbsCohpmRunningMinSNRy_Object = MibTableColumn
nbsCohpmRunningMinSNRy = _NbsCohpmRunningMinSNRy_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 83),
    _NbsCohpmRunningMinSNRy_Type()
)
nbsCohpmRunningMinSNRy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMinSNRy.setStatus("current")


class _NbsCohpmRunningMaxSNRy_Type(Unsigned32):
    """Custom type nbsCohpmRunningMaxSNRy based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningMaxSNRy_Type.__name__ = "Unsigned32"
_NbsCohpmRunningMaxSNRy_Object = MibTableColumn
nbsCohpmRunningMaxSNRy = _NbsCohpmRunningMaxSNRy_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 86),
    _NbsCohpmRunningMaxSNRy_Type()
)
nbsCohpmRunningMaxSNRy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMaxSNRy.setStatus("current")


class _NbsCohpmRunningAvePDL_Type(Unsigned32):
    """Custom type nbsCohpmRunningAvePDL based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningAvePDL_Type.__name__ = "Unsigned32"
_NbsCohpmRunningAvePDL_Object = MibTableColumn
nbsCohpmRunningAvePDL = _NbsCohpmRunningAvePDL_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 90),
    _NbsCohpmRunningAvePDL_Type()
)
nbsCohpmRunningAvePDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningAvePDL.setStatus("current")


class _NbsCohpmRunningMinPDL_Type(Unsigned32):
    """Custom type nbsCohpmRunningMinPDL based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningMinPDL_Type.__name__ = "Unsigned32"
_NbsCohpmRunningMinPDL_Object = MibTableColumn
nbsCohpmRunningMinPDL = _NbsCohpmRunningMinPDL_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 93),
    _NbsCohpmRunningMinPDL_Type()
)
nbsCohpmRunningMinPDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMinPDL.setStatus("current")


class _NbsCohpmRunningMaxPDL_Type(Unsigned32):
    """Custom type nbsCohpmRunningMaxPDL based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningMaxPDL_Type.__name__ = "Unsigned32"
_NbsCohpmRunningMaxPDL_Object = MibTableColumn
nbsCohpmRunningMaxPDL = _NbsCohpmRunningMaxPDL_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 96),
    _NbsCohpmRunningMaxPDL_Type()
)
nbsCohpmRunningMaxPDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMaxPDL.setStatus("current")


class _NbsCohpmRunningAveSOP_Type(Unsigned32):
    """Custom type nbsCohpmRunningAveSOP based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningAveSOP_Type.__name__ = "Unsigned32"
_NbsCohpmRunningAveSOP_Object = MibTableColumn
nbsCohpmRunningAveSOP = _NbsCohpmRunningAveSOP_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 100),
    _NbsCohpmRunningAveSOP_Type()
)
nbsCohpmRunningAveSOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningAveSOP.setStatus("current")


class _NbsCohpmRunningMinSOP_Type(Unsigned32):
    """Custom type nbsCohpmRunningMinSOP based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningMinSOP_Type.__name__ = "Unsigned32"
_NbsCohpmRunningMinSOP_Object = MibTableColumn
nbsCohpmRunningMinSOP = _NbsCohpmRunningMinSOP_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 103),
    _NbsCohpmRunningMinSOP_Type()
)
nbsCohpmRunningMinSOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMinSOP.setStatus("current")


class _NbsCohpmRunningMaxSOP_Type(Unsigned32):
    """Custom type nbsCohpmRunningMaxSOP based on Unsigned32"""
    defaultValue = 0


_NbsCohpmRunningMaxSOP_Type.__name__ = "Unsigned32"
_NbsCohpmRunningMaxSOP_Object = MibTableColumn
nbsCohpmRunningMaxSOP = _NbsCohpmRunningMaxSOP_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 24, 3, 1, 106),
    _NbsCohpmRunningMaxSOP_Type()
)
nbsCohpmRunningMaxSOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCohpmRunningMaxSOP.setStatus("current")
_NbsCoherentStatsGrp_ObjectIdentity = ObjectIdentity
nbsCoherentStatsGrp = _NbsCoherentStatsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 242, 90)
)
if mibBuilder.loadTexts:
    nbsCoherentStatsGrp.setStatus("current")
_NbsCoherentStatsTable_Object = MibTable
nbsCoherentStatsTable = _NbsCoherentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2)
)
if mibBuilder.loadTexts:
    nbsCoherentStatsTable.setStatus("current")
_NbsCoherentStatsEntry_Object = MibTableRow
nbsCoherentStatsEntry = _NbsCoherentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1)
)
nbsCoherentStatsEntry.setIndexNames(
    (0, "NBS-COHERENT-MIB", "nbsCoherentStatsIfIndex"),
)
if mibBuilder.loadTexts:
    nbsCoherentStatsEntry.setStatus("current")
_NbsCoherentStatsIfIndex_Type = InterfaceIndex
_NbsCoherentStatsIfIndex_Object = MibTableColumn
nbsCoherentStatsIfIndex = _NbsCoherentStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 1),
    _NbsCoherentStatsIfIndex_Type()
)
nbsCoherentStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsIfIndex.setStatus("current")
_NbsCoherentStatsDate_Type = Integer32
_NbsCoherentStatsDate_Object = MibTableColumn
nbsCoherentStatsDate = _NbsCoherentStatsDate_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 5),
    _NbsCoherentStatsDate_Type()
)
nbsCoherentStatsDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsDate.setStatus("current")
_NbsCoherentStatsTime_Type = Integer32
_NbsCoherentStatsTime_Object = MibTableColumn
nbsCoherentStatsTime = _NbsCoherentStatsTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 6),
    _NbsCoherentStatsTime_Type()
)
nbsCoherentStatsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsTime.setStatus("current")
_NbsCoherentStatsSpan_Type = Integer32
_NbsCoherentStatsSpan_Object = MibTableColumn
nbsCoherentStatsSpan = _NbsCoherentStatsSpan_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 7),
    _NbsCoherentStatsSpan_Type()
)
nbsCoherentStatsSpan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsSpan.setStatus("current")


class _NbsCoherentStatsState_Type(Integer32):
    """Custom type nbsCoherentStatsState based on Integer32"""
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
        *(("notSupported", 1),
          ("counting", 2),
          ("clearing", 3),
          ("stopped", 4),
          ("resumed", 5))
    )


_NbsCoherentStatsState_Type.__name__ = "Integer32"
_NbsCoherentStatsState_Object = MibTableColumn
nbsCoherentStatsState = _NbsCoherentStatsState_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 8),
    _NbsCoherentStatsState_Type()
)
nbsCoherentStatsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCoherentStatsState.setStatus("current")


class _NbsCoherentStatsAveNetBERsig_Type(Integer32):
    """Custom type nbsCoherentStatsAveNetBERsig based on Integer32"""
    defaultValue = 0


_NbsCoherentStatsAveNetBERsig_Type.__name__ = "Integer32"
_NbsCoherentStatsAveNetBERsig_Object = MibTableColumn
nbsCoherentStatsAveNetBERsig = _NbsCoherentStatsAveNetBERsig_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 11),
    _NbsCoherentStatsAveNetBERsig_Type()
)
nbsCoherentStatsAveNetBERsig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsAveNetBERsig.setStatus("current")


class _NbsCoherentStatsAveNetBERexp_Type(Integer32):
    """Custom type nbsCoherentStatsAveNetBERexp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCoherentStatsAveNetBERexp_Type.__name__ = "Integer32"
_NbsCoherentStatsAveNetBERexp_Object = MibTableColumn
nbsCoherentStatsAveNetBERexp = _NbsCoherentStatsAveNetBERexp_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 12),
    _NbsCoherentStatsAveNetBERexp_Type()
)
nbsCoherentStatsAveNetBERexp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsAveNetBERexp.setStatus("current")


class _NbsCoherentStatsMinNetBERsig_Type(Integer32):
    """Custom type nbsCoherentStatsMinNetBERsig based on Integer32"""
    defaultValue = 0


_NbsCoherentStatsMinNetBERsig_Type.__name__ = "Integer32"
_NbsCoherentStatsMinNetBERsig_Object = MibTableColumn
nbsCoherentStatsMinNetBERsig = _NbsCoherentStatsMinNetBERsig_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 14),
    _NbsCoherentStatsMinNetBERsig_Type()
)
nbsCoherentStatsMinNetBERsig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMinNetBERsig.setStatus("current")


class _NbsCoherentStatsMinNetBERexp_Type(Integer32):
    """Custom type nbsCoherentStatsMinNetBERexp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCoherentStatsMinNetBERexp_Type.__name__ = "Integer32"
_NbsCoherentStatsMinNetBERexp_Object = MibTableColumn
nbsCoherentStatsMinNetBERexp = _NbsCoherentStatsMinNetBERexp_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 15),
    _NbsCoherentStatsMinNetBERexp_Type()
)
nbsCoherentStatsMinNetBERexp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMinNetBERexp.setStatus("current")


class _NbsCoherentStatsMaxNetBERsig_Type(Integer32):
    """Custom type nbsCoherentStatsMaxNetBERsig based on Integer32"""
    defaultValue = 0


_NbsCoherentStatsMaxNetBERsig_Type.__name__ = "Integer32"
_NbsCoherentStatsMaxNetBERsig_Object = MibTableColumn
nbsCoherentStatsMaxNetBERsig = _NbsCoherentStatsMaxNetBERsig_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 17),
    _NbsCoherentStatsMaxNetBERsig_Type()
)
nbsCoherentStatsMaxNetBERsig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMaxNetBERsig.setStatus("current")


class _NbsCoherentStatsMaxNetBERexp_Type(Integer32):
    """Custom type nbsCoherentStatsMaxNetBERexp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCoherentStatsMaxNetBERexp_Type.__name__ = "Integer32"
_NbsCoherentStatsMaxNetBERexp_Object = MibTableColumn
nbsCoherentStatsMaxNetBERexp = _NbsCoherentStatsMaxNetBERexp_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 18),
    _NbsCoherentStatsMaxNetBERexp_Type()
)
nbsCoherentStatsMaxNetBERexp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMaxNetBERexp.setStatus("current")


class _NbsCoherentStatsAveCD_Type(Integer32):
    """Custom type nbsCoherentStatsAveCD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCoherentStatsAveCD_Type.__name__ = "Integer32"
_NbsCoherentStatsAveCD_Object = MibTableColumn
nbsCoherentStatsAveCD = _NbsCoherentStatsAveCD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 20),
    _NbsCoherentStatsAveCD_Type()
)
nbsCoherentStatsAveCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsAveCD.setStatus("current")


class _NbsCoherentStatsMinCD_Type(Integer32):
    """Custom type nbsCoherentStatsMinCD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCoherentStatsMinCD_Type.__name__ = "Integer32"
_NbsCoherentStatsMinCD_Object = MibTableColumn
nbsCoherentStatsMinCD = _NbsCoherentStatsMinCD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 23),
    _NbsCoherentStatsMinCD_Type()
)
nbsCoherentStatsMinCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMinCD.setStatus("current")


class _NbsCoherentStatsMaxCD_Type(Integer32):
    """Custom type nbsCoherentStatsMaxCD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCoherentStatsMaxCD_Type.__name__ = "Integer32"
_NbsCoherentStatsMaxCD_Object = MibTableColumn
nbsCoherentStatsMaxCD = _NbsCoherentStatsMaxCD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 26),
    _NbsCoherentStatsMaxCD_Type()
)
nbsCoherentStatsMaxCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMaxCD.setStatus("current")


class _NbsCoherentStatsAveDGD_Type(Unsigned32):
    """Custom type nbsCoherentStatsAveDGD based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsAveDGD_Type.__name__ = "Unsigned32"
_NbsCoherentStatsAveDGD_Object = MibTableColumn
nbsCoherentStatsAveDGD = _NbsCoherentStatsAveDGD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 30),
    _NbsCoherentStatsAveDGD_Type()
)
nbsCoherentStatsAveDGD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsAveDGD.setStatus("current")


class _NbsCoherentStatsMinDGD_Type(Unsigned32):
    """Custom type nbsCoherentStatsMinDGD based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsMinDGD_Type.__name__ = "Unsigned32"
_NbsCoherentStatsMinDGD_Object = MibTableColumn
nbsCoherentStatsMinDGD = _NbsCoherentStatsMinDGD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 33),
    _NbsCoherentStatsMinDGD_Type()
)
nbsCoherentStatsMinDGD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMinDGD.setStatus("current")


class _NbsCoherentStatsMaxDGD_Type(Unsigned32):
    """Custom type nbsCoherentStatsMaxDGD based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsMaxDGD_Type.__name__ = "Unsigned32"
_NbsCoherentStatsMaxDGD_Object = MibTableColumn
nbsCoherentStatsMaxDGD = _NbsCoherentStatsMaxDGD_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 36),
    _NbsCoherentStatsMaxDGD_Type()
)
nbsCoherentStatsMaxDGD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMaxDGD.setStatus("current")


class _NbsCoherentStatsAveQ_Type(Unsigned32):
    """Custom type nbsCoherentStatsAveQ based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsAveQ_Type.__name__ = "Unsigned32"
_NbsCoherentStatsAveQ_Object = MibTableColumn
nbsCoherentStatsAveQ = _NbsCoherentStatsAveQ_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 40),
    _NbsCoherentStatsAveQ_Type()
)
nbsCoherentStatsAveQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsAveQ.setStatus("current")


class _NbsCoherentStatsMinQ_Type(Unsigned32):
    """Custom type nbsCoherentStatsMinQ based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsMinQ_Type.__name__ = "Unsigned32"
_NbsCoherentStatsMinQ_Object = MibTableColumn
nbsCoherentStatsMinQ = _NbsCoherentStatsMinQ_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 43),
    _NbsCoherentStatsMinQ_Type()
)
nbsCoherentStatsMinQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMinQ.setStatus("current")


class _NbsCoherentStatsMaxQ_Type(Unsigned32):
    """Custom type nbsCoherentStatsMaxQ based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsMaxQ_Type.__name__ = "Unsigned32"
_NbsCoherentStatsMaxQ_Object = MibTableColumn
nbsCoherentStatsMaxQ = _NbsCoherentStatsMaxQ_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 46),
    _NbsCoherentStatsMaxQ_Type()
)
nbsCoherentStatsMaxQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMaxQ.setStatus("current")


class _NbsCoherentStatsAveCFO_Type(Integer32):
    """Custom type nbsCoherentStatsAveCFO based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCoherentStatsAveCFO_Type.__name__ = "Integer32"
_NbsCoherentStatsAveCFO_Object = MibTableColumn
nbsCoherentStatsAveCFO = _NbsCoherentStatsAveCFO_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 50),
    _NbsCoherentStatsAveCFO_Type()
)
nbsCoherentStatsAveCFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsAveCFO.setStatus("current")


class _NbsCoherentStatsMinCFO_Type(Integer32):
    """Custom type nbsCoherentStatsMinCFO based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCoherentStatsMinCFO_Type.__name__ = "Integer32"
_NbsCoherentStatsMinCFO_Object = MibTableColumn
nbsCoherentStatsMinCFO = _NbsCoherentStatsMinCFO_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 53),
    _NbsCoherentStatsMinCFO_Type()
)
nbsCoherentStatsMinCFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMinCFO.setStatus("current")


class _NbsCoherentStatsMaxCFO_Type(Integer32):
    """Custom type nbsCoherentStatsMaxCFO based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCoherentStatsMaxCFO_Type.__name__ = "Integer32"
_NbsCoherentStatsMaxCFO_Object = MibTableColumn
nbsCoherentStatsMaxCFO = _NbsCoherentStatsMaxCFO_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 56),
    _NbsCoherentStatsMaxCFO_Type()
)
nbsCoherentStatsMaxCFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMaxCFO.setStatus("current")


class _NbsCoherentStatsAveOSNR_Type(Unsigned32):
    """Custom type nbsCoherentStatsAveOSNR based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsAveOSNR_Type.__name__ = "Unsigned32"
_NbsCoherentStatsAveOSNR_Object = MibTableColumn
nbsCoherentStatsAveOSNR = _NbsCoherentStatsAveOSNR_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 60),
    _NbsCoherentStatsAveOSNR_Type()
)
nbsCoherentStatsAveOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsAveOSNR.setStatus("current")


class _NbsCoherentStatsMinOSNR_Type(Unsigned32):
    """Custom type nbsCoherentStatsMinOSNR based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsMinOSNR_Type.__name__ = "Unsigned32"
_NbsCoherentStatsMinOSNR_Object = MibTableColumn
nbsCoherentStatsMinOSNR = _NbsCoherentStatsMinOSNR_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 63),
    _NbsCoherentStatsMinOSNR_Type()
)
nbsCoherentStatsMinOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMinOSNR.setStatus("current")


class _NbsCoherentStatsMaxOSNR_Type(Unsigned32):
    """Custom type nbsCoherentStatsMaxOSNR based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsMaxOSNR_Type.__name__ = "Unsigned32"
_NbsCoherentStatsMaxOSNR_Object = MibTableColumn
nbsCoherentStatsMaxOSNR = _NbsCoherentStatsMaxOSNR_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 66),
    _NbsCoherentStatsMaxOSNR_Type()
)
nbsCoherentStatsMaxOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMaxOSNR.setStatus("current")


class _NbsCoherentStatsAveSNRx_Type(Unsigned32):
    """Custom type nbsCoherentStatsAveSNRx based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsAveSNRx_Type.__name__ = "Unsigned32"
_NbsCoherentStatsAveSNRx_Object = MibTableColumn
nbsCoherentStatsAveSNRx = _NbsCoherentStatsAveSNRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 70),
    _NbsCoherentStatsAveSNRx_Type()
)
nbsCoherentStatsAveSNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsAveSNRx.setStatus("current")


class _NbsCoherentStatsMinSNRx_Type(Unsigned32):
    """Custom type nbsCoherentStatsMinSNRx based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsMinSNRx_Type.__name__ = "Unsigned32"
_NbsCoherentStatsMinSNRx_Object = MibTableColumn
nbsCoherentStatsMinSNRx = _NbsCoherentStatsMinSNRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 73),
    _NbsCoherentStatsMinSNRx_Type()
)
nbsCoherentStatsMinSNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMinSNRx.setStatus("current")


class _NbsCoherentStatsMaxSNRx_Type(Unsigned32):
    """Custom type nbsCoherentStatsMaxSNRx based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsMaxSNRx_Type.__name__ = "Unsigned32"
_NbsCoherentStatsMaxSNRx_Object = MibTableColumn
nbsCoherentStatsMaxSNRx = _NbsCoherentStatsMaxSNRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 76),
    _NbsCoherentStatsMaxSNRx_Type()
)
nbsCoherentStatsMaxSNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMaxSNRx.setStatus("current")


class _NbsCoherentStatsAveSNRy_Type(Unsigned32):
    """Custom type nbsCoherentStatsAveSNRy based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsAveSNRy_Type.__name__ = "Unsigned32"
_NbsCoherentStatsAveSNRy_Object = MibTableColumn
nbsCoherentStatsAveSNRy = _NbsCoherentStatsAveSNRy_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 80),
    _NbsCoherentStatsAveSNRy_Type()
)
nbsCoherentStatsAveSNRy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsAveSNRy.setStatus("current")


class _NbsCoherentStatsMinSNRy_Type(Unsigned32):
    """Custom type nbsCoherentStatsMinSNRy based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsMinSNRy_Type.__name__ = "Unsigned32"
_NbsCoherentStatsMinSNRy_Object = MibTableColumn
nbsCoherentStatsMinSNRy = _NbsCoherentStatsMinSNRy_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 83),
    _NbsCoherentStatsMinSNRy_Type()
)
nbsCoherentStatsMinSNRy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMinSNRy.setStatus("current")


class _NbsCoherentStatsMaxSNRy_Type(Unsigned32):
    """Custom type nbsCoherentStatsMaxSNRy based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsMaxSNRy_Type.__name__ = "Unsigned32"
_NbsCoherentStatsMaxSNRy_Object = MibTableColumn
nbsCoherentStatsMaxSNRy = _NbsCoherentStatsMaxSNRy_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 86),
    _NbsCoherentStatsMaxSNRy_Type()
)
nbsCoherentStatsMaxSNRy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMaxSNRy.setStatus("current")


class _NbsCoherentStatsAvePDL_Type(Unsigned32):
    """Custom type nbsCoherentStatsAvePDL based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsAvePDL_Type.__name__ = "Unsigned32"
_NbsCoherentStatsAvePDL_Object = MibTableColumn
nbsCoherentStatsAvePDL = _NbsCoherentStatsAvePDL_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 90),
    _NbsCoherentStatsAvePDL_Type()
)
nbsCoherentStatsAvePDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsAvePDL.setStatus("current")


class _NbsCoherentStatsMinPDL_Type(Unsigned32):
    """Custom type nbsCoherentStatsMinPDL based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsMinPDL_Type.__name__ = "Unsigned32"
_NbsCoherentStatsMinPDL_Object = MibTableColumn
nbsCoherentStatsMinPDL = _NbsCoherentStatsMinPDL_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 93),
    _NbsCoherentStatsMinPDL_Type()
)
nbsCoherentStatsMinPDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMinPDL.setStatus("current")


class _NbsCoherentStatsMaxPDL_Type(Unsigned32):
    """Custom type nbsCoherentStatsMaxPDL based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsMaxPDL_Type.__name__ = "Unsigned32"
_NbsCoherentStatsMaxPDL_Object = MibTableColumn
nbsCoherentStatsMaxPDL = _NbsCoherentStatsMaxPDL_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 96),
    _NbsCoherentStatsMaxPDL_Type()
)
nbsCoherentStatsMaxPDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMaxPDL.setStatus("current")


class _NbsCoherentStatsAveSOP_Type(Unsigned32):
    """Custom type nbsCoherentStatsAveSOP based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsAveSOP_Type.__name__ = "Unsigned32"
_NbsCoherentStatsAveSOP_Object = MibTableColumn
nbsCoherentStatsAveSOP = _NbsCoherentStatsAveSOP_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 100),
    _NbsCoherentStatsAveSOP_Type()
)
nbsCoherentStatsAveSOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsAveSOP.setStatus("current")


class _NbsCoherentStatsMinSOP_Type(Unsigned32):
    """Custom type nbsCoherentStatsMinSOP based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsMinSOP_Type.__name__ = "Unsigned32"
_NbsCoherentStatsMinSOP_Object = MibTableColumn
nbsCoherentStatsMinSOP = _NbsCoherentStatsMinSOP_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 103),
    _NbsCoherentStatsMinSOP_Type()
)
nbsCoherentStatsMinSOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMinSOP.setStatus("current")


class _NbsCoherentStatsMaxSOP_Type(Unsigned32):
    """Custom type nbsCoherentStatsMaxSOP based on Unsigned32"""
    defaultValue = 0


_NbsCoherentStatsMaxSOP_Type.__name__ = "Unsigned32"
_NbsCoherentStatsMaxSOP_Object = MibTableColumn
nbsCoherentStatsMaxSOP = _NbsCoherentStatsMaxSOP_Object(
    (1, 3, 6, 1, 4, 1, 629, 242, 90, 2, 1, 106),
    _NbsCoherentStatsMaxSOP_Type()
)
nbsCoherentStatsMaxSOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCoherentStatsMaxSOP.setStatus("current")
_NbsCohpmEventsGrp_ObjectIdentity = ObjectIdentity
nbsCohpmEventsGrp = _NbsCohpmEventsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 242, 100)
)
if mibBuilder.loadTexts:
    nbsCohpmEventsGrp.setStatus("current")
_NbsCohpmTraps_ObjectIdentity = ObjectIdentity
nbsCohpmTraps = _NbsCohpmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0)
)
if mibBuilder.loadTexts:
    nbsCohpmTraps.setStatus("current")

# Managed Objects groups


# Notification objects

nbsCohpmTrapsAveBER = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 11)
)
nbsCohpmTrapsAveBER.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentAveNetBERsig"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentAveNetBERexp"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsAveBER.setStatus(
        "current"
    )

nbsCohpmTrapsMinBER = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 14)
)
nbsCohpmTrapsMinBER.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMinNetBERsig"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMinNetBERexp"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMinBER.setStatus(
        "current"
    )

nbsCohpmTrapsMaxBER = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 17)
)
nbsCohpmTrapsMaxBER.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMaxNetBERsig"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMaxNetBERexp"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMaxBER.setStatus(
        "current"
    )

nbsCohpmTrapsAveCD = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 20)
)
nbsCohpmTrapsAveCD.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentAveCD"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsAveCD.setStatus(
        "current"
    )

nbsCohpmTrapsMinCD = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 23)
)
nbsCohpmTrapsMinCD.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMinCD"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMinCD.setStatus(
        "current"
    )

nbsCohpmTrapsMaxCD = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 26)
)
nbsCohpmTrapsMaxCD.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMaxCD"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMaxCD.setStatus(
        "current"
    )

nbsCohpmTrapsAveDGD = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 30)
)
nbsCohpmTrapsAveDGD.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentAveDGD"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsAveDGD.setStatus(
        "current"
    )

nbsCohpmTrapsMinDGD = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 33)
)
nbsCohpmTrapsMinDGD.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMinDGD"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMinDGD.setStatus(
        "current"
    )

nbsCohpmTrapsMaxDGD = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 36)
)
nbsCohpmTrapsMaxDGD.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMaxDGD"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMaxDGD.setStatus(
        "current"
    )

nbsCohpmTrapsAveQ = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 40)
)
nbsCohpmTrapsAveQ.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentAveQ"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsAveQ.setStatus(
        "current"
    )

nbsCohpmTrapsMinQ = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 43)
)
nbsCohpmTrapsMinQ.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMinQ"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMinQ.setStatus(
        "current"
    )

nbsCohpmTrapsMaxQ = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 46)
)
nbsCohpmTrapsMaxQ.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMaxQ"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMaxQ.setStatus(
        "current"
    )

nbsCohpmTrapsAveCFO = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 50)
)
nbsCohpmTrapsAveCFO.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentAveCFO"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsAveCFO.setStatus(
        "current"
    )

nbsCohpmTrapsMinCFO = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 53)
)
nbsCohpmTrapsMinCFO.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMinCFO"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMinCFO.setStatus(
        "current"
    )

nbsCohpmTrapsMaxCFO = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 56)
)
nbsCohpmTrapsMaxCFO.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMaxCFO"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMaxCFO.setStatus(
        "current"
    )

nbsCohpmTrapsAveOSNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 60)
)
nbsCohpmTrapsAveOSNR.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentAveOSNR"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsAveOSNR.setStatus(
        "current"
    )

nbsCohpmTrapsMinOSNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 63)
)
nbsCohpmTrapsMinOSNR.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMinOSNR"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMinOSNR.setStatus(
        "current"
    )

nbsCohpmTrapsMaxOSNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 66)
)
nbsCohpmTrapsMaxOSNR.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMaxOSNR"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMaxOSNR.setStatus(
        "current"
    )

nbsCohpmTrapsAveSNRx = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 70)
)
nbsCohpmTrapsAveSNRx.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentAveSNRx"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsAveSNRx.setStatus(
        "current"
    )

nbsCohpmTrapsMinSNRx = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 73)
)
nbsCohpmTrapsMinSNRx.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMinSNRx"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMinSNRx.setStatus(
        "current"
    )

nbsCohpmTrapsMaxSNRx = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 76)
)
nbsCohpmTrapsMaxSNRx.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMaxSNRx"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMaxSNRx.setStatus(
        "current"
    )

nbsCohpmTrapsAveSNRy = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 80)
)
nbsCohpmTrapsAveSNRy.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentAveSNRy"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsAveSNRy.setStatus(
        "current"
    )

nbsCohpmTrapsMinSNRy = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 83)
)
nbsCohpmTrapsMinSNRy.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMinSNRy"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMinSNRy.setStatus(
        "current"
    )

nbsCohpmTrapsMaxSNRy = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 86)
)
nbsCohpmTrapsMaxSNRy.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMaxSNRy"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMaxSNRy.setStatus(
        "current"
    )

nbsCohpmTrapsAvePDL = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 90)
)
nbsCohpmTrapsAvePDL.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentAvePDL"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsAvePDL.setStatus(
        "current"
    )

nbsCohpmTrapsMinPDL = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 93)
)
nbsCohpmTrapsMinPDL.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMinPDL"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMinPDL.setStatus(
        "current"
    )

nbsCohpmTrapsMaxPDL = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 96)
)
nbsCohpmTrapsMaxPDL.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMaxPDL"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMaxPDL.setStatus(
        "current"
    )

nbsCohpmTrapsAveSOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 100)
)
nbsCohpmTrapsAveSOP.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentAveSOP"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsAveSOP.setStatus(
        "current"
    )

nbsCohpmTrapsMinSOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 103)
)
nbsCohpmTrapsMinSOP.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMinSOP"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMinSOP.setStatus(
        "current"
    )

nbsCohpmTrapsMaxSOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 242, 100, 0, 106)
)
nbsCohpmTrapsMaxSOP.setObjects(
      *(("NBS-COHERENT-MIB", "nbsCohpmCurrentIfIndex"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentInterval"),
        ("NBS-COHERENT-MIB", "nbsCohpmCurrentMaxSOP"))
)
if mibBuilder.loadTexts:
    nbsCohpmTrapsMaxSOP.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-COHERENT-MIB",
    **{"nbsCoherentMib": nbsCoherentMib,
       "nbsCoherentCfgGrp": nbsCoherentCfgGrp,
       "nbsCoherentCfgTable": nbsCoherentCfgTable,
       "nbsCoherentCfgEntry": nbsCoherentCfgEntry,
       "nbsCoherentCfgIfIndex": nbsCoherentCfgIfIndex,
       "nbsCoherentCfgCDmodeCaps": nbsCoherentCfgCDmodeCaps,
       "nbsCoherentCfgCDmodeAdmin": nbsCoherentCfgCDmodeAdmin,
       "nbsCoherentCfgCDmodeOper": nbsCoherentCfgCDmodeOper,
       "nbsCoherentCfgCDautolAdmin": nbsCoherentCfgCDautolAdmin,
       "nbsCoherentCfgCDautolOper": nbsCoherentCfgCDautolOper,
       "nbsCoherentCfgCDautohAdmin": nbsCoherentCfgCDautohAdmin,
       "nbsCoherentCfgCDautohOper": nbsCoherentCfgCDautohOper,
       "nbsCoherentCfgCDfixedAdmin": nbsCoherentCfgCDfixedAdmin,
       "nbsCoherentCfgCDfixedOper": nbsCoherentCfgCDfixedOper,
       "nbsCoherentCfgSOPmodeAdmin": nbsCoherentCfgSOPmodeAdmin,
       "nbsCoherentCfgSOPmodeOper": nbsCoherentCfgSOPmodeOper,
       "nbsCohpmThresholdsGrp": nbsCohpmThresholdsGrp,
       "nbsCohpmThresholdsTable": nbsCohpmThresholdsTable,
       "nbsCohpmThresholdsEntry": nbsCohpmThresholdsEntry,
       "nbsCohpmThresholdsIfIndex": nbsCohpmThresholdsIfIndex,
       "nbsCohpmThresholdsInterval": nbsCohpmThresholdsInterval,
       "nbsCohpmThresholdsAveNetBERsig": nbsCohpmThresholdsAveNetBERsig,
       "nbsCohpmThresholdsAveNetBERexp": nbsCohpmThresholdsAveNetBERexp,
       "nbsCohpmThresholdsMinNetBERsig": nbsCohpmThresholdsMinNetBERsig,
       "nbsCohpmThresholdsMinNetBERexp": nbsCohpmThresholdsMinNetBERexp,
       "nbsCohpmThresholdsMaxNetBERsig": nbsCohpmThresholdsMaxNetBERsig,
       "nbsCohpmThresholdsMaxNetBERexp": nbsCohpmThresholdsMaxNetBERexp,
       "nbsCohpmThresholdsAveCD": nbsCohpmThresholdsAveCD,
       "nbsCohpmThresholdsMinCD": nbsCohpmThresholdsMinCD,
       "nbsCohpmThresholdsMaxCD": nbsCohpmThresholdsMaxCD,
       "nbsCohpmThresholdsAveDGD": nbsCohpmThresholdsAveDGD,
       "nbsCohpmThresholdsMinDGD": nbsCohpmThresholdsMinDGD,
       "nbsCohpmThresholdsMaxDGD": nbsCohpmThresholdsMaxDGD,
       "nbsCohpmThresholdsAveQ": nbsCohpmThresholdsAveQ,
       "nbsCohpmThresholdsMinQ": nbsCohpmThresholdsMinQ,
       "nbsCohpmThresholdsMaxQ": nbsCohpmThresholdsMaxQ,
       "nbsCohpmThresholdsAveCFO": nbsCohpmThresholdsAveCFO,
       "nbsCohpmThresholdsMinCFO": nbsCohpmThresholdsMinCFO,
       "nbsCohpmThresholdsMaxCFO": nbsCohpmThresholdsMaxCFO,
       "nbsCohpmThresholdsAveOSNR": nbsCohpmThresholdsAveOSNR,
       "nbsCohpmThresholdsMinOSNR": nbsCohpmThresholdsMinOSNR,
       "nbsCohpmThresholdsMaxOSNR": nbsCohpmThresholdsMaxOSNR,
       "nbsCohpmThresholdsAveSNRx": nbsCohpmThresholdsAveSNRx,
       "nbsCohpmThresholdsMinSNRx": nbsCohpmThresholdsMinSNRx,
       "nbsCohpmThresholdsMaxSNRx": nbsCohpmThresholdsMaxSNRx,
       "nbsCohpmThresholdsAveSNRy": nbsCohpmThresholdsAveSNRy,
       "nbsCohpmThresholdsMinSNRy": nbsCohpmThresholdsMinSNRy,
       "nbsCohpmThresholdsMaxSNRy": nbsCohpmThresholdsMaxSNRy,
       "nbsCohpmThresholdsAvePDL": nbsCohpmThresholdsAvePDL,
       "nbsCohpmThresholdsMinPDL": nbsCohpmThresholdsMinPDL,
       "nbsCohpmThresholdsMaxPDL": nbsCohpmThresholdsMaxPDL,
       "nbsCohpmThresholdsAveSOP": nbsCohpmThresholdsAveSOP,
       "nbsCohpmThresholdsMinSOP": nbsCohpmThresholdsMinSOP,
       "nbsCohpmThresholdsMaxSOP": nbsCohpmThresholdsMaxSOP,
       "nbsCohpmCurrentGrp": nbsCohpmCurrentGrp,
       "nbsCohpmCurrentTable": nbsCohpmCurrentTable,
       "nbsCohpmCurrentEntry": nbsCohpmCurrentEntry,
       "nbsCohpmCurrentIfIndex": nbsCohpmCurrentIfIndex,
       "nbsCohpmCurrentInterval": nbsCohpmCurrentInterval,
       "nbsCohpmCurrentDate": nbsCohpmCurrentDate,
       "nbsCohpmCurrentTime": nbsCohpmCurrentTime,
       "nbsCohpmCurrentAveNetBERsig": nbsCohpmCurrentAveNetBERsig,
       "nbsCohpmCurrentAveNetBERexp": nbsCohpmCurrentAveNetBERexp,
       "nbsCohpmCurrentMinNetBERsig": nbsCohpmCurrentMinNetBERsig,
       "nbsCohpmCurrentMinNetBERexp": nbsCohpmCurrentMinNetBERexp,
       "nbsCohpmCurrentMaxNetBERsig": nbsCohpmCurrentMaxNetBERsig,
       "nbsCohpmCurrentMaxNetBERexp": nbsCohpmCurrentMaxNetBERexp,
       "nbsCohpmCurrentAveCD": nbsCohpmCurrentAveCD,
       "nbsCohpmCurrentMinCD": nbsCohpmCurrentMinCD,
       "nbsCohpmCurrentMaxCD": nbsCohpmCurrentMaxCD,
       "nbsCohpmCurrentAveDGD": nbsCohpmCurrentAveDGD,
       "nbsCohpmCurrentMinDGD": nbsCohpmCurrentMinDGD,
       "nbsCohpmCurrentMaxDGD": nbsCohpmCurrentMaxDGD,
       "nbsCohpmCurrentAveQ": nbsCohpmCurrentAveQ,
       "nbsCohpmCurrentMinQ": nbsCohpmCurrentMinQ,
       "nbsCohpmCurrentMaxQ": nbsCohpmCurrentMaxQ,
       "nbsCohpmCurrentAveCFO": nbsCohpmCurrentAveCFO,
       "nbsCohpmCurrentMinCFO": nbsCohpmCurrentMinCFO,
       "nbsCohpmCurrentMaxCFO": nbsCohpmCurrentMaxCFO,
       "nbsCohpmCurrentAveOSNR": nbsCohpmCurrentAveOSNR,
       "nbsCohpmCurrentMinOSNR": nbsCohpmCurrentMinOSNR,
       "nbsCohpmCurrentMaxOSNR": nbsCohpmCurrentMaxOSNR,
       "nbsCohpmCurrentAveSNRx": nbsCohpmCurrentAveSNRx,
       "nbsCohpmCurrentMinSNRx": nbsCohpmCurrentMinSNRx,
       "nbsCohpmCurrentMaxSNRx": nbsCohpmCurrentMaxSNRx,
       "nbsCohpmCurrentAveSNRy": nbsCohpmCurrentAveSNRy,
       "nbsCohpmCurrentMinSNRy": nbsCohpmCurrentMinSNRy,
       "nbsCohpmCurrentMaxSNRy": nbsCohpmCurrentMaxSNRy,
       "nbsCohpmCurrentAvePDL": nbsCohpmCurrentAvePDL,
       "nbsCohpmCurrentMinPDL": nbsCohpmCurrentMinPDL,
       "nbsCohpmCurrentMaxPDL": nbsCohpmCurrentMaxPDL,
       "nbsCohpmCurrentAveSOP": nbsCohpmCurrentAveSOP,
       "nbsCohpmCurrentMinSOP": nbsCohpmCurrentMinSOP,
       "nbsCohpmCurrentMaxSOP": nbsCohpmCurrentMaxSOP,
       "nbsCohpmHistoricGrp": nbsCohpmHistoricGrp,
       "nbsCohpmHistoricTable": nbsCohpmHistoricTable,
       "nbsCohpmHistoricEntry": nbsCohpmHistoricEntry,
       "nbsCohpmHistoricIfIndex": nbsCohpmHistoricIfIndex,
       "nbsCohpmHistoricInterval": nbsCohpmHistoricInterval,
       "nbsCohpmHistoricSample": nbsCohpmHistoricSample,
       "nbsCohpmHistoricDate": nbsCohpmHistoricDate,
       "nbsCohpmHistoricTime": nbsCohpmHistoricTime,
       "nbsCohpmHistoricAveNetBERsig": nbsCohpmHistoricAveNetBERsig,
       "nbsCohpmHistoricAveNetBERexp": nbsCohpmHistoricAveNetBERexp,
       "nbsCohpmHistoricMinNetBERsig": nbsCohpmHistoricMinNetBERsig,
       "nbsCohpmHistoricMinNetBERexp": nbsCohpmHistoricMinNetBERexp,
       "nbsCohpmHistoricMaxNetBERsig": nbsCohpmHistoricMaxNetBERsig,
       "nbsCohpmHistoricMaxNetBERexp": nbsCohpmHistoricMaxNetBERexp,
       "nbsCohpmHistoricAveCD": nbsCohpmHistoricAveCD,
       "nbsCohpmHistoricMinCD": nbsCohpmHistoricMinCD,
       "nbsCohpmHistoricMaxCD": nbsCohpmHistoricMaxCD,
       "nbsCohpmHistoricAveDGD": nbsCohpmHistoricAveDGD,
       "nbsCohpmHistoricMinDGD": nbsCohpmHistoricMinDGD,
       "nbsCohpmHistoricMaxDGD": nbsCohpmHistoricMaxDGD,
       "nbsCohpmHistoricAveQ": nbsCohpmHistoricAveQ,
       "nbsCohpmHistoricMinQ": nbsCohpmHistoricMinQ,
       "nbsCohpmHistoricMaxQ": nbsCohpmHistoricMaxQ,
       "nbsCohpmHistoricAveCFO": nbsCohpmHistoricAveCFO,
       "nbsCohpmHistoricMinCFO": nbsCohpmHistoricMinCFO,
       "nbsCohpmHistoricMaxCFO": nbsCohpmHistoricMaxCFO,
       "nbsCohpmHistoricAveOSNR": nbsCohpmHistoricAveOSNR,
       "nbsCohpmHistoricMinOSNR": nbsCohpmHistoricMinOSNR,
       "nbsCohpmHistoricMaxOSNR": nbsCohpmHistoricMaxOSNR,
       "nbsCohpmHistoricAveSNRx": nbsCohpmHistoricAveSNRx,
       "nbsCohpmHistoricMinSNRx": nbsCohpmHistoricMinSNRx,
       "nbsCohpmHistoricMaxSNRx": nbsCohpmHistoricMaxSNRx,
       "nbsCohpmHistoricAveSNRy": nbsCohpmHistoricAveSNRy,
       "nbsCohpmHistoricMinSNRy": nbsCohpmHistoricMinSNRy,
       "nbsCohpmHistoricMaxSNRy": nbsCohpmHistoricMaxSNRy,
       "nbsCohpmHistoricAvePDL": nbsCohpmHistoricAvePDL,
       "nbsCohpmHistoricMinPDL": nbsCohpmHistoricMinPDL,
       "nbsCohpmHistoricMaxPDL": nbsCohpmHistoricMaxPDL,
       "nbsCohpmHistoricAveSOP": nbsCohpmHistoricAveSOP,
       "nbsCohpmHistoricMinSOP": nbsCohpmHistoricMinSOP,
       "nbsCohpmHistoricMaxSOP": nbsCohpmHistoricMaxSOP,
       "nbsCohpmRunningGrp": nbsCohpmRunningGrp,
       "nbsCohpmRunningTable": nbsCohpmRunningTable,
       "nbsCohpmRunningEntry": nbsCohpmRunningEntry,
       "nbsCohpmRunningIfIndex": nbsCohpmRunningIfIndex,
       "nbsCohpmRunningDate": nbsCohpmRunningDate,
       "nbsCohpmRunningTime": nbsCohpmRunningTime,
       "nbsCohpmRunningAveNetBERsig": nbsCohpmRunningAveNetBERsig,
       "nbsCohpmRunningAveNetBERexp": nbsCohpmRunningAveNetBERexp,
       "nbsCohpmRunningMinNetBERsig": nbsCohpmRunningMinNetBERsig,
       "nbsCohpmRunningMinNetBERexp": nbsCohpmRunningMinNetBERexp,
       "nbsCohpmRunningMaxNetBERsig": nbsCohpmRunningMaxNetBERsig,
       "nbsCohpmRunningMaxNetBERexp": nbsCohpmRunningMaxNetBERexp,
       "nbsCohpmRunningAveCD": nbsCohpmRunningAveCD,
       "nbsCohpmRunningMinCD": nbsCohpmRunningMinCD,
       "nbsCohpmRunningMaxCD": nbsCohpmRunningMaxCD,
       "nbsCohpmRunningAveDGD": nbsCohpmRunningAveDGD,
       "nbsCohpmRunningMinDGD": nbsCohpmRunningMinDGD,
       "nbsCohpmRunningMaxDGD": nbsCohpmRunningMaxDGD,
       "nbsCohpmRunningAveQ": nbsCohpmRunningAveQ,
       "nbsCohpmRunningMinQ": nbsCohpmRunningMinQ,
       "nbsCohpmRunningMaxQ": nbsCohpmRunningMaxQ,
       "nbsCohpmRunningAveCFO": nbsCohpmRunningAveCFO,
       "nbsCohpmRunningMinCFO": nbsCohpmRunningMinCFO,
       "nbsCohpmRunningMaxCFO": nbsCohpmRunningMaxCFO,
       "nbsCohpmRunningAveOSNR": nbsCohpmRunningAveOSNR,
       "nbsCohpmRunningMinOSNR": nbsCohpmRunningMinOSNR,
       "nbsCohpmRunningMaxOSNR": nbsCohpmRunningMaxOSNR,
       "nbsCohpmRunningAveSNRx": nbsCohpmRunningAveSNRx,
       "nbsCohpmRunningMinSNRx": nbsCohpmRunningMinSNRx,
       "nbsCohpmRunningMaxSNRx": nbsCohpmRunningMaxSNRx,
       "nbsCohpmRunningAveSNRy": nbsCohpmRunningAveSNRy,
       "nbsCohpmRunningMinSNRy": nbsCohpmRunningMinSNRy,
       "nbsCohpmRunningMaxSNRy": nbsCohpmRunningMaxSNRy,
       "nbsCohpmRunningAvePDL": nbsCohpmRunningAvePDL,
       "nbsCohpmRunningMinPDL": nbsCohpmRunningMinPDL,
       "nbsCohpmRunningMaxPDL": nbsCohpmRunningMaxPDL,
       "nbsCohpmRunningAveSOP": nbsCohpmRunningAveSOP,
       "nbsCohpmRunningMinSOP": nbsCohpmRunningMinSOP,
       "nbsCohpmRunningMaxSOP": nbsCohpmRunningMaxSOP,
       "nbsCoherentStatsGrp": nbsCoherentStatsGrp,
       "nbsCoherentStatsTable": nbsCoherentStatsTable,
       "nbsCoherentStatsEntry": nbsCoherentStatsEntry,
       "nbsCoherentStatsIfIndex": nbsCoherentStatsIfIndex,
       "nbsCoherentStatsDate": nbsCoherentStatsDate,
       "nbsCoherentStatsTime": nbsCoherentStatsTime,
       "nbsCoherentStatsSpan": nbsCoherentStatsSpan,
       "nbsCoherentStatsState": nbsCoherentStatsState,
       "nbsCoherentStatsAveNetBERsig": nbsCoherentStatsAveNetBERsig,
       "nbsCoherentStatsAveNetBERexp": nbsCoherentStatsAveNetBERexp,
       "nbsCoherentStatsMinNetBERsig": nbsCoherentStatsMinNetBERsig,
       "nbsCoherentStatsMinNetBERexp": nbsCoherentStatsMinNetBERexp,
       "nbsCoherentStatsMaxNetBERsig": nbsCoherentStatsMaxNetBERsig,
       "nbsCoherentStatsMaxNetBERexp": nbsCoherentStatsMaxNetBERexp,
       "nbsCoherentStatsAveCD": nbsCoherentStatsAveCD,
       "nbsCoherentStatsMinCD": nbsCoherentStatsMinCD,
       "nbsCoherentStatsMaxCD": nbsCoherentStatsMaxCD,
       "nbsCoherentStatsAveDGD": nbsCoherentStatsAveDGD,
       "nbsCoherentStatsMinDGD": nbsCoherentStatsMinDGD,
       "nbsCoherentStatsMaxDGD": nbsCoherentStatsMaxDGD,
       "nbsCoherentStatsAveQ": nbsCoherentStatsAveQ,
       "nbsCoherentStatsMinQ": nbsCoherentStatsMinQ,
       "nbsCoherentStatsMaxQ": nbsCoherentStatsMaxQ,
       "nbsCoherentStatsAveCFO": nbsCoherentStatsAveCFO,
       "nbsCoherentStatsMinCFO": nbsCoherentStatsMinCFO,
       "nbsCoherentStatsMaxCFO": nbsCoherentStatsMaxCFO,
       "nbsCoherentStatsAveOSNR": nbsCoherentStatsAveOSNR,
       "nbsCoherentStatsMinOSNR": nbsCoherentStatsMinOSNR,
       "nbsCoherentStatsMaxOSNR": nbsCoherentStatsMaxOSNR,
       "nbsCoherentStatsAveSNRx": nbsCoherentStatsAveSNRx,
       "nbsCoherentStatsMinSNRx": nbsCoherentStatsMinSNRx,
       "nbsCoherentStatsMaxSNRx": nbsCoherentStatsMaxSNRx,
       "nbsCoherentStatsAveSNRy": nbsCoherentStatsAveSNRy,
       "nbsCoherentStatsMinSNRy": nbsCoherentStatsMinSNRy,
       "nbsCoherentStatsMaxSNRy": nbsCoherentStatsMaxSNRy,
       "nbsCoherentStatsAvePDL": nbsCoherentStatsAvePDL,
       "nbsCoherentStatsMinPDL": nbsCoherentStatsMinPDL,
       "nbsCoherentStatsMaxPDL": nbsCoherentStatsMaxPDL,
       "nbsCoherentStatsAveSOP": nbsCoherentStatsAveSOP,
       "nbsCoherentStatsMinSOP": nbsCoherentStatsMinSOP,
       "nbsCoherentStatsMaxSOP": nbsCoherentStatsMaxSOP,
       "nbsCohpmEventsGrp": nbsCohpmEventsGrp,
       "nbsCohpmTraps": nbsCohpmTraps,
       "nbsCohpmTrapsAveBER": nbsCohpmTrapsAveBER,
       "nbsCohpmTrapsMinBER": nbsCohpmTrapsMinBER,
       "nbsCohpmTrapsMaxBER": nbsCohpmTrapsMaxBER,
       "nbsCohpmTrapsAveCD": nbsCohpmTrapsAveCD,
       "nbsCohpmTrapsMinCD": nbsCohpmTrapsMinCD,
       "nbsCohpmTrapsMaxCD": nbsCohpmTrapsMaxCD,
       "nbsCohpmTrapsAveDGD": nbsCohpmTrapsAveDGD,
       "nbsCohpmTrapsMinDGD": nbsCohpmTrapsMinDGD,
       "nbsCohpmTrapsMaxDGD": nbsCohpmTrapsMaxDGD,
       "nbsCohpmTrapsAveQ": nbsCohpmTrapsAveQ,
       "nbsCohpmTrapsMinQ": nbsCohpmTrapsMinQ,
       "nbsCohpmTrapsMaxQ": nbsCohpmTrapsMaxQ,
       "nbsCohpmTrapsAveCFO": nbsCohpmTrapsAveCFO,
       "nbsCohpmTrapsMinCFO": nbsCohpmTrapsMinCFO,
       "nbsCohpmTrapsMaxCFO": nbsCohpmTrapsMaxCFO,
       "nbsCohpmTrapsAveOSNR": nbsCohpmTrapsAveOSNR,
       "nbsCohpmTrapsMinOSNR": nbsCohpmTrapsMinOSNR,
       "nbsCohpmTrapsMaxOSNR": nbsCohpmTrapsMaxOSNR,
       "nbsCohpmTrapsAveSNRx": nbsCohpmTrapsAveSNRx,
       "nbsCohpmTrapsMinSNRx": nbsCohpmTrapsMinSNRx,
       "nbsCohpmTrapsMaxSNRx": nbsCohpmTrapsMaxSNRx,
       "nbsCohpmTrapsAveSNRy": nbsCohpmTrapsAveSNRy,
       "nbsCohpmTrapsMinSNRy": nbsCohpmTrapsMinSNRy,
       "nbsCohpmTrapsMaxSNRy": nbsCohpmTrapsMaxSNRy,
       "nbsCohpmTrapsAvePDL": nbsCohpmTrapsAvePDL,
       "nbsCohpmTrapsMinPDL": nbsCohpmTrapsMinPDL,
       "nbsCohpmTrapsMaxPDL": nbsCohpmTrapsMaxPDL,
       "nbsCohpmTrapsAveSOP": nbsCohpmTrapsAveSOP,
       "nbsCohpmTrapsMinSOP": nbsCohpmTrapsMinSOP,
       "nbsCohpmTrapsMaxSOP": nbsCohpmTrapsMaxSOP}
)
