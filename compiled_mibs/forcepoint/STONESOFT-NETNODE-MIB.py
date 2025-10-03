# SNMP MIB module (STONESOFT-NETNODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\forcepoint\STONESOFT-NETNODE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:42 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")

(stonesoftModules,
 stonesoftNetworkNode) = mibBuilder.importSymbols(
    "STONESOFT-SMI-MIB",
    "stonesoftModules",
    "stonesoftNetworkNode")


# MODULE-IDENTITY

stonesoftNetworkNodeMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 3, 4)
)
if mibBuilder.loadTexts:
    stonesoftNetworkNodeMibModule.setRevisions(
        ("2016-05-06 00:00",
         "2015-10-29 00:00",
         "2015-10-15 00:00",
         "2014-03-10 00:00",
         "2008-02-04 00:00",
         "2004-06-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetNodeObjects_ObjectIdentity = ObjectIdentity
netNodeObjects = _NetNodeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1)
)


class _NodeClusterId_Type(Integer32):
    """Custom type nodeClusterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NodeClusterId_Type.__name__ = "Integer32"
_NodeClusterId_Object = MibScalar
nodeClusterId = _NodeClusterId_Object(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1, 1),
    _NodeClusterId_Type()
)
nodeClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeClusterId.setStatus("current")


class _NodeMemberId_Type(Integer32):
    """Custom type nodeMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NodeMemberId_Type.__name__ = "Integer32"
_NodeMemberId_Object = MibScalar
nodeMemberId = _NodeMemberId_Object(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1, 2),
    _NodeMemberId_Type()
)
nodeMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeMemberId.setStatus("current")


class _NodeOperState_Type(Integer32):
    """Custom type nodeOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("online", 1),
          ("goingOnline", 2),
          ("lockedOnline", 3),
          ("goingLockedOnline", 4),
          ("offline", 5),
          ("goingOffline", 6),
          ("lockedOffline", 7),
          ("goingLockedOffline", 8),
          ("standby", 9),
          ("goingStandby", 10))
    )


_NodeOperState_Type.__name__ = "Integer32"
_NodeOperState_Object = MibScalar
nodeOperState = _NodeOperState_Object(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1, 3),
    _NodeOperState_Type()
)
nodeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeOperState.setStatus("current")


class _NodeCPULoad_Type(Integer32):
    """Custom type nodeCPULoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NodeCPULoad_Type.__name__ = "Integer32"
_NodeCPULoad_Object = MibScalar
nodeCPULoad = _NodeCPULoad_Object(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1, 4),
    _NodeCPULoad_Type()
)
nodeCPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeCPULoad.setStatus("current")
_NodeLastLogin_Type = DisplayString
_NodeLastLogin_Object = MibScalar
nodeLastLogin = _NodeLastLogin_Object(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1, 5),
    _NodeLastLogin_Type()
)
nodeLastLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeLastLogin.setStatus("current")
_NodeLastLoginTime_Type = TimeStamp
_NodeLastLoginTime_Object = MibScalar
nodeLastLoginTime = _NodeLastLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1, 6),
    _NodeLastLoginTime_Type()
)
nodeLastLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeLastLoginTime.setStatus("current")
_NodeTestTable_Object = MibTable
nodeTestTable = _NodeTestTable_Object(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1, 7)
)
if mibBuilder.loadTexts:
    nodeTestTable.setStatus("current")
_NodeTestEntry_Object = MibTableRow
nodeTestEntry = _NodeTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1, 7, 1)
)
nodeTestEntry.setIndexNames(
    (0, "STONESOFT-NETNODE-MIB", "nodeTestIndex"),
)
if mibBuilder.loadTexts:
    nodeTestEntry.setStatus("current")


class _NodeTestIndex_Type(Unsigned32):
    """Custom type nodeTestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NodeTestIndex_Type.__name__ = "Unsigned32"
_NodeTestIndex_Object = MibTableColumn
nodeTestIndex = _NodeTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1, 7, 1, 1),
    _NodeTestIndex_Type()
)
nodeTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nodeTestIndex.setStatus("current")
_NodeTestIdentity_Type = DisplayString
_NodeTestIdentity_Object = MibTableColumn
nodeTestIdentity = _NodeTestIdentity_Object(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1, 7, 1, 2),
    _NodeTestIdentity_Type()
)
nodeTestIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeTestIdentity.setStatus("current")


class _NodeTestResult_Type(Integer32):
    """Custom type nodeTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failure", 2))
    )


_NodeTestResult_Type.__name__ = "Integer32"
_NodeTestResult_Object = MibTableColumn
nodeTestResult = _NodeTestResult_Object(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1, 7, 1, 3),
    _NodeTestResult_Type()
)
nodeTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeTestResult.setStatus("current")
_NodeTestResultTime_Type = TimeStamp
_NodeTestResultTime_Object = MibTableColumn
nodeTestResultTime = _NodeTestResultTime_Object(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1, 7, 1, 4),
    _NodeTestResultTime_Type()
)
nodeTestResultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeTestResultTime.setStatus("current")
_NodeHwmonEvent_Type = DisplayString
_NodeHwmonEvent_Object = MibScalar
nodeHwmonEvent = _NodeHwmonEvent_Object(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1, 8),
    _NodeHwmonEvent_Type()
)
nodeHwmonEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeHwmonEvent.setStatus("current")
_NodeApplianceModel_Type = DisplayString
_NodeApplianceModel_Object = MibScalar
nodeApplianceModel = _NodeApplianceModel_Object(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1, 9),
    _NodeApplianceModel_Type()
)
nodeApplianceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeApplianceModel.setStatus("current")
_NodeSerialNumber_Type = DisplayString
_NodeSerialNumber_Object = MibScalar
nodeSerialNumber = _NodeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1, 10),
    _NodeSerialNumber_Type()
)
nodeSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSerialNumber.setStatus("current")
_NodePosCode_Type = DisplayString
_NodePosCode_Object = MibScalar
nodePosCode = _NodePosCode_Object(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1, 11),
    _NodePosCode_Type()
)
nodePosCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePosCode.setStatus("current")
_NodeLoginTime_Type = DateAndTime
_NodeLoginTime_Object = MibScalar
nodeLoginTime = _NodeLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1, 12),
    _NodeLoginTime_Type()
)
nodeLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeLoginTime.setStatus("current")
_NodePolicyApplyTime_Type = DateAndTime
_NodePolicyApplyTime_Object = MibScalar
nodePolicyApplyTime = _NodePolicyApplyTime_Object(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 1, 13),
    _NodePolicyApplyTime_Type()
)
nodePolicyApplyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePolicyApplyTime.setStatus("current")
_NetNodeEvents_ObjectIdentity = ObjectIdentity
netNodeEvents = _NetNodeEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 2)
)
_NetNodeEventsV2_ObjectIdentity = ObjectIdentity
netNodeEventsV2 = _NetNodeEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 2, 0)
)
_NetNodeConformance_ObjectIdentity = ObjectIdentity
netNodeConformance = _NetNodeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 3)
)
_NetNodeGroups_ObjectIdentity = ObjectIdentity
netNodeGroups = _NetNodeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 3, 1)
)
_NetNodeCompliances_ObjectIdentity = ObjectIdentity
netNodeCompliances = _NetNodeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 3, 2)
)

# Managed Objects groups

nodeIdentificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 3, 1, 1)
)
nodeIdentificationGroup.setObjects(
      *(("STONESOFT-NETNODE-MIB", "nodeClusterId"),
        ("STONESOFT-NETNODE-MIB", "nodeMemberId"),
        ("STONESOFT-NETNODE-MIB", "nodeApplianceModel"),
        ("STONESOFT-NETNODE-MIB", "nodeSerialNumber"),
        ("STONESOFT-NETNODE-MIB", "nodePosCode"))
)
if mibBuilder.loadTexts:
    nodeIdentificationGroup.setStatus("current")

nodeStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 3, 1, 2)
)
nodeStatusGroup.setObjects(
      *(("STONESOFT-NETNODE-MIB", "nodeOperState"),
        ("STONESOFT-NETNODE-MIB", "nodeCPULoad"),
        ("STONESOFT-NETNODE-MIB", "nodePolicyApplyTime"))
)
if mibBuilder.loadTexts:
    nodeStatusGroup.setStatus("current")

nodeLoginGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 3, 1, 3)
)
nodeLoginGroup.setObjects(
      *(("STONESOFT-NETNODE-MIB", "nodeLastLogin"),
        ("STONESOFT-NETNODE-MIB", "nodeLastLoginTime"),
        ("STONESOFT-NETNODE-MIB", "nodeLoginTime"))
)
if mibBuilder.loadTexts:
    nodeLoginGroup.setStatus("current")

nodeTesterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 3, 1, 4)
)
nodeTesterGroup.setObjects(
      *(("STONESOFT-NETNODE-MIB", "nodeTestIdentity"),
        ("STONESOFT-NETNODE-MIB", "nodeTestResult"),
        ("STONESOFT-NETNODE-MIB", "nodeTestResultTime"))
)
if mibBuilder.loadTexts:
    nodeTesterGroup.setStatus("current")

nodeHwmonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 3, 1, 8)
)
nodeHwmonGroup.setObjects(
    ("STONESOFT-NETNODE-MIB", "nodeHwmonEvent")
)
if mibBuilder.loadTexts:
    nodeHwmonGroup.setStatus("current")


# Notification objects

nodeOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 2, 0, 1)
)
nodeOnline.setObjects(
    ("STONESOFT-NETNODE-MIB", "nodeOperState")
)
if mibBuilder.loadTexts:
    nodeOnline.setStatus(
        "current"
    )

nodeOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 2, 0, 2)
)
nodeOffline.setObjects(
    ("STONESOFT-NETNODE-MIB", "nodeOperState")
)
if mibBuilder.loadTexts:
    nodeOffline.setStatus(
        "current"
    )

nodeBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 2, 0, 3)
)
if mibBuilder.loadTexts:
    nodeBoot.setStatus(
        "current"
    )

nodeShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 2, 0, 4)
)
if mibBuilder.loadTexts:
    nodeShutdown.setStatus(
        "current"
    )

nodeUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 2, 0, 5)
)
nodeUserLogin.setObjects(
    ("STONESOFT-NETNODE-MIB", "nodeLastLogin")
)
if mibBuilder.loadTexts:
    nodeUserLogin.setStatus(
        "current"
    )

nodeTestFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 2, 0, 6)
)
nodeTestFailure.setObjects(
    ("STONESOFT-NETNODE-MIB", "nodeTestIdentity")
)
if mibBuilder.loadTexts:
    nodeTestFailure.setStatus(
        "current"
    )

nodeHwmon = NotificationType(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 2, 0, 7)
)
nodeHwmon.setObjects(
    ("STONESOFT-NETNODE-MIB", "nodeHwmonEvent")
)
if mibBuilder.loadTexts:
    nodeHwmon.setStatus(
        "current"
    )

nodeFailedUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 2, 0, 8)
)
if mibBuilder.loadTexts:
    nodeFailedUserLogin.setStatus(
        "current"
    )

nodeUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 2, 0, 9)
)
if mibBuilder.loadTexts:
    nodeUserLogout.setStatus(
        "current"
    )


# Notifications groups

nodeStatusNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 3, 1, 5)
)
nodeStatusNotificationsGroup.setObjects(
      *(("STONESOFT-NETNODE-MIB", "nodeOnline"),
        ("STONESOFT-NETNODE-MIB", "nodeOffline"),
        ("STONESOFT-NETNODE-MIB", "nodeBoot"),
        ("STONESOFT-NETNODE-MIB", "nodeShutdown"))
)
if mibBuilder.loadTexts:
    nodeStatusNotificationsGroup.setStatus(
        "current"
    )

nodeLoginNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 3, 1, 6)
)
nodeLoginNotificationsGroup.setObjects(
      *(("STONESOFT-NETNODE-MIB", "nodeUserLogin"),
        ("STONESOFT-NETNODE-MIB", "nodeFailedUserLogin"),
        ("STONESOFT-NETNODE-MIB", "nodeUserLogout"))
)
if mibBuilder.loadTexts:
    nodeLoginNotificationsGroup.setStatus(
        "current"
    )

nodeTesterNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 3, 1, 7)
)
nodeTesterNotificationsGroup.setObjects(
    ("STONESOFT-NETNODE-MIB", "nodeTestFailure")
)
if mibBuilder.loadTexts:
    nodeTesterNotificationsGroup.setStatus(
        "current"
    )

nodeHwmonNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 3, 1, 9)
)
nodeHwmonNotificationsGroup.setObjects(
    ("STONESOFT-NETNODE-MIB", "nodeHwmon")
)
if mibBuilder.loadTexts:
    nodeHwmonNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

nodeCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1, 3, 2, 1)
)
nodeCompliance1.setObjects(
      *(("STONESOFT-NETNODE-MIB", "nodeStatusGroup"),
        ("STONESOFT-NETNODE-MIB", "nodeStatusNotificationsGroup"),
        ("STONESOFT-NETNODE-MIB", "nodeIdentificationGroup"),
        ("STONESOFT-NETNODE-MIB", "nodeLoginGroup"),
        ("STONESOFT-NETNODE-MIB", "nodeLoginNotificationsGroup"),
        ("STONESOFT-NETNODE-MIB", "nodeTesterGroup"),
        ("STONESOFT-NETNODE-MIB", "nodeTesterNotificationsGroup"),
        ("STONESOFT-NETNODE-MIB", "nodeHwmonGroup"),
        ("STONESOFT-NETNODE-MIB", "nodeHwmonNotificationsGroup"))
)
if mibBuilder.loadTexts:
    nodeCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STONESOFT-NETNODE-MIB",
    **{"stonesoftNetworkNodeMibModule": stonesoftNetworkNodeMibModule,
       "netNodeObjects": netNodeObjects,
       "nodeClusterId": nodeClusterId,
       "nodeMemberId": nodeMemberId,
       "nodeOperState": nodeOperState,
       "nodeCPULoad": nodeCPULoad,
       "nodeLastLogin": nodeLastLogin,
       "nodeLastLoginTime": nodeLastLoginTime,
       "nodeTestTable": nodeTestTable,
       "nodeTestEntry": nodeTestEntry,
       "nodeTestIndex": nodeTestIndex,
       "nodeTestIdentity": nodeTestIdentity,
       "nodeTestResult": nodeTestResult,
       "nodeTestResultTime": nodeTestResultTime,
       "nodeHwmonEvent": nodeHwmonEvent,
       "nodeApplianceModel": nodeApplianceModel,
       "nodeSerialNumber": nodeSerialNumber,
       "nodePosCode": nodePosCode,
       "nodeLoginTime": nodeLoginTime,
       "nodePolicyApplyTime": nodePolicyApplyTime,
       "netNodeEvents": netNodeEvents,
       "netNodeEventsV2": netNodeEventsV2,
       "nodeOnline": nodeOnline,
       "nodeOffline": nodeOffline,
       "nodeBoot": nodeBoot,
       "nodeShutdown": nodeShutdown,
       "nodeUserLogin": nodeUserLogin,
       "nodeTestFailure": nodeTestFailure,
       "nodeHwmon": nodeHwmon,
       "nodeFailedUserLogin": nodeFailedUserLogin,
       "nodeUserLogout": nodeUserLogout,
       "netNodeConformance": netNodeConformance,
       "netNodeGroups": netNodeGroups,
       "nodeIdentificationGroup": nodeIdentificationGroup,
       "nodeStatusGroup": nodeStatusGroup,
       "nodeLoginGroup": nodeLoginGroup,
       "nodeTesterGroup": nodeTesterGroup,
       "nodeStatusNotificationsGroup": nodeStatusNotificationsGroup,
       "nodeLoginNotificationsGroup": nodeLoginNotificationsGroup,
       "nodeTesterNotificationsGroup": nodeTesterNotificationsGroup,
       "nodeHwmonGroup": nodeHwmonGroup,
       "nodeHwmonNotificationsGroup": nodeHwmonNotificationsGroup,
       "netNodeCompliances": netNodeCompliances,
       "nodeCompliance1": nodeCompliance1}
)
