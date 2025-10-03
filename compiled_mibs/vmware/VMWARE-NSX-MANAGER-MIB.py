# SNMP MIB module (VMWARE-NSX-MANAGER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vmware\VMWARE-NSX-MANAGER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:23 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(UUID,) = mibBuilder.importSymbols(
    "UUID-TC-MIB",
    "UUID")

(vmwNsxManager,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwNsxManager")


# MODULE-IDENTITY

vmwNsxManagerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1)
)
if mibBuilder.loadTexts:
    vmwNsxManagerMIB.setRevisions(
        ("2020-06-03 00:01",
         "2019-07-09 00:01",
         "2019-02-12 00:01",
         "2018-05-31 00:01",
         "2018-04-25 00:01",
         "2018-03-08 00:00",
         "2017-12-08 00:00",
         "2017-11-22 00:00",
         "2017-11-01 00:00",
         "2017-07-05 00:00",
         "2017-07-03 00:00",
         "2017-06-01 00:00",
         "2017-04-27 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VmwNsxManagerTypeSeverity(TextualConvention, Integer32):
    status = "current"
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
        *(("informational", 1),
          ("low", 2),
          ("medium", 3),
          ("major", 4),
          ("critical", 5),
          ("high", 6))
    )



class VmwNsxManagerSourceID(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxManagerSourceType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxManagerSourceIPAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_VmwNsxMAlertData_ObjectIdentity = ObjectIdentity
vmwNsxMAlertData = _VmwNsxMAlertData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1)
)
if mibBuilder.loadTexts:
    vmwNsxMAlertData.setStatus("current")


class _VmwNsxMEventCode_Type(Integer32):
    """Custom type vmwNsxMEventCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VmwNsxMEventCode_Type.__name__ = "Integer32"
_VmwNsxMEventCode_Object = MibScalar
vmwNsxMEventCode = _VmwNsxMEventCode_Object(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1, 1),
    _VmwNsxMEventCode_Type()
)
vmwNsxMEventCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxMEventCode.setStatus("current")
_VmwNsxMEventTimestamp_Type = DateAndTime
_VmwNsxMEventTimestamp_Object = MibScalar
vmwNsxMEventTimestamp = _VmwNsxMEventTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1, 2),
    _VmwNsxMEventTimestamp_Type()
)
vmwNsxMEventTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxMEventTimestamp.setStatus("current")
_VmwNsxMEventMessage_Type = OctetString
_VmwNsxMEventMessage_Object = MibScalar
vmwNsxMEventMessage = _VmwNsxMEventMessage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1, 3),
    _VmwNsxMEventMessage_Type()
)
vmwNsxMEventMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxMEventMessage.setStatus("current")
_VmwNsxMEventSeverity_Type = VmwNsxManagerTypeSeverity
_VmwNsxMEventSeverity_Object = MibScalar
vmwNsxMEventSeverity = _VmwNsxMEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1, 4),
    _VmwNsxMEventSeverity_Type()
)
vmwNsxMEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxMEventSeverity.setStatus("current")
_VmwNsxMEventComponent_Type = OctetString
_VmwNsxMEventComponent_Object = MibScalar
vmwNsxMEventComponent = _VmwNsxMEventComponent_Object(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1, 5),
    _VmwNsxMEventComponent_Type()
)
vmwNsxMEventComponent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxMEventComponent.setStatus("current")
_VmwNsxMUuid_Type = UUID
_VmwNsxMUuid_Object = MibScalar
vmwNsxMUuid = _VmwNsxMUuid_Object(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1, 6),
    _VmwNsxMUuid_Type()
)
vmwNsxMUuid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxMUuid.setStatus("current")


class _VmwNsxMCount_Type(Integer32):
    """Custom type vmwNsxMCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VmwNsxMCount_Type.__name__ = "Integer32"
_VmwNsxMCount_Object = MibScalar
vmwNsxMCount = _VmwNsxMCount_Object(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1, 7),
    _VmwNsxMCount_Type()
)
vmwNsxMCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxMCount.setStatus("current")
_VmwNsxMEventSourceID_Type = VmwNsxManagerSourceID
_VmwNsxMEventSourceID_Object = MibScalar
vmwNsxMEventSourceID = _VmwNsxMEventSourceID_Object(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1, 8),
    _VmwNsxMEventSourceID_Type()
)
vmwNsxMEventSourceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxMEventSourceID.setStatus("current")
_VmwNsxMEventSourceType_Type = VmwNsxManagerSourceType
_VmwNsxMEventSourceType_Object = MibScalar
vmwNsxMEventSourceType = _VmwNsxMEventSourceType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1, 9),
    _VmwNsxMEventSourceType_Type()
)
vmwNsxMEventSourceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxMEventSourceType.setStatus("current")
_VmwNsxMEventSourceIP_Type = VmwNsxManagerSourceIPAddress
_VmwNsxMEventSourceIP_Object = MibScalar
vmwNsxMEventSourceIP = _VmwNsxMEventSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1, 10),
    _VmwNsxMEventSourceIP_Type()
)
vmwNsxMEventSourceIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxMEventSourceIP.setStatus("current")
_VmwNsxMNotification_ObjectIdentity = ObjectIdentity
vmwNsxMNotification = _VmwNsxMNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2)
)
if mibBuilder.loadTexts:
    vmwNsxMNotification.setStatus("current")
_VmwNsxMBranch_ObjectIdentity = ObjectIdentity
vmwNsxMBranch = _VmwNsxMBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMBranch.setStatus("current")
_VmwNsxMGroupsBranch_ObjectIdentity = ObjectIdentity
vmwNsxMGroupsBranch = _VmwNsxMGroupsBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 0, 1)
)
if mibBuilder.loadTexts:
    vmwNsxMGroupsBranch.setStatus("current")
_VmwNsxMGroupsPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMGroupsPrefix = _VmwNsxMGroupsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 0, 1, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMGroupsPrefix.setStatus("current")
_VmwNsxMSnmp_ObjectIdentity = ObjectIdentity
vmwNsxMSnmp = _VmwNsxMSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vmwNsxMSnmp.setStatus("current")
_VmwNsxMSnmpPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMSnmpPrefix = _VmwNsxMSnmpPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 1, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMSnmpPrefix.setStatus("current")
_VmwNsxMSecurity_ObjectIdentity = ObjectIdentity
vmwNsxMSecurity = _VmwNsxMSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2)
)
if mibBuilder.loadTexts:
    vmwNsxMSecurity.setStatus("current")
_VmwNsxMSecurityPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMSecurityPrefix = _VmwNsxMSecurityPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMSecurityPrefix.setStatus("current")
_VmwNsxMFirewall_ObjectIdentity = ObjectIdentity
vmwNsxMFirewall = _VmwNsxMFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3)
)
if mibBuilder.loadTexts:
    vmwNsxMFirewall.setStatus("current")
_VmwNsxMFirewallPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMFirewallPrefix = _VmwNsxMFirewallPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallPrefix.setStatus("current")
_VmwNsxMEdge_ObjectIdentity = ObjectIdentity
vmwNsxMEdge = _VmwNsxMEdge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4)
)
if mibBuilder.loadTexts:
    vmwNsxMEdge.setStatus("current")
_VmwNsxMEdgePrefix_ObjectIdentity = ObjectIdentity
vmwNsxMEdgePrefix = _VmwNsxMEdgePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMEdgePrefix.setStatus("current")
_VmwNsxMEndpoint_ObjectIdentity = ObjectIdentity
vmwNsxMEndpoint = _VmwNsxMEndpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5)
)
if mibBuilder.loadTexts:
    vmwNsxMEndpoint.setStatus("current")
_VmwNsxMEndpointPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMEndpointPrefix = _VmwNsxMEndpointPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMEndpointPrefix.setStatus("current")
_VmwNsxMEam_ObjectIdentity = ObjectIdentity
vmwNsxMEam = _VmwNsxMEam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 6)
)
if mibBuilder.loadTexts:
    vmwNsxMEam.setStatus("current")
_VmwNsxMEamPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMEamPrefix = _VmwNsxMEamPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 6, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMEamPrefix.setStatus("current")
_VmwNsxMFabric_ObjectIdentity = ObjectIdentity
vmwNsxMFabric = _VmwNsxMFabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7)
)
if mibBuilder.loadTexts:
    vmwNsxMFabric.setStatus("current")
_VmwNsxMFabricPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMFabricPrefix = _VmwNsxMFabricPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMFabricPrefix.setStatus("current")
_VmwNsxMDepPlugin_ObjectIdentity = ObjectIdentity
vmwNsxMDepPlugin = _VmwNsxMDepPlugin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 8)
)
if mibBuilder.loadTexts:
    vmwNsxMDepPlugin.setStatus("current")
_VmwNsxMDepPluginPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMDepPluginPrefix = _VmwNsxMDepPluginPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 8, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMDepPluginPrefix.setStatus("current")
_VmwNsxMMessaging_ObjectIdentity = ObjectIdentity
vmwNsxMMessaging = _VmwNsxMMessaging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 9)
)
if mibBuilder.loadTexts:
    vmwNsxMMessaging.setStatus("current")
_VmwNsxMMessagingPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMMessagingPrefix = _VmwNsxMMessagingPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 9, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMMessagingPrefix.setStatus("current")
_VmwNsxMServiceComposer_ObjectIdentity = ObjectIdentity
vmwNsxMServiceComposer = _VmwNsxMServiceComposer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10)
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposer.setStatus("current")
_VmwNsxMServiceComposerPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMServiceComposerPrefix = _VmwNsxMServiceComposerPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerPrefix.setStatus("current")
_VmwNsxMSvmOperations_ObjectIdentity = ObjectIdentity
vmwNsxMSvmOperations = _VmwNsxMSvmOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 11)
)
if mibBuilder.loadTexts:
    vmwNsxMSvmOperations.setStatus("current")
_VmwNsxMSvmOperationsPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMSvmOperationsPrefix = _VmwNsxMSvmOperationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 11, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMSvmOperationsPrefix.setStatus("current")
_VmwNsxMTranslation_ObjectIdentity = ObjectIdentity
vmwNsxMTranslation = _VmwNsxMTranslation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 12)
)
if mibBuilder.loadTexts:
    vmwNsxMTranslation.setStatus("current")
_VmwNsxMTranslationPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMTranslationPrefix = _VmwNsxMTranslationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 12, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMTranslationPrefix.setStatus("current")
_VmwNsxMUniversalSync_ObjectIdentity = ObjectIdentity
vmwNsxMUniversalSync = _VmwNsxMUniversalSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 13)
)
if mibBuilder.loadTexts:
    vmwNsxMUniversalSync.setStatus("current")
_VmwNsxMUniversalSyncPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMUniversalSyncPrefix = _VmwNsxMUniversalSyncPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 13, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMUniversalSyncPrefix.setStatus("current")
_VmwNsxMAsyncRest_ObjectIdentity = ObjectIdentity
vmwNsxMAsyncRest = _VmwNsxMAsyncRest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 14)
)
if mibBuilder.loadTexts:
    vmwNsxMAsyncRest.setStatus("current")
_VmwNsxMAsyncRestPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMAsyncRestPrefix = _VmwNsxMAsyncRestPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 14, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMAsyncRestPrefix.setStatus("current")
_VmwNsxMExtensionRegistration_ObjectIdentity = ObjectIdentity
vmwNsxMExtensionRegistration = _VmwNsxMExtensionRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 15)
)
if mibBuilder.loadTexts:
    vmwNsxMExtensionRegistration.setStatus("current")
_VmwNsxMExtensionRegistrationPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMExtensionRegistrationPrefix = _VmwNsxMExtensionRegistrationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 15, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMExtensionRegistrationPrefix.setStatus("current")
_VmwNsxMDlp_ObjectIdentity = ObjectIdentity
vmwNsxMDlp = _VmwNsxMDlp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 16)
)
if mibBuilder.loadTexts:
    vmwNsxMDlp.setStatus("current")
_VmwNsxMDlpPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMDlpPrefix = _VmwNsxMDlpPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 16, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMDlpPrefix.setStatus("current")
_VmwNsxMSamSystem_ObjectIdentity = ObjectIdentity
vmwNsxMSamSystem = _VmwNsxMSamSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 17)
)
if mibBuilder.loadTexts:
    vmwNsxMSamSystem.setStatus("current")
_VmwNsxMSamSystemPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMSamSystemPrefix = _VmwNsxMSamSystemPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 17, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMSamSystemPrefix.setStatus("current")
_VmwNsxMUsvm_ObjectIdentity = ObjectIdentity
vmwNsxMUsvm = _VmwNsxMUsvm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 18)
)
if mibBuilder.loadTexts:
    vmwNsxMUsvm.setStatus("current")
_VmwNsxMUsvmPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMUsvmPrefix = _VmwNsxMUsvmPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 18, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMUsvmPrefix.setStatus("current")
_VmwNsxMVsmCore_ObjectIdentity = ObjectIdentity
vmwNsxMVsmCore = _VmwNsxMVsmCore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19)
)
if mibBuilder.loadTexts:
    vmwNsxMVsmCore.setStatus("current")
_VmwNsxMVsmCorePrefix_ObjectIdentity = ObjectIdentity
vmwNsxMVsmCorePrefix = _VmwNsxMVsmCorePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMVsmCorePrefix.setStatus("current")
_VmwNsxMVxlan_ObjectIdentity = ObjectIdentity
vmwNsxMVxlan = _VmwNsxMVxlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20)
)
if mibBuilder.loadTexts:
    vmwNsxMVxlan.setStatus("current")
_VmwNsxMVxlanPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMVxlanPrefix = _VmwNsxMVxlanPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanPrefix.setStatus("current")
_VmwNsxMLogserver_ObjectIdentity = ObjectIdentity
vmwNsxMLogserver = _VmwNsxMLogserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 21)
)
if mibBuilder.loadTexts:
    vmwNsxMLogserver.setStatus("current")
_VmwNsxMLogserverPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMLogserverPrefix = _VmwNsxMLogserverPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 21, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMLogserverPrefix.setStatus("current")
_VmwNsxMApplicationRuleManager_ObjectIdentity = ObjectIdentity
vmwNsxMApplicationRuleManager = _VmwNsxMApplicationRuleManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 22)
)
if mibBuilder.loadTexts:
    vmwNsxMApplicationRuleManager.setStatus("current")
_VmwNsxMApplicationRuleManagerPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMApplicationRuleManagerPrefix = _VmwNsxMApplicationRuleManagerPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 22, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMApplicationRuleManagerPrefix.setStatus("current")
_VmwNsxManagerMIBConformance_ObjectIdentity = ObjectIdentity
vmwNsxManagerMIBConformance = _VmwNsxManagerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99)
)
_VmwNsxManagerMIBCompliances_ObjectIdentity = ObjectIdentity
vmwNsxManagerMIBCompliances = _VmwNsxManagerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 1)
)
_VmwNsxManagerMIBGroups_ObjectIdentity = ObjectIdentity
vmwNsxManagerMIBGroups = _VmwNsxManagerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 2)
)

# Managed Objects groups

vmwNsxManagerNotificationInfoGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 2, 2)
)
vmwNsxManagerNotificationInfoGroup1.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMCount"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerNotificationInfoGroup1.setStatus("current")


# Notification objects

vmwNsxMConfigGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 0, 1, 0, 1)
)
vmwNsxMConfigGroup.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMCount"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMConfigGroup.setStatus(
        "current"
    )

vmwNsxMSnmpDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 1, 0, 1)
)
vmwNsxMSnmpDisabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSnmpDisabled.setStatus(
        "current"
    )

vmwNsxMSnmpManagerConfigUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 1, 0, 2)
)
vmwNsxMSnmpManagerConfigUpdated.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSnmpManagerConfigUpdated.setStatus(
        "current"
    )

vmwNsxMIpAddedBlackList = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 1)
)
vmwNsxMIpAddedBlackList.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMIpAddedBlackList.setStatus(
        "current"
    )

vmwNsxMIpRemovedBlackList = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 2)
)
vmwNsxMIpRemovedBlackList.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMIpRemovedBlackList.setStatus(
        "current"
    )

vmwNsxMSsoConfigFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 3)
)
vmwNsxMSsoConfigFailure.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSsoConfigFailure.setStatus(
        "current"
    )

vmwNsxMSsoUnconfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 4)
)
vmwNsxMSsoUnconfigured.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSsoUnconfigured.setStatus(
        "current"
    )

vmwNsxMUserRoleAssigned = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 5)
)
vmwNsxMUserRoleAssigned.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMUserRoleAssigned.setStatus(
        "current"
    )

vmwNsxMUserRoleUnassigned = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 6)
)
vmwNsxMUserRoleUnassigned.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMUserRoleUnassigned.setStatus(
        "current"
    )

vmwNsxMGroupRoleAssigned = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 7)
)
vmwNsxMGroupRoleAssigned.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMGroupRoleAssigned.setStatus(
        "current"
    )

vmwNsxMGroupRoleUnassigned = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 8)
)
vmwNsxMGroupRoleUnassigned.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMGroupRoleUnassigned.setStatus(
        "current"
    )

vmwNsxMVcLoginFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 9)
)
vmwNsxMVcLoginFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVcLoginFailed.setStatus(
        "current"
    )

vmwNsxMVcDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 10)
)
vmwNsxMVcDisconnected.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVcDisconnected.setStatus(
        "current"
    )

vmwNsxMLostVcConnectivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 11)
)
vmwNsxMLostVcConnectivity.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMLostVcConnectivity.setStatus(
        "current"
    )

vmwNsxMSsoDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 12)
)
vmwNsxMSsoDisconnected.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSsoDisconnected.setStatus(
        "current"
    )

vmwNsxMSsoTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 13)
)
vmwNsxMSsoTimeout.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSsoTimeout.setStatus(
        "current"
    )

vmwNsxMFltrCnfgUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 1)
)
vmwNsxMFltrCnfgUpdateFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFltrCnfgUpdateFailed.setStatus(
        "current"
    )

vmwNsxMFltrCnfgNotAppliedToVnic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 2)
)
vmwNsxMFltrCnfgNotAppliedToVnic.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFltrCnfgNotAppliedToVnic.setStatus(
        "current"
    )

vmwNsxMFltrCnfgAppliedToVnic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 3)
)
vmwNsxMFltrCnfgAppliedToVnic.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFltrCnfgAppliedToVnic.setStatus(
        "current"
    )

vmwNsxMFltrCreatedForVnic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 4)
)
vmwNsxMFltrCreatedForVnic.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFltrCreatedForVnic.setStatus(
        "current"
    )

vmwNsxMFltrDeletedForVnic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 5)
)
vmwNsxMFltrDeletedForVnic.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFltrDeletedForVnic.setStatus(
        "current"
    )

vmwNsxMFirewallConfigUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 6)
)
vmwNsxMFirewallConfigUpdateFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallConfigUpdateFailed.setStatus(
        "current"
    )

vmwNsxMFirewallRuleFailedVnic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 7)
)
vmwNsxMFirewallRuleFailedVnic.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallRuleFailedVnic.setStatus(
        "current"
    )

vmwNsxMFirewallRuleAppliedVnic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 8)
)
vmwNsxMFirewallRuleAppliedVnic.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallRuleAppliedVnic.setStatus(
        "current"
    )

vmwNsxMCntnrCnfgUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 9)
)
vmwNsxMCntnrCnfgUpdateFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMCntnrCnfgUpdateFailed.setStatus(
        "current"
    )

vmwNsxMFlowMissed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 10)
)
vmwNsxMFlowMissed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFlowMissed.setStatus(
        "current"
    )

vmwNsxMSpoofGuardCnfgUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 11)
)
vmwNsxMSpoofGuardCnfgUpdateFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSpoofGuardCnfgUpdateFailed.setStatus(
        "current"
    )

vmwNsxMSpoofGuardFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 12)
)
vmwNsxMSpoofGuardFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSpoofGuardFailed.setStatus(
        "current"
    )

vmwNsxMSpoofGuardApplied = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 13)
)
vmwNsxMSpoofGuardApplied.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSpoofGuardApplied.setStatus(
        "current"
    )

vmwNsxMSpoofGuardDisableFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 14)
)
vmwNsxMSpoofGuardDisableFail.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSpoofGuardDisableFail.setStatus(
        "current"
    )

vmwNsxMSpoofGuardDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 15)
)
vmwNsxMSpoofGuardDisabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSpoofGuardDisabled.setStatus(
        "current"
    )

vmwNsxMLegacyAppServiceDeletionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 16)
)
vmwNsxMLegacyAppServiceDeletionFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMLegacyAppServiceDeletionFailed.setStatus(
        "current"
    )

vmwNsxMFirewallCpuThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 17)
)
vmwNsxMFirewallCpuThresholdCrossed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallCpuThresholdCrossed.setStatus(
        "current"
    )

vmwNsxMFirewallMemThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 18)
)
vmwNsxMFirewallMemThresholdCrossed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallMemThresholdCrossed.setStatus(
        "current"
    )

vmwNsxMConnPerSecThrshldCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 19)
)
vmwNsxMConnPerSecThrshldCrossed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMConnPerSecThrshldCrossed.setStatus(
        "current"
    )

vmwNsxMFirewallCnfgUpdateTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 20)
)
vmwNsxMFirewallCnfgUpdateTimedOut.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallCnfgUpdateTimedOut.setStatus(
        "current"
    )

vmwNsxMSpoofGuardCnfgUpdateTmOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 21)
)
vmwNsxMSpoofGuardCnfgUpdateTmOut.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSpoofGuardCnfgUpdateTmOut.setStatus(
        "current"
    )

vmwNsxMFirewallPublishFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 22)
)
vmwNsxMFirewallPublishFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallPublishFailed.setStatus(
        "current"
    )

vmwNsxMCntnrUpdatePublishFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 23)
)
vmwNsxMCntnrUpdatePublishFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMCntnrUpdatePublishFailed.setStatus(
        "current"
    )

vmwNsxMSpoofGuardUpdatePublishFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 24)
)
vmwNsxMSpoofGuardUpdatePublishFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSpoofGuardUpdatePublishFailed.setStatus(
        "current"
    )

vmwNsxMExcludeListPublishFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 25)
)
vmwNsxMExcludeListPublishFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMExcludeListPublishFailed.setStatus(
        "current"
    )

vmwNsxMFirewallCnfgUpdateOnDltCntnr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 26)
)
vmwNsxMFirewallCnfgUpdateOnDltCntnr.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallCnfgUpdateOnDltCntnr.setStatus(
        "current"
    )

vmwNsxMHostSyncFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 27)
)
vmwNsxMHostSyncFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMHostSyncFailed.setStatus(
        "current"
    )

vmwNsxMHostSynced = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 28)
)
vmwNsxMHostSynced.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMHostSynced.setStatus(
        "current"
    )

vmwNsxMFirewallInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 29)
)
vmwNsxMFirewallInstalled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallInstalled.setStatus(
        "current"
    )

vmwNsxMFirewallInstallFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 30)
)
vmwNsxMFirewallInstallFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallInstallFailed.setStatus(
        "current"
    )

vmwNsxMFirewallClusterInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 31)
)
vmwNsxMFirewallClusterInstalled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallClusterInstalled.setStatus(
        "current"
    )

vmwNsxMFirewallClusterUninstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 32)
)
vmwNsxMFirewallClusterUninstalled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallClusterUninstalled.setStatus(
        "current"
    )

vmwNsxMFirewallClusterDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 33)
)
vmwNsxMFirewallClusterDisabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallClusterDisabled.setStatus(
        "current"
    )

vmwNsxMFirewallForceSyncClusterFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 34)
)
vmwNsxMFirewallForceSyncClusterFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallForceSyncClusterFailed.setStatus(
        "current"
    )

vmwNsxMFirewallForceSyncClusterSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 35)
)
vmwNsxMFirewallForceSyncClusterSuccess.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallForceSyncClusterSuccess.setStatus(
        "current"
    )

vmwNsxMFirewallVsfwdProcessStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 36)
)
vmwNsxMFirewallVsfwdProcessStarted.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallVsfwdProcessStarted.setStatus(
        "current"
    )

vmwNsxMFirewallRulesetApplyAllFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 37)
)
vmwNsxMFirewallRulesetApplyAllFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallRulesetApplyAllFailed.setStatus(
        "current"
    )

vmwNsxMFirewallRulesetAppliedAll = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 38)
)
vmwNsxMFirewallRulesetAppliedAll.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallRulesetAppliedAll.setStatus(
        "current"
    )

vmwNsxMCntnrCnfgApplyFailedToVnic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 39)
)
vmwNsxMCntnrCnfgApplyFailedToVnic.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMCntnrCnfgApplyFailedToVnic.setStatus(
        "current"
    )

vmwNsxMCntnrCnfgApplyAllFailedToVnic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 40)
)
vmwNsxMCntnrCnfgApplyAllFailedToVnic.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMCntnrCnfgApplyAllFailedToVnic.setStatus(
        "current"
    )

vmwNsxMCntnrCnfgAppliedAllToVnic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 41)
)
vmwNsxMCntnrCnfgAppliedAllToVnic.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMCntnrCnfgAppliedAllToVnic.setStatus(
        "current"
    )

vmwNsxMSpoofGuardApplyAllFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 42)
)
vmwNsxMSpoofGuardApplyAllFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSpoofGuardApplyAllFailed.setStatus(
        "current"
    )

vmwNsxMSpoofGuardAppliedAll = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 43)
)
vmwNsxMSpoofGuardAppliedAll.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSpoofGuardAppliedAll.setStatus(
        "current"
    )

vmwNsxMFirewallTimeoutUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 44)
)
vmwNsxMFirewallTimeoutUpdateFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallTimeoutUpdateFailed.setStatus(
        "current"
    )

vmwNsxMFirewallTimeoutApplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 45)
)
vmwNsxMFirewallTimeoutApplyFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallTimeoutApplyFailed.setStatus(
        "current"
    )

vmwNsxMFirewallTimeoutApplied = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 46)
)
vmwNsxMFirewallTimeoutApplied.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallTimeoutApplied.setStatus(
        "current"
    )

vmwNsxMFirewallTimeoutApplyAllFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 47)
)
vmwNsxMFirewallTimeoutApplyAllFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallTimeoutApplyAllFailed.setStatus(
        "current"
    )

vmwNsxMFirewallTimeoutAppliedAll = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 48)
)
vmwNsxMFirewallTimeoutAppliedAll.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallTimeoutAppliedAll.setStatus(
        "current"
    )

vmwNsxMCntnrCnfgAppliedToVnic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 49)
)
vmwNsxMCntnrCnfgAppliedToVnic.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMCntnrCnfgAppliedToVnic.setStatus(
        "current"
    )

vmwNsxMFirewallMaxConcurrentConnectionsThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 50)
)
vmwNsxMFirewallMaxConcurrentConnectionsThresholdCrossed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallMaxConcurrentConnectionsThresholdCrossed.setStatus(
        "current"
    )

vmwNsxMFirewallProcessMemoryThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 51)
)
vmwNsxMFirewallProcessMemoryThresholdCrossed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallProcessMemoryThresholdCrossed.setStatus(
        "current"
    )

vmwNsxMFirewallCpuThresholdCrossCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 52)
)
vmwNsxMFirewallCpuThresholdCrossCleared.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallCpuThresholdCrossCleared.setStatus(
        "current"
    )

vmwNsxMFirewallMemThresholdCrossCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 53)
)
vmwNsxMFirewallMemThresholdCrossCleared.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallMemThresholdCrossCleared.setStatus(
        "current"
    )

vmwNsxMConnPerSecThrshldCrossCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 54)
)
vmwNsxMConnPerSecThrshldCrossCleared.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMConnPerSecThrshldCrossCleared.setStatus(
        "current"
    )

vmwNsxMFirewallMaxConcurrentConnectionsThresholdCrossCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 55)
)
vmwNsxMFirewallMaxConcurrentConnectionsThresholdCrossCleared.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallMaxConcurrentConnectionsThresholdCrossCleared.setStatus(
        "current"
    )

vmwNsxMFirewallProcessMemoryThresholdCrossCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 56)
)
vmwNsxMFirewallProcessMemoryThresholdCrossCleared.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallProcessMemoryThresholdCrossCleared.setStatus(
        "current"
    )

vmwNsxMFirewallThresholdConfigApplied = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 57)
)
vmwNsxMFirewallThresholdConfigApplied.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallThresholdConfigApplied.setStatus(
        "current"
    )

vmwNsxMFirewallThresholdConfigApplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 58)
)
vmwNsxMFirewallThresholdConfigApplyFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallThresholdConfigApplyFailed.setStatus(
        "current"
    )

vmwNsxMUnsupportedIPsetConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 59)
)
vmwNsxMUnsupportedIPsetConfigured.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMUnsupportedIPsetConfigured.setStatus(
        "current"
    )

vmwNsxMEdgeNoVmServing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 1)
)
vmwNsxMEdgeNoVmServing.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeNoVmServing.setStatus(
        "current"
    )

vmwNsxMEdgeGatewayCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 2)
)
vmwNsxMEdgeGatewayCreated.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeGatewayCreated.setStatus(
        "current"
    )

vmwNsxMEdgeVmBadState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 3)
)
vmwNsxMEdgeVmBadState.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmBadState.setStatus(
        "current"
    )

vmwNsxMEdgeVmCommFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 4)
)
vmwNsxMEdgeVmCommFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmCommFailed.setStatus(
        "current"
    )

vmwNsxMEdgeVmCnfgChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 5)
)
vmwNsxMEdgeVmCnfgChanged.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmCnfgChanged.setStatus(
        "current"
    )

vmwNsxMEdgeGatewayDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 6)
)
vmwNsxMEdgeGatewayDeleted.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeGatewayDeleted.setStatus(
        "current"
    )

vmwNsxMEdgeGatewayReDeployed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 7)
)
vmwNsxMEdgeGatewayReDeployed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeGatewayReDeployed.setStatus(
        "current"
    )

vmwNsxMEdgeVmPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 8)
)
vmwNsxMEdgeVmPowerOff.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmPowerOff.setStatus(
        "current"
    )

vmwNsxMEdgeApplianceSizeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 9)
)
vmwNsxMEdgeApplianceSizeChanged.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeApplianceSizeChanged.setStatus(
        "current"
    )

vmwNsxMEdgeUpgrade51x = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 10)
)
vmwNsxMEdgeUpgrade51x.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeUpgrade51x.setStatus(
        "current"
    )

vmwNsxMEdgeLicenseChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 11)
)
vmwNsxMEdgeLicenseChanged.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeLicenseChanged.setStatus(
        "current"
    )

vmwNsxMEdgeApplianceMoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 12)
)
vmwNsxMEdgeApplianceMoved.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeApplianceMoved.setStatus(
        "current"
    )

vmwNsxMEdgeApplianceNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 13)
)
vmwNsxMEdgeApplianceNotFound.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeApplianceNotFound.setStatus(
        "current"
    )

vmwNsxMEdgeVMHealthCheckMiss = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 14)
)
vmwNsxMEdgeVMHealthCheckMiss.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVMHealthCheckMiss.setStatus(
        "current"
    )

vmwNsxMEdgeHealthCheckMiss = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 15)
)
vmwNsxMEdgeHealthCheckMiss.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeHealthCheckMiss.setStatus(
        "current"
    )

vmwNsxMEdgeCommAgentNotConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 16)
)
vmwNsxMEdgeCommAgentNotConnected.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeCommAgentNotConnected.setStatus(
        "current"
    )

vmwNsxMApplianceWithDifferentId = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 17)
)
vmwNsxMApplianceWithDifferentId.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMApplianceWithDifferentId.setStatus(
        "current"
    )

vmwNsxMFirewallRuleModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 18)
)
vmwNsxMFirewallRuleModified.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallRuleModified.setStatus(
        "current"
    )

vmwNsxMEdgeAntiAffinityRuleViolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 19)
)
vmwNsxMEdgeAntiAffinityRuleViolated.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeAntiAffinityRuleViolated.setStatus(
        "current"
    )

vmwNsxMEdgeHaEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 20)
)
vmwNsxMEdgeHaEnabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeHaEnabled.setStatus(
        "current"
    )

vmwNsxMEdgeHaDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 21)
)
vmwNsxMEdgeHaDisabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeHaDisabled.setStatus(
        "current"
    )

vmwNsxMEdgeGatewayRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 22)
)
vmwNsxMEdgeGatewayRecovered.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeGatewayRecovered.setStatus(
        "current"
    )

vmwNsxMEdgeVmRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 23)
)
vmwNsxMEdgeVmRecovered.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmRecovered.setStatus(
        "current"
    )

vmwNsxMEdgeGatewayUpgraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 24)
)
vmwNsxMEdgeGatewayUpgraded.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeGatewayUpgraded.setStatus(
        "current"
    )

vmwNsxMEdgeVmHlthChkDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 25)
)
vmwNsxMEdgeVmHlthChkDisabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmHlthChkDisabled.setStatus(
        "current"
    )

vmwNsxMEdgePrePublishFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 26)
)
vmwNsxMEdgePrePublishFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgePrePublishFailed.setStatus(
        "current"
    )

vmwNsxMEdgeForcedSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 27)
)
vmwNsxMEdgeForcedSync.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeForcedSync.setStatus(
        "current"
    )

vmwNsxMEdgeVmBooted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 28)
)
vmwNsxMEdgeVmBooted.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmBooted.setStatus(
        "current"
    )

vmwNsxMEdgeVmInBadState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 29)
)
vmwNsxMEdgeVmInBadState.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmInBadState.setStatus(
        "current"
    )

vmwNsxMEdgeVmCpuUsageIncreased = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 30)
)
vmwNsxMEdgeVmCpuUsageIncreased.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmCpuUsageIncreased.setStatus(
        "current"
    )

vmwNsxMEdgeVmMemUsageIncreased = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 31)
)
vmwNsxMEdgeVmMemUsageIncreased.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmMemUsageIncreased.setStatus(
        "current"
    )

vmwNsxMEdgeVmProcessFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 32)
)
vmwNsxMEdgeVmProcessFailure.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmProcessFailure.setStatus(
        "current"
    )

vmwNsxMEdgeVmSysTimeBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 33)
)
vmwNsxMEdgeVmSysTimeBad.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmSysTimeBad.setStatus(
        "current"
    )

vmwNsxMEdgeVmSysTimeSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 34)
)
vmwNsxMEdgeVmSysTimeSync.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmSysTimeSync.setStatus(
        "current"
    )

vmwNsxMEdgeAesniCryptoEngineUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 35)
)
vmwNsxMEdgeAesniCryptoEngineUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeAesniCryptoEngineUp.setStatus(
        "current"
    )

vmwNsxMEdgeAesniCryptoEngineDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 36)
)
vmwNsxMEdgeAesniCryptoEngineDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeAesniCryptoEngineDown.setStatus(
        "current"
    )

vmwNsxMEdgeVmOom = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 37)
)
vmwNsxMEdgeVmOom.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmOom.setStatus(
        "current"
    )

vmwNsxMEdgeFileSysRo = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 38)
)
vmwNsxMEdgeFileSysRo.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeFileSysRo.setStatus(
        "current"
    )

vmwNsxMEdgeHaCommDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 39)
)
vmwNsxMEdgeHaCommDisconnected.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeHaCommDisconnected.setStatus(
        "current"
    )

vmwNsxMEdgeHaSwitchOverSelf = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 40)
)
vmwNsxMEdgeHaSwitchOverSelf.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeHaSwitchOverSelf.setStatus(
        "current"
    )

vmwNsxMEdgeHaSwitchOverActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 41)
)
vmwNsxMEdgeHaSwitchOverActive.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeHaSwitchOverActive.setStatus(
        "current"
    )

vmwNsxMEdgeHaSwitchOverStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 42)
)
vmwNsxMEdgeHaSwitchOverStandby.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeHaSwitchOverStandby.setStatus(
        "current"
    )

vmwNsxMEdgeMonitorProcessFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 43)
)
vmwNsxMEdgeMonitorProcessFailure.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeMonitorProcessFailure.setStatus(
        "current"
    )

vmwNsxMLbVirtualServerPoolUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 44)
)
vmwNsxMLbVirtualServerPoolUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMLbVirtualServerPoolUp.setStatus(
        "current"
    )

vmwNsxMLbVirtualServerPoolDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 45)
)
vmwNsxMLbVirtualServerPoolDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMLbVirtualServerPoolDown.setStatus(
        "current"
    )

vmwNsxMLbVirtualServerPoolWrong = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 46)
)
vmwNsxMLbVirtualServerPoolWrong.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMLbVirtualServerPoolWrong.setStatus(
        "current"
    )

vmwNsxMLbPoolWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 47)
)
vmwNsxMLbPoolWarning.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMLbPoolWarning.setStatus(
        "current"
    )

vmwNsxMIpsecChannelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 48)
)
vmwNsxMIpsecChannelUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMIpsecChannelUp.setStatus(
        "current"
    )

vmwNsxMIpsecChannelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 49)
)
vmwNsxMIpsecChannelDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMIpsecChannelDown.setStatus(
        "current"
    )

vmwNsxMIpsecTunnelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 50)
)
vmwNsxMIpsecTunnelUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMIpsecTunnelUp.setStatus(
        "current"
    )

vmwNsxMIpsecTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 51)
)
vmwNsxMIpsecTunnelDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMIpsecTunnelDown.setStatus(
        "current"
    )

vmwNsxMIpsecChannelUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 52)
)
vmwNsxMIpsecChannelUnknown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMIpsecChannelUnknown.setStatus(
        "current"
    )

vmwNsxMIpsecTunnelUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 53)
)
vmwNsxMIpsecTunnelUnknown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMIpsecTunnelUnknown.setStatus(
        "current"
    )

vmwNsxMGlobalLbMemberUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 54)
)
vmwNsxMGlobalLbMemberUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMGlobalLbMemberUp.setStatus(
        "current"
    )

vmwNsxMGlobalLbMemberWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 55)
)
vmwNsxMGlobalLbMemberWarning.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMGlobalLbMemberWarning.setStatus(
        "current"
    )

vmwNsxMGlobalLbMemberDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 56)
)
vmwNsxMGlobalLbMemberDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMGlobalLbMemberDown.setStatus(
        "current"
    )

vmwNsxMGlobalLbMemberUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 57)
)
vmwNsxMGlobalLbMemberUnknown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMGlobalLbMemberUnknown.setStatus(
        "current"
    )

vmwNsxMGlobalLbPeerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 58)
)
vmwNsxMGlobalLbPeerUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMGlobalLbPeerUp.setStatus(
        "current"
    )

vmwNsxMGlobalLbPeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 59)
)
vmwNsxMGlobalLbPeerDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMGlobalLbPeerDown.setStatus(
        "current"
    )

vmwNsxMDhcpServiceDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 60)
)
vmwNsxMDhcpServiceDisabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMDhcpServiceDisabled.setStatus(
        "current"
    )

vmwNsxMEdgeResourceReservationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 61)
)
vmwNsxMEdgeResourceReservationFailure.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeResourceReservationFailure.setStatus(
        "current"
    )

vmwNsxMEdgeSplitBrainDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 62)
)
vmwNsxMEdgeSplitBrainDetected.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeSplitBrainDetected.setStatus(
        "current"
    )

vmwNsxMEdgeSplitBrainRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 63)
)
vmwNsxMEdgeSplitBrainRecovered.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeSplitBrainRecovered.setStatus(
        "current"
    )

vmwNsxMEdgeSplitBrainRecoveryAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 64)
)
vmwNsxMEdgeSplitBrainRecoveryAttempt.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeSplitBrainRecoveryAttempt.setStatus(
        "current"
    )

vmwNsxMEdgeResourceReservationSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 65)
)
vmwNsxMEdgeResourceReservationSuccess.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeResourceReservationSuccess.setStatus(
        "current"
    )

vmwNsxMEdgeSddcChannelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 66)
)
vmwNsxMEdgeSddcChannelUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeSddcChannelUp.setStatus(
        "current"
    )

vmwNsxMEdgeSddcChannelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 67)
)
vmwNsxMEdgeSddcChannelDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeSddcChannelDown.setStatus(
        "current"
    )

vmwNsxMEdgeDuplicateIpDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 68)
)
vmwNsxMEdgeDuplicateIpDetected.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeDuplicateIpDetected.setStatus(
        "current"
    )

vmwNsxMEdgeDuplicateIpResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 69)
)
vmwNsxMEdgeDuplicateIpResolved.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeDuplicateIpResolved.setStatus(
        "current"
    )

vmwNsxMEdgeBgpNeighborUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 70)
)
vmwNsxMEdgeBgpNeighborUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeBgpNeighborUp.setStatus(
        "current"
    )

vmwNsxMEdgeBgpNeighborDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 71)
)
vmwNsxMEdgeBgpNeighborDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeBgpNeighborDown.setStatus(
        "current"
    )

vmwNsxMEdgeBgpNeighborASMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 72)
)
vmwNsxMEdgeBgpNeighborASMismatch.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeBgpNeighborASMismatch.setStatus(
        "current"
    )

vmwNsxMEdgeOSPFNeighborUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 73)
)
vmwNsxMEdgeOSPFNeighborUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeOSPFNeighborUp.setStatus(
        "current"
    )

vmwNsxMEdgeOSPFNeighborDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 74)
)
vmwNsxMEdgeOSPFNeighborDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeOSPFNeighborDown.setStatus(
        "current"
    )

vmwNsxMEdgeOSPFNeighborMTUMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 75)
)
vmwNsxMEdgeOSPFNeighborMTUMismatch.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeOSPFNeighborMTUMismatch.setStatus(
        "current"
    )

vmwNsxMEdgeOSPFNeighborAreaIdMisMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 76)
)
vmwNsxMEdgeOSPFNeighborAreaIdMisMatch.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeOSPFNeighborAreaIdMisMatch.setStatus(
        "current"
    )

vmwNsxMEdgeOSPFNeighborHelloTimerMisMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 77)
)
vmwNsxMEdgeOSPFNeighborHelloTimerMisMatch.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeOSPFNeighborHelloTimerMisMatch.setStatus(
        "current"
    )

vmwNsxMEdgeOSPFNeighborDeadTimerMisMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 78)
)
vmwNsxMEdgeOSPFNeighborDeadTimerMisMatch.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeOSPFNeighborDeadTimerMisMatch.setStatus(
        "current"
    )

vmwNsxMEdgeL2vpnTunnelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 79)
)
vmwNsxMEdgeL2vpnTunnelUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeL2vpnTunnelUp.setStatus(
        "current"
    )

vmwNsxMEdgeL2vpnTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 80)
)
vmwNsxMEdgeL2vpnTunnelDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeL2vpnTunnelDown.setStatus(
        "current"
    )

vmwNsxMEdgeHAForceStandbyRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 81)
)
vmwNsxMEdgeHAForceStandbyRemoved.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeHAForceStandbyRemoved.setStatus(
        "current"
    )

vmwNsxMEdgeHAForceStandbyRemovalFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 82)
)
vmwNsxMEdgeHAForceStandbyRemovalFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeHAForceStandbyRemovalFailed.setStatus(
        "current"
    )

vmwNsxMEdgeVmBADStateRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 83)
)
vmwNsxMEdgeVmBADStateRecovered.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmBADStateRecovered.setStatus(
        "current"
    )

vmwNsxMEdgeVmBADStateAutoHealRecoveryDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 84)
)
vmwNsxMEdgeVmBADStateAutoHealRecoveryDisabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmBADStateAutoHealRecoveryDisabled.setStatus(
        "current"
    )

vmwNsxMEdgeHaInUseVnicChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 85)
)
vmwNsxMEdgeHaInUseVnicChanged.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeHaInUseVnicChanged.setStatus(
        "current"
    )

vmwNsxMEdgeHaCommConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 86)
)
vmwNsxMEdgeHaCommConnected.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeHaCommConnected.setStatus(
        "current"
    )

vmwNsxMEdgeVmRenameFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 87)
)
vmwNsxMEdgeVmRenameFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmRenameFailed.setStatus(
        "current"
    )

vmwNsxMEdgeBgpNeighborshipError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 88)
)
vmwNsxMEdgeBgpNeighborshipError.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeBgpNeighborshipError.setStatus(
        "current"
    )

vmwNsxMEdgeVmBadStateNotRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 89)
)
vmwNsxMEdgeVmBadStateNotRecovered.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmBadStateNotRecovered.setStatus(
        "current"
    )

vmwNsxMEdgeVmDcnOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 90)
)
vmwNsxMEdgeVmDcnOutOfSync.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmDcnOutOfSync.setStatus(
        "current"
    )

vmwNsxMEdgeConsumedResourcesMissingInInventory = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 91)
)
vmwNsxMEdgeConsumedResourcesMissingInInventory.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeConsumedResourcesMissingInInventory.setStatus(
        "current"
    )

vmwNsxMEdgeIpsecDeprecatedComplianceSuiteInUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 92)
)
vmwNsxMEdgeIpsecDeprecatedComplianceSuiteInUse.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeIpsecDeprecatedComplianceSuiteInUse.setStatus(
        "current"
    )

vmwNsxMEdgeConnectedToMultipleTZHavingSameClusters = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 93)
)
vmwNsxMEdgeConnectedToMultipleTZHavingSameClusters.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeConnectedToMultipleTZHavingSameClusters.setStatus(
        "current"
    )

vmwNsxMEdgeConnectedToMultipleTZHavingDifferentClusters = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 94)
)
vmwNsxMEdgeConnectedToMultipleTZHavingDifferentClusters.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeConnectedToMultipleTZHavingDifferentClusters.setStatus(
        "current"
    )

vmwNsxMEndpointThinAgentEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0, 1)
)
vmwNsxMEndpointThinAgentEnabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMEndpointThinAgentEnabled.setStatus(
        "current"
    )

vmwNsxMGuestIntrspctnEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0, 2)
)
vmwNsxMGuestIntrspctnEnabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMGuestIntrspctnEnabled.setStatus(
        "current"
    )

vmwNsxMGuestIntrspctnIncompatibleEsx = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0, 3)
)
vmwNsxMGuestIntrspctnIncompatibleEsx.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMGuestIntrspctnIncompatibleEsx.setStatus(
        "current"
    )

vmwNsxMGuestIntrspctnEsxConnFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0, 4)
)
vmwNsxMGuestIntrspctnEsxConnFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMGuestIntrspctnEsxConnFailed.setStatus(
        "current"
    )

vmwNsxMGuestIntrspctnStatusRcvFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0, 5)
)
vmwNsxMGuestIntrspctnStatusRcvFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMGuestIntrspctnStatusRcvFailed.setStatus(
        "current"
    )

vmwNsxMEsxModuleEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0, 6)
)
vmwNsxMEsxModuleEnabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMEsxModuleEnabled.setStatus(
        "current"
    )

vmwNsxMEsxModuleUninstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0, 7)
)
vmwNsxMEsxModuleUninstalled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMEsxModuleUninstalled.setStatus(
        "current"
    )

vmwNsxMGuestIntrspctnHstMxMssngRep = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0, 8)
)
vmwNsxMGuestIntrspctnHstMxMssngRep.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMGuestIntrspctnHstMxMssngRep.setStatus(
        "current"
    )

vmwNsxMEndpointUndefined = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0, 9)
)
vmwNsxMEndpointUndefined.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMEndpointUndefined.setStatus(
        "current"
    )

vmwNsxMEamGenericAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 6, 0, 1)
)
vmwNsxMEamGenericAlarm.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMEamGenericAlarm.setStatus(
        "current"
    )

vmwNsxMFabricDplymntStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 1)
)
vmwNsxMFabricDplymntStatusChanged.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricDplymntStatusChanged.setStatus(
        "current"
    )

vmwNsxMFabricDplymntUnitCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 2)
)
vmwNsxMFabricDplymntUnitCreated.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricDplymntUnitCreated.setStatus(
        "current"
    )

vmwNsxMFabricDplymntUnitUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 3)
)
vmwNsxMFabricDplymntUnitUpdated.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricDplymntUnitUpdated.setStatus(
        "current"
    )

vmwNsxMFabricDplymntUnitDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 4)
)
vmwNsxMFabricDplymntUnitDestroyed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricDplymntUnitDestroyed.setStatus(
        "current"
    )

vmwNsxMDataStoreNotCnfgrdOnHost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 5)
)
vmwNsxMDataStoreNotCnfgrdOnHost.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMDataStoreNotCnfgrdOnHost.setStatus(
        "current"
    )

vmwNsxMFabricDplymntInstallationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 6)
)
vmwNsxMFabricDplymntInstallationFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricDplymntInstallationFailed.setStatus(
        "current"
    )

vmwNsxMFabricAgentCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 7)
)
vmwNsxMFabricAgentCreated.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricAgentCreated.setStatus(
        "current"
    )

vmwNsxMFabricAgentDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 8)
)
vmwNsxMFabricAgentDestroyed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricAgentDestroyed.setStatus(
        "current"
    )

vmwNsxMFabricSrvceNeedsRedplymnt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 9)
)
vmwNsxMFabricSrvceNeedsRedplymnt.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricSrvceNeedsRedplymnt.setStatus(
        "current"
    )

vmwNsxMUpgradeOfDplymntFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 10)
)
vmwNsxMUpgradeOfDplymntFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMUpgradeOfDplymntFailed.setStatus(
        "current"
    )

vmwNsxMFabricDependenciesNotInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 11)
)
vmwNsxMFabricDependenciesNotInstalled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricDependenciesNotInstalled.setStatus(
        "current"
    )

vmwNsxMFabricErrorNotifSecBfrUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 12)
)
vmwNsxMFabricErrorNotifSecBfrUpgrade.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricErrorNotifSecBfrUpgrade.setStatus(
        "current"
    )

vmwNsxMFabricErrCallbackNtRcvdUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 13)
)
vmwNsxMFabricErrCallbackNtRcvdUpgrade.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricErrCallbackNtRcvdUpgrade.setStatus(
        "current"
    )

vmwNsxMFabricErrCallbackNtRcvdUninstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 14)
)
vmwNsxMFabricErrCallbackNtRcvdUninstall.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricErrCallbackNtRcvdUninstall.setStatus(
        "current"
    )

vmwNsxMFabricUninstallServiceFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 15)
)
vmwNsxMFabricUninstallServiceFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricUninstallServiceFailed.setStatus(
        "current"
    )

vmwNsxMFabricErrorNotifSecBfrUninstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 16)
)
vmwNsxMFabricErrorNotifSecBfrUninstall.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricErrorNotifSecBfrUninstall.setStatus(
        "current"
    )

vmwNsxMFabricServerRebootUninstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 17)
)
vmwNsxMFabricServerRebootUninstall.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricServerRebootUninstall.setStatus(
        "current"
    )

vmwNsxMFabricServerRebootUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 18)
)
vmwNsxMFabricServerRebootUpgrade.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricServerRebootUpgrade.setStatus(
        "current"
    )

vmwNsxMFabricConnEamFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 19)
)
vmwNsxMFabricConnEamFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricConnEamFailed.setStatus(
        "current"
    )

vmwNsxMFabricConnEamRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 20)
)
vmwNsxMFabricConnEamRestored.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricConnEamRestored.setStatus(
        "current"
    )

vmwNsxMFabricPreUninstallCleanUpFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 21)
)
vmwNsxMFabricPreUninstallCleanUpFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricPreUninstallCleanUpFailed.setStatus(
        "current"
    )

vmwNsxMFabricBackingEamNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 22)
)
vmwNsxMFabricBackingEamNotFound.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricBackingEamNotFound.setStatus(
        "current"
    )

vmwNsxMFabricVibManualInstallationRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 23)
)
vmwNsxMFabricVibManualInstallationRequired.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricVibManualInstallationRequired.setStatus(
        "current"
    )

vmwNsxMFabricUninstallDeploymentUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 24)
)
vmwNsxMFabricUninstallDeploymentUnit.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricUninstallDeploymentUnit.setStatus(
        "current"
    )

vmwNsxMDepPluginIpPoolExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 8, 0, 1)
)
vmwNsxMDepPluginIpPoolExhausted.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMDepPluginIpPoolExhausted.setStatus(
        "current"
    )

vmwNsxMDepPluginGenericAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 8, 0, 2)
)
vmwNsxMDepPluginGenericAlarm.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMDepPluginGenericAlarm.setStatus(
        "current"
    )

vmwNsxMDepPluginGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 8, 0, 3)
)
vmwNsxMDepPluginGenericException.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMDepPluginGenericException.setStatus(
        "current"
    )

vmwNsxMDepPluginVmReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 8, 0, 4)
)
vmwNsxMDepPluginVmReboot.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMDepPluginVmReboot.setStatus(
        "current"
    )

vmwNsxMMessagingConfigFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 9, 0, 1)
)
vmwNsxMMessagingConfigFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMMessagingConfigFailed.setStatus(
        "current"
    )

vmwNsxMMessagingReconfigFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 9, 0, 2)
)
vmwNsxMMessagingReconfigFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMMessagingReconfigFailed.setStatus(
        "current"
    )

vmwNsxMMessagingConfigFailedNotifSkip = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 9, 0, 3)
)
vmwNsxMMessagingConfigFailedNotifSkip.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMMessagingConfigFailedNotifSkip.setStatus(
        "current"
    )

vmwNsxMMessagingInfraUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 9, 0, 4)
)
vmwNsxMMessagingInfraUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMMessagingInfraUp.setStatus(
        "current"
    )

vmwNsxMMessagingInfraDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 9, 0, 5)
)
vmwNsxMMessagingInfraDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMMessagingInfraDown.setStatus(
        "current"
    )

vmwNsxMMessagingDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 9, 0, 6)
)
vmwNsxMMessagingDisabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMMessagingDisabled.setStatus(
        "current"
    )

vmwNsxMServiceComposerPolicyOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 1)
)
vmwNsxMServiceComposerPolicyOutOfSync.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerPolicyOutOfSync.setStatus(
        "current"
    )

vmwNsxMServiceComposerPolicyDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 2)
)
vmwNsxMServiceComposerPolicyDeleted.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerPolicyDeleted.setStatus(
        "current"
    )

vmwNsxMServiceComposerFirewallPolicyOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 3)
)
vmwNsxMServiceComposerFirewallPolicyOutOfSync.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerFirewallPolicyOutOfSync.setStatus(
        "current"
    )

vmwNsxMServiceComposerNetworkPolicyOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 4)
)
vmwNsxMServiceComposerNetworkPolicyOutOfSync.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerNetworkPolicyOutOfSync.setStatus(
        "current"
    )

vmwNsxMServiceComposerGuestPolicyOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 5)
)
vmwNsxMServiceComposerGuestPolicyOutOfSync.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerGuestPolicyOutOfSync.setStatus(
        "current"
    )

vmwNsxMServiceComposerOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 6)
)
vmwNsxMServiceComposerOutOfSync.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerOutOfSync.setStatus(
        "current"
    )

vmwNsxMServiceComposerOutOfSyncRebootFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 7)
)
vmwNsxMServiceComposerOutOfSyncRebootFailure.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerOutOfSyncRebootFailure.setStatus(
        "current"
    )

vmwNsxMServiceComposerOutOfSyncDraftRollback = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 8)
)
vmwNsxMServiceComposerOutOfSyncDraftRollback.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerOutOfSyncDraftRollback.setStatus(
        "current"
    )

vmwNsxMServiceComposerOutOfSyncSectionDeletionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 9)
)
vmwNsxMServiceComposerOutOfSyncSectionDeletionFailure.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerOutOfSyncSectionDeletionFailure.setStatus(
        "current"
    )

vmwNsxMServiceComposerOutOfSyncPrecedenceChangeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 10)
)
vmwNsxMServiceComposerOutOfSyncPrecedenceChangeFailure.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerOutOfSyncPrecedenceChangeFailure.setStatus(
        "current"
    )

vmwNsxMServiceComposerOutOfSyncDraftSettingFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 11)
)
vmwNsxMServiceComposerOutOfSyncDraftSettingFailure.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerOutOfSyncDraftSettingFailure.setStatus(
        "current"
    )

vmwNsxMInconsistentSvmAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 11, 0, 1)
)
vmwNsxMInconsistentSvmAlarm.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMInconsistentSvmAlarm.setStatus(
        "current"
    )

vmwNsxMSvmRestartAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 11, 0, 2)
)
vmwNsxMSvmRestartAlarm.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSvmRestartAlarm.setStatus(
        "current"
    )

vmwNsxMSvmAgentUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 11, 0, 3)
)
vmwNsxMSvmAgentUnavailable.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSvmAgentUnavailable.setStatus(
        "current"
    )

vmwNsxMVmAddedToSg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 12, 0, 1)
)
vmwNsxMVmAddedToSg.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVmAddedToSg.setStatus(
        "current"
    )

vmwNsxMVmRemovedFromSg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 12, 0, 2)
)
vmwNsxMVmRemovedFromSg.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVmRemovedFromSg.setStatus(
        "current"
    )

vmwNsxMFullUniversalSyncFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 13, 0, 1)
)
vmwNsxMFullUniversalSyncFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMFullUniversalSyncFailed.setStatus(
        "current"
    )

vmwNsxMSecondaryDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 13, 0, 2)
)
vmwNsxMSecondaryDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSecondaryDown.setStatus(
        "current"
    )

vmwNsxMUniversalSyncFailedForEntity = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 13, 0, 3)
)
vmwNsxMUniversalSyncFailedForEntity.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMUniversalSyncFailedForEntity.setStatus(
        "current"
    )

vmwNsxMUniversalSyncStoppedOnSecondary = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 13, 0, 4)
)
vmwNsxMUniversalSyncStoppedOnSecondary.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMUniversalSyncStoppedOnSecondary.setStatus(
        "current"
    )

vmwNsxMUniversalSyncResumedOnSecondary = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 13, 0, 5)
)
vmwNsxMUniversalSyncResumedOnSecondary.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMUniversalSyncResumedOnSecondary.setStatus(
        "current"
    )

vmwNsxMServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 14, 0, 1)
)
vmwNsxMServerUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMServerUp.setStatus(
        "current"
    )

vmwNsxMExtensionRegistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 15, 0, 1)
)
vmwNsxMExtensionRegistered.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMExtensionRegistered.setStatus(
        "current"
    )

vmwNsxMExtensionUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 15, 0, 2)
)
vmwNsxMExtensionUpdated.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMExtensionUpdated.setStatus(
        "current"
    )

vmwNsxMDataSecScanStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 16, 0, 1)
)
vmwNsxMDataSecScanStarted.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMDataSecScanStarted.setStatus(
        "current"
    )

vmwNsxMDataSecScanEnded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 16, 0, 2)
)
vmwNsxMDataSecScanEnded.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMDataSecScanEnded.setStatus(
        "current"
    )

vmwNsxMSamDataCollectionEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 17, 0, 1)
)
vmwNsxMSamDataCollectionEnabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSamDataCollectionEnabled.setStatus(
        "current"
    )

vmwNsxMSamDataCollectionDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 17, 0, 2)
)
vmwNsxMSamDataCollectionDisabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSamDataCollectionDisabled.setStatus(
        "current"
    )

vmwNsxMSamDataStoppedFlowing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 17, 0, 3)
)
vmwNsxMSamDataStoppedFlowing.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSamDataStoppedFlowing.setStatus(
        "current"
    )

vmwNsxMSamDataResumedFlowing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 17, 0, 4)
)
vmwNsxMSamDataResumedFlowing.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMSamDataResumedFlowing.setStatus(
        "current"
    )

vmwNsxMUsvmHeartbeatStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 18, 0, 1)
)
vmwNsxMUsvmHeartbeatStopped.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMUsvmHeartbeatStopped.setStatus(
        "current"
    )

vmwNsxMUsvmHeartbeatResumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 18, 0, 2)
)
vmwNsxMUsvmHeartbeatResumed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMUsvmHeartbeatResumed.setStatus(
        "current"
    )

vmwNsxMUsvmReceivedHello = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 18, 0, 3)
)
vmwNsxMUsvmReceivedHello.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMUsvmReceivedHello.setStatus(
        "current"
    )

vmwNsxMUpgradeSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19, 0, 1)
)
vmwNsxMUpgradeSuccess.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMUpgradeSuccess.setStatus(
        "current"
    )

vmwNsxMRestoreSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19, 0, 2)
)
vmwNsxMRestoreSuccess.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMRestoreSuccess.setStatus(
        "current"
    )

vmwNsxMDuplicateIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19, 0, 3)
)
vmwNsxMDuplicateIp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMDuplicateIp.setStatus(
        "current"
    )

vmwNsxMVirtualMachineMarkedAsSystemResource = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19, 0, 4)
)
vmwNsxMVirtualMachineMarkedAsSystemResource.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVirtualMachineMarkedAsSystemResource.setStatus(
        "current"
    )

vmwNsxMScaleAboveSupportedLimits = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19, 0, 5)
)
vmwNsxMScaleAboveSupportedLimits.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMScaleAboveSupportedLimits.setStatus(
        "current"
    )

vmwNsxMScaleAboveThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19, 0, 6)
)
vmwNsxMScaleAboveThreshold.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMScaleAboveThreshold.setStatus(
        "current"
    )

vmwNsxMScaleNormalized = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19, 0, 7)
)
vmwNsxMScaleNormalized.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMScaleNormalized.setStatus(
        "current"
    )

vmwNsxMScaleNotEqualToRecommendedValue = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19, 0, 8)
)
vmwNsxMScaleNotEqualToRecommendedValue.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMScaleNotEqualToRecommendedValue.setStatus(
        "current"
    )

vmwNsxMCertificateExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19, 0, 10)
)
vmwNsxMCertificateExpired.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMCertificateExpired.setStatus(
        "current"
    )

vmwNsxMCertificateAboutToExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19, 0, 11)
)
vmwNsxMCertificateAboutToExpire.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"))
)
if mibBuilder.loadTexts:
    vmwNsxMCertificateAboutToExpire.setStatus(
        "current"
    )

vmwNsxMCPUHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19, 0, 12)
)
vmwNsxMCPUHigh.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMCPUHigh.setStatus(
        "current"
    )

vmwNsxMCPUNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19, 0, 13)
)
vmwNsxMCPUNormal.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMCPUNormal.setStatus(
        "current"
    )

vmwNsxMVxlanLogicalSwitchImproperlyCnfg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 1)
)
vmwNsxMVxlanLogicalSwitchImproperlyCnfg.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanLogicalSwitchImproperlyCnfg.setStatus(
        "current"
    )

vmwNsxMVxlanLogicalSwitchProperlyCnfg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 2)
)
vmwNsxMVxlanLogicalSwitchProperlyCnfg.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanLogicalSwitchProperlyCnfg.setStatus(
        "current"
    )

vmwNsxMVxlanInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 3)
)
vmwNsxMVxlanInitFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanInitFailed.setStatus(
        "current"
    )

vmwNsxMVxlanPortInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 4)
)
vmwNsxMVxlanPortInitFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanPortInitFailed.setStatus(
        "current"
    )

vmwNsxMVxlanInstanceDoesNotExist = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 5)
)
vmwNsxMVxlanInstanceDoesNotExist.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanInstanceDoesNotExist.setStatus(
        "current"
    )

vmwNsxMVxlanLogicalSwitchWrkngImproperly = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 6)
)
vmwNsxMVxlanLogicalSwitchWrkngImproperly.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanLogicalSwitchWrkngImproperly.setStatus(
        "current"
    )

vmwNsxMVxlanTransportZoneIncorrectlyWrkng = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 7)
)
vmwNsxMVxlanTransportZoneIncorrectlyWrkng.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanTransportZoneIncorrectlyWrkng.setStatus(
        "current"
    )

vmwNsxMVxlanTransportZoneNotUsed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 8)
)
vmwNsxMVxlanTransportZoneNotUsed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanTransportZoneNotUsed.setStatus(
        "current"
    )

vmwNsxMVxlanOverlayClassMissingOnDvs = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 9)
)
vmwNsxMVxlanOverlayClassMissingOnDvs.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanOverlayClassMissingOnDvs.setStatus(
        "current"
    )

vmwNsxMVxlanControllerRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 10)
)
vmwNsxMVxlanControllerRemoved.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanControllerRemoved.setStatus(
        "current"
    )

vmwNsxMVxlanControllerConnProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 11)
)
vmwNsxMVxlanControllerConnProblem.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanControllerConnProblem.setStatus(
        "current"
    )

vmwNsxMVxlanControllerInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 12)
)
vmwNsxMVxlanControllerInactive.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanControllerInactive.setStatus(
        "current"
    )

vmwNsxMVxlanControllerActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 13)
)
vmwNsxMVxlanControllerActive.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanControllerActive.setStatus(
        "current"
    )

vmwNsxMVxlanVmknicMissingOrDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 14)
)
vmwNsxMVxlanVmknicMissingOrDeleted.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanVmknicMissingOrDeleted.setStatus(
        "current"
    )

vmwNsxMVxlanInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 15)
)
vmwNsxMVxlanInfo.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanInfo.setStatus(
        "current"
    )

vmwNsxMVxlanVmknicPortGrpMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 16)
)
vmwNsxMVxlanVmknicPortGrpMissing.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanVmknicPortGrpMissing.setStatus(
        "current"
    )

vmwNsxMVxlanVmknicPortGrpAppears = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 17)
)
vmwNsxMVxlanVmknicPortGrpAppears.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanVmknicPortGrpAppears.setStatus(
        "current"
    )

vmwNsxMVxlanConnDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 18)
)
vmwNsxMVxlanConnDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanConnDown.setStatus(
        "current"
    )

vmwNsxMBackingPortgroupMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 19)
)
vmwNsxMBackingPortgroupMissing.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMBackingPortgroupMissing.setStatus(
        "current"
    )

vmwNsxMBackingPortgroupReappears = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 20)
)
vmwNsxMBackingPortgroupReappears.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMBackingPortgroupReappears.setStatus(
        "current"
    )

vmwNsxMManagedObjectIdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 21)
)
vmwNsxMManagedObjectIdChanged.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMManagedObjectIdChanged.setStatus(
        "current"
    )

vmwNsxMHighLatencyOnDisk = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 22)
)
vmwNsxMHighLatencyOnDisk.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMHighLatencyOnDisk.setStatus(
        "current"
    )

vmwNsxMHighLatencyOnDiskResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 23)
)
vmwNsxMHighLatencyOnDiskResolved.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMHighLatencyOnDiskResolved.setStatus(
        "current"
    )

vmwNsxMControllerVmPoweredOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 24)
)
vmwNsxMControllerVmPoweredOff.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMControllerVmPoweredOff.setStatus(
        "current"
    )

vmwNsxMControllerVmDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 25)
)
vmwNsxMControllerVmDeleted.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMControllerVmDeleted.setStatus(
        "current"
    )

vmwNsxMVxlanConfigNotSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 26)
)
vmwNsxMVxlanConfigNotSet.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanConfigNotSet.setStatus(
        "current"
    )

vmwNsxMVxlanPortgroupDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 27)
)
vmwNsxMVxlanPortgroupDeleted.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanPortgroupDeleted.setStatus(
        "current"
    )

vmwNsxMVxlanVDSandPgMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 28)
)
vmwNsxMVxlanVDSandPgMismatch.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanVDSandPgMismatch.setStatus(
        "current"
    )

vmwNsxMVxlanControllerDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 29)
)
vmwNsxMVxlanControllerDisconnected.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanControllerDisconnected.setStatus(
        "current"
    )

vmwNsxMVxlanControllerConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 30)
)
vmwNsxMVxlanControllerConnected.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanControllerConnected.setStatus(
        "current"
    )

vmwNsxMVxlanControllerVmPoweredOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 31)
)
vmwNsxMVxlanControllerVmPoweredOn.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanControllerVmPoweredOn.setStatus(
        "current"
    )

vmwNsxMVxlanHostEvents = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 32)
)
vmwNsxMVxlanHostEvents.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceID"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceType"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSourceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanHostEvents.setStatus(
        "current"
    )

vmwNsxMLogserverEventGenStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 21, 0, 1)
)
vmwNsxMLogserverEventGenStopped.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMLogserverEventGenStopped.setStatus(
        "current"
    )

vmwNsxMApplicationRuleManagerFlowAnalysisStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 22, 0, 1)
)
vmwNsxMApplicationRuleManagerFlowAnalysisStart.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMApplicationRuleManagerFlowAnalysisStart.setStatus(
        "current"
    )

vmwNsxMApplicationRuleManagerFlowAnalysisFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 22, 0, 2)
)
vmwNsxMApplicationRuleManagerFlowAnalysisFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMApplicationRuleManagerFlowAnalysisFailed.setStatus(
        "current"
    )

vmwNsxMApplicationRuleManagerFlowAnalysisComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 22, 0, 3)
)
vmwNsxMApplicationRuleManagerFlowAnalysisComplete.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMApplicationRuleManagerFlowAnalysisComplete.setStatus(
        "current"
    )


# Notifications groups

vmwNsxManagerNotificationGroup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 2, 3)
)
vmwNsxManagerNotificationGroup1.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMConfigGroup"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMIpAddedBlackList"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMIpRemovedBlackList"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSsoConfigFailure"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSsoUnconfigured"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUserRoleAssigned"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUserRoleUnassigned"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGroupRoleAssigned"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGroupRoleUnassigned"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVcLoginFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVcDisconnected"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMLostVcConnectivity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFltrCnfgUpdateFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFltrCnfgNotAppliedToVnic"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFltrCnfgAppliedToVnic"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFltrCreatedForVnic"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFltrDeletedForVnic"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallConfigUpdateFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallRuleFailedVnic"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallRuleAppliedVnic"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMCntnrCnfgUpdateFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFlowMissed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSpoofGuardCnfgUpdateFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSpoofGuardFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSpoofGuardApplied"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSpoofGuardDisableFail"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSpoofGuardDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMLegacyAppServiceDeletionFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallCpuThresholdCrossed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallMemThresholdCrossed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMConnPerSecThrshldCrossed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallCnfgUpdateTimedOut"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSpoofGuardCnfgUpdateTmOut"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallPublishFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMCntnrUpdatePublishFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSpoofGuardUpdatePublishFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMExcludeListPublishFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallCnfgUpdateOnDltCntnr"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMHostSyncFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMHostSynced"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallInstalled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallClusterInstalled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallClusterUninstalled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallClusterDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeNoVmServing"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeGatewayCreated"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmBadState"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmCommFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmCnfgChanged"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeGatewayDeleted"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeGatewayReDeployed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmPowerOff"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeApplianceSizeChanged"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeUpgrade51x"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeLicenseChanged"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeApplianceMoved"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeApplianceNotFound"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVMHealthCheckMiss"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeHealthCheckMiss"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeCommAgentNotConnected"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMApplianceWithDifferentId"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallRuleModified"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeAntiAffinityRuleViolated"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeHaEnabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeHaDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeHaInUseVnicChanged"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeGatewayRecovered"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmRecovered"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeGatewayUpgraded"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmHlthChkDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgePrePublishFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeForcedSync"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmBooted"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmInBadState"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmCpuUsageIncreased"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmMemUsageIncreased"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmProcessFailure"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmSysTimeBad"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmSysTimeSync"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeAesniCryptoEngineUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeAesniCryptoEngineDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmOom"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeFileSysRo"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeHaCommDisconnected"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeHaSwitchOverSelf"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeHaSwitchOverActive"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeHaSwitchOverStandby"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeMonitorProcessFailure"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMLbVirtualServerPoolUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMLbVirtualServerPoolDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMLbVirtualServerPoolWrong"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMLbPoolWarning"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMIpsecChannelUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMIpsecChannelDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMIpsecTunnelUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMIpsecTunnelDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMIpsecChannelUnknown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMIpsecTunnelUnknown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGlobalLbMemberUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGlobalLbMemberWarning"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGlobalLbMemberDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGlobalLbMemberUnknown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGlobalLbPeerUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGlobalLbPeerDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMDhcpServiceDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEndpointThinAgentEnabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGuestIntrspctnEnabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGuestIntrspctnIncompatibleEsx"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGuestIntrspctnEsxConnFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGuestIntrspctnStatusRcvFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEsxModuleEnabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEsxModuleUninstalled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGuestIntrspctnHstMxMssngRep"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEndpointUndefined"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEamGenericAlarm"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricDplymntStatusChanged"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricDplymntUnitCreated"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricDplymntUnitUpdated"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricDplymntUnitDestroyed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMDataStoreNotCnfgrdOnHost"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricDplymntInstallationFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricAgentCreated"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricAgentDestroyed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricSrvceNeedsRedplymnt"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUpgradeOfDplymntFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricDependenciesNotInstalled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricErrorNotifSecBfrUpgrade"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricErrCallbackNtRcvdUpgrade"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricErrCallbackNtRcvdUninstall"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricUninstallServiceFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricErrorNotifSecBfrUninstall"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricServerRebootUninstall"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricServerRebootUpgrade"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricConnEamFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricConnEamRestored"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricPreUninstallCleanUpFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricBackingEamNotFound"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricUninstallDeploymentUnit"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMDepPluginIpPoolExhausted"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMDepPluginGenericAlarm"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMDepPluginGenericException"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMDepPluginVmReboot"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMMessagingConfigFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMMessagingReconfigFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMMessagingConfigFailedNotifSkip"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMMessagingInfraUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMMessagingInfraDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMMessagingDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerPolicyOutOfSync"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerPolicyDeleted"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMInconsistentSvmAlarm"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSvmRestartAlarm"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSvmAgentUnavailable"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVmAddedToSg"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVmRemovedFromSg"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFullUniversalSyncFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSecondaryDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUniversalSyncFailedForEntity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServerUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMExtensionRegistered"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMExtensionUpdated"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMDataSecScanStarted"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMDataSecScanEnded"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSamDataCollectionEnabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSamDataCollectionDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSamDataStoppedFlowing"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSamDataResumedFlowing"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUsvmHeartbeatStopped"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUsvmHeartbeatResumed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUsvmReceivedHello"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUpgradeSuccess"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMRestoreSuccess"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanLogicalSwitchImproperlyCnfg"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanLogicalSwitchProperlyCnfg"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanInitFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanPortInitFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanInstanceDoesNotExist"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanLogicalSwitchWrkngImproperly"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanTransportZoneIncorrectlyWrkng"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanTransportZoneNotUsed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanOverlayClassMissingOnDvs"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanControllerRemoved"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanControllerConnProblem"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanControllerInactive"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanControllerActive"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanVmknicMissingOrDeleted"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanInfo"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanVmknicPortGrpMissing"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanVmknicPortGrpAppears"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanConnDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSamDataCollectionDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSamDataStoppedFlowing"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSamDataResumedFlowing"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanOverlayClassMissingOnDvs"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanControllerRemoved"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanControllerConnProblem"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanControllerInactive"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSsoDisconnected"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallInstallFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallForceSyncClusterFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallForceSyncClusterSuccess"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallVsfwdProcessStarted"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeResourceReservationFailure"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeSplitBrainDetected"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeSplitBrainRecovered"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeSplitBrainRecoveryAttempt"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerFirewallPolicyOutOfSync"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerNetworkPolicyOutOfSync"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerGuestPolicyOutOfSync"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerOutOfSync"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerOutOfSyncRebootFailure"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerOutOfSyncDraftRollback"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerOutOfSyncSectionDeletionFailure"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerOutOfSyncPrecedenceChangeFailure"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerOutOfSyncDraftSettingFailure"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMBackingPortgroupMissing"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMBackingPortgroupReappears"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMManagedObjectIdChanged"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMHighLatencyOnDisk"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMHighLatencyOnDiskResolved"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMControllerVmPoweredOff"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMControllerVmDeleted"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanConfigNotSet"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSnmpDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSnmpManagerConfigUpdated"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMDuplicateIp"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerNotificationGroup1.setStatus(
        "current"
    )

vmwNsxManagerNotificationGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 2, 4)
)
vmwNsxManagerNotificationGroup2.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallRulesetApplyAllFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallRulesetAppliedAll"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMCntnrCnfgApplyFailedToVnic"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMCntnrCnfgApplyAllFailedToVnic"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMCntnrCnfgAppliedAllToVnic"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSpoofGuardApplyAllFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSpoofGuardAppliedAll"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallTimeoutUpdateFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallTimeoutApplyFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallTimeoutApplied"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallTimeoutApplyAllFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallTimeoutAppliedAll"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMCntnrCnfgAppliedToVnic"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMLogserverEventGenStopped"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMApplicationRuleManagerFlowAnalysisStart"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMApplicationRuleManagerFlowAnalysisFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMApplicationRuleManagerFlowAnalysisComplete"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeResourceReservationSuccess"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVirtualMachineMarkedAsSystemResource"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeSddcChannelUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeSddcChannelDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMScaleAboveSupportedLimits"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMScaleAboveThreshold"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMScaleNormalized"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanPortgroupDeleted"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanVDSandPgMismatch"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerNotificationGroup2.setStatus(
        "current"
    )

vmwNsxManagerNotificationGroup3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 2, 5)
)
vmwNsxManagerNotificationGroup3.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeDuplicateIpDetected"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeDuplicateIpResolved"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeBgpNeighborUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeBgpNeighborDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeBgpNeighborASMismatch"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeOSPFNeighborUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeOSPFNeighborDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeOSPFNeighborMTUMismatch"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeOSPFNeighborAreaIdMisMatch"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeOSPFNeighborHelloTimerMisMatch"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeOSPFNeighborDeadTimerMisMatch"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeL2vpnTunnelUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeL2vpnTunnelDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeHAForceStandbyRemoved"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeHAForceStandbyRemovalFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmBADStateRecovered"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmBADStateAutoHealRecoveryDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallMaxConcurrentConnectionsThresholdCrossed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallProcessMemoryThresholdCrossed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallCpuThresholdCrossCleared"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallMemThresholdCrossCleared"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMConnPerSecThrshldCrossCleared"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallMaxConcurrentConnectionsThresholdCrossCleared"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallProcessMemoryThresholdCrossCleared"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallThresholdConfigApplied"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallThresholdConfigApplyFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeHaCommConnected"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanControllerDisconnected"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanControllerConnected"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanControllerVmPoweredOn"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanHostEvents"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMScaleNotEqualToRecommendedValue"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerNotificationGroup3.setStatus(
        "current"
    )

vmwNsxManagerNotificationGroup4 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 2, 6)
)
vmwNsxManagerNotificationGroup4.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUniversalSyncStoppedOnSecondary"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUniversalSyncResumedOnSecondary"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerNotificationGroup4.setStatus(
        "current"
    )

vmwNsxManagerNotificationGroup5 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 2, 7)
)
vmwNsxManagerNotificationGroup5.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUniversalSyncStoppedOnSecondary"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUniversalSyncResumedOnSecondary"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMCertificateExpired"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMCertificateAboutToExpire"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMCPUHigh"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMCPUNormal"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUnsupportedIPsetConfigured"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerNotificationGroup5.setStatus(
        "current"
    )

vmwNsxManagerNotificationGroup6 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 2, 8)
)
vmwNsxManagerNotificationGroup6.setObjects(
    ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUnsupportedIPsetConfigured")
)
if mibBuilder.loadTexts:
    vmwNsxManagerNotificationGroup6.setStatus(
        "current"
    )

vmwNsxManagerNotificationGroup7 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 2, 9)
)
vmwNsxManagerNotificationGroup7.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSsoTimeout"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricVibManualInstallationRequired"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerNotificationGroup7.setStatus(
        "current"
    )

vmwNsxManagerNotificationGroup8 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 2, 10)
)
vmwNsxManagerNotificationGroup8.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmRenameFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeBgpNeighborshipError"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerNotificationGroup8.setStatus(
        "current"
    )

vmwNsxManagerNotificationGroup9 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 2, 11)
)
vmwNsxManagerNotificationGroup9.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmBadStateNotRecovered"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmDcnOutOfSync"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeConsumedResourcesMissingInInventory"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerNotificationGroup9.setStatus(
        "current"
    )

vmwNsxManagerNotificationGroup10 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 2, 12)
)
vmwNsxManagerNotificationGroup10.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeIpsecDeprecatedComplianceSuiteInUse"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeConnectedToMultipleTZHavingSameClusters"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeConnectedToMultipleTZHavingDifferentClusters"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerNotificationGroup10.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmwNsxManagerMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 1, 3)
)
vmwNsxManagerMIBBasicCompliance.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationInfoGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup1"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerMIBBasicCompliance.setStatus(
        "obsolete"
    )

vmwNsxManagerMIB630Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 1, 4)
)
vmwNsxManagerMIB630Compliance.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationInfoGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup2"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerMIB630Compliance.setStatus(
        "deprecated"
    )

vmwNsxManagerMIB64Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 1, 5)
)
vmwNsxManagerMIB64Compliance.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationInfoGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup2"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup3"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerMIB64Compliance.setStatus(
        "current"
    )

vmwNsxManagerMIB636Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 1, 6)
)
vmwNsxManagerMIB636Compliance.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationInfoGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup2"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup3"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup4"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerMIB636Compliance.setStatus(
        "current"
    )

vmwNsxManagerMIB641Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 1, 7)
)
vmwNsxManagerMIB641Compliance.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationInfoGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup2"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup3"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup5"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerMIB641Compliance.setStatus(
        "current"
    )

vmwNsxManagerMIB637Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 1, 8)
)
vmwNsxManagerMIB637Compliance.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationInfoGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup2"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup3"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup4"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup6"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerMIB637Compliance.setStatus(
        "current"
    )

vmwNsxManagerMIB642Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 1, 9)
)
vmwNsxManagerMIB642Compliance.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationInfoGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup2"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup3"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup5"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup7"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerMIB642Compliance.setStatus(
        "current"
    )

vmwNsxManagerMIB645Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 1, 10)
)
vmwNsxManagerMIB645Compliance.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationInfoGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup2"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup3"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup5"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup7"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup8"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerMIB645Compliance.setStatus(
        "current"
    )

vmwNsxManagerMIB646Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 1, 11)
)
vmwNsxManagerMIB646Compliance.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationInfoGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup2"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup3"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup5"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup7"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup8"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup9"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerMIB646Compliance.setStatus(
        "current"
    )

vmwNsxManagerMIB647Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 1, 12)
)
vmwNsxManagerMIB647Compliance.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationInfoGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup1"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup2"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup3"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup5"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup7"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup8"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup9"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxManagerNotificationGroup10"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerMIB647Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-NSX-MANAGER-MIB",
    **{"VmwNsxManagerTypeSeverity": VmwNsxManagerTypeSeverity,
       "VmwNsxManagerSourceID": VmwNsxManagerSourceID,
       "VmwNsxManagerSourceType": VmwNsxManagerSourceType,
       "VmwNsxManagerSourceIPAddress": VmwNsxManagerSourceIPAddress,
       "vmwNsxManagerMIB": vmwNsxManagerMIB,
       "vmwNsxMAlertData": vmwNsxMAlertData,
       "vmwNsxMEventCode": vmwNsxMEventCode,
       "vmwNsxMEventTimestamp": vmwNsxMEventTimestamp,
       "vmwNsxMEventMessage": vmwNsxMEventMessage,
       "vmwNsxMEventSeverity": vmwNsxMEventSeverity,
       "vmwNsxMEventComponent": vmwNsxMEventComponent,
       "vmwNsxMUuid": vmwNsxMUuid,
       "vmwNsxMCount": vmwNsxMCount,
       "vmwNsxMEventSourceID": vmwNsxMEventSourceID,
       "vmwNsxMEventSourceType": vmwNsxMEventSourceType,
       "vmwNsxMEventSourceIP": vmwNsxMEventSourceIP,
       "vmwNsxMNotification": vmwNsxMNotification,
       "vmwNsxMBranch": vmwNsxMBranch,
       "vmwNsxMGroupsBranch": vmwNsxMGroupsBranch,
       "vmwNsxMGroupsPrefix": vmwNsxMGroupsPrefix,
       "vmwNsxMConfigGroup": vmwNsxMConfigGroup,
       "vmwNsxMSnmp": vmwNsxMSnmp,
       "vmwNsxMSnmpPrefix": vmwNsxMSnmpPrefix,
       "vmwNsxMSnmpDisabled": vmwNsxMSnmpDisabled,
       "vmwNsxMSnmpManagerConfigUpdated": vmwNsxMSnmpManagerConfigUpdated,
       "vmwNsxMSecurity": vmwNsxMSecurity,
       "vmwNsxMSecurityPrefix": vmwNsxMSecurityPrefix,
       "vmwNsxMIpAddedBlackList": vmwNsxMIpAddedBlackList,
       "vmwNsxMIpRemovedBlackList": vmwNsxMIpRemovedBlackList,
       "vmwNsxMSsoConfigFailure": vmwNsxMSsoConfigFailure,
       "vmwNsxMSsoUnconfigured": vmwNsxMSsoUnconfigured,
       "vmwNsxMUserRoleAssigned": vmwNsxMUserRoleAssigned,
       "vmwNsxMUserRoleUnassigned": vmwNsxMUserRoleUnassigned,
       "vmwNsxMGroupRoleAssigned": vmwNsxMGroupRoleAssigned,
       "vmwNsxMGroupRoleUnassigned": vmwNsxMGroupRoleUnassigned,
       "vmwNsxMVcLoginFailed": vmwNsxMVcLoginFailed,
       "vmwNsxMVcDisconnected": vmwNsxMVcDisconnected,
       "vmwNsxMLostVcConnectivity": vmwNsxMLostVcConnectivity,
       "vmwNsxMSsoDisconnected": vmwNsxMSsoDisconnected,
       "vmwNsxMSsoTimeout": vmwNsxMSsoTimeout,
       "vmwNsxMFirewall": vmwNsxMFirewall,
       "vmwNsxMFirewallPrefix": vmwNsxMFirewallPrefix,
       "vmwNsxMFltrCnfgUpdateFailed": vmwNsxMFltrCnfgUpdateFailed,
       "vmwNsxMFltrCnfgNotAppliedToVnic": vmwNsxMFltrCnfgNotAppliedToVnic,
       "vmwNsxMFltrCnfgAppliedToVnic": vmwNsxMFltrCnfgAppliedToVnic,
       "vmwNsxMFltrCreatedForVnic": vmwNsxMFltrCreatedForVnic,
       "vmwNsxMFltrDeletedForVnic": vmwNsxMFltrDeletedForVnic,
       "vmwNsxMFirewallConfigUpdateFailed": vmwNsxMFirewallConfigUpdateFailed,
       "vmwNsxMFirewallRuleFailedVnic": vmwNsxMFirewallRuleFailedVnic,
       "vmwNsxMFirewallRuleAppliedVnic": vmwNsxMFirewallRuleAppliedVnic,
       "vmwNsxMCntnrCnfgUpdateFailed": vmwNsxMCntnrCnfgUpdateFailed,
       "vmwNsxMFlowMissed": vmwNsxMFlowMissed,
       "vmwNsxMSpoofGuardCnfgUpdateFailed": vmwNsxMSpoofGuardCnfgUpdateFailed,
       "vmwNsxMSpoofGuardFailed": vmwNsxMSpoofGuardFailed,
       "vmwNsxMSpoofGuardApplied": vmwNsxMSpoofGuardApplied,
       "vmwNsxMSpoofGuardDisableFail": vmwNsxMSpoofGuardDisableFail,
       "vmwNsxMSpoofGuardDisabled": vmwNsxMSpoofGuardDisabled,
       "vmwNsxMLegacyAppServiceDeletionFailed": vmwNsxMLegacyAppServiceDeletionFailed,
       "vmwNsxMFirewallCpuThresholdCrossed": vmwNsxMFirewallCpuThresholdCrossed,
       "vmwNsxMFirewallMemThresholdCrossed": vmwNsxMFirewallMemThresholdCrossed,
       "vmwNsxMConnPerSecThrshldCrossed": vmwNsxMConnPerSecThrshldCrossed,
       "vmwNsxMFirewallCnfgUpdateTimedOut": vmwNsxMFirewallCnfgUpdateTimedOut,
       "vmwNsxMSpoofGuardCnfgUpdateTmOut": vmwNsxMSpoofGuardCnfgUpdateTmOut,
       "vmwNsxMFirewallPublishFailed": vmwNsxMFirewallPublishFailed,
       "vmwNsxMCntnrUpdatePublishFailed": vmwNsxMCntnrUpdatePublishFailed,
       "vmwNsxMSpoofGuardUpdatePublishFailed": vmwNsxMSpoofGuardUpdatePublishFailed,
       "vmwNsxMExcludeListPublishFailed": vmwNsxMExcludeListPublishFailed,
       "vmwNsxMFirewallCnfgUpdateOnDltCntnr": vmwNsxMFirewallCnfgUpdateOnDltCntnr,
       "vmwNsxMHostSyncFailed": vmwNsxMHostSyncFailed,
       "vmwNsxMHostSynced": vmwNsxMHostSynced,
       "vmwNsxMFirewallInstalled": vmwNsxMFirewallInstalled,
       "vmwNsxMFirewallInstallFailed": vmwNsxMFirewallInstallFailed,
       "vmwNsxMFirewallClusterInstalled": vmwNsxMFirewallClusterInstalled,
       "vmwNsxMFirewallClusterUninstalled": vmwNsxMFirewallClusterUninstalled,
       "vmwNsxMFirewallClusterDisabled": vmwNsxMFirewallClusterDisabled,
       "vmwNsxMFirewallForceSyncClusterFailed": vmwNsxMFirewallForceSyncClusterFailed,
       "vmwNsxMFirewallForceSyncClusterSuccess": vmwNsxMFirewallForceSyncClusterSuccess,
       "vmwNsxMFirewallVsfwdProcessStarted": vmwNsxMFirewallVsfwdProcessStarted,
       "vmwNsxMFirewallRulesetApplyAllFailed": vmwNsxMFirewallRulesetApplyAllFailed,
       "vmwNsxMFirewallRulesetAppliedAll": vmwNsxMFirewallRulesetAppliedAll,
       "vmwNsxMCntnrCnfgApplyFailedToVnic": vmwNsxMCntnrCnfgApplyFailedToVnic,
       "vmwNsxMCntnrCnfgApplyAllFailedToVnic": vmwNsxMCntnrCnfgApplyAllFailedToVnic,
       "vmwNsxMCntnrCnfgAppliedAllToVnic": vmwNsxMCntnrCnfgAppliedAllToVnic,
       "vmwNsxMSpoofGuardApplyAllFailed": vmwNsxMSpoofGuardApplyAllFailed,
       "vmwNsxMSpoofGuardAppliedAll": vmwNsxMSpoofGuardAppliedAll,
       "vmwNsxMFirewallTimeoutUpdateFailed": vmwNsxMFirewallTimeoutUpdateFailed,
       "vmwNsxMFirewallTimeoutApplyFailed": vmwNsxMFirewallTimeoutApplyFailed,
       "vmwNsxMFirewallTimeoutApplied": vmwNsxMFirewallTimeoutApplied,
       "vmwNsxMFirewallTimeoutApplyAllFailed": vmwNsxMFirewallTimeoutApplyAllFailed,
       "vmwNsxMFirewallTimeoutAppliedAll": vmwNsxMFirewallTimeoutAppliedAll,
       "vmwNsxMCntnrCnfgAppliedToVnic": vmwNsxMCntnrCnfgAppliedToVnic,
       "vmwNsxMFirewallMaxConcurrentConnectionsThresholdCrossed": vmwNsxMFirewallMaxConcurrentConnectionsThresholdCrossed,
       "vmwNsxMFirewallProcessMemoryThresholdCrossed": vmwNsxMFirewallProcessMemoryThresholdCrossed,
       "vmwNsxMFirewallCpuThresholdCrossCleared": vmwNsxMFirewallCpuThresholdCrossCleared,
       "vmwNsxMFirewallMemThresholdCrossCleared": vmwNsxMFirewallMemThresholdCrossCleared,
       "vmwNsxMConnPerSecThrshldCrossCleared": vmwNsxMConnPerSecThrshldCrossCleared,
       "vmwNsxMFirewallMaxConcurrentConnectionsThresholdCrossCleared": vmwNsxMFirewallMaxConcurrentConnectionsThresholdCrossCleared,
       "vmwNsxMFirewallProcessMemoryThresholdCrossCleared": vmwNsxMFirewallProcessMemoryThresholdCrossCleared,
       "vmwNsxMFirewallThresholdConfigApplied": vmwNsxMFirewallThresholdConfigApplied,
       "vmwNsxMFirewallThresholdConfigApplyFailed": vmwNsxMFirewallThresholdConfigApplyFailed,
       "vmwNsxMUnsupportedIPsetConfigured": vmwNsxMUnsupportedIPsetConfigured,
       "vmwNsxMEdge": vmwNsxMEdge,
       "vmwNsxMEdgePrefix": vmwNsxMEdgePrefix,
       "vmwNsxMEdgeNoVmServing": vmwNsxMEdgeNoVmServing,
       "vmwNsxMEdgeGatewayCreated": vmwNsxMEdgeGatewayCreated,
       "vmwNsxMEdgeVmBadState": vmwNsxMEdgeVmBadState,
       "vmwNsxMEdgeVmCommFailed": vmwNsxMEdgeVmCommFailed,
       "vmwNsxMEdgeVmCnfgChanged": vmwNsxMEdgeVmCnfgChanged,
       "vmwNsxMEdgeGatewayDeleted": vmwNsxMEdgeGatewayDeleted,
       "vmwNsxMEdgeGatewayReDeployed": vmwNsxMEdgeGatewayReDeployed,
       "vmwNsxMEdgeVmPowerOff": vmwNsxMEdgeVmPowerOff,
       "vmwNsxMEdgeApplianceSizeChanged": vmwNsxMEdgeApplianceSizeChanged,
       "vmwNsxMEdgeUpgrade51x": vmwNsxMEdgeUpgrade51x,
       "vmwNsxMEdgeLicenseChanged": vmwNsxMEdgeLicenseChanged,
       "vmwNsxMEdgeApplianceMoved": vmwNsxMEdgeApplianceMoved,
       "vmwNsxMEdgeApplianceNotFound": vmwNsxMEdgeApplianceNotFound,
       "vmwNsxMEdgeVMHealthCheckMiss": vmwNsxMEdgeVMHealthCheckMiss,
       "vmwNsxMEdgeHealthCheckMiss": vmwNsxMEdgeHealthCheckMiss,
       "vmwNsxMEdgeCommAgentNotConnected": vmwNsxMEdgeCommAgentNotConnected,
       "vmwNsxMApplianceWithDifferentId": vmwNsxMApplianceWithDifferentId,
       "vmwNsxMFirewallRuleModified": vmwNsxMFirewallRuleModified,
       "vmwNsxMEdgeAntiAffinityRuleViolated": vmwNsxMEdgeAntiAffinityRuleViolated,
       "vmwNsxMEdgeHaEnabled": vmwNsxMEdgeHaEnabled,
       "vmwNsxMEdgeHaDisabled": vmwNsxMEdgeHaDisabled,
       "vmwNsxMEdgeGatewayRecovered": vmwNsxMEdgeGatewayRecovered,
       "vmwNsxMEdgeVmRecovered": vmwNsxMEdgeVmRecovered,
       "vmwNsxMEdgeGatewayUpgraded": vmwNsxMEdgeGatewayUpgraded,
       "vmwNsxMEdgeVmHlthChkDisabled": vmwNsxMEdgeVmHlthChkDisabled,
       "vmwNsxMEdgePrePublishFailed": vmwNsxMEdgePrePublishFailed,
       "vmwNsxMEdgeForcedSync": vmwNsxMEdgeForcedSync,
       "vmwNsxMEdgeVmBooted": vmwNsxMEdgeVmBooted,
       "vmwNsxMEdgeVmInBadState": vmwNsxMEdgeVmInBadState,
       "vmwNsxMEdgeVmCpuUsageIncreased": vmwNsxMEdgeVmCpuUsageIncreased,
       "vmwNsxMEdgeVmMemUsageIncreased": vmwNsxMEdgeVmMemUsageIncreased,
       "vmwNsxMEdgeVmProcessFailure": vmwNsxMEdgeVmProcessFailure,
       "vmwNsxMEdgeVmSysTimeBad": vmwNsxMEdgeVmSysTimeBad,
       "vmwNsxMEdgeVmSysTimeSync": vmwNsxMEdgeVmSysTimeSync,
       "vmwNsxMEdgeAesniCryptoEngineUp": vmwNsxMEdgeAesniCryptoEngineUp,
       "vmwNsxMEdgeAesniCryptoEngineDown": vmwNsxMEdgeAesniCryptoEngineDown,
       "vmwNsxMEdgeVmOom": vmwNsxMEdgeVmOom,
       "vmwNsxMEdgeFileSysRo": vmwNsxMEdgeFileSysRo,
       "vmwNsxMEdgeHaCommDisconnected": vmwNsxMEdgeHaCommDisconnected,
       "vmwNsxMEdgeHaSwitchOverSelf": vmwNsxMEdgeHaSwitchOverSelf,
       "vmwNsxMEdgeHaSwitchOverActive": vmwNsxMEdgeHaSwitchOverActive,
       "vmwNsxMEdgeHaSwitchOverStandby": vmwNsxMEdgeHaSwitchOverStandby,
       "vmwNsxMEdgeMonitorProcessFailure": vmwNsxMEdgeMonitorProcessFailure,
       "vmwNsxMLbVirtualServerPoolUp": vmwNsxMLbVirtualServerPoolUp,
       "vmwNsxMLbVirtualServerPoolDown": vmwNsxMLbVirtualServerPoolDown,
       "vmwNsxMLbVirtualServerPoolWrong": vmwNsxMLbVirtualServerPoolWrong,
       "vmwNsxMLbPoolWarning": vmwNsxMLbPoolWarning,
       "vmwNsxMIpsecChannelUp": vmwNsxMIpsecChannelUp,
       "vmwNsxMIpsecChannelDown": vmwNsxMIpsecChannelDown,
       "vmwNsxMIpsecTunnelUp": vmwNsxMIpsecTunnelUp,
       "vmwNsxMIpsecTunnelDown": vmwNsxMIpsecTunnelDown,
       "vmwNsxMIpsecChannelUnknown": vmwNsxMIpsecChannelUnknown,
       "vmwNsxMIpsecTunnelUnknown": vmwNsxMIpsecTunnelUnknown,
       "vmwNsxMGlobalLbMemberUp": vmwNsxMGlobalLbMemberUp,
       "vmwNsxMGlobalLbMemberWarning": vmwNsxMGlobalLbMemberWarning,
       "vmwNsxMGlobalLbMemberDown": vmwNsxMGlobalLbMemberDown,
       "vmwNsxMGlobalLbMemberUnknown": vmwNsxMGlobalLbMemberUnknown,
       "vmwNsxMGlobalLbPeerUp": vmwNsxMGlobalLbPeerUp,
       "vmwNsxMGlobalLbPeerDown": vmwNsxMGlobalLbPeerDown,
       "vmwNsxMDhcpServiceDisabled": vmwNsxMDhcpServiceDisabled,
       "vmwNsxMEdgeResourceReservationFailure": vmwNsxMEdgeResourceReservationFailure,
       "vmwNsxMEdgeSplitBrainDetected": vmwNsxMEdgeSplitBrainDetected,
       "vmwNsxMEdgeSplitBrainRecovered": vmwNsxMEdgeSplitBrainRecovered,
       "vmwNsxMEdgeSplitBrainRecoveryAttempt": vmwNsxMEdgeSplitBrainRecoveryAttempt,
       "vmwNsxMEdgeResourceReservationSuccess": vmwNsxMEdgeResourceReservationSuccess,
       "vmwNsxMEdgeSddcChannelUp": vmwNsxMEdgeSddcChannelUp,
       "vmwNsxMEdgeSddcChannelDown": vmwNsxMEdgeSddcChannelDown,
       "vmwNsxMEdgeDuplicateIpDetected": vmwNsxMEdgeDuplicateIpDetected,
       "vmwNsxMEdgeDuplicateIpResolved": vmwNsxMEdgeDuplicateIpResolved,
       "vmwNsxMEdgeBgpNeighborUp": vmwNsxMEdgeBgpNeighborUp,
       "vmwNsxMEdgeBgpNeighborDown": vmwNsxMEdgeBgpNeighborDown,
       "vmwNsxMEdgeBgpNeighborASMismatch": vmwNsxMEdgeBgpNeighborASMismatch,
       "vmwNsxMEdgeOSPFNeighborUp": vmwNsxMEdgeOSPFNeighborUp,
       "vmwNsxMEdgeOSPFNeighborDown": vmwNsxMEdgeOSPFNeighborDown,
       "vmwNsxMEdgeOSPFNeighborMTUMismatch": vmwNsxMEdgeOSPFNeighborMTUMismatch,
       "vmwNsxMEdgeOSPFNeighborAreaIdMisMatch": vmwNsxMEdgeOSPFNeighborAreaIdMisMatch,
       "vmwNsxMEdgeOSPFNeighborHelloTimerMisMatch": vmwNsxMEdgeOSPFNeighborHelloTimerMisMatch,
       "vmwNsxMEdgeOSPFNeighborDeadTimerMisMatch": vmwNsxMEdgeOSPFNeighborDeadTimerMisMatch,
       "vmwNsxMEdgeL2vpnTunnelUp": vmwNsxMEdgeL2vpnTunnelUp,
       "vmwNsxMEdgeL2vpnTunnelDown": vmwNsxMEdgeL2vpnTunnelDown,
       "vmwNsxMEdgeHAForceStandbyRemoved": vmwNsxMEdgeHAForceStandbyRemoved,
       "vmwNsxMEdgeHAForceStandbyRemovalFailed": vmwNsxMEdgeHAForceStandbyRemovalFailed,
       "vmwNsxMEdgeVmBADStateRecovered": vmwNsxMEdgeVmBADStateRecovered,
       "vmwNsxMEdgeVmBADStateAutoHealRecoveryDisabled": vmwNsxMEdgeVmBADStateAutoHealRecoveryDisabled,
       "vmwNsxMEdgeHaInUseVnicChanged": vmwNsxMEdgeHaInUseVnicChanged,
       "vmwNsxMEdgeHaCommConnected": vmwNsxMEdgeHaCommConnected,
       "vmwNsxMEdgeVmRenameFailed": vmwNsxMEdgeVmRenameFailed,
       "vmwNsxMEdgeBgpNeighborshipError": vmwNsxMEdgeBgpNeighborshipError,
       "vmwNsxMEdgeVmBadStateNotRecovered": vmwNsxMEdgeVmBadStateNotRecovered,
       "vmwNsxMEdgeVmDcnOutOfSync": vmwNsxMEdgeVmDcnOutOfSync,
       "vmwNsxMEdgeConsumedResourcesMissingInInventory": vmwNsxMEdgeConsumedResourcesMissingInInventory,
       "vmwNsxMEdgeIpsecDeprecatedComplianceSuiteInUse": vmwNsxMEdgeIpsecDeprecatedComplianceSuiteInUse,
       "vmwNsxMEdgeConnectedToMultipleTZHavingSameClusters": vmwNsxMEdgeConnectedToMultipleTZHavingSameClusters,
       "vmwNsxMEdgeConnectedToMultipleTZHavingDifferentClusters": vmwNsxMEdgeConnectedToMultipleTZHavingDifferentClusters,
       "vmwNsxMEndpoint": vmwNsxMEndpoint,
       "vmwNsxMEndpointPrefix": vmwNsxMEndpointPrefix,
       "vmwNsxMEndpointThinAgentEnabled": vmwNsxMEndpointThinAgentEnabled,
       "vmwNsxMGuestIntrspctnEnabled": vmwNsxMGuestIntrspctnEnabled,
       "vmwNsxMGuestIntrspctnIncompatibleEsx": vmwNsxMGuestIntrspctnIncompatibleEsx,
       "vmwNsxMGuestIntrspctnEsxConnFailed": vmwNsxMGuestIntrspctnEsxConnFailed,
       "vmwNsxMGuestIntrspctnStatusRcvFailed": vmwNsxMGuestIntrspctnStatusRcvFailed,
       "vmwNsxMEsxModuleEnabled": vmwNsxMEsxModuleEnabled,
       "vmwNsxMEsxModuleUninstalled": vmwNsxMEsxModuleUninstalled,
       "vmwNsxMGuestIntrspctnHstMxMssngRep": vmwNsxMGuestIntrspctnHstMxMssngRep,
       "vmwNsxMEndpointUndefined": vmwNsxMEndpointUndefined,
       "vmwNsxMEam": vmwNsxMEam,
       "vmwNsxMEamPrefix": vmwNsxMEamPrefix,
       "vmwNsxMEamGenericAlarm": vmwNsxMEamGenericAlarm,
       "vmwNsxMFabric": vmwNsxMFabric,
       "vmwNsxMFabricPrefix": vmwNsxMFabricPrefix,
       "vmwNsxMFabricDplymntStatusChanged": vmwNsxMFabricDplymntStatusChanged,
       "vmwNsxMFabricDplymntUnitCreated": vmwNsxMFabricDplymntUnitCreated,
       "vmwNsxMFabricDplymntUnitUpdated": vmwNsxMFabricDplymntUnitUpdated,
       "vmwNsxMFabricDplymntUnitDestroyed": vmwNsxMFabricDplymntUnitDestroyed,
       "vmwNsxMDataStoreNotCnfgrdOnHost": vmwNsxMDataStoreNotCnfgrdOnHost,
       "vmwNsxMFabricDplymntInstallationFailed": vmwNsxMFabricDplymntInstallationFailed,
       "vmwNsxMFabricAgentCreated": vmwNsxMFabricAgentCreated,
       "vmwNsxMFabricAgentDestroyed": vmwNsxMFabricAgentDestroyed,
       "vmwNsxMFabricSrvceNeedsRedplymnt": vmwNsxMFabricSrvceNeedsRedplymnt,
       "vmwNsxMUpgradeOfDplymntFailed": vmwNsxMUpgradeOfDplymntFailed,
       "vmwNsxMFabricDependenciesNotInstalled": vmwNsxMFabricDependenciesNotInstalled,
       "vmwNsxMFabricErrorNotifSecBfrUpgrade": vmwNsxMFabricErrorNotifSecBfrUpgrade,
       "vmwNsxMFabricErrCallbackNtRcvdUpgrade": vmwNsxMFabricErrCallbackNtRcvdUpgrade,
       "vmwNsxMFabricErrCallbackNtRcvdUninstall": vmwNsxMFabricErrCallbackNtRcvdUninstall,
       "vmwNsxMFabricUninstallServiceFailed": vmwNsxMFabricUninstallServiceFailed,
       "vmwNsxMFabricErrorNotifSecBfrUninstall": vmwNsxMFabricErrorNotifSecBfrUninstall,
       "vmwNsxMFabricServerRebootUninstall": vmwNsxMFabricServerRebootUninstall,
       "vmwNsxMFabricServerRebootUpgrade": vmwNsxMFabricServerRebootUpgrade,
       "vmwNsxMFabricConnEamFailed": vmwNsxMFabricConnEamFailed,
       "vmwNsxMFabricConnEamRestored": vmwNsxMFabricConnEamRestored,
       "vmwNsxMFabricPreUninstallCleanUpFailed": vmwNsxMFabricPreUninstallCleanUpFailed,
       "vmwNsxMFabricBackingEamNotFound": vmwNsxMFabricBackingEamNotFound,
       "vmwNsxMFabricVibManualInstallationRequired": vmwNsxMFabricVibManualInstallationRequired,
       "vmwNsxMFabricUninstallDeploymentUnit": vmwNsxMFabricUninstallDeploymentUnit,
       "vmwNsxMDepPlugin": vmwNsxMDepPlugin,
       "vmwNsxMDepPluginPrefix": vmwNsxMDepPluginPrefix,
       "vmwNsxMDepPluginIpPoolExhausted": vmwNsxMDepPluginIpPoolExhausted,
       "vmwNsxMDepPluginGenericAlarm": vmwNsxMDepPluginGenericAlarm,
       "vmwNsxMDepPluginGenericException": vmwNsxMDepPluginGenericException,
       "vmwNsxMDepPluginVmReboot": vmwNsxMDepPluginVmReboot,
       "vmwNsxMMessaging": vmwNsxMMessaging,
       "vmwNsxMMessagingPrefix": vmwNsxMMessagingPrefix,
       "vmwNsxMMessagingConfigFailed": vmwNsxMMessagingConfigFailed,
       "vmwNsxMMessagingReconfigFailed": vmwNsxMMessagingReconfigFailed,
       "vmwNsxMMessagingConfigFailedNotifSkip": vmwNsxMMessagingConfigFailedNotifSkip,
       "vmwNsxMMessagingInfraUp": vmwNsxMMessagingInfraUp,
       "vmwNsxMMessagingInfraDown": vmwNsxMMessagingInfraDown,
       "vmwNsxMMessagingDisabled": vmwNsxMMessagingDisabled,
       "vmwNsxMServiceComposer": vmwNsxMServiceComposer,
       "vmwNsxMServiceComposerPrefix": vmwNsxMServiceComposerPrefix,
       "vmwNsxMServiceComposerPolicyOutOfSync": vmwNsxMServiceComposerPolicyOutOfSync,
       "vmwNsxMServiceComposerPolicyDeleted": vmwNsxMServiceComposerPolicyDeleted,
       "vmwNsxMServiceComposerFirewallPolicyOutOfSync": vmwNsxMServiceComposerFirewallPolicyOutOfSync,
       "vmwNsxMServiceComposerNetworkPolicyOutOfSync": vmwNsxMServiceComposerNetworkPolicyOutOfSync,
       "vmwNsxMServiceComposerGuestPolicyOutOfSync": vmwNsxMServiceComposerGuestPolicyOutOfSync,
       "vmwNsxMServiceComposerOutOfSync": vmwNsxMServiceComposerOutOfSync,
       "vmwNsxMServiceComposerOutOfSyncRebootFailure": vmwNsxMServiceComposerOutOfSyncRebootFailure,
       "vmwNsxMServiceComposerOutOfSyncDraftRollback": vmwNsxMServiceComposerOutOfSyncDraftRollback,
       "vmwNsxMServiceComposerOutOfSyncSectionDeletionFailure": vmwNsxMServiceComposerOutOfSyncSectionDeletionFailure,
       "vmwNsxMServiceComposerOutOfSyncPrecedenceChangeFailure": vmwNsxMServiceComposerOutOfSyncPrecedenceChangeFailure,
       "vmwNsxMServiceComposerOutOfSyncDraftSettingFailure": vmwNsxMServiceComposerOutOfSyncDraftSettingFailure,
       "vmwNsxMSvmOperations": vmwNsxMSvmOperations,
       "vmwNsxMSvmOperationsPrefix": vmwNsxMSvmOperationsPrefix,
       "vmwNsxMInconsistentSvmAlarm": vmwNsxMInconsistentSvmAlarm,
       "vmwNsxMSvmRestartAlarm": vmwNsxMSvmRestartAlarm,
       "vmwNsxMSvmAgentUnavailable": vmwNsxMSvmAgentUnavailable,
       "vmwNsxMTranslation": vmwNsxMTranslation,
       "vmwNsxMTranslationPrefix": vmwNsxMTranslationPrefix,
       "vmwNsxMVmAddedToSg": vmwNsxMVmAddedToSg,
       "vmwNsxMVmRemovedFromSg": vmwNsxMVmRemovedFromSg,
       "vmwNsxMUniversalSync": vmwNsxMUniversalSync,
       "vmwNsxMUniversalSyncPrefix": vmwNsxMUniversalSyncPrefix,
       "vmwNsxMFullUniversalSyncFailed": vmwNsxMFullUniversalSyncFailed,
       "vmwNsxMSecondaryDown": vmwNsxMSecondaryDown,
       "vmwNsxMUniversalSyncFailedForEntity": vmwNsxMUniversalSyncFailedForEntity,
       "vmwNsxMUniversalSyncStoppedOnSecondary": vmwNsxMUniversalSyncStoppedOnSecondary,
       "vmwNsxMUniversalSyncResumedOnSecondary": vmwNsxMUniversalSyncResumedOnSecondary,
       "vmwNsxMAsyncRest": vmwNsxMAsyncRest,
       "vmwNsxMAsyncRestPrefix": vmwNsxMAsyncRestPrefix,
       "vmwNsxMServerUp": vmwNsxMServerUp,
       "vmwNsxMExtensionRegistration": vmwNsxMExtensionRegistration,
       "vmwNsxMExtensionRegistrationPrefix": vmwNsxMExtensionRegistrationPrefix,
       "vmwNsxMExtensionRegistered": vmwNsxMExtensionRegistered,
       "vmwNsxMExtensionUpdated": vmwNsxMExtensionUpdated,
       "vmwNsxMDlp": vmwNsxMDlp,
       "vmwNsxMDlpPrefix": vmwNsxMDlpPrefix,
       "vmwNsxMDataSecScanStarted": vmwNsxMDataSecScanStarted,
       "vmwNsxMDataSecScanEnded": vmwNsxMDataSecScanEnded,
       "vmwNsxMSamSystem": vmwNsxMSamSystem,
       "vmwNsxMSamSystemPrefix": vmwNsxMSamSystemPrefix,
       "vmwNsxMSamDataCollectionEnabled": vmwNsxMSamDataCollectionEnabled,
       "vmwNsxMSamDataCollectionDisabled": vmwNsxMSamDataCollectionDisabled,
       "vmwNsxMSamDataStoppedFlowing": vmwNsxMSamDataStoppedFlowing,
       "vmwNsxMSamDataResumedFlowing": vmwNsxMSamDataResumedFlowing,
       "vmwNsxMUsvm": vmwNsxMUsvm,
       "vmwNsxMUsvmPrefix": vmwNsxMUsvmPrefix,
       "vmwNsxMUsvmHeartbeatStopped": vmwNsxMUsvmHeartbeatStopped,
       "vmwNsxMUsvmHeartbeatResumed": vmwNsxMUsvmHeartbeatResumed,
       "vmwNsxMUsvmReceivedHello": vmwNsxMUsvmReceivedHello,
       "vmwNsxMVsmCore": vmwNsxMVsmCore,
       "vmwNsxMVsmCorePrefix": vmwNsxMVsmCorePrefix,
       "vmwNsxMUpgradeSuccess": vmwNsxMUpgradeSuccess,
       "vmwNsxMRestoreSuccess": vmwNsxMRestoreSuccess,
       "vmwNsxMDuplicateIp": vmwNsxMDuplicateIp,
       "vmwNsxMVirtualMachineMarkedAsSystemResource": vmwNsxMVirtualMachineMarkedAsSystemResource,
       "vmwNsxMScaleAboveSupportedLimits": vmwNsxMScaleAboveSupportedLimits,
       "vmwNsxMScaleAboveThreshold": vmwNsxMScaleAboveThreshold,
       "vmwNsxMScaleNormalized": vmwNsxMScaleNormalized,
       "vmwNsxMScaleNotEqualToRecommendedValue": vmwNsxMScaleNotEqualToRecommendedValue,
       "vmwNsxMCertificateExpired": vmwNsxMCertificateExpired,
       "vmwNsxMCertificateAboutToExpire": vmwNsxMCertificateAboutToExpire,
       "vmwNsxMCPUHigh": vmwNsxMCPUHigh,
       "vmwNsxMCPUNormal": vmwNsxMCPUNormal,
       "vmwNsxMVxlan": vmwNsxMVxlan,
       "vmwNsxMVxlanPrefix": vmwNsxMVxlanPrefix,
       "vmwNsxMVxlanLogicalSwitchImproperlyCnfg": vmwNsxMVxlanLogicalSwitchImproperlyCnfg,
       "vmwNsxMVxlanLogicalSwitchProperlyCnfg": vmwNsxMVxlanLogicalSwitchProperlyCnfg,
       "vmwNsxMVxlanInitFailed": vmwNsxMVxlanInitFailed,
       "vmwNsxMVxlanPortInitFailed": vmwNsxMVxlanPortInitFailed,
       "vmwNsxMVxlanInstanceDoesNotExist": vmwNsxMVxlanInstanceDoesNotExist,
       "vmwNsxMVxlanLogicalSwitchWrkngImproperly": vmwNsxMVxlanLogicalSwitchWrkngImproperly,
       "vmwNsxMVxlanTransportZoneIncorrectlyWrkng": vmwNsxMVxlanTransportZoneIncorrectlyWrkng,
       "vmwNsxMVxlanTransportZoneNotUsed": vmwNsxMVxlanTransportZoneNotUsed,
       "vmwNsxMVxlanOverlayClassMissingOnDvs": vmwNsxMVxlanOverlayClassMissingOnDvs,
       "vmwNsxMVxlanControllerRemoved": vmwNsxMVxlanControllerRemoved,
       "vmwNsxMVxlanControllerConnProblem": vmwNsxMVxlanControllerConnProblem,
       "vmwNsxMVxlanControllerInactive": vmwNsxMVxlanControllerInactive,
       "vmwNsxMVxlanControllerActive": vmwNsxMVxlanControllerActive,
       "vmwNsxMVxlanVmknicMissingOrDeleted": vmwNsxMVxlanVmknicMissingOrDeleted,
       "vmwNsxMVxlanInfo": vmwNsxMVxlanInfo,
       "vmwNsxMVxlanVmknicPortGrpMissing": vmwNsxMVxlanVmknicPortGrpMissing,
       "vmwNsxMVxlanVmknicPortGrpAppears": vmwNsxMVxlanVmknicPortGrpAppears,
       "vmwNsxMVxlanConnDown": vmwNsxMVxlanConnDown,
       "vmwNsxMBackingPortgroupMissing": vmwNsxMBackingPortgroupMissing,
       "vmwNsxMBackingPortgroupReappears": vmwNsxMBackingPortgroupReappears,
       "vmwNsxMManagedObjectIdChanged": vmwNsxMManagedObjectIdChanged,
       "vmwNsxMHighLatencyOnDisk": vmwNsxMHighLatencyOnDisk,
       "vmwNsxMHighLatencyOnDiskResolved": vmwNsxMHighLatencyOnDiskResolved,
       "vmwNsxMControllerVmPoweredOff": vmwNsxMControllerVmPoweredOff,
       "vmwNsxMControllerVmDeleted": vmwNsxMControllerVmDeleted,
       "vmwNsxMVxlanConfigNotSet": vmwNsxMVxlanConfigNotSet,
       "vmwNsxMVxlanPortgroupDeleted": vmwNsxMVxlanPortgroupDeleted,
       "vmwNsxMVxlanVDSandPgMismatch": vmwNsxMVxlanVDSandPgMismatch,
       "vmwNsxMVxlanControllerDisconnected": vmwNsxMVxlanControllerDisconnected,
       "vmwNsxMVxlanControllerConnected": vmwNsxMVxlanControllerConnected,
       "vmwNsxMVxlanControllerVmPoweredOn": vmwNsxMVxlanControllerVmPoweredOn,
       "vmwNsxMVxlanHostEvents": vmwNsxMVxlanHostEvents,
       "vmwNsxMLogserver": vmwNsxMLogserver,
       "vmwNsxMLogserverPrefix": vmwNsxMLogserverPrefix,
       "vmwNsxMLogserverEventGenStopped": vmwNsxMLogserverEventGenStopped,
       "vmwNsxMApplicationRuleManager": vmwNsxMApplicationRuleManager,
       "vmwNsxMApplicationRuleManagerPrefix": vmwNsxMApplicationRuleManagerPrefix,
       "vmwNsxMApplicationRuleManagerFlowAnalysisStart": vmwNsxMApplicationRuleManagerFlowAnalysisStart,
       "vmwNsxMApplicationRuleManagerFlowAnalysisFailed": vmwNsxMApplicationRuleManagerFlowAnalysisFailed,
       "vmwNsxMApplicationRuleManagerFlowAnalysisComplete": vmwNsxMApplicationRuleManagerFlowAnalysisComplete,
       "vmwNsxManagerMIBConformance": vmwNsxManagerMIBConformance,
       "vmwNsxManagerMIBCompliances": vmwNsxManagerMIBCompliances,
       "vmwNsxManagerMIBBasicCompliance": vmwNsxManagerMIBBasicCompliance,
       "vmwNsxManagerMIB630Compliance": vmwNsxManagerMIB630Compliance,
       "vmwNsxManagerMIB64Compliance": vmwNsxManagerMIB64Compliance,
       "vmwNsxManagerMIB636Compliance": vmwNsxManagerMIB636Compliance,
       "vmwNsxManagerMIB641Compliance": vmwNsxManagerMIB641Compliance,
       "vmwNsxManagerMIB637Compliance": vmwNsxManagerMIB637Compliance,
       "vmwNsxManagerMIB642Compliance": vmwNsxManagerMIB642Compliance,
       "vmwNsxManagerMIB645Compliance": vmwNsxManagerMIB645Compliance,
       "vmwNsxManagerMIB646Compliance": vmwNsxManagerMIB646Compliance,
       "vmwNsxManagerMIB647Compliance": vmwNsxManagerMIB647Compliance,
       "vmwNsxManagerMIBGroups": vmwNsxManagerMIBGroups,
       "vmwNsxManagerNotificationInfoGroup1": vmwNsxManagerNotificationInfoGroup1,
       "vmwNsxManagerNotificationGroup1": vmwNsxManagerNotificationGroup1,
       "vmwNsxManagerNotificationGroup2": vmwNsxManagerNotificationGroup2,
       "vmwNsxManagerNotificationGroup3": vmwNsxManagerNotificationGroup3,
       "vmwNsxManagerNotificationGroup4": vmwNsxManagerNotificationGroup4,
       "vmwNsxManagerNotificationGroup5": vmwNsxManagerNotificationGroup5,
       "vmwNsxManagerNotificationGroup6": vmwNsxManagerNotificationGroup6,
       "vmwNsxManagerNotificationGroup7": vmwNsxManagerNotificationGroup7,
       "vmwNsxManagerNotificationGroup8": vmwNsxManagerNotificationGroup8,
       "vmwNsxManagerNotificationGroup9": vmwNsxManagerNotificationGroup9,
       "vmwNsxManagerNotificationGroup10": vmwNsxManagerNotificationGroup10}
)
