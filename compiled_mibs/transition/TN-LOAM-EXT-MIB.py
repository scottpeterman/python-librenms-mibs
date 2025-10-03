# SNMP MIB module (TN-LOAM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-LOAM-EXT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:49 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnLOAMExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 7)
)
if mibBuilder.loadTexts:
    tnLOAMExtMIB.setRevisions(
        ("2012-01-08 00:00",
         "2009-01-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnLOAMNotifications_ObjectIdentity = ObjectIdentity
tnLOAMNotifications = _TnLOAMNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 7, 0)
)
_TnLOAMObjects_ObjectIdentity = ObjectIdentity
tnLOAMObjects = _TnLOAMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 7, 1)
)
_TnLOAMIfMgmt_ObjectIdentity = ObjectIdentity
tnLOAMIfMgmt = _TnLOAMIfMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 7, 1, 1)
)
_TnLOAMIfMgmtTable_Object = MibTable
tnLOAMIfMgmtTable = _TnLOAMIfMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnLOAMIfMgmtTable.setStatus("current")
_TnLOAMIfMgmtEntry_Object = MibTableRow
tnLOAMIfMgmtEntry = _TnLOAMIfMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 7, 1, 1, 1, 1)
)
tnLOAMIfMgmtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnLOAMIfMgmtEntry.setStatus("current")


class _TnLOAMIfModeCtrl_Type(Integer32):
    """Custom type tnLOAMIfModeCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_TnLOAMIfModeCtrl_Type.__name__ = "Integer32"
_TnLOAMIfModeCtrl_Object = MibTableColumn
tnLOAMIfModeCtrl = _TnLOAMIfModeCtrl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 7, 1, 1, 1, 1, 1),
    _TnLOAMIfModeCtrl_Type()
)
tnLOAMIfModeCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLOAMIfModeCtrl.setStatus("current")


class _TnLOAMIfClearStats_Type(Integer32):
    """Custom type tnLOAMIfClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("doNothing", 2))
    )


_TnLOAMIfClearStats_Type.__name__ = "Integer32"
_TnLOAMIfClearStats_Object = MibTableColumn
tnLOAMIfClearStats = _TnLOAMIfClearStats_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 7, 1, 1, 1, 1, 2),
    _TnLOAMIfClearStats_Type()
)
tnLOAMIfClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLOAMIfClearStats.setStatus("current")


class _TnLOAMIfMUXState_Type(Integer32):
    """Custom type tnLOAMIfMUXState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2))
    )


_TnLOAMIfMUXState_Type.__name__ = "Integer32"
_TnLOAMIfMUXState_Object = MibTableColumn
tnLOAMIfMUXState = _TnLOAMIfMUXState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 7, 1, 1, 1, 1, 3),
    _TnLOAMIfMUXState_Type()
)
tnLOAMIfMUXState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLOAMIfMUXState.setStatus("current")


class _TnLOAMIfPARState_Type(Integer32):
    """Custom type tnLOAMIfPARState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("loopback", 2),
          ("discard", 3))
    )


_TnLOAMIfPARState_Type.__name__ = "Integer32"
_TnLOAMIfPARState_Object = MibTableColumn
tnLOAMIfPARState = _TnLOAMIfPARState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 7, 1, 1, 1, 1, 4),
    _TnLOAMIfPARState_Type()
)
tnLOAMIfPARState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLOAMIfPARState.setStatus("current")
_TnLOAMConformance_ObjectIdentity = ObjectIdentity
tnLOAMConformance = _TnLOAMConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 7, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-LOAM-EXT-MIB",
    **{"tnLOAMExtMIB": tnLOAMExtMIB,
       "tnLOAMNotifications": tnLOAMNotifications,
       "tnLOAMObjects": tnLOAMObjects,
       "tnLOAMIfMgmt": tnLOAMIfMgmt,
       "tnLOAMIfMgmtTable": tnLOAMIfMgmtTable,
       "tnLOAMIfMgmtEntry": tnLOAMIfMgmtEntry,
       "tnLOAMIfModeCtrl": tnLOAMIfModeCtrl,
       "tnLOAMIfClearStats": tnLOAMIfClearStats,
       "tnLOAMIfMUXState": tnLOAMIfMUXState,
       "tnLOAMIfPARState": tnLOAMIfPARState,
       "tnLOAMConformance": tnLOAMConformance}
)
