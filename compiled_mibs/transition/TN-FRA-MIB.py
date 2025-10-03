# SNMP MIB module (TN-FRA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-FRA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:34 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnFraMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 21)
)
if mibBuilder.loadTexts:
    tnFraMIB.setRevisions(
        ("2012-06-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnFraObjects_ObjectIdentity = ObjectIdentity
tnFraObjects = _TnFraObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 21, 1)
)
_TnFraMgmt_ObjectIdentity = ObjectIdentity
tnFraMgmt = _TnFraMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 21, 1, 1)
)


class _TnFraRelayAlarmState_Type(Integer32):
    """Custom type tnFraRelayAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("negated", 2))
    )


_TnFraRelayAlarmState_Type.__name__ = "Integer32"
_TnFraRelayAlarmState_Object = MibScalar
tnFraRelayAlarmState = _TnFraRelayAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 21, 1, 1, 1),
    _TnFraRelayAlarmState_Type()
)
tnFraRelayAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnFraRelayAlarmState.setStatus("current")
_TnFraPowerSupplyTable_Object = MibTable
tnFraPowerSupplyTable = _TnFraPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 21, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnFraPowerSupplyTable.setStatus("current")
_TnFraPowerSupplyEntry_Object = MibTableRow
tnFraPowerSupplyEntry = _TnFraPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 21, 1, 1, 2, 1)
)
tnFraPowerSupplyEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnFraPowerSupplyEntry.setStatus("current")


class _TnFraPowerSupplyState_Type(Integer32):
    """Custom type tnFraPowerSupplyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnFraPowerSupplyState_Type.__name__ = "Integer32"
_TnFraPowerSupplyState_Object = MibTableColumn
tnFraPowerSupplyState = _TnFraPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 21, 1, 1, 2, 1, 1),
    _TnFraPowerSupplyState_Type()
)
tnFraPowerSupplyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnFraPowerSupplyState.setStatus("current")
_TnFraLinkTable_Object = MibTable
tnFraLinkTable = _TnFraLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 21, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tnFraLinkTable.setStatus("current")
_TnFraLinkEntry_Object = MibTableRow
tnFraLinkEntry = _TnFraLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 21, 1, 1, 3, 1)
)
tnFraLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnFraLinkEntry.setStatus("current")


class _TnFraLinkState_Type(Integer32):
    """Custom type tnFraLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnFraLinkState_Type.__name__ = "Integer32"
_TnFraLinkState_Object = MibTableColumn
tnFraLinkState = _TnFraLinkState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 21, 1, 1, 3, 1, 1),
    _TnFraLinkState_Type()
)
tnFraLinkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnFraLinkState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-FRA-MIB",
    **{"tnFraMIB": tnFraMIB,
       "tnFraObjects": tnFraObjects,
       "tnFraMgmt": tnFraMgmt,
       "tnFraRelayAlarmState": tnFraRelayAlarmState,
       "tnFraPowerSupplyTable": tnFraPowerSupplyTable,
       "tnFraPowerSupplyEntry": tnFraPowerSupplyEntry,
       "tnFraPowerSupplyState": tnFraPowerSupplyState,
       "tnFraLinkTable": tnFraLinkTable,
       "tnFraLinkEntry": tnFraLinkEntry,
       "tnFraLinkState": tnFraLinkState}
)
