# SNMP MIB module (SLE-PPPOE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-PPPOE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:57 2025
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

(sleMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleMgmt")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

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

slePppoe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlePppoeBase_ObjectIdentity = ObjectIdentity
slePppoeBase = _SlePppoeBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 1)
)
_SlePppoeIntermediateAgent_ObjectIdentity = ObjectIdentity
slePppoeIntermediateAgent = _SlePppoeIntermediateAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2)
)
_SlePpppoeIABaseInfo_ObjectIdentity = ObjectIdentity
slePpppoeIABaseInfo = _SlePpppoeIABaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 1)
)


class _SlePpppoeIAEnableStatus_Type(Integer32):
    """Custom type slePpppoeIAEnableStatus based on Integer32"""
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


_SlePpppoeIAEnableStatus_Type.__name__ = "Integer32"
_SlePpppoeIAEnableStatus_Object = MibScalar
slePpppoeIAEnableStatus = _SlePpppoeIAEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 1, 1),
    _SlePpppoeIAEnableStatus_Type()
)
slePpppoeIAEnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePpppoeIAEnableStatus.setStatus("current")
_SlePpppoeIAAccessNode_Type = OctetString
_SlePpppoeIAAccessNode_Object = MibScalar
slePpppoeIAAccessNode = _SlePpppoeIAAccessNode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 1, 2),
    _SlePpppoeIAAccessNode_Type()
)
slePpppoeIAAccessNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePpppoeIAAccessNode.setStatus("current")
_SlePpppoeIACircuitId_Type = OctetString
_SlePpppoeIACircuitId_Object = MibScalar
slePpppoeIACircuitId = _SlePpppoeIACircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 1, 3),
    _SlePpppoeIACircuitId_Type()
)
slePpppoeIACircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePpppoeIACircuitId.setStatus("current")
_SlePpppoeIARemoteId_Type = OctetString
_SlePpppoeIARemoteId_Object = MibScalar
slePpppoeIARemoteId = _SlePpppoeIARemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 1, 4),
    _SlePpppoeIARemoteId_Type()
)
slePpppoeIARemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePpppoeIARemoteId.setStatus("current")
_SlePpppoeIAControl_ObjectIdentity = ObjectIdentity
slePpppoeIAControl = _SlePpppoeIAControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 2)
)


class _SlePpppoeIAControlRequest_Type(Integer32):
    """Custom type slePpppoeIAControlRequest based on Integer32"""
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
        *(("setIntermediateAgentEnableStatus", 1),
          ("setFormatTypeAccessnodeId", 2),
          ("setFormatTypeCircuitId", 3),
          ("setFormatTypeRemoteId", 4))
    )


_SlePpppoeIAControlRequest_Type.__name__ = "Integer32"
_SlePpppoeIAControlRequest_Object = MibScalar
slePpppoeIAControlRequest = _SlePpppoeIAControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 2, 1),
    _SlePpppoeIAControlRequest_Type()
)
slePpppoeIAControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePpppoeIAControlRequest.setStatus("current")
_SlePpppoeIAControlStatus_Type = SleControlStatusType
_SlePpppoeIAControlStatus_Object = MibScalar
slePpppoeIAControlStatus = _SlePpppoeIAControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 2, 2),
    _SlePpppoeIAControlStatus_Type()
)
slePpppoeIAControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePpppoeIAControlStatus.setStatus("current")
_SlePpppoeIAControlTimer_Type = Gauge32
_SlePpppoeIAControlTimer_Object = MibScalar
slePpppoeIAControlTimer = _SlePpppoeIAControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 2, 3),
    _SlePpppoeIAControlTimer_Type()
)
slePpppoeIAControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePpppoeIAControlTimer.setStatus("current")
_SlePpppoeIAControlTimeStamp_Type = TimeTicks
_SlePpppoeIAControlTimeStamp_Object = MibScalar
slePpppoeIAControlTimeStamp = _SlePpppoeIAControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 2, 4),
    _SlePpppoeIAControlTimeStamp_Type()
)
slePpppoeIAControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePpppoeIAControlTimeStamp.setStatus("current")
_SlePpppoeIAControlReqResult_Type = SleControlRequestResultType
_SlePpppoeIAControlReqResult_Object = MibScalar
slePpppoeIAControlReqResult = _SlePpppoeIAControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 2, 5),
    _SlePpppoeIAControlReqResult_Type()
)
slePpppoeIAControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePpppoeIAControlReqResult.setStatus("current")


class _SlePpppoeIAControlEnableStatus_Type(Integer32):
    """Custom type slePpppoeIAControlEnableStatus based on Integer32"""
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


_SlePpppoeIAControlEnableStatus_Type.__name__ = "Integer32"
_SlePpppoeIAControlEnableStatus_Object = MibScalar
slePpppoeIAControlEnableStatus = _SlePpppoeIAControlEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 2, 6),
    _SlePpppoeIAControlEnableStatus_Type()
)
slePpppoeIAControlEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePpppoeIAControlEnableStatus.setStatus("current")
_SlePpppoeIAControlAccessNode_Type = OctetString
_SlePpppoeIAControlAccessNode_Object = MibScalar
slePpppoeIAControlAccessNode = _SlePpppoeIAControlAccessNode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 2, 7),
    _SlePpppoeIAControlAccessNode_Type()
)
slePpppoeIAControlAccessNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePpppoeIAControlAccessNode.setStatus("current")
_SlePpppoeIAControlCircuitId_Type = OctetString
_SlePpppoeIAControlCircuitId_Object = MibScalar
slePpppoeIAControlCircuitId = _SlePpppoeIAControlCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 2, 8),
    _SlePpppoeIAControlCircuitId_Type()
)
slePpppoeIAControlCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePpppoeIAControlCircuitId.setStatus("current")
_SlePpppoeIAControlRemoteId_Type = OctetString
_SlePpppoeIAControlRemoteId_Object = MibScalar
slePpppoeIAControlRemoteId = _SlePpppoeIAControlRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 2, 9),
    _SlePpppoeIAControlRemoteId_Type()
)
slePpppoeIAControlRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePpppoeIAControlRemoteId.setStatus("current")
_SlePpppoeIANotification_ObjectIdentity = ObjectIdentity
slePpppoeIANotification = _SlePpppoeIANotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 3)
)

# Managed Objects groups

slePppoeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 3)
)
slePppoeGroup.setObjects(
      *(("SLE-PPPOE-MIB", "slePpppoeIAEnableStatus"),
        ("SLE-PPPOE-MIB", "slePpppoeIAAccessNode"),
        ("SLE-PPPOE-MIB", "slePpppoeIACircuitId"),
        ("SLE-PPPOE-MIB", "slePpppoeIARemoteId"),
        ("SLE-PPPOE-MIB", "slePpppoeIAControlRequest"),
        ("SLE-PPPOE-MIB", "slePpppoeIAControlStatus"),
        ("SLE-PPPOE-MIB", "slePpppoeIAControlTimer"),
        ("SLE-PPPOE-MIB", "slePpppoeIAControlTimeStamp"),
        ("SLE-PPPOE-MIB", "slePpppoeIAControlReqResult"),
        ("SLE-PPPOE-MIB", "slePpppoeIAControlEnableStatus"),
        ("SLE-PPPOE-MIB", "slePpppoeIAControlAccessNode"),
        ("SLE-PPPOE-MIB", "slePpppoeIAControlCircuitId"),
        ("SLE-PPPOE-MIB", "slePpppoeIAControlRemoteId"))
)
if mibBuilder.loadTexts:
    slePppoeGroup.setStatus("current")


# Notification objects

slePpppoeIAEnableStatuschanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 3, 1)
)
slePpppoeIAEnableStatuschanged.setObjects(
      *(("SLE-PPPOE-MIB", "slePpppoeIAControlRequest"),
        ("SLE-PPPOE-MIB", "slePpppoeIAControlTimeStamp"),
        ("SLE-PPPOE-MIB", "slePpppoeIAControlEnableStatus"))
)
if mibBuilder.loadTexts:
    slePpppoeIAEnableStatuschanged.setStatus(
        "current"
    )

slePpppoeIAAccessnodeIdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 3, 2)
)
slePpppoeIAAccessnodeIdChanged.setObjects(
      *(("SLE-PPPOE-MIB", "slePpppoeIAControlRequest"),
        ("SLE-PPPOE-MIB", "slePpppoeIAControlTimeStamp"),
        ("SLE-PPPOE-MIB", "slePpppoeIAControlAccessNode"))
)
if mibBuilder.loadTexts:
    slePpppoeIAAccessnodeIdChanged.setStatus(
        "current"
    )

slePpppoeIACircuitIdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 3, 3)
)
slePpppoeIACircuitIdChanged.setObjects(
      *(("SLE-PPPOE-MIB", "slePpppoeIAControlRequest"),
        ("SLE-PPPOE-MIB", "slePpppoeIAControlTimeStamp"),
        ("SLE-PPPOE-MIB", "slePpppoeIAControlCircuitId"))
)
if mibBuilder.loadTexts:
    slePpppoeIACircuitIdChanged.setStatus(
        "current"
    )

slePpppoeIARemoteIdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 2, 3, 4)
)
slePpppoeIARemoteIdChanged.setObjects(
      *(("SLE-PPPOE-MIB", "slePpppoeIAControlRequest"),
        ("SLE-PPPOE-MIB", "slePpppoeIAControlTimeStamp"),
        ("SLE-PPPOE-MIB", "slePpppoeIAControlRemoteId"))
)
if mibBuilder.loadTexts:
    slePpppoeIARemoteIdChanged.setStatus(
        "current"
    )


# Notifications groups

slePppoeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 24, 4)
)
slePppoeNotificationGroup.setObjects(
      *(("SLE-PPPOE-MIB", "slePpppoeIAEnableStatuschanged"),
        ("SLE-PPPOE-MIB", "slePpppoeIAAccessnodeIdChanged"),
        ("SLE-PPPOE-MIB", "slePpppoeIACircuitIdChanged"),
        ("SLE-PPPOE-MIB", "slePpppoeIARemoteIdChanged"))
)
if mibBuilder.loadTexts:
    slePppoeNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-PPPOE-MIB",
    **{"slePppoe": slePppoe,
       "slePppoeBase": slePppoeBase,
       "slePppoeIntermediateAgent": slePppoeIntermediateAgent,
       "slePpppoeIABaseInfo": slePpppoeIABaseInfo,
       "slePpppoeIAEnableStatus": slePpppoeIAEnableStatus,
       "slePpppoeIAAccessNode": slePpppoeIAAccessNode,
       "slePpppoeIACircuitId": slePpppoeIACircuitId,
       "slePpppoeIARemoteId": slePpppoeIARemoteId,
       "slePpppoeIAControl": slePpppoeIAControl,
       "slePpppoeIAControlRequest": slePpppoeIAControlRequest,
       "slePpppoeIAControlStatus": slePpppoeIAControlStatus,
       "slePpppoeIAControlTimer": slePpppoeIAControlTimer,
       "slePpppoeIAControlTimeStamp": slePpppoeIAControlTimeStamp,
       "slePpppoeIAControlReqResult": slePpppoeIAControlReqResult,
       "slePpppoeIAControlEnableStatus": slePpppoeIAControlEnableStatus,
       "slePpppoeIAControlAccessNode": slePpppoeIAControlAccessNode,
       "slePpppoeIAControlCircuitId": slePpppoeIAControlCircuitId,
       "slePpppoeIAControlRemoteId": slePpppoeIAControlRemoteId,
       "slePpppoeIANotification": slePpppoeIANotification,
       "slePpppoeIAEnableStatuschanged": slePpppoeIAEnableStatuschanged,
       "slePpppoeIAAccessnodeIdChanged": slePpppoeIAAccessnodeIdChanged,
       "slePpppoeIACircuitIdChanged": slePpppoeIACircuitIdChanged,
       "slePpppoeIARemoteIdChanged": slePpppoeIARemoteIdChanged,
       "slePppoeGroup": slePppoeGroup,
       "slePppoeNotificationGroup": slePppoeNotificationGroup}
)
