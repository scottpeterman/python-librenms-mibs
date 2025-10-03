# SNMP MIB module (CTRON-CSMACD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CTRON-CSMACD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:40:41 2025
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

(ctCSMACD,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctCSMACD")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtFnbCSMACD_ObjectIdentity = ObjectIdentity
ctFnbCSMACD = _CtFnbCSMACD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 1)
)
_CtFnbCSMACDTable_Object = MibTable
ctFnbCSMACDTable = _CtFnbCSMACDTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ctFnbCSMACDTable.setStatus("mandatory")
_CtFnbCSMACDEntry_Object = MibTableRow
ctFnbCSMACDEntry = _CtFnbCSMACDEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 1, 1, 1)
)
ctFnbCSMACDEntry.setIndexNames(
    (0, "CTRON-CSMACD-MIB", "ctFnbCSMACDIndex"),
)
if mibBuilder.loadTexts:
    ctFnbCSMACDEntry.setStatus("mandatory")
_CtFnbCSMACDIndex_Type = Integer32
_CtFnbCSMACDIndex_Object = MibTableColumn
ctFnbCSMACDIndex = _CtFnbCSMACDIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 1, 1, 1, 1),
    _CtFnbCSMACDIndex_Type()
)
ctFnbCSMACDIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFnbCSMACDIndex.setStatus("mandatory")


class _CtFnbConnect_Type(Integer32):
    """Custom type ctFnbConnect based on Integer32"""
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
        *(("connectB", 1),
          ("connectC", 2),
          ("disconnect", 3),
          ("connectA", 4),
          ("subnetB", 5),
          ("subnetC", 6),
          ("multiChannel", 7),
          ("frontpanel", 8))
    )


_CtFnbConnect_Type.__name__ = "Integer32"
_CtFnbConnect_Object = MibTableColumn
ctFnbConnect = _CtFnbConnect_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 1, 1, 1, 2),
    _CtFnbConnect_Type()
)
ctFnbConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFnbConnect.setStatus("mandatory")
_CtFnbPortChanges_Type = Counter32
_CtFnbPortChanges_Object = MibTableColumn
ctFnbPortChanges = _CtFnbPortChanges_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 1, 1, 1, 3),
    _CtFnbPortChanges_Type()
)
ctFnbPortChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFnbPortChanges.setStatus("mandatory")
_CtFnbPortConnect_ObjectIdentity = ObjectIdentity
ctFnbPortConnect = _CtFnbPortConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2)
)
_CtFnbPortConnectTable_Object = MibTable
ctFnbPortConnectTable = _CtFnbPortConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ctFnbPortConnectTable.setStatus("mandatory")
_CtFnbPortConnectEntry_Object = MibTableRow
ctFnbPortConnectEntry = _CtFnbPortConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 1, 1)
)
ctFnbPortConnectEntry.setIndexNames(
    (0, "CTRON-CSMACD-MIB", "ctFnbPortConnectBoardIndex"),
    (0, "CTRON-CSMACD-MIB", "ctFnbPortConnectPortIndex"),
)
if mibBuilder.loadTexts:
    ctFnbPortConnectEntry.setStatus("mandatory")
_CtFnbPortConnectBoardIndex_Type = Integer32
_CtFnbPortConnectBoardIndex_Object = MibTableColumn
ctFnbPortConnectBoardIndex = _CtFnbPortConnectBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 1, 1, 1),
    _CtFnbPortConnectBoardIndex_Type()
)
ctFnbPortConnectBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFnbPortConnectBoardIndex.setStatus("mandatory")
_CtFnbPortConnectPortIndex_Type = Integer32
_CtFnbPortConnectPortIndex_Object = MibTableColumn
ctFnbPortConnectPortIndex = _CtFnbPortConnectPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 1, 1, 2),
    _CtFnbPortConnectPortIndex_Type()
)
ctFnbPortConnectPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFnbPortConnectPortIndex.setStatus("mandatory")


class _CtFnbPortConnectPortAssignment_Type(Integer32):
    """Custom type ctFnbPortConnectPortAssignment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connectA", 1),
          ("connectB", 2),
          ("connectC", 3))
    )


_CtFnbPortConnectPortAssignment_Type.__name__ = "Integer32"
_CtFnbPortConnectPortAssignment_Object = MibTableColumn
ctFnbPortConnectPortAssignment = _CtFnbPortConnectPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 1, 1, 3),
    _CtFnbPortConnectPortAssignment_Type()
)
ctFnbPortConnectPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFnbPortConnectPortAssignment.setStatus("mandatory")
_CtFnbPortCompID_Type = Integer32
_CtFnbPortCompID_Object = MibTableColumn
ctFnbPortCompID = _CtFnbPortCompID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 1, 1, 4),
    _CtFnbPortCompID_Type()
)
ctFnbPortCompID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFnbPortCompID.setStatus("mandatory")
_CtFnbPortConnectionChanges_Type = Counter32
_CtFnbPortConnectionChanges_Object = MibScalar
ctFnbPortConnectionChanges = _CtFnbPortConnectionChanges_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 2),
    _CtFnbPortConnectionChanges_Type()
)
ctFnbPortConnectionChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFnbPortConnectionChanges.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-CSMACD-MIB",
    **{"ctFnbCSMACD": ctFnbCSMACD,
       "ctFnbCSMACDTable": ctFnbCSMACDTable,
       "ctFnbCSMACDEntry": ctFnbCSMACDEntry,
       "ctFnbCSMACDIndex": ctFnbCSMACDIndex,
       "ctFnbConnect": ctFnbConnect,
       "ctFnbPortChanges": ctFnbPortChanges,
       "ctFnbPortConnect": ctFnbPortConnect,
       "ctFnbPortConnectTable": ctFnbPortConnectTable,
       "ctFnbPortConnectEntry": ctFnbPortConnectEntry,
       "ctFnbPortConnectBoardIndex": ctFnbPortConnectBoardIndex,
       "ctFnbPortConnectPortIndex": ctFnbPortConnectPortIndex,
       "ctFnbPortConnectPortAssignment": ctFnbPortConnectPortAssignment,
       "ctFnbPortCompID": ctFnbPortCompID,
       "ctFnbPortConnectionChanges": ctFnbPortConnectionChanges}
)
