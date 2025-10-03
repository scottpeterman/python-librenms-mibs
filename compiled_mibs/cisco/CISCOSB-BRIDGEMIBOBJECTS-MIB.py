# SNMP MIB module (CISCOSB-BRIDGEMIBOBJECTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-BRIDGEMIBOBJECTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:28:19 2025
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

(BridgeId,
 MacAddress,
 Timeout,
 dot1dBasePort,
 dot1dStpPort) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "MacAddress",
    "Timeout",
    "dot1dBasePort",
    "dot1dStpPort")

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

rlpBridgeMIBObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57)
)
if mibBuilder.loadTexts:
    rlpBridgeMIBObjects.setRevisions(
        ("2007-01-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanList1(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class VlanList2(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class VlanList3(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class VlanList4(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



# MIB Managed Objects in the order of their OIDs

_Rldot1dPriority_ObjectIdentity = ObjectIdentity
rldot1dPriority = _Rldot1dPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 1)
)
_Rldot1dPriorityMibVersion_Type = Integer32
_Rldot1dPriorityMibVersion_Object = MibScalar
rldot1dPriorityMibVersion = _Rldot1dPriorityMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 1, 1),
    _Rldot1dPriorityMibVersion_Type()
)
rldot1dPriorityMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dPriorityMibVersion.setStatus("current")
_Rldot1dPriorityPortGroupTable_Object = MibTable
rldot1dPriorityPortGroupTable = _Rldot1dPriorityPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 1, 2)
)
if mibBuilder.loadTexts:
    rldot1dPriorityPortGroupTable.setStatus("current")
_Rldot1dPriorityPortGroupEntry_Object = MibTableRow
rldot1dPriorityPortGroupEntry = _Rldot1dPriorityPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 1, 2, 1)
)
rldot1dPriorityPortGroupEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rldot1dPriorityPortGroupEntry.setStatus("current")
_Rldot1dPriorityPortGroupNumber_Type = Integer32
_Rldot1dPriorityPortGroupNumber_Object = MibTableColumn
rldot1dPriorityPortGroupNumber = _Rldot1dPriorityPortGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 1, 2, 1, 1),
    _Rldot1dPriorityPortGroupNumber_Type()
)
rldot1dPriorityPortGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dPriorityPortGroupNumber.setStatus("current")
_Rldot1dStp_ObjectIdentity = ObjectIdentity
rldot1dStp = _Rldot1dStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2)
)
_Rldot1dStpMibVersion_Type = Integer32
_Rldot1dStpMibVersion_Object = MibScalar
rldot1dStpMibVersion = _Rldot1dStpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 1),
    _Rldot1dStpMibVersion_Type()
)
rldot1dStpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpMibVersion.setStatus("current")


class _Rldot1dStpType_Type(Integer32):
    """Custom type rldot1dStpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("perDevice", 1),
          ("mstp", 4))
    )


_Rldot1dStpType_Type.__name__ = "Integer32"
_Rldot1dStpType_Object = MibScalar
rldot1dStpType = _Rldot1dStpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 2),
    _Rldot1dStpType_Type()
)
rldot1dStpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpType.setStatus("current")


class _Rldot1dStpEnable_Type(TruthValue):
    """Custom type rldot1dStpEnable based on TruthValue"""
    defaultValue = 1


_Rldot1dStpEnable_Type.__name__ = "TruthValue"
_Rldot1dStpEnable_Object = MibScalar
rldot1dStpEnable = _Rldot1dStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 3),
    _Rldot1dStpEnable_Type()
)
rldot1dStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpEnable.setStatus("current")


class _Rldot1dStpPortMustBelongToVlan_Type(TruthValue):
    """Custom type rldot1dStpPortMustBelongToVlan based on TruthValue"""
    defaultValue = 1


_Rldot1dStpPortMustBelongToVlan_Type.__name__ = "TruthValue"
_Rldot1dStpPortMustBelongToVlan_Object = MibScalar
rldot1dStpPortMustBelongToVlan = _Rldot1dStpPortMustBelongToVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 4),
    _Rldot1dStpPortMustBelongToVlan_Type()
)
rldot1dStpPortMustBelongToVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpPortMustBelongToVlan.setStatus("current")


class _Rldot1dStpExtendedPortNumberFormat_Type(TruthValue):
    """Custom type rldot1dStpExtendedPortNumberFormat based on TruthValue"""
    defaultValue = 2


_Rldot1dStpExtendedPortNumberFormat_Type.__name__ = "TruthValue"
_Rldot1dStpExtendedPortNumberFormat_Object = MibScalar
rldot1dStpExtendedPortNumberFormat = _Rldot1dStpExtendedPortNumberFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 5),
    _Rldot1dStpExtendedPortNumberFormat_Type()
)
rldot1dStpExtendedPortNumberFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpExtendedPortNumberFormat.setStatus("current")
_Rldot1dStpVlanTable_Object = MibTable
rldot1dStpVlanTable = _Rldot1dStpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 6)
)
if mibBuilder.loadTexts:
    rldot1dStpVlanTable.setStatus("current")
_Rldot1dStpVlanEntry_Object = MibTableRow
rldot1dStpVlanEntry = _Rldot1dStpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 6, 1)
)
rldot1dStpVlanEntry.setIndexNames(
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1dStpVlan"),
)
if mibBuilder.loadTexts:
    rldot1dStpVlanEntry.setStatus("current")
_Rldot1dStpVlan_Type = Integer32
_Rldot1dStpVlan_Object = MibTableColumn
rldot1dStpVlan = _Rldot1dStpVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 6, 1, 1),
    _Rldot1dStpVlan_Type()
)
rldot1dStpVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpVlan.setStatus("current")


class _Rldot1dStpVlanEnable_Type(TruthValue):
    """Custom type rldot1dStpVlanEnable based on TruthValue"""
    defaultValue = 1


_Rldot1dStpVlanEnable_Type.__name__ = "TruthValue"
_Rldot1dStpVlanEnable_Object = MibTableColumn
rldot1dStpVlanEnable = _Rldot1dStpVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 6, 1, 2),
    _Rldot1dStpVlanEnable_Type()
)
rldot1dStpVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpVlanEnable.setStatus("current")
_Rldot1dStpTimeSinceTopologyChange_Type = TimeTicks
_Rldot1dStpTimeSinceTopologyChange_Object = MibTableColumn
rldot1dStpTimeSinceTopologyChange = _Rldot1dStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 6, 1, 3),
    _Rldot1dStpTimeSinceTopologyChange_Type()
)
rldot1dStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpTimeSinceTopologyChange.setStatus("current")
_Rldot1dStpTopChanges_Type = Counter32
_Rldot1dStpTopChanges_Object = MibTableColumn
rldot1dStpTopChanges = _Rldot1dStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 6, 1, 4),
    _Rldot1dStpTopChanges_Type()
)
rldot1dStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpTopChanges.setStatus("current")
_Rldot1dStpDesignatedRoot_Type = BridgeId
_Rldot1dStpDesignatedRoot_Object = MibTableColumn
rldot1dStpDesignatedRoot = _Rldot1dStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 6, 1, 5),
    _Rldot1dStpDesignatedRoot_Type()
)
rldot1dStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpDesignatedRoot.setStatus("current")
_Rldot1dStpRootCost_Type = Integer32
_Rldot1dStpRootCost_Object = MibTableColumn
rldot1dStpRootCost = _Rldot1dStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 6, 1, 6),
    _Rldot1dStpRootCost_Type()
)
rldot1dStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpRootCost.setStatus("current")
_Rldot1dStpRootPort_Type = Integer32
_Rldot1dStpRootPort_Object = MibTableColumn
rldot1dStpRootPort = _Rldot1dStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 6, 1, 7),
    _Rldot1dStpRootPort_Type()
)
rldot1dStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpRootPort.setStatus("current")
_Rldot1dStpMaxAge_Type = Timeout
_Rldot1dStpMaxAge_Object = MibTableColumn
rldot1dStpMaxAge = _Rldot1dStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 6, 1, 8),
    _Rldot1dStpMaxAge_Type()
)
rldot1dStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpMaxAge.setStatus("current")
_Rldot1dStpHelloTime_Type = Timeout
_Rldot1dStpHelloTime_Object = MibTableColumn
rldot1dStpHelloTime = _Rldot1dStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 6, 1, 9),
    _Rldot1dStpHelloTime_Type()
)
rldot1dStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpHelloTime.setStatus("current")
_Rldot1dStpHoldTime_Type = Integer32
_Rldot1dStpHoldTime_Object = MibTableColumn
rldot1dStpHoldTime = _Rldot1dStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 6, 1, 10),
    _Rldot1dStpHoldTime_Type()
)
rldot1dStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpHoldTime.setStatus("current")
_Rldot1dStpForwardDelay_Type = Timeout
_Rldot1dStpForwardDelay_Object = MibTableColumn
rldot1dStpForwardDelay = _Rldot1dStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 6, 1, 11),
    _Rldot1dStpForwardDelay_Type()
)
rldot1dStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpForwardDelay.setStatus("current")
_Rldot1dStpVlanPortTable_Object = MibTable
rldot1dStpVlanPortTable = _Rldot1dStpVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 7)
)
if mibBuilder.loadTexts:
    rldot1dStpVlanPortTable.setStatus("current")
_Rldot1dStpVlanPortEntry_Object = MibTableRow
rldot1dStpVlanPortEntry = _Rldot1dStpVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 7, 1)
)
rldot1dStpVlanPortEntry.setIndexNames(
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1dStpVlanPortVlan"),
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1dStpVlanPortPort"),
)
if mibBuilder.loadTexts:
    rldot1dStpVlanPortEntry.setStatus("current")


class _Rldot1dStpVlanPortVlan_Type(Integer32):
    """Custom type rldot1dStpVlanPortVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Rldot1dStpVlanPortVlan_Type.__name__ = "Integer32"
_Rldot1dStpVlanPortVlan_Object = MibTableColumn
rldot1dStpVlanPortVlan = _Rldot1dStpVlanPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 7, 1, 1),
    _Rldot1dStpVlanPortVlan_Type()
)
rldot1dStpVlanPortVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortVlan.setStatus("current")


class _Rldot1dStpVlanPortPort_Type(Integer32):
    """Custom type rldot1dStpVlanPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Rldot1dStpVlanPortPort_Type.__name__ = "Integer32"
_Rldot1dStpVlanPortPort_Object = MibTableColumn
rldot1dStpVlanPortPort = _Rldot1dStpVlanPortPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 7, 1, 2),
    _Rldot1dStpVlanPortPort_Type()
)
rldot1dStpVlanPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortPort.setStatus("current")


class _Rldot1dStpVlanPortPriority_Type(Integer32):
    """Custom type rldot1dStpVlanPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Rldot1dStpVlanPortPriority_Type.__name__ = "Integer32"
_Rldot1dStpVlanPortPriority_Object = MibTableColumn
rldot1dStpVlanPortPriority = _Rldot1dStpVlanPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 7, 1, 3),
    _Rldot1dStpVlanPortPriority_Type()
)
rldot1dStpVlanPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortPriority.setStatus("current")


class _Rldot1dStpVlanPortState_Type(Integer32):
    """Custom type rldot1dStpVlanPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6))
    )


_Rldot1dStpVlanPortState_Type.__name__ = "Integer32"
_Rldot1dStpVlanPortState_Object = MibTableColumn
rldot1dStpVlanPortState = _Rldot1dStpVlanPortState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 7, 1, 4),
    _Rldot1dStpVlanPortState_Type()
)
rldot1dStpVlanPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortState.setStatus("current")


class _Rldot1dStpVlanPortEnable_Type(Integer32):
    """Custom type rldot1dStpVlanPortEnable based on Integer32"""
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


_Rldot1dStpVlanPortEnable_Type.__name__ = "Integer32"
_Rldot1dStpVlanPortEnable_Object = MibTableColumn
rldot1dStpVlanPortEnable = _Rldot1dStpVlanPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 7, 1, 5),
    _Rldot1dStpVlanPortEnable_Type()
)
rldot1dStpVlanPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortEnable.setStatus("current")


class _Rldot1dStpVlanPortPathCost_Type(Integer32):
    """Custom type rldot1dStpVlanPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Rldot1dStpVlanPortPathCost_Type.__name__ = "Integer32"
_Rldot1dStpVlanPortPathCost_Object = MibTableColumn
rldot1dStpVlanPortPathCost = _Rldot1dStpVlanPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 7, 1, 6),
    _Rldot1dStpVlanPortPathCost_Type()
)
rldot1dStpVlanPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortPathCost.setStatus("current")
_Rldot1dStpVlanPortDesignatedRoot_Type = BridgeId
_Rldot1dStpVlanPortDesignatedRoot_Object = MibTableColumn
rldot1dStpVlanPortDesignatedRoot = _Rldot1dStpVlanPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 7, 1, 7),
    _Rldot1dStpVlanPortDesignatedRoot_Type()
)
rldot1dStpVlanPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortDesignatedRoot.setStatus("current")
_Rldot1dStpVlanPortDesignatedCost_Type = Integer32
_Rldot1dStpVlanPortDesignatedCost_Object = MibTableColumn
rldot1dStpVlanPortDesignatedCost = _Rldot1dStpVlanPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 7, 1, 8),
    _Rldot1dStpVlanPortDesignatedCost_Type()
)
rldot1dStpVlanPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortDesignatedCost.setStatus("current")
_Rldot1dStpVlanPortDesignatedBridge_Type = BridgeId
_Rldot1dStpVlanPortDesignatedBridge_Object = MibTableColumn
rldot1dStpVlanPortDesignatedBridge = _Rldot1dStpVlanPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 7, 1, 9),
    _Rldot1dStpVlanPortDesignatedBridge_Type()
)
rldot1dStpVlanPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortDesignatedBridge.setStatus("current")


class _Rldot1dStpVlanPortDesignatedPort_Type(OctetString):
    """Custom type rldot1dStpVlanPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_Rldot1dStpVlanPortDesignatedPort_Type.__name__ = "OctetString"
_Rldot1dStpVlanPortDesignatedPort_Object = MibTableColumn
rldot1dStpVlanPortDesignatedPort = _Rldot1dStpVlanPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 7, 1, 10),
    _Rldot1dStpVlanPortDesignatedPort_Type()
)
rldot1dStpVlanPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortDesignatedPort.setStatus("current")
_Rldot1dStpVlanPortForwardTransitions_Type = Counter32
_Rldot1dStpVlanPortForwardTransitions_Object = MibTableColumn
rldot1dStpVlanPortForwardTransitions = _Rldot1dStpVlanPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 7, 1, 11),
    _Rldot1dStpVlanPortForwardTransitions_Type()
)
rldot1dStpVlanPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortForwardTransitions.setStatus("current")
_Rldot1dStpTrapVariable_ObjectIdentity = ObjectIdentity
rldot1dStpTrapVariable = _Rldot1dStpTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 8)
)
_Rldot1dStpTrapVrblifIndex_Type = InterfaceIndex
_Rldot1dStpTrapVrblifIndex_Object = MibScalar
rldot1dStpTrapVrblifIndex = _Rldot1dStpTrapVrblifIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 8, 1),
    _Rldot1dStpTrapVrblifIndex_Type()
)
rldot1dStpTrapVrblifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpTrapVrblifIndex.setStatus("current")
_Rldot1dStpTrapVrblVID_Type = Integer32
_Rldot1dStpTrapVrblVID_Object = MibScalar
rldot1dStpTrapVrblVID = _Rldot1dStpTrapVrblVID_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 8, 2),
    _Rldot1dStpTrapVrblVID_Type()
)
rldot1dStpTrapVrblVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpTrapVrblVID.setStatus("current")


class _Rldot1dStpTypeAfterReset_Type(Integer32):
    """Custom type rldot1dStpTypeAfterReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("perDevice", 1),
          ("mstp", 4))
    )


_Rldot1dStpTypeAfterReset_Type.__name__ = "Integer32"
_Rldot1dStpTypeAfterReset_Object = MibScalar
rldot1dStpTypeAfterReset = _Rldot1dStpTypeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 9),
    _Rldot1dStpTypeAfterReset_Type()
)
rldot1dStpTypeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpTypeAfterReset.setStatus("current")


class _Rldot1dStpMonitorTime_Type(Integer32):
    """Custom type rldot1dStpMonitorTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Rldot1dStpMonitorTime_Type.__name__ = "Integer32"
_Rldot1dStpMonitorTime_Object = MibScalar
rldot1dStpMonitorTime = _Rldot1dStpMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 10),
    _Rldot1dStpMonitorTime_Type()
)
rldot1dStpMonitorTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpMonitorTime.setStatus("current")


class _Rldot1dStpBpduCount_Type(Integer32):
    """Custom type rldot1dStpBpduCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Rldot1dStpBpduCount_Type.__name__ = "Integer32"
_Rldot1dStpBpduCount_Object = MibScalar
rldot1dStpBpduCount = _Rldot1dStpBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 11),
    _Rldot1dStpBpduCount_Type()
)
rldot1dStpBpduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpBpduCount.setStatus("current")
_Rldot1dStpLastChanged_Type = TimeTicks
_Rldot1dStpLastChanged_Object = MibScalar
rldot1dStpLastChanged = _Rldot1dStpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 12),
    _Rldot1dStpLastChanged_Type()
)
rldot1dStpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpLastChanged.setStatus("current")
_Rldot1dStpPortTable_Object = MibTable
rldot1dStpPortTable = _Rldot1dStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 13)
)
if mibBuilder.loadTexts:
    rldot1dStpPortTable.setStatus("current")
_Rldot1dStpPortEntry_Object = MibTableRow
rldot1dStpPortEntry = _Rldot1dStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 13, 1)
)
rldot1dStpPortEntry.setIndexNames(
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1dStpPortPort"),
)
if mibBuilder.loadTexts:
    rldot1dStpPortEntry.setStatus("current")


class _Rldot1dStpPortPort_Type(Integer32):
    """Custom type rldot1dStpPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Rldot1dStpPortPort_Type.__name__ = "Integer32"
_Rldot1dStpPortPort_Object = MibTableColumn
rldot1dStpPortPort = _Rldot1dStpPortPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 13, 1, 1),
    _Rldot1dStpPortPort_Type()
)
rldot1dStpPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpPortPort.setStatus("current")


class _Rldot1dStpPortDampEnable_Type(TruthValue):
    """Custom type rldot1dStpPortDampEnable based on TruthValue"""
    defaultValue = 2


_Rldot1dStpPortDampEnable_Type.__name__ = "TruthValue"
_Rldot1dStpPortDampEnable_Object = MibTableColumn
rldot1dStpPortDampEnable = _Rldot1dStpPortDampEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 13, 1, 2),
    _Rldot1dStpPortDampEnable_Type()
)
rldot1dStpPortDampEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpPortDampEnable.setStatus("current")


class _Rldot1dStpPortDampStable_Type(TruthValue):
    """Custom type rldot1dStpPortDampStable based on TruthValue"""
    defaultValue = 1


_Rldot1dStpPortDampStable_Type.__name__ = "TruthValue"
_Rldot1dStpPortDampStable_Object = MibTableColumn
rldot1dStpPortDampStable = _Rldot1dStpPortDampStable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 13, 1, 3),
    _Rldot1dStpPortDampStable_Type()
)
rldot1dStpPortDampStable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpPortDampStable.setStatus("current")


class _Rldot1dStpPortFilterBpdu_Type(Integer32):
    """Custom type rldot1dStpPortFilterBpdu based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("none", 2))
    )


_Rldot1dStpPortFilterBpdu_Type.__name__ = "Integer32"
_Rldot1dStpPortFilterBpdu_Object = MibTableColumn
rldot1dStpPortFilterBpdu = _Rldot1dStpPortFilterBpdu_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 13, 1, 4),
    _Rldot1dStpPortFilterBpdu_Type()
)
rldot1dStpPortFilterBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpPortFilterBpdu.setStatus("current")
_Rldot1dStpPortBpduSent_Type = Counter32
_Rldot1dStpPortBpduSent_Object = MibTableColumn
rldot1dStpPortBpduSent = _Rldot1dStpPortBpduSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 13, 1, 5),
    _Rldot1dStpPortBpduSent_Type()
)
rldot1dStpPortBpduSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpPortBpduSent.setStatus("current")
_Rldot1dStpPortBpduReceived_Type = Counter32
_Rldot1dStpPortBpduReceived_Object = MibTableColumn
rldot1dStpPortBpduReceived = _Rldot1dStpPortBpduReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 13, 1, 6),
    _Rldot1dStpPortBpduReceived_Type()
)
rldot1dStpPortBpduReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpPortBpduReceived.setStatus("current")


class _Rldot1dStpPortRole_Type(Integer32):
    """Custom type rldot1dStpPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("disabled", 1),
          ("alternate", 2),
          ("backup", 3),
          ("root", 4),
          ("designated", 5))
    )


_Rldot1dStpPortRole_Type.__name__ = "Integer32"
_Rldot1dStpPortRole_Object = MibTableColumn
rldot1dStpPortRole = _Rldot1dStpPortRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 13, 1, 7),
    _Rldot1dStpPortRole_Type()
)
rldot1dStpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpPortRole.setStatus("current")


class _Rldot1dStpBpduType_Type(Integer32):
    """Custom type rldot1dStpBpduType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("stp", 0),
          ("rstp", 1))
    )


_Rldot1dStpBpduType_Type.__name__ = "Integer32"
_Rldot1dStpBpduType_Object = MibTableColumn
rldot1dStpBpduType = _Rldot1dStpBpduType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 13, 1, 8),
    _Rldot1dStpBpduType_Type()
)
rldot1dStpBpduType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpBpduType.setStatus("current")


class _Rldot1dStpPortRestrictedRole_Type(TruthValue):
    """Custom type rldot1dStpPortRestrictedRole based on TruthValue"""
    defaultValue = 2


_Rldot1dStpPortRestrictedRole_Type.__name__ = "TruthValue"
_Rldot1dStpPortRestrictedRole_Object = MibTableColumn
rldot1dStpPortRestrictedRole = _Rldot1dStpPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 13, 1, 9),
    _Rldot1dStpPortRestrictedRole_Type()
)
rldot1dStpPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpPortRestrictedRole.setStatus("current")


class _Rldot1dStpPortAutoEdgePort_Type(TruthValue):
    """Custom type rldot1dStpPortAutoEdgePort based on TruthValue"""
    defaultValue = 2


_Rldot1dStpPortAutoEdgePort_Type.__name__ = "TruthValue"
_Rldot1dStpPortAutoEdgePort_Object = MibTableColumn
rldot1dStpPortAutoEdgePort = _Rldot1dStpPortAutoEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 13, 1, 10),
    _Rldot1dStpPortAutoEdgePort_Type()
)
rldot1dStpPortAutoEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpPortAutoEdgePort.setStatus("current")
_Rldot1dStpPortLoopback_Type = TruthValue
_Rldot1dStpPortLoopback_Object = MibTableColumn
rldot1dStpPortLoopback = _Rldot1dStpPortLoopback_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 13, 1, 11),
    _Rldot1dStpPortLoopback_Type()
)
rldot1dStpPortLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpPortLoopback.setStatus("current")


class _Rldot1dStpPortBpduOperStatus_Type(Integer32):
    """Custom type rldot1dStpPortBpduOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filter", 0),
          ("flood", 1),
          ("bridge", 2),
          ("stp", 3))
    )


_Rldot1dStpPortBpduOperStatus_Type.__name__ = "Integer32"
_Rldot1dStpPortBpduOperStatus_Object = MibTableColumn
rldot1dStpPortBpduOperStatus = _Rldot1dStpPortBpduOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 13, 1, 12),
    _Rldot1dStpPortBpduOperStatus_Type()
)
rldot1dStpPortBpduOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpPortBpduOperStatus.setStatus("current")
_Rldot1dStpPortTcnGuardEnable_Type = TruthValue
_Rldot1dStpPortTcnGuardEnable_Object = MibTableColumn
rldot1dStpPortTcnGuardEnable = _Rldot1dStpPortTcnGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 13, 1, 13),
    _Rldot1dStpPortTcnGuardEnable_Type()
)
rldot1dStpPortTcnGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpPortTcnGuardEnable.setStatus("current")


class _Rldot1dStpPortsEnable_Type(TruthValue):
    """Custom type rldot1dStpPortsEnable based on TruthValue"""
    defaultValue = 1


_Rldot1dStpPortsEnable_Type.__name__ = "TruthValue"
_Rldot1dStpPortsEnable_Object = MibScalar
rldot1dStpPortsEnable = _Rldot1dStpPortsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 14),
    _Rldot1dStpPortsEnable_Type()
)
rldot1dStpPortsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpPortsEnable.setStatus("current")
_Rldot1dStpTaggedFlooding_Type = TruthValue
_Rldot1dStpTaggedFlooding_Object = MibScalar
rldot1dStpTaggedFlooding = _Rldot1dStpTaggedFlooding_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 15),
    _Rldot1dStpTaggedFlooding_Type()
)
rldot1dStpTaggedFlooding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpTaggedFlooding.setStatus("current")
_Rldot1dStpPortBelongToVlanDefault_Type = TruthValue
_Rldot1dStpPortBelongToVlanDefault_Object = MibScalar
rldot1dStpPortBelongToVlanDefault = _Rldot1dStpPortBelongToVlanDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 16),
    _Rldot1dStpPortBelongToVlanDefault_Type()
)
rldot1dStpPortBelongToVlanDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpPortBelongToVlanDefault.setStatus("current")
_Rldot1dStpEnableByDefault_Type = TruthValue
_Rldot1dStpEnableByDefault_Object = MibScalar
rldot1dStpEnableByDefault = _Rldot1dStpEnableByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 17),
    _Rldot1dStpEnableByDefault_Type()
)
rldot1dStpEnableByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpEnableByDefault.setStatus("current")
_Rldot1dStpPortToDefault_Type = Integer32
_Rldot1dStpPortToDefault_Object = MibScalar
rldot1dStpPortToDefault = _Rldot1dStpPortToDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 18),
    _Rldot1dStpPortToDefault_Type()
)
rldot1dStpPortToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpPortToDefault.setStatus("current")


class _Rldot1dStpSupportedType_Type(Integer32):
    """Custom type rldot1dStpSupportedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("perDevice", 1),
          ("perVlan", 2),
          ("mstp", 3))
    )


_Rldot1dStpSupportedType_Type.__name__ = "Integer32"
_Rldot1dStpSupportedType_Object = MibScalar
rldot1dStpSupportedType = _Rldot1dStpSupportedType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 19),
    _Rldot1dStpSupportedType_Type()
)
rldot1dStpSupportedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpSupportedType.setStatus("current")
_Rldot1dStpEdgeportSupportInStp_Type = TruthValue
_Rldot1dStpEdgeportSupportInStp_Object = MibScalar
rldot1dStpEdgeportSupportInStp = _Rldot1dStpEdgeportSupportInStp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 20),
    _Rldot1dStpEdgeportSupportInStp_Type()
)
rldot1dStpEdgeportSupportInStp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpEdgeportSupportInStp.setStatus("current")
_Rldot1dStpFilterBpdu_Type = TruthValue
_Rldot1dStpFilterBpdu_Object = MibScalar
rldot1dStpFilterBpdu = _Rldot1dStpFilterBpdu_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 21),
    _Rldot1dStpFilterBpdu_Type()
)
rldot1dStpFilterBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpFilterBpdu.setStatus("current")


class _Rldot1dStpFloodBpduMethod_Type(Integer32):
    """Custom type rldot1dStpFloodBpduMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("classic", 0),
          ("bridging", 1))
    )


_Rldot1dStpFloodBpduMethod_Type.__name__ = "Integer32"
_Rldot1dStpFloodBpduMethod_Object = MibScalar
rldot1dStpFloodBpduMethod = _Rldot1dStpFloodBpduMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 22),
    _Rldot1dStpFloodBpduMethod_Type()
)
rldot1dStpFloodBpduMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpFloodBpduMethod.setStatus("current")
_Rldot1dStpSeparatedBridges_ObjectIdentity = ObjectIdentity
rldot1dStpSeparatedBridges = _Rldot1dStpSeparatedBridges_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 23)
)
_Rldot1dStpSeparatedBridgesTable_Object = MibTable
rldot1dStpSeparatedBridgesTable = _Rldot1dStpSeparatedBridgesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 23, 1)
)
if mibBuilder.loadTexts:
    rldot1dStpSeparatedBridgesTable.setStatus("current")
_Rldot1dStpSeparatedBridgesEntry_Object = MibTableRow
rldot1dStpSeparatedBridgesEntry = _Rldot1dStpSeparatedBridgesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 23, 1, 1)
)
rldot1dStpSeparatedBridgesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rldot1dStpSeparatedBridgesEntry.setStatus("current")


class _Rldot1dStpSeparatedBridgesPortEnable_Type(TruthValue):
    """Custom type rldot1dStpSeparatedBridgesPortEnable based on TruthValue"""
    defaultValue = 2


_Rldot1dStpSeparatedBridgesPortEnable_Type.__name__ = "TruthValue"
_Rldot1dStpSeparatedBridgesPortEnable_Object = MibTableColumn
rldot1dStpSeparatedBridgesPortEnable = _Rldot1dStpSeparatedBridgesPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 23, 1, 1, 1),
    _Rldot1dStpSeparatedBridgesPortEnable_Type()
)
rldot1dStpSeparatedBridgesPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpSeparatedBridgesPortEnable.setStatus("current")


class _Rldot1dStpSeparatedBridgesEnable_Type(TruthValue):
    """Custom type rldot1dStpSeparatedBridgesEnable based on TruthValue"""
    defaultValue = 2


_Rldot1dStpSeparatedBridgesEnable_Type.__name__ = "TruthValue"
_Rldot1dStpSeparatedBridgesEnable_Object = MibScalar
rldot1dStpSeparatedBridgesEnable = _Rldot1dStpSeparatedBridgesEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 23, 2),
    _Rldot1dStpSeparatedBridgesEnable_Type()
)
rldot1dStpSeparatedBridgesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpSeparatedBridgesEnable.setStatus("current")


class _Rldot1dStpSeparatedBridgesAutoConfig_Type(TruthValue):
    """Custom type rldot1dStpSeparatedBridgesAutoConfig based on TruthValue"""
    defaultValue = 2


_Rldot1dStpSeparatedBridgesAutoConfig_Type.__name__ = "TruthValue"
_Rldot1dStpSeparatedBridgesAutoConfig_Object = MibScalar
rldot1dStpSeparatedBridgesAutoConfig = _Rldot1dStpSeparatedBridgesAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 23, 3),
    _Rldot1dStpSeparatedBridgesAutoConfig_Type()
)
rldot1dStpSeparatedBridgesAutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpSeparatedBridgesAutoConfig.setStatus("current")
_Rldot1dStpPortBpduGuardTable_Object = MibTable
rldot1dStpPortBpduGuardTable = _Rldot1dStpPortBpduGuardTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 24)
)
if mibBuilder.loadTexts:
    rldot1dStpPortBpduGuardTable.setStatus("current")
_Rldot1dStpPortBpduGuardEntry_Object = MibTableRow
rldot1dStpPortBpduGuardEntry = _Rldot1dStpPortBpduGuardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 24, 1)
)
rldot1dStpPortBpduGuardEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rldot1dStpPortBpduGuardEntry.setStatus("current")


class _Rldot1dStpPortBpduGuardEnable_Type(TruthValue):
    """Custom type rldot1dStpPortBpduGuardEnable based on TruthValue"""
    defaultValue = 2


_Rldot1dStpPortBpduGuardEnable_Type.__name__ = "TruthValue"
_Rldot1dStpPortBpduGuardEnable_Object = MibTableColumn
rldot1dStpPortBpduGuardEnable = _Rldot1dStpPortBpduGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 24, 1, 1),
    _Rldot1dStpPortBpduGuardEnable_Type()
)
rldot1dStpPortBpduGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpPortBpduGuardEnable.setStatus("current")


class _Rldot1dStpLoopbackGuardEnable_Type(TruthValue):
    """Custom type rldot1dStpLoopbackGuardEnable based on TruthValue"""
    defaultValue = 2


_Rldot1dStpLoopbackGuardEnable_Type.__name__ = "TruthValue"
_Rldot1dStpLoopbackGuardEnable_Object = MibScalar
rldot1dStpLoopbackGuardEnable = _Rldot1dStpLoopbackGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 25),
    _Rldot1dStpLoopbackGuardEnable_Type()
)
rldot1dStpLoopbackGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpLoopbackGuardEnable.setStatus("current")
_Rldot1dStpDisabledPortStateTable_Object = MibTable
rldot1dStpDisabledPortStateTable = _Rldot1dStpDisabledPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 26)
)
if mibBuilder.loadTexts:
    rldot1dStpDisabledPortStateTable.setStatus("current")
_Rldot1dStpDisabledPortStateEntry_Object = MibTableRow
rldot1dStpDisabledPortStateEntry = _Rldot1dStpDisabledPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 26, 1)
)
rldot1dStpDisabledPortStateEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dStpPort"),
)
if mibBuilder.loadTexts:
    rldot1dStpDisabledPortStateEntry.setStatus("current")


class _Rldot1dStpDisabledPortState_Type(Integer32):
    """Custom type rldot1dStpDisabledPortState based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5))
    )


_Rldot1dStpDisabledPortState_Type.__name__ = "Integer32"
_Rldot1dStpDisabledPortState_Object = MibTableColumn
rldot1dStpDisabledPortState = _Rldot1dStpDisabledPortState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 26, 1, 1),
    _Rldot1dStpDisabledPortState_Type()
)
rldot1dStpDisabledPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpDisabledPortState.setStatus("current")
_Rldot1dStpClearPortCounters_Type = InterfaceIndexOrZero
_Rldot1dStpClearPortCounters_Object = MibScalar
rldot1dStpClearPortCounters = _Rldot1dStpClearPortCounters_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 2, 27),
    _Rldot1dStpClearPortCounters_Type()
)
rldot1dStpClearPortCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpClearPortCounters.setStatus("current")
_Rldot1dExtBase_ObjectIdentity = ObjectIdentity
rldot1dExtBase = _Rldot1dExtBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 3)
)
_Rldot1dExtBaseMibVersion_Type = Integer32
_Rldot1dExtBaseMibVersion_Object = MibScalar
rldot1dExtBaseMibVersion = _Rldot1dExtBaseMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 3, 1),
    _Rldot1dExtBaseMibVersion_Type()
)
rldot1dExtBaseMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dExtBaseMibVersion.setStatus("current")


class _Rldot1dDeviceCapabilities_Type(OctetString):
    """Custom type rldot1dDeviceCapabilities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_Rldot1dDeviceCapabilities_Type.__name__ = "OctetString"
_Rldot1dDeviceCapabilities_Object = MibScalar
rldot1dDeviceCapabilities = _Rldot1dDeviceCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 3, 2),
    _Rldot1dDeviceCapabilities_Type()
)
rldot1dDeviceCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dDeviceCapabilities.setStatus("current")
_Rldot1wRStp_ObjectIdentity = ObjectIdentity
rldot1wRStp = _Rldot1wRStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 4)
)
_Rldot1wRStpVlanEdgePortTable_Object = MibTable
rldot1wRStpVlanEdgePortTable = _Rldot1wRStpVlanEdgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 4, 1)
)
if mibBuilder.loadTexts:
    rldot1wRStpVlanEdgePortTable.setStatus("current")
_Rldot1wRStpVlanEdgePortEntry_Object = MibTableRow
rldot1wRStpVlanEdgePortEntry = _Rldot1wRStpVlanEdgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 4, 1, 1)
)
rldot1wRStpVlanEdgePortEntry.setIndexNames(
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1wRStpVlanEdgePortVlan"),
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1wRStpVlanEdgePortPort"),
)
if mibBuilder.loadTexts:
    rldot1wRStpVlanEdgePortEntry.setStatus("current")


class _Rldot1wRStpVlanEdgePortVlan_Type(Integer32):
    """Custom type rldot1wRStpVlanEdgePortVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Rldot1wRStpVlanEdgePortVlan_Type.__name__ = "Integer32"
_Rldot1wRStpVlanEdgePortVlan_Object = MibTableColumn
rldot1wRStpVlanEdgePortVlan = _Rldot1wRStpVlanEdgePortVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 4, 1, 1, 1),
    _Rldot1wRStpVlanEdgePortVlan_Type()
)
rldot1wRStpVlanEdgePortVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1wRStpVlanEdgePortVlan.setStatus("current")
_Rldot1wRStpVlanEdgePortPort_Type = Integer32
_Rldot1wRStpVlanEdgePortPort_Object = MibTableColumn
rldot1wRStpVlanEdgePortPort = _Rldot1wRStpVlanEdgePortPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 4, 1, 1, 2),
    _Rldot1wRStpVlanEdgePortPort_Type()
)
rldot1wRStpVlanEdgePortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1wRStpVlanEdgePortPort.setStatus("current")


class _Rldot1wRStpEdgePortStatus_Type(TruthValue):
    """Custom type rldot1wRStpEdgePortStatus based on TruthValue"""
    defaultValue = 2


_Rldot1wRStpEdgePortStatus_Type.__name__ = "TruthValue"
_Rldot1wRStpEdgePortStatus_Object = MibTableColumn
rldot1wRStpEdgePortStatus = _Rldot1wRStpEdgePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 4, 1, 1, 3),
    _Rldot1wRStpEdgePortStatus_Type()
)
rldot1wRStpEdgePortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1wRStpEdgePortStatus.setStatus("current")
_Rldot1wRStpForceVersionTable_Object = MibTable
rldot1wRStpForceVersionTable = _Rldot1wRStpForceVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 4, 2)
)
if mibBuilder.loadTexts:
    rldot1wRStpForceVersionTable.setStatus("current")
_Rldot1wRStpForceVersionEntry_Object = MibTableRow
rldot1wRStpForceVersionEntry = _Rldot1wRStpForceVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 4, 2, 1)
)
rldot1wRStpForceVersionEntry.setIndexNames(
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1wRStpForceVersionVlan"),
)
if mibBuilder.loadTexts:
    rldot1wRStpForceVersionEntry.setStatus("current")


class _Rldot1wRStpForceVersionVlan_Type(Integer32):
    """Custom type rldot1wRStpForceVersionVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Rldot1wRStpForceVersionVlan_Type.__name__ = "Integer32"
_Rldot1wRStpForceVersionVlan_Object = MibTableColumn
rldot1wRStpForceVersionVlan = _Rldot1wRStpForceVersionVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 4, 2, 1, 1),
    _Rldot1wRStpForceVersionVlan_Type()
)
rldot1wRStpForceVersionVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1wRStpForceVersionVlan.setStatus("current")


class _Rldot1wRStpForceVersionState_Type(Integer32):
    """Custom type rldot1wRStpForceVersionState based on Integer32"""
    defaultValue = 2


_Rldot1wRStpForceVersionState_Type.__name__ = "Integer32"
_Rldot1wRStpForceVersionState_Object = MibTableColumn
rldot1wRStpForceVersionState = _Rldot1wRStpForceVersionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 4, 2, 1, 2),
    _Rldot1wRStpForceVersionState_Type()
)
rldot1wRStpForceVersionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1wRStpForceVersionState.setStatus("current")
_Rldot1pPriorityMap_ObjectIdentity = ObjectIdentity
rldot1pPriorityMap = _Rldot1pPriorityMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 5)
)


class _Rldot1pPriorityMapState_Type(Integer32):
    """Custom type rldot1pPriorityMapState based on Integer32"""
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


_Rldot1pPriorityMapState_Type.__name__ = "Integer32"
_Rldot1pPriorityMapState_Object = MibScalar
rldot1pPriorityMapState = _Rldot1pPriorityMapState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 5, 1),
    _Rldot1pPriorityMapState_Type()
)
rldot1pPriorityMapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1pPriorityMapState.setStatus("current")
_Rldot1pPriorityMapTable_Object = MibTable
rldot1pPriorityMapTable = _Rldot1pPriorityMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 5, 2)
)
if mibBuilder.loadTexts:
    rldot1pPriorityMapTable.setStatus("current")
_Rldot1pPriorityMapEntry_Object = MibTableRow
rldot1pPriorityMapEntry = _Rldot1pPriorityMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 5, 2, 1)
)
rldot1pPriorityMapEntry.setIndexNames(
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1pPriorityMapName"),
)
if mibBuilder.loadTexts:
    rldot1pPriorityMapEntry.setStatus("current")


class _Rldot1pPriorityMapName_Type(DisplayString):
    """Custom type rldot1pPriorityMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_Rldot1pPriorityMapName_Type.__name__ = "DisplayString"
_Rldot1pPriorityMapName_Object = MibTableColumn
rldot1pPriorityMapName = _Rldot1pPriorityMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 5, 2, 1, 1),
    _Rldot1pPriorityMapName_Type()
)
rldot1pPriorityMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1pPriorityMapName.setStatus("current")


class _Rldot1pPriorityMapPriority_Type(OctetString):
    """Custom type rldot1pPriorityMapPriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Rldot1pPriorityMapPriority_Type.__name__ = "OctetString"
_Rldot1pPriorityMapPriority_Object = MibTableColumn
rldot1pPriorityMapPriority = _Rldot1pPriorityMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 5, 2, 1, 2),
    _Rldot1pPriorityMapPriority_Type()
)
rldot1pPriorityMapPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rldot1pPriorityMapPriority.setStatus("current")
_Rldot1pPriorityMapPort_Type = PortList
_Rldot1pPriorityMapPort_Object = MibTableColumn
rldot1pPriorityMapPort = _Rldot1pPriorityMapPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 5, 2, 1, 3),
    _Rldot1pPriorityMapPort_Type()
)
rldot1pPriorityMapPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rldot1pPriorityMapPort.setStatus("current")
_Rldot1pPriorityMapPortList_Type = PortList
_Rldot1pPriorityMapPortList_Object = MibTableColumn
rldot1pPriorityMapPortList = _Rldot1pPriorityMapPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 5, 2, 1, 4),
    _Rldot1pPriorityMapPortList_Type()
)
rldot1pPriorityMapPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1pPriorityMapPortList.setStatus("current")
_Rldot1pPriorityMapStatus_Type = RowStatus
_Rldot1pPriorityMapStatus_Object = MibTableColumn
rldot1pPriorityMapStatus = _Rldot1pPriorityMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 5, 2, 1, 5),
    _Rldot1pPriorityMapStatus_Type()
)
rldot1pPriorityMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rldot1pPriorityMapStatus.setStatus("current")
_Rldot1sMstp_ObjectIdentity = ObjectIdentity
rldot1sMstp = _Rldot1sMstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6)
)
_Rldot1sMstpInstanceTable_Object = MibTable
rldot1sMstpInstanceTable = _Rldot1sMstpInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 1)
)
if mibBuilder.loadTexts:
    rldot1sMstpInstanceTable.setStatus("current")
_Rldot1sMstpInstanceEntry_Object = MibTableRow
rldot1sMstpInstanceEntry = _Rldot1sMstpInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 1, 1)
)
rldot1sMstpInstanceEntry.setIndexNames(
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1sMstpInstanceId"),
)
if mibBuilder.loadTexts:
    rldot1sMstpInstanceEntry.setStatus("current")


class _Rldot1sMstpInstanceId_Type(Integer32):
    """Custom type rldot1sMstpInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Rldot1sMstpInstanceId_Type.__name__ = "Integer32"
_Rldot1sMstpInstanceId_Object = MibTableColumn
rldot1sMstpInstanceId = _Rldot1sMstpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 1, 1, 1),
    _Rldot1sMstpInstanceId_Type()
)
rldot1sMstpInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceId.setStatus("current")
_Rldot1sMstpInstanceEnable_Type = TruthValue
_Rldot1sMstpInstanceEnable_Object = MibTableColumn
rldot1sMstpInstanceEnable = _Rldot1sMstpInstanceEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 1, 1, 2),
    _Rldot1sMstpInstanceEnable_Type()
)
rldot1sMstpInstanceEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceEnable.setStatus("current")
_Rldot1sMstpInstanceTimeSinceTopologyChange_Type = TimeTicks
_Rldot1sMstpInstanceTimeSinceTopologyChange_Object = MibTableColumn
rldot1sMstpInstanceTimeSinceTopologyChange = _Rldot1sMstpInstanceTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 1, 1, 3),
    _Rldot1sMstpInstanceTimeSinceTopologyChange_Type()
)
rldot1sMstpInstanceTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceTimeSinceTopologyChange.setStatus("current")
_Rldot1sMstpInstanceTopChanges_Type = Counter32
_Rldot1sMstpInstanceTopChanges_Object = MibTableColumn
rldot1sMstpInstanceTopChanges = _Rldot1sMstpInstanceTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 1, 1, 4),
    _Rldot1sMstpInstanceTopChanges_Type()
)
rldot1sMstpInstanceTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceTopChanges.setStatus("current")
_Rldot1sMstpInstanceDesignatedRoot_Type = BridgeId
_Rldot1sMstpInstanceDesignatedRoot_Object = MibTableColumn
rldot1sMstpInstanceDesignatedRoot = _Rldot1sMstpInstanceDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 1, 1, 5),
    _Rldot1sMstpInstanceDesignatedRoot_Type()
)
rldot1sMstpInstanceDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceDesignatedRoot.setStatus("current")
_Rldot1sMstpInstanceRootCost_Type = Integer32
_Rldot1sMstpInstanceRootCost_Object = MibTableColumn
rldot1sMstpInstanceRootCost = _Rldot1sMstpInstanceRootCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 1, 1, 6),
    _Rldot1sMstpInstanceRootCost_Type()
)
rldot1sMstpInstanceRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceRootCost.setStatus("current")
_Rldot1sMstpInstanceRootPort_Type = Integer32
_Rldot1sMstpInstanceRootPort_Object = MibTableColumn
rldot1sMstpInstanceRootPort = _Rldot1sMstpInstanceRootPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 1, 1, 7),
    _Rldot1sMstpInstanceRootPort_Type()
)
rldot1sMstpInstanceRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceRootPort.setStatus("current")
_Rldot1sMstpInstanceMaxAge_Type = Timeout
_Rldot1sMstpInstanceMaxAge_Object = MibTableColumn
rldot1sMstpInstanceMaxAge = _Rldot1sMstpInstanceMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 1, 1, 8),
    _Rldot1sMstpInstanceMaxAge_Type()
)
rldot1sMstpInstanceMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceMaxAge.setStatus("current")
_Rldot1sMstpInstanceHelloTime_Type = Timeout
_Rldot1sMstpInstanceHelloTime_Object = MibTableColumn
rldot1sMstpInstanceHelloTime = _Rldot1sMstpInstanceHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 1, 1, 9),
    _Rldot1sMstpInstanceHelloTime_Type()
)
rldot1sMstpInstanceHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceHelloTime.setStatus("current")
_Rldot1sMstpInstanceHoldTime_Type = Integer32
_Rldot1sMstpInstanceHoldTime_Object = MibTableColumn
rldot1sMstpInstanceHoldTime = _Rldot1sMstpInstanceHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 1, 1, 10),
    _Rldot1sMstpInstanceHoldTime_Type()
)
rldot1sMstpInstanceHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceHoldTime.setStatus("current")
_Rldot1sMstpInstanceForwardDelay_Type = Timeout
_Rldot1sMstpInstanceForwardDelay_Object = MibTableColumn
rldot1sMstpInstanceForwardDelay = _Rldot1sMstpInstanceForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 1, 1, 11),
    _Rldot1sMstpInstanceForwardDelay_Type()
)
rldot1sMstpInstanceForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceForwardDelay.setStatus("current")


class _Rldot1sMstpInstancePriority_Type(Integer32):
    """Custom type rldot1sMstpInstancePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Rldot1sMstpInstancePriority_Type.__name__ = "Integer32"
_Rldot1sMstpInstancePriority_Object = MibTableColumn
rldot1sMstpInstancePriority = _Rldot1sMstpInstancePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 1, 1, 12),
    _Rldot1sMstpInstancePriority_Type()
)
rldot1sMstpInstancePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePriority.setStatus("current")
_Rldot1sMstpInstanceRemainingHopes_Type = Integer32
_Rldot1sMstpInstanceRemainingHopes_Object = MibTableColumn
rldot1sMstpInstanceRemainingHopes = _Rldot1sMstpInstanceRemainingHopes_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 1, 1, 13),
    _Rldot1sMstpInstanceRemainingHopes_Type()
)
rldot1sMstpInstanceRemainingHopes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceRemainingHopes.setStatus("current")
_Rldot1sMstpInstanceSwId_Type = Integer32
_Rldot1sMstpInstanceSwId_Object = MibTableColumn
rldot1sMstpInstanceSwId = _Rldot1sMstpInstanceSwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 1, 1, 14),
    _Rldot1sMstpInstanceSwId_Type()
)
rldot1sMstpInstanceSwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceSwId.setStatus("current")
_Rldot1sMstpInstancePortTable_Object = MibTable
rldot1sMstpInstancePortTable = _Rldot1sMstpInstancePortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 2)
)
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortTable.setStatus("current")
_Rldot1sMstpInstancePortEntry_Object = MibTableRow
rldot1sMstpInstancePortEntry = _Rldot1sMstpInstancePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 2, 1)
)
rldot1sMstpInstancePortEntry.setIndexNames(
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1sMstpInstancePortMstiId"),
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1sMstpInstancePortPort"),
)
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortEntry.setStatus("current")


class _Rldot1sMstpInstancePortMstiId_Type(Integer32):
    """Custom type rldot1sMstpInstancePortMstiId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Rldot1sMstpInstancePortMstiId_Type.__name__ = "Integer32"
_Rldot1sMstpInstancePortMstiId_Object = MibTableColumn
rldot1sMstpInstancePortMstiId = _Rldot1sMstpInstancePortMstiId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 2, 1, 1),
    _Rldot1sMstpInstancePortMstiId_Type()
)
rldot1sMstpInstancePortMstiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortMstiId.setStatus("current")


class _Rldot1sMstpInstancePortPort_Type(Integer32):
    """Custom type rldot1sMstpInstancePortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Rldot1sMstpInstancePortPort_Type.__name__ = "Integer32"
_Rldot1sMstpInstancePortPort_Object = MibTableColumn
rldot1sMstpInstancePortPort = _Rldot1sMstpInstancePortPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 2, 1, 2),
    _Rldot1sMstpInstancePortPort_Type()
)
rldot1sMstpInstancePortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortPort.setStatus("current")


class _Rldot1sMstpInstancePortPriority_Type(Integer32):
    """Custom type rldot1sMstpInstancePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Rldot1sMstpInstancePortPriority_Type.__name__ = "Integer32"
_Rldot1sMstpInstancePortPriority_Object = MibTableColumn
rldot1sMstpInstancePortPriority = _Rldot1sMstpInstancePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 2, 1, 3),
    _Rldot1sMstpInstancePortPriority_Type()
)
rldot1sMstpInstancePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortPriority.setStatus("current")


class _Rldot1sMstpInstancePortState_Type(Integer32):
    """Custom type rldot1sMstpInstancePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6))
    )


_Rldot1sMstpInstancePortState_Type.__name__ = "Integer32"
_Rldot1sMstpInstancePortState_Object = MibTableColumn
rldot1sMstpInstancePortState = _Rldot1sMstpInstancePortState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 2, 1, 4),
    _Rldot1sMstpInstancePortState_Type()
)
rldot1sMstpInstancePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortState.setStatus("current")


class _Rldot1sMstpInstancePortEnable_Type(Integer32):
    """Custom type rldot1sMstpInstancePortEnable based on Integer32"""
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


_Rldot1sMstpInstancePortEnable_Type.__name__ = "Integer32"
_Rldot1sMstpInstancePortEnable_Object = MibTableColumn
rldot1sMstpInstancePortEnable = _Rldot1sMstpInstancePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 2, 1, 5),
    _Rldot1sMstpInstancePortEnable_Type()
)
rldot1sMstpInstancePortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortEnable.setStatus("current")


class _Rldot1sMstpInstancePortPathCost_Type(Integer32):
    """Custom type rldot1sMstpInstancePortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_Rldot1sMstpInstancePortPathCost_Type.__name__ = "Integer32"
_Rldot1sMstpInstancePortPathCost_Object = MibTableColumn
rldot1sMstpInstancePortPathCost = _Rldot1sMstpInstancePortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 2, 1, 6),
    _Rldot1sMstpInstancePortPathCost_Type()
)
rldot1sMstpInstancePortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortPathCost.setStatus("current")
_Rldot1sMstpInstancePortDesignatedRoot_Type = BridgeId
_Rldot1sMstpInstancePortDesignatedRoot_Object = MibTableColumn
rldot1sMstpInstancePortDesignatedRoot = _Rldot1sMstpInstancePortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 2, 1, 7),
    _Rldot1sMstpInstancePortDesignatedRoot_Type()
)
rldot1sMstpInstancePortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortDesignatedRoot.setStatus("current")
_Rldot1sMstpInstancePortDesignatedCost_Type = Integer32
_Rldot1sMstpInstancePortDesignatedCost_Object = MibTableColumn
rldot1sMstpInstancePortDesignatedCost = _Rldot1sMstpInstancePortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 2, 1, 8),
    _Rldot1sMstpInstancePortDesignatedCost_Type()
)
rldot1sMstpInstancePortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortDesignatedCost.setStatus("current")
_Rldot1sMstpInstancePortDesignatedBridge_Type = BridgeId
_Rldot1sMstpInstancePortDesignatedBridge_Object = MibTableColumn
rldot1sMstpInstancePortDesignatedBridge = _Rldot1sMstpInstancePortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 2, 1, 9),
    _Rldot1sMstpInstancePortDesignatedBridge_Type()
)
rldot1sMstpInstancePortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortDesignatedBridge.setStatus("current")


class _Rldot1sMstpInstancePortDesignatedPort_Type(OctetString):
    """Custom type rldot1sMstpInstancePortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_Rldot1sMstpInstancePortDesignatedPort_Type.__name__ = "OctetString"
_Rldot1sMstpInstancePortDesignatedPort_Object = MibTableColumn
rldot1sMstpInstancePortDesignatedPort = _Rldot1sMstpInstancePortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 2, 1, 10),
    _Rldot1sMstpInstancePortDesignatedPort_Type()
)
rldot1sMstpInstancePortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortDesignatedPort.setStatus("current")
_Rldot1sMstpInstancePortForwardTransitions_Type = Counter32
_Rldot1sMstpInstancePortForwardTransitions_Object = MibTableColumn
rldot1sMstpInstancePortForwardTransitions = _Rldot1sMstpInstancePortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 2, 1, 11),
    _Rldot1sMstpInstancePortForwardTransitions_Type()
)
rldot1sMstpInstancePortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortForwardTransitions.setStatus("current")


class _Rldot1sMStpInstancePortAdminPathCost_Type(Integer32):
    """Custom type rldot1sMStpInstancePortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Rldot1sMStpInstancePortAdminPathCost_Type.__name__ = "Integer32"
_Rldot1sMStpInstancePortAdminPathCost_Object = MibTableColumn
rldot1sMStpInstancePortAdminPathCost = _Rldot1sMStpInstancePortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 2, 1, 12),
    _Rldot1sMStpInstancePortAdminPathCost_Type()
)
rldot1sMStpInstancePortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1sMStpInstancePortAdminPathCost.setStatus("current")


class _Rldot1sMStpInstancePortRole_Type(Integer32):
    """Custom type rldot1sMStpInstancePortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("disabled", 1),
          ("alternate", 2),
          ("backup", 3),
          ("root", 4),
          ("designated", 5),
          ("master", 6))
    )


_Rldot1sMStpInstancePortRole_Type.__name__ = "Integer32"
_Rldot1sMStpInstancePortRole_Object = MibTableColumn
rldot1sMStpInstancePortRole = _Rldot1sMStpInstancePortRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 2, 1, 13),
    _Rldot1sMStpInstancePortRole_Type()
)
rldot1sMStpInstancePortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMStpInstancePortRole.setStatus("current")


class _Rldot1sMstpMaxHopes_Type(Integer32):
    """Custom type rldot1sMstpMaxHopes based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_Rldot1sMstpMaxHopes_Type.__name__ = "Integer32"
_Rldot1sMstpMaxHopes_Object = MibScalar
rldot1sMstpMaxHopes = _Rldot1sMstpMaxHopes_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 3),
    _Rldot1sMstpMaxHopes_Type()
)
rldot1sMstpMaxHopes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1sMstpMaxHopes.setStatus("current")
_Rldot1sMstpConfigurationName_Type = SnmpAdminString
_Rldot1sMstpConfigurationName_Object = MibScalar
rldot1sMstpConfigurationName = _Rldot1sMstpConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 4),
    _Rldot1sMstpConfigurationName_Type()
)
rldot1sMstpConfigurationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpConfigurationName.setStatus("current")


class _Rldot1sMstpRevisionLevel_Type(Integer32):
    """Custom type rldot1sMstpRevisionLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rldot1sMstpRevisionLevel_Type.__name__ = "Integer32"
_Rldot1sMstpRevisionLevel_Object = MibScalar
rldot1sMstpRevisionLevel = _Rldot1sMstpRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 5),
    _Rldot1sMstpRevisionLevel_Type()
)
rldot1sMstpRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpRevisionLevel.setStatus("current")
_Rldot1sMstpVlanTable_Object = MibTable
rldot1sMstpVlanTable = _Rldot1sMstpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 6)
)
if mibBuilder.loadTexts:
    rldot1sMstpVlanTable.setStatus("current")
_Rldot1sMstpVlanEntry_Object = MibTableRow
rldot1sMstpVlanEntry = _Rldot1sMstpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 6, 1)
)
rldot1sMstpVlanEntry.setIndexNames(
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1sMstpVlan"),
)
if mibBuilder.loadTexts:
    rldot1sMstpVlanEntry.setStatus("current")


class _Rldot1sMstpVlan_Type(Integer32):
    """Custom type rldot1sMstpVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Rldot1sMstpVlan_Type.__name__ = "Integer32"
_Rldot1sMstpVlan_Object = MibTableColumn
rldot1sMstpVlan = _Rldot1sMstpVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 6, 1, 1),
    _Rldot1sMstpVlan_Type()
)
rldot1sMstpVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpVlan.setStatus("current")


class _Rldot1sMstpGroup_Type(Integer32):
    """Custom type rldot1sMstpGroup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Rldot1sMstpGroup_Type.__name__ = "Integer32"
_Rldot1sMstpGroup_Object = MibTableColumn
rldot1sMstpGroup = _Rldot1sMstpGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 6, 1, 2),
    _Rldot1sMstpGroup_Type()
)
rldot1sMstpGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpGroup.setStatus("current")


class _Rldot1sMstpPendingGroup_Type(Integer32):
    """Custom type rldot1sMstpPendingGroup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Rldot1sMstpPendingGroup_Type.__name__ = "Integer32"
_Rldot1sMstpPendingGroup_Object = MibTableColumn
rldot1sMstpPendingGroup = _Rldot1sMstpPendingGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 6, 1, 3),
    _Rldot1sMstpPendingGroup_Type()
)
rldot1sMstpPendingGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1sMstpPendingGroup.setStatus("current")
_Rldot1sMstpExtPortTable_Object = MibTable
rldot1sMstpExtPortTable = _Rldot1sMstpExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 7)
)
if mibBuilder.loadTexts:
    rldot1sMstpExtPortTable.setStatus("current")
_Rldot1sMstpExtPortEntry_Object = MibTableRow
rldot1sMstpExtPortEntry = _Rldot1sMstpExtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 7, 1)
)
rldot1sMstpExtPortEntry.setIndexNames(
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1sMstpExtPortPort"),
)
if mibBuilder.loadTexts:
    rldot1sMstpExtPortEntry.setStatus("current")


class _Rldot1sMstpExtPortPort_Type(Integer32):
    """Custom type rldot1sMstpExtPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Rldot1sMstpExtPortPort_Type.__name__ = "Integer32"
_Rldot1sMstpExtPortPort_Object = MibTableColumn
rldot1sMstpExtPortPort = _Rldot1sMstpExtPortPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 7, 1, 1),
    _Rldot1sMstpExtPortPort_Type()
)
rldot1sMstpExtPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpExtPortPort.setStatus("current")


class _Rldot1sMstpExtPortInternalOperPathCost_Type(Integer32):
    """Custom type rldot1sMstpExtPortInternalOperPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_Rldot1sMstpExtPortInternalOperPathCost_Type.__name__ = "Integer32"
_Rldot1sMstpExtPortInternalOperPathCost_Object = MibTableColumn
rldot1sMstpExtPortInternalOperPathCost = _Rldot1sMstpExtPortInternalOperPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 7, 1, 2),
    _Rldot1sMstpExtPortInternalOperPathCost_Type()
)
rldot1sMstpExtPortInternalOperPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpExtPortInternalOperPathCost.setStatus("current")
_Rldot1sMstpExtPortDesignatedRegionalRoot_Type = BridgeId
_Rldot1sMstpExtPortDesignatedRegionalRoot_Object = MibTableColumn
rldot1sMstpExtPortDesignatedRegionalRoot = _Rldot1sMstpExtPortDesignatedRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 7, 1, 3),
    _Rldot1sMstpExtPortDesignatedRegionalRoot_Type()
)
rldot1sMstpExtPortDesignatedRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpExtPortDesignatedRegionalRoot.setStatus("current")
_Rldot1sMstpExtPortDesignatedRegionalCost_Type = Integer32
_Rldot1sMstpExtPortDesignatedRegionalCost_Object = MibTableColumn
rldot1sMstpExtPortDesignatedRegionalCost = _Rldot1sMstpExtPortDesignatedRegionalCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 7, 1, 4),
    _Rldot1sMstpExtPortDesignatedRegionalCost_Type()
)
rldot1sMstpExtPortDesignatedRegionalCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpExtPortDesignatedRegionalCost.setStatus("current")
_Rldot1sMstpExtPortBoundary_Type = TruthValue
_Rldot1sMstpExtPortBoundary_Object = MibTableColumn
rldot1sMstpExtPortBoundary = _Rldot1sMstpExtPortBoundary_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 7, 1, 5),
    _Rldot1sMstpExtPortBoundary_Type()
)
rldot1sMstpExtPortBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpExtPortBoundary.setStatus("current")


class _Rldot1sMstpExtPortInternalAdminPathCost_Type(Integer32):
    """Custom type rldot1sMstpExtPortInternalAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Rldot1sMstpExtPortInternalAdminPathCost_Type.__name__ = "Integer32"
_Rldot1sMstpExtPortInternalAdminPathCost_Object = MibTableColumn
rldot1sMstpExtPortInternalAdminPathCost = _Rldot1sMstpExtPortInternalAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 7, 1, 6),
    _Rldot1sMstpExtPortInternalAdminPathCost_Type()
)
rldot1sMstpExtPortInternalAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1sMstpExtPortInternalAdminPathCost.setStatus("current")


class _Rldot1sMstpDesignatedMaxHopes_Type(Integer32):
    """Custom type rldot1sMstpDesignatedMaxHopes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_Rldot1sMstpDesignatedMaxHopes_Type.__name__ = "Integer32"
_Rldot1sMstpDesignatedMaxHopes_Object = MibScalar
rldot1sMstpDesignatedMaxHopes = _Rldot1sMstpDesignatedMaxHopes_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 8),
    _Rldot1sMstpDesignatedMaxHopes_Type()
)
rldot1sMstpDesignatedMaxHopes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpDesignatedMaxHopes.setStatus("current")
_Rldot1sMstpRegionalRoot_Type = BridgeId
_Rldot1sMstpRegionalRoot_Object = MibScalar
rldot1sMstpRegionalRoot = _Rldot1sMstpRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 9),
    _Rldot1sMstpRegionalRoot_Type()
)
rldot1sMstpRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpRegionalRoot.setStatus("current")
_Rldot1sMstpRegionalRootCost_Type = Integer32
_Rldot1sMstpRegionalRootCost_Object = MibScalar
rldot1sMstpRegionalRootCost = _Rldot1sMstpRegionalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 10),
    _Rldot1sMstpRegionalRootCost_Type()
)
rldot1sMstpRegionalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpRegionalRootCost.setStatus("current")


class _Rldot1sMstpPendingConfigurationName_Type(SnmpAdminString):
    """Custom type rldot1sMstpPendingConfigurationName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Rldot1sMstpPendingConfigurationName_Type.__name__ = "SnmpAdminString"
_Rldot1sMstpPendingConfigurationName_Object = MibScalar
rldot1sMstpPendingConfigurationName = _Rldot1sMstpPendingConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 11),
    _Rldot1sMstpPendingConfigurationName_Type()
)
rldot1sMstpPendingConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1sMstpPendingConfigurationName.setStatus("current")


class _Rldot1sMstpPendingRevisionLevel_Type(Integer32):
    """Custom type rldot1sMstpPendingRevisionLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rldot1sMstpPendingRevisionLevel_Type.__name__ = "Integer32"
_Rldot1sMstpPendingRevisionLevel_Object = MibScalar
rldot1sMstpPendingRevisionLevel = _Rldot1sMstpPendingRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 12),
    _Rldot1sMstpPendingRevisionLevel_Type()
)
rldot1sMstpPendingRevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1sMstpPendingRevisionLevel.setStatus("current")


class _Rldot1sMstpPendingAction_Type(Integer32):
    """Custom type rldot1sMstpPendingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copyPendingActive", 1),
          ("copyActivePending", 2))
    )


_Rldot1sMstpPendingAction_Type.__name__ = "Integer32"
_Rldot1sMstpPendingAction_Object = MibScalar
rldot1sMstpPendingAction = _Rldot1sMstpPendingAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 13),
    _Rldot1sMstpPendingAction_Type()
)
rldot1sMstpPendingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1sMstpPendingAction.setStatus("current")
_Rldot1sMstpRemainingHops_Type = Integer32
_Rldot1sMstpRemainingHops_Object = MibScalar
rldot1sMstpRemainingHops = _Rldot1sMstpRemainingHops_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 14),
    _Rldot1sMstpRemainingHops_Type()
)
rldot1sMstpRemainingHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpRemainingHops.setStatus("current")
_Rldot1sMstpInstanceVlanTable_Object = MibTable
rldot1sMstpInstanceVlanTable = _Rldot1sMstpInstanceVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 15)
)
if mibBuilder.loadTexts:
    rldot1sMstpInstanceVlanTable.setStatus("current")
_Rldot1sMstpInstanceVlanEntry_Object = MibTableRow
rldot1sMstpInstanceVlanEntry = _Rldot1sMstpInstanceVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 15, 1)
)
rldot1sMstpInstanceVlanEntry.setIndexNames(
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1sMstpInstanceVlanId"),
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1sMstpInstanceVlanDbType"),
)
if mibBuilder.loadTexts:
    rldot1sMstpInstanceVlanEntry.setStatus("current")


class _Rldot1sMstpInstanceVlanId_Type(Integer32):
    """Custom type rldot1sMstpInstanceVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Rldot1sMstpInstanceVlanId_Type.__name__ = "Integer32"
_Rldot1sMstpInstanceVlanId_Object = MibTableColumn
rldot1sMstpInstanceVlanId = _Rldot1sMstpInstanceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 15, 1, 1),
    _Rldot1sMstpInstanceVlanId_Type()
)
rldot1sMstpInstanceVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceVlanId.setStatus("current")


class _Rldot1sMstpInstanceVlanDbType_Type(Integer32):
    """Custom type rldot1sMstpInstanceVlanDbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("pending", 2))
    )


_Rldot1sMstpInstanceVlanDbType_Type.__name__ = "Integer32"
_Rldot1sMstpInstanceVlanDbType_Object = MibTableColumn
rldot1sMstpInstanceVlanDbType = _Rldot1sMstpInstanceVlanDbType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 15, 1, 2),
    _Rldot1sMstpInstanceVlanDbType_Type()
)
rldot1sMstpInstanceVlanDbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceVlanDbType.setStatus("current")
_Rldot1sMstpInstanceVlanId1To1024_Type = VlanList1
_Rldot1sMstpInstanceVlanId1To1024_Object = MibTableColumn
rldot1sMstpInstanceVlanId1To1024 = _Rldot1sMstpInstanceVlanId1To1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 15, 1, 3),
    _Rldot1sMstpInstanceVlanId1To1024_Type()
)
rldot1sMstpInstanceVlanId1To1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceVlanId1To1024.setStatus("current")
_Rldot1sMstpInstanceVlanId1025To2048_Type = VlanList2
_Rldot1sMstpInstanceVlanId1025To2048_Object = MibTableColumn
rldot1sMstpInstanceVlanId1025To2048 = _Rldot1sMstpInstanceVlanId1025To2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 15, 1, 4),
    _Rldot1sMstpInstanceVlanId1025To2048_Type()
)
rldot1sMstpInstanceVlanId1025To2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceVlanId1025To2048.setStatus("current")
_Rldot1sMstpInstanceVlanId2049To3072_Type = VlanList3
_Rldot1sMstpInstanceVlanId2049To3072_Object = MibTableColumn
rldot1sMstpInstanceVlanId2049To3072 = _Rldot1sMstpInstanceVlanId2049To3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 15, 1, 5),
    _Rldot1sMstpInstanceVlanId2049To3072_Type()
)
rldot1sMstpInstanceVlanId2049To3072.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceVlanId2049To3072.setStatus("current")
_Rldot1sMstpInstanceVlanId3073To4094_Type = VlanList4
_Rldot1sMstpInstanceVlanId3073To4094_Object = MibTableColumn
rldot1sMstpInstanceVlanId3073To4094 = _Rldot1sMstpInstanceVlanId3073To4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 15, 1, 6),
    _Rldot1sMstpInstanceVlanId3073To4094_Type()
)
rldot1sMstpInstanceVlanId3073To4094.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceVlanId3073To4094.setStatus("current")


class _Rldot1sMstpConfigurationDigest_Type(OctetString):
    """Custom type rldot1sMstpConfigurationDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Rldot1sMstpConfigurationDigest_Type.__name__ = "OctetString"
_Rldot1sMstpConfigurationDigest_Object = MibScalar
rldot1sMstpConfigurationDigest = _Rldot1sMstpConfigurationDigest_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 16),
    _Rldot1sMstpConfigurationDigest_Type()
)
rldot1sMstpConfigurationDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpConfigurationDigest.setStatus("current")


class _Rldot1sMstpPendingConfigurationDigest_Type(OctetString):
    """Custom type rldot1sMstpPendingConfigurationDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Rldot1sMstpPendingConfigurationDigest_Type.__name__ = "OctetString"
_Rldot1sMstpPendingConfigurationDigest_Object = MibScalar
rldot1sMstpPendingConfigurationDigest = _Rldot1sMstpPendingConfigurationDigest_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 17),
    _Rldot1sMstpPendingConfigurationDigest_Type()
)
rldot1sMstpPendingConfigurationDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpPendingConfigurationDigest.setStatus("current")
_Rldot1sMstpSwInstanceTable_Object = MibTable
rldot1sMstpSwInstanceTable = _Rldot1sMstpSwInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 18)
)
if mibBuilder.loadTexts:
    rldot1sMstpSwInstanceTable.setStatus("current")
_Rldot1sMstpSwInstanceEntry_Object = MibTableRow
rldot1sMstpSwInstanceEntry = _Rldot1sMstpSwInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 18, 1)
)
rldot1sMstpSwInstanceEntry.setIndexNames(
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1sMstpSwInstanceSwId"),
)
if mibBuilder.loadTexts:
    rldot1sMstpSwInstanceEntry.setStatus("current")


class _Rldot1sMstpSwInstanceSwId_Type(Integer32):
    """Custom type rldot1sMstpSwInstanceSwId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Rldot1sMstpSwInstanceSwId_Type.__name__ = "Integer32"
_Rldot1sMstpSwInstanceSwId_Object = MibTableColumn
rldot1sMstpSwInstanceSwId = _Rldot1sMstpSwInstanceSwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 18, 1, 1),
    _Rldot1sMstpSwInstanceSwId_Type()
)
rldot1sMstpSwInstanceSwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpSwInstanceSwId.setStatus("current")


class _Rldot1sMstpSwInstanceId_Type(Integer32):
    """Custom type rldot1sMstpSwInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Rldot1sMstpSwInstanceId_Type.__name__ = "Integer32"
_Rldot1sMstpSwInstanceId_Object = MibTableColumn
rldot1sMstpSwInstanceId = _Rldot1sMstpSwInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 18, 1, 2),
    _Rldot1sMstpSwInstanceId_Type()
)
rldot1sMstpSwInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpSwInstanceId.setStatus("current")
_Rldot1sMstpSwInstanceStatus_Type = RowStatus
_Rldot1sMstpSwInstanceStatus_Object = MibTableColumn
rldot1sMstpSwInstanceStatus = _Rldot1sMstpSwInstanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 6, 18, 1, 3),
    _Rldot1sMstpSwInstanceStatus_Type()
)
rldot1sMstpSwInstanceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rldot1sMstpSwInstanceStatus.setStatus("current")
_Rldot1dTpAgingTime_ObjectIdentity = ObjectIdentity
rldot1dTpAgingTime = _Rldot1dTpAgingTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 7)
)
_Rldot1dTpAgingTimeMin_Type = Integer32
_Rldot1dTpAgingTimeMin_Object = MibScalar
rldot1dTpAgingTimeMin = _Rldot1dTpAgingTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 7, 1),
    _Rldot1dTpAgingTimeMin_Type()
)
rldot1dTpAgingTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dTpAgingTimeMin.setStatus("current")
_Rldot1dTpAgingTimeMax_Type = Integer32
_Rldot1dTpAgingTimeMax_Object = MibScalar
rldot1dTpAgingTimeMax = _Rldot1dTpAgingTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 7, 2),
    _Rldot1dTpAgingTimeMax_Type()
)
rldot1dTpAgingTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dTpAgingTimeMax.setStatus("current")
_RlBrgPvst_ObjectIdentity = ObjectIdentity
rlBrgPvst = _RlBrgPvst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9)
)
_RlBrgPvstVlanTable_Object = MibTable
rlBrgPvstVlanTable = _RlBrgPvstVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 1)
)
if mibBuilder.loadTexts:
    rlBrgPvstVlanTable.setStatus("current")
_RlBrgPvstVlanEntry_Object = MibTableRow
rlBrgPvstVlanEntry = _RlBrgPvstVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 1, 1)
)
rlBrgPvstVlanEntry.setIndexNames(
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rlBrgPvstVlanId"),
)
if mibBuilder.loadTexts:
    rlBrgPvstVlanEntry.setStatus("current")


class _RlBrgPvstVlanId_Type(Integer32):
    """Custom type rlBrgPvstVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RlBrgPvstVlanId_Type.__name__ = "Integer32"
_RlBrgPvstVlanId_Object = MibTableColumn
rlBrgPvstVlanId = _RlBrgPvstVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 1, 1, 1),
    _RlBrgPvstVlanId_Type()
)
rlBrgPvstVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstVlanId.setStatus("current")


class _RlBrgPvstVlanHelloTime_Type(Integer32):
    """Custom type rlBrgPvstVlanHelloTime based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RlBrgPvstVlanHelloTime_Type.__name__ = "Integer32"
_RlBrgPvstVlanHelloTime_Object = MibTableColumn
rlBrgPvstVlanHelloTime = _RlBrgPvstVlanHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 1, 1, 2),
    _RlBrgPvstVlanHelloTime_Type()
)
rlBrgPvstVlanHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgPvstVlanHelloTime.setStatus("current")


class _RlBrgPvstVlanForwardDelay_Type(Integer32):
    """Custom type rlBrgPvstVlanForwardDelay based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_RlBrgPvstVlanForwardDelay_Type.__name__ = "Integer32"
_RlBrgPvstVlanForwardDelay_Object = MibTableColumn
rlBrgPvstVlanForwardDelay = _RlBrgPvstVlanForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 1, 1, 3),
    _RlBrgPvstVlanForwardDelay_Type()
)
rlBrgPvstVlanForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgPvstVlanForwardDelay.setStatus("current")


class _RlBrgPvstVlanMaxAge_Type(Integer32):
    """Custom type rlBrgPvstVlanMaxAge based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_RlBrgPvstVlanMaxAge_Type.__name__ = "Integer32"
_RlBrgPvstVlanMaxAge_Object = MibTableColumn
rlBrgPvstVlanMaxAge = _RlBrgPvstVlanMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 1, 1, 4),
    _RlBrgPvstVlanMaxAge_Type()
)
rlBrgPvstVlanMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgPvstVlanMaxAge.setStatus("current")


class _RlBrgPvstVlanPriority_Type(Integer32):
    """Custom type rlBrgPvstVlanPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_RlBrgPvstVlanPriority_Type.__name__ = "Integer32"
_RlBrgPvstVlanPriority_Object = MibTableColumn
rlBrgPvstVlanPriority = _RlBrgPvstVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 1, 1, 5),
    _RlBrgPvstVlanPriority_Type()
)
rlBrgPvstVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgPvstVlanPriority.setStatus("current")
_RlBrgPvstVlanStatus_Type = RowStatus
_RlBrgPvstVlanStatus_Object = MibTableColumn
rlBrgPvstVlanStatus = _RlBrgPvstVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 1, 1, 6),
    _RlBrgPvstVlanStatus_Type()
)
rlBrgPvstVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlBrgPvstVlanStatus.setStatus("current")
_RlBrgPvstOperVlanTable_Object = MibTable
rlBrgPvstOperVlanTable = _RlBrgPvstOperVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 2)
)
if mibBuilder.loadTexts:
    rlBrgPvstOperVlanTable.setStatus("current")
_RlBrgPvstOperVlanEntry_Object = MibTableRow
rlBrgPvstOperVlanEntry = _RlBrgPvstOperVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 2, 1)
)
rlBrgPvstOperVlanEntry.setIndexNames(
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rlBrgPvstOperVlanId"),
)
if mibBuilder.loadTexts:
    rlBrgPvstOperVlanEntry.setStatus("current")
_RlBrgPvstOperVlanId_Type = Integer32
_RlBrgPvstOperVlanId_Object = MibTableColumn
rlBrgPvstOperVlanId = _RlBrgPvstOperVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 2, 1, 1),
    _RlBrgPvstOperVlanId_Type()
)
rlBrgPvstOperVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperVlanId.setStatus("current")
_RlBrgPvstOperVlanEnable_Type = TruthValue
_RlBrgPvstOperVlanEnable_Object = MibTableColumn
rlBrgPvstOperVlanEnable = _RlBrgPvstOperVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 2, 1, 2),
    _RlBrgPvstOperVlanEnable_Type()
)
rlBrgPvstOperVlanEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperVlanEnable.setStatus("current")
_RlBrgPvstOperVlanTimeSinceTopologyChange_Type = TimeTicks
_RlBrgPvstOperVlanTimeSinceTopologyChange_Object = MibTableColumn
rlBrgPvstOperVlanTimeSinceTopologyChange = _RlBrgPvstOperVlanTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 2, 1, 3),
    _RlBrgPvstOperVlanTimeSinceTopologyChange_Type()
)
rlBrgPvstOperVlanTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperVlanTimeSinceTopologyChange.setStatus("current")
_RlBrgPvstOperVlanTopChanges_Type = Counter32
_RlBrgPvstOperVlanTopChanges_Object = MibTableColumn
rlBrgPvstOperVlanTopChanges = _RlBrgPvstOperVlanTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 2, 1, 4),
    _RlBrgPvstOperVlanTopChanges_Type()
)
rlBrgPvstOperVlanTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperVlanTopChanges.setStatus("current")
_RlBrgPvstOperVlanDesignatedRoot_Type = BridgeId
_RlBrgPvstOperVlanDesignatedRoot_Object = MibTableColumn
rlBrgPvstOperVlanDesignatedRoot = _RlBrgPvstOperVlanDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 2, 1, 5),
    _RlBrgPvstOperVlanDesignatedRoot_Type()
)
rlBrgPvstOperVlanDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperVlanDesignatedRoot.setStatus("current")
_RlBrgPvstOperVlanRootCost_Type = Integer32
_RlBrgPvstOperVlanRootCost_Object = MibTableColumn
rlBrgPvstOperVlanRootCost = _RlBrgPvstOperVlanRootCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 2, 1, 6),
    _RlBrgPvstOperVlanRootCost_Type()
)
rlBrgPvstOperVlanRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperVlanRootCost.setStatus("current")
_RlBrgPvstOperVlanRootPort_Type = Integer32
_RlBrgPvstOperVlanRootPort_Object = MibTableColumn
rlBrgPvstOperVlanRootPort = _RlBrgPvstOperVlanRootPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 2, 1, 7),
    _RlBrgPvstOperVlanRootPort_Type()
)
rlBrgPvstOperVlanRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperVlanRootPort.setStatus("current")
_RlBrgPvstOperVlanRootMaxAge_Type = Integer32
_RlBrgPvstOperVlanRootMaxAge_Object = MibTableColumn
rlBrgPvstOperVlanRootMaxAge = _RlBrgPvstOperVlanRootMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 2, 1, 8),
    _RlBrgPvstOperVlanRootMaxAge_Type()
)
rlBrgPvstOperVlanRootMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperVlanRootMaxAge.setStatus("current")
_RlBrgPvstOperVlanRootHelloTime_Type = Integer32
_RlBrgPvstOperVlanRootHelloTime_Object = MibTableColumn
rlBrgPvstOperVlanRootHelloTime = _RlBrgPvstOperVlanRootHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 2, 1, 9),
    _RlBrgPvstOperVlanRootHelloTime_Type()
)
rlBrgPvstOperVlanRootHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperVlanRootHelloTime.setStatus("current")
_RlBrgPvstOperVlanRootForwardDelay_Type = Integer32
_RlBrgPvstOperVlanRootForwardDelay_Object = MibTableColumn
rlBrgPvstOperVlanRootForwardDelay = _RlBrgPvstOperVlanRootForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 2, 1, 10),
    _RlBrgPvstOperVlanRootForwardDelay_Type()
)
rlBrgPvstOperVlanRootForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperVlanRootForwardDelay.setStatus("current")
_RlBrgPvstOperVlanMaxAge_Type = Integer32
_RlBrgPvstOperVlanMaxAge_Object = MibTableColumn
rlBrgPvstOperVlanMaxAge = _RlBrgPvstOperVlanMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 2, 1, 11),
    _RlBrgPvstOperVlanMaxAge_Type()
)
rlBrgPvstOperVlanMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperVlanMaxAge.setStatus("current")
_RlBrgPvstOperVlanHelloTime_Type = Integer32
_RlBrgPvstOperVlanHelloTime_Object = MibTableColumn
rlBrgPvstOperVlanHelloTime = _RlBrgPvstOperVlanHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 2, 1, 12),
    _RlBrgPvstOperVlanHelloTime_Type()
)
rlBrgPvstOperVlanHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperVlanHelloTime.setStatus("current")
_RlBrgPvstOperVlanForwardDelay_Type = Integer32
_RlBrgPvstOperVlanForwardDelay_Object = MibTableColumn
rlBrgPvstOperVlanForwardDelay = _RlBrgPvstOperVlanForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 2, 1, 13),
    _RlBrgPvstOperVlanForwardDelay_Type()
)
rlBrgPvstOperVlanForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperVlanForwardDelay.setStatus("current")
_RlBrgPvstOperVlanPriority_Type = Integer32
_RlBrgPvstOperVlanPriority_Object = MibTableColumn
rlBrgPvstOperVlanPriority = _RlBrgPvstOperVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 2, 1, 14),
    _RlBrgPvstOperVlanPriority_Type()
)
rlBrgPvstOperVlanPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperVlanPriority.setStatus("current")
_RlBrgPvstPortTable_Object = MibTable
rlBrgPvstPortTable = _RlBrgPvstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 3)
)
if mibBuilder.loadTexts:
    rlBrgPvstPortTable.setStatus("current")
_RlBrgPvstPortEntry_Object = MibTableRow
rlBrgPvstPortEntry = _RlBrgPvstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 3, 1)
)
rlBrgPvstPortEntry.setIndexNames(
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rlBrgPvstPortVlanId"),
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rlBrgPvstPortPort"),
)
if mibBuilder.loadTexts:
    rlBrgPvstPortEntry.setStatus("current")


class _RlBrgPvstPortVlanId_Type(Integer32):
    """Custom type rlBrgPvstPortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RlBrgPvstPortVlanId_Type.__name__ = "Integer32"
_RlBrgPvstPortVlanId_Object = MibTableColumn
rlBrgPvstPortVlanId = _RlBrgPvstPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 3, 1, 1),
    _RlBrgPvstPortVlanId_Type()
)
rlBrgPvstPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstPortVlanId.setStatus("current")


class _RlBrgPvstPortPort_Type(Integer32):
    """Custom type rlBrgPvstPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_RlBrgPvstPortPort_Type.__name__ = "Integer32"
_RlBrgPvstPortPort_Object = MibTableColumn
rlBrgPvstPortPort = _RlBrgPvstPortPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 3, 1, 2),
    _RlBrgPvstPortPort_Type()
)
rlBrgPvstPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstPortPort.setStatus("current")


class _RlBrgPvstPortPathCost_Type(Integer32):
    """Custom type rlBrgPvstPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_RlBrgPvstPortPathCost_Type.__name__ = "Integer32"
_RlBrgPvstPortPathCost_Object = MibTableColumn
rlBrgPvstPortPathCost = _RlBrgPvstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 3, 1, 3),
    _RlBrgPvstPortPathCost_Type()
)
rlBrgPvstPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgPvstPortPathCost.setStatus("current")


class _RlBrgPvstPortPriority_Type(Integer32):
    """Custom type rlBrgPvstPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_RlBrgPvstPortPriority_Type.__name__ = "Integer32"
_RlBrgPvstPortPriority_Object = MibTableColumn
rlBrgPvstPortPriority = _RlBrgPvstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 3, 1, 4),
    _RlBrgPvstPortPriority_Type()
)
rlBrgPvstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgPvstPortPriority.setStatus("current")
_RlBrgPvstPortStatus_Type = RowStatus
_RlBrgPvstPortStatus_Object = MibTableColumn
rlBrgPvstPortStatus = _RlBrgPvstPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 3, 1, 5),
    _RlBrgPvstPortStatus_Type()
)
rlBrgPvstPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlBrgPvstPortStatus.setStatus("current")
_RlBrgPvstOperPortTable_Object = MibTable
rlBrgPvstOperPortTable = _RlBrgPvstOperPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 4)
)
if mibBuilder.loadTexts:
    rlBrgPvstOperPortTable.setStatus("current")
_RlBrgPvstOperPortEntry_Object = MibTableRow
rlBrgPvstOperPortEntry = _RlBrgPvstOperPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 4, 1)
)
rlBrgPvstOperPortEntry.setIndexNames(
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rlBrgPvstOperPortVlanId"),
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rlBrgPvstOperPortPort"),
)
if mibBuilder.loadTexts:
    rlBrgPvstOperPortEntry.setStatus("current")
_RlBrgPvstOperPortVlanId_Type = Integer32
_RlBrgPvstOperPortVlanId_Object = MibTableColumn
rlBrgPvstOperPortVlanId = _RlBrgPvstOperPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 4, 1, 1),
    _RlBrgPvstOperPortVlanId_Type()
)
rlBrgPvstOperPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperPortVlanId.setStatus("current")
_RlBrgPvstOperPortPort_Type = Integer32
_RlBrgPvstOperPortPort_Object = MibTableColumn
rlBrgPvstOperPortPort = _RlBrgPvstOperPortPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 4, 1, 2),
    _RlBrgPvstOperPortPort_Type()
)
rlBrgPvstOperPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperPortPort.setStatus("current")
_RlBrgPvstOperPortEnable_Type = TruthValue
_RlBrgPvstOperPortEnable_Object = MibTableColumn
rlBrgPvstOperPortEnable = _RlBrgPvstOperPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 4, 1, 3),
    _RlBrgPvstOperPortEnable_Type()
)
rlBrgPvstOperPortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperPortEnable.setStatus("current")
_RlBrgPvstOperPortPathCost_Type = Integer32
_RlBrgPvstOperPortPathCost_Object = MibTableColumn
rlBrgPvstOperPortPathCost = _RlBrgPvstOperPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 4, 1, 4),
    _RlBrgPvstOperPortPathCost_Type()
)
rlBrgPvstOperPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperPortPathCost.setStatus("current")
_RlBrgPvstOperPortPriority_Type = Integer32
_RlBrgPvstOperPortPriority_Object = MibTableColumn
rlBrgPvstOperPortPriority = _RlBrgPvstOperPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 4, 1, 5),
    _RlBrgPvstOperPortPriority_Type()
)
rlBrgPvstOperPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperPortPriority.setStatus("current")


class _RlBrgPvstOperPortState_Type(Integer32):
    """Custom type rlBrgPvstOperPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6))
    )


_RlBrgPvstOperPortState_Type.__name__ = "Integer32"
_RlBrgPvstOperPortState_Object = MibTableColumn
rlBrgPvstOperPortState = _RlBrgPvstOperPortState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 4, 1, 6),
    _RlBrgPvstOperPortState_Type()
)
rlBrgPvstOperPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperPortState.setStatus("current")


class _RlBrgPvstOperPortRole_Type(Integer32):
    """Custom type rlBrgPvstOperPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("disabled", 1),
          ("alternate", 2),
          ("backup", 3),
          ("root", 4),
          ("designated", 5))
    )


_RlBrgPvstOperPortRole_Type.__name__ = "Integer32"
_RlBrgPvstOperPortRole_Object = MibTableColumn
rlBrgPvstOperPortRole = _RlBrgPvstOperPortRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 4, 1, 7),
    _RlBrgPvstOperPortRole_Type()
)
rlBrgPvstOperPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperPortRole.setStatus("current")


class _RlBrgPvstOperPortBpduType_Type(Integer32):
    """Custom type rlBrgPvstOperPortBpduType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pvst", 2),
          ("rpvst", 3))
    )


_RlBrgPvstOperPortBpduType_Type.__name__ = "Integer32"
_RlBrgPvstOperPortBpduType_Object = MibTableColumn
rlBrgPvstOperPortBpduType = _RlBrgPvstOperPortBpduType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 4, 1, 8),
    _RlBrgPvstOperPortBpduType_Type()
)
rlBrgPvstOperPortBpduType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperPortBpduType.setStatus("current")
_RlBrgPvstOperPortDesignatedRoot_Type = BridgeId
_RlBrgPvstOperPortDesignatedRoot_Object = MibTableColumn
rlBrgPvstOperPortDesignatedRoot = _RlBrgPvstOperPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 4, 1, 9),
    _RlBrgPvstOperPortDesignatedRoot_Type()
)
rlBrgPvstOperPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperPortDesignatedRoot.setStatus("current")
_RlBrgPvstOperPortDesignatedCost_Type = Integer32
_RlBrgPvstOperPortDesignatedCost_Object = MibTableColumn
rlBrgPvstOperPortDesignatedCost = _RlBrgPvstOperPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 4, 1, 10),
    _RlBrgPvstOperPortDesignatedCost_Type()
)
rlBrgPvstOperPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperPortDesignatedCost.setStatus("current")
_RlBrgPvstOperPortDesignatedBridge_Type = BridgeId
_RlBrgPvstOperPortDesignatedBridge_Object = MibTableColumn
rlBrgPvstOperPortDesignatedBridge = _RlBrgPvstOperPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 4, 1, 11),
    _RlBrgPvstOperPortDesignatedBridge_Type()
)
rlBrgPvstOperPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperPortDesignatedBridge.setStatus("current")


class _RlBrgPvstOperPortDesignatedPort_Type(OctetString):
    """Custom type rlBrgPvstOperPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_RlBrgPvstOperPortDesignatedPort_Type.__name__ = "OctetString"
_RlBrgPvstOperPortDesignatedPort_Object = MibTableColumn
rlBrgPvstOperPortDesignatedPort = _RlBrgPvstOperPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 4, 1, 12),
    _RlBrgPvstOperPortDesignatedPort_Type()
)
rlBrgPvstOperPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperPortDesignatedPort.setStatus("current")
_RlBrgPvstOperPortForwardTransitions_Type = Counter32
_RlBrgPvstOperPortForwardTransitions_Object = MibTableColumn
rlBrgPvstOperPortForwardTransitions = _RlBrgPvstOperPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 4, 1, 13),
    _RlBrgPvstOperPortForwardTransitions_Type()
)
rlBrgPvstOperPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperPortForwardTransitions.setStatus("current")
_RlBrgPvstOperPortEdgePort_Type = TruthValue
_RlBrgPvstOperPortEdgePort_Object = MibTableColumn
rlBrgPvstOperPortEdgePort = _RlBrgPvstOperPortEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 4, 1, 14),
    _RlBrgPvstOperPortEdgePort_Type()
)
rlBrgPvstOperPortEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperPortEdgePort.setStatus("current")
_RlBrgPvstOperPortBpduSent_Type = Counter32
_RlBrgPvstOperPortBpduSent_Object = MibTableColumn
rlBrgPvstOperPortBpduSent = _RlBrgPvstOperPortBpduSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 4, 1, 15),
    _RlBrgPvstOperPortBpduSent_Type()
)
rlBrgPvstOperPortBpduSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperPortBpduSent.setStatus("current")
_RlBrgPvstOperPortBpduReceived_Type = Counter32
_RlBrgPvstOperPortBpduReceived_Object = MibTableColumn
rlBrgPvstOperPortBpduReceived = _RlBrgPvstOperPortBpduReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 4, 1, 16),
    _RlBrgPvstOperPortBpduReceived_Type()
)
rlBrgPvstOperPortBpduReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstOperPortBpduReceived.setStatus("current")
_RlBrgPvstInconsistencyPortTable_Object = MibTable
rlBrgPvstInconsistencyPortTable = _RlBrgPvstInconsistencyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 5)
)
if mibBuilder.loadTexts:
    rlBrgPvstInconsistencyPortTable.setStatus("current")
_RlBrgPvstInconsistencyPortEntry_Object = MibTableRow
rlBrgPvstInconsistencyPortEntry = _RlBrgPvstInconsistencyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 5, 1)
)
rlBrgPvstInconsistencyPortEntry.setIndexNames(
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rlBrgPvstInconsistencyVlanId"),
    (0, "CISCOSB-BRIDGEMIBOBJECTS-MIB", "rlBrgPvstInconsistencyPort"),
)
if mibBuilder.loadTexts:
    rlBrgPvstInconsistencyPortEntry.setStatus("current")


class _RlBrgPvstInconsistencyVlanId_Type(Integer32):
    """Custom type rlBrgPvstInconsistencyVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RlBrgPvstInconsistencyVlanId_Type.__name__ = "Integer32"
_RlBrgPvstInconsistencyVlanId_Object = MibTableColumn
rlBrgPvstInconsistencyVlanId = _RlBrgPvstInconsistencyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 5, 1, 1),
    _RlBrgPvstInconsistencyVlanId_Type()
)
rlBrgPvstInconsistencyVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstInconsistencyVlanId.setStatus("current")


class _RlBrgPvstInconsistencyPort_Type(Integer32):
    """Custom type rlBrgPvstInconsistencyPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_RlBrgPvstInconsistencyPort_Type.__name__ = "Integer32"
_RlBrgPvstInconsistencyPort_Object = MibTableColumn
rlBrgPvstInconsistencyPort = _RlBrgPvstInconsistencyPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 5, 1, 2),
    _RlBrgPvstInconsistencyPort_Type()
)
rlBrgPvstInconsistencyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstInconsistencyPort.setStatus("current")


class _RlBrgPvstInconsistencyState_Type(Bits):
    """Custom type rlBrgPvstInconsistencyState based on Bits"""
    namedValues = NamedValues(
        *(("type", 0),
          ("pvid", 1))
    )

_RlBrgPvstInconsistencyState_Type.__name__ = "Bits"
_RlBrgPvstInconsistencyState_Object = MibTableColumn
rlBrgPvstInconsistencyState = _RlBrgPvstInconsistencyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57, 9, 5, 1, 3),
    _RlBrgPvstInconsistencyState_Type()
)
rlBrgPvstInconsistencyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgPvstInconsistencyState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-BRIDGEMIBOBJECTS-MIB",
    **{"VlanList1": VlanList1,
       "VlanList2": VlanList2,
       "VlanList3": VlanList3,
       "VlanList4": VlanList4,
       "rlpBridgeMIBObjects": rlpBridgeMIBObjects,
       "rldot1dPriority": rldot1dPriority,
       "rldot1dPriorityMibVersion": rldot1dPriorityMibVersion,
       "rldot1dPriorityPortGroupTable": rldot1dPriorityPortGroupTable,
       "rldot1dPriorityPortGroupEntry": rldot1dPriorityPortGroupEntry,
       "rldot1dPriorityPortGroupNumber": rldot1dPriorityPortGroupNumber,
       "rldot1dStp": rldot1dStp,
       "rldot1dStpMibVersion": rldot1dStpMibVersion,
       "rldot1dStpType": rldot1dStpType,
       "rldot1dStpEnable": rldot1dStpEnable,
       "rldot1dStpPortMustBelongToVlan": rldot1dStpPortMustBelongToVlan,
       "rldot1dStpExtendedPortNumberFormat": rldot1dStpExtendedPortNumberFormat,
       "rldot1dStpVlanTable": rldot1dStpVlanTable,
       "rldot1dStpVlanEntry": rldot1dStpVlanEntry,
       "rldot1dStpVlan": rldot1dStpVlan,
       "rldot1dStpVlanEnable": rldot1dStpVlanEnable,
       "rldot1dStpTimeSinceTopologyChange": rldot1dStpTimeSinceTopologyChange,
       "rldot1dStpTopChanges": rldot1dStpTopChanges,
       "rldot1dStpDesignatedRoot": rldot1dStpDesignatedRoot,
       "rldot1dStpRootCost": rldot1dStpRootCost,
       "rldot1dStpRootPort": rldot1dStpRootPort,
       "rldot1dStpMaxAge": rldot1dStpMaxAge,
       "rldot1dStpHelloTime": rldot1dStpHelloTime,
       "rldot1dStpHoldTime": rldot1dStpHoldTime,
       "rldot1dStpForwardDelay": rldot1dStpForwardDelay,
       "rldot1dStpVlanPortTable": rldot1dStpVlanPortTable,
       "rldot1dStpVlanPortEntry": rldot1dStpVlanPortEntry,
       "rldot1dStpVlanPortVlan": rldot1dStpVlanPortVlan,
       "rldot1dStpVlanPortPort": rldot1dStpVlanPortPort,
       "rldot1dStpVlanPortPriority": rldot1dStpVlanPortPriority,
       "rldot1dStpVlanPortState": rldot1dStpVlanPortState,
       "rldot1dStpVlanPortEnable": rldot1dStpVlanPortEnable,
       "rldot1dStpVlanPortPathCost": rldot1dStpVlanPortPathCost,
       "rldot1dStpVlanPortDesignatedRoot": rldot1dStpVlanPortDesignatedRoot,
       "rldot1dStpVlanPortDesignatedCost": rldot1dStpVlanPortDesignatedCost,
       "rldot1dStpVlanPortDesignatedBridge": rldot1dStpVlanPortDesignatedBridge,
       "rldot1dStpVlanPortDesignatedPort": rldot1dStpVlanPortDesignatedPort,
       "rldot1dStpVlanPortForwardTransitions": rldot1dStpVlanPortForwardTransitions,
       "rldot1dStpTrapVariable": rldot1dStpTrapVariable,
       "rldot1dStpTrapVrblifIndex": rldot1dStpTrapVrblifIndex,
       "rldot1dStpTrapVrblVID": rldot1dStpTrapVrblVID,
       "rldot1dStpTypeAfterReset": rldot1dStpTypeAfterReset,
       "rldot1dStpMonitorTime": rldot1dStpMonitorTime,
       "rldot1dStpBpduCount": rldot1dStpBpduCount,
       "rldot1dStpLastChanged": rldot1dStpLastChanged,
       "rldot1dStpPortTable": rldot1dStpPortTable,
       "rldot1dStpPortEntry": rldot1dStpPortEntry,
       "rldot1dStpPortPort": rldot1dStpPortPort,
       "rldot1dStpPortDampEnable": rldot1dStpPortDampEnable,
       "rldot1dStpPortDampStable": rldot1dStpPortDampStable,
       "rldot1dStpPortFilterBpdu": rldot1dStpPortFilterBpdu,
       "rldot1dStpPortBpduSent": rldot1dStpPortBpduSent,
       "rldot1dStpPortBpduReceived": rldot1dStpPortBpduReceived,
       "rldot1dStpPortRole": rldot1dStpPortRole,
       "rldot1dStpBpduType": rldot1dStpBpduType,
       "rldot1dStpPortRestrictedRole": rldot1dStpPortRestrictedRole,
       "rldot1dStpPortAutoEdgePort": rldot1dStpPortAutoEdgePort,
       "rldot1dStpPortLoopback": rldot1dStpPortLoopback,
       "rldot1dStpPortBpduOperStatus": rldot1dStpPortBpduOperStatus,
       "rldot1dStpPortTcnGuardEnable": rldot1dStpPortTcnGuardEnable,
       "rldot1dStpPortsEnable": rldot1dStpPortsEnable,
       "rldot1dStpTaggedFlooding": rldot1dStpTaggedFlooding,
       "rldot1dStpPortBelongToVlanDefault": rldot1dStpPortBelongToVlanDefault,
       "rldot1dStpEnableByDefault": rldot1dStpEnableByDefault,
       "rldot1dStpPortToDefault": rldot1dStpPortToDefault,
       "rldot1dStpSupportedType": rldot1dStpSupportedType,
       "rldot1dStpEdgeportSupportInStp": rldot1dStpEdgeportSupportInStp,
       "rldot1dStpFilterBpdu": rldot1dStpFilterBpdu,
       "rldot1dStpFloodBpduMethod": rldot1dStpFloodBpduMethod,
       "rldot1dStpSeparatedBridges": rldot1dStpSeparatedBridges,
       "rldot1dStpSeparatedBridgesTable": rldot1dStpSeparatedBridgesTable,
       "rldot1dStpSeparatedBridgesEntry": rldot1dStpSeparatedBridgesEntry,
       "rldot1dStpSeparatedBridgesPortEnable": rldot1dStpSeparatedBridgesPortEnable,
       "rldot1dStpSeparatedBridgesEnable": rldot1dStpSeparatedBridgesEnable,
       "rldot1dStpSeparatedBridgesAutoConfig": rldot1dStpSeparatedBridgesAutoConfig,
       "rldot1dStpPortBpduGuardTable": rldot1dStpPortBpduGuardTable,
       "rldot1dStpPortBpduGuardEntry": rldot1dStpPortBpduGuardEntry,
       "rldot1dStpPortBpduGuardEnable": rldot1dStpPortBpduGuardEnable,
       "rldot1dStpLoopbackGuardEnable": rldot1dStpLoopbackGuardEnable,
       "rldot1dStpDisabledPortStateTable": rldot1dStpDisabledPortStateTable,
       "rldot1dStpDisabledPortStateEntry": rldot1dStpDisabledPortStateEntry,
       "rldot1dStpDisabledPortState": rldot1dStpDisabledPortState,
       "rldot1dStpClearPortCounters": rldot1dStpClearPortCounters,
       "rldot1dExtBase": rldot1dExtBase,
       "rldot1dExtBaseMibVersion": rldot1dExtBaseMibVersion,
       "rldot1dDeviceCapabilities": rldot1dDeviceCapabilities,
       "rldot1wRStp": rldot1wRStp,
       "rldot1wRStpVlanEdgePortTable": rldot1wRStpVlanEdgePortTable,
       "rldot1wRStpVlanEdgePortEntry": rldot1wRStpVlanEdgePortEntry,
       "rldot1wRStpVlanEdgePortVlan": rldot1wRStpVlanEdgePortVlan,
       "rldot1wRStpVlanEdgePortPort": rldot1wRStpVlanEdgePortPort,
       "rldot1wRStpEdgePortStatus": rldot1wRStpEdgePortStatus,
       "rldot1wRStpForceVersionTable": rldot1wRStpForceVersionTable,
       "rldot1wRStpForceVersionEntry": rldot1wRStpForceVersionEntry,
       "rldot1wRStpForceVersionVlan": rldot1wRStpForceVersionVlan,
       "rldot1wRStpForceVersionState": rldot1wRStpForceVersionState,
       "rldot1pPriorityMap": rldot1pPriorityMap,
       "rldot1pPriorityMapState": rldot1pPriorityMapState,
       "rldot1pPriorityMapTable": rldot1pPriorityMapTable,
       "rldot1pPriorityMapEntry": rldot1pPriorityMapEntry,
       "rldot1pPriorityMapName": rldot1pPriorityMapName,
       "rldot1pPriorityMapPriority": rldot1pPriorityMapPriority,
       "rldot1pPriorityMapPort": rldot1pPriorityMapPort,
       "rldot1pPriorityMapPortList": rldot1pPriorityMapPortList,
       "rldot1pPriorityMapStatus": rldot1pPriorityMapStatus,
       "rldot1sMstp": rldot1sMstp,
       "rldot1sMstpInstanceTable": rldot1sMstpInstanceTable,
       "rldot1sMstpInstanceEntry": rldot1sMstpInstanceEntry,
       "rldot1sMstpInstanceId": rldot1sMstpInstanceId,
       "rldot1sMstpInstanceEnable": rldot1sMstpInstanceEnable,
       "rldot1sMstpInstanceTimeSinceTopologyChange": rldot1sMstpInstanceTimeSinceTopologyChange,
       "rldot1sMstpInstanceTopChanges": rldot1sMstpInstanceTopChanges,
       "rldot1sMstpInstanceDesignatedRoot": rldot1sMstpInstanceDesignatedRoot,
       "rldot1sMstpInstanceRootCost": rldot1sMstpInstanceRootCost,
       "rldot1sMstpInstanceRootPort": rldot1sMstpInstanceRootPort,
       "rldot1sMstpInstanceMaxAge": rldot1sMstpInstanceMaxAge,
       "rldot1sMstpInstanceHelloTime": rldot1sMstpInstanceHelloTime,
       "rldot1sMstpInstanceHoldTime": rldot1sMstpInstanceHoldTime,
       "rldot1sMstpInstanceForwardDelay": rldot1sMstpInstanceForwardDelay,
       "rldot1sMstpInstancePriority": rldot1sMstpInstancePriority,
       "rldot1sMstpInstanceRemainingHopes": rldot1sMstpInstanceRemainingHopes,
       "rldot1sMstpInstanceSwId": rldot1sMstpInstanceSwId,
       "rldot1sMstpInstancePortTable": rldot1sMstpInstancePortTable,
       "rldot1sMstpInstancePortEntry": rldot1sMstpInstancePortEntry,
       "rldot1sMstpInstancePortMstiId": rldot1sMstpInstancePortMstiId,
       "rldot1sMstpInstancePortPort": rldot1sMstpInstancePortPort,
       "rldot1sMstpInstancePortPriority": rldot1sMstpInstancePortPriority,
       "rldot1sMstpInstancePortState": rldot1sMstpInstancePortState,
       "rldot1sMstpInstancePortEnable": rldot1sMstpInstancePortEnable,
       "rldot1sMstpInstancePortPathCost": rldot1sMstpInstancePortPathCost,
       "rldot1sMstpInstancePortDesignatedRoot": rldot1sMstpInstancePortDesignatedRoot,
       "rldot1sMstpInstancePortDesignatedCost": rldot1sMstpInstancePortDesignatedCost,
       "rldot1sMstpInstancePortDesignatedBridge": rldot1sMstpInstancePortDesignatedBridge,
       "rldot1sMstpInstancePortDesignatedPort": rldot1sMstpInstancePortDesignatedPort,
       "rldot1sMstpInstancePortForwardTransitions": rldot1sMstpInstancePortForwardTransitions,
       "rldot1sMStpInstancePortAdminPathCost": rldot1sMStpInstancePortAdminPathCost,
       "rldot1sMStpInstancePortRole": rldot1sMStpInstancePortRole,
       "rldot1sMstpMaxHopes": rldot1sMstpMaxHopes,
       "rldot1sMstpConfigurationName": rldot1sMstpConfigurationName,
       "rldot1sMstpRevisionLevel": rldot1sMstpRevisionLevel,
       "rldot1sMstpVlanTable": rldot1sMstpVlanTable,
       "rldot1sMstpVlanEntry": rldot1sMstpVlanEntry,
       "rldot1sMstpVlan": rldot1sMstpVlan,
       "rldot1sMstpGroup": rldot1sMstpGroup,
       "rldot1sMstpPendingGroup": rldot1sMstpPendingGroup,
       "rldot1sMstpExtPortTable": rldot1sMstpExtPortTable,
       "rldot1sMstpExtPortEntry": rldot1sMstpExtPortEntry,
       "rldot1sMstpExtPortPort": rldot1sMstpExtPortPort,
       "rldot1sMstpExtPortInternalOperPathCost": rldot1sMstpExtPortInternalOperPathCost,
       "rldot1sMstpExtPortDesignatedRegionalRoot": rldot1sMstpExtPortDesignatedRegionalRoot,
       "rldot1sMstpExtPortDesignatedRegionalCost": rldot1sMstpExtPortDesignatedRegionalCost,
       "rldot1sMstpExtPortBoundary": rldot1sMstpExtPortBoundary,
       "rldot1sMstpExtPortInternalAdminPathCost": rldot1sMstpExtPortInternalAdminPathCost,
       "rldot1sMstpDesignatedMaxHopes": rldot1sMstpDesignatedMaxHopes,
       "rldot1sMstpRegionalRoot": rldot1sMstpRegionalRoot,
       "rldot1sMstpRegionalRootCost": rldot1sMstpRegionalRootCost,
       "rldot1sMstpPendingConfigurationName": rldot1sMstpPendingConfigurationName,
       "rldot1sMstpPendingRevisionLevel": rldot1sMstpPendingRevisionLevel,
       "rldot1sMstpPendingAction": rldot1sMstpPendingAction,
       "rldot1sMstpRemainingHops": rldot1sMstpRemainingHops,
       "rldot1sMstpInstanceVlanTable": rldot1sMstpInstanceVlanTable,
       "rldot1sMstpInstanceVlanEntry": rldot1sMstpInstanceVlanEntry,
       "rldot1sMstpInstanceVlanId": rldot1sMstpInstanceVlanId,
       "rldot1sMstpInstanceVlanDbType": rldot1sMstpInstanceVlanDbType,
       "rldot1sMstpInstanceVlanId1To1024": rldot1sMstpInstanceVlanId1To1024,
       "rldot1sMstpInstanceVlanId1025To2048": rldot1sMstpInstanceVlanId1025To2048,
       "rldot1sMstpInstanceVlanId2049To3072": rldot1sMstpInstanceVlanId2049To3072,
       "rldot1sMstpInstanceVlanId3073To4094": rldot1sMstpInstanceVlanId3073To4094,
       "rldot1sMstpConfigurationDigest": rldot1sMstpConfigurationDigest,
       "rldot1sMstpPendingConfigurationDigest": rldot1sMstpPendingConfigurationDigest,
       "rldot1sMstpSwInstanceTable": rldot1sMstpSwInstanceTable,
       "rldot1sMstpSwInstanceEntry": rldot1sMstpSwInstanceEntry,
       "rldot1sMstpSwInstanceSwId": rldot1sMstpSwInstanceSwId,
       "rldot1sMstpSwInstanceId": rldot1sMstpSwInstanceId,
       "rldot1sMstpSwInstanceStatus": rldot1sMstpSwInstanceStatus,
       "rldot1dTpAgingTime": rldot1dTpAgingTime,
       "rldot1dTpAgingTimeMin": rldot1dTpAgingTimeMin,
       "rldot1dTpAgingTimeMax": rldot1dTpAgingTimeMax,
       "rlBrgPvst": rlBrgPvst,
       "rlBrgPvstVlanTable": rlBrgPvstVlanTable,
       "rlBrgPvstVlanEntry": rlBrgPvstVlanEntry,
       "rlBrgPvstVlanId": rlBrgPvstVlanId,
       "rlBrgPvstVlanHelloTime": rlBrgPvstVlanHelloTime,
       "rlBrgPvstVlanForwardDelay": rlBrgPvstVlanForwardDelay,
       "rlBrgPvstVlanMaxAge": rlBrgPvstVlanMaxAge,
       "rlBrgPvstVlanPriority": rlBrgPvstVlanPriority,
       "rlBrgPvstVlanStatus": rlBrgPvstVlanStatus,
       "rlBrgPvstOperVlanTable": rlBrgPvstOperVlanTable,
       "rlBrgPvstOperVlanEntry": rlBrgPvstOperVlanEntry,
       "rlBrgPvstOperVlanId": rlBrgPvstOperVlanId,
       "rlBrgPvstOperVlanEnable": rlBrgPvstOperVlanEnable,
       "rlBrgPvstOperVlanTimeSinceTopologyChange": rlBrgPvstOperVlanTimeSinceTopologyChange,
       "rlBrgPvstOperVlanTopChanges": rlBrgPvstOperVlanTopChanges,
       "rlBrgPvstOperVlanDesignatedRoot": rlBrgPvstOperVlanDesignatedRoot,
       "rlBrgPvstOperVlanRootCost": rlBrgPvstOperVlanRootCost,
       "rlBrgPvstOperVlanRootPort": rlBrgPvstOperVlanRootPort,
       "rlBrgPvstOperVlanRootMaxAge": rlBrgPvstOperVlanRootMaxAge,
       "rlBrgPvstOperVlanRootHelloTime": rlBrgPvstOperVlanRootHelloTime,
       "rlBrgPvstOperVlanRootForwardDelay": rlBrgPvstOperVlanRootForwardDelay,
       "rlBrgPvstOperVlanMaxAge": rlBrgPvstOperVlanMaxAge,
       "rlBrgPvstOperVlanHelloTime": rlBrgPvstOperVlanHelloTime,
       "rlBrgPvstOperVlanForwardDelay": rlBrgPvstOperVlanForwardDelay,
       "rlBrgPvstOperVlanPriority": rlBrgPvstOperVlanPriority,
       "rlBrgPvstPortTable": rlBrgPvstPortTable,
       "rlBrgPvstPortEntry": rlBrgPvstPortEntry,
       "rlBrgPvstPortVlanId": rlBrgPvstPortVlanId,
       "rlBrgPvstPortPort": rlBrgPvstPortPort,
       "rlBrgPvstPortPathCost": rlBrgPvstPortPathCost,
       "rlBrgPvstPortPriority": rlBrgPvstPortPriority,
       "rlBrgPvstPortStatus": rlBrgPvstPortStatus,
       "rlBrgPvstOperPortTable": rlBrgPvstOperPortTable,
       "rlBrgPvstOperPortEntry": rlBrgPvstOperPortEntry,
       "rlBrgPvstOperPortVlanId": rlBrgPvstOperPortVlanId,
       "rlBrgPvstOperPortPort": rlBrgPvstOperPortPort,
       "rlBrgPvstOperPortEnable": rlBrgPvstOperPortEnable,
       "rlBrgPvstOperPortPathCost": rlBrgPvstOperPortPathCost,
       "rlBrgPvstOperPortPriority": rlBrgPvstOperPortPriority,
       "rlBrgPvstOperPortState": rlBrgPvstOperPortState,
       "rlBrgPvstOperPortRole": rlBrgPvstOperPortRole,
       "rlBrgPvstOperPortBpduType": rlBrgPvstOperPortBpduType,
       "rlBrgPvstOperPortDesignatedRoot": rlBrgPvstOperPortDesignatedRoot,
       "rlBrgPvstOperPortDesignatedCost": rlBrgPvstOperPortDesignatedCost,
       "rlBrgPvstOperPortDesignatedBridge": rlBrgPvstOperPortDesignatedBridge,
       "rlBrgPvstOperPortDesignatedPort": rlBrgPvstOperPortDesignatedPort,
       "rlBrgPvstOperPortForwardTransitions": rlBrgPvstOperPortForwardTransitions,
       "rlBrgPvstOperPortEdgePort": rlBrgPvstOperPortEdgePort,
       "rlBrgPvstOperPortBpduSent": rlBrgPvstOperPortBpduSent,
       "rlBrgPvstOperPortBpduReceived": rlBrgPvstOperPortBpduReceived,
       "rlBrgPvstInconsistencyPortTable": rlBrgPvstInconsistencyPortTable,
       "rlBrgPvstInconsistencyPortEntry": rlBrgPvstInconsistencyPortEntry,
       "rlBrgPvstInconsistencyVlanId": rlBrgPvstInconsistencyVlanId,
       "rlBrgPvstInconsistencyPort": rlBrgPvstInconsistencyPort,
       "rlBrgPvstInconsistencyState": rlBrgPvstInconsistencyState}
)
