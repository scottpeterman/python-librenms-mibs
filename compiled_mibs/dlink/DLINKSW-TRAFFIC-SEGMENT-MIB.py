# SNMP MIB module (DLINKSW-TRAFFIC-SEGMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-TRAFFIC-SEGMENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:05 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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


# MODULE-IDENTITY

dlinkSwTrafficSegMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 26)
)
if mibBuilder.loadTexts:
    dlinkSwTrafficSegMIB.setRevisions(
        ("2013-03-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DTrafficSegNotifications_ObjectIdentity = ObjectIdentity
dTrafficSegNotifications = _DTrafficSegNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 26, 0)
)
_DTrafficSegObjects_ObjectIdentity = ObjectIdentity
dTrafficSegObjects = _DTrafficSegObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 26, 1)
)
_DTrafficSegForwardDomainTable_Object = MibTable
dTrafficSegForwardDomainTable = _DTrafficSegForwardDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 26, 1, 1)
)
if mibBuilder.loadTexts:
    dTrafficSegForwardDomainTable.setStatus("current")
_DTrafficSegForwardDomainEntry_Object = MibTableRow
dTrafficSegForwardDomainEntry = _DTrafficSegForwardDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 26, 1, 1, 1)
)
dTrafficSegForwardDomainEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dTrafficSegForwardDomainEntry.setStatus("current")
_DTrafficSegForwardPorts_Type = PortList
_DTrafficSegForwardPorts_Object = MibTableColumn
dTrafficSegForwardPorts = _DTrafficSegForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 26, 1, 1, 1, 1),
    _DTrafficSegForwardPorts_Type()
)
dTrafficSegForwardPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTrafficSegForwardPorts.setStatus("current")
_DTrafficSegConformance_ObjectIdentity = ObjectIdentity
dTrafficSegConformance = _DTrafficSegConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 26, 2)
)
_DTrafficSegMIBCompliances_ObjectIdentity = ObjectIdentity
dTrafficSegMIBCompliances = _DTrafficSegMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 26, 2, 1)
)
_DTrafficSegMIBGroups_ObjectIdentity = ObjectIdentity
dTrafficSegMIBGroups = _DTrafficSegMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 26, 2, 2)
)

# Managed Objects groups

dTrafficSegIfCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 26, 2, 2, 1)
)
dTrafficSegIfCfgGroup.setObjects(
    ("DLINKSW-TRAFFIC-SEGMENT-MIB", "dTrafficSegForwardPorts")
)
if mibBuilder.loadTexts:
    dTrafficSegIfCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dTrafficSegMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 26, 2, 1, 1)
)
dTrafficSegMIBCompliance.setObjects(
    ("DLINKSW-TRAFFIC-SEGMENT-MIB", "dTrafficSegIfCfgGroup")
)
if mibBuilder.loadTexts:
    dTrafficSegMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-TRAFFIC-SEGMENT-MIB",
    **{"dlinkSwTrafficSegMIB": dlinkSwTrafficSegMIB,
       "dTrafficSegNotifications": dTrafficSegNotifications,
       "dTrafficSegObjects": dTrafficSegObjects,
       "dTrafficSegForwardDomainTable": dTrafficSegForwardDomainTable,
       "dTrafficSegForwardDomainEntry": dTrafficSegForwardDomainEntry,
       "dTrafficSegForwardPorts": dTrafficSegForwardPorts,
       "dTrafficSegConformance": dTrafficSegConformance,
       "dTrafficSegMIBCompliances": dTrafficSegMIBCompliances,
       "dTrafficSegMIBCompliance": dTrafficSegMIBCompliance,
       "dTrafficSegMIBGroups": dTrafficSegMIBGroups,
       "dTrafficSegIfCfgGroup": dTrafficSegIfCfgGroup}
)
