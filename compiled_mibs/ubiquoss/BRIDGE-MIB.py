# SNMP MIB module (BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\BRIDGE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:26 2025
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dot1dBridge = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 17)
)
if mibBuilder.loadTexts:
    dot1dBridge.setRevisions(
        ("2005-09-19 00:00",
         "1993-07-31 00:00",
         "1991-12-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BridgeId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class Timeout(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_Dot1dNotifications_ObjectIdentity = ObjectIdentity
dot1dNotifications = _Dot1dNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 0)
)
_Dot1dBase_ObjectIdentity = ObjectIdentity
dot1dBase = _Dot1dBase_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 1)
)
_Dot1dBaseBridgeAddress_Type = MacAddress
_Dot1dBaseBridgeAddress_Object = MibScalar
dot1dBaseBridgeAddress = _Dot1dBaseBridgeAddress_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 1),
    _Dot1dBaseBridgeAddress_Type()
)
dot1dBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBaseBridgeAddress.setStatus("current")
_Dot1dBaseNumPorts_Type = Integer32
_Dot1dBaseNumPorts_Object = MibScalar
dot1dBaseNumPorts = _Dot1dBaseNumPorts_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 2),
    _Dot1dBaseNumPorts_Type()
)
dot1dBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBaseNumPorts.setStatus("current")
if mibBuilder.loadTexts:
    dot1dBaseNumPorts.setUnits("ports")


class _Dot1dBaseType_Type(Integer32):
    """Custom type dot1dBaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("transparent-only", 2),
          ("sourceroute-only", 3),
          ("srt", 4))
    )


_Dot1dBaseType_Type.__name__ = "Integer32"
_Dot1dBaseType_Object = MibScalar
dot1dBaseType = _Dot1dBaseType_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 3),
    _Dot1dBaseType_Type()
)
dot1dBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBaseType.setStatus("current")
_Dot1dBasePortTable_Object = MibTable
dot1dBasePortTable = _Dot1dBasePortTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 4)
)
if mibBuilder.loadTexts:
    dot1dBasePortTable.setStatus("current")
_Dot1dBasePortEntry_Object = MibTableRow
dot1dBasePortEntry = _Dot1dBasePortEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 4, 1)
)
dot1dBasePortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dot1dBasePortEntry.setStatus("current")


class _Dot1dBasePort_Type(Integer32):
    """Custom type dot1dBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1dBasePort_Type.__name__ = "Integer32"
_Dot1dBasePort_Object = MibTableColumn
dot1dBasePort = _Dot1dBasePort_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 1),
    _Dot1dBasePort_Type()
)
dot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePort.setStatus("current")
_Dot1dBasePortIfIndex_Type = InterfaceIndex
_Dot1dBasePortIfIndex_Object = MibTableColumn
dot1dBasePortIfIndex = _Dot1dBasePortIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 2),
    _Dot1dBasePortIfIndex_Type()
)
dot1dBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortIfIndex.setStatus("current")
_Dot1dBasePortCircuit_Type = ObjectIdentifier
_Dot1dBasePortCircuit_Object = MibTableColumn
dot1dBasePortCircuit = _Dot1dBasePortCircuit_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 3),
    _Dot1dBasePortCircuit_Type()
)
dot1dBasePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortCircuit.setStatus("current")
_Dot1dBasePortDelayExceededDiscards_Type = Counter32
_Dot1dBasePortDelayExceededDiscards_Object = MibTableColumn
dot1dBasePortDelayExceededDiscards = _Dot1dBasePortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 4),
    _Dot1dBasePortDelayExceededDiscards_Type()
)
dot1dBasePortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortDelayExceededDiscards.setStatus("current")
_Dot1dBasePortMtuExceededDiscards_Type = Counter32
_Dot1dBasePortMtuExceededDiscards_Object = MibTableColumn
dot1dBasePortMtuExceededDiscards = _Dot1dBasePortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 5),
    _Dot1dBasePortMtuExceededDiscards_Type()
)
dot1dBasePortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortMtuExceededDiscards.setStatus("current")
_Dot1dStp_ObjectIdentity = ObjectIdentity
dot1dStp = _Dot1dStp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 2)
)


class _Dot1dStpProtocolSpecification_Type(Integer32):
    """Custom type dot1dStpProtocolSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("decLb100", 2),
          ("ieee8021d", 3))
    )


_Dot1dStpProtocolSpecification_Type.__name__ = "Integer32"
_Dot1dStpProtocolSpecification_Object = MibScalar
dot1dStpProtocolSpecification = _Dot1dStpProtocolSpecification_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 1),
    _Dot1dStpProtocolSpecification_Type()
)
dot1dStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpProtocolSpecification.setStatus("current")


class _Dot1dStpPriority_Type(Integer32):
    """Custom type dot1dStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1dStpPriority_Type.__name__ = "Integer32"
_Dot1dStpPriority_Object = MibScalar
dot1dStpPriority = _Dot1dStpPriority_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 2),
    _Dot1dStpPriority_Type()
)
dot1dStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPriority.setStatus("current")
_Dot1dStpTimeSinceTopologyChange_Type = TimeTicks
_Dot1dStpTimeSinceTopologyChange_Object = MibScalar
dot1dStpTimeSinceTopologyChange = _Dot1dStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 3),
    _Dot1dStpTimeSinceTopologyChange_Type()
)
dot1dStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpTimeSinceTopologyChange.setStatus("current")
if mibBuilder.loadTexts:
    dot1dStpTimeSinceTopologyChange.setUnits("centi-seconds")
_Dot1dStpTopChanges_Type = Counter32
_Dot1dStpTopChanges_Object = MibScalar
dot1dStpTopChanges = _Dot1dStpTopChanges_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 4),
    _Dot1dStpTopChanges_Type()
)
dot1dStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpTopChanges.setStatus("current")
_Dot1dStpDesignatedRoot_Type = BridgeId
_Dot1dStpDesignatedRoot_Object = MibScalar
dot1dStpDesignatedRoot = _Dot1dStpDesignatedRoot_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 5),
    _Dot1dStpDesignatedRoot_Type()
)
dot1dStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpDesignatedRoot.setStatus("current")
_Dot1dStpRootCost_Type = Integer32
_Dot1dStpRootCost_Object = MibScalar
dot1dStpRootCost = _Dot1dStpRootCost_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 6),
    _Dot1dStpRootCost_Type()
)
dot1dStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpRootCost.setStatus("current")
_Dot1dStpRootPort_Type = Integer32
_Dot1dStpRootPort_Object = MibScalar
dot1dStpRootPort = _Dot1dStpRootPort_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 7),
    _Dot1dStpRootPort_Type()
)
dot1dStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpRootPort.setStatus("current")
_Dot1dStpMaxAge_Type = Timeout
_Dot1dStpMaxAge_Object = MibScalar
dot1dStpMaxAge = _Dot1dStpMaxAge_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 8),
    _Dot1dStpMaxAge_Type()
)
dot1dStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    dot1dStpMaxAge.setUnits("centi-seconds")
_Dot1dStpHelloTime_Type = Timeout
_Dot1dStpHelloTime_Object = MibScalar
dot1dStpHelloTime = _Dot1dStpHelloTime_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 9),
    _Dot1dStpHelloTime_Type()
)
dot1dStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    dot1dStpHelloTime.setUnits("centi-seconds")
_Dot1dStpHoldTime_Type = Integer32
_Dot1dStpHoldTime_Object = MibScalar
dot1dStpHoldTime = _Dot1dStpHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 10),
    _Dot1dStpHoldTime_Type()
)
dot1dStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    dot1dStpHoldTime.setUnits("centi-seconds")
_Dot1dStpForwardDelay_Type = Timeout
_Dot1dStpForwardDelay_Object = MibScalar
dot1dStpForwardDelay = _Dot1dStpForwardDelay_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 11),
    _Dot1dStpForwardDelay_Type()
)
dot1dStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    dot1dStpForwardDelay.setUnits("centi-seconds")


class _Dot1dStpBridgeMaxAge_Type(Timeout):
    """Custom type dot1dStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_Dot1dStpBridgeMaxAge_Type.__name__ = "Timeout"
_Dot1dStpBridgeMaxAge_Object = MibScalar
dot1dStpBridgeMaxAge = _Dot1dStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 12),
    _Dot1dStpBridgeMaxAge_Type()
)
dot1dStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpBridgeMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    dot1dStpBridgeMaxAge.setUnits("centi-seconds")


class _Dot1dStpBridgeHelloTime_Type(Timeout):
    """Custom type dot1dStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_Dot1dStpBridgeHelloTime_Type.__name__ = "Timeout"
_Dot1dStpBridgeHelloTime_Object = MibScalar
dot1dStpBridgeHelloTime = _Dot1dStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 13),
    _Dot1dStpBridgeHelloTime_Type()
)
dot1dStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpBridgeHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    dot1dStpBridgeHelloTime.setUnits("centi-seconds")


class _Dot1dStpBridgeForwardDelay_Type(Timeout):
    """Custom type dot1dStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_Dot1dStpBridgeForwardDelay_Type.__name__ = "Timeout"
_Dot1dStpBridgeForwardDelay_Object = MibScalar
dot1dStpBridgeForwardDelay = _Dot1dStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 14),
    _Dot1dStpBridgeForwardDelay_Type()
)
dot1dStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpBridgeForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    dot1dStpBridgeForwardDelay.setUnits("centi-seconds")
_Dot1dStpPortTable_Object = MibTable
dot1dStpPortTable = _Dot1dStpPortTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15)
)
if mibBuilder.loadTexts:
    dot1dStpPortTable.setStatus("current")
_Dot1dStpPortEntry_Object = MibTableRow
dot1dStpPortEntry = _Dot1dStpPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1)
)
dot1dStpPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dStpPort"),
)
if mibBuilder.loadTexts:
    dot1dStpPortEntry.setStatus("current")


class _Dot1dStpPort_Type(Integer32):
    """Custom type dot1dStpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1dStpPort_Type.__name__ = "Integer32"
_Dot1dStpPort_Object = MibTableColumn
dot1dStpPort = _Dot1dStpPort_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 1),
    _Dot1dStpPort_Type()
)
dot1dStpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPort.setStatus("current")


class _Dot1dStpPortPriority_Type(Integer32):
    """Custom type dot1dStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot1dStpPortPriority_Type.__name__ = "Integer32"
_Dot1dStpPortPriority_Object = MibTableColumn
dot1dStpPortPriority = _Dot1dStpPortPriority_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 2),
    _Dot1dStpPortPriority_Type()
)
dot1dStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortPriority.setStatus("current")


class _Dot1dStpPortState_Type(Integer32):
    """Custom type dot1dStpPortState based on Integer32"""
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


_Dot1dStpPortState_Type.__name__ = "Integer32"
_Dot1dStpPortState_Object = MibTableColumn
dot1dStpPortState = _Dot1dStpPortState_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 3),
    _Dot1dStpPortState_Type()
)
dot1dStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortState.setStatus("current")


class _Dot1dStpPortEnable_Type(Integer32):
    """Custom type dot1dStpPortEnable based on Integer32"""
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


_Dot1dStpPortEnable_Type.__name__ = "Integer32"
_Dot1dStpPortEnable_Object = MibTableColumn
dot1dStpPortEnable = _Dot1dStpPortEnable_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 4),
    _Dot1dStpPortEnable_Type()
)
dot1dStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortEnable.setStatus("current")


class _Dot1dStpPortPathCost_Type(Integer32):
    """Custom type dot1dStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1dStpPortPathCost_Type.__name__ = "Integer32"
_Dot1dStpPortPathCost_Object = MibTableColumn
dot1dStpPortPathCost = _Dot1dStpPortPathCost_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 5),
    _Dot1dStpPortPathCost_Type()
)
dot1dStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortPathCost.setStatus("current")
_Dot1dStpPortDesignatedRoot_Type = BridgeId
_Dot1dStpPortDesignatedRoot_Object = MibTableColumn
dot1dStpPortDesignatedRoot = _Dot1dStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 6),
    _Dot1dStpPortDesignatedRoot_Type()
)
dot1dStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedRoot.setStatus("current")
_Dot1dStpPortDesignatedCost_Type = Integer32
_Dot1dStpPortDesignatedCost_Object = MibTableColumn
dot1dStpPortDesignatedCost = _Dot1dStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 7),
    _Dot1dStpPortDesignatedCost_Type()
)
dot1dStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedCost.setStatus("current")
_Dot1dStpPortDesignatedBridge_Type = BridgeId
_Dot1dStpPortDesignatedBridge_Object = MibTableColumn
dot1dStpPortDesignatedBridge = _Dot1dStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 8),
    _Dot1dStpPortDesignatedBridge_Type()
)
dot1dStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedBridge.setStatus("current")


class _Dot1dStpPortDesignatedPort_Type(OctetString):
    """Custom type dot1dStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_Dot1dStpPortDesignatedPort_Type.__name__ = "OctetString"
_Dot1dStpPortDesignatedPort_Object = MibTableColumn
dot1dStpPortDesignatedPort = _Dot1dStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 9),
    _Dot1dStpPortDesignatedPort_Type()
)
dot1dStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedPort.setStatus("current")
_Dot1dStpPortForwardTransitions_Type = Counter32
_Dot1dStpPortForwardTransitions_Object = MibTableColumn
dot1dStpPortForwardTransitions = _Dot1dStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 10),
    _Dot1dStpPortForwardTransitions_Type()
)
dot1dStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortForwardTransitions.setStatus("current")


class _Dot1dStpPortPathCost32_Type(Integer32):
    """Custom type dot1dStpPortPathCost32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_Dot1dStpPortPathCost32_Type.__name__ = "Integer32"
_Dot1dStpPortPathCost32_Object = MibTableColumn
dot1dStpPortPathCost32 = _Dot1dStpPortPathCost32_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 11),
    _Dot1dStpPortPathCost32_Type()
)
dot1dStpPortPathCost32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortPathCost32.setStatus("current")
_Dot1dSr_ObjectIdentity = ObjectIdentity
dot1dSr = _Dot1dSr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 3)
)
_Dot1dTp_ObjectIdentity = ObjectIdentity
dot1dTp = _Dot1dTp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 4)
)
_Dot1dTpLearnedEntryDiscards_Type = Counter32
_Dot1dTpLearnedEntryDiscards_Object = MibScalar
dot1dTpLearnedEntryDiscards = _Dot1dTpLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 1),
    _Dot1dTpLearnedEntryDiscards_Type()
)
dot1dTpLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpLearnedEntryDiscards.setStatus("current")


class _Dot1dTpAgingTime_Type(Integer32):
    """Custom type dot1dTpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Dot1dTpAgingTime_Type.__name__ = "Integer32"
_Dot1dTpAgingTime_Object = MibScalar
dot1dTpAgingTime = _Dot1dTpAgingTime_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 2),
    _Dot1dTpAgingTime_Type()
)
dot1dTpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dTpAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    dot1dTpAgingTime.setUnits("seconds")
_Dot1dTpFdbTable_Object = MibTable
dot1dTpFdbTable = _Dot1dTpFdbTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 3)
)
if mibBuilder.loadTexts:
    dot1dTpFdbTable.setStatus("current")
_Dot1dTpFdbEntry_Object = MibTableRow
dot1dTpFdbEntry = _Dot1dTpFdbEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 3, 1)
)
dot1dTpFdbEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dTpFdbAddress"),
)
if mibBuilder.loadTexts:
    dot1dTpFdbEntry.setStatus("current")
_Dot1dTpFdbAddress_Type = MacAddress
_Dot1dTpFdbAddress_Object = MibTableColumn
dot1dTpFdbAddress = _Dot1dTpFdbAddress_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 3, 1, 1),
    _Dot1dTpFdbAddress_Type()
)
dot1dTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpFdbAddress.setStatus("current")
_Dot1dTpFdbPort_Type = Integer32
_Dot1dTpFdbPort_Object = MibTableColumn
dot1dTpFdbPort = _Dot1dTpFdbPort_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 3, 1, 2),
    _Dot1dTpFdbPort_Type()
)
dot1dTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpFdbPort.setStatus("current")


class _Dot1dTpFdbStatus_Type(Integer32):
    """Custom type dot1dTpFdbStatus based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("learned", 3),
          ("self", 4),
          ("mgmt", 5))
    )


_Dot1dTpFdbStatus_Type.__name__ = "Integer32"
_Dot1dTpFdbStatus_Object = MibTableColumn
dot1dTpFdbStatus = _Dot1dTpFdbStatus_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 3, 1, 3),
    _Dot1dTpFdbStatus_Type()
)
dot1dTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpFdbStatus.setStatus("current")
_Dot1dTpPortTable_Object = MibTable
dot1dTpPortTable = _Dot1dTpPortTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 4)
)
if mibBuilder.loadTexts:
    dot1dTpPortTable.setStatus("current")
_Dot1dTpPortEntry_Object = MibTableRow
dot1dTpPortEntry = _Dot1dTpPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 4, 1)
)
dot1dTpPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dTpPort"),
)
if mibBuilder.loadTexts:
    dot1dTpPortEntry.setStatus("current")


class _Dot1dTpPort_Type(Integer32):
    """Custom type dot1dTpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1dTpPort_Type.__name__ = "Integer32"
_Dot1dTpPort_Object = MibTableColumn
dot1dTpPort = _Dot1dTpPort_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 1),
    _Dot1dTpPort_Type()
)
dot1dTpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPort.setStatus("current")
_Dot1dTpPortMaxInfo_Type = Integer32
_Dot1dTpPortMaxInfo_Object = MibTableColumn
dot1dTpPortMaxInfo = _Dot1dTpPortMaxInfo_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 2),
    _Dot1dTpPortMaxInfo_Type()
)
dot1dTpPortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortMaxInfo.setStatus("current")
if mibBuilder.loadTexts:
    dot1dTpPortMaxInfo.setUnits("bytes")
_Dot1dTpPortInFrames_Type = Counter32
_Dot1dTpPortInFrames_Object = MibTableColumn
dot1dTpPortInFrames = _Dot1dTpPortInFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 3),
    _Dot1dTpPortInFrames_Type()
)
dot1dTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortInFrames.setStatus("current")
if mibBuilder.loadTexts:
    dot1dTpPortInFrames.setUnits("frames")
_Dot1dTpPortOutFrames_Type = Counter32
_Dot1dTpPortOutFrames_Object = MibTableColumn
dot1dTpPortOutFrames = _Dot1dTpPortOutFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 4),
    _Dot1dTpPortOutFrames_Type()
)
dot1dTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortOutFrames.setStatus("current")
if mibBuilder.loadTexts:
    dot1dTpPortOutFrames.setUnits("frames")
_Dot1dTpPortInDiscards_Type = Counter32
_Dot1dTpPortInDiscards_Object = MibTableColumn
dot1dTpPortInDiscards = _Dot1dTpPortInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 5),
    _Dot1dTpPortInDiscards_Type()
)
dot1dTpPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortInDiscards.setStatus("current")
if mibBuilder.loadTexts:
    dot1dTpPortInDiscards.setUnits("frames")
_Dot1dStatic_ObjectIdentity = ObjectIdentity
dot1dStatic = _Dot1dStatic_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 5)
)
_Dot1dStaticTable_Object = MibTable
dot1dStaticTable = _Dot1dStaticTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 5, 1)
)
if mibBuilder.loadTexts:
    dot1dStaticTable.setStatus("current")
_Dot1dStaticEntry_Object = MibTableRow
dot1dStaticEntry = _Dot1dStaticEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 5, 1, 1)
)
dot1dStaticEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dStaticAddress"),
    (0, "BRIDGE-MIB", "dot1dStaticReceivePort"),
)
if mibBuilder.loadTexts:
    dot1dStaticEntry.setStatus("current")
_Dot1dStaticAddress_Type = MacAddress
_Dot1dStaticAddress_Object = MibTableColumn
dot1dStaticAddress = _Dot1dStaticAddress_Object(
    (1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 1),
    _Dot1dStaticAddress_Type()
)
dot1dStaticAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1dStaticAddress.setStatus("current")


class _Dot1dStaticReceivePort_Type(Integer32):
    """Custom type dot1dStaticReceivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1dStaticReceivePort_Type.__name__ = "Integer32"
_Dot1dStaticReceivePort_Object = MibTableColumn
dot1dStaticReceivePort = _Dot1dStaticReceivePort_Object(
    (1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 2),
    _Dot1dStaticReceivePort_Type()
)
dot1dStaticReceivePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1dStaticReceivePort.setStatus("current")


class _Dot1dStaticAllowedToGoTo_Type(OctetString):
    """Custom type dot1dStaticAllowedToGoTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Dot1dStaticAllowedToGoTo_Type.__name__ = "OctetString"
_Dot1dStaticAllowedToGoTo_Object = MibTableColumn
dot1dStaticAllowedToGoTo = _Dot1dStaticAllowedToGoTo_Object(
    (1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 3),
    _Dot1dStaticAllowedToGoTo_Type()
)
dot1dStaticAllowedToGoTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1dStaticAllowedToGoTo.setStatus("current")


class _Dot1dStaticStatus_Type(Integer32):
    """Custom type dot1dStaticStatus based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("permanent", 3),
          ("deleteOnReset", 4),
          ("deleteOnTimeout", 5))
    )


_Dot1dStaticStatus_Type.__name__ = "Integer32"
_Dot1dStaticStatus_Object = MibTableColumn
dot1dStaticStatus = _Dot1dStaticStatus_Object(
    (1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 4),
    _Dot1dStaticStatus_Type()
)
dot1dStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1dStaticStatus.setStatus("current")
_Dot1dConformance_ObjectIdentity = ObjectIdentity
dot1dConformance = _Dot1dConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 8)
)
_Dot1dGroups_ObjectIdentity = ObjectIdentity
dot1dGroups = _Dot1dGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 8, 1)
)
_Dot1dCompliances_ObjectIdentity = ObjectIdentity
dot1dCompliances = _Dot1dCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 8, 2)
)

# Managed Objects groups

dot1dBaseBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 8, 1, 1)
)
dot1dBaseBridgeGroup.setObjects(
      *(("BRIDGE-MIB", "dot1dBaseBridgeAddress"),
        ("BRIDGE-MIB", "dot1dBaseNumPorts"),
        ("BRIDGE-MIB", "dot1dBaseType"))
)
if mibBuilder.loadTexts:
    dot1dBaseBridgeGroup.setStatus("current")

dot1dBasePortGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 8, 1, 2)
)
dot1dBasePortGroup.setObjects(
      *(("BRIDGE-MIB", "dot1dBasePort"),
        ("BRIDGE-MIB", "dot1dBasePortIfIndex"),
        ("BRIDGE-MIB", "dot1dBasePortCircuit"),
        ("BRIDGE-MIB", "dot1dBasePortDelayExceededDiscards"),
        ("BRIDGE-MIB", "dot1dBasePortMtuExceededDiscards"))
)
if mibBuilder.loadTexts:
    dot1dBasePortGroup.setStatus("current")

dot1dStpBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 8, 1, 3)
)
dot1dStpBridgeGroup.setObjects(
      *(("BRIDGE-MIB", "dot1dStpProtocolSpecification"),
        ("BRIDGE-MIB", "dot1dStpPriority"),
        ("BRIDGE-MIB", "dot1dStpTimeSinceTopologyChange"),
        ("BRIDGE-MIB", "dot1dStpTopChanges"),
        ("BRIDGE-MIB", "dot1dStpDesignatedRoot"),
        ("BRIDGE-MIB", "dot1dStpRootCost"),
        ("BRIDGE-MIB", "dot1dStpRootPort"),
        ("BRIDGE-MIB", "dot1dStpMaxAge"),
        ("BRIDGE-MIB", "dot1dStpHelloTime"),
        ("BRIDGE-MIB", "dot1dStpHoldTime"),
        ("BRIDGE-MIB", "dot1dStpForwardDelay"),
        ("BRIDGE-MIB", "dot1dStpBridgeMaxAge"),
        ("BRIDGE-MIB", "dot1dStpBridgeHelloTime"),
        ("BRIDGE-MIB", "dot1dStpBridgeForwardDelay"))
)
if mibBuilder.loadTexts:
    dot1dStpBridgeGroup.setStatus("current")

dot1dStpPortGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 8, 1, 4)
)
dot1dStpPortGroup.setObjects(
      *(("BRIDGE-MIB", "dot1dStpPort"),
        ("BRIDGE-MIB", "dot1dStpPortPriority"),
        ("BRIDGE-MIB", "dot1dStpPortState"),
        ("BRIDGE-MIB", "dot1dStpPortEnable"),
        ("BRIDGE-MIB", "dot1dStpPortPathCost"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedRoot"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedCost"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedBridge"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedPort"),
        ("BRIDGE-MIB", "dot1dStpPortForwardTransitions"))
)
if mibBuilder.loadTexts:
    dot1dStpPortGroup.setStatus("current")

dot1dStpPortGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 8, 1, 5)
)
dot1dStpPortGroup2.setObjects(
      *(("BRIDGE-MIB", "dot1dStpPort"),
        ("BRIDGE-MIB", "dot1dStpPortPriority"),
        ("BRIDGE-MIB", "dot1dStpPortState"),
        ("BRIDGE-MIB", "dot1dStpPortEnable"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedRoot"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedCost"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedBridge"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedPort"),
        ("BRIDGE-MIB", "dot1dStpPortForwardTransitions"),
        ("BRIDGE-MIB", "dot1dStpPortPathCost32"))
)
if mibBuilder.loadTexts:
    dot1dStpPortGroup2.setStatus("current")

dot1dStpPortGroup3 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 8, 1, 6)
)
dot1dStpPortGroup3.setObjects(
    ("BRIDGE-MIB", "dot1dStpPortPathCost32")
)
if mibBuilder.loadTexts:
    dot1dStpPortGroup3.setStatus("current")

dot1dTpBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 8, 1, 7)
)
dot1dTpBridgeGroup.setObjects(
      *(("BRIDGE-MIB", "dot1dTpLearnedEntryDiscards"),
        ("BRIDGE-MIB", "dot1dTpAgingTime"))
)
if mibBuilder.loadTexts:
    dot1dTpBridgeGroup.setStatus("current")

dot1dTpFdbGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 8, 1, 8)
)
dot1dTpFdbGroup.setObjects(
      *(("BRIDGE-MIB", "dot1dTpFdbAddress"),
        ("BRIDGE-MIB", "dot1dTpFdbPort"),
        ("BRIDGE-MIB", "dot1dTpFdbStatus"))
)
if mibBuilder.loadTexts:
    dot1dTpFdbGroup.setStatus("current")

dot1dTpGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 8, 1, 9)
)
dot1dTpGroup.setObjects(
      *(("BRIDGE-MIB", "dot1dTpPort"),
        ("BRIDGE-MIB", "dot1dTpPortMaxInfo"),
        ("BRIDGE-MIB", "dot1dTpPortInFrames"),
        ("BRIDGE-MIB", "dot1dTpPortOutFrames"),
        ("BRIDGE-MIB", "dot1dTpPortInDiscards"))
)
if mibBuilder.loadTexts:
    dot1dTpGroup.setStatus("current")

dot1dStaticGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 8, 1, 10)
)
dot1dStaticGroup.setObjects(
      *(("BRIDGE-MIB", "dot1dStaticAddress"),
        ("BRIDGE-MIB", "dot1dStaticReceivePort"),
        ("BRIDGE-MIB", "dot1dStaticAllowedToGoTo"),
        ("BRIDGE-MIB", "dot1dStaticStatus"))
)
if mibBuilder.loadTexts:
    dot1dStaticGroup.setStatus("current")


# Notification objects

newRoot = NotificationType(
    (1, 3, 6, 1, 2, 1, 17, 0, 1)
)
if mibBuilder.loadTexts:
    newRoot.setStatus(
        "current"
    )

topologyChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 17, 0, 2)
)
if mibBuilder.loadTexts:
    topologyChange.setStatus(
        "current"
    )


# Notifications groups

dot1dNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 17, 8, 1, 11)
)
dot1dNotificationGroup.setObjects(
      *(("BRIDGE-MIB", "newRoot"),
        ("BRIDGE-MIB", "topologyChange"))
)
if mibBuilder.loadTexts:
    dot1dNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bridgeCompliance1493 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 17, 8, 2, 1)
)
bridgeCompliance1493.setObjects(
      *(("BRIDGE-MIB", "dot1dBaseBridgeGroup"),
        ("BRIDGE-MIB", "dot1dBasePortGroup"),
        ("BRIDGE-MIB", "dot1dStpBridgeGroup"),
        ("BRIDGE-MIB", "dot1dStpPortGroup"),
        ("BRIDGE-MIB", "dot1dTpBridgeGroup"),
        ("BRIDGE-MIB", "dot1dTpFdbGroup"),
        ("BRIDGE-MIB", "dot1dTpGroup"),
        ("BRIDGE-MIB", "dot1dStaticGroup"),
        ("BRIDGE-MIB", "dot1dNotificationGroup"))
)
if mibBuilder.loadTexts:
    bridgeCompliance1493.setStatus(
        "current"
    )

bridgeCompliance4188 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 17, 8, 2, 2)
)
bridgeCompliance4188.setObjects(
      *(("BRIDGE-MIB", "dot1dBaseBridgeGroup"),
        ("BRIDGE-MIB", "dot1dBasePortGroup"),
        ("BRIDGE-MIB", "dot1dStpBridgeGroup"),
        ("BRIDGE-MIB", "dot1dStpPortGroup2"),
        ("BRIDGE-MIB", "dot1dStpPortGroup3"),
        ("BRIDGE-MIB", "dot1dTpBridgeGroup"),
        ("BRIDGE-MIB", "dot1dTpFdbGroup"),
        ("BRIDGE-MIB", "dot1dTpGroup"),
        ("BRIDGE-MIB", "dot1dStaticGroup"),
        ("BRIDGE-MIB", "dot1dNotificationGroup"))
)
if mibBuilder.loadTexts:
    bridgeCompliance4188.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRIDGE-MIB",
    **{"BridgeId": BridgeId,
       "Timeout": Timeout,
       "dot1dBridge": dot1dBridge,
       "dot1dNotifications": dot1dNotifications,
       "newRoot": newRoot,
       "topologyChange": topologyChange,
       "dot1dBase": dot1dBase,
       "dot1dBaseBridgeAddress": dot1dBaseBridgeAddress,
       "dot1dBaseNumPorts": dot1dBaseNumPorts,
       "dot1dBaseType": dot1dBaseType,
       "dot1dBasePortTable": dot1dBasePortTable,
       "dot1dBasePortEntry": dot1dBasePortEntry,
       "dot1dBasePort": dot1dBasePort,
       "dot1dBasePortIfIndex": dot1dBasePortIfIndex,
       "dot1dBasePortCircuit": dot1dBasePortCircuit,
       "dot1dBasePortDelayExceededDiscards": dot1dBasePortDelayExceededDiscards,
       "dot1dBasePortMtuExceededDiscards": dot1dBasePortMtuExceededDiscards,
       "dot1dStp": dot1dStp,
       "dot1dStpProtocolSpecification": dot1dStpProtocolSpecification,
       "dot1dStpPriority": dot1dStpPriority,
       "dot1dStpTimeSinceTopologyChange": dot1dStpTimeSinceTopologyChange,
       "dot1dStpTopChanges": dot1dStpTopChanges,
       "dot1dStpDesignatedRoot": dot1dStpDesignatedRoot,
       "dot1dStpRootCost": dot1dStpRootCost,
       "dot1dStpRootPort": dot1dStpRootPort,
       "dot1dStpMaxAge": dot1dStpMaxAge,
       "dot1dStpHelloTime": dot1dStpHelloTime,
       "dot1dStpHoldTime": dot1dStpHoldTime,
       "dot1dStpForwardDelay": dot1dStpForwardDelay,
       "dot1dStpBridgeMaxAge": dot1dStpBridgeMaxAge,
       "dot1dStpBridgeHelloTime": dot1dStpBridgeHelloTime,
       "dot1dStpBridgeForwardDelay": dot1dStpBridgeForwardDelay,
       "dot1dStpPortTable": dot1dStpPortTable,
       "dot1dStpPortEntry": dot1dStpPortEntry,
       "dot1dStpPort": dot1dStpPort,
       "dot1dStpPortPriority": dot1dStpPortPriority,
       "dot1dStpPortState": dot1dStpPortState,
       "dot1dStpPortEnable": dot1dStpPortEnable,
       "dot1dStpPortPathCost": dot1dStpPortPathCost,
       "dot1dStpPortDesignatedRoot": dot1dStpPortDesignatedRoot,
       "dot1dStpPortDesignatedCost": dot1dStpPortDesignatedCost,
       "dot1dStpPortDesignatedBridge": dot1dStpPortDesignatedBridge,
       "dot1dStpPortDesignatedPort": dot1dStpPortDesignatedPort,
       "dot1dStpPortForwardTransitions": dot1dStpPortForwardTransitions,
       "dot1dStpPortPathCost32": dot1dStpPortPathCost32,
       "dot1dSr": dot1dSr,
       "dot1dTp": dot1dTp,
       "dot1dTpLearnedEntryDiscards": dot1dTpLearnedEntryDiscards,
       "dot1dTpAgingTime": dot1dTpAgingTime,
       "dot1dTpFdbTable": dot1dTpFdbTable,
       "dot1dTpFdbEntry": dot1dTpFdbEntry,
       "dot1dTpFdbAddress": dot1dTpFdbAddress,
       "dot1dTpFdbPort": dot1dTpFdbPort,
       "dot1dTpFdbStatus": dot1dTpFdbStatus,
       "dot1dTpPortTable": dot1dTpPortTable,
       "dot1dTpPortEntry": dot1dTpPortEntry,
       "dot1dTpPort": dot1dTpPort,
       "dot1dTpPortMaxInfo": dot1dTpPortMaxInfo,
       "dot1dTpPortInFrames": dot1dTpPortInFrames,
       "dot1dTpPortOutFrames": dot1dTpPortOutFrames,
       "dot1dTpPortInDiscards": dot1dTpPortInDiscards,
       "dot1dStatic": dot1dStatic,
       "dot1dStaticTable": dot1dStaticTable,
       "dot1dStaticEntry": dot1dStaticEntry,
       "dot1dStaticAddress": dot1dStaticAddress,
       "dot1dStaticReceivePort": dot1dStaticReceivePort,
       "dot1dStaticAllowedToGoTo": dot1dStaticAllowedToGoTo,
       "dot1dStaticStatus": dot1dStaticStatus,
       "dot1dConformance": dot1dConformance,
       "dot1dGroups": dot1dGroups,
       "dot1dBaseBridgeGroup": dot1dBaseBridgeGroup,
       "dot1dBasePortGroup": dot1dBasePortGroup,
       "dot1dStpBridgeGroup": dot1dStpBridgeGroup,
       "dot1dStpPortGroup": dot1dStpPortGroup,
       "dot1dStpPortGroup2": dot1dStpPortGroup2,
       "dot1dStpPortGroup3": dot1dStpPortGroup3,
       "dot1dTpBridgeGroup": dot1dTpBridgeGroup,
       "dot1dTpFdbGroup": dot1dTpFdbGroup,
       "dot1dTpGroup": dot1dTpGroup,
       "dot1dStaticGroup": dot1dStaticGroup,
       "dot1dNotificationGroup": dot1dNotificationGroup,
       "dot1dCompliances": dot1dCompliances,
       "bridgeCompliance1493": bridgeCompliance1493,
       "bridgeCompliance4188": bridgeCompliance4188}
)
