# SNMP MIB module (SL-L2TOPOLOGY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-L2TOPOLOGY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:52 2025
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

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(slMain,) = mibBuilder.importSymbols(
    "SL-MAIN-MIB",
    "slMain")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

slL2Topology = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TopologyL2Links_ObjectIdentity = ObjectIdentity
topologyL2Links = _TopologyL2Links_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1)
)
_TopologyL2LinkTable_Object = MibTable
topologyL2LinkTable = _TopologyL2LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1)
)
if mibBuilder.loadTexts:
    topologyL2LinkTable.setStatus("current")
_TopologyL2LinkEntry_Object = MibTableRow
topologyL2LinkEntry = _TopologyL2LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1)
)
topologyL2LinkEntry.setIndexNames(
    (0, "SL-L2TOPOLOGY-MIB", "topologyL2LinkLocalIp"),
    (0, "SL-L2TOPOLOGY-MIB", "topologyL2LinkLocalPort"),
)
if mibBuilder.loadTexts:
    topologyL2LinkEntry.setStatus("current")
_TopologyL2LinkLocalIp_Type = IpAddress
_TopologyL2LinkLocalIp_Object = MibTableColumn
topologyL2LinkLocalIp = _TopologyL2LinkLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 1),
    _TopologyL2LinkLocalIp_Type()
)
topologyL2LinkLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologyL2LinkLocalIp.setStatus("current")
_TopologyL2LinkLocalPort_Type = Integer32
_TopologyL2LinkLocalPort_Object = MibTableColumn
topologyL2LinkLocalPort = _TopologyL2LinkLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 2),
    _TopologyL2LinkLocalPort_Type()
)
topologyL2LinkLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologyL2LinkLocalPort.setStatus("current")
_TopologyL2LinkLocalMac_Type = PhysAddress
_TopologyL2LinkLocalMac_Object = MibTableColumn
topologyL2LinkLocalMac = _TopologyL2LinkLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 3),
    _TopologyL2LinkLocalMac_Type()
)
topologyL2LinkLocalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologyL2LinkLocalMac.setStatus("current")


class _TopologyL2LinkLocalTid_Type(DisplayString):
    """Custom type topologyL2LinkLocalTid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TopologyL2LinkLocalTid_Type.__name__ = "DisplayString"
_TopologyL2LinkLocalTid_Object = MibTableColumn
topologyL2LinkLocalTid = _TopologyL2LinkLocalTid_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 4),
    _TopologyL2LinkLocalTid_Type()
)
topologyL2LinkLocalTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologyL2LinkLocalTid.setStatus("current")
_TopologyL2LinkRemoteIp_Type = IpAddress
_TopologyL2LinkRemoteIp_Object = MibTableColumn
topologyL2LinkRemoteIp = _TopologyL2LinkRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 5),
    _TopologyL2LinkRemoteIp_Type()
)
topologyL2LinkRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologyL2LinkRemoteIp.setStatus("current")
_TopologyL2LinkRemotePort_Type = Integer32
_TopologyL2LinkRemotePort_Object = MibTableColumn
topologyL2LinkRemotePort = _TopologyL2LinkRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 6),
    _TopologyL2LinkRemotePort_Type()
)
topologyL2LinkRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologyL2LinkRemotePort.setStatus("current")
_TopologyL2LinkRemoteMac_Type = PhysAddress
_TopologyL2LinkRemoteMac_Object = MibTableColumn
topologyL2LinkRemoteMac = _TopologyL2LinkRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 7),
    _TopologyL2LinkRemoteMac_Type()
)
topologyL2LinkRemoteMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologyL2LinkRemoteMac.setStatus("current")


class _TopologyL2LinkRemoteTid_Type(DisplayString):
    """Custom type topologyL2LinkRemoteTid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TopologyL2LinkRemoteTid_Type.__name__ = "DisplayString"
_TopologyL2LinkRemoteTid_Object = MibTableColumn
topologyL2LinkRemoteTid = _TopologyL2LinkRemoteTid_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 8),
    _TopologyL2LinkRemoteTid_Type()
)
topologyL2LinkRemoteTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologyL2LinkRemoteTid.setStatus("current")
_TopologyL2Traps_ObjectIdentity = ObjectIdentity
topologyL2Traps = _TopologyL2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 2)
)
_TopologyL2LastChange_Type = TimeStamp
_TopologyL2LastChange_Object = MibScalar
topologyL2LastChange = _TopologyL2LastChange_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 2, 1),
    _TopologyL2LastChange_Type()
)
topologyL2LastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologyL2LastChange.setStatus("current")


class _TopologyL2ChangeTrapEnable_Type(TruthValue):
    """Custom type topologyL2ChangeTrapEnable based on TruthValue"""
    defaultValue = 1


_TopologyL2ChangeTrapEnable_Type.__name__ = "TruthValue"
_TopologyL2ChangeTrapEnable_Object = MibScalar
topologyL2ChangeTrapEnable = _TopologyL2ChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 2, 2),
    _TopologyL2ChangeTrapEnable_Type()
)
topologyL2ChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyL2ChangeTrapEnable.setStatus("current")

# Managed Objects groups


# Notification objects

topologyL2LinkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 2, 3)
)
if mibBuilder.loadTexts:
    topologyL2LinkChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-L2TOPOLOGY-MIB",
    **{"slL2Topology": slL2Topology,
       "topologyL2Links": topologyL2Links,
       "topologyL2LinkTable": topologyL2LinkTable,
       "topologyL2LinkEntry": topologyL2LinkEntry,
       "topologyL2LinkLocalIp": topologyL2LinkLocalIp,
       "topologyL2LinkLocalPort": topologyL2LinkLocalPort,
       "topologyL2LinkLocalMac": topologyL2LinkLocalMac,
       "topologyL2LinkLocalTid": topologyL2LinkLocalTid,
       "topologyL2LinkRemoteIp": topologyL2LinkRemoteIp,
       "topologyL2LinkRemotePort": topologyL2LinkRemotePort,
       "topologyL2LinkRemoteMac": topologyL2LinkRemoteMac,
       "topologyL2LinkRemoteTid": topologyL2LinkRemoteTid,
       "topologyL2Traps": topologyL2Traps,
       "topologyL2LastChange": topologyL2LastChange,
       "topologyL2ChangeTrapEnable": topologyL2ChangeTrapEnable,
       "topologyL2LinkChange": topologyL2LinkChange}
)
