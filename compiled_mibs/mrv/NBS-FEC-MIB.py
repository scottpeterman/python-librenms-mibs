# SNMP MIB module (NBS-FEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mrv\NBS-FEC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:16 2025
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

nbsFecMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 232)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NbsFecCode(TextualConvention, Integer32):
    status = "current"
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
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("noFec", 1),
          ("zero", 2),
          ("gfec", 3),
          ("ufec7", 4),
          ("ufec10", 5),
          ("ufec25", 6),
          ("hgfec7", 7),
          ("sdfec0", 8),
          ("sdfec1", 9),
          ("sdfec2", 10),
          ("sdfec3", 11),
          ("g975i4", 12),
          ("g975i7", 13),
          ("xfec7", 14),
          ("sdfec15", 15))
    )



# MIB Managed Objects in the order of their OIDs

_NbsFecCfgGrp_ObjectIdentity = ObjectIdentity
nbsFecCfgGrp = _NbsFecCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 232, 1)
)
if mibBuilder.loadTexts:
    nbsFecCfgGrp.setStatus("current")
_NbsFecCfgTable_Object = MibTable
nbsFecCfgTable = _NbsFecCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 232, 1, 1)
)
if mibBuilder.loadTexts:
    nbsFecCfgTable.setStatus("current")
_NbsFecCfgEntry_Object = MibTableRow
nbsFecCfgEntry = _NbsFecCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1)
)
nbsFecCfgEntry.setIndexNames(
    (0, "NBS-FEC-MIB", "nbsFecCfgIfIndex"),
)
if mibBuilder.loadTexts:
    nbsFecCfgEntry.setStatus("current")
_NbsFecCfgIfIndex_Type = InterfaceIndex
_NbsFecCfgIfIndex_Object = MibTableColumn
nbsFecCfgIfIndex = _NbsFecCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 1),
    _NbsFecCfgIfIndex_Type()
)
nbsFecCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsFecCfgIfIndex.setStatus("current")


class _NbsFecCfgCodeCaps_Type(OctetString):
    """Custom type nbsFecCfgCodeCaps based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_NbsFecCfgCodeCaps_Type.__name__ = "OctetString"
_NbsFecCfgCodeCaps_Object = MibTableColumn
nbsFecCfgCodeCaps = _NbsFecCfgCodeCaps_Object(
    (1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 2),
    _NbsFecCfgCodeCaps_Type()
)
nbsFecCfgCodeCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecCfgCodeCaps.setStatus("current")
_NbsFecCfgCodeAdmin_Type = NbsFecCode
_NbsFecCfgCodeAdmin_Object = MibTableColumn
nbsFecCfgCodeAdmin = _NbsFecCfgCodeAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 3),
    _NbsFecCfgCodeAdmin_Type()
)
nbsFecCfgCodeAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsFecCfgCodeAdmin.setStatus("current")
_NbsFecCfgCodeOper_Type = NbsFecCode
_NbsFecCfgCodeOper_Object = MibTableColumn
nbsFecCfgCodeOper = _NbsFecCfgCodeOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 4),
    _NbsFecCfgCodeOper_Type()
)
nbsFecCfgCodeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecCfgCodeOper.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-FEC-MIB",
    **{"NbsFecCode": NbsFecCode,
       "nbsFecMib": nbsFecMib,
       "nbsFecCfgGrp": nbsFecCfgGrp,
       "nbsFecCfgTable": nbsFecCfgTable,
       "nbsFecCfgEntry": nbsFecCfgEntry,
       "nbsFecCfgIfIndex": nbsFecCfgIfIndex,
       "nbsFecCfgCodeCaps": nbsFecCfgCodeCaps,
       "nbsFecCfgCodeAdmin": nbsFecCfgCodeAdmin,
       "nbsFecCfgCodeOper": nbsFecCfgCodeOper}
)
