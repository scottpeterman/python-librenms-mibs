# SNMP MIB module (AT-FIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\allied\AT-FIREWALL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:23 2025
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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

firewall = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77)
)
if mibBuilder.loadTexts:
    firewall.setRevisions(
        ("2006-06-28 12:22",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FirewallTraps_ObjectIdentity = ObjectIdentity
firewallTraps = _FirewallTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 0)
)
_FirewallTrapMessage_Type = DisplayString
_FirewallTrapMessage_Object = MibScalar
firewallTrapMessage = _FirewallTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 1),
    _FirewallTrapMessage_Type()
)
firewallTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallTrapMessage.setStatus("current")
_FirewallSessionsStatistics_ObjectIdentity = ObjectIdentity
firewallSessionsStatistics = _FirewallSessionsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 2)
)
_TotalNumberOfSessions_Type = Gauge32
_TotalNumberOfSessions_Object = MibScalar
totalNumberOfSessions = _TotalNumberOfSessions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 2, 1),
    _TotalNumberOfSessions_Type()
)
totalNumberOfSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalNumberOfSessions.setStatus("mandatory")


class _NumberOfSessionsPerNodeCountingStatus_Type(Integer32):
    """Custom type numberOfSessionsPerNodeCountingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_NumberOfSessionsPerNodeCountingStatus_Type.__name__ = "Integer32"
_NumberOfSessionsPerNodeCountingStatus_Object = MibScalar
numberOfSessionsPerNodeCountingStatus = _NumberOfSessionsPerNodeCountingStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 2, 2),
    _NumberOfSessionsPerNodeCountingStatus_Type()
)
numberOfSessionsPerNodeCountingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberOfSessionsPerNodeCountingStatus.setStatus("mandatory")
_NumberOfSessionsPerNodeTable_Object = MibTable
numberOfSessionsPerNodeTable = _NumberOfSessionsPerNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 2, 3)
)
if mibBuilder.loadTexts:
    numberOfSessionsPerNodeTable.setStatus("current")
_NumberOfSessionsPerNodeEntry_Object = MibTableRow
numberOfSessionsPerNodeEntry = _NumberOfSessionsPerNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 2, 3, 1)
)
numberOfSessionsPerNodeEntry.setIndexNames(
    (0, "AT-FIREWALL-MIB", "nodeIpAddress"),
)
if mibBuilder.loadTexts:
    numberOfSessionsPerNodeEntry.setStatus("current")
_NodeIpAddress_Type = IpAddress
_NodeIpAddress_Object = MibTableColumn
nodeIpAddress = _NodeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 2, 3, 1, 1),
    _NodeIpAddress_Type()
)
nodeIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeIpAddress.setStatus("current")
_NumberOfSessionsPerNode_Type = Gauge32
_NumberOfSessionsPerNode_Object = MibTableColumn
numberOfSessionsPerNode = _NumberOfSessionsPerNode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 2, 3, 1, 2),
    _NumberOfSessionsPerNode_Type()
)
numberOfSessionsPerNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfSessionsPerNode.setStatus("current")

# Managed Objects groups


# Notification objects

firewallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 0, 1)
)
firewallTrap.setObjects(
    ("AT-FIREWALL-MIB", "firewallTrapMessage")
)
if mibBuilder.loadTexts:
    firewallTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-FIREWALL-MIB",
    **{"firewall": firewall,
       "firewallTraps": firewallTraps,
       "firewallTrap": firewallTrap,
       "firewallTrapMessage": firewallTrapMessage,
       "firewallSessionsStatistics": firewallSessionsStatistics,
       "totalNumberOfSessions": totalNumberOfSessions,
       "numberOfSessionsPerNodeCountingStatus": numberOfSessionsPerNodeCountingStatus,
       "numberOfSessionsPerNodeTable": numberOfSessionsPerNodeTable,
       "numberOfSessionsPerNodeEntry": numberOfSessionsPerNodeEntry,
       "nodeIpAddress": nodeIpAddress,
       "numberOfSessionsPerNode": numberOfSessionsPerNode}
)
