# SNMP MIB module (NSCRTV-EPON-STP-MGM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fs\NSCRTV-EPON-STP-MGM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:46:58 2025
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
 Timeout) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout")

(AutoNegotiationTechAbility,
 EponAlarmCode,
 EponAlarmInstance,
 EponCardIndex,
 EponDeviceIndex,
 EponPortIndex,
 EponSeverityType,
 EponStats15MinRecordType,
 EponStats24HourRecordType,
 EponStatsThresholdType,
 TAddress,
 stpManagementObjects) = mibBuilder.importSymbols(
    "NSCRTV-EPONEOC-EPON-MIB",
    "AutoNegotiationTechAbility",
    "EponAlarmCode",
    "EponAlarmInstance",
    "EponCardIndex",
    "EponDeviceIndex",
    "EponPortIndex",
    "EponSeverityType",
    "EponStats15MinRecordType",
    "EponStats24HourRecordType",
    "EponStatsThresholdType",
    "TAddress",
    "stpManagementObjects")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StpGlobalSetTable_Object = MibTable
stpGlobalSetTable = _StpGlobalSetTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1)
)
if mibBuilder.loadTexts:
    stpGlobalSetTable.setStatus("current")
_StpGlobalSetEntry_Object = MibTableRow
stpGlobalSetEntry = _StpGlobalSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1)
)
stpGlobalSetEntry.setIndexNames(
    (0, "NSCRTV-EPON-STP-MGM-MIB", "stpGlobalSetIndex"),
)
if mibBuilder.loadTexts:
    stpGlobalSetEntry.setStatus("current")
_StpGlobalSetIndex_Type = EponDeviceIndex
_StpGlobalSetIndex_Object = MibTableColumn
stpGlobalSetIndex = _StpGlobalSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 1),
    _StpGlobalSetIndex_Type()
)
stpGlobalSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpGlobalSetIndex.setStatus("current")


class _StpGlobalSetVersion_Type(Integer32):
    """Custom type stpGlobalSetVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 1),
          ("stp", 2))
    )


_StpGlobalSetVersion_Type.__name__ = "Integer32"
_StpGlobalSetVersion_Object = MibTableColumn
stpGlobalSetVersion = _StpGlobalSetVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 2),
    _StpGlobalSetVersion_Type()
)
stpGlobalSetVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpGlobalSetVersion.setStatus("current")


class _StpGlobalSetPriority_Type(Integer32):
    """Custom type stpGlobalSetPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StpGlobalSetPriority_Type.__name__ = "Integer32"
_StpGlobalSetPriority_Object = MibTableColumn
stpGlobalSetPriority = _StpGlobalSetPriority_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 3),
    _StpGlobalSetPriority_Type()
)
stpGlobalSetPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpGlobalSetPriority.setStatus("current")
_StpGlobalSetTimeSinceTopologyChange_Type = TimeTicks
_StpGlobalSetTimeSinceTopologyChange_Object = MibTableColumn
stpGlobalSetTimeSinceTopologyChange = _StpGlobalSetTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 4),
    _StpGlobalSetTimeSinceTopologyChange_Type()
)
stpGlobalSetTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpGlobalSetTimeSinceTopologyChange.setStatus("current")
_StpGlobalSetTopChanges_Type = Counter32
_StpGlobalSetTopChanges_Object = MibTableColumn
stpGlobalSetTopChanges = _StpGlobalSetTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 5),
    _StpGlobalSetTopChanges_Type()
)
stpGlobalSetTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpGlobalSetTopChanges.setStatus("current")
if mibBuilder.loadTexts:
    stpGlobalSetTopChanges.setUnits("topology changes")
_StpGlobalSetDesignatedRoot_Type = BridgeId
_StpGlobalSetDesignatedRoot_Object = MibTableColumn
stpGlobalSetDesignatedRoot = _StpGlobalSetDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 6),
    _StpGlobalSetDesignatedRoot_Type()
)
stpGlobalSetDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpGlobalSetDesignatedRoot.setStatus("current")
_StpGlobalSetRootCost_Type = Integer32
_StpGlobalSetRootCost_Object = MibTableColumn
stpGlobalSetRootCost = _StpGlobalSetRootCost_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 7),
    _StpGlobalSetRootCost_Type()
)
stpGlobalSetRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpGlobalSetRootCost.setStatus("current")


class _StpGlobalSetRootPort_Type(OctetString):
    """Custom type stpGlobalSetRootPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_StpGlobalSetRootPort_Type.__name__ = "OctetString"
_StpGlobalSetRootPort_Object = MibTableColumn
stpGlobalSetRootPort = _StpGlobalSetRootPort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 8),
    _StpGlobalSetRootPort_Type()
)
stpGlobalSetRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpGlobalSetRootPort.setStatus("current")
_StpGlobalSetMaxAge_Type = Timeout
_StpGlobalSetMaxAge_Object = MibTableColumn
stpGlobalSetMaxAge = _StpGlobalSetMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 9),
    _StpGlobalSetMaxAge_Type()
)
stpGlobalSetMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpGlobalSetMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    stpGlobalSetMaxAge.setUnits("centi-seconds")
_StpGlobalSetHelloTime_Type = Timeout
_StpGlobalSetHelloTime_Object = MibTableColumn
stpGlobalSetHelloTime = _StpGlobalSetHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 10),
    _StpGlobalSetHelloTime_Type()
)
stpGlobalSetHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpGlobalSetHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    stpGlobalSetHelloTime.setUnits("centi-seconds")
_StpGlobalSetHoldTime_Type = Integer32
_StpGlobalSetHoldTime_Object = MibTableColumn
stpGlobalSetHoldTime = _StpGlobalSetHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 11),
    _StpGlobalSetHoldTime_Type()
)
stpGlobalSetHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpGlobalSetHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    stpGlobalSetHoldTime.setUnits("centi-seconds")
_StpGlobalSetForwardDelay_Type = Timeout
_StpGlobalSetForwardDelay_Object = MibTableColumn
stpGlobalSetForwardDelay = _StpGlobalSetForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 12),
    _StpGlobalSetForwardDelay_Type()
)
stpGlobalSetForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpGlobalSetForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    stpGlobalSetForwardDelay.setUnits("centi-seconds")


class _StpGlobalSetBridgeMaxAge_Type(Timeout):
    """Custom type stpGlobalSetBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_StpGlobalSetBridgeMaxAge_Type.__name__ = "Timeout"
_StpGlobalSetBridgeMaxAge_Object = MibTableColumn
stpGlobalSetBridgeMaxAge = _StpGlobalSetBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 13),
    _StpGlobalSetBridgeMaxAge_Type()
)
stpGlobalSetBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpGlobalSetBridgeMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    stpGlobalSetBridgeMaxAge.setUnits("centi-seconds")


class _StpGlobalSetBridgeHelloTime_Type(Timeout):
    """Custom type stpGlobalSetBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_StpGlobalSetBridgeHelloTime_Type.__name__ = "Timeout"
_StpGlobalSetBridgeHelloTime_Object = MibTableColumn
stpGlobalSetBridgeHelloTime = _StpGlobalSetBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 14),
    _StpGlobalSetBridgeHelloTime_Type()
)
stpGlobalSetBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpGlobalSetBridgeHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    stpGlobalSetBridgeHelloTime.setUnits("centi-seconds")


class _StpGlobalSetBridgeForwardDelay_Type(Timeout):
    """Custom type stpGlobalSetBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_StpGlobalSetBridgeForwardDelay_Type.__name__ = "Timeout"
_StpGlobalSetBridgeForwardDelay_Object = MibTableColumn
stpGlobalSetBridgeForwardDelay = _StpGlobalSetBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 15),
    _StpGlobalSetBridgeForwardDelay_Type()
)
stpGlobalSetBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpGlobalSetBridgeForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    stpGlobalSetBridgeForwardDelay.setUnits("centi-seconds")


class _StpGlobalSetRstpTxHoldCount_Type(Integer32):
    """Custom type stpGlobalSetRstpTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StpGlobalSetRstpTxHoldCount_Type.__name__ = "Integer32"
_StpGlobalSetRstpTxHoldCount_Object = MibTableColumn
stpGlobalSetRstpTxHoldCount = _StpGlobalSetRstpTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 16),
    _StpGlobalSetRstpTxHoldCount_Type()
)
stpGlobalSetRstpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpGlobalSetRstpTxHoldCount.setStatus("current")
_StpGlobalSetEnable_Type = TruthValue
_StpGlobalSetEnable_Object = MibTableColumn
stpGlobalSetEnable = _StpGlobalSetEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 17),
    _StpGlobalSetEnable_Type()
)
stpGlobalSetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpGlobalSetEnable.setStatus("current")
_StpPortTable_Object = MibTable
stpPortTable = _StpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2)
)
if mibBuilder.loadTexts:
    stpPortTable.setStatus("current")
_StpPortEntry_Object = MibTableRow
stpPortEntry = _StpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1)
)
stpPortEntry.setIndexNames(
    (0, "NSCRTV-EPON-STP-MGM-MIB", "stpPortStpIndex"),
    (0, "NSCRTV-EPON-STP-MGM-MIB", "stpPortCardIndex"),
    (0, "NSCRTV-EPON-STP-MGM-MIB", "stpPortIndex"),
)
if mibBuilder.loadTexts:
    stpPortEntry.setStatus("current")
_StpPortStpIndex_Type = EponDeviceIndex
_StpPortStpIndex_Object = MibTableColumn
stpPortStpIndex = _StpPortStpIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 1),
    _StpPortStpIndex_Type()
)
stpPortStpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpPortStpIndex.setStatus("current")
_StpPortCardIndex_Type = EponCardIndex
_StpPortCardIndex_Object = MibTableColumn
stpPortCardIndex = _StpPortCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 2),
    _StpPortCardIndex_Type()
)
stpPortCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpPortCardIndex.setStatus("current")
_StpPortIndex_Type = EponPortIndex
_StpPortIndex_Object = MibTableColumn
stpPortIndex = _StpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 3),
    _StpPortIndex_Type()
)
stpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpPortIndex.setStatus("current")


class _StpPortStatus_Type(Integer32):
    """Custom type stpPortStatus based on Integer32"""
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


_StpPortStatus_Type.__name__ = "Integer32"
_StpPortStatus_Object = MibTableColumn
stpPortStatus = _StpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 4),
    _StpPortStatus_Type()
)
stpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortStatus.setStatus("current")


class _StpPortPriority_Type(Integer32):
    """Custom type stpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StpPortPriority_Type.__name__ = "Integer32"
_StpPortPriority_Object = MibTableColumn
stpPortPriority = _StpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 5),
    _StpPortPriority_Type()
)
stpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortPriority.setStatus("current")


class _StpPortPathCost_Type(Integer32):
    """Custom type stpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_StpPortPathCost_Type.__name__ = "Integer32"
_StpPortPathCost_Object = MibTableColumn
stpPortPathCost = _StpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 6),
    _StpPortPathCost_Type()
)
stpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortPathCost.setStatus("current")
_StpPortDesignatedRoot_Type = BridgeId
_StpPortDesignatedRoot_Object = MibTableColumn
stpPortDesignatedRoot = _StpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 7),
    _StpPortDesignatedRoot_Type()
)
stpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedRoot.setStatus("current")
_StpPortDesignatedCost_Type = Integer32
_StpPortDesignatedCost_Object = MibTableColumn
stpPortDesignatedCost = _StpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 8),
    _StpPortDesignatedCost_Type()
)
stpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedCost.setStatus("current")
_StpPortDesignatedBridge_Type = BridgeId
_StpPortDesignatedBridge_Object = MibTableColumn
stpPortDesignatedBridge = _StpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 9),
    _StpPortDesignatedBridge_Type()
)
stpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedBridge.setStatus("current")
_StpPortDesignatedPort_Type = Gauge32
_StpPortDesignatedPort_Object = MibTableColumn
stpPortDesignatedPort = _StpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 10),
    _StpPortDesignatedPort_Type()
)
stpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedPort.setStatus("current")
_StpPortForwardTransitions_Type = Unsigned32
_StpPortForwardTransitions_Object = MibTableColumn
stpPortForwardTransitions = _StpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 11),
    _StpPortForwardTransitions_Type()
)
stpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortForwardTransitions.setStatus("current")
if mibBuilder.loadTexts:
    stpPortForwardTransitions.setUnits("seconds")
_StpPortRstpProtocolMigration_Type = TruthValue
_StpPortRstpProtocolMigration_Object = MibTableColumn
stpPortRstpProtocolMigration = _StpPortRstpProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 12),
    _StpPortRstpProtocolMigration_Type()
)
stpPortRstpProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortRstpProtocolMigration.setStatus("current")
_StpPortRstpAdminEdgePort_Type = TruthValue
_StpPortRstpAdminEdgePort_Object = MibTableColumn
stpPortRstpAdminEdgePort = _StpPortRstpAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 13),
    _StpPortRstpAdminEdgePort_Type()
)
stpPortRstpAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortRstpAdminEdgePort.setStatus("current")
_StpPortRstpOperEdgePort_Type = TruthValue
_StpPortRstpOperEdgePort_Object = MibTableColumn
stpPortRstpOperEdgePort = _StpPortRstpOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 14),
    _StpPortRstpOperEdgePort_Type()
)
stpPortRstpOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortRstpOperEdgePort.setStatus("current")


class _StpPortPointToPointAdminStatus_Type(Integer32):
    """Custom type stpPortPointToPointAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceFalse", 0),
          ("forceTrue", 1),
          ("auto", 2))
    )


_StpPortPointToPointAdminStatus_Type.__name__ = "Integer32"
_StpPortPointToPointAdminStatus_Object = MibTableColumn
stpPortPointToPointAdminStatus = _StpPortPointToPointAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 15),
    _StpPortPointToPointAdminStatus_Type()
)
stpPortPointToPointAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortPointToPointAdminStatus.setStatus("current")
_StpPortPointToPointOperStatus_Type = TruthValue
_StpPortPointToPointOperStatus_Object = MibTableColumn
stpPortPointToPointOperStatus = _StpPortPointToPointOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 16),
    _StpPortPointToPointOperStatus_Type()
)
stpPortPointToPointOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortPointToPointOperStatus.setStatus("current")
_StpPortEnabled_Type = TruthValue
_StpPortEnabled_Object = MibTableColumn
stpPortEnabled = _StpPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 17),
    _StpPortEnabled_Type()
)
stpPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortEnabled.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-EPON-STP-MGM-MIB",
    **{"stpGlobalSetTable": stpGlobalSetTable,
       "stpGlobalSetEntry": stpGlobalSetEntry,
       "stpGlobalSetIndex": stpGlobalSetIndex,
       "stpGlobalSetVersion": stpGlobalSetVersion,
       "stpGlobalSetPriority": stpGlobalSetPriority,
       "stpGlobalSetTimeSinceTopologyChange": stpGlobalSetTimeSinceTopologyChange,
       "stpGlobalSetTopChanges": stpGlobalSetTopChanges,
       "stpGlobalSetDesignatedRoot": stpGlobalSetDesignatedRoot,
       "stpGlobalSetRootCost": stpGlobalSetRootCost,
       "stpGlobalSetRootPort": stpGlobalSetRootPort,
       "stpGlobalSetMaxAge": stpGlobalSetMaxAge,
       "stpGlobalSetHelloTime": stpGlobalSetHelloTime,
       "stpGlobalSetHoldTime": stpGlobalSetHoldTime,
       "stpGlobalSetForwardDelay": stpGlobalSetForwardDelay,
       "stpGlobalSetBridgeMaxAge": stpGlobalSetBridgeMaxAge,
       "stpGlobalSetBridgeHelloTime": stpGlobalSetBridgeHelloTime,
       "stpGlobalSetBridgeForwardDelay": stpGlobalSetBridgeForwardDelay,
       "stpGlobalSetRstpTxHoldCount": stpGlobalSetRstpTxHoldCount,
       "stpGlobalSetEnable": stpGlobalSetEnable,
       "stpPortTable": stpPortTable,
       "stpPortEntry": stpPortEntry,
       "stpPortStpIndex": stpPortStpIndex,
       "stpPortCardIndex": stpPortCardIndex,
       "stpPortIndex": stpPortIndex,
       "stpPortStatus": stpPortStatus,
       "stpPortPriority": stpPortPriority,
       "stpPortPathCost": stpPortPathCost,
       "stpPortDesignatedRoot": stpPortDesignatedRoot,
       "stpPortDesignatedCost": stpPortDesignatedCost,
       "stpPortDesignatedBridge": stpPortDesignatedBridge,
       "stpPortDesignatedPort": stpPortDesignatedPort,
       "stpPortForwardTransitions": stpPortForwardTransitions,
       "stpPortRstpProtocolMigration": stpPortRstpProtocolMigration,
       "stpPortRstpAdminEdgePort": stpPortRstpAdminEdgePort,
       "stpPortRstpOperEdgePort": stpPortRstpOperEdgePort,
       "stpPortPointToPointAdminStatus": stpPortPointToPointAdminStatus,
       "stpPortPointToPointOperStatus": stpPortPointToPointOperStatus,
       "stpPortEnabled": stpPortEnabled}
)
