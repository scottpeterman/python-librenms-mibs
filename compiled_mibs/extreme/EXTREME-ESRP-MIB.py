# SNMP MIB module (EXTREME-ESRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\extreme\EXTREME-ESRP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:27 2025
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

(ExtremeGenAddr,
 PortList,
 extremeAgent) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "ExtremeGenAddr",
    "PortList",
    "extremeAgent")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeEsrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeEsrpTable_Object = MibTable
extremeEsrpTable = _ExtremeEsrpTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2)
)
if mibBuilder.loadTexts:
    extremeEsrpTable.setStatus("current")
_ExtremeEsrpEntry_Object = MibTableRow
extremeEsrpEntry = _ExtremeEsrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1)
)
extremeEsrpEntry.setIndexNames(
    (0, "EXTREME-ESRP-MIB", "extremeEsrpVlanIfIndex"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpGroup"),
)
if mibBuilder.loadTexts:
    extremeEsrpEntry.setStatus("current")


class _ExtremeEsrpVlanIfIndex_Type(Integer32):
    """Custom type extremeEsrpVlanIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeEsrpVlanIfIndex_Type.__name__ = "Integer32"
_ExtremeEsrpVlanIfIndex_Object = MibTableColumn
extremeEsrpVlanIfIndex = _ExtremeEsrpVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 1),
    _ExtremeEsrpVlanIfIndex_Type()
)
extremeEsrpVlanIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeEsrpVlanIfIndex.setStatus("current")


class _ExtremeEsrpGroup_Type(Integer32):
    """Custom type extremeEsrpGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeEsrpGroup_Type.__name__ = "Integer32"
_ExtremeEsrpGroup_Object = MibTableColumn
extremeEsrpGroup = _ExtremeEsrpGroup_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 2),
    _ExtremeEsrpGroup_Type()
)
extremeEsrpGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeEsrpGroup.setStatus("current")
_ExtremeEsrpRowStatus_Type = RowStatus
_ExtremeEsrpRowStatus_Object = MibTableColumn
extremeEsrpRowStatus = _ExtremeEsrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 3),
    _ExtremeEsrpRowStatus_Type()
)
extremeEsrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpRowStatus.setStatus("current")
_ExtremeEsrpNetAddress_Type = ExtremeGenAddr
_ExtremeEsrpNetAddress_Object = MibTableColumn
extremeEsrpNetAddress = _ExtremeEsrpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 4),
    _ExtremeEsrpNetAddress_Type()
)
extremeEsrpNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNetAddress.setStatus("current")


class _ExtremeEsrpState_Type(Integer32):
    """Custom type extremeEsrpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("neutral", 1),
          ("master", 2),
          ("slave", 3))
    )


_ExtremeEsrpState_Type.__name__ = "Integer32"
_ExtremeEsrpState_Object = MibTableColumn
extremeEsrpState = _ExtremeEsrpState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 5),
    _ExtremeEsrpState_Type()
)
extremeEsrpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpState.setStatus("current")


class _ExtremeEsrpPriority_Type(Integer32):
    """Custom type extremeEsrpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ExtremeEsrpPriority_Type.__name__ = "Integer32"
_ExtremeEsrpPriority_Object = MibTableColumn
extremeEsrpPriority = _ExtremeEsrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 6),
    _ExtremeEsrpPriority_Type()
)
extremeEsrpPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpPriority.setStatus("current")


class _ExtremeEsrpElectionAlgorithm_Type(Integer32):
    """Custom type extremeEsrpElectionAlgorithm based on Integer32"""
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
        *(("portsTrackPriorityMac", 1),
          ("trackPortsPriorityMac", 2),
          ("priorityPortsTrackMac", 3),
          ("priorityTrackPortsMac", 4),
          ("priorityMacOnly", 5))
    )


_ExtremeEsrpElectionAlgorithm_Type.__name__ = "Integer32"
_ExtremeEsrpElectionAlgorithm_Object = MibTableColumn
extremeEsrpElectionAlgorithm = _ExtremeEsrpElectionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 7),
    _ExtremeEsrpElectionAlgorithm_Type()
)
extremeEsrpElectionAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpElectionAlgorithm.setStatus("current")


class _ExtremeEsrpHelloTimer_Type(Integer32):
    """Custom type extremeEsrpHelloTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ExtremeEsrpHelloTimer_Type.__name__ = "Integer32"
_ExtremeEsrpHelloTimer_Object = MibTableColumn
extremeEsrpHelloTimer = _ExtremeEsrpHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 8),
    _ExtremeEsrpHelloTimer_Type()
)
extremeEsrpHelloTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpHelloTimer.setStatus("current")


class _ExtremeEsrpActivePorts_Type(Integer32):
    """Custom type extremeEsrpActivePorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpActivePorts_Type.__name__ = "Integer32"
_ExtremeEsrpActivePorts_Object = MibTableColumn
extremeEsrpActivePorts = _ExtremeEsrpActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 9),
    _ExtremeEsrpActivePorts_Type()
)
extremeEsrpActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpActivePorts.setStatus("current")
_ExtremeEsrpTrackedActivePorts_Type = Integer32
_ExtremeEsrpTrackedActivePorts_Object = MibTableColumn
extremeEsrpTrackedActivePorts = _ExtremeEsrpTrackedActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 10),
    _ExtremeEsrpTrackedActivePorts_Type()
)
extremeEsrpTrackedActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpTrackedActivePorts.setStatus("current")
_ExtremeEsrpTrackedIpRoutes_Type = Integer32
_ExtremeEsrpTrackedIpRoutes_Object = MibTableColumn
extremeEsrpTrackedIpRoutes = _ExtremeEsrpTrackedIpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 11),
    _ExtremeEsrpTrackedIpRoutes_Type()
)
extremeEsrpTrackedIpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpTrackedIpRoutes.setStatus("current")
_ExtremeEsrpTrackedPings_Type = Integer32
_ExtremeEsrpTrackedPings_Object = MibTableColumn
extremeEsrpTrackedPings = _ExtremeEsrpTrackedPings_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 12),
    _ExtremeEsrpTrackedPings_Type()
)
extremeEsrpTrackedPings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpTrackedPings.setStatus("current")
_ExtremeEsrpNumTransitionsToMaster_Type = Integer32
_ExtremeEsrpNumTransitionsToMaster_Object = MibTableColumn
extremeEsrpNumTransitionsToMaster = _ExtremeEsrpNumTransitionsToMaster_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 13),
    _ExtremeEsrpNumTransitionsToMaster_Type()
)
extremeEsrpNumTransitionsToMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNumTransitionsToMaster.setStatus("current")
_ExtremeEsrpNumTransitionsToSlave_Type = Integer32
_ExtremeEsrpNumTransitionsToSlave_Object = MibTableColumn
extremeEsrpNumTransitionsToSlave = _ExtremeEsrpNumTransitionsToSlave_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 14),
    _ExtremeEsrpNumTransitionsToSlave_Type()
)
extremeEsrpNumTransitionsToSlave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNumTransitionsToSlave.setStatus("current")


class _ExtremeEsrpInternalActivePorts_Type(Integer32):
    """Custom type extremeEsrpInternalActivePorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpInternalActivePorts_Type.__name__ = "Integer32"
_ExtremeEsrpInternalActivePorts_Object = MibTableColumn
extremeEsrpInternalActivePorts = _ExtremeEsrpInternalActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 15),
    _ExtremeEsrpInternalActivePorts_Type()
)
extremeEsrpInternalActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpInternalActivePorts.setStatus("current")
_ExtremeEsrpNeighborTable_Object = MibTable
extremeEsrpNeighborTable = _ExtremeEsrpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3)
)
if mibBuilder.loadTexts:
    extremeEsrpNeighborTable.setStatus("current")
_ExtremeEsrpNeighborEntry_Object = MibTableRow
extremeEsrpNeighborEntry = _ExtremeEsrpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1)
)
extremeEsrpNeighborEntry.setIndexNames(
    (0, "EXTREME-ESRP-MIB", "extremeEsrpVlanIfIndex"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpGroup"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpNeighborMacAddress"),
)
if mibBuilder.loadTexts:
    extremeEsrpNeighborEntry.setStatus("current")
_ExtremeEsrpNeighborMacAddress_Type = MacAddress
_ExtremeEsrpNeighborMacAddress_Object = MibTableColumn
extremeEsrpNeighborMacAddress = _ExtremeEsrpNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 1),
    _ExtremeEsrpNeighborMacAddress_Type()
)
extremeEsrpNeighborMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeEsrpNeighborMacAddress.setStatus("current")


class _ExtremeEsrpNeighborGroup_Type(Integer32):
    """Custom type extremeEsrpNeighborGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeEsrpNeighborGroup_Type.__name__ = "Integer32"
_ExtremeEsrpNeighborGroup_Object = MibTableColumn
extremeEsrpNeighborGroup = _ExtremeEsrpNeighborGroup_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 2),
    _ExtremeEsrpNeighborGroup_Type()
)
extremeEsrpNeighborGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeEsrpNeighborGroup.setStatus("current")
_ExtremeEsrpNeighborNetAddress_Type = ExtremeGenAddr
_ExtremeEsrpNeighborNetAddress_Object = MibTableColumn
extremeEsrpNeighborNetAddress = _ExtremeEsrpNeighborNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 3),
    _ExtremeEsrpNeighborNetAddress_Type()
)
extremeEsrpNeighborNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNeighborNetAddress.setStatus("current")


class _ExtremeEsrpNeighborState_Type(Integer32):
    """Custom type extremeEsrpNeighborState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("neutral", 1),
          ("master", 2),
          ("slave", 3))
    )


_ExtremeEsrpNeighborState_Type.__name__ = "Integer32"
_ExtremeEsrpNeighborState_Object = MibTableColumn
extremeEsrpNeighborState = _ExtremeEsrpNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 4),
    _ExtremeEsrpNeighborState_Type()
)
extremeEsrpNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNeighborState.setStatus("current")
_ExtremeEsrpNeighborPriority_Type = Integer32
_ExtremeEsrpNeighborPriority_Object = MibTableColumn
extremeEsrpNeighborPriority = _ExtremeEsrpNeighborPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 5),
    _ExtremeEsrpNeighborPriority_Type()
)
extremeEsrpNeighborPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNeighborPriority.setStatus("current")


class _ExtremeEsrpNeighborElectionAlgorithm_Type(Integer32):
    """Custom type extremeEsrpNeighborElectionAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("portAndPriority", 1),
          ("priority", 2),
          ("priorityThenPort", 3))
    )


_ExtremeEsrpNeighborElectionAlgorithm_Type.__name__ = "Integer32"
_ExtremeEsrpNeighborElectionAlgorithm_Object = MibTableColumn
extremeEsrpNeighborElectionAlgorithm = _ExtremeEsrpNeighborElectionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 6),
    _ExtremeEsrpNeighborElectionAlgorithm_Type()
)
extremeEsrpNeighborElectionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNeighborElectionAlgorithm.setStatus("current")
_ExtremeEsrpNeighborHelloTimer_Type = Integer32
_ExtremeEsrpNeighborHelloTimer_Object = MibTableColumn
extremeEsrpNeighborHelloTimer = _ExtremeEsrpNeighborHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 7),
    _ExtremeEsrpNeighborHelloTimer_Type()
)
extremeEsrpNeighborHelloTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNeighborHelloTimer.setStatus("current")
_ExtremeEsrpNeighborActivePorts_Type = Integer32
_ExtremeEsrpNeighborActivePorts_Object = MibTableColumn
extremeEsrpNeighborActivePorts = _ExtremeEsrpNeighborActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 8),
    _ExtremeEsrpNeighborActivePorts_Type()
)
extremeEsrpNeighborActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNeighborActivePorts.setStatus("current")
_ExtremeEsrpNeighborTrackedActivePorts_Type = Integer32
_ExtremeEsrpNeighborTrackedActivePorts_Object = MibTableColumn
extremeEsrpNeighborTrackedActivePorts = _ExtremeEsrpNeighborTrackedActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 9),
    _ExtremeEsrpNeighborTrackedActivePorts_Type()
)
extremeEsrpNeighborTrackedActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNeighborTrackedActivePorts.setStatus("current")
_ExtremeEsrpNeighborTrackedIpRoutes_Type = Integer32
_ExtremeEsrpNeighborTrackedIpRoutes_Object = MibTableColumn
extremeEsrpNeighborTrackedIpRoutes = _ExtremeEsrpNeighborTrackedIpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 10),
    _ExtremeEsrpNeighborTrackedIpRoutes_Type()
)
extremeEsrpNeighborTrackedIpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNeighborTrackedIpRoutes.setStatus("current")
_ExtremeEsrpNeighborInternalActivePorts_Type = Integer32
_ExtremeEsrpNeighborInternalActivePorts_Object = MibTableColumn
extremeEsrpNeighborInternalActivePorts = _ExtremeEsrpNeighborInternalActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 11),
    _ExtremeEsrpNeighborInternalActivePorts_Type()
)
extremeEsrpNeighborInternalActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNeighborInternalActivePorts.setStatus("current")
_ExtremeEsrpTrackVlanTable_Object = MibTable
extremeEsrpTrackVlanTable = _ExtremeEsrpTrackVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 4)
)
if mibBuilder.loadTexts:
    extremeEsrpTrackVlanTable.setStatus("current")
_ExtremeEsrpTrackVlanEntry_Object = MibTableRow
extremeEsrpTrackVlanEntry = _ExtremeEsrpTrackVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 4, 1)
)
extremeEsrpTrackVlanEntry.setIndexNames(
    (0, "EXTREME-ESRP-MIB", "extremeEsrpVlanIfIndex"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpGroup"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpTrackVlanIfIndex"),
)
if mibBuilder.loadTexts:
    extremeEsrpTrackVlanEntry.setStatus("current")


class _ExtremeEsrpTrackVlanIfIndex_Type(Integer32):
    """Custom type extremeEsrpTrackVlanIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeEsrpTrackVlanIfIndex_Type.__name__ = "Integer32"
_ExtremeEsrpTrackVlanIfIndex_Object = MibTableColumn
extremeEsrpTrackVlanIfIndex = _ExtremeEsrpTrackVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 4, 1, 1),
    _ExtremeEsrpTrackVlanIfIndex_Type()
)
extremeEsrpTrackVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeEsrpTrackVlanIfIndex.setStatus("current")
_ExtremeEsrpTrackVlanRowStatus_Type = RowStatus
_ExtremeEsrpTrackVlanRowStatus_Object = MibTableColumn
extremeEsrpTrackVlanRowStatus = _ExtremeEsrpTrackVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 4, 1, 2),
    _ExtremeEsrpTrackVlanRowStatus_Type()
)
extremeEsrpTrackVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpTrackVlanRowStatus.setStatus("current")
_ExtremeEsrpTrackIpRouteTable_Object = MibTable
extremeEsrpTrackIpRouteTable = _ExtremeEsrpTrackIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 5)
)
if mibBuilder.loadTexts:
    extremeEsrpTrackIpRouteTable.setStatus("current")
_ExtremeEsrpTrackIpRouteEntry_Object = MibTableRow
extremeEsrpTrackIpRouteEntry = _ExtremeEsrpTrackIpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 5, 1)
)
extremeEsrpTrackIpRouteEntry.setIndexNames(
    (0, "EXTREME-ESRP-MIB", "extremeEsrpVlanIfIndex"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpGroup"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpTrackIpRouteIpAddress"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpTrackIpRouteNetMask"),
)
if mibBuilder.loadTexts:
    extremeEsrpTrackIpRouteEntry.setStatus("current")
_ExtremeEsrpTrackIpRouteIpAddress_Type = IpAddress
_ExtremeEsrpTrackIpRouteIpAddress_Object = MibTableColumn
extremeEsrpTrackIpRouteIpAddress = _ExtremeEsrpTrackIpRouteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 5, 1, 1),
    _ExtremeEsrpTrackIpRouteIpAddress_Type()
)
extremeEsrpTrackIpRouteIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeEsrpTrackIpRouteIpAddress.setStatus("current")
_ExtremeEsrpTrackIpRouteNetMask_Type = IpAddress
_ExtremeEsrpTrackIpRouteNetMask_Object = MibTableColumn
extremeEsrpTrackIpRouteNetMask = _ExtremeEsrpTrackIpRouteNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 5, 1, 2),
    _ExtremeEsrpTrackIpRouteNetMask_Type()
)
extremeEsrpTrackIpRouteNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeEsrpTrackIpRouteNetMask.setStatus("current")
_ExtremeEsrpTrackIpRouteRowStatus_Type = RowStatus
_ExtremeEsrpTrackIpRouteRowStatus_Object = MibTableColumn
extremeEsrpTrackIpRouteRowStatus = _ExtremeEsrpTrackIpRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 5, 1, 3),
    _ExtremeEsrpTrackIpRouteRowStatus_Type()
)
extremeEsrpTrackIpRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpTrackIpRouteRowStatus.setStatus("current")
_ExtremeEsrpPortTable_Object = MibTable
extremeEsrpPortTable = _ExtremeEsrpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 6)
)
if mibBuilder.loadTexts:
    extremeEsrpPortTable.setStatus("current")
_ExtremeEsrpPortEntry_Object = MibTableRow
extremeEsrpPortEntry = _ExtremeEsrpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 6, 1)
)
extremeEsrpPortEntry.setIndexNames(
    (0, "EXTREME-ESRP-MIB", "extremeEsrpVlanIfIndex"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpPortIfIndex"),
)
if mibBuilder.loadTexts:
    extremeEsrpPortEntry.setStatus("current")
_ExtremeEsrpPortIfIndex_Type = Integer32
_ExtremeEsrpPortIfIndex_Object = MibTableColumn
extremeEsrpPortIfIndex = _ExtremeEsrpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 6, 1, 1),
    _ExtremeEsrpPortIfIndex_Type()
)
extremeEsrpPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeEsrpPortIfIndex.setStatus("current")
_ExtremeEsrpPortState_Type = TruthValue
_ExtremeEsrpPortState_Object = MibTableColumn
extremeEsrpPortState = _ExtremeEsrpPortState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 6, 1, 2),
    _ExtremeEsrpPortState_Type()
)
extremeEsrpPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeEsrpPortState.setStatus("current")
_ExtremeEsrpNotifications_ObjectIdentity = ObjectIdentity
extremeEsrpNotifications = _ExtremeEsrpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 7)
)
_ExtremeEsrpNotificationsPrefix_ObjectIdentity = ObjectIdentity
extremeEsrpNotificationsPrefix = _ExtremeEsrpNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 7, 0)
)
_ExtremeEsrpObjects_ObjectIdentity = ObjectIdentity
extremeEsrpObjects = _ExtremeEsrpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8)
)
_ExtremeEsrpDomainTable_Object = MibTable
extremeEsrpDomainTable = _ExtremeEsrpDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1)
)
if mibBuilder.loadTexts:
    extremeEsrpDomainTable.setStatus("current")
_ExtremeEsrpDomainEntry_Object = MibTableRow
extremeEsrpDomainEntry = _ExtremeEsrpDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1)
)
extremeEsrpDomainEntry.setIndexNames(
    (0, "EXTREME-ESRP-MIB", "extremeEsrpDmnName"),
)
if mibBuilder.loadTexts:
    extremeEsrpDomainEntry.setStatus("current")


class _ExtremeEsrpDmnName_Type(DisplayString):
    """Custom type extremeEsrpDmnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ExtremeEsrpDmnName_Type.__name__ = "DisplayString"
_ExtremeEsrpDmnName_Object = MibTableColumn
extremeEsrpDmnName = _ExtremeEsrpDmnName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 1),
    _ExtremeEsrpDmnName_Type()
)
extremeEsrpDmnName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeEsrpDmnName.setStatus("current")


class _ExtremeEsrpDmnGroup_Type(Integer32):
    """Custom type extremeEsrpDmnGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ExtremeEsrpDmnGroup_Type.__name__ = "Integer32"
_ExtremeEsrpDmnGroup_Object = MibTableColumn
extremeEsrpDmnGroup = _ExtremeEsrpDmnGroup_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 2),
    _ExtremeEsrpDmnGroup_Type()
)
extremeEsrpDmnGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpDmnGroup.setStatus("current")


class _ExtremeEsrpDmnVersion_Type(Integer32):
    """Custom type extremeEsrpDmnVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_ExtremeEsrpDmnVersion_Type.__name__ = "Integer32"
_ExtremeEsrpDmnVersion_Object = MibTableColumn
extremeEsrpDmnVersion = _ExtremeEsrpDmnVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 3),
    _ExtremeEsrpDmnVersion_Type()
)
extremeEsrpDmnVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnVersion.setStatus("current")


class _ExtremeEsrpDmnAdminStatus_Type(Integer32):
    """Custom type extremeEsrpDmnAdminStatus based on Integer32"""
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


_ExtremeEsrpDmnAdminStatus_Type.__name__ = "Integer32"
_ExtremeEsrpDmnAdminStatus_Object = MibTableColumn
extremeEsrpDmnAdminStatus = _ExtremeEsrpDmnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 4),
    _ExtremeEsrpDmnAdminStatus_Type()
)
extremeEsrpDmnAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpDmnAdminStatus.setStatus("current")
_ExtremeEsrpDmnVlan_Type = DisplayString
_ExtremeEsrpDmnVlan_Object = MibTableColumn
extremeEsrpDmnVlan = _ExtremeEsrpDmnVlan_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 5),
    _ExtremeEsrpDmnVlan_Type()
)
extremeEsrpDmnVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnVlan.setStatus("current")


class _ExtremeEsrpDmnVlanTag_Type(Integer32):
    """Custom type extremeEsrpDmnVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_ExtremeEsrpDmnVlanTag_Type.__name__ = "Integer32"
_ExtremeEsrpDmnVlanTag_Object = MibTableColumn
extremeEsrpDmnVlanTag = _ExtremeEsrpDmnVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 6),
    _ExtremeEsrpDmnVlanTag_Type()
)
extremeEsrpDmnVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnVlanTag.setStatus("current")


class _ExtremeEsrpDmnId_Type(Integer32):
    """Custom type extremeEsrpDmnId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeEsrpDmnId_Type.__name__ = "Integer32"
_ExtremeEsrpDmnId_Object = MibTableColumn
extremeEsrpDmnId = _ExtremeEsrpDmnId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 7),
    _ExtremeEsrpDmnId_Type()
)
extremeEsrpDmnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpDmnId.setStatus("current")


class _ExtremeEsrpDmnState_Type(Integer32):
    """Custom type extremeEsrpDmnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("neutral", 0),
          ("master", 1),
          ("slave", 2),
          ("premaster", 3),
          ("aware", 4))
    )


_ExtremeEsrpDmnState_Type.__name__ = "Integer32"
_ExtremeEsrpDmnState_Object = MibTableColumn
extremeEsrpDmnState = _ExtremeEsrpDmnState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 8),
    _ExtremeEsrpDmnState_Type()
)
extremeEsrpDmnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnState.setStatus("current")
_ExtremeEsrpDmnNetAddress_Type = IpAddress
_ExtremeEsrpDmnNetAddress_Object = MibTableColumn
extremeEsrpDmnNetAddress = _ExtremeEsrpDmnNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 9),
    _ExtremeEsrpDmnNetAddress_Type()
)
extremeEsrpDmnNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnNetAddress.setStatus("current")
_ExtremeEsrpDmnMasterMacAddress_Type = MacAddress
_ExtremeEsrpDmnMasterMacAddress_Object = MibTableColumn
extremeEsrpDmnMasterMacAddress = _ExtremeEsrpDmnMasterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 10),
    _ExtremeEsrpDmnMasterMacAddress_Type()
)
extremeEsrpDmnMasterMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnMasterMacAddress.setStatus("current")


class _ExtremeEsrpDmnPriority_Type(Integer32):
    """Custom type extremeEsrpDmnPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExtremeEsrpDmnPriority_Type.__name__ = "Integer32"
_ExtremeEsrpDmnPriority_Object = MibTableColumn
extremeEsrpDmnPriority = _ExtremeEsrpDmnPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 11),
    _ExtremeEsrpDmnPriority_Type()
)
extremeEsrpDmnPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpDmnPriority.setStatus("current")


class _ExtremeEsrpDmnOperPriority_Type(Integer32):
    """Custom type extremeEsrpDmnOperPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExtremeEsrpDmnOperPriority_Type.__name__ = "Integer32"
_ExtremeEsrpDmnOperPriority_Object = MibTableColumn
extremeEsrpDmnOperPriority = _ExtremeEsrpDmnOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 12),
    _ExtremeEsrpDmnOperPriority_Type()
)
extremeEsrpDmnOperPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpDmnOperPriority.setStatus("current")


class _ExtremeEsrpDmnHelloTimer_Type(Integer32):
    """Custom type extremeEsrpDmnHelloTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ExtremeEsrpDmnHelloTimer_Type.__name__ = "Integer32"
_ExtremeEsrpDmnHelloTimer_Object = MibTableColumn
extremeEsrpDmnHelloTimer = _ExtremeEsrpDmnHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 13),
    _ExtremeEsrpDmnHelloTimer_Type()
)
extremeEsrpDmnHelloTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpDmnHelloTimer.setStatus("current")


class _ExtremeEsrpDmnNeutralTimer_Type(Integer32):
    """Custom type extremeEsrpDmnNeutralTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ExtremeEsrpDmnNeutralTimer_Type.__name__ = "Integer32"
_ExtremeEsrpDmnNeutralTimer_Object = MibTableColumn
extremeEsrpDmnNeutralTimer = _ExtremeEsrpDmnNeutralTimer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 14),
    _ExtremeEsrpDmnNeutralTimer_Type()
)
extremeEsrpDmnNeutralTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpDmnNeutralTimer.setStatus("current")


class _ExtremeEsrpDmnPreMasterTimer_Type(Integer32):
    """Custom type extremeEsrpDmnPreMasterTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ExtremeEsrpDmnPreMasterTimer_Type.__name__ = "Integer32"
_ExtremeEsrpDmnPreMasterTimer_Object = MibTableColumn
extremeEsrpDmnPreMasterTimer = _ExtremeEsrpDmnPreMasterTimer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 15),
    _ExtremeEsrpDmnPreMasterTimer_Type()
)
extremeEsrpDmnPreMasterTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpDmnPreMasterTimer.setStatus("current")


class _ExtremeEsrpDmnNbrTimer_Type(Integer32):
    """Custom type extremeEsrpDmnNbrTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ExtremeEsrpDmnNbrTimer_Type.__name__ = "Integer32"
_ExtremeEsrpDmnNbrTimer_Object = MibTableColumn
extremeEsrpDmnNbrTimer = _ExtremeEsrpDmnNbrTimer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 16),
    _ExtremeEsrpDmnNbrTimer_Type()
)
extremeEsrpDmnNbrTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpDmnNbrTimer.setStatus("current")


class _ExtremeEsrpDmnRestartTimer_Type(Integer32):
    """Custom type extremeEsrpDmnRestartTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ExtremeEsrpDmnRestartTimer_Type.__name__ = "Integer32"
_ExtremeEsrpDmnRestartTimer_Object = MibTableColumn
extremeEsrpDmnRestartTimer = _ExtremeEsrpDmnRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 17),
    _ExtremeEsrpDmnRestartTimer_Type()
)
extremeEsrpDmnRestartTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpDmnRestartTimer.setStatus("current")


class _ExtremeEsrpDmnActivePorts_Type(Integer32):
    """Custom type extremeEsrpDmnActivePorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnActivePorts_Type.__name__ = "Integer32"
_ExtremeEsrpDmnActivePorts_Object = MibTableColumn
extremeEsrpDmnActivePorts = _ExtremeEsrpDmnActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 18),
    _ExtremeEsrpDmnActivePorts_Type()
)
extremeEsrpDmnActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnActivePorts.setStatus("current")


class _ExtremeEsrpDmnActivePortWeight_Type(Integer32):
    """Custom type extremeEsrpDmnActivePortWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnActivePortWeight_Type.__name__ = "Integer32"
_ExtremeEsrpDmnActivePortWeight_Object = MibTableColumn
extremeEsrpDmnActivePortWeight = _ExtremeEsrpDmnActivePortWeight_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 19),
    _ExtremeEsrpDmnActivePortWeight_Type()
)
extremeEsrpDmnActivePortWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnActivePortWeight.setStatus("current")


class _ExtremeEsrpDmnInternalActivePorts_Type(Integer32):
    """Custom type extremeEsrpDmnInternalActivePorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnInternalActivePorts_Type.__name__ = "Integer32"
_ExtremeEsrpDmnInternalActivePorts_Object = MibTableColumn
extremeEsrpDmnInternalActivePorts = _ExtremeEsrpDmnInternalActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 20),
    _ExtremeEsrpDmnInternalActivePorts_Type()
)
extremeEsrpDmnInternalActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnInternalActivePorts.setStatus("current")


class _ExtremeEsrpDmnTrackedActivePorts_Type(Integer32):
    """Custom type extremeEsrpDmnTrackedActivePorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnTrackedActivePorts_Type.__name__ = "Integer32"
_ExtremeEsrpDmnTrackedActivePorts_Object = MibTableColumn
extremeEsrpDmnTrackedActivePorts = _ExtremeEsrpDmnTrackedActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 21),
    _ExtremeEsrpDmnTrackedActivePorts_Type()
)
extremeEsrpDmnTrackedActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnTrackedActivePorts.setStatus("current")


class _ExtremeEsrpDmnTrackedActivePortWeight_Type(Integer32):
    """Custom type extremeEsrpDmnTrackedActivePortWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnTrackedActivePortWeight_Type.__name__ = "Integer32"
_ExtremeEsrpDmnTrackedActivePortWeight_Object = MibTableColumn
extremeEsrpDmnTrackedActivePortWeight = _ExtremeEsrpDmnTrackedActivePortWeight_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 22),
    _ExtremeEsrpDmnTrackedActivePortWeight_Type()
)
extremeEsrpDmnTrackedActivePortWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnTrackedActivePortWeight.setStatus("current")


class _ExtremeEsrpDmnTrackedIpRoutes_Type(Integer32):
    """Custom type extremeEsrpDmnTrackedIpRoutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnTrackedIpRoutes_Type.__name__ = "Integer32"
_ExtremeEsrpDmnTrackedIpRoutes_Object = MibTableColumn
extremeEsrpDmnTrackedIpRoutes = _ExtremeEsrpDmnTrackedIpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 23),
    _ExtremeEsrpDmnTrackedIpRoutes_Type()
)
extremeEsrpDmnTrackedIpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnTrackedIpRoutes.setStatus("current")


class _ExtremeEsrpDmnTrackedPings_Type(Integer32):
    """Custom type extremeEsrpDmnTrackedPings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnTrackedPings_Type.__name__ = "Integer32"
_ExtremeEsrpDmnTrackedPings_Object = MibTableColumn
extremeEsrpDmnTrackedPings = _ExtremeEsrpDmnTrackedPings_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 24),
    _ExtremeEsrpDmnTrackedPings_Type()
)
extremeEsrpDmnTrackedPings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnTrackedPings.setStatus("current")


class _ExtremeEsrpDmnTrackedVlans_Type(Integer32):
    """Custom type extremeEsrpDmnTrackedVlans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnTrackedVlans_Type.__name__ = "Integer32"
_ExtremeEsrpDmnTrackedVlans_Object = MibTableColumn
extremeEsrpDmnTrackedVlans = _ExtremeEsrpDmnTrackedVlans_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 25),
    _ExtremeEsrpDmnTrackedVlans_Type()
)
extremeEsrpDmnTrackedVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnTrackedVlans.setStatus("current")


class _ExtremeEsrpDmnElectPreferenceForPorts_Type(Integer32):
    """Custom type extremeEsrpDmnElectPreferenceForPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnElectPreferenceForPorts_Type.__name__ = "Integer32"
_ExtremeEsrpDmnElectPreferenceForPorts_Object = MibTableColumn
extremeEsrpDmnElectPreferenceForPorts = _ExtremeEsrpDmnElectPreferenceForPorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 26),
    _ExtremeEsrpDmnElectPreferenceForPorts_Type()
)
extremeEsrpDmnElectPreferenceForPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpDmnElectPreferenceForPorts.setStatus("current")


class _ExtremeEsrpDmnElectPreferenceForPriority_Type(Integer32):
    """Custom type extremeEsrpDmnElectPreferenceForPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnElectPreferenceForPriority_Type.__name__ = "Integer32"
_ExtremeEsrpDmnElectPreferenceForPriority_Object = MibTableColumn
extremeEsrpDmnElectPreferenceForPriority = _ExtremeEsrpDmnElectPreferenceForPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 27),
    _ExtremeEsrpDmnElectPreferenceForPriority_Type()
)
extremeEsrpDmnElectPreferenceForPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpDmnElectPreferenceForPriority.setStatus("current")


class _ExtremeEsrpDmnElectPreferenceForMac_Type(Integer32):
    """Custom type extremeEsrpDmnElectPreferenceForMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnElectPreferenceForMac_Type.__name__ = "Integer32"
_ExtremeEsrpDmnElectPreferenceForMac_Object = MibTableColumn
extremeEsrpDmnElectPreferenceForMac = _ExtremeEsrpDmnElectPreferenceForMac_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 28),
    _ExtremeEsrpDmnElectPreferenceForMac_Type()
)
extremeEsrpDmnElectPreferenceForMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpDmnElectPreferenceForMac.setStatus("current")


class _ExtremeEsrpDmnElectPreferenceForTrack_Type(Integer32):
    """Custom type extremeEsrpDmnElectPreferenceForTrack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnElectPreferenceForTrack_Type.__name__ = "Integer32"
_ExtremeEsrpDmnElectPreferenceForTrack_Object = MibTableColumn
extremeEsrpDmnElectPreferenceForTrack = _ExtremeEsrpDmnElectPreferenceForTrack_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 29),
    _ExtremeEsrpDmnElectPreferenceForTrack_Type()
)
extremeEsrpDmnElectPreferenceForTrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpDmnElectPreferenceForTrack.setStatus("current")


class _ExtremeEsrpDmnElectPreferenceForSticky_Type(Integer32):
    """Custom type extremeEsrpDmnElectPreferenceForSticky based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnElectPreferenceForSticky_Type.__name__ = "Integer32"
_ExtremeEsrpDmnElectPreferenceForSticky_Object = MibTableColumn
extremeEsrpDmnElectPreferenceForSticky = _ExtremeEsrpDmnElectPreferenceForSticky_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 30),
    _ExtremeEsrpDmnElectPreferenceForSticky_Type()
)
extremeEsrpDmnElectPreferenceForSticky.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpDmnElectPreferenceForSticky.setStatus("current")


class _ExtremeEsrpDmnElectPreferenceForWeight_Type(Integer32):
    """Custom type extremeEsrpDmnElectPreferenceForWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnElectPreferenceForWeight_Type.__name__ = "Integer32"
_ExtremeEsrpDmnElectPreferenceForWeight_Object = MibTableColumn
extremeEsrpDmnElectPreferenceForWeight = _ExtremeEsrpDmnElectPreferenceForWeight_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 31),
    _ExtremeEsrpDmnElectPreferenceForWeight_Type()
)
extremeEsrpDmnElectPreferenceForWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpDmnElectPreferenceForWeight.setStatus("current")
_ExtremeEsrpDmnRowStatus_Type = RowStatus
_ExtremeEsrpDmnRowStatus_Object = MibTableColumn
extremeEsrpDmnRowStatus = _ExtremeEsrpDmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 1, 1, 32),
    _ExtremeEsrpDmnRowStatus_Type()
)
extremeEsrpDmnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpDmnRowStatus.setStatus("current")
_ExtremeEsrpDomainMemberTable_Object = MibTable
extremeEsrpDomainMemberTable = _ExtremeEsrpDomainMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 2)
)
if mibBuilder.loadTexts:
    extremeEsrpDomainMemberTable.setStatus("current")
_ExtremeEsrpDomainMemberEntry_Object = MibTableRow
extremeEsrpDomainMemberEntry = _ExtremeEsrpDomainMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 2, 1)
)
extremeEsrpDomainMemberEntry.setIndexNames(
    (0, "EXTREME-ESRP-MIB", "extremeEsrpDmnName"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpVlanDescr"),
)
if mibBuilder.loadTexts:
    extremeEsrpDomainMemberEntry.setStatus("current")


class _ExtremeEsrpVlanDescr_Type(DisplayString):
    """Custom type extremeEsrpVlanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ExtremeEsrpVlanDescr_Type.__name__ = "DisplayString"
_ExtremeEsrpVlanDescr_Object = MibTableColumn
extremeEsrpVlanDescr = _ExtremeEsrpVlanDescr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 2, 1, 1),
    _ExtremeEsrpVlanDescr_Type()
)
extremeEsrpVlanDescr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeEsrpVlanDescr.setStatus("current")


class _ExtremeEsrpVlanType_Type(Integer32):
    """Custom type extremeEsrpVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("protected", 2))
    )


_ExtremeEsrpVlanType_Type.__name__ = "Integer32"
_ExtremeEsrpVlanType_Object = MibTableColumn
extremeEsrpVlanType = _ExtremeEsrpVlanType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 2, 1, 2),
    _ExtremeEsrpVlanType_Type()
)
extremeEsrpVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpVlanType.setStatus("current")
_ExtremeEsrpDomainVlanIfIndex_Type = Integer32
_ExtremeEsrpDomainVlanIfIndex_Object = MibTableColumn
extremeEsrpDomainVlanIfIndex = _ExtremeEsrpDomainVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 2, 1, 3),
    _ExtremeEsrpDomainVlanIfIndex_Type()
)
extremeEsrpDomainVlanIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpDomainVlanIfIndex.setStatus("current")
_ExtremeEsrpVlanRowStatus_Type = RowStatus
_ExtremeEsrpVlanRowStatus_Object = MibTableColumn
extremeEsrpVlanRowStatus = _ExtremeEsrpVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 2, 1, 4),
    _ExtremeEsrpVlanRowStatus_Type()
)
extremeEsrpVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpVlanRowStatus.setStatus("current")
_ExtremeEsrpDomainNeighborTable_Object = MibTable
extremeEsrpDomainNeighborTable = _ExtremeEsrpDomainNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 3)
)
if mibBuilder.loadTexts:
    extremeEsrpDomainNeighborTable.setStatus("current")
_ExtremeEsrpDomainNeighborEntry_Object = MibTableRow
extremeEsrpDomainNeighborEntry = _ExtremeEsrpDomainNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 3, 1)
)
extremeEsrpDomainNeighborEntry.setIndexNames(
    (0, "EXTREME-ESRP-MIB", "extremeEsrpDmnName"),
)
if mibBuilder.loadTexts:
    extremeEsrpDomainNeighborEntry.setStatus("current")
_ExtremeEsrpDmnNeighborMacAddress_Type = MacAddress
_ExtremeEsrpDmnNeighborMacAddress_Object = MibTableColumn
extremeEsrpDmnNeighborMacAddress = _ExtremeEsrpDmnNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 3, 1, 1),
    _ExtremeEsrpDmnNeighborMacAddress_Type()
)
extremeEsrpDmnNeighborMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnNeighborMacAddress.setStatus("current")


class _ExtremeEsrpDmnNeighborGroup_Type(Integer32):
    """Custom type extremeEsrpDmnNeighborGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ExtremeEsrpDmnNeighborGroup_Type.__name__ = "Integer32"
_ExtremeEsrpDmnNeighborGroup_Object = MibTableColumn
extremeEsrpDmnNeighborGroup = _ExtremeEsrpDmnNeighborGroup_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 3, 1, 2),
    _ExtremeEsrpDmnNeighborGroup_Type()
)
extremeEsrpDmnNeighborGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnNeighborGroup.setStatus("current")
_ExtremeEsrpDmnNeighborNetAddress_Type = IpAddress
_ExtremeEsrpDmnNeighborNetAddress_Object = MibTableColumn
extremeEsrpDmnNeighborNetAddress = _ExtremeEsrpDmnNeighborNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 3, 1, 3),
    _ExtremeEsrpDmnNeighborNetAddress_Type()
)
extremeEsrpDmnNeighborNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnNeighborNetAddress.setStatus("current")


class _ExtremeEsrpDmnNeighborState_Type(Integer32):
    """Custom type extremeEsrpDmnNeighborState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("neutral", 0),
          ("master", 1),
          ("slave", 2),
          ("premaster", 3),
          ("aware", 4))
    )


_ExtremeEsrpDmnNeighborState_Type.__name__ = "Integer32"
_ExtremeEsrpDmnNeighborState_Object = MibTableColumn
extremeEsrpDmnNeighborState = _ExtremeEsrpDmnNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 3, 1, 4),
    _ExtremeEsrpDmnNeighborState_Type()
)
extremeEsrpDmnNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnNeighborState.setStatus("current")


class _ExtremeEsrpDmnNeighborPriority_Type(Integer32):
    """Custom type extremeEsrpDmnNeighborPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExtremeEsrpDmnNeighborPriority_Type.__name__ = "Integer32"
_ExtremeEsrpDmnNeighborPriority_Object = MibTableColumn
extremeEsrpDmnNeighborPriority = _ExtremeEsrpDmnNeighborPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 3, 1, 5),
    _ExtremeEsrpDmnNeighborPriority_Type()
)
extremeEsrpDmnNeighborPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnNeighborPriority.setStatus("current")


class _ExtremeEsrpDmnNeighborHelloTimer_Type(Integer32):
    """Custom type extremeEsrpDmnNeighborHelloTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ExtremeEsrpDmnNeighborHelloTimer_Type.__name__ = "Integer32"
_ExtremeEsrpDmnNeighborHelloTimer_Object = MibTableColumn
extremeEsrpDmnNeighborHelloTimer = _ExtremeEsrpDmnNeighborHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 3, 1, 6),
    _ExtremeEsrpDmnNeighborHelloTimer_Type()
)
extremeEsrpDmnNeighborHelloTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnNeighborHelloTimer.setStatus("current")


class _ExtremeEsrpDmnNeighborActivePorts_Type(Integer32):
    """Custom type extremeEsrpDmnNeighborActivePorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnNeighborActivePorts_Type.__name__ = "Integer32"
_ExtremeEsrpDmnNeighborActivePorts_Object = MibTableColumn
extremeEsrpDmnNeighborActivePorts = _ExtremeEsrpDmnNeighborActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 3, 1, 7),
    _ExtremeEsrpDmnNeighborActivePorts_Type()
)
extremeEsrpDmnNeighborActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnNeighborActivePorts.setStatus("current")


class _ExtremeEsrpDmnNeighborInternalActivePorts_Type(Integer32):
    """Custom type extremeEsrpDmnNeighborInternalActivePorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnNeighborInternalActivePorts_Type.__name__ = "Integer32"
_ExtremeEsrpDmnNeighborInternalActivePorts_Object = MibTableColumn
extremeEsrpDmnNeighborInternalActivePorts = _ExtremeEsrpDmnNeighborInternalActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 3, 1, 8),
    _ExtremeEsrpDmnNeighborInternalActivePorts_Type()
)
extremeEsrpDmnNeighborInternalActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnNeighborInternalActivePorts.setStatus("current")


class _ExtremeEsrpDmnNeighborTrackedActivePorts_Type(Integer32):
    """Custom type extremeEsrpDmnNeighborTrackedActivePorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnNeighborTrackedActivePorts_Type.__name__ = "Integer32"
_ExtremeEsrpDmnNeighborTrackedActivePorts_Object = MibTableColumn
extremeEsrpDmnNeighborTrackedActivePorts = _ExtremeEsrpDmnNeighborTrackedActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 3, 1, 9),
    _ExtremeEsrpDmnNeighborTrackedActivePorts_Type()
)
extremeEsrpDmnNeighborTrackedActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnNeighborTrackedActivePorts.setStatus("current")


class _ExtremeEsrpDmnNeighborTrackedIpCount_Type(Integer32):
    """Custom type extremeEsrpDmnNeighborTrackedIpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnNeighborTrackedIpCount_Type.__name__ = "Integer32"
_ExtremeEsrpDmnNeighborTrackedIpCount_Object = MibTableColumn
extremeEsrpDmnNeighborTrackedIpCount = _ExtremeEsrpDmnNeighborTrackedIpCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 3, 1, 10),
    _ExtremeEsrpDmnNeighborTrackedIpCount_Type()
)
extremeEsrpDmnNeighborTrackedIpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnNeighborTrackedIpCount.setStatus("current")


class _ExtremeEsrpDmnNeighborActivePortWeight_Type(Integer32):
    """Custom type extremeEsrpDmnNeighborActivePortWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnNeighborActivePortWeight_Type.__name__ = "Integer32"
_ExtremeEsrpDmnNeighborActivePortWeight_Object = MibTableColumn
extremeEsrpDmnNeighborActivePortWeight = _ExtremeEsrpDmnNeighborActivePortWeight_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 3, 1, 11),
    _ExtremeEsrpDmnNeighborActivePortWeight_Type()
)
extremeEsrpDmnNeighborActivePortWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnNeighborActivePortWeight.setStatus("current")


class _ExtremeEsrpDmnNeighborTrackedActivePortWeight_Type(Integer32):
    """Custom type extremeEsrpDmnNeighborTrackedActivePortWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpDmnNeighborTrackedActivePortWeight_Type.__name__ = "Integer32"
_ExtremeEsrpDmnNeighborTrackedActivePortWeight_Object = MibTableColumn
extremeEsrpDmnNeighborTrackedActivePortWeight = _ExtremeEsrpDmnNeighborTrackedActivePortWeight_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 3, 1, 12),
    _ExtremeEsrpDmnNeighborTrackedActivePortWeight_Type()
)
extremeEsrpDmnNeighborTrackedActivePortWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDmnNeighborTrackedActivePortWeight.setStatus("current")
_ExtremeEsrpDomainAwareTable_Object = MibTable
extremeEsrpDomainAwareTable = _ExtremeEsrpDomainAwareTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 4)
)
if mibBuilder.loadTexts:
    extremeEsrpDomainAwareTable.setStatus("current")
_ExtremeEsrpDomainAwareEntry_Object = MibTableRow
extremeEsrpDomainAwareEntry = _ExtremeEsrpDomainAwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 4, 1)
)
extremeEsrpDomainAwareEntry.setIndexNames(
    (0, "EXTREME-ESRP-MIB", "extremeEsrpDmnName"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpDmnGroup"),
)
if mibBuilder.loadTexts:
    extremeEsrpDomainAwareEntry.setStatus("current")
_ExtremeEsrpMasterMacAddress_Type = MacAddress
_ExtremeEsrpMasterMacAddress_Object = MibTableColumn
extremeEsrpMasterMacAddress = _ExtremeEsrpMasterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 4, 1, 1),
    _ExtremeEsrpMasterMacAddress_Type()
)
extremeEsrpMasterMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpMasterMacAddress.setStatus("current")


class _ExtremeEsrpMasterLastChanged_Type(DisplayString):
    """Custom type extremeEsrpMasterLastChanged based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ExtremeEsrpMasterLastChanged_Type.__name__ = "DisplayString"
_ExtremeEsrpMasterLastChanged_Object = MibTableColumn
extremeEsrpMasterLastChanged = _ExtremeEsrpMasterLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 4, 1, 2),
    _ExtremeEsrpMasterLastChanged_Type()
)
extremeEsrpMasterLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpMasterLastChanged.setStatus("current")
_ExtremeEsrpNumFdbFlushes_Type = Counter32
_ExtremeEsrpNumFdbFlushes_Object = MibTableColumn
extremeEsrpNumFdbFlushes = _ExtremeEsrpNumFdbFlushes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 4, 1, 3),
    _ExtremeEsrpNumFdbFlushes_Type()
)
extremeEsrpNumFdbFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNumFdbFlushes.setStatus("current")
_ExtremeEsrpHelloPktsReceived_Type = Counter32
_ExtremeEsrpHelloPktsReceived_Object = MibTableColumn
extremeEsrpHelloPktsReceived = _ExtremeEsrpHelloPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 4, 1, 4),
    _ExtremeEsrpHelloPktsReceived_Type()
)
extremeEsrpHelloPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpHelloPktsReceived.setStatus("current")
_ExtremeEsrpHelloPktsForwarded_Type = Counter32
_ExtremeEsrpHelloPktsForwarded_Object = MibTableColumn
extremeEsrpHelloPktsForwarded = _ExtremeEsrpHelloPktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 4, 1, 5),
    _ExtremeEsrpHelloPktsForwarded_Type()
)
extremeEsrpHelloPktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpHelloPktsForwarded.setStatus("current")
_ExtremeEsrpDomainStatsTable_Object = MibTable
extremeEsrpDomainStatsTable = _ExtremeEsrpDomainStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 5)
)
if mibBuilder.loadTexts:
    extremeEsrpDomainStatsTable.setStatus("current")
_ExtremeEsrpDomainStatsEntry_Object = MibTableRow
extremeEsrpDomainStatsEntry = _ExtremeEsrpDomainStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 5, 1)
)
extremeEsrpDomainStatsEntry.setIndexNames(
    (0, "EXTREME-ESRP-MIB", "extremeEsrpDmnName"),
)
if mibBuilder.loadTexts:
    extremeEsrpDomainStatsEntry.setStatus("current")


class _ExtremeEsrpLastStateChanged_Type(DisplayString):
    """Custom type extremeEsrpLastStateChanged based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ExtremeEsrpLastStateChanged_Type.__name__ = "DisplayString"
_ExtremeEsrpLastStateChanged_Object = MibTableColumn
extremeEsrpLastStateChanged = _ExtremeEsrpLastStateChanged_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 5, 1, 1),
    _ExtremeEsrpLastStateChanged_Type()
)
extremeEsrpLastStateChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpLastStateChanged.setStatus("current")
_ExtremeEsrpDomainNumTransitionsToMaster_Type = Counter32
_ExtremeEsrpDomainNumTransitionsToMaster_Object = MibTableColumn
extremeEsrpDomainNumTransitionsToMaster = _ExtremeEsrpDomainNumTransitionsToMaster_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 5, 1, 2),
    _ExtremeEsrpDomainNumTransitionsToMaster_Type()
)
extremeEsrpDomainNumTransitionsToMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDomainNumTransitionsToMaster.setStatus("current")
_ExtremeEsrpNumTransitionsToPreMaster_Type = Counter32
_ExtremeEsrpNumTransitionsToPreMaster_Object = MibTableColumn
extremeEsrpNumTransitionsToPreMaster = _ExtremeEsrpNumTransitionsToPreMaster_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 5, 1, 3),
    _ExtremeEsrpNumTransitionsToPreMaster_Type()
)
extremeEsrpNumTransitionsToPreMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNumTransitionsToPreMaster.setStatus("current")
_ExtremeEsrpDomainNumTransitionsToSlave_Type = Counter32
_ExtremeEsrpDomainNumTransitionsToSlave_Object = MibTableColumn
extremeEsrpDomainNumTransitionsToSlave = _ExtremeEsrpDomainNumTransitionsToSlave_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 5, 1, 4),
    _ExtremeEsrpDomainNumTransitionsToSlave_Type()
)
extremeEsrpDomainNumTransitionsToSlave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpDomainNumTransitionsToSlave.setStatus("current")
_ExtremeEsrpNumTransitionsToNeutral_Type = Counter32
_ExtremeEsrpNumTransitionsToNeutral_Object = MibTableColumn
extremeEsrpNumTransitionsToNeutral = _ExtremeEsrpNumTransitionsToNeutral_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 5, 1, 5),
    _ExtremeEsrpNumTransitionsToNeutral_Type()
)
extremeEsrpNumTransitionsToNeutral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNumTransitionsToNeutral.setStatus("current")
_ExtremeEsrpNumTransitionsToAware_Type = Counter32
_ExtremeEsrpNumTransitionsToAware_Object = MibTableColumn
extremeEsrpNumTransitionsToAware = _ExtremeEsrpNumTransitionsToAware_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 5, 1, 6),
    _ExtremeEsrpNumTransitionsToAware_Type()
)
extremeEsrpNumTransitionsToAware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNumTransitionsToAware.setStatus("current")
_ExtremeEsrpHelloPktsReceived1_Type = Counter32
_ExtremeEsrpHelloPktsReceived1_Object = MibTableColumn
extremeEsrpHelloPktsReceived1 = _ExtremeEsrpHelloPktsReceived1_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 5, 1, 7),
    _ExtremeEsrpHelloPktsReceived1_Type()
)
extremeEsrpHelloPktsReceived1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpHelloPktsReceived1.setStatus("current")
_ExtremeEsrpHelloPktsTransmitted_Type = Counter32
_ExtremeEsrpHelloPktsTransmitted_Object = MibTableColumn
extremeEsrpHelloPktsTransmitted = _ExtremeEsrpHelloPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 5, 1, 8),
    _ExtremeEsrpHelloPktsTransmitted_Type()
)
extremeEsrpHelloPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpHelloPktsTransmitted.setStatus("current")
_ExtremeEsrpAwareSelectForwardPortsTable_Object = MibTable
extremeEsrpAwareSelectForwardPortsTable = _ExtremeEsrpAwareSelectForwardPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 6)
)
if mibBuilder.loadTexts:
    extremeEsrpAwareSelectForwardPortsTable.setStatus("current")
_ExtremeEsrpAwareSelectForwardPortsEntry_Object = MibTableRow
extremeEsrpAwareSelectForwardPortsEntry = _ExtremeEsrpAwareSelectForwardPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 6, 1)
)
extremeEsrpAwareSelectForwardPortsEntry.setIndexNames(
    (0, "EXTREME-ESRP-MIB", "extremeEsrpAwareSelFwdListDmnName"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpAwareSelFwdListDmnGroup"),
)
if mibBuilder.loadTexts:
    extremeEsrpAwareSelectForwardPortsEntry.setStatus("current")
_ExtremeEsrpAwareSelFwdListDmnName_Type = DisplayString
_ExtremeEsrpAwareSelFwdListDmnName_Object = MibTableColumn
extremeEsrpAwareSelFwdListDmnName = _ExtremeEsrpAwareSelFwdListDmnName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 6, 1, 1),
    _ExtremeEsrpAwareSelFwdListDmnName_Type()
)
extremeEsrpAwareSelFwdListDmnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpAwareSelFwdListDmnName.setStatus("current")


class _ExtremeEsrpAwareSelFwdListDmnGroup_Type(Integer32):
    """Custom type extremeEsrpAwareSelFwdListDmnGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ExtremeEsrpAwareSelFwdListDmnGroup_Type.__name__ = "Integer32"
_ExtremeEsrpAwareSelFwdListDmnGroup_Object = MibTableColumn
extremeEsrpAwareSelFwdListDmnGroup = _ExtremeEsrpAwareSelFwdListDmnGroup_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 6, 1, 2),
    _ExtremeEsrpAwareSelFwdListDmnGroup_Type()
)
extremeEsrpAwareSelFwdListDmnGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpAwareSelFwdListDmnGroup.setStatus("current")


class _ExtremeEsrpAwareSelFwdListPortCount_Type(Integer32):
    """Custom type extremeEsrpAwareSelFwdListPortCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEsrpAwareSelFwdListPortCount_Type.__name__ = "Integer32"
_ExtremeEsrpAwareSelFwdListPortCount_Object = MibTableColumn
extremeEsrpAwareSelFwdListPortCount = _ExtremeEsrpAwareSelFwdListPortCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 6, 1, 3),
    _ExtremeEsrpAwareSelFwdListPortCount_Type()
)
extremeEsrpAwareSelFwdListPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpAwareSelFwdListPortCount.setStatus("current")
_ExtremeEsrpAwareSelFwdListPortList_Type = PortList
_ExtremeEsrpAwareSelFwdListPortList_Object = MibTableColumn
extremeEsrpAwareSelFwdListPortList = _ExtremeEsrpAwareSelFwdListPortList_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 8, 6, 1, 4),
    _ExtremeEsrpAwareSelFwdListPortList_Type()
)
extremeEsrpAwareSelFwdListPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpAwareSelFwdListPortList.setStatus("current")

# Managed Objects groups


# Notification objects

extremeEsrpDomainStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 7, 0, 1)
)
extremeEsrpDomainStateChange.setObjects(
      *(("EXTREME-ESRP-MIB", "extremeEsrpDmnName"),
        ("EXTREME-ESRP-MIB", "extremeEsrpDmnGroup"),
        ("EXTREME-ESRP-MIB", "extremeEsrpDmnState"),
        ("EXTREME-ESRP-MIB", "extremeEsrpDmnNetAddress"),
        ("EXTREME-ESRP-MIB", "extremeEsrpDmnMasterMacAddress"),
        ("EXTREME-ESRP-MIB", "extremeEsrpDmnActivePorts"),
        ("EXTREME-ESRP-MIB", "extremeEsrpDmnInternalActivePorts"),
        ("EXTREME-ESRP-MIB", "extremeEsrpDmnTrackedActivePorts"),
        ("EXTREME-ESRP-MIB", "extremeEsrpDmnTrackedIpRoutes"),
        ("EXTREME-ESRP-MIB", "extremeEsrpDmnTrackedPings"),
        ("EXTREME-ESRP-MIB", "extremeEsrpDmnActivePortWeight"),
        ("EXTREME-ESRP-MIB", "extremeEsrpDmnTrackedActivePortWeight"))
)
if mibBuilder.loadTexts:
    extremeEsrpDomainStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-ESRP-MIB",
    **{"extremeEsrp": extremeEsrp,
       "extremeEsrpTable": extremeEsrpTable,
       "extremeEsrpEntry": extremeEsrpEntry,
       "extremeEsrpVlanIfIndex": extremeEsrpVlanIfIndex,
       "extremeEsrpGroup": extremeEsrpGroup,
       "extremeEsrpRowStatus": extremeEsrpRowStatus,
       "extremeEsrpNetAddress": extremeEsrpNetAddress,
       "extremeEsrpState": extremeEsrpState,
       "extremeEsrpPriority": extremeEsrpPriority,
       "extremeEsrpElectionAlgorithm": extremeEsrpElectionAlgorithm,
       "extremeEsrpHelloTimer": extremeEsrpHelloTimer,
       "extremeEsrpActivePorts": extremeEsrpActivePorts,
       "extremeEsrpTrackedActivePorts": extremeEsrpTrackedActivePorts,
       "extremeEsrpTrackedIpRoutes": extremeEsrpTrackedIpRoutes,
       "extremeEsrpTrackedPings": extremeEsrpTrackedPings,
       "extremeEsrpNumTransitionsToMaster": extremeEsrpNumTransitionsToMaster,
       "extremeEsrpNumTransitionsToSlave": extremeEsrpNumTransitionsToSlave,
       "extremeEsrpInternalActivePorts": extremeEsrpInternalActivePorts,
       "extremeEsrpNeighborTable": extremeEsrpNeighborTable,
       "extremeEsrpNeighborEntry": extremeEsrpNeighborEntry,
       "extremeEsrpNeighborMacAddress": extremeEsrpNeighborMacAddress,
       "extremeEsrpNeighborGroup": extremeEsrpNeighborGroup,
       "extremeEsrpNeighborNetAddress": extremeEsrpNeighborNetAddress,
       "extremeEsrpNeighborState": extremeEsrpNeighborState,
       "extremeEsrpNeighborPriority": extremeEsrpNeighborPriority,
       "extremeEsrpNeighborElectionAlgorithm": extremeEsrpNeighborElectionAlgorithm,
       "extremeEsrpNeighborHelloTimer": extremeEsrpNeighborHelloTimer,
       "extremeEsrpNeighborActivePorts": extremeEsrpNeighborActivePorts,
       "extremeEsrpNeighborTrackedActivePorts": extremeEsrpNeighborTrackedActivePorts,
       "extremeEsrpNeighborTrackedIpRoutes": extremeEsrpNeighborTrackedIpRoutes,
       "extremeEsrpNeighborInternalActivePorts": extremeEsrpNeighborInternalActivePorts,
       "extremeEsrpTrackVlanTable": extremeEsrpTrackVlanTable,
       "extremeEsrpTrackVlanEntry": extremeEsrpTrackVlanEntry,
       "extremeEsrpTrackVlanIfIndex": extremeEsrpTrackVlanIfIndex,
       "extremeEsrpTrackVlanRowStatus": extremeEsrpTrackVlanRowStatus,
       "extremeEsrpTrackIpRouteTable": extremeEsrpTrackIpRouteTable,
       "extremeEsrpTrackIpRouteEntry": extremeEsrpTrackIpRouteEntry,
       "extremeEsrpTrackIpRouteIpAddress": extremeEsrpTrackIpRouteIpAddress,
       "extremeEsrpTrackIpRouteNetMask": extremeEsrpTrackIpRouteNetMask,
       "extremeEsrpTrackIpRouteRowStatus": extremeEsrpTrackIpRouteRowStatus,
       "extremeEsrpPortTable": extremeEsrpPortTable,
       "extremeEsrpPortEntry": extremeEsrpPortEntry,
       "extremeEsrpPortIfIndex": extremeEsrpPortIfIndex,
       "extremeEsrpPortState": extremeEsrpPortState,
       "extremeEsrpNotifications": extremeEsrpNotifications,
       "extremeEsrpNotificationsPrefix": extremeEsrpNotificationsPrefix,
       "extremeEsrpDomainStateChange": extremeEsrpDomainStateChange,
       "extremeEsrpObjects": extremeEsrpObjects,
       "extremeEsrpDomainTable": extremeEsrpDomainTable,
       "extremeEsrpDomainEntry": extremeEsrpDomainEntry,
       "extremeEsrpDmnName": extremeEsrpDmnName,
       "extremeEsrpDmnGroup": extremeEsrpDmnGroup,
       "extremeEsrpDmnVersion": extremeEsrpDmnVersion,
       "extremeEsrpDmnAdminStatus": extremeEsrpDmnAdminStatus,
       "extremeEsrpDmnVlan": extremeEsrpDmnVlan,
       "extremeEsrpDmnVlanTag": extremeEsrpDmnVlanTag,
       "extremeEsrpDmnId": extremeEsrpDmnId,
       "extremeEsrpDmnState": extremeEsrpDmnState,
       "extremeEsrpDmnNetAddress": extremeEsrpDmnNetAddress,
       "extremeEsrpDmnMasterMacAddress": extremeEsrpDmnMasterMacAddress,
       "extremeEsrpDmnPriority": extremeEsrpDmnPriority,
       "extremeEsrpDmnOperPriority": extremeEsrpDmnOperPriority,
       "extremeEsrpDmnHelloTimer": extremeEsrpDmnHelloTimer,
       "extremeEsrpDmnNeutralTimer": extremeEsrpDmnNeutralTimer,
       "extremeEsrpDmnPreMasterTimer": extremeEsrpDmnPreMasterTimer,
       "extremeEsrpDmnNbrTimer": extremeEsrpDmnNbrTimer,
       "extremeEsrpDmnRestartTimer": extremeEsrpDmnRestartTimer,
       "extremeEsrpDmnActivePorts": extremeEsrpDmnActivePorts,
       "extremeEsrpDmnActivePortWeight": extremeEsrpDmnActivePortWeight,
       "extremeEsrpDmnInternalActivePorts": extremeEsrpDmnInternalActivePorts,
       "extremeEsrpDmnTrackedActivePorts": extremeEsrpDmnTrackedActivePorts,
       "extremeEsrpDmnTrackedActivePortWeight": extremeEsrpDmnTrackedActivePortWeight,
       "extremeEsrpDmnTrackedIpRoutes": extremeEsrpDmnTrackedIpRoutes,
       "extremeEsrpDmnTrackedPings": extremeEsrpDmnTrackedPings,
       "extremeEsrpDmnTrackedVlans": extremeEsrpDmnTrackedVlans,
       "extremeEsrpDmnElectPreferenceForPorts": extremeEsrpDmnElectPreferenceForPorts,
       "extremeEsrpDmnElectPreferenceForPriority": extremeEsrpDmnElectPreferenceForPriority,
       "extremeEsrpDmnElectPreferenceForMac": extremeEsrpDmnElectPreferenceForMac,
       "extremeEsrpDmnElectPreferenceForTrack": extremeEsrpDmnElectPreferenceForTrack,
       "extremeEsrpDmnElectPreferenceForSticky": extremeEsrpDmnElectPreferenceForSticky,
       "extremeEsrpDmnElectPreferenceForWeight": extremeEsrpDmnElectPreferenceForWeight,
       "extremeEsrpDmnRowStatus": extremeEsrpDmnRowStatus,
       "extremeEsrpDomainMemberTable": extremeEsrpDomainMemberTable,
       "extremeEsrpDomainMemberEntry": extremeEsrpDomainMemberEntry,
       "extremeEsrpVlanDescr": extremeEsrpVlanDescr,
       "extremeEsrpVlanType": extremeEsrpVlanType,
       "extremeEsrpDomainVlanIfIndex": extremeEsrpDomainVlanIfIndex,
       "extremeEsrpVlanRowStatus": extremeEsrpVlanRowStatus,
       "extremeEsrpDomainNeighborTable": extremeEsrpDomainNeighborTable,
       "extremeEsrpDomainNeighborEntry": extremeEsrpDomainNeighborEntry,
       "extremeEsrpDmnNeighborMacAddress": extremeEsrpDmnNeighborMacAddress,
       "extremeEsrpDmnNeighborGroup": extremeEsrpDmnNeighborGroup,
       "extremeEsrpDmnNeighborNetAddress": extremeEsrpDmnNeighborNetAddress,
       "extremeEsrpDmnNeighborState": extremeEsrpDmnNeighborState,
       "extremeEsrpDmnNeighborPriority": extremeEsrpDmnNeighborPriority,
       "extremeEsrpDmnNeighborHelloTimer": extremeEsrpDmnNeighborHelloTimer,
       "extremeEsrpDmnNeighborActivePorts": extremeEsrpDmnNeighborActivePorts,
       "extremeEsrpDmnNeighborInternalActivePorts": extremeEsrpDmnNeighborInternalActivePorts,
       "extremeEsrpDmnNeighborTrackedActivePorts": extremeEsrpDmnNeighborTrackedActivePorts,
       "extremeEsrpDmnNeighborTrackedIpCount": extremeEsrpDmnNeighborTrackedIpCount,
       "extremeEsrpDmnNeighborActivePortWeight": extremeEsrpDmnNeighborActivePortWeight,
       "extremeEsrpDmnNeighborTrackedActivePortWeight": extremeEsrpDmnNeighborTrackedActivePortWeight,
       "extremeEsrpDomainAwareTable": extremeEsrpDomainAwareTable,
       "extremeEsrpDomainAwareEntry": extremeEsrpDomainAwareEntry,
       "extremeEsrpMasterMacAddress": extremeEsrpMasterMacAddress,
       "extremeEsrpMasterLastChanged": extremeEsrpMasterLastChanged,
       "extremeEsrpNumFdbFlushes": extremeEsrpNumFdbFlushes,
       "extremeEsrpHelloPktsReceived": extremeEsrpHelloPktsReceived,
       "extremeEsrpHelloPktsForwarded": extremeEsrpHelloPktsForwarded,
       "extremeEsrpDomainStatsTable": extremeEsrpDomainStatsTable,
       "extremeEsrpDomainStatsEntry": extremeEsrpDomainStatsEntry,
       "extremeEsrpLastStateChanged": extremeEsrpLastStateChanged,
       "extremeEsrpDomainNumTransitionsToMaster": extremeEsrpDomainNumTransitionsToMaster,
       "extremeEsrpNumTransitionsToPreMaster": extremeEsrpNumTransitionsToPreMaster,
       "extremeEsrpDomainNumTransitionsToSlave": extremeEsrpDomainNumTransitionsToSlave,
       "extremeEsrpNumTransitionsToNeutral": extremeEsrpNumTransitionsToNeutral,
       "extremeEsrpNumTransitionsToAware": extremeEsrpNumTransitionsToAware,
       "extremeEsrpHelloPktsReceived1": extremeEsrpHelloPktsReceived1,
       "extremeEsrpHelloPktsTransmitted": extremeEsrpHelloPktsTransmitted,
       "extremeEsrpAwareSelectForwardPortsTable": extremeEsrpAwareSelectForwardPortsTable,
       "extremeEsrpAwareSelectForwardPortsEntry": extremeEsrpAwareSelectForwardPortsEntry,
       "extremeEsrpAwareSelFwdListDmnName": extremeEsrpAwareSelFwdListDmnName,
       "extremeEsrpAwareSelFwdListDmnGroup": extremeEsrpAwareSelFwdListDmnGroup,
       "extremeEsrpAwareSelFwdListPortCount": extremeEsrpAwareSelFwdListPortCount,
       "extremeEsrpAwareSelFwdListPortList": extremeEsrpAwareSelFwdListPortList}
)
