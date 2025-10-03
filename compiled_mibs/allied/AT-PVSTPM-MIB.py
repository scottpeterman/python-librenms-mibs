# SNMP MIB module (AT-PVSTPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\allied\AT-PVSTPM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:34 2025
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

pvstpm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140)
)
if mibBuilder.loadTexts:
    pvstpm.setRevisions(
        ("2006-03-29 16:51",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PvstpmEvents_ObjectIdentity = ObjectIdentity
pvstpmEvents = _PvstpmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 0)
)
_PvstpmEventVariables_ObjectIdentity = ObjectIdentity
pvstpmEventVariables = _PvstpmEventVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 1)
)
_PvstpmBridgeId_Type = OctetString
_PvstpmBridgeId_Object = MibScalar
pvstpmBridgeId = _PvstpmBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 1, 1),
    _PvstpmBridgeId_Type()
)
pvstpmBridgeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pvstpmBridgeId.setStatus("current")
_PvstpmTopologyChangeVlan_Type = VlanIndex
_PvstpmTopologyChangeVlan_Object = MibScalar
pvstpmTopologyChangeVlan = _PvstpmTopologyChangeVlan_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 1, 2),
    _PvstpmTopologyChangeVlan_Type()
)
pvstpmTopologyChangeVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pvstpmTopologyChangeVlan.setStatus("current")
_PvstpmRxPort_Type = Integer32
_PvstpmRxPort_Object = MibScalar
pvstpmRxPort = _PvstpmRxPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 1, 3),
    _PvstpmRxPort_Type()
)
pvstpmRxPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pvstpmRxPort.setStatus("current")
_PvstpmRxVlan_Type = VlanIndex
_PvstpmRxVlan_Object = MibScalar
pvstpmRxVlan = _PvstpmRxVlan_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 1, 4),
    _PvstpmRxVlan_Type()
)
pvstpmRxVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pvstpmRxVlan.setStatus("current")
_PvstpmTxVlan_Type = VlanIndex
_PvstpmTxVlan_Object = MibScalar
pvstpmTxVlan = _PvstpmTxVlan_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 1, 5),
    _PvstpmTxVlan_Type()
)
pvstpmTxVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pvstpmTxVlan.setStatus("current")

# Managed Objects groups


# Notification objects

pvstpmTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 0, 1)
)
pvstpmTopologyChange.setObjects(
      *(("AT-PVSTPM-MIB", "pvstpmBridgeId"),
        ("AT-PVSTPM-MIB", "pvstpmTopologyChangeVlan"))
)
if mibBuilder.loadTexts:
    pvstpmTopologyChange.setStatus(
        "current"
    )

pvstpmInconsistentBPDU = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 0, 2)
)
pvstpmInconsistentBPDU.setObjects(
      *(("AT-PVSTPM-MIB", "pvstpmBridgeId"),
        ("AT-PVSTPM-MIB", "pvstpmRxPort"),
        ("AT-PVSTPM-MIB", "pvstpmRxVlan"),
        ("AT-PVSTPM-MIB", "pvstpmTxVlan"))
)
if mibBuilder.loadTexts:
    pvstpmInconsistentBPDU.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-PVSTPM-MIB",
    **{"pvstpm": pvstpm,
       "pvstpmEvents": pvstpmEvents,
       "pvstpmTopologyChange": pvstpmTopologyChange,
       "pvstpmInconsistentBPDU": pvstpmInconsistentBPDU,
       "pvstpmEventVariables": pvstpmEventVariables,
       "pvstpmBridgeId": pvstpmBridgeId,
       "pvstpmTopologyChangeVlan": pvstpmTopologyChangeVlan,
       "pvstpmRxPort": pvstpmRxPort,
       "pvstpmRxVlan": pvstpmRxVlan,
       "pvstpmTxVlan": pvstpmTxVlan}
)
