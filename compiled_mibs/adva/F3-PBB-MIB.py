# SNMP MIB module (F3-PBB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-PBB-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:16:33 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(PerfCounter64,) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "PerfCounter64")

(FlowTagControl,
 cmEthernetAccPortEntry,
 cmEthernetNetPortEntry,
 cmFlowEntry) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "FlowTagControl",
    "cmEthernetAccPortEntry",
    "cmEthernetNetPortEntry",
    "cmFlowEntry")

(ipManagementTunnelEntry,) = mibBuilder.importSymbols(
    "CM-IP-MIB",
    "ipManagementTunnelEntry")

(cmEthernetNetPortHistoryEntry,
 cmEthernetNetPortStatsEntry) = mibBuilder.importSymbols(
    "CM-PERFORMANCE-MIB",
    "cmEthernetNetPortHistoryEntry",
    "cmEthernetNetPortStatsEntry")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3PBBMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21)
)
if mibBuilder.loadTexts:
    f3PBBMIB.setRevisions(
        ("2012-10-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F3PBBConfigObjects_ObjectIdentity = ObjectIdentity
f3PBBConfigObjects = _F3PBBConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1)
)
_F3PbbEthernetAccPortTable_Object = MibTable
f3PbbEthernetAccPortTable = _F3PbbEthernetAccPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 1)
)
if mibBuilder.loadTexts:
    f3PbbEthernetAccPortTable.setStatus("current")
_F3PbbEthernetAccPortEntry_Object = MibTableRow
f3PbbEthernetAccPortEntry = _F3PbbEthernetAccPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 1, 1)
)
if mibBuilder.loadTexts:
    f3PbbEthernetAccPortEntry.setStatus("current")
_F3PbbEthernetAccPortITagLoopbackMask_Type = Integer32
_F3PbbEthernetAccPortITagLoopbackMask_Object = MibTableColumn
f3PbbEthernetAccPortITagLoopbackMask = _F3PbbEthernetAccPortITagLoopbackMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 1, 1, 1),
    _F3PbbEthernetAccPortITagLoopbackMask_Type()
)
f3PbbEthernetAccPortITagLoopbackMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbEthernetAccPortITagLoopbackMask.setStatus("current")
_F3PbbEthernetAccPortITagLoopback1_Type = DisplayString
_F3PbbEthernetAccPortITagLoopback1_Object = MibTableColumn
f3PbbEthernetAccPortITagLoopback1 = _F3PbbEthernetAccPortITagLoopback1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 1, 1, 2),
    _F3PbbEthernetAccPortITagLoopback1_Type()
)
f3PbbEthernetAccPortITagLoopback1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbEthernetAccPortITagLoopback1.setStatus("current")
_F3PbbEthernetAccPortITagLoopback2_Type = DisplayString
_F3PbbEthernetAccPortITagLoopback2_Object = MibTableColumn
f3PbbEthernetAccPortITagLoopback2 = _F3PbbEthernetAccPortITagLoopback2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 1, 1, 3),
    _F3PbbEthernetAccPortITagLoopback2_Type()
)
f3PbbEthernetAccPortITagLoopback2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbEthernetAccPortITagLoopback2.setStatus("current")
_F3PbbEthernetAccPortITagLoopback3_Type = DisplayString
_F3PbbEthernetAccPortITagLoopback3_Object = MibTableColumn
f3PbbEthernetAccPortITagLoopback3 = _F3PbbEthernetAccPortITagLoopback3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 1, 1, 4),
    _F3PbbEthernetAccPortITagLoopback3_Type()
)
f3PbbEthernetAccPortITagLoopback3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbEthernetAccPortITagLoopback3.setStatus("current")
_F3PbbEthernetNetPortTable_Object = MibTable
f3PbbEthernetNetPortTable = _F3PbbEthernetNetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2)
)
if mibBuilder.loadTexts:
    f3PbbEthernetNetPortTable.setStatus("current")
_F3PbbEthernetNetPortEntry_Object = MibTableRow
f3PbbEthernetNetPortEntry = _F3PbbEthernetNetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2, 1)
)
if mibBuilder.loadTexts:
    f3PbbEthernetNetPortEntry.setStatus("current")
_F3PbbEthernetNetPortBackboneMacAddress_Type = MacAddress
_F3PbbEthernetNetPortBackboneMacAddress_Object = MibTableColumn
f3PbbEthernetNetPortBackboneMacAddress = _F3PbbEthernetNetPortBackboneMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2, 1, 1),
    _F3PbbEthernetNetPortBackboneMacAddress_Type()
)
f3PbbEthernetNetPortBackboneMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbEthernetNetPortBackboneMacAddress.setStatus("current")
_F3PbbEthernetNetPortITagLoopbackMask_Type = Integer32
_F3PbbEthernetNetPortITagLoopbackMask_Object = MibTableColumn
f3PbbEthernetNetPortITagLoopbackMask = _F3PbbEthernetNetPortITagLoopbackMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2, 1, 2),
    _F3PbbEthernetNetPortITagLoopbackMask_Type()
)
f3PbbEthernetNetPortITagLoopbackMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbEthernetNetPortITagLoopbackMask.setStatus("current")
_F3PbbEthernetNetPortITagLoopback1_Type = DisplayString
_F3PbbEthernetNetPortITagLoopback1_Object = MibTableColumn
f3PbbEthernetNetPortITagLoopback1 = _F3PbbEthernetNetPortITagLoopback1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2, 1, 3),
    _F3PbbEthernetNetPortITagLoopback1_Type()
)
f3PbbEthernetNetPortITagLoopback1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbEthernetNetPortITagLoopback1.setStatus("current")
_F3PbbEthernetNetPortITagLoopback2_Type = DisplayString
_F3PbbEthernetNetPortITagLoopback2_Object = MibTableColumn
f3PbbEthernetNetPortITagLoopback2 = _F3PbbEthernetNetPortITagLoopback2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2, 1, 4),
    _F3PbbEthernetNetPortITagLoopback2_Type()
)
f3PbbEthernetNetPortITagLoopback2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbEthernetNetPortITagLoopback2.setStatus("current")
_F3PbbEthernetNetPortITagLoopback3_Type = DisplayString
_F3PbbEthernetNetPortITagLoopback3_Object = MibTableColumn
f3PbbEthernetNetPortITagLoopback3 = _F3PbbEthernetNetPortITagLoopback3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2, 1, 5),
    _F3PbbEthernetNetPortITagLoopback3_Type()
)
f3PbbEthernetNetPortITagLoopback3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbEthernetNetPortITagLoopback3.setStatus("current")
_F3PbbFlowTable_Object = MibTable
f3PbbFlowTable = _F3PbbFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3)
)
if mibBuilder.loadTexts:
    f3PbbFlowTable.setStatus("current")
_F3PbbFlowEntry_Object = MibTableRow
f3PbbFlowEntry = _F3PbbFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1)
)
if mibBuilder.loadTexts:
    f3PbbFlowEntry.setStatus("current")
_F3PbbFlowITagControl_Type = FlowTagControl
_F3PbbFlowITagControl_Object = MibTableColumn
f3PbbFlowITagControl = _F3PbbFlowITagControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1, 1),
    _F3PbbFlowITagControl_Type()
)
f3PbbFlowITagControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbFlowITagControl.setStatus("current")


class _F3PbbFlowITagISID_Type(Integer32):
    """Custom type f3PbbFlowITagISID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 16777214),
    )


_F3PbbFlowITagISID_Type.__name__ = "Integer32"
_F3PbbFlowITagISID_Object = MibTableColumn
f3PbbFlowITagISID = _F3PbbFlowITagISID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1, 2),
    _F3PbbFlowITagISID_Type()
)
f3PbbFlowITagISID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbFlowITagISID.setStatus("current")


class _F3PbbFlowITagPriority_Type(Integer32):
    """Custom type f3PbbFlowITagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_F3PbbFlowITagPriority_Type.__name__ = "Integer32"
_F3PbbFlowITagPriority_Object = MibTableColumn
f3PbbFlowITagPriority = _F3PbbFlowITagPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1, 3),
    _F3PbbFlowITagPriority_Type()
)
f3PbbFlowITagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbFlowITagPriority.setStatus("current")
_F3PbbFlowBackboneMacDestinationEnabled_Type = TruthValue
_F3PbbFlowBackboneMacDestinationEnabled_Object = MibTableColumn
f3PbbFlowBackboneMacDestinationEnabled = _F3PbbFlowBackboneMacDestinationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1, 4),
    _F3PbbFlowBackboneMacDestinationEnabled_Type()
)
f3PbbFlowBackboneMacDestinationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbFlowBackboneMacDestinationEnabled.setStatus("current")
_F3PbbFlowBackboneMacDestinationAddress_Type = MacAddress
_F3PbbFlowBackboneMacDestinationAddress_Object = MibTableColumn
f3PbbFlowBackboneMacDestinationAddress = _F3PbbFlowBackboneMacDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1, 5),
    _F3PbbFlowBackboneMacDestinationAddress_Type()
)
f3PbbFlowBackboneMacDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbFlowBackboneMacDestinationAddress.setStatus("current")
_F3PbbFlowA2NPbbCapableFlag_Type = TruthValue
_F3PbbFlowA2NPbbCapableFlag_Object = MibTableColumn
f3PbbFlowA2NPbbCapableFlag = _F3PbbFlowA2NPbbCapableFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1, 6),
    _F3PbbFlowA2NPbbCapableFlag_Type()
)
f3PbbFlowA2NPbbCapableFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbFlowA2NPbbCapableFlag.setStatus("current")
_F3PbbIpManagementTunnelTable_Object = MibTable
f3PbbIpManagementTunnelTable = _F3PbbIpManagementTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4)
)
if mibBuilder.loadTexts:
    f3PbbIpManagementTunnelTable.setStatus("current")
_F3PbbIpManagementTunnelEntry_Object = MibTableRow
f3PbbIpManagementTunnelEntry = _F3PbbIpManagementTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4, 1)
)
if mibBuilder.loadTexts:
    f3PbbIpManagementTunnelEntry.setStatus("current")
_F3PbbIpManagementTunnelItagEnabled_Type = TruthValue
_F3PbbIpManagementTunnelItagEnabled_Object = MibTableColumn
f3PbbIpManagementTunnelItagEnabled = _F3PbbIpManagementTunnelItagEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4, 1, 1),
    _F3PbbIpManagementTunnelItagEnabled_Type()
)
f3PbbIpManagementTunnelItagEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbIpManagementTunnelItagEnabled.setStatus("current")


class _F3PbbIpManagementTunnelISID_Type(Integer32):
    """Custom type f3PbbIpManagementTunnelISID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 16777214),
    )


_F3PbbIpManagementTunnelISID_Type.__name__ = "Integer32"
_F3PbbIpManagementTunnelISID_Object = MibTableColumn
f3PbbIpManagementTunnelISID = _F3PbbIpManagementTunnelISID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4, 1, 2),
    _F3PbbIpManagementTunnelISID_Type()
)
f3PbbIpManagementTunnelISID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbIpManagementTunnelISID.setStatus("current")


class _F3PbbIpManagementTunnelIPriority_Type(Integer32):
    """Custom type f3PbbIpManagementTunnelIPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_F3PbbIpManagementTunnelIPriority_Type.__name__ = "Integer32"
_F3PbbIpManagementTunnelIPriority_Object = MibTableColumn
f3PbbIpManagementTunnelIPriority = _F3PbbIpManagementTunnelIPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4, 1, 3),
    _F3PbbIpManagementTunnelIPriority_Type()
)
f3PbbIpManagementTunnelIPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbIpManagementTunnelIPriority.setStatus("current")
_F3PbbIpManagementTunnelBackboneMacDestinationEnabled_Type = TruthValue
_F3PbbIpManagementTunnelBackboneMacDestinationEnabled_Object = MibTableColumn
f3PbbIpManagementTunnelBackboneMacDestinationEnabled = _F3PbbIpManagementTunnelBackboneMacDestinationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4, 1, 4),
    _F3PbbIpManagementTunnelBackboneMacDestinationEnabled_Type()
)
f3PbbIpManagementTunnelBackboneMacDestinationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbIpManagementTunnelBackboneMacDestinationEnabled.setStatus("current")
_F3PbbIpManagementTunnelBackboneMacDestinationAddress_Type = MacAddress
_F3PbbIpManagementTunnelBackboneMacDestinationAddress_Object = MibTableColumn
f3PbbIpManagementTunnelBackboneMacDestinationAddress = _F3PbbIpManagementTunnelBackboneMacDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4, 1, 5),
    _F3PbbIpManagementTunnelBackboneMacDestinationAddress_Type()
)
f3PbbIpManagementTunnelBackboneMacDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PbbIpManagementTunnelBackboneMacDestinationAddress.setStatus("current")
_F3PBBPerformanceObjects_ObjectIdentity = ObjectIdentity
f3PBBPerformanceObjects = _F3PBBPerformanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2)
)
_F3PbbEthernetNetPortStatsTable_Object = MibTable
f3PbbEthernetNetPortStatsTable = _F3PbbEthernetNetPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 1)
)
if mibBuilder.loadTexts:
    f3PbbEthernetNetPortStatsTable.setStatus("current")
_F3PbbEthernetNetPortStatsEntry_Object = MibTableRow
f3PbbEthernetNetPortStatsEntry = _F3PbbEthernetNetPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 1, 1)
)
if mibBuilder.loadTexts:
    f3PbbEthernetNetPortStatsEntry.setStatus("current")
_F3PbbEthernetNetPortStatsPbbUniBdaDiscard_Type = PerfCounter64
_F3PbbEthernetNetPortStatsPbbUniBdaDiscard_Object = MibTableColumn
f3PbbEthernetNetPortStatsPbbUniBdaDiscard = _F3PbbEthernetNetPortStatsPbbUniBdaDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 1, 1, 1),
    _F3PbbEthernetNetPortStatsPbbUniBdaDiscard_Type()
)
f3PbbEthernetNetPortStatsPbbUniBdaDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PbbEthernetNetPortStatsPbbUniBdaDiscard.setStatus("current")
_F3PbbEthernetNetPortStatsPbbGroupBdaDiscard_Type = PerfCounter64
_F3PbbEthernetNetPortStatsPbbGroupBdaDiscard_Object = MibTableColumn
f3PbbEthernetNetPortStatsPbbGroupBdaDiscard = _F3PbbEthernetNetPortStatsPbbGroupBdaDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 1, 1, 2),
    _F3PbbEthernetNetPortStatsPbbGroupBdaDiscard_Type()
)
f3PbbEthernetNetPortStatsPbbGroupBdaDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PbbEthernetNetPortStatsPbbGroupBdaDiscard.setStatus("current")
_F3PbbEthernetNetPortHistoryStatsTable_Object = MibTable
f3PbbEthernetNetPortHistoryStatsTable = _F3PbbEthernetNetPortHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 2)
)
if mibBuilder.loadTexts:
    f3PbbEthernetNetPortHistoryStatsTable.setStatus("current")
_F3PbbEthernetNetPortHistoryStatsEntry_Object = MibTableRow
f3PbbEthernetNetPortHistoryStatsEntry = _F3PbbEthernetNetPortHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 2, 1)
)
if mibBuilder.loadTexts:
    f3PbbEthernetNetPortHistoryStatsEntry.setStatus("current")
_F3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard_Type = PerfCounter64
_F3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard_Object = MibTableColumn
f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard = _F3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 2, 1, 1),
    _F3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard_Type()
)
f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard.setStatus("current")
_F3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard_Type = PerfCounter64
_F3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard_Object = MibTableColumn
f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard = _F3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 2, 1, 2),
    _F3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard_Type()
)
f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard.setStatus("current")
_F3PBBConformance_ObjectIdentity = ObjectIdentity
f3PBBConformance = _F3PBBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 3)
)
_F3PBBCompliances_ObjectIdentity = ObjectIdentity
f3PBBCompliances = _F3PBBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 3, 1)
)
_F3PBBGroups_ObjectIdentity = ObjectIdentity
f3PBBGroups = _F3PBBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 3, 2)
)
cmEthernetAccPortEntry.registerAugmentions(
    ("F3-PBB-MIB",
     "f3PbbEthernetAccPortEntry")
)
f3PbbEthernetAccPortEntry.setIndexNames(*cmEthernetAccPortEntry.getIndexNames())
cmEthernetNetPortEntry.registerAugmentions(
    ("F3-PBB-MIB",
     "f3PbbEthernetNetPortEntry")
)
f3PbbEthernetNetPortEntry.setIndexNames(*cmEthernetNetPortEntry.getIndexNames())
cmFlowEntry.registerAugmentions(
    ("F3-PBB-MIB",
     "f3PbbFlowEntry")
)
f3PbbFlowEntry.setIndexNames(*cmFlowEntry.getIndexNames())
ipManagementTunnelEntry.registerAugmentions(
    ("F3-PBB-MIB",
     "f3PbbIpManagementTunnelEntry")
)
f3PbbIpManagementTunnelEntry.setIndexNames(*ipManagementTunnelEntry.getIndexNames())
cmEthernetNetPortStatsEntry.registerAugmentions(
    ("F3-PBB-MIB",
     "f3PbbEthernetNetPortStatsEntry")
)
f3PbbEthernetNetPortStatsEntry.setIndexNames(*cmEthernetNetPortStatsEntry.getIndexNames())
cmEthernetNetPortHistoryEntry.registerAugmentions(
    ("F3-PBB-MIB",
     "f3PbbEthernetNetPortHistoryStatsEntry")
)
f3PbbEthernetNetPortHistoryStatsEntry.setIndexNames(*cmEthernetNetPortHistoryEntry.getIndexNames())

# Managed Objects groups

f3PbbConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 3, 2, 1)
)
f3PbbConfigGroup.setObjects(
      *(("F3-PBB-MIB", "f3PbbEthernetAccPortITagLoopbackMask"),
        ("F3-PBB-MIB", "f3PbbEthernetAccPortITagLoopback1"),
        ("F3-PBB-MIB", "f3PbbEthernetAccPortITagLoopback2"),
        ("F3-PBB-MIB", "f3PbbEthernetAccPortITagLoopback3"),
        ("F3-PBB-MIB", "f3PbbEthernetNetPortBackboneMacAddress"),
        ("F3-PBB-MIB", "f3PbbEthernetNetPortITagLoopbackMask"),
        ("F3-PBB-MIB", "f3PbbEthernetNetPortITagLoopback1"),
        ("F3-PBB-MIB", "f3PbbEthernetNetPortITagLoopback2"),
        ("F3-PBB-MIB", "f3PbbEthernetNetPortITagLoopback3"),
        ("F3-PBB-MIB", "f3PbbFlowITagControl"),
        ("F3-PBB-MIB", "f3PbbFlowITagISID"),
        ("F3-PBB-MIB", "f3PbbFlowITagPriority"),
        ("F3-PBB-MIB", "f3PbbFlowBackboneMacDestinationEnabled"),
        ("F3-PBB-MIB", "f3PbbFlowBackboneMacDestinationAddress"),
        ("F3-PBB-MIB", "f3PbbFlowA2NPbbCapableFlag"),
        ("F3-PBB-MIB", "f3PbbIpManagementTunnelItagEnabled"),
        ("F3-PBB-MIB", "f3PbbIpManagementTunnelISID"),
        ("F3-PBB-MIB", "f3PbbIpManagementTunnelIPriority"),
        ("F3-PBB-MIB", "f3PbbIpManagementTunnelBackboneMacDestinationEnabled"),
        ("F3-PBB-MIB", "f3PbbIpManagementTunnelBackboneMacDestinationAddress"))
)
if mibBuilder.loadTexts:
    f3PbbConfigGroup.setStatus("current")

f3PbbStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 3, 2, 2)
)
f3PbbStatsGroup.setObjects(
      *(("F3-PBB-MIB", "f3PbbEthernetNetPortStatsPbbUniBdaDiscard"),
        ("F3-PBB-MIB", "f3PbbEthernetNetPortStatsPbbGroupBdaDiscard"),
        ("F3-PBB-MIB", "f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard"),
        ("F3-PBB-MIB", "f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard"))
)
if mibBuilder.loadTexts:
    f3PbbStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f3PBBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 3, 1, 1)
)
f3PBBCompliance.setObjects(
      *(("F3-PBB-MIB", "f3PbbConfigGroup"),
        ("F3-PBB-MIB", "f3PbbStatsGroup"))
)
if mibBuilder.loadTexts:
    f3PBBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-PBB-MIB",
    **{"f3PBBMIB": f3PBBMIB,
       "f3PBBConfigObjects": f3PBBConfigObjects,
       "f3PbbEthernetAccPortTable": f3PbbEthernetAccPortTable,
       "f3PbbEthernetAccPortEntry": f3PbbEthernetAccPortEntry,
       "f3PbbEthernetAccPortITagLoopbackMask": f3PbbEthernetAccPortITagLoopbackMask,
       "f3PbbEthernetAccPortITagLoopback1": f3PbbEthernetAccPortITagLoopback1,
       "f3PbbEthernetAccPortITagLoopback2": f3PbbEthernetAccPortITagLoopback2,
       "f3PbbEthernetAccPortITagLoopback3": f3PbbEthernetAccPortITagLoopback3,
       "f3PbbEthernetNetPortTable": f3PbbEthernetNetPortTable,
       "f3PbbEthernetNetPortEntry": f3PbbEthernetNetPortEntry,
       "f3PbbEthernetNetPortBackboneMacAddress": f3PbbEthernetNetPortBackboneMacAddress,
       "f3PbbEthernetNetPortITagLoopbackMask": f3PbbEthernetNetPortITagLoopbackMask,
       "f3PbbEthernetNetPortITagLoopback1": f3PbbEthernetNetPortITagLoopback1,
       "f3PbbEthernetNetPortITagLoopback2": f3PbbEthernetNetPortITagLoopback2,
       "f3PbbEthernetNetPortITagLoopback3": f3PbbEthernetNetPortITagLoopback3,
       "f3PbbFlowTable": f3PbbFlowTable,
       "f3PbbFlowEntry": f3PbbFlowEntry,
       "f3PbbFlowITagControl": f3PbbFlowITagControl,
       "f3PbbFlowITagISID": f3PbbFlowITagISID,
       "f3PbbFlowITagPriority": f3PbbFlowITagPriority,
       "f3PbbFlowBackboneMacDestinationEnabled": f3PbbFlowBackboneMacDestinationEnabled,
       "f3PbbFlowBackboneMacDestinationAddress": f3PbbFlowBackboneMacDestinationAddress,
       "f3PbbFlowA2NPbbCapableFlag": f3PbbFlowA2NPbbCapableFlag,
       "f3PbbIpManagementTunnelTable": f3PbbIpManagementTunnelTable,
       "f3PbbIpManagementTunnelEntry": f3PbbIpManagementTunnelEntry,
       "f3PbbIpManagementTunnelItagEnabled": f3PbbIpManagementTunnelItagEnabled,
       "f3PbbIpManagementTunnelISID": f3PbbIpManagementTunnelISID,
       "f3PbbIpManagementTunnelIPriority": f3PbbIpManagementTunnelIPriority,
       "f3PbbIpManagementTunnelBackboneMacDestinationEnabled": f3PbbIpManagementTunnelBackboneMacDestinationEnabled,
       "f3PbbIpManagementTunnelBackboneMacDestinationAddress": f3PbbIpManagementTunnelBackboneMacDestinationAddress,
       "f3PBBPerformanceObjects": f3PBBPerformanceObjects,
       "f3PbbEthernetNetPortStatsTable": f3PbbEthernetNetPortStatsTable,
       "f3PbbEthernetNetPortStatsEntry": f3PbbEthernetNetPortStatsEntry,
       "f3PbbEthernetNetPortStatsPbbUniBdaDiscard": f3PbbEthernetNetPortStatsPbbUniBdaDiscard,
       "f3PbbEthernetNetPortStatsPbbGroupBdaDiscard": f3PbbEthernetNetPortStatsPbbGroupBdaDiscard,
       "f3PbbEthernetNetPortHistoryStatsTable": f3PbbEthernetNetPortHistoryStatsTable,
       "f3PbbEthernetNetPortHistoryStatsEntry": f3PbbEthernetNetPortHistoryStatsEntry,
       "f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard": f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard,
       "f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard": f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard,
       "f3PBBConformance": f3PBBConformance,
       "f3PBBCompliances": f3PBBCompliances,
       "f3PBBCompliance": f3PBBCompliance,
       "f3PBBGroups": f3PBBGroups,
       "f3PbbConfigGroup": f3PbbConfigGroup,
       "f3PbbStatsGroup": f3PbbStatsGroup}
)
