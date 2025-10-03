# SNMP MIB module (CISCOSB-ProtectedPorts-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-ProtectedPorts-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:29:21 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlProtectedPorts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132)
)
if mibBuilder.loadTexts:
    rlProtectedPorts.setRevisions(
        ("2008-05-03 12:34",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlProtectedPortsTable_Object = MibTable
rlProtectedPortsTable = _RlProtectedPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 1)
)
if mibBuilder.loadTexts:
    rlProtectedPortsTable.setStatus("current")
_RlProtectedPortsEntry_Object = MibTableRow
rlProtectedPortsEntry = _RlProtectedPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 1, 1)
)
rlProtectedPortsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlProtectedPortsEntry.setStatus("current")


class _RlProtectedPortType_Type(Integer32):
    """Custom type rlProtectedPortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-protected", 1),
          ("protected", 2))
    )


_RlProtectedPortType_Type.__name__ = "Integer32"
_RlProtectedPortType_Object = MibTableColumn
rlProtectedPortType = _RlProtectedPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 1, 1, 1),
    _RlProtectedPortType_Type()
)
rlProtectedPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlProtectedPortType.setStatus("current")


class _RlProtectedPortCommunity_Type(Integer32):
    """Custom type rlProtectedPortCommunity based on Integer32"""
    defaultValue = 0


_RlProtectedPortCommunity_Type.__name__ = "Integer32"
_RlProtectedPortCommunity_Object = MibTableColumn
rlProtectedPortCommunity = _RlProtectedPortCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 1, 1, 2),
    _RlProtectedPortCommunity_Type()
)
rlProtectedPortCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlProtectedPortCommunity.setStatus("current")
_RlProtectedPortsStatusTable_Object = MibTable
rlProtectedPortsStatusTable = _RlProtectedPortsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 2)
)
if mibBuilder.loadTexts:
    rlProtectedPortsStatusTable.setStatus("current")
_RlProtectedPortsStatusEntry_Object = MibTableRow
rlProtectedPortsStatusEntry = _RlProtectedPortsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 2, 1)
)
rlProtectedPortsStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlProtectedPortsStatusEntry.setStatus("current")
_RlProtectedPortEgressPorts_Type = PortList
_RlProtectedPortEgressPorts_Object = MibTableColumn
rlProtectedPortEgressPorts = _RlProtectedPortEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 2, 1, 1),
    _RlProtectedPortEgressPorts_Type()
)
rlProtectedPortEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlProtectedPortEgressPorts.setStatus("current")


class _RlProtectedPortsGlobalEnable_Type(TruthValue):
    """Custom type rlProtectedPortsGlobalEnable based on TruthValue"""
    defaultValue = 2


_RlProtectedPortsGlobalEnable_Type.__name__ = "TruthValue"
_RlProtectedPortsGlobalEnable_Object = MibScalar
rlProtectedPortsGlobalEnable = _RlProtectedPortsGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 3),
    _RlProtectedPortsGlobalEnable_Type()
)
rlProtectedPortsGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlProtectedPortsGlobalEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-ProtectedPorts-MIB",
    **{"rlProtectedPorts": rlProtectedPorts,
       "rlProtectedPortsTable": rlProtectedPortsTable,
       "rlProtectedPortsEntry": rlProtectedPortsEntry,
       "rlProtectedPortType": rlProtectedPortType,
       "rlProtectedPortCommunity": rlProtectedPortCommunity,
       "rlProtectedPortsStatusTable": rlProtectedPortsStatusTable,
       "rlProtectedPortsStatusEntry": rlProtectedPortsStatusEntry,
       "rlProtectedPortEgressPorts": rlProtectedPortEgressPorts,
       "rlProtectedPortsGlobalEnable": rlProtectedPortsGlobalEnable}
)
