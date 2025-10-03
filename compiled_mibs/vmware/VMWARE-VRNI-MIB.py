# SNMP MIB module (VMWARE-VRNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vmware\VMWARE-VRNI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:38 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(vmwNetworkInsight,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwNetworkInsight")

(VmwLongSnmpAdminString,) = mibBuilder.importSymbols(
    "VMWARE-TC-MIB",
    "VmwLongSnmpAdminString")


# MODULE-IDENTITY

vmwNetworkInsightMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1)
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIB.setRevisions(
        ("2023-03-10 00:00",
         "2022-09-07 00:00",
         "2022-03-30 00:00",
         "2021-10-01 00:00",
         "2021-05-24 00:00",
         "2020-05-20 00:00",
         "2019-08-19 00:00",
         "2019-06-06 00:00",
         "2019-03-22 00:00",
         "2018-11-27 00:00",
         "2018-09-12 00:00",
         "2017-09-05 00:00",
         "2017-06-01 00:00",
         "2017-02-20 00:00",
         "2016-10-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VmwVrniSeverity(TextualConvention, OctetString):
    status = "current"
    displayHint = "255t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_VmwVRNIEvents_ObjectIdentity = ObjectIdentity
vmwVRNIEvents = _VmwVRNIEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0)
)
if mibBuilder.loadTexts:
    vmwVRNIEvents.setStatus("current")
_VmwVRNIData_ObjectIdentity = ObjectIdentity
vmwVRNIData = _VmwVRNIData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 1)
)
if mibBuilder.loadTexts:
    vmwVRNIData.setStatus("current")
_VmwAffectedObject_Type = SnmpAdminString
_VmwAffectedObject_Object = MibScalar
vmwAffectedObject = _VmwAffectedObject_Object(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 1, 102),
    _VmwAffectedObject_Type()
)
vmwAffectedObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAffectedObject.setStatus("current")
_VmwEventSeverity_Type = VmwVrniSeverity
_VmwEventSeverity_Object = MibScalar
vmwEventSeverity = _VmwEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 1, 103),
    _VmwEventSeverity_Type()
)
vmwEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwEventSeverity.setStatus("current")
_VmwVrniUrl_Type = SnmpAdminString
_VmwVrniUrl_Object = MibScalar
vmwVrniUrl = _VmwVrniUrl_Object(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 1, 104),
    _VmwVrniUrl_Type()
)
vmwVrniUrl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVrniUrl.setStatus("current")
_VmwTimestamp_Type = DateAndTime
_VmwTimestamp_Object = MibScalar
vmwTimestamp = _VmwTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 1, 105),
    _VmwTimestamp_Type()
)
vmwTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwTimestamp.setStatus("current")
_VmwOperatorDesc_Type = VmwLongSnmpAdminString
_VmwOperatorDesc_Object = MibScalar
vmwOperatorDesc = _VmwOperatorDesc_Object(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 1, 106),
    _VmwOperatorDesc_Type()
)
vmwOperatorDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwOperatorDesc.setStatus("current")
_VmwEventName_Type = VmwLongSnmpAdminString
_VmwEventName_Object = MibScalar
vmwEventName = _VmwEventName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 1, 107),
    _VmwEventName_Type()
)
vmwEventName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwEventName.setStatus("current")
_VmwNetworkInsightMIBConformance_ObjectIdentity = ObjectIdentity
vmwNetworkInsightMIBConformance = _VmwNetworkInsightMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99)
)
_VmwNetworkInsightMIBCompliances_ObjectIdentity = ObjectIdentity
vmwNetworkInsightMIBCompliances = _VmwNetworkInsightMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1)
)
_VmwNetworkInsightMIBGroups_ObjectIdentity = ObjectIdentity
vmwNetworkInsightMIBGroups = _VmwNetworkInsightMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2)
)

# Managed Objects groups

vmwNetworkInsightNotificationInfoGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 2)
)
vmwNetworkInsightNotificationInfoGroup1.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationInfoGroup1.setStatus("current")

vmwNetworkInsightNotificationInfoGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 20)
)
vmwNetworkInsightNotificationInfoGroup2.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationInfoGroup2.setStatus("deprecated")

vmwNetworkInsightNotificationInfoGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 55)
)
vmwNetworkInsightNotificationInfoGroup3.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationInfoGroup3.setStatus("current")


# Notification objects

vmwSnmpTrapsAreConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 101)
)
vmwSnmpTrapsAreConfigured.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSnmpTrapsAreConfigured.setStatus(
        "current"
    )

vmwSnmpTrapsAreDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 102)
)
vmwSnmpTrapsAreDisabled.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSnmpTrapsAreDisabled.setStatus(
        "current"
    )

vmwTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 103)
)
vmwTestTrap.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwTestTrap.setStatus(
        "current"
    )

vmwArkinApplicationMemberLimitEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 568)
)
vmwArkinApplicationMemberLimitEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwArkinApplicationMemberLimitEvent.setStatus(
        "current"
    )

vmwNsxiApplianceAvailableEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 974)
)
vmwNsxiApplianceAvailableEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNsxiApplianceAvailableEvent.setStatus(
        "current"
    )

vmwNsxiSubscriptionCreateFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 975)
)
vmwNsxiSubscriptionCreateFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNsxiSubscriptionCreateFailedEvent.setStatus(
        "current"
    )

vmwNsxiSubscriptionDeleteFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 976)
)
vmwNsxiSubscriptionDeleteFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNsxiSubscriptionDeleteFailedEvent.setStatus(
        "current"
    )

vmwNsxiSubscriptionUpdateFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 977)
)
vmwNsxiSubscriptionUpdateFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNsxiSubscriptionUpdateFailedEvent.setStatus(
        "current"
    )

vmwNsxiSslHandshakeFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 978)
)
vmwNsxiSslHandshakeFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNsxiSslHandshakeFailedEvent.setStatus(
        "current"
    )

vmwHybridConnectBgpStatusDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 1279)
)
vmwHybridConnectBgpStatusDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHybridConnectBgpStatusDownEvent.setStatus(
        "current"
    )

vmwKubernetesBaseEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 1510)
)
vmwKubernetesBaseEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwKubernetesBaseEvent.setStatus(
        "current"
    )

vmwNSXALBSystemEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 3558)
)
vmwNSXALBSystemEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXALBSystemEvent.setStatus(
        "current"
    )

vmwEntityDiscoveryChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20001)
)
vmwEntityDiscoveryChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEntityDiscoveryChangeEvent.setStatus(
        "current"
    )

vmwEntityPropertiesChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20002)
)
vmwEntityPropertiesChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEntityPropertiesChangeEvent.setStatus(
        "current"
    )

vmwFirewallNotInstalledOnHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20003)
)
vmwFirewallNotInstalledOnHostEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFirewallNotInstalledOnHostEvent.setStatus(
        "current"
    )

vmwHostWithStaleFirewallRulesEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20004)
)
vmwHostWithStaleFirewallRulesEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostWithStaleFirewallRulesEvent.setStatus(
        "current"
    )

vmwIpAddressChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20005)
)
vmwIpAddressChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwIpAddressChangeEvent.setStatus(
        "current"
    )

vmwL2GatewayAnomalyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20006)
)
vmwL2GatewayAnomalyEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwL2GatewayAnomalyEvent.setStatus(
        "current"
    )

vmwL2NetworkAddressAnomalyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20007)
)
vmwL2NetworkAddressAnomalyEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwL2NetworkAddressAnomalyEvent.setStatus(
        "current"
    )

vmwL2NetworkDiameterExceededEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20008)
)
vmwL2NetworkDiameterExceededEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwL2NetworkDiameterExceededEvent.setStatus(
        "current"
    )

vmwL2NetworkUplinkMissingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20009)
)
vmwL2NetworkUplinkMissingEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwL2NetworkUplinkMissingEvent.setStatus(
        "current"
    )

vmwL2NetworkWithNoVMsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20010)
)
vmwL2NetworkWithNoVMsEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwL2NetworkWithNoVMsEvent.setStatus(
        "current"
    )

vmwLayer2NetworkDiameterChangedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20011)
)
vmwLayer2NetworkDiameterChangedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwLayer2NetworkDiameterChangedEvent.setStatus(
        "current"
    )

vmwMTUMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20012)
)
vmwMTUMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwMTUMismatchEvent.setStatus(
        "current"
    )

vmwNetworkIsolationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20013)
)
vmwNetworkIsolationEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNetworkIsolationEvent.setStatus(
        "current"
    )

vmwNoPathEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20014)
)
vmwNoPathEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNoPathEvent.setStatus(
        "current"
    )

vmwSpoofguardDisabledEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20015)
)
vmwSpoofguardDisabledEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSpoofguardDisabledEvent.setStatus(
        "current"
    )

vmwVMotionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20018)
)
vmwVMotionEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMotionEvent.setStatus(
        "current"
    )

vmwVMWithDisconnectedVnicsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20019)
)
vmwVMWithDisconnectedVnicsEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMWithDisconnectedVnicsEvent.setStatus(
        "current"
    )

vmwVMWithMulipleVnicsOnDifferentVxlansEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20020)
)
vmwVMWithMulipleVnicsOnDifferentVxlansEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMWithMulipleVnicsOnDifferentVxlansEvent.setStatus(
        "current"
    )

vmwVMWithMulipleVnicsOnSameL2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20021)
)
vmwVMWithMulipleVnicsOnSameL2Event.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMWithMulipleVnicsOnSameL2Event.setStatus(
        "current"
    )

vmwVMWithNoIpAddressEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20022)
)
vmwVMWithNoIpAddressEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMWithNoIpAddressEvent.setStatus(
        "current"
    )

vmwVTEPMissingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20023)
)
vmwVTEPMissingEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVTEPMissingEvent.setStatus(
        "current"
    )

vmwL2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20024)
)
vmwL2Event.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwL2Event.setStatus(
        "current"
    )

vmwMembershipChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20025)
)
vmwMembershipChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwMembershipChangeEvent.setStatus(
        "current"
    )

vmwSecurityGroupMembershipChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20026)
)
vmwSecurityGroupMembershipChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSecurityGroupMembershipChangeEvent.setStatus(
        "current"
    )

vmwFirewallRuleMembershipChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20027)
)
vmwFirewallRuleMembershipChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFirewallRuleMembershipChangeEvent.setStatus(
        "current"
    )

vmwVlanMembershipChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20028)
)
vmwVlanMembershipChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVlanMembershipChangeEvent.setStatus(
        "current"
    )

vmwVxlanMembershipChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20029)
)
vmwVxlanMembershipChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVxlanMembershipChangeEvent.setStatus(
        "current"
    )

vmwDeleteChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20030)
)
vmwDeleteChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDeleteChangeEvent.setStatus(
        "current"
    )

vmwVtepFailedPingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20031)
)
vmwVtepFailedPingEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVtepFailedPingEvent.setStatus(
        "current"
    )

vmwEmptySearchStreamChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20034)
)
vmwEmptySearchStreamChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEmptySearchStreamChangeEvent.setStatus(
        "current"
    )

vmwSearchStreamMembershipChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20035)
)
vmwSearchStreamMembershipChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSearchStreamMembershipChangeEvent.setStatus(
        "current"
    )

vmwEmptySearchStreamProblemEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20036)
)
vmwEmptySearchStreamProblemEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEmptySearchStreamProblemEvent.setStatus(
        "current"
    )

vmwSearchStreamMembershipProblemEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20037)
)
vmwSearchStreamMembershipProblemEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSearchStreamMembershipProblemEvent.setStatus(
        "current"
    )

vmwOspfConfigurationMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20038)
)
vmwOspfConfigurationMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwOspfConfigurationMismatchEvent.setStatus(
        "current"
    )

vmwServiceVMNotHealthyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20039)
)
vmwServiceVMNotHealthyEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwServiceVMNotHealthyEvent.setStatus(
        "current"
    )

vmwServiceVMNotPoweredOnEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20040)
)
vmwServiceVMNotPoweredOnEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwServiceVMNotPoweredOnEvent.setStatus(
        "current"
    )

vmwServiceVMHighCPUUsageEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20041)
)
vmwServiceVMHighCPUUsageEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwServiceVMHighCPUUsageEvent.setStatus(
        "current"
    )

vmwServiceVMHighMemoryUsageEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20042)
)
vmwServiceVMHighMemoryUsageEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwServiceVMHighMemoryUsageEvent.setStatus(
        "current"
    )

vmwServiceVMHighDiskUsageEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20043)
)
vmwServiceVMHighDiskUsageEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwServiceVMHighDiskUsageEvent.setStatus(
        "current"
    )

vmwIPSetPropertiesChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20050)
)
vmwIPSetPropertiesChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwIPSetPropertiesChangeEvent.setStatus(
        "current"
    )

vmwFirewallRulePropertiesChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20051)
)
vmwFirewallRulePropertiesChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFirewallRulePropertiesChangeEvent.setStatus(
        "current"
    )

vmwSecurityGroupPropertiesChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20052)
)
vmwSecurityGroupPropertiesChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSecurityGroupPropertiesChangeEvent.setStatus(
        "current"
    )

vmwIPSetMembershipChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20053)
)
vmwIPSetMembershipChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwIPSetMembershipChangeEvent.setStatus(
        "current"
    )

vmwFirewallRuleMaskEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20054)
)
vmwFirewallRuleMaskEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFirewallRuleMaskEvent.setStatus(
        "current"
    )

vmwSecurityMembershipChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20056)
)
vmwSecurityMembershipChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSecurityMembershipChangeEvent.setStatus(
        "current"
    )

vmwSecurityTagPropertiesChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20057)
)
vmwSecurityTagPropertiesChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSecurityTagPropertiesChangeEvent.setStatus(
        "current"
    )

vmwSecurityTagMembershipChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20058)
)
vmwSecurityTagMembershipChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSecurityTagMembershipChangeEvent.setStatus(
        "current"
    )

vmwHostDatastoreChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20059)
)
vmwHostDatastoreChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostDatastoreChangeEvent.setStatus(
        "current"
    )

vmwVMDatastoreChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20060)
)
vmwVMDatastoreChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMDatastoreChangeEvent.setStatus(
        "current"
    )

vmwVMSnapshotChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20061)
)
vmwVMSnapshotChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMSnapshotChangeEvent.setStatus(
        "current"
    )

vmwVMVirtualDiskChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20062)
)
vmwVMVirtualDiskChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMVirtualDiskChangeEvent.setStatus(
        "current"
    )

vmwIPSetDefinitionMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20063)
)
vmwIPSetDefinitionMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwIPSetDefinitionMismatchEvent.setStatus(
        "current"
    )

vmwSegmentMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20064)
)
vmwSegmentMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSegmentMismatchEvent.setStatus(
        "current"
    )

vmwVtepEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20065)
)
vmwVtepEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVtepEvent.setStatus(
        "current"
    )

vmwVtepConfigurationFaultEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20066)
)
vmwVtepConfigurationFaultEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVtepConfigurationFaultEvent.setStatus(
        "current"
    )

vmwDLRNetworksNotReachableEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20067)
)
vmwDLRNetworksNotReachableEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDLRNetworksNotReachableEvent.setStatus(
        "current"
    )

vmwVtepSubnetMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20068)
)
vmwVtepSubnetMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVtepSubnetMismatchEvent.setStatus(
        "current"
    )

vmwVtepCountMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20069)
)
vmwVtepCountMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVtepCountMismatchEvent.setStatus(
        "current"
    )

vmwEdgeNetworksNotReachableEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20070)
)
vmwEdgeNetworksNotReachableEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEdgeNetworksNotReachableEvent.setStatus(
        "current"
    )

vmwNiInfraChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20089)
)
vmwNiInfraChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNiInfraChangeEvent.setStatus(
        "current"
    )

vmwDataSourceEnabledChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20090)
)
vmwDataSourceEnabledChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDataSourceEnabledChangeEvent.setStatus(
        "current"
    )

vmwDataSourceDisabledChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20091)
)
vmwDataSourceDisabledChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDataSourceDisabledChangeEvent.setStatus(
        "current"
    )

vmwDataSourceCreatedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20092)
)
vmwDataSourceCreatedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDataSourceCreatedEvent.setStatus(
        "current"
    )

vmwPlatformCpuCoreChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20093)
)
vmwPlatformCpuCoreChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPlatformCpuCoreChangeEvent.setStatus(
        "current"
    )

vmwPlatformDiskChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20094)
)
vmwPlatformDiskChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPlatformDiskChangeEvent.setStatus(
        "current"
    )

vmwPlatformMemoryChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20095)
)
vmwPlatformMemoryChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPlatformMemoryChangeEvent.setStatus(
        "current"
    )

vmwPlatformRebootedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20096)
)
vmwPlatformRebootedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPlatformRebootedEvent.setStatus(
        "current"
    )

vmwProxyCpuCoreChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20097)
)
vmwProxyCpuCoreChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwProxyCpuCoreChangeEvent.setStatus(
        "current"
    )

vmwProxyDiskChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20098)
)
vmwProxyDiskChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwProxyDiskChangeEvent.setStatus(
        "current"
    )

vmwProxyMemoryChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20099)
)
vmwProxyMemoryChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwProxyMemoryChangeEvent.setStatus(
        "current"
    )

vmwProxyRebootedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20100)
)
vmwProxyRebootedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwProxyRebootedEvent.setStatus(
        "current"
    )

vmwNIClusterChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20101)
)
vmwNIClusterChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNIClusterChangeEvent.setStatus(
        "current"
    )

vmwNISystemProxyChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20102)
)
vmwNISystemProxyChangeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNISystemProxyChangeEvent.setStatus(
        "current"
    )

vmwNIClusterCreateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 20103)
)
vmwNIClusterCreateEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNIClusterCreateEvent.setStatus(
        "current"
    )

vmwThresholdExceededEventCpuReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30001)
)
vmwThresholdExceededEventCpuReady.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventCpuReady.setStatus(
        "current"
    )

vmwThresholdExceededEventCpuCoStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30002)
)
vmwThresholdExceededEventCpuCoStop.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventCpuCoStop.setStatus(
        "current"
    )

vmwThresholdExceededEventDiskCommandAbortRule = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30003)
)
vmwThresholdExceededEventDiskCommandAbortRule.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventDiskCommandAbortRule.setStatus(
        "current"
    )

vmwThresholdExceededEventIODeviceLatencyRule = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30004)
)
vmwThresholdExceededEventIODeviceLatencyRule.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventIODeviceLatencyRule.setStatus(
        "current"
    )

vmwThresholdExceededEventIOKernelLatencyRule = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30005)
)
vmwThresholdExceededEventIOKernelLatencyRule.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventIOKernelLatencyRule.setStatus(
        "current"
    )

vmwThresholdExceededEventMemorySwapInRule = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30006)
)
vmwThresholdExceededEventMemorySwapInRule.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventMemorySwapInRule.setStatus(
        "current"
    )

vmwThresholdExceededEventMemorySwapOutRule = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30007)
)
vmwThresholdExceededEventMemorySwapOutRule.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventMemorySwapOutRule.setStatus(
        "current"
    )

vmwThresholdExceededEventNetworkRxDropRule = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30008)
)
vmwThresholdExceededEventNetworkRxDropRule.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventNetworkRxDropRule.setStatus(
        "current"
    )

vmwThresholdExceededEventNetworkTxDropRule = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30009)
)
vmwThresholdExceededEventNetworkTxDropRule.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventNetworkTxDropRule.setStatus(
        "current"
    )

vmwAWSRegionSGLimitEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30010)
)
vmwAWSRegionSGLimitEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwAWSRegionSGLimitEvent.setStatus(
        "current"
    )

vmwAWSVPCSGLimitEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30011)
)
vmwAWSVPCSGLimitEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwAWSVPCSGLimitEvent.setStatus(
        "current"
    )

vmwAWSSGInboundRuleLimitEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30012)
)
vmwAWSSGInboundRuleLimitEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwAWSSGInboundRuleLimitEvent.setStatus(
        "current"
    )

vmwAWSSGOutboundRuleLimitEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30013)
)
vmwAWSSGOutboundRuleLimitEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwAWSSGOutboundRuleLimitEvent.setStatus(
        "current"
    )

vmwAWSInterfaceSGLimitEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30014)
)
vmwAWSInterfaceSGLimitEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwAWSInterfaceSGLimitEvent.setStatus(
        "current"
    )

vmwPacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30100)
)
vmwPacketDropEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPacketDropEvent.setStatus(
        "current"
    )

vmwSwitchPortPacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30101)
)
vmwSwitchPortPacketDropEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSwitchPortPacketDropEvent.setStatus(
        "current"
    )

vmwRouterInterfacePacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30102)
)
vmwRouterInterfacePacketDropEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwRouterInterfacePacketDropEvent.setStatus(
        "current"
    )

vmwVnicPacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30103)
)
vmwVnicPacketDropEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVnicPacketDropEvent.setStatus(
        "current"
    )

vmwVTEPUnderlayPacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30104)
)
vmwVTEPUnderlayPacketDropEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVTEPUnderlayPacketDropEvent.setStatus(
        "current"
    )

vmwPnicUnderlyingSwitchPortPacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30105)
)
vmwPnicUnderlyingSwitchPortPacketDropEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPnicUnderlyingSwitchPortPacketDropEvent.setStatus(
        "current"
    )

vmwDevicePacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30106)
)
vmwDevicePacketDropEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDevicePacketDropEvent.setStatus(
        "current"
    )

vmwSwitchPortUptimeThresholdRecededEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30110)
)
vmwSwitchPortUptimeThresholdRecededEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSwitchPortUptimeThresholdRecededEvent.setStatus(
        "current"
    )

vmwSwitchPortOperationalDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30111)
)
vmwSwitchPortOperationalDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSwitchPortOperationalDownEvent.setStatus(
        "current"
    )

vmwRouterInterfaceOperationalDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30112)
)
vmwRouterInterfaceOperationalDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwRouterInterfaceOperationalDownEvent.setStatus(
        "current"
    )

vmwUnderlayDeviceGenericEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30114)
)
vmwUnderlayDeviceGenericEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnderlayDeviceGenericEvent.setStatus(
        "current"
    )

vmwUnderlayDeviceFexOfflineEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30115)
)
vmwUnderlayDeviceFexOfflineEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnderlayDeviceFexOfflineEvent.setStatus(
        "current"
    )

vmwUnderlayDeviceFanMalFunctionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30116)
)
vmwUnderlayDeviceFanMalFunctionEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnderlayDeviceFanMalFunctionEvent.setStatus(
        "current"
    )

vmwUnderlayDeviceTemperatureThresholdExceededEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30117)
)
vmwUnderlayDeviceTemperatureThresholdExceededEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnderlayDeviceTemperatureThresholdExceededEvent.setStatus(
        "current"
    )

vmwUnderlayDeviceFexFanMalFunctionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30118)
)
vmwUnderlayDeviceFexFanMalFunctionEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnderlayDeviceFexFanMalFunctionEvent.setStatus(
        "current"
    )

vmwUnderlayDeviceFexPsMalFunctionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30119)
)
vmwUnderlayDeviceFexPsMalFunctionEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnderlayDeviceFexPsMalFunctionEvent.setStatus(
        "current"
    )

vmwUnderlayDeviceModuleMalFunctionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30120)
)
vmwUnderlayDeviceModuleMalFunctionEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnderlayDeviceModuleMalFunctionEvent.setStatus(
        "current"
    )

vmwUnderlayDevicePsMalFunctionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30121)
)
vmwUnderlayDevicePsMalFunctionEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnderlayDevicePsMalFunctionEvent.setStatus(
        "current"
    )

vmwUnderlayDeviceBfdSessionRemovedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30122)
)
vmwUnderlayDeviceBfdSessionRemovedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnderlayDeviceBfdSessionRemovedEvent.setStatus(
        "current"
    )

vmwUnderlayDeviceLldpNeighbourRemovedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30123)
)
vmwUnderlayDeviceLldpNeighbourRemovedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnderlayDeviceLldpNeighbourRemovedEvent.setStatus(
        "current"
    )

vmwSwitchPortRPFPacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30124)
)
vmwSwitchPortRPFPacketDropEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSwitchPortRPFPacketDropEvent.setStatus(
        "current"
    )

vmwThresholdExceededEventDataSourceCpuUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30198)
)
vmwThresholdExceededEventDataSourceCpuUsage.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventDataSourceCpuUsage.setStatus(
        "current"
    )

vmwThresholdExceededEventDataSourceMemoryUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30199)
)
vmwThresholdExceededEventDataSourceMemoryUsage.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventDataSourceMemoryUsage.setStatus(
        "current"
    )

vmwThresholdExceededEventDataSourceTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30200)
)
vmwThresholdExceededEventDataSourceTemperature.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventDataSourceTemperature.setStatus(
        "current"
    )

vmwThresholdExceededEventDatastoreFreeSpaceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30203)
)
vmwThresholdExceededEventDatastoreFreeSpaceWarning.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventDatastoreFreeSpaceWarning.setStatus(
        "current"
    )

vmwThresholdExceededEventDatastoreFreeSpaceCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30204)
)
vmwThresholdExceededEventDatastoreFreeSpaceCritical.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventDatastoreFreeSpaceCritical.setStatus(
        "current"
    )

vmwThresholdExceededEventDatastoreReadLatency = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30205)
)
vmwThresholdExceededEventDatastoreReadLatency.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventDatastoreReadLatency.setStatus(
        "current"
    )

vmwThresholdExceededEventDatastoreWriteLatency = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 30206)
)
vmwThresholdExceededEventDatastoreWriteLatency.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwThresholdExceededEventDatastoreWriteLatency.setStatus(
        "current"
    )

vmwDistributedFirewallApplyHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35001)
)
vmwDistributedFirewallApplyHostEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDistributedFirewallApplyHostEvent.setStatus(
        "current"
    )

vmwDistributedFirewallApplyVMEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35002)
)
vmwDistributedFirewallApplyVMEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDistributedFirewallApplyVMEvent.setStatus(
        "current"
    )

vmwNsxEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35003)
)
vmwNsxEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNsxEvent.setStatus(
        "current"
    )

vmwFeatureImpactedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35004)
)
vmwFeatureImpactedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFeatureImpactedEvent.setStatus(
        "current"
    )

vmwNSXComponentEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35221)
)
vmwNSXComponentEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXComponentEvent.setStatus(
        "current"
    )

vmwNSXBackupEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35222)
)
vmwNSXBackupEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXBackupEvent.setStatus(
        "current"
    )

vmwNSXBackupAuditLogExcludedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35223)
)
vmwNSXBackupAuditLogExcludedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXBackupAuditLogExcludedEvent.setStatus(
        "current"
    )

vmwNSXUnsecureBackupEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35224)
)
vmwNSXUnsecureBackupEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXUnsecureBackupEvent.setStatus(
        "current"
    )

vmwNSXBackupSystemEventsExcludedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35225)
)
vmwNSXBackupSystemEventsExcludedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXBackupSystemEventsExcludedEvent.setStatus(
        "current"
    )

vmwNSXBackupNotScheduledEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35226)
)
vmwNSXBackupNotScheduledEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXBackupNotScheduledEvent.setStatus(
        "current"
    )

vmwNSXBackupNotRecordedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35227)
)
vmwNSXBackupNotRecordedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXBackupNotRecordedEvent.setStatus(
        "current"
    )

vmwNSXNtpServerEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35228)
)
vmwNSXNtpServerEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXNtpServerEvent.setStatus(
        "current"
    )

vmwNSXSysLogServerEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35229)
)
vmwNSXSysLogServerEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXSysLogServerEvent.setStatus(
        "current"
    )

vmwControllerSysLogServerEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35230)
)
vmwControllerSysLogServerEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwControllerSysLogServerEvent.setStatus(
        "current"
    )

vmwNSXIpV6EnabledEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35231)
)
vmwNSXIpV6EnabledEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXIpV6EnabledEvent.setStatus(
        "current"
    )

vmwNSXOspfNeighborDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 35232)
)
vmwNSXOspfNeighborDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXOspfNeighborDownEvent.setStatus(
        "current"
    )

vmwClusterFeatureVersionMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36022)
)
vmwClusterFeatureVersionMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwClusterFeatureVersionMismatchEvent.setStatus(
        "current"
    )

vmwHostFeatureVersionMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36023)
)
vmwHostFeatureVersionMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostFeatureVersionMismatchEvent.setStatus(
        "current"
    )

vmwFeatureVersionMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36024)
)
vmwFeatureVersionMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFeatureVersionMismatchEvent.setStatus(
        "current"
    )

vmwHostFeatureEnabledMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36025)
)
vmwHostFeatureEnabledMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostFeatureEnabledMismatchEvent.setStatus(
        "current"
    )

vmwHostFeatureInstalledMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36026)
)
vmwHostFeatureInstalledMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostFeatureInstalledMismatchEvent.setStatus(
        "current"
    )

vmwHostVtepNotFoundEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36027)
)
vmwHostVtepNotFoundEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostVtepNotFoundEvent.setStatus(
        "current"
    )

vmwHostVtepDisconnectedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36028)
)
vmwHostVtepDisconnectedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostVtepDisconnectedEvent.setStatus(
        "current"
    )

vmwHostVtepEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36029)
)
vmwHostVtepEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostVtepEvent.setStatus(
        "current"
    )

vmwClusterHostsVtepMTUMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36030)
)
vmwClusterHostsVtepMTUMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwClusterHostsVtepMTUMismatchEvent.setStatus(
        "current"
    )

vmwFeatureUnhealthyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36031)
)
vmwFeatureUnhealthyEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFeatureUnhealthyEvent.setStatus(
        "current"
    )

vmwEdgeHANotConfiguredEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36032)
)
vmwEdgeHANotConfiguredEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEdgeHANotConfiguredEvent.setStatus(
        "current"
    )

vmwEdgeInterfacesDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36033)
)
vmwEdgeInterfacesDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEdgeInterfacesDownEvent.setStatus(
        "current"
    )

vmwModuleUnhealthyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36041)
)
vmwModuleUnhealthyEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwModuleUnhealthyEvent.setStatus(
        "current"
    )

vmwModuleNotLoadedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36042)
)
vmwModuleNotLoadedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwModuleNotLoadedEvent.setStatus(
        "current"
    )

vmwModuleNetworkConnectionFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36043)
)
vmwModuleNetworkConnectionFailureEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwModuleNetworkConnectionFailureEvent.setStatus(
        "current"
    )

vmwHostNetworkControlPlaneMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36044)
)
vmwHostNetworkControlPlaneMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostNetworkControlPlaneMismatchEvent.setStatus(
        "current"
    )

vmwHostNetworkControlPlaneConnectionFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36045)
)
vmwHostNetworkControlPlaneConnectionFailureEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostNetworkControlPlaneConnectionFailureEvent.setStatus(
        "current"
    )

vmwHostNetworkControlPlaneNotSyncedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36046)
)
vmwHostNetworkControlPlaneNotSyncedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostNetworkControlPlaneNotSyncedEvent.setStatus(
        "current"
    )

vmwNSXControllerClusterMajorityEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36047)
)
vmwNSXControllerClusterMajorityEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXControllerClusterMajorityEvent.setStatus(
        "current"
    )

vmwNSXControllersVMOnSameHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36048)
)
vmwNSXControllersVMOnSameHostEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXControllersVMOnSameHostEvent.setStatus(
        "current"
    )

vmwVxLanRangeExhaustEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36049)
)
vmwVxLanRangeExhaustEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVxLanRangeExhaustEvent.setStatus(
        "current"
    )

vmwNSXFirewallDefaultAllowAllRulesEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36050)
)
vmwNSXFirewallDefaultAllowAllRulesEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXFirewallDefaultAllowAllRulesEvent.setStatus(
        "current"
    )

vmwLogicalRouterNoUplinkEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36051)
)
vmwLogicalRouterNoUplinkEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwLogicalRouterNoUplinkEvent.setStatus(
        "current"
    )

vmwEdgeNotHAEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36052)
)
vmwEdgeNotHAEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEdgeNotHAEvent.setStatus(
        "current"
    )

vmwEdgeNotDeployedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36053)
)
vmwEdgeNotDeployedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEdgeNotDeployedEvent.setStatus(
        "current"
    )

vmwEcmpIsEnabledAndStatefulServicesAreUpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36054)
)
vmwEcmpIsEnabledAndStatefulServicesAreUpEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEcmpIsEnabledAndStatefulServicesAreUpEvent.setStatus(
        "current"
    )

vmwLogicalRouterDeployedOnEcmpEdgeHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36055)
)
vmwLogicalRouterDeployedOnEcmpEdgeHostEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwLogicalRouterDeployedOnEcmpEdgeHostEvent.setStatus(
        "current"
    )

vmwEdgeMissingInterfaceOSPFAreaMappingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36056)
)
vmwEdgeMissingInterfaceOSPFAreaMappingEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEdgeMissingInterfaceOSPFAreaMappingEvent.setStatus(
        "current"
    )

vmwOspfInsecureAuthRouterEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36057)
)
vmwOspfInsecureAuthRouterEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwOspfInsecureAuthRouterEvent.setStatus(
        "current"
    )

vmwNSXControllersDeployedCountEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36058)
)
vmwNSXControllersDeployedCountEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXControllersDeployedCountEvent.setStatus(
        "current"
    )

vmwNSXControllerNotActiveCountEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36059)
)
vmwNSXControllerNotActiveCountEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXControllerNotActiveCountEvent.setStatus(
        "current"
    )

vmwNSXControllerEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36060)
)
vmwNSXControllerEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXControllerEvent.setStatus(
        "current"
    )

vmwNSXEcmpEdgeDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36061)
)
vmwNSXEcmpEdgeDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXEcmpEdgeDownEvent.setStatus(
        "current"
    )

vmwNSXMajorityEcmpEdgesDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36062)
)
vmwNSXMajorityEcmpEdgesDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXMajorityEcmpEdgesDownEvent.setStatus(
        "current"
    )

vmwNSXAllEcmpEdgesDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36063)
)
vmwNSXAllEcmpEdgesDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXAllEcmpEdgesDownEvent.setStatus(
        "current"
    )

vmwNSXEdgeMtuMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36064)
)
vmwNSXEdgeMtuMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXEdgeMtuMismatchEvent.setStatus(
        "current"
    )

vmwNSXEdgeSplitBrainEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36065)
)
vmwNSXEdgeSplitBrainEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXEdgeSplitBrainEvent.setStatus(
        "current"
    )

vmwVirtualDistributedRoutingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36066)
)
vmwVirtualDistributedRoutingEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVirtualDistributedRoutingEvent.setStatus(
        "current"
    )

vmwNSXEdgeBGPNeighbourDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 36067)
)
vmwNSXEdgeBGPNeighbourDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXEdgeBGPNeighbourDownEvent.setStatus(
        "current"
    )

vmwAnalyticsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 37001)
)
vmwAnalyticsEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwAnalyticsEvent.setStatus(
        "current"
    )

vmwAnalyticsOutlierEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 37002)
)
vmwAnalyticsOutlierEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwAnalyticsOutlierEvent.setStatus(
        "current"
    )

vmwAnalyticsThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 37003)
)
vmwAnalyticsThresholdEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwAnalyticsThresholdEvent.setStatus(
        "current"
    )

vmwAnalyticsThresholdCompositeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 37004)
)
vmwAnalyticsThresholdCompositeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwAnalyticsThresholdCompositeEvent.setStatus(
        "current"
    )

vmwAnalyticsThresholdCompositeProblemEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 37006)
)
vmwAnalyticsThresholdCompositeProblemEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwAnalyticsThresholdCompositeProblemEvent.setStatus(
        "current"
    )

vmwVMCEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 38001)
)
vmwVMCEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMCEvent.setStatus(
        "current"
    )

vmwVMCSDDCTGWConnectivityFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 38003)
)
vmwVMCSDDCTGWConnectivityFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMCSDDCTGWConnectivityFailedEvent.setStatus(
        "current"
    )

vmwCriticalHostNotAccessibleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 40001)
)
vmwCriticalHostNotAccessibleEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwCriticalHostNotAccessibleEvent.setStatus(
        "current"
    )

vmwGenericNSXSystemEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70000)
)
vmwGenericNSXSystemEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwGenericNSXSystemEvent.setStatus(
        "current"
    )

vmwFilterConfigApplyOnHostFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70001)
)
vmwFilterConfigApplyOnHostFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFilterConfigApplyOnHostFailedEvent.setStatus(
        "current"
    )

vmwRulesetLoadOnHostFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70002)
)
vmwRulesetLoadOnHostFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwRulesetLoadOnHostFailedEvent.setStatus(
        "current"
    )

vmwConfigUpdateOnHostFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70003)
)
vmwConfigUpdateOnHostFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwConfigUpdateOnHostFailedEvent.setStatus(
        "current"
    )

vmwSpoofguardConfigUpdateOnHostFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70004)
)
vmwSpoofguardConfigUpdateOnHostFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSpoofguardConfigUpdateOnHostFailedEvent.setStatus(
        "current"
    )

vmwApplyRuleToVnicFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70005)
)
vmwApplyRuleToVnicFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwApplyRuleToVnicFailedEvent.setStatus(
        "current"
    )

vmwContainerConfigUpdateOnVnicFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70006)
)
vmwContainerConfigUpdateOnVnicFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwContainerConfigUpdateOnVnicFailedEvent.setStatus(
        "current"
    )

vmwSpoofguardApplyToVnicFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70007)
)
vmwSpoofguardApplyToVnicFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSpoofguardApplyToVnicFailedEvent.setStatus(
        "current"
    )

vmwHostMessagingConfigurationFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70008)
)
vmwHostMessagingConfigurationFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostMessagingConfigurationFailedEvent.setStatus(
        "current"
    )

vmwHostMessagingConnectionReconfigurationFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70009)
)
vmwHostMessagingConnectionReconfigurationFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostMessagingConnectionReconfigurationFailedEvent.setStatus(
        "current"
    )

vmwHostMessagingConfigurationFailedNotificationSkippedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70010)
)
vmwHostMessagingConfigurationFailedNotificationSkippedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostMessagingConfigurationFailedNotificationSkippedEvent.setStatus(
        "current"
    )

vmwHostMessagingInfrastructureDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70011)
)
vmwHostMessagingInfrastructureDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostMessagingInfrastructureDownEvent.setStatus(
        "current"
    )

vmwEdgeVMNotRespondingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70012)
)
vmwEdgeVMNotRespondingEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEdgeVMNotRespondingEvent.setStatus(
        "current"
    )

vmwEdgeUnhealthyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70013)
)
vmwEdgeUnhealthyEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEdgeUnhealthyEvent.setStatus(
        "current"
    )

vmwEdgeVMCommunicationFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70014)
)
vmwEdgeVMCommunicationFailureEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwEdgeVMCommunicationFailureEvent.setStatus(
        "current"
    )

vmwNSXEdgeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 70015)
)
vmwNSXEdgeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXEdgeEvent.setStatus(
        "current"
    )

vmwOtherCriticalNSXEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 71000)
)
vmwOtherCriticalNSXEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwOtherCriticalNSXEvent.setStatus(
        "current"
    )

vmwPanEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80000)
)
vmwPanEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPanEvent.setStatus(
        "current"
    )

vmwPanNsxNotInRegisteredStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80001)
)
vmwPanNsxNotInRegisteredStateEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPanNsxNotInRegisteredStateEvent.setStatus(
        "current"
    )

vmwPanNsxDynamicUpdateDelayedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80002)
)
vmwPanNsxDynamicUpdateDelayedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPanNsxDynamicUpdateDelayedEvent.setStatus(
        "current"
    )

vmwPanDeviceInDisconnectedStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80003)
)
vmwPanDeviceInDisconnectedStateEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPanDeviceInDisconnectedStateEvent.setStatus(
        "current"
    )

vmwPanNsxServiceApplianceViewMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80004)
)
vmwPanNsxServiceApplianceViewMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPanNsxServiceApplianceViewMismatchEvent.setStatus(
        "current"
    )

vmwPanNsxFabricAgentNotFoundOnHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80005)
)
vmwPanNsxFabricAgentNotFoundOnHostEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPanNsxFabricAgentNotFoundOnHostEvent.setStatus(
        "current"
    )

vmwPanNsxServiceVMNotFoundOnHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80006)
)
vmwPanNsxServiceVMNotFoundOnHostEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPanNsxServiceVMNotFoundOnHostEvent.setStatus(
        "current"
    )

vmwPanLogInsightDroppedFlowEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80050)
)
vmwPanLogInsightDroppedFlowEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPanLogInsightDroppedFlowEvent.setStatus(
        "current"
    )

vmwCPLogInsightDroppedFlowEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80051)
)
vmwCPLogInsightDroppedFlowEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwCPLogInsightDroppedFlowEvent.setStatus(
        "current"
    )

vmwCheckpointEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80100)
)
vmwCheckpointEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwCheckpointEvent.setStatus(
        "current"
    )

vmwCheckpointNsxFabricAgentNotFoundOnHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80102)
)
vmwCheckpointNsxFabricAgentNotFoundOnHostEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwCheckpointNsxFabricAgentNotFoundOnHostEvent.setStatus(
        "current"
    )

vmwCheckpointNsxServiceVMNotFoundOnHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80103)
)
vmwCheckpointNsxServiceVMNotFoundOnHostEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwCheckpointNsxServiceVMNotFoundOnHostEvent.setStatus(
        "current"
    )

vmwCheckpointGatewaySicStatusNotCommunicatingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80104)
)
vmwCheckpointGatewaySicStatusNotCommunicatingEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwCheckpointGatewaySicStatusNotCommunicatingEvent.setStatus(
        "current"
    )

vmwCheckpointNsxServiceApplianceViewMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80105)
)
vmwCheckpointNsxServiceApplianceViewMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwCheckpointNsxServiceApplianceViewMismatchEvent.setStatus(
        "current"
    )

vmwNSXTEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80200)
)
vmwNSXTEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTEvent.setStatus(
        "current"
    )

vmwNSXTVcNotAddedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80201)
)
vmwNSXTVcNotAddedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTVcNotAddedEvent.setStatus(
        "current"
    )

vmwNSXTStandaloneHostsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80202)
)
vmwNSXTStandaloneHostsEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTStandaloneHostsEvent.setStatus(
        "current"
    )

vmwNSXTSystemEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80203)
)
vmwNSXTSystemEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTSystemEvent.setStatus(
        "current"
    )

vmwNSXTNoUplinkConnectivityEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80205)
)
vmwNSXTNoUplinkConnectivityEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTNoUplinkConnectivityEvent.setStatus(
        "current"
    )

vmwNSXTRoutingAdvertisementEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80206)
)
vmwNSXTRoutingAdvertisementEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTRoutingAdvertisementEvent.setStatus(
        "current"
    )

vmwNSXTManagerConnectivityDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80207)
)
vmwNSXTManagerConnectivityDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTManagerConnectivityDownEvent.setStatus(
        "current"
    )

vmwNSXTControllerConnectivityDegradedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80208)
)
vmwNSXTControllerConnectivityDegradedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTControllerConnectivityDegradedEvent.setStatus(
        "current"
    )

vmwNSXTControllerConnectivityDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80209)
)
vmwNSXTControllerConnectivityDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTControllerConnectivityDownEvent.setStatus(
        "current"
    )

vmwNSXTMtuMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80210)
)
vmwNSXTMtuMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMtuMismatchEvent.setStatus(
        "current"
    )

vmwNSXTExcludedVmFlowEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80211)
)
vmwNSXTExcludedVmFlowEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTExcludedVmFlowEvent.setStatus(
        "current"
    )

vmwNSXTDoubleVlanTaggingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80212)
)
vmwNSXTDoubleVlanTaggingEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTDoubleVlanTaggingEvent.setStatus(
        "current"
    )

vmwNSXTNoTzAttachedOnTnEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80213)
)
vmwNSXTNoTzAttachedOnTnEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTNoTzAttachedOnTnEvent.setStatus(
        "current"
    )

vmwNSXTVtepDeleteEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80214)
)
vmwNSXTVtepDeleteEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTVtepDeleteEvent.setStatus(
        "current"
    )

vmwDuplicateL3SwitchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80215)
)
vmwDuplicateL3SwitchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDuplicateL3SwitchEvent.setStatus(
        "current"
    )

vmwLBPoolMemberDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80216)
)
vmwLBPoolMemberDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwLBPoolMemberDownEvent.setStatus(
        "current"
    )

vmwLBPoolDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80217)
)
vmwLBPoolDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwLBPoolDownEvent.setStatus(
        "current"
    )

vmwLBPoolEmptyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80218)
)
vmwLBPoolEmptyEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwLBPoolEmptyEvent.setStatus(
        "current"
    )

vmwLBPoolMemberVMDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80219)
)
vmwLBPoolMemberVMDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwLBPoolMemberVMDownEvent.setStatus(
        "current"
    )

vmwLBVirtualServerDisableEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80220)
)
vmwLBVirtualServerDisableEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwLBVirtualServerDisableEvent.setStatus(
        "current"
    )

vmwLBServiceNodeIPNotFoundEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80221)
)
vmwLBServiceNodeIPNotFoundEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwLBServiceNodeIPNotFoundEvent.setStatus(
        "current"
    )

vmwLBServiceNodeMultipleNicFoundEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80222)
)
vmwLBServiceNodeMultipleNicFoundEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwLBServiceNodeMultipleNicFoundEvent.setStatus(
        "current"
    )

vmwNSXTSwitchIpfixEnabledEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80223)
)
vmwNSXTSwitchIpfixEnabledEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTSwitchIpfixEnabledEvent.setStatus(
        "current"
    )

vmwNSXTStandaloneHostsWithoutVcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80224)
)
vmwNSXTStandaloneHostsWithoutVcEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTStandaloneHostsWithoutVcEvent.setStatus(
        "current"
    )

vmwNSXTControllerNodeToControlClusterConnectivityEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80225)
)
vmwNSXTControllerNodeToControlClusterConnectivityEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTControllerNodeToControlClusterConnectivityEvent.setStatus(
        "current"
    )

vmwNSXTControllerNodeToMgmtPlaneConnectivityEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80226)
)
vmwNSXTControllerNodeToMgmtPlaneConnectivityEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTControllerNodeToMgmtPlaneConnectivityEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeToMgmtClusterConnectivityEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80227)
)
vmwNSXTMPNodeToMgmtClusterConnectivityEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeToMgmtClusterConnectivityEvent.setStatus(
        "current"
    )

vmwNSXTHostNodePnicStatusDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80228)
)
vmwNSXTHostNodePnicStatusDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTHostNodePnicStatusDownEvent.setStatus(
        "current"
    )

vmwNSXTHostNodePnicStatusDegradedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80229)
)
vmwNSXTHostNodePnicStatusDegradedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTHostNodePnicStatusDegradedEvent.setStatus(
        "current"
    )

vmwNSXTHostNodePnicStatusUnknownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80230)
)
vmwNSXTHostNodePnicStatusUnknownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTHostNodePnicStatusUnknownEvent.setStatus(
        "current"
    )

vmwNSXTHostNodeTunnelStatusDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80231)
)
vmwNSXTHostNodeTunnelStatusDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTHostNodeTunnelStatusDownEvent.setStatus(
        "current"
    )

vmwNSXTHostNodeTunnelStatusDegradedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80232)
)
vmwNSXTHostNodeTunnelStatusDegradedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTHostNodeTunnelStatusDegradedEvent.setStatus(
        "current"
    )

vmwNSXTHostNodeTunnelStatusUnknownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80233)
)
vmwNSXTHostNodeTunnelStatusUnknownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTHostNodeTunnelStatusUnknownEvent.setStatus(
        "current"
    )

vmwNSXTHostNodeStatusDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80234)
)
vmwNSXTHostNodeStatusDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTHostNodeStatusDownEvent.setStatus(
        "current"
    )

vmwNSXTHostNodeStatusDegradedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80235)
)
vmwNSXTHostNodeStatusDegradedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTHostNodeStatusDegradedEvent.setStatus(
        "current"
    )

vmwNSXTHostNodeStatusUnknownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80236)
)
vmwNSXTHostNodeStatusUnknownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTHostNodeStatusUnknownEvent.setStatus(
        "current"
    )

vmwNSXTEdgeNodePnicStatusDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80237)
)
vmwNSXTEdgeNodePnicStatusDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTEdgeNodePnicStatusDownEvent.setStatus(
        "current"
    )

vmwNSXTEdgeNodePnicStatusDegradedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80238)
)
vmwNSXTEdgeNodePnicStatusDegradedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTEdgeNodePnicStatusDegradedEvent.setStatus(
        "current"
    )

vmwNSXTEdgeNodePnicStatusUnknownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80239)
)
vmwNSXTEdgeNodePnicStatusUnknownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTEdgeNodePnicStatusUnknownEvent.setStatus(
        "current"
    )

vmwNSXTEdgeNodeTunnelStatusDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80240)
)
vmwNSXTEdgeNodeTunnelStatusDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTEdgeNodeTunnelStatusDownEvent.setStatus(
        "current"
    )

vmwNSXTEdgeNodeTunnelStatusDegradedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80241)
)
vmwNSXTEdgeNodeTunnelStatusDegradedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTEdgeNodeTunnelStatusDegradedEvent.setStatus(
        "current"
    )

vmwNSXTEdgeNodeTunnelStatusUnknownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80242)
)
vmwNSXTEdgeNodeTunnelStatusUnknownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTEdgeNodeTunnelStatusUnknownEvent.setStatus(
        "current"
    )

vmwNSXTEdgeNodeStatusDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80243)
)
vmwNSXTEdgeNodeStatusDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTEdgeNodeStatusDownEvent.setStatus(
        "current"
    )

vmwNSXTEdgeNodeStatusDegradedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80244)
)
vmwNSXTEdgeNodeStatusDegradedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTEdgeNodeStatusDegradedEvent.setStatus(
        "current"
    )

vmwNSXTEdgeNodeStatusUnknownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80245)
)
vmwNSXTEdgeNodeStatusUnknownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTEdgeNodeStatusUnknownEvent.setStatus(
        "current"
    )

vmwNSXTHostNodeMgmtConnectivityStatusDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80246)
)
vmwNSXTHostNodeMgmtConnectivityStatusDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTHostNodeMgmtConnectivityStatusDownEvent.setStatus(
        "current"
    )

vmwNSXTEdgeNodeCtlrConnectivityStatusUnknownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80247)
)
vmwNSXTEdgeNodeCtlrConnectivityStatusUnknownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTEdgeNodeCtlrConnectivityStatusUnknownEvent.setStatus(
        "current"
    )

vmwNSXTHostNodeCtlrConnectivityStatusDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80248)
)
vmwNSXTHostNodeCtlrConnectivityStatusDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTHostNodeCtlrConnectivityStatusDownEvent.setStatus(
        "current"
    )

vmwNSXTHostNodeCtlrConnectivityStatusDegradedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80249)
)
vmwNSXTHostNodeCtlrConnectivityStatusDegradedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTHostNodeCtlrConnectivityStatusDegradedEvent.setStatus(
        "current"
    )

vmwNSXTHostNodeCtlrConnectivityStatusUnknownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80250)
)
vmwNSXTHostNodeCtlrConnectivityStatusUnknownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTHostNodeCtlrConnectivityStatusUnknownEvent.setStatus(
        "current"
    )

vmwNSXTLogicalSwitchAdminStatusDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80252)
)
vmwNSXTLogicalSwitchAdminStatusDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTLogicalSwitchAdminStatusDownEvent.setStatus(
        "current"
    )

vmwNSXTLogicalPortOperationalStatusDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80253)
)
vmwNSXTLogicalPortOperationalStatusDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTLogicalPortOperationalStatusDownEvent.setStatus(
        "current"
    )

vmwNSXTLogicalPortOperationalStatusUnknownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80254)
)
vmwNSXTLogicalPortOperationalStatusUnknownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTLogicalPortOperationalStatusUnknownEvent.setStatus(
        "current"
    )

vmwNSXTComputeManagerConnectionStatusNotUpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80255)
)
vmwNSXTComputeManagerConnectionStatusNotUpEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTComputeManagerConnectionStatusNotUpEvent.setStatus(
        "current"
    )

vmwNSXTClusterBackUpDisabledEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80256)
)
vmwNSXTClusterBackUpDisabledEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTClusterBackUpDisabledEvent.setStatus(
        "current"
    )

vmwNSXTDFWFirewallDisabledEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80257)
)
vmwNSXTDFWFirewallDisabledEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTDFWFirewallDisabledEvent.setStatus(
        "current"
    )

vmwNSXTLogicalPortReceivedPacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80258)
)
vmwNSXTLogicalPortReceivedPacketDropEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTLogicalPortReceivedPacketDropEvent.setStatus(
        "current"
    )

vmwNSXTLogicalPortTransmittedPacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80259)
)
vmwNSXTLogicalPortTransmittedPacketDropEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTLogicalPortTransmittedPacketDropEvent.setStatus(
        "current"
    )

vmwNSXTLogicalSwitchReceivedPacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80260)
)
vmwNSXTLogicalSwitchReceivedPacketDropEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTLogicalSwitchReceivedPacketDropEvent.setStatus(
        "current"
    )

vmwNSXTLogicalSwitchTransmittedPacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80261)
)
vmwNSXTLogicalSwitchTransmittedPacketDropEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTLogicalSwitchTransmittedPacketDropEvent.setStatus(
        "current"
    )

vmwNSXTRxPacketDropOnMPNicEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80262)
)
vmwNSXTRxPacketDropOnMPNicEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTRxPacketDropOnMPNicEvent.setStatus(
        "current"
    )

vmwNSXTRxPacketDropOnEdgeTnNicEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80263)
)
vmwNSXTRxPacketDropOnEdgeTnNicEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTRxPacketDropOnEdgeTnNicEvent.setStatus(
        "current"
    )

vmwNSXTRxPacketDropOnHostTnNicEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80264)
)
vmwNSXTRxPacketDropOnHostTnNicEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTRxPacketDropOnHostTnNicEvent.setStatus(
        "current"
    )

vmwNSXTTxPacketDropOnMPNicEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80265)
)
vmwNSXTTxPacketDropOnMPNicEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTTxPacketDropOnMPNicEvent.setStatus(
        "current"
    )

vmwNSXTTxPacketDropOnEdgeTnNicEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80266)
)
vmwNSXTTxPacketDropOnEdgeTnNicEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTTxPacketDropOnEdgeTnNicEvent.setStatus(
        "current"
    )

vmwNSXTTxPacketDropOnHostTnNicEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80267)
)
vmwNSXTTxPacketDropOnHostTnNicEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTTxPacketDropOnHostTnNicEvent.setStatus(
        "current"
    )

vmwNatRuleLargeSubnetEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80270)
)
vmwNatRuleLargeSubnetEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNatRuleLargeSubnetEvent.setStatus(
        "current"
    )

vmwNSXTEdgeNodeMaintenanceModeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80271)
)
vmwNSXTEdgeNodeMaintenanceModeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTEdgeNodeMaintenanceModeEvent.setStatus(
        "current"
    )

vmwNSXTHostNodeMaintenanceModeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80272)
)
vmwNSXTHostNodeMaintenanceModeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTHostNodeMaintenanceModeEvent.setStatus(
        "current"
    )

vmwNSXTEdgeDVPGsIPFIXDisabledEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80273)
)
vmwNSXTEdgeDVPGsIPFIXDisabledEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTEdgeDVPGsIPFIXDisabledEvent.setStatus(
        "current"
    )

vmwNSXTRouterInterfaceRPFPacketDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80274)
)
vmwNSXTRouterInterfaceRPFPacketDropEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTRouterInterfaceRPFPacketDropEvent.setStatus(
        "current"
    )

vmwNsxtIpfixMultipleCollectorConfigurationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80275)
)
vmwNsxtIpfixMultipleCollectorConfigurationEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNsxtIpfixMultipleCollectorConfigurationEvent.setStatus(
        "current"
    )

vmwHardwareVTEPMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80301)
)
vmwHardwareVTEPMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHardwareVTEPMismatchEvent.setStatus(
        "current"
    )

vmwHardwareVTEPPortDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80302)
)
vmwHardwareVTEPPortDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHardwareVTEPPortDownEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceCmInventoryStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80402)
)
vmwNSXTMPNodeServiceCmInventoryStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceCmInventoryStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceControllerStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80403)
)
vmwNSXTMPNodeServiceControllerStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceControllerStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceDataStoreStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80404)
)
vmwNSXTMPNodeServiceDataStoreStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceDataStoreStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceHttpStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80405)
)
vmwNSXTMPNodeServiceHttpStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceHttpStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceInstallUpgradeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80406)
)
vmwNSXTMPNodeServiceInstallUpgradeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceInstallUpgradeEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceLiagentStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80407)
)
vmwNSXTMPNodeServiceLiagentStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceLiagentStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceManagerStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80408)
)
vmwNSXTMPNodeServiceManagerStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceManagerStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceMgmtPlaneBusStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80409)
)
vmwNSXTMPNodeServiceMgmtPlaneBusStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceMgmtPlaneBusStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceMigrationCoordinatorStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80410)
)
vmwNSXTMPNodeServiceMigrationCoordinatorStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceMigrationCoordinatorStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceNodeMgmtStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80411)
)
vmwNSXTMPNodeServiceNodeMgmtStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceNodeMgmtStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceNodeStatsStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80412)
)
vmwNSXTMPNodeServiceNodeStatsStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceNodeStatsStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceNSXMessageBusStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80413)
)
vmwNSXTMPNodeServiceNSXMessageBusStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceNSXMessageBusStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceNSXPlatformClientStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80414)
)
vmwNSXTMPNodeServiceNSXPlatformClientStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceNSXPlatformClientStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceNSXUpgradeAgentStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80415)
)
vmwNSXTMPNodeServiceNSXUpgradeAgentStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceNSXUpgradeAgentStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceNTPStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80416)
)
vmwNSXTMPNodeServiceNTPStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceNTPStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServicePolicyStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80417)
)
vmwNSXTMPNodeServicePolicyStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServicePolicyStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceSearchStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80418)
)
vmwNSXTMPNodeServiceSearchStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceSearchStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceSNMPStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80419)
)
vmwNSXTMPNodeServiceSNMPStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceSNMPStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceSSHStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80420)
)
vmwNSXTMPNodeServiceSSHStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceSSHStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceSyslogStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80421)
)
vmwNSXTMPNodeServiceSyslogStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceSyslogStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceTelemetryStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80422)
)
vmwNSXTMPNodeServiceTelemetryStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceTelemetryStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceUIServiceStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80423)
)
vmwNSXTMPNodeServiceUIServiceStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceUIServiceStatusEvent.setStatus(
        "current"
    )

vmwNSXTMPNodeServiceClusterManagerStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80424)
)
vmwNSXTMPNodeServiceClusterManagerStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTMPNodeServiceClusterManagerStatusEvent.setStatus(
        "current"
    )

vmwIndexerLagEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80501)
)
vmwIndexerLagEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwIndexerLagEvent.setStatus(
        "current"
    )

vmwIPFIXFlowDPPausedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80502)
)
vmwIPFIXFlowDPPausedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwIPFIXFlowDPPausedEvent.setStatus(
        "current"
    )

vmwGridProcessingStoppedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80503)
)
vmwGridProcessingStoppedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwGridProcessingStoppedEvent.setStatus(
        "current"
    )

vmwUnableToSendEmailsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80504)
)
vmwUnableToSendEmailsEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnableToSendEmailsEvent.setStatus(
        "current"
    )

vmwSMTPNotConfiguredEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80505)
)
vmwSMTPNotConfiguredEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSMTPNotConfiguredEvent.setStatus(
        "current"
    )

vmwSNMPNotConfiguredEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80506)
)
vmwSNMPNotConfiguredEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSNMPNotConfiguredEvent.setStatus(
        "current"
    )

vmwReindexingInProgressEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80507)
)
vmwReindexingInProgressEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwReindexingInProgressEvent.setStatus(
        "current"
    )

vmwNodesVersionMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80508)
)
vmwNodesVersionMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNodesVersionMismatchEvent.setStatus(
        "current"
    )

vmwNotAllServicesRunningEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80509)
)
vmwNotAllServicesRunningEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNotAllServicesRunningEvent.setStatus(
        "current"
    )

vmwNotAllServicesHealthyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80510)
)
vmwNotAllServicesHealthyEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNotAllServicesHealthyEvent.setStatus(
        "current"
    )

vmwExpandPartitionFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80511)
)
vmwExpandPartitionFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwExpandPartitionFailedEvent.setStatus(
        "current"
    )

vmwDiskCleanupFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80512)
)
vmwDiskCleanupFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDiskCleanupFailedEvent.setStatus(
        "current"
    )

vmwVaccumFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80513)
)
vmwVaccumFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVaccumFailedEvent.setStatus(
        "current"
    )

vmwConfigStoreCleanupFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80514)
)
vmwConfigStoreCleanupFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwConfigStoreCleanupFailedEvent.setStatus(
        "current"
    )

vmwHBaseRetentionToolFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80515)
)
vmwHBaseRetentionToolFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHBaseRetentionToolFailedEvent.setStatus(
        "current"
    )

vmwMetricStoreUpdaterFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80516)
)
vmwMetricStoreUpdaterFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwMetricStoreUpdaterFailedEvent.setStatus(
        "current"
    )

vmwCollectorLagEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80517)
)
vmwCollectorLagEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwCollectorLagEvent.setStatus(
        "current"
    )

vmwCollectionLagEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80518)
)
vmwCollectionLagEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwCollectionLagEvent.setStatus(
        "current"
    )

vmwGridProcessingLagEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80519)
)
vmwGridProcessingLagEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwGridProcessingLagEvent.setStatus(
        "current"
    )

vmwConnectionErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80520)
)
vmwConnectionErrorEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwConnectionErrorEvent.setStatus(
        "current"
    )

vmwNodeNotActiveEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80521)
)
vmwNodeNotActiveEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNodeNotActiveEvent.setStatus(
        "current"
    )

vmwHighDiskUtilizationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80522)
)
vmwHighDiskUtilizationEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHighDiskUtilizationEvent.setStatus(
        "current"
    )

vmwIndexingAbortedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80523)
)
vmwIndexingAbortedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwIndexingAbortedEvent.setStatus(
        "current"
    )

vmwUpgradeFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80524)
)
vmwUpgradeFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUpgradeFailedEvent.setStatus(
        "current"
    )

vmwFlowProcessingSuspendedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80525)
)
vmwFlowProcessingSuspendedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFlowProcessingSuspendedEvent.setStatus(
        "current"
    )

vmwLargeSdmsDroppedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80526)
)
vmwLargeSdmsDroppedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwLargeSdmsDroppedEvent.setStatus(
        "current"
    )

vmwApplianceNotConfiguredEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80527)
)
vmwApplianceNotConfiguredEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwApplianceNotConfiguredEvent.setStatus(
        "current"
    )

vmwDiskAllocationInsufficientEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80528)
)
vmwDiskAllocationInsufficientEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDiskAllocationInsufficientEvent.setStatus(
        "current"
    )

vmwFdbConfigStoreCleanupFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80531)
)
vmwFdbConfigStoreCleanupFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFdbConfigStoreCleanupFailedEvent.setStatus(
        "current"
    )

vmwDeploymentDefMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80532)
)
vmwDeploymentDefMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDeploymentDefMismatchEvent.setStatus(
        "current"
    )

vmwLicenseExpiredEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80537)
)
vmwLicenseExpiredEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwLicenseExpiredEvent.setStatus(
        "current"
    )

vmwInGracePeriodEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80538)
)
vmwInGracePeriodEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwInGracePeriodEvent.setStatus(
        "current"
    )

vmwUnableToSendSNMPTrapsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80539)
)
vmwUnableToSendSNMPTrapsEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnableToSendSNMPTrapsEvent.setStatus(
        "current"
    )

vmwStreamProcessingFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80540)
)
vmwStreamProcessingFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwStreamProcessingFailedEvent.setStatus(
        "current"
    )

vmwIpfixFlowLagEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80541)
)
vmwIpfixFlowLagEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwIpfixFlowLagEvent.setStatus(
        "current"
    )

vmwChangeEventsDroppedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80542)
)
vmwChangeEventsDroppedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwChangeEventsDroppedEvent.setStatus(
        "current"
    )

vmwServiceRestartCountExceededEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80544)
)
vmwServiceRestartCountExceededEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwServiceRestartCountExceededEvent.setStatus(
        "current"
    )

vmwFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80601)
)
vmwFailedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFailedEvent.setStatus(
        "current"
    )

vmwTimeoutEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80602)
)
vmwTimeoutEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwTimeoutEvent.setStatus(
        "current"
    )

vmwConnectionRefusedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80603)
)
vmwConnectionRefusedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwConnectionRefusedEvent.setStatus(
        "current"
    )

vmwSNOWMandatoryPrivilegesMissingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80604)
)
vmwSNOWMandatoryPrivilegesMissingEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSNOWMandatoryPrivilegesMissingEvent.setStatus(
        "current"
    )

vmwIncorrectConnectionStringEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80605)
)
vmwIncorrectConnectionStringEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwIncorrectConnectionStringEvent.setStatus(
        "current"
    )

vmwInvalidCredentialsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80606)
)
vmwInvalidCredentialsEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwInvalidCredentialsEvent.setStatus(
        "current"
    )

vmwUnknownHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80608)
)
vmwUnknownHostEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnknownHostEvent.setStatus(
        "current"
    )

vmwSNMPConnectionInvalidEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80609)
)
vmwSNMPConnectionInvalidEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSNMPConnectionInvalidEvent.setStatus(
        "current"
    )

vmwFailedCredsEncryptEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80611)
)
vmwFailedCredsEncryptEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFailedCredsEncryptEvent.setStatus(
        "current"
    )

vmwPwdAuthModeDisabledEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80612)
)
vmwPwdAuthModeDisabledEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPwdAuthModeDisabledEvent.setStatus(
        "current"
    )

vmwInsufficientPrivilegesEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80613)
)
vmwInsufficientPrivilegesEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwInsufficientPrivilegesEvent.setStatus(
        "current"
    )

vmwNotFoundEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80614)
)
vmwNotFoundEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNotFoundEvent.setStatus(
        "current"
    )

vmwInvalidConfigEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80616)
)
vmwInvalidConfigEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwInvalidConfigEvent.setStatus(
        "current"
    )

vmwWarnConfigEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80617)
)
vmwWarnConfigEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwWarnConfigEvent.setStatus(
        "current"
    )

vmwUnexpectedDSTypeOrVersionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80618)
)
vmwUnexpectedDSTypeOrVersionEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnexpectedDSTypeOrVersionEvent.setStatus(
        "current"
    )

vmwNSXControllerNotFoundEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80619)
)
vmwNSXControllerNotFoundEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXControllerNotFoundEvent.setStatus(
        "current"
    )

vmwHostNotReachableEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80620)
)
vmwHostNotReachableEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostNotReachableEvent.setStatus(
        "current"
    )

vmwInvalidResponseFromDatasourceEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80621)
)
vmwInvalidResponseFromDatasourceEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwInvalidResponseFromDatasourceEvent.setStatus(
        "current"
    )

vmwDataProviderNotRunningEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80622)
)
vmwDataProviderNotRunningEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDataProviderNotRunningEvent.setStatus(
        "current"
    )

vmwPrimaryNSXNotAddedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80623)
)
vmwPrimaryNSXNotAddedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPrimaryNSXNotAddedEvent.setStatus(
        "current"
    )

vmwHostnameResolutionErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80624)
)
vmwHostnameResolutionErrorEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHostnameResolutionErrorEvent.setStatus(
        "current"
    )

vmwNumVMsOrHostsNotFoundEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80625)
)
vmwNumVMsOrHostsNotFoundEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNumVMsOrHostsNotFoundEvent.setStatus(
        "current"
    )

vmwNSXIPFIXStatusMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80626)
)
vmwNSXIPFIXStatusMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXIPFIXStatusMismatchEvent.setStatus(
        "current"
    )

vmwFlowPhysicalNodeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80627)
)
vmwFlowPhysicalNodeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFlowPhysicalNodeEvent.setStatus(
        "current"
    )

vmwNotEmptyNodeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80628)
)
vmwNotEmptyNodeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNotEmptyNodeEvent.setStatus(
        "current"
    )

vmwUnsupportedNSXTVersionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80629)
)
vmwUnsupportedNSXTVersionEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnsupportedNSXTVersionEvent.setStatus(
        "current"
    )

vmwComputeManagersNotFoundEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80630)
)
vmwComputeManagersNotFoundEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwComputeManagersNotFoundEvent.setStatus(
        "current"
    )

vmwComputeManagersNotAddedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80631)
)
vmwComputeManagersNotAddedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwComputeManagersNotAddedEvent.setStatus(
        "current"
    )

vmwUnsupportedLogInsightVersionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80632)
)
vmwUnsupportedLogInsightVersionEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnsupportedLogInsightVersionEvent.setStatus(
        "current"
    )

vmwUnsupportedVRNIContentPackVersionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80633)
)
vmwUnsupportedVRNIContentPackVersionEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnsupportedVRNIContentPackVersionEvent.setStatus(
        "current"
    )

vmwVRNIContentPackNotInstalledEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80634)
)
vmwVRNIContentPackNotInstalledEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVRNIContentPackNotInstalledEvent.setStatus(
        "current"
    )

vmwWebhookNotEnabledOnAlertEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80635)
)
vmwWebhookNotEnabledOnAlertEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwWebhookNotEnabledOnAlertEvent.setStatus(
        "current"
    )

vmwIncorrectWebhookConfiguredOnAlertEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80636)
)
vmwIncorrectWebhookConfiguredOnAlertEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwIncorrectWebhookConfiguredOnAlertEvent.setStatus(
        "current"
    )

vmwWebhookNotRunningEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80637)
)
vmwWebhookNotRunningEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwWebhookNotRunningEvent.setStatus(
        "current"
    )

vmwInfobloxRecordLimitExceededEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80638)
)
vmwInfobloxRecordLimitExceededEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwInfobloxRecordLimitExceededEvent.setStatus(
        "current"
    )

vmwIncorrectInfobloxCredentialEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80639)
)
vmwIncorrectInfobloxCredentialEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwIncorrectInfobloxCredentialEvent.setStatus(
        "current"
    )

vmwUnsupportedInfobloxVersionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80640)
)
vmwUnsupportedInfobloxVersionEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnsupportedInfobloxVersionEvent.setStatus(
        "current"
    )

vmwUnknownInfobloxVersionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80641)
)
vmwUnknownInfobloxVersionEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnknownInfobloxVersionEvent.setStatus(
        "current"
    )

vmwNoDVSAvailableEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80642)
)
vmwNoDVSAvailableEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNoDVSAvailableEvent.setStatus(
        "current"
    )

vmwVCNotOnSameProxyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80643)
)
vmwVCNotOnSameProxyEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVCNotOnSameProxyEvent.setStatus(
        "current"
    )

vmwNSXTIPFixNoCollectorProfileEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80644)
)
vmwNSXTIPFixNoCollectorProfileEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTIPFixNoCollectorProfileEvent.setStatus(
        "current"
    )

vmwNSXTIPFixNoNewCollectorProfileCanBeAddedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80645)
)
vmwNSXTIPFixNoNewCollectorProfileCanBeAddedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTIPFixNoNewCollectorProfileCanBeAddedEvent.setStatus(
        "current"
    )

vmwNSXTIPFixNoIPFixProfileEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80646)
)
vmwNSXTIPFixNoIPFixProfileEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTIPFixNoIPFixProfileEvent.setStatus(
        "current"
    )

vmwNSXTIPFixIPFixProfilePriorityNotZeroEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80647)
)
vmwNSXTIPFixIPFixProfilePriorityNotZeroEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTIPFixIPFixProfilePriorityNotZeroEvent.setStatus(
        "current"
    )

vmwNSXTIPFixCollectorAndIPFixProfileMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80648)
)
vmwNSXTIPFixCollectorAndIPFixProfileMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTIPFixCollectorAndIPFixProfileMismatchEvent.setStatus(
        "current"
    )

vmwNSXTIPFixPortIncorrectEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80649)
)
vmwNSXTIPFixPortIncorrectEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTIPFixPortIncorrectEvent.setStatus(
        "current"
    )

vmwNSXTIPFixDFWStatusNotEnabledEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80650)
)
vmwNSXTIPFixDFWStatusNotEnabledEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTIPFixDFWStatusNotEnabledEvent.setStatus(
        "current"
    )

vmwPolicyManagerNoDfwIPFixProfile = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80651)
)
vmwPolicyManagerNoDfwIPFixProfile.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPolicyManagerNoDfwIPFixProfile.setStatus(
        "current"
    )

vmwPolicyManagerVrniDfwIPFixCollectorAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80652)
)
vmwPolicyManagerVrniDfwIPFixCollectorAbsent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPolicyManagerVrniDfwIPFixCollectorAbsent.setStatus(
        "current"
    )

vmwDatasourceIdentificationChangedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80653)
)
vmwDatasourceIdentificationChangedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwDatasourceIdentificationChangedEvent.setStatus(
        "current"
    )

vmwPKSKubernetesUnknownHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80654)
)
vmwPKSKubernetesUnknownHostEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPKSKubernetesUnknownHostEvent.setStatus(
        "current"
    )

vmwKubernetesInsufficientPrivilegesEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80655)
)
vmwKubernetesInsufficientPrivilegesEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwKubernetesInsufficientPrivilegesEvent.setStatus(
        "current"
    )

vmwUANIFileNotProvidedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80657)
)
vmwUANIFileNotProvidedEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUANIFileNotProvidedEvent.setStatus(
        "current"
    )

vmwUANIFileDoesNotExistEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80658)
)
vmwUANIFileDoesNotExistEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUANIFileDoesNotExistEvent.setStatus(
        "current"
    )

vmwNSXTLatencyNotEnabledEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80659)
)
vmwNSXTLatencyNotEnabledEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTLatencyNotEnabledEvent.setStatus(
        "current"
    )

vmwNSXTLatencyMoreBFDProfileEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80660)
)
vmwNSXTLatencyMoreBFDProfileEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTLatencyMoreBFDProfileEvent.setStatus(
        "current"
    )

vmwNSXTLatencyNoBFDProfileEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80661)
)
vmwNSXTLatencyNoBFDProfileEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTLatencyNoBFDProfileEvent.setStatus(
        "current"
    )

vmwNSXTLatencyCollectorMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80662)
)
vmwNSXTLatencyCollectorMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXTLatencyCollectorMismatchEvent.setStatus(
        "current"
    )

vmwBigIpInsufficientShellAccessEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80663)
)
vmwBigIpInsufficientShellAccessEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwBigIpInsufficientShellAccessEvent.setStatus(
        "current"
    )

vmwBigIpInsufficientPartitionAccessEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80664)
)
vmwBigIpInsufficientPartitionAccessEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwBigIpInsufficientPartitionAccessEvent.setStatus(
        "current"
    )

vmwBigIpInsufficientRoleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80665)
)
vmwBigIpInsufficientRoleEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwBigIpInsufficientRoleEvent.setStatus(
        "current"
    )

vmwNsxtLatencyStatProfileMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80667)
)
vmwNsxtLatencyStatProfileMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNsxtLatencyStatProfileMismatchEvent.setStatus(
        "current"
    )

vmwNsxtLatencyNodeGroupMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80668)
)
vmwNsxtLatencyNodeGroupMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNsxtLatencyNodeGroupMismatchEvent.setStatus(
        "current"
    )

vmwNsxtLatencyServiceConfigMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80669)
)
vmwNsxtLatencyServiceConfigMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNsxtLatencyServiceConfigMismatchEvent.setStatus(
        "current"
    )

vmwNsxtNotificationWebhookDisabledEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80670)
)
vmwNsxtNotificationWebhookDisabledEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNsxtNotificationWebhookDisabledEvent.setStatus(
        "current"
    )

vmwFailedDatasourceOperationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80672)
)
vmwFailedDatasourceOperationEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFailedDatasourceOperationEvent.setStatus(
        "current"
    )

vmwUnsupportedNsxAlbVersionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80700)
)
vmwUnsupportedNsxAlbVersionEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnsupportedNsxAlbVersionEvent.setStatus(
        "current"
    )

vmwTkgiKubernetesNotReachableEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80800)
)
vmwTkgiKubernetesNotReachableEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwTkgiKubernetesNotReachableEvent.setStatus(
        "current"
    )

vmwTkgiClustersInsufficientPriviledgesEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 80801)
)
vmwTkgiClustersInsufficientPriviledgesEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwTkgiClustersInsufficientPriviledgesEvent.setStatus(
        "current"
    )

vmwVeloCloudEdgeDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90001)
)
vmwVeloCloudEdgeDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVeloCloudEdgeDownEvent.setStatus(
        "current"
    )

vmwVeloCloudLinkDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90002)
)
vmwVeloCloudLinkDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVeloCloudLinkDownEvent.setStatus(
        "current"
    )

vmwVeloCloudLinkLostPacketEventTx = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90005)
)
vmwVeloCloudLinkLostPacketEventTx.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVeloCloudLinkLostPacketEventTx.setStatus(
        "current"
    )

vmwVeloCloudLinkDegradedVoiceQoeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90007)
)
vmwVeloCloudLinkDegradedVoiceQoeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVeloCloudLinkDegradedVoiceQoeEvent.setStatus(
        "current"
    )

vmwVeloCloudLinkDegradedVideoQoeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90008)
)
vmwVeloCloudLinkDegradedVideoQoeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVeloCloudLinkDegradedVideoQoeEvent.setStatus(
        "current"
    )

vmwVeloCloudLinkDegradedTransQoeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90009)
)
vmwVeloCloudLinkDegradedTransQoeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVeloCloudLinkDegradedTransQoeEvent.setStatus(
        "current"
    )

vmwVeloCloudEdgeDegradedVoiceQoeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90010)
)
vmwVeloCloudEdgeDegradedVoiceQoeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVeloCloudEdgeDegradedVoiceQoeEvent.setStatus(
        "current"
    )

vmwVeloCloudEdgeDegradedVideoQoeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90011)
)
vmwVeloCloudEdgeDegradedVideoQoeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVeloCloudEdgeDegradedVideoQoeEvent.setStatus(
        "current"
    )

vmwVeloCloudEdgeDegradedTransQoeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90012)
)
vmwVeloCloudEdgeDegradedTransQoeEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVeloCloudEdgeDegradedTransQoeEvent.setStatus(
        "current"
    )

vmwVeloCloudLinkLostPacketEventRx = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90013)
)
vmwVeloCloudLinkLostPacketEventRx.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVeloCloudLinkLostPacketEventRx.setStatus(
        "current"
    )

vmwSDWanLinkTrafficThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90017)
)
vmwSDWanLinkTrafficThresholdEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSDWanLinkTrafficThresholdEvent.setStatus(
        "current"
    )

vmwHcxIXServiceStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90501)
)
vmwHcxIXServiceStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxIXServiceStatusEvent.setStatus(
        "current"
    )

vmwHcxIXApplianceEncryptionTunnelStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90502)
)
vmwHcxIXApplianceEncryptionTunnelStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxIXApplianceEncryptionTunnelStatusEvent.setStatus(
        "current"
    )

vmwHcxNEServiceStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90503)
)
vmwHcxNEServiceStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxNEServiceStatusEvent.setStatus(
        "current"
    )

vmwHcxNEApplianceEncryptionTunnelStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90504)
)
vmwHcxNEApplianceEncryptionTunnelStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxNEApplianceEncryptionTunnelStatusEvent.setStatus(
        "current"
    )

vmwHcxIXApplianceServicePipelineStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90505)
)
vmwHcxIXApplianceServicePipelineStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxIXApplianceServicePipelineStatusEvent.setStatus(
        "current"
    )

vmwHcxNEApplianceServicePipelineStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90506)
)
vmwHcxNEApplianceServicePipelineStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxNEApplianceServicePipelineStatusEvent.setStatus(
        "current"
    )

vmwHcxIXApplianceServiceTransportStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90507)
)
vmwHcxIXApplianceServiceTransportStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxIXApplianceServiceTransportStatusEvent.setStatus(
        "current"
    )

vmwHcxNEApplianceServiceTransportStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90508)
)
vmwHcxNEApplianceServiceTransportStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxNEApplianceServiceTransportStatusEvent.setStatus(
        "current"
    )

vmwHcxIXApplianceServiceSystemStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90509)
)
vmwHcxIXApplianceServiceSystemStateEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxIXApplianceServiceSystemStateEvent.setStatus(
        "current"
    )

vmwHcxNEApplianceServiceSystemStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90510)
)
vmwHcxNEApplianceServiceSystemStateEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxNEApplianceServiceSystemStateEvent.setStatus(
        "current"
    )

vmwHcxWanOptServiceStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90511)
)
vmwHcxWanOptServiceStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxWanOptServiceStatusEvent.setStatus(
        "current"
    )

vmwHcxBMServiceStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90512)
)
vmwHcxBMServiceStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxBMServiceStatusEvent.setStatus(
        "current"
    )

vmwHcxVMotionServiceStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90513)
)
vmwHcxVMotionServiceStatusEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxVMotionServiceStatusEvent.setStatus(
        "current"
    )

vmwHcxIXServiceNotRunningEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90514)
)
vmwHcxIXServiceNotRunningEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxIXServiceNotRunningEvent.setStatus(
        "current"
    )

vmwHcxNEServiceNotRunningEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90515)
)
vmwHcxNEServiceNotRunningEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxNEServiceNotRunningEvent.setStatus(
        "current"
    )

vmwHcxWanOptServiceNotRunningEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90516)
)
vmwHcxWanOptServiceNotRunningEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxWanOptServiceNotRunningEvent.setStatus(
        "current"
    )

vmwHcxApplianceAllTunnelDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90517)
)
vmwHcxApplianceAllTunnelDownEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxApplianceAllTunnelDownEvent.setStatus(
        "current"
    )

vmwHcxConnectionRuleViolationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90518)
)
vmwHcxConnectionRuleViolationEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxConnectionRuleViolationEvent.setStatus(
        "current"
    )

vmwHcxMtuMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90519)
)
vmwHcxMtuMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxMtuMismatchEvent.setStatus(
        "current"
    )

vmwHcxApplianceUnhealthyTunnelsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90520)
)
vmwHcxApplianceUnhealthyTunnelsEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxApplianceUnhealthyTunnelsEvent.setStatus(
        "current"
    )

vmwHcxManagerVersionMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90521)
)
vmwHcxManagerVersionMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxManagerVersionMismatchEvent.setStatus(
        "current"
    )

vmwHcxApplianceVersionMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 90522)
)
vmwHcxApplianceVersionMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwHcxApplianceVersionMismatchEvent.setStatus(
        "current"
    )

vmwNSXVLatencyNoDataEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 100001)
)
vmwNSXVLatencyNoDataEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNSXVLatencyNoDataEvent.setStatus(
        "current"
    )

vmwVMCVMLimitExceededEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 100051)
)
vmwVMCVMLimitExceededEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMCVMLimitExceededEvent.setStatus(
        "current"
    )

vmwVMCHostLimitExceededEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 100052)
)
vmwVMCHostLimitExceededEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMCHostLimitExceededEvent.setStatus(
        "current"
    )

vmwVMCHostPerClusterLimitExceededEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 100053)
)
vmwVMCHostPerClusterLimitExceededEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMCHostPerClusterLimitExceededEvent.setStatus(
        "current"
    )

vmwVMCVMPerHostLimitExceededEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 100054)
)
vmwVMCVMPerHostLimitExceededEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMCVMPerHostLimitExceededEvent.setStatus(
        "current"
    )

vmwVMCClusterLimitExceededEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 100055)
)
vmwVMCClusterLimitExceededEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMCClusterLimitExceededEvent.setStatus(
        "current"
    )

vmwVMCCapacityThresholdBreachEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 100056)
)
vmwVMCCapacityThresholdBreachEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwVMCCapacityThresholdBreachEvent.setStatus(
        "current"
    )

vmwProtectionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 100061)
)
vmwProtectionEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwProtectionEvent.setStatus(
        "current"
    )

vmwNativeVlanMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 110011)
)
vmwNativeVlanMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNativeVlanMismatchEvent.setStatus(
        "current"
    )

vmwNativeVlanTaggingMismatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 110012)
)
vmwNativeVlanTaggingMismatchEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwNativeVlanTaggingMismatchEvent.setStatus(
        "current"
    )

vmwSnapshotNotBuildingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 110013)
)
vmwSnapshotNotBuildingEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSnapshotNotBuildingEvent.setStatus(
        "current"
    )

vmwProtectionActiveEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 110015)
)
vmwProtectionActiveEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwProtectionActiveEvent.setStatus(
        "current"
    )

vmwSNMPTrapEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 110017)
)
vmwSNMPTrapEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwSNMPTrapEvent.setStatus(
        "current"
    )

vmwFlowCollectionErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 8061313)
)
vmwFlowCollectionErrorEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwFlowCollectionErrorEvent.setStatus(
        "current"
    )

vmwAWSThrottlingExceptionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 8061314)
)
vmwAWSThrottlingExceptionEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwAWSThrottlingExceptionEvent.setStatus(
        "current"
    )

vmwAWSFlowLogAccessDeniedExceptionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 8061315)
)
vmwAWSFlowLogAccessDeniedExceptionEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwAWSFlowLogAccessDeniedExceptionEvent.setStatus(
        "current"
    )

vmwPwdAuthModeDisabledAristaEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 806100012)
)
vmwPwdAuthModeDisabledAristaEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwPwdAuthModeDisabledAristaEvent.setStatus(
        "current"
    )

vmwUnsupportedNSXVersionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 0, 806100018)
)
vmwUnsupportedNSXVersionEvent.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwEventSeverity"),
        ("VMWARE-VRNI-MIB", "vmwAffectedObject"),
        ("VMWARE-VRNI-MIB", "vmwOperatorDesc"),
        ("VMWARE-VRNI-MIB", "vmwVrniUrl"),
        ("VMWARE-VRNI-MIB", "vmwTimestamp"),
        ("VMWARE-VRNI-MIB", "vmwEventName"))
)
if mibBuilder.loadTexts:
    vmwUnsupportedNSXVersionEvent.setStatus(
        "current"
    )


# Notifications groups

vmwNetworkInsightNotificationGroup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 3)
)
vmwNetworkInsightNotificationGroup1.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwSnmpTrapsAreConfigured"),
        ("VMWARE-VRNI-MIB", "vmwSnmpTrapsAreDisabled"),
        ("VMWARE-VRNI-MIB", "vmwTestTrap"),
        ("VMWARE-VRNI-MIB", "vmwEntityDiscoveryChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwEntityPropertiesChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwFirewallNotInstalledOnHostEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostWithStaleFirewallRulesEvent"),
        ("VMWARE-VRNI-MIB", "vmwIpAddressChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwL2GatewayAnomalyEvent"),
        ("VMWARE-VRNI-MIB", "vmwL2NetworkAddressAnomalyEvent"),
        ("VMWARE-VRNI-MIB", "vmwL2NetworkDiameterExceededEvent"),
        ("VMWARE-VRNI-MIB", "vmwL2NetworkUplinkMissingEvent"),
        ("VMWARE-VRNI-MIB", "vmwL2NetworkWithNoVMsEvent"),
        ("VMWARE-VRNI-MIB", "vmwLayer2NetworkDiameterChangedEvent"),
        ("VMWARE-VRNI-MIB", "vmwMTUMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwNetworkIsolationEvent"),
        ("VMWARE-VRNI-MIB", "vmwNoPathEvent"),
        ("VMWARE-VRNI-MIB", "vmwSpoofguardDisabledEvent"),
        ("VMWARE-VRNI-MIB", "vmwVMotionEvent"),
        ("VMWARE-VRNI-MIB", "vmwVMWithDisconnectedVnicsEvent"),
        ("VMWARE-VRNI-MIB", "vmwVMWithMulipleVnicsOnDifferentVxlansEvent"),
        ("VMWARE-VRNI-MIB", "vmwVMWithMulipleVnicsOnSameL2Event"),
        ("VMWARE-VRNI-MIB", "vmwVMWithNoIpAddressEvent"),
        ("VMWARE-VRNI-MIB", "vmwVTEPMissingEvent"),
        ("VMWARE-VRNI-MIB", "vmwL2Event"),
        ("VMWARE-VRNI-MIB", "vmwMembershipChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwSecurityGroupMembershipChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwFirewallRuleMembershipChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwVlanMembershipChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwVxlanMembershipChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwDeleteChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwVtepFailedPingEvent"),
        ("VMWARE-VRNI-MIB", "vmwEmptySearchStreamChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwSearchStreamMembershipChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwEmptySearchStreamProblemEvent"),
        ("VMWARE-VRNI-MIB", "vmwSearchStreamMembershipProblemEvent"),
        ("VMWARE-VRNI-MIB", "vmwOspfConfigurationMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwServiceVMNotHealthyEvent"),
        ("VMWARE-VRNI-MIB", "vmwServiceVMNotPoweredOnEvent"),
        ("VMWARE-VRNI-MIB", "vmwServiceVMHighCPUUsageEvent"),
        ("VMWARE-VRNI-MIB", "vmwServiceVMHighMemoryUsageEvent"),
        ("VMWARE-VRNI-MIB", "vmwServiceVMHighDiskUsageEvent"),
        ("VMWARE-VRNI-MIB", "vmwIPSetPropertiesChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwFirewallRulePropertiesChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwSecurityGroupPropertiesChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwIPSetMembershipChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwFirewallRuleMaskEvent"),
        ("VMWARE-VRNI-MIB", "vmwSecurityMembershipChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwSecurityTagPropertiesChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwSecurityTagMembershipChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostDatastoreChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwVMDatastoreChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwVMSnapshotChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwVMVirtualDiskChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwIPSetDefinitionMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwSegmentMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwVtepEvent"),
        ("VMWARE-VRNI-MIB", "vmwVtepConfigurationFaultEvent"),
        ("VMWARE-VRNI-MIB", "vmwVtepSubnetMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwVtepCountMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwDLRNetworksNotReachableEvent"),
        ("VMWARE-VRNI-MIB", "vmwEdgeNetworksNotReachableEvent"),
        ("VMWARE-VRNI-MIB", "vmwThresholdExceededEventCpuReady"),
        ("VMWARE-VRNI-MIB", "vmwThresholdExceededEventCpuCoStop"),
        ("VMWARE-VRNI-MIB", "vmwThresholdExceededEventDiskCommandAbortRule"),
        ("VMWARE-VRNI-MIB", "vmwThresholdExceededEventIODeviceLatencyRule"),
        ("VMWARE-VRNI-MIB", "vmwThresholdExceededEventIOKernelLatencyRule"),
        ("VMWARE-VRNI-MIB", "vmwThresholdExceededEventMemorySwapInRule"),
        ("VMWARE-VRNI-MIB", "vmwThresholdExceededEventMemorySwapOutRule"),
        ("VMWARE-VRNI-MIB", "vmwThresholdExceededEventNetworkRxDropRule"),
        ("VMWARE-VRNI-MIB", "vmwThresholdExceededEventNetworkTxDropRule"),
        ("VMWARE-VRNI-MIB", "vmwPacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwSwitchPortPacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwRouterInterfacePacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwVnicPacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwVTEPUnderlayPacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwPnicUnderlyingSwitchPortPacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwDevicePacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwThresholdExceededEventDatastoreFreeSpaceWarning"),
        ("VMWARE-VRNI-MIB", "vmwThresholdExceededEventDatastoreFreeSpaceCritical"),
        ("VMWARE-VRNI-MIB", "vmwThresholdExceededEventDatastoreReadLatency"),
        ("VMWARE-VRNI-MIB", "vmwThresholdExceededEventDatastoreWriteLatency"),
        ("VMWARE-VRNI-MIB", "vmwDistributedFirewallApplyHostEvent"),
        ("VMWARE-VRNI-MIB", "vmwDistributedFirewallApplyVMEvent"),
        ("VMWARE-VRNI-MIB", "vmwNsxEvent"),
        ("VMWARE-VRNI-MIB", "vmwFeatureImpactedEvent"),
        ("VMWARE-VRNI-MIB", "vmwClusterFeatureVersionMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostFeatureVersionMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwFeatureVersionMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostFeatureEnabledMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostFeatureInstalledMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostVtepNotFoundEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostVtepDisconnectedEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostVtepEvent"),
        ("VMWARE-VRNI-MIB", "vmwClusterHostsVtepMTUMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwFeatureUnhealthyEvent"),
        ("VMWARE-VRNI-MIB", "vmwEdgeHANotConfiguredEvent"),
        ("VMWARE-VRNI-MIB", "vmwEdgeInterfacesDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwModuleUnhealthyEvent"),
        ("VMWARE-VRNI-MIB", "vmwModuleNotLoadedEvent"),
        ("VMWARE-VRNI-MIB", "vmwModuleNetworkConnectionFailureEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostNetworkControlPlaneMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostNetworkControlPlaneConnectionFailureEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostNetworkControlPlaneNotSyncedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXControllerClusterMajorityEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXControllersVMOnSameHostEvent"),
        ("VMWARE-VRNI-MIB", "vmwVxLanRangeExhaustEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXFirewallDefaultAllowAllRulesEvent"),
        ("VMWARE-VRNI-MIB", "vmwEdgeNotHAEvent"),
        ("VMWARE-VRNI-MIB", "vmwEdgeNotDeployedEvent"),
        ("VMWARE-VRNI-MIB", "vmwEcmpIsEnabledAndStatefulServicesAreUpEvent"),
        ("VMWARE-VRNI-MIB", "vmwLogicalRouterDeployedOnEcmpEdgeHostEvent"),
        ("VMWARE-VRNI-MIB", "vmwEdgeMissingInterfaceOSPFAreaMappingEvent"),
        ("VMWARE-VRNI-MIB", "vmwOspfInsecureAuthRouterEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXControllersDeployedCountEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXControllerNotActiveCountEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXControllerEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXBackupEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXUnsecureBackupEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXBackupSystemEventsExcludedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXBackupNotScheduledEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXBackupNotRecordedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXNtpServerEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXSysLogServerEvent"),
        ("VMWARE-VRNI-MIB", "vmwControllerSysLogServerEvent"),
        ("VMWARE-VRNI-MIB", "vmwGenericNSXSystemEvent"),
        ("VMWARE-VRNI-MIB", "vmwOtherCriticalNSXEvent"),
        ("VMWARE-VRNI-MIB", "vmwFilterConfigApplyOnHostFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwRulesetLoadOnHostFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwConfigUpdateOnHostFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwSpoofguardConfigUpdateOnHostFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwApplyRuleToVnicFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwContainerConfigUpdateOnVnicFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwSpoofguardApplyToVnicFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostMessagingConfigurationFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostMessagingConnectionReconfigurationFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostMessagingConfigurationFailedNotificationSkippedEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostMessagingInfrastructureDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwEdgeVMNotRespondingEvent"),
        ("VMWARE-VRNI-MIB", "vmwEdgeUnhealthyEvent"),
        ("VMWARE-VRNI-MIB", "vmwEdgeVMCommunicationFailureEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXEdgeEvent"),
        ("VMWARE-VRNI-MIB", "vmwPanEvent"),
        ("VMWARE-VRNI-MIB", "vmwPanNsxNotInRegisteredStateEvent"),
        ("VMWARE-VRNI-MIB", "vmwPanNsxDynamicUpdateDelayedEvent"),
        ("VMWARE-VRNI-MIB", "vmwPanDeviceInDisconnectedStateEvent"),
        ("VMWARE-VRNI-MIB", "vmwPanNsxServiceApplianceViewMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwPanNsxFabricAgentNotFoundOnHostEvent"),
        ("VMWARE-VRNI-MIB", "vmwPanNsxServiceVMNotFoundOnHostEvent"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup1.setStatus(
        "current"
    )

vmwNetworkInsightNotificationGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 30)
)
vmwNetworkInsightNotificationGroup2.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwLogicalRouterNoUplinkEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXComponentEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXBackupEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXBackupAuditLogExcludedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXUnsecureBackupEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXBackupSystemEventsExcludedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXBackupNotScheduledEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXBackupNotRecordedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXNtpServerEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXSysLogServerEvent"),
        ("VMWARE-VRNI-MIB", "vmwControllerSysLogServerEvent"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup2.setStatus(
        "current"
    )

vmwNetworkInsightNotificationGroup3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 40)
)
vmwNetworkInsightNotificationGroup3.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwMTUMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwVMWithMulipleVnicsOnSameL2Event"),
        ("VMWARE-VRNI-MIB", "vmwMembershipChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwSecurityGroupMembershipChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwFirewallRuleMembershipChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwVlanMembershipChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwVxlanMembershipChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwSearchStreamMembershipChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwIPSetMembershipChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwSecurityMembershipChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwVtepEvent"),
        ("VMWARE-VRNI-MIB", "vmwPacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwSwitchPortPacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwRouterInterfacePacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwVnicPacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwVTEPUnderlayPacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwPnicUnderlyingSwitchPortPacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostFeatureVersionMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwSpoofguardConfigUpdateOnHostFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXEcmpEdgeDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXMajorityEcmpEdgesDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXAllEcmpEdgesDownEvent"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup3.setStatus(
        "current"
    )

vmwNetworkInsightNotificationGroup4 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 50)
)
vmwNetworkInsightNotificationGroup4.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNSXEdgeSplitBrainEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXIpV6EnabledEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXOspfNeighborDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwCheckpointEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXEdgeMtuMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwCheckpointNsxFabricAgentNotFoundOnHostEvent"),
        ("VMWARE-VRNI-MIB", "vmwCheckpointNsxServiceVMNotFoundOnHostEvent"),
        ("VMWARE-VRNI-MIB", "vmwCheckpointGatewaySicStatusNotCommunicatingEvent"),
        ("VMWARE-VRNI-MIB", "vmwCheckpointNsxServiceApplianceViewMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwCriticalHostNotAccessibleEvent"),
        ("VMWARE-VRNI-MIB", "vmwVlanMembershipChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwClusterFeatureVersionMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostFeatureVersionMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwConfigUpdateOnHostFailedEvent"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup4.setStatus(
        "current"
    )

vmwNetworkInsightNotificationGroup5 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 65)
)
vmwNetworkInsightNotificationGroup5.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNiInfraChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwDataSourceEnabledChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwDataSourceDisabledChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwDataSourceCreatedEvent"),
        ("VMWARE-VRNI-MIB", "vmwPlatformCpuCoreChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwPlatformDiskChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwPlatformMemoryChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwPlatformRebootedEvent"),
        ("VMWARE-VRNI-MIB", "vmwProxyCpuCoreChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwProxyDiskChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwProxyMemoryChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwProxyRebootedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNIClusterChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwNISystemProxyChangeEvent"),
        ("VMWARE-VRNI-MIB", "vmwNIClusterCreateEvent"),
        ("VMWARE-VRNI-MIB", "vmwAWSRegionSGLimitEvent"),
        ("VMWARE-VRNI-MIB", "vmwAWSVPCSGLimitEvent"),
        ("VMWARE-VRNI-MIB", "vmwAWSSGInboundRuleLimitEvent"),
        ("VMWARE-VRNI-MIB", "vmwAWSSGOutboundRuleLimitEvent"),
        ("VMWARE-VRNI-MIB", "vmwAWSInterfaceSGLimitEvent"),
        ("VMWARE-VRNI-MIB", "vmwVirtualDistributedRoutingEvent"),
        ("VMWARE-VRNI-MIB", "vmwIndexerLagEvent"),
        ("VMWARE-VRNI-MIB", "vmwIPFIXFlowDPPausedEvent"),
        ("VMWARE-VRNI-MIB", "vmwGridProcessingStoppedEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnableToSendEmailsEvent"),
        ("VMWARE-VRNI-MIB", "vmwSMTPNotConfiguredEvent"),
        ("VMWARE-VRNI-MIB", "vmwSNMPNotConfiguredEvent"),
        ("VMWARE-VRNI-MIB", "vmwReindexingInProgressEvent"),
        ("VMWARE-VRNI-MIB", "vmwNodesVersionMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwNotAllServicesRunningEvent"),
        ("VMWARE-VRNI-MIB", "vmwNotAllServicesHealthyEvent"),
        ("VMWARE-VRNI-MIB", "vmwExpandPartitionFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwDiskCleanupFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwVaccumFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwConfigStoreCleanupFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwHBaseRetentionToolFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwMetricStoreUpdaterFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwCollectorLagEvent"),
        ("VMWARE-VRNI-MIB", "vmwCollectionLagEvent"),
        ("VMWARE-VRNI-MIB", "vmwGridProcessingLagEvent"),
        ("VMWARE-VRNI-MIB", "vmwConnectionErrorEvent"),
        ("VMWARE-VRNI-MIB", "vmwNodeNotActiveEvent"),
        ("VMWARE-VRNI-MIB", "vmwHighDiskUtilizationEvent"),
        ("VMWARE-VRNI-MIB", "vmwIndexingAbortedEvent"),
        ("VMWARE-VRNI-MIB", "vmwUpgradeFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwFlowProcessingSuspendedEvent"),
        ("VMWARE-VRNI-MIB", "vmwVCNotOnSameProxyEvent"),
        ("VMWARE-VRNI-MIB", "vmwNoDVSAvailableEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnknownInfobloxVersionEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnsupportedInfobloxVersionEvent"),
        ("VMWARE-VRNI-MIB", "vmwIncorrectInfobloxCredentialEvent"),
        ("VMWARE-VRNI-MIB", "vmwInfobloxRecordLimitExceededEvent"),
        ("VMWARE-VRNI-MIB", "vmwWebhookNotRunningEvent"),
        ("VMWARE-VRNI-MIB", "vmwIncorrectWebhookConfiguredOnAlertEvent"),
        ("VMWARE-VRNI-MIB", "vmwWebhookNotEnabledOnAlertEvent"),
        ("VMWARE-VRNI-MIB", "vmwVRNIContentPackNotInstalledEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnsupportedVRNIContentPackVersionEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnsupportedLogInsightVersionEvent"),
        ("VMWARE-VRNI-MIB", "vmwComputeManagersNotAddedEvent"),
        ("VMWARE-VRNI-MIB", "vmwComputeManagersNotFoundEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnsupportedNSXTVersionEvent"),
        ("VMWARE-VRNI-MIB", "vmwNotEmptyNodeEvent"),
        ("VMWARE-VRNI-MIB", "vmwFlowPhysicalNodeEvent"),
        ("VMWARE-VRNI-MIB", "vmwFlowCollectionErrorEvent"),
        ("VMWARE-VRNI-MIB", "vmwAWSThrottlingExceptionEvent"),
        ("VMWARE-VRNI-MIB", "vmwAWSFlowLogAccessDeniedExceptionEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXIPFIXStatusMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwNumVMsOrHostsNotFoundEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnsupportedNSXVersionEvent"),
        ("VMWARE-VRNI-MIB", "vmwPwdAuthModeDisabledAristaEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostnameResolutionErrorEvent"),
        ("VMWARE-VRNI-MIB", "vmwPrimaryNSXNotAddedEvent"),
        ("VMWARE-VRNI-MIB", "vmwDataProviderNotRunningEvent"),
        ("VMWARE-VRNI-MIB", "vmwInvalidResponseFromDatasourceEvent"),
        ("VMWARE-VRNI-MIB", "vmwHostNotReachableEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXControllerNotFoundEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnexpectedDSTypeOrVersionEvent"),
        ("VMWARE-VRNI-MIB", "vmwWarnConfigEvent"),
        ("VMWARE-VRNI-MIB", "vmwInvalidConfigEvent"),
        ("VMWARE-VRNI-MIB", "vmwNotFoundEvent"),
        ("VMWARE-VRNI-MIB", "vmwInsufficientPrivilegesEvent"),
        ("VMWARE-VRNI-MIB", "vmwPwdAuthModeDisabledEvent"),
        ("VMWARE-VRNI-MIB", "vmwFailedCredsEncryptEvent"),
        ("VMWARE-VRNI-MIB", "vmwSNMPConnectionInvalidEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnknownHostEvent"),
        ("VMWARE-VRNI-MIB", "vmwInvalidCredentialsEvent"),
        ("VMWARE-VRNI-MIB", "vmwIncorrectConnectionStringEvent"),
        ("VMWARE-VRNI-MIB", "vmwConnectionRefusedEvent"),
        ("VMWARE-VRNI-MIB", "vmwTimeoutEvent"),
        ("VMWARE-VRNI-MIB", "vmwFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTVcNotAddedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTStandaloneHostsEvent"),
        ("VMWARE-VRNI-MIB", "vmwLargeSdmsDroppedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTIPFixDFWStatusNotEnabledEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTIPFixPortIncorrectEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTIPFixCollectorAndIPFixProfileMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTIPFixIPFixProfilePriorityNotZeroEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTIPFixNoIPFixProfileEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTIPFixNoNewCollectorProfileCanBeAddedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTIPFixNoCollectorProfileEvent"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup5.setStatus(
        "current"
    )

vmwNetworkInsightNotificationGroup6 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 75)
)
vmwNetworkInsightNotificationGroup6.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNSXTSystemEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTNoUplinkConnectivityEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTRoutingAdvertisementEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTManagerConnectivityDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTControllerConnectivityDegradedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTControllerConnectivityDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMtuMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXEdgeBGPNeighbourDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwAnalyticsEvent"),
        ("VMWARE-VRNI-MIB", "vmwAnalyticsOutlierEvent"),
        ("VMWARE-VRNI-MIB", "vmwAnalyticsThresholdEvent"),
        ("VMWARE-VRNI-MIB", "vmwVMCEvent"),
        ("VMWARE-VRNI-MIB", "vmwPolicyManagerVrniDfwIPFixCollectorAbsent"),
        ("VMWARE-VRNI-MIB", "vmwPolicyManagerNoDfwIPFixProfile"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup6.setStatus(
        "current"
    )

vmwNetworkInsightNotificationGroup7 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 85)
)
vmwNetworkInsightNotificationGroup7.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNSXTDoubleVlanTaggingEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTVtepDeleteEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTNoTzAttachedOnTnEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTExcludedVmFlowEvent"),
        ("VMWARE-VRNI-MIB", "vmwKubernetesInsufficientPrivilegesEvent"),
        ("VMWARE-VRNI-MIB", "vmwPKSKubernetesUnknownHostEvent"),
        ("VMWARE-VRNI-MIB", "vmwDatasourceIdentificationChangedEvent"),
        ("VMWARE-VRNI-MIB", "vmwLBPoolMemberDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwLBPoolDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwLBPoolMemberVMDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwLBServiceNodeIPNotFoundEvent"),
        ("VMWARE-VRNI-MIB", "vmwLBServiceNodeMultipleNicFoundEvent"),
        ("VMWARE-VRNI-MIB", "vmwLBVirtualServerDisableEvent"),
        ("VMWARE-VRNI-MIB", "vmwLBPoolEmptyEvent"),
        ("VMWARE-VRNI-MIB", "vmwDuplicateL3SwitchEvent"),
        ("VMWARE-VRNI-MIB", "vmwArkinApplicationMemberLimitEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTSwitchIpfixEnabledEvent"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup7.setStatus(
        "current"
    )

vmwNetworkInsightNotificationGroup8 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 95)
)
vmwNetworkInsightNotificationGroup8.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwUANIFileNotProvidedEvent"),
        ("VMWARE-VRNI-MIB", "vmwUANIFileDoesNotExistEvent"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup8.setStatus(
        "current"
    )

vmwNetworkInsightNotificationGroup9 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 105)
)
vmwNetworkInsightNotificationGroup9.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNSXTStandaloneHostsWithoutVcEvent"),
        ("VMWARE-VRNI-MIB", "vmwApplianceNotConfiguredEvent"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup9.setStatus(
        "current"
    )

vmwNetworkInsightNotificationGroup10 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 115)
)
vmwNetworkInsightNotificationGroup10.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwSwitchPortUptimeThresholdRecededEvent"),
        ("VMWARE-VRNI-MIB", "vmwFdbConfigStoreCleanupFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwDiskAllocationInsufficientEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTControllerNodeToControlClusterConnectivityEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTControllerNodeToMgmtPlaneConnectivityEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeToMgmtClusterConnectivityEvent"),
        ("VMWARE-VRNI-MIB", "vmwBigIpInsufficientShellAccessEvent"),
        ("VMWARE-VRNI-MIB", "vmwBigIpInsufficientPartitionAccessEvent"),
        ("VMWARE-VRNI-MIB", "vmwBigIpInsufficientRoleEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTLatencyCollectorMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTLatencyNoBFDProfileEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTLatencyMoreBFDProfileEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTLatencyNotEnabledEvent"),
        ("VMWARE-VRNI-MIB", "vmwHardwareVTEPMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwHardwareVTEPPortDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXVLatencyNoDataEvent"),
        ("VMWARE-VRNI-MIB", "vmwKubernetesBaseEvent"),
        ("VMWARE-VRNI-MIB", "vmwVMCVMLimitExceededEvent"),
        ("VMWARE-VRNI-MIB", "vmwVMCHostLimitExceededEvent"),
        ("VMWARE-VRNI-MIB", "vmwVeloCloudEdgeDegradedTransQoeEvent"),
        ("VMWARE-VRNI-MIB", "vmwVeloCloudEdgeDegradedVideoQoeEvent"),
        ("VMWARE-VRNI-MIB", "vmwVeloCloudEdgeDegradedVoiceQoeEvent"),
        ("VMWARE-VRNI-MIB", "vmwVeloCloudEdgeDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwVeloCloudLinkLostPacketEventRx"),
        ("VMWARE-VRNI-MIB", "vmwVeloCloudLinkDegradedTransQoeEvent"),
        ("VMWARE-VRNI-MIB", "vmwVeloCloudLinkLostPacketEventTx"),
        ("VMWARE-VRNI-MIB", "vmwVeloCloudLinkDegradedVideoQoeEvent"),
        ("VMWARE-VRNI-MIB", "vmwVeloCloudLinkDegradedVoiceQoeEvent"),
        ("VMWARE-VRNI-MIB", "vmwVeloCloudLinkDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTHostNodeMgmtConnectivityStatusDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTEdgeNodeCtlrConnectivityStatusUnknownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTHostNodeCtlrConnectivityStatusDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTHostNodeCtlrConnectivityStatusDegradedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTHostNodeCtlrConnectivityStatusUnknownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTHostNodePnicStatusDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTHostNodePnicStatusDegradedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTHostNodePnicStatusUnknownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTEdgeNodePnicStatusDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTEdgeNodePnicStatusDegradedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTEdgeNodePnicStatusUnknownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTHostNodeTunnelStatusDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTHostNodeTunnelStatusDegradedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTHostNodeTunnelStatusUnknownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTEdgeNodeTunnelStatusDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTEdgeNodeTunnelStatusDegradedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTEdgeNodeTunnelStatusUnknownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTHostNodeStatusDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTHostNodeStatusDegradedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTHostNodeStatusUnknownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTEdgeNodeStatusDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTEdgeNodeStatusDegradedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTEdgeNodeStatusUnknownEvent"),
        ("VMWARE-VRNI-MIB", "vmwSwitchPortOperationalDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwRouterInterfaceOperationalDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnderlayDeviceGenericEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnderlayDeviceFexOfflineEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnderlayDeviceFanMalFunctionEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnderlayDeviceTemperatureThresholdExceededEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnderlayDeviceFexFanMalFunctionEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnderlayDeviceFexPsMalFunctionEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnderlayDeviceModuleMalFunctionEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnderlayDevicePsMalFunctionEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnderlayDeviceBfdSessionRemovedEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnderlayDeviceLldpNeighbourRemovedEvent"),
        ("VMWARE-VRNI-MIB", "vmwThresholdExceededEventDataSourceCpuUsage"),
        ("VMWARE-VRNI-MIB", "vmwThresholdExceededEventDataSourceMemoryUsage"),
        ("VMWARE-VRNI-MIB", "vmwThresholdExceededEventDataSourceTemperature"),
        ("VMWARE-VRNI-MIB", "vmwDeploymentDefMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwNsxtLatencyServiceConfigMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwNsxtLatencyNodeGroupMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwNsxtLatencyStatProfileMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwHybridConnectBgpStatusDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTClusterBackUpDisabledEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTDFWFirewallDisabledEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTComputeManagerConnectionStatusNotUpEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTLogicalSwitchAdminStatusDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTLogicalPortOperationalStatusDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTLogicalPortOperationalStatusUnknownEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTLogicalPortReceivedPacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTLogicalPortTransmittedPacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTLogicalSwitchReceivedPacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTLogicalSwitchTransmittedPacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTRxPacketDropOnMPNicEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTRxPacketDropOnEdgeTnNicEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTRxPacketDropOnHostTnNicEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTTxPacketDropOnMPNicEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTTxPacketDropOnEdgeTnNicEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTTxPacketDropOnHostTnNicEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceClusterManagerStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceCmInventoryStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceControllerStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceDataStoreStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceHttpStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceInstallUpgradeEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceLiagentStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceManagerStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceMgmtPlaneBusStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceMigrationCoordinatorStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceNodeMgmtStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceNodeStatsStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceNSXMessageBusStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceNSXPlatformClientStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceNSXUpgradeAgentStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceNTPStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServicePolicyStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceSearchStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceSNMPStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceSSHStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceSyslogStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceTelemetryStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTMPNodeServiceUIServiceStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwVMCHostPerClusterLimitExceededEvent"),
        ("VMWARE-VRNI-MIB", "vmwVMCVMPerHostLimitExceededEvent"),
        ("VMWARE-VRNI-MIB", "vmwVMCClusterLimitExceededEvent"),
        ("VMWARE-VRNI-MIB", "vmwProtectionEvent"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup10.setStatus(
        "current"
    )

vmwNetworkInsightNotificationGroup11 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 125)
)
vmwNetworkInsightNotificationGroup11.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNsxiApplianceAvailableEvent"),
        ("VMWARE-VRNI-MIB", "vmwNsxiSubscriptionCreateFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNsxiSubscriptionDeleteFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNsxiSubscriptionUpdateFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwNsxiSslHandshakeFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwAnalyticsThresholdCompositeEvent"),
        ("VMWARE-VRNI-MIB", "vmwAnalyticsThresholdCompositeProblemEvent"),
        ("VMWARE-VRNI-MIB", "vmwLicenseExpiredEvent"),
        ("VMWARE-VRNI-MIB", "vmwInGracePeriodEvent"),
        ("VMWARE-VRNI-MIB", "vmwFailedDatasourceOperationEvent"),
        ("VMWARE-VRNI-MIB", "vmwNsxtNotificationWebhookDisabledEvent"),
        ("VMWARE-VRNI-MIB", "vmwNatRuleLargeSubnetEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTHostNodeMaintenanceModeEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTEdgeNodeMaintenanceModeEvent"),
        ("VMWARE-VRNI-MIB", "vmwSDWanLinkTrafficThresholdEvent"),
        ("VMWARE-VRNI-MIB", "vmwVMCCapacityThresholdBreachEvent"),
        ("VMWARE-VRNI-MIB", "vmwNativeVlanMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwNativeVlanTaggingMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwSnapshotNotBuildingEvent"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup11.setStatus(
        "current"
    )

vmwNetworkInsightNotificationGroup12 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 135)
)
vmwNetworkInsightNotificationGroup12.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwProtectionActiveEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnableToSendSNMPTrapsEvent"),
        ("VMWARE-VRNI-MIB", "vmwStreamProcessingFailedEvent"),
        ("VMWARE-VRNI-MIB", "vmwSNOWMandatoryPrivilegesMissingEvent"),
        ("VMWARE-VRNI-MIB", "vmwVMCSDDCTGWConnectivityFailedEvent"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup12.setStatus(
        "current"
    )

vmwNetworkInsightNotificationGroup13 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 145)
)
vmwNetworkInsightNotificationGroup13.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNSXTEdgeDVPGsIPFIXDisabledEvent"),
        ("VMWARE-VRNI-MIB", "vmwUnsupportedNsxAlbVersionEvent"),
        ("VMWARE-VRNI-MIB", "vmwIpfixFlowLagEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXALBSystemEvent"),
        ("VMWARE-VRNI-MIB", "vmwTkgiKubernetesNotReachableEvent"),
        ("VMWARE-VRNI-MIB", "vmwTkgiClustersInsufficientPriviledgesEvent"),
        ("VMWARE-VRNI-MIB", "vmwNSXTRouterInterfaceRPFPacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwChangeEventsDroppedEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxIXServiceStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxNEServiceStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxBMServiceStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxVMotionServiceStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxIXApplianceEncryptionTunnelStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxNEApplianceEncryptionTunnelStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxIXApplianceServicePipelineStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxNEApplianceServicePipelineStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxIXApplianceServiceTransportStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxNEApplianceServiceTransportStatusEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxIXApplianceServiceSystemStateEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxNEApplianceServiceSystemStateEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxIXServiceNotRunningEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxNEServiceNotRunningEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxWanOptServiceNotRunningEvent"),
        ("VMWARE-VRNI-MIB", "vmwPanLogInsightDroppedFlowEvent"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup13.setStatus(
        "current"
    )

vmwNetworkInsightNotificationGroup14 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 155)
)
vmwNetworkInsightNotificationGroup14.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwHcxConnectionRuleViolationEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxApplianceAllTunnelDownEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxMtuMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwSwitchPortRPFPacketDropEvent"),
        ("VMWARE-VRNI-MIB", "vmwCPLogInsightDroppedFlowEvent"),
        ("VMWARE-VRNI-MIB", "vmwSNMPTrapEvent"),
        ("VMWARE-VRNI-MIB", "vmwServiceRestartCountExceededEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxWanOptServiceStatusEvent"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup14.setStatus(
        "current"
    )

vmwNetworkInsightNotificationGroup15 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 2, 165)
)
vmwNetworkInsightNotificationGroup15.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNsxtIpfixMultipleCollectorConfigurationEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxApplianceUnhealthyTunnelsEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxManagerVersionMismatchEvent"),
        ("VMWARE-VRNI-MIB", "vmwHcxApplianceVersionMismatchEvent"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightNotificationGroup15.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmwNetworkInsightMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 3)
)
vmwNetworkInsightMIBBasicCompliance.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationInfoGroup1"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup1"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance.setStatus(
        "deprecated"
    )

vmwNetworkInsightMIBBasicCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 30)
)
vmwNetworkInsightMIBBasicCompliance2.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationInfoGroup2"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup1"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup2"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance2.setStatus(
        "deprecated"
    )

vmwNetworkInsightMIBBasicCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 35)
)
vmwNetworkInsightMIBBasicCompliance3.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationInfoGroup2"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup1"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup2"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup3"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance3.setStatus(
        "deprecated"
    )

vmwNetworkInsightMIBBasicCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 45)
)
vmwNetworkInsightMIBBasicCompliance4.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationInfoGroup2"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup1"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup2"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup4"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance4.setStatus(
        "deprecated"
    )

vmwNetworkInsightMIBBasicCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 60)
)
vmwNetworkInsightMIBBasicCompliance5.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationInfoGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup1"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup2"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup4"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup5"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance5.setStatus(
        "deprecated"
    )

vmwNetworkInsightMIBBasicCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 70)
)
vmwNetworkInsightMIBBasicCompliance6.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationInfoGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup1"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup2"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup4"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup5"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup6"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance6.setStatus(
        "deprecated"
    )

vmwNetworkInsightMIBBasicCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 80)
)
vmwNetworkInsightMIBBasicCompliance7.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationInfoGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup1"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup2"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup4"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup5"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup6"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup7"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance7.setStatus(
        "deprecated"
    )

vmwNetworkInsightMIBBasicCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 90)
)
vmwNetworkInsightMIBBasicCompliance8.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationInfoGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup1"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup2"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup4"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup5"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup6"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup7"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup8"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance8.setStatus(
        "deprecated"
    )

vmwNetworkInsightMIBBasicCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 100)
)
vmwNetworkInsightMIBBasicCompliance9.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationInfoGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup1"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup2"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup4"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup5"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup6"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup7"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup8"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup9"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance9.setStatus(
        "deprecated"
    )

vmwNetworkInsightMIBBasicCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 110)
)
vmwNetworkInsightMIBBasicCompliance10.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationInfoGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup1"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup2"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup4"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup5"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup6"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup7"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup8"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup9"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup10"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance10.setStatus(
        "deprecated"
    )

vmwNetworkInsightMIBBasicCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 120)
)
vmwNetworkInsightMIBBasicCompliance11.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationInfoGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup1"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup2"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup4"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup5"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup6"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup7"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup8"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup9"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup10"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup11"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance11.setStatus(
        "deprecated"
    )

vmwNetworkInsightMIBBasicCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 130)
)
vmwNetworkInsightMIBBasicCompliance12.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationInfoGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup1"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup2"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup4"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup5"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup6"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup7"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup8"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup9"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup10"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup11"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup12"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance12.setStatus(
        "deprecated"
    )

vmwNetworkInsightMIBBasicCompliance13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 140)
)
vmwNetworkInsightMIBBasicCompliance13.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationInfoGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup1"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup2"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup4"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup5"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup6"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup7"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup8"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup9"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup10"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup11"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup12"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup13"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance13.setStatus(
        "deprecated"
    )

vmwNetworkInsightMIBBasicCompliance14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 150)
)
vmwNetworkInsightMIBBasicCompliance14.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationInfoGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup1"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup2"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup4"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup5"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup6"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup7"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup8"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup9"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup10"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup11"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup12"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup13"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup14"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance14.setStatus(
        "deprecated"
    )

vmwNetworkInsightMIBBasicCompliance15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 100, 1, 99, 1, 160)
)
vmwNetworkInsightMIBBasicCompliance15.setObjects(
      *(("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationInfoGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup1"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup2"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup3"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup4"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup5"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup6"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup7"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup8"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup9"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup10"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup11"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup12"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup13"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup14"),
        ("VMWARE-VRNI-MIB", "vmwNetworkInsightNotificationGroup15"))
)
if mibBuilder.loadTexts:
    vmwNetworkInsightMIBBasicCompliance15.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-VRNI-MIB",
    **{"VmwVrniSeverity": VmwVrniSeverity,
       "vmwNetworkInsightMIB": vmwNetworkInsightMIB,
       "vmwVRNIEvents": vmwVRNIEvents,
       "vmwSnmpTrapsAreConfigured": vmwSnmpTrapsAreConfigured,
       "vmwSnmpTrapsAreDisabled": vmwSnmpTrapsAreDisabled,
       "vmwTestTrap": vmwTestTrap,
       "vmwArkinApplicationMemberLimitEvent": vmwArkinApplicationMemberLimitEvent,
       "vmwNsxiApplianceAvailableEvent": vmwNsxiApplianceAvailableEvent,
       "vmwNsxiSubscriptionCreateFailedEvent": vmwNsxiSubscriptionCreateFailedEvent,
       "vmwNsxiSubscriptionDeleteFailedEvent": vmwNsxiSubscriptionDeleteFailedEvent,
       "vmwNsxiSubscriptionUpdateFailedEvent": vmwNsxiSubscriptionUpdateFailedEvent,
       "vmwNsxiSslHandshakeFailedEvent": vmwNsxiSslHandshakeFailedEvent,
       "vmwHybridConnectBgpStatusDownEvent": vmwHybridConnectBgpStatusDownEvent,
       "vmwKubernetesBaseEvent": vmwKubernetesBaseEvent,
       "vmwNSXALBSystemEvent": vmwNSXALBSystemEvent,
       "vmwEntityDiscoveryChangeEvent": vmwEntityDiscoveryChangeEvent,
       "vmwEntityPropertiesChangeEvent": vmwEntityPropertiesChangeEvent,
       "vmwFirewallNotInstalledOnHostEvent": vmwFirewallNotInstalledOnHostEvent,
       "vmwHostWithStaleFirewallRulesEvent": vmwHostWithStaleFirewallRulesEvent,
       "vmwIpAddressChangeEvent": vmwIpAddressChangeEvent,
       "vmwL2GatewayAnomalyEvent": vmwL2GatewayAnomalyEvent,
       "vmwL2NetworkAddressAnomalyEvent": vmwL2NetworkAddressAnomalyEvent,
       "vmwL2NetworkDiameterExceededEvent": vmwL2NetworkDiameterExceededEvent,
       "vmwL2NetworkUplinkMissingEvent": vmwL2NetworkUplinkMissingEvent,
       "vmwL2NetworkWithNoVMsEvent": vmwL2NetworkWithNoVMsEvent,
       "vmwLayer2NetworkDiameterChangedEvent": vmwLayer2NetworkDiameterChangedEvent,
       "vmwMTUMismatchEvent": vmwMTUMismatchEvent,
       "vmwNetworkIsolationEvent": vmwNetworkIsolationEvent,
       "vmwNoPathEvent": vmwNoPathEvent,
       "vmwSpoofguardDisabledEvent": vmwSpoofguardDisabledEvent,
       "vmwVMotionEvent": vmwVMotionEvent,
       "vmwVMWithDisconnectedVnicsEvent": vmwVMWithDisconnectedVnicsEvent,
       "vmwVMWithMulipleVnicsOnDifferentVxlansEvent": vmwVMWithMulipleVnicsOnDifferentVxlansEvent,
       "vmwVMWithMulipleVnicsOnSameL2Event": vmwVMWithMulipleVnicsOnSameL2Event,
       "vmwVMWithNoIpAddressEvent": vmwVMWithNoIpAddressEvent,
       "vmwVTEPMissingEvent": vmwVTEPMissingEvent,
       "vmwL2Event": vmwL2Event,
       "vmwMembershipChangeEvent": vmwMembershipChangeEvent,
       "vmwSecurityGroupMembershipChangeEvent": vmwSecurityGroupMembershipChangeEvent,
       "vmwFirewallRuleMembershipChangeEvent": vmwFirewallRuleMembershipChangeEvent,
       "vmwVlanMembershipChangeEvent": vmwVlanMembershipChangeEvent,
       "vmwVxlanMembershipChangeEvent": vmwVxlanMembershipChangeEvent,
       "vmwDeleteChangeEvent": vmwDeleteChangeEvent,
       "vmwVtepFailedPingEvent": vmwVtepFailedPingEvent,
       "vmwEmptySearchStreamChangeEvent": vmwEmptySearchStreamChangeEvent,
       "vmwSearchStreamMembershipChangeEvent": vmwSearchStreamMembershipChangeEvent,
       "vmwEmptySearchStreamProblemEvent": vmwEmptySearchStreamProblemEvent,
       "vmwSearchStreamMembershipProblemEvent": vmwSearchStreamMembershipProblemEvent,
       "vmwOspfConfigurationMismatchEvent": vmwOspfConfigurationMismatchEvent,
       "vmwServiceVMNotHealthyEvent": vmwServiceVMNotHealthyEvent,
       "vmwServiceVMNotPoweredOnEvent": vmwServiceVMNotPoweredOnEvent,
       "vmwServiceVMHighCPUUsageEvent": vmwServiceVMHighCPUUsageEvent,
       "vmwServiceVMHighMemoryUsageEvent": vmwServiceVMHighMemoryUsageEvent,
       "vmwServiceVMHighDiskUsageEvent": vmwServiceVMHighDiskUsageEvent,
       "vmwIPSetPropertiesChangeEvent": vmwIPSetPropertiesChangeEvent,
       "vmwFirewallRulePropertiesChangeEvent": vmwFirewallRulePropertiesChangeEvent,
       "vmwSecurityGroupPropertiesChangeEvent": vmwSecurityGroupPropertiesChangeEvent,
       "vmwIPSetMembershipChangeEvent": vmwIPSetMembershipChangeEvent,
       "vmwFirewallRuleMaskEvent": vmwFirewallRuleMaskEvent,
       "vmwSecurityMembershipChangeEvent": vmwSecurityMembershipChangeEvent,
       "vmwSecurityTagPropertiesChangeEvent": vmwSecurityTagPropertiesChangeEvent,
       "vmwSecurityTagMembershipChangeEvent": vmwSecurityTagMembershipChangeEvent,
       "vmwHostDatastoreChangeEvent": vmwHostDatastoreChangeEvent,
       "vmwVMDatastoreChangeEvent": vmwVMDatastoreChangeEvent,
       "vmwVMSnapshotChangeEvent": vmwVMSnapshotChangeEvent,
       "vmwVMVirtualDiskChangeEvent": vmwVMVirtualDiskChangeEvent,
       "vmwIPSetDefinitionMismatchEvent": vmwIPSetDefinitionMismatchEvent,
       "vmwSegmentMismatchEvent": vmwSegmentMismatchEvent,
       "vmwVtepEvent": vmwVtepEvent,
       "vmwVtepConfigurationFaultEvent": vmwVtepConfigurationFaultEvent,
       "vmwDLRNetworksNotReachableEvent": vmwDLRNetworksNotReachableEvent,
       "vmwVtepSubnetMismatchEvent": vmwVtepSubnetMismatchEvent,
       "vmwVtepCountMismatchEvent": vmwVtepCountMismatchEvent,
       "vmwEdgeNetworksNotReachableEvent": vmwEdgeNetworksNotReachableEvent,
       "vmwNiInfraChangeEvent": vmwNiInfraChangeEvent,
       "vmwDataSourceEnabledChangeEvent": vmwDataSourceEnabledChangeEvent,
       "vmwDataSourceDisabledChangeEvent": vmwDataSourceDisabledChangeEvent,
       "vmwDataSourceCreatedEvent": vmwDataSourceCreatedEvent,
       "vmwPlatformCpuCoreChangeEvent": vmwPlatformCpuCoreChangeEvent,
       "vmwPlatformDiskChangeEvent": vmwPlatformDiskChangeEvent,
       "vmwPlatformMemoryChangeEvent": vmwPlatformMemoryChangeEvent,
       "vmwPlatformRebootedEvent": vmwPlatformRebootedEvent,
       "vmwProxyCpuCoreChangeEvent": vmwProxyCpuCoreChangeEvent,
       "vmwProxyDiskChangeEvent": vmwProxyDiskChangeEvent,
       "vmwProxyMemoryChangeEvent": vmwProxyMemoryChangeEvent,
       "vmwProxyRebootedEvent": vmwProxyRebootedEvent,
       "vmwNIClusterChangeEvent": vmwNIClusterChangeEvent,
       "vmwNISystemProxyChangeEvent": vmwNISystemProxyChangeEvent,
       "vmwNIClusterCreateEvent": vmwNIClusterCreateEvent,
       "vmwThresholdExceededEventCpuReady": vmwThresholdExceededEventCpuReady,
       "vmwThresholdExceededEventCpuCoStop": vmwThresholdExceededEventCpuCoStop,
       "vmwThresholdExceededEventDiskCommandAbortRule": vmwThresholdExceededEventDiskCommandAbortRule,
       "vmwThresholdExceededEventIODeviceLatencyRule": vmwThresholdExceededEventIODeviceLatencyRule,
       "vmwThresholdExceededEventIOKernelLatencyRule": vmwThresholdExceededEventIOKernelLatencyRule,
       "vmwThresholdExceededEventMemorySwapInRule": vmwThresholdExceededEventMemorySwapInRule,
       "vmwThresholdExceededEventMemorySwapOutRule": vmwThresholdExceededEventMemorySwapOutRule,
       "vmwThresholdExceededEventNetworkRxDropRule": vmwThresholdExceededEventNetworkRxDropRule,
       "vmwThresholdExceededEventNetworkTxDropRule": vmwThresholdExceededEventNetworkTxDropRule,
       "vmwAWSRegionSGLimitEvent": vmwAWSRegionSGLimitEvent,
       "vmwAWSVPCSGLimitEvent": vmwAWSVPCSGLimitEvent,
       "vmwAWSSGInboundRuleLimitEvent": vmwAWSSGInboundRuleLimitEvent,
       "vmwAWSSGOutboundRuleLimitEvent": vmwAWSSGOutboundRuleLimitEvent,
       "vmwAWSInterfaceSGLimitEvent": vmwAWSInterfaceSGLimitEvent,
       "vmwPacketDropEvent": vmwPacketDropEvent,
       "vmwSwitchPortPacketDropEvent": vmwSwitchPortPacketDropEvent,
       "vmwRouterInterfacePacketDropEvent": vmwRouterInterfacePacketDropEvent,
       "vmwVnicPacketDropEvent": vmwVnicPacketDropEvent,
       "vmwVTEPUnderlayPacketDropEvent": vmwVTEPUnderlayPacketDropEvent,
       "vmwPnicUnderlyingSwitchPortPacketDropEvent": vmwPnicUnderlyingSwitchPortPacketDropEvent,
       "vmwDevicePacketDropEvent": vmwDevicePacketDropEvent,
       "vmwSwitchPortUptimeThresholdRecededEvent": vmwSwitchPortUptimeThresholdRecededEvent,
       "vmwSwitchPortOperationalDownEvent": vmwSwitchPortOperationalDownEvent,
       "vmwRouterInterfaceOperationalDownEvent": vmwRouterInterfaceOperationalDownEvent,
       "vmwUnderlayDeviceGenericEvent": vmwUnderlayDeviceGenericEvent,
       "vmwUnderlayDeviceFexOfflineEvent": vmwUnderlayDeviceFexOfflineEvent,
       "vmwUnderlayDeviceFanMalFunctionEvent": vmwUnderlayDeviceFanMalFunctionEvent,
       "vmwUnderlayDeviceTemperatureThresholdExceededEvent": vmwUnderlayDeviceTemperatureThresholdExceededEvent,
       "vmwUnderlayDeviceFexFanMalFunctionEvent": vmwUnderlayDeviceFexFanMalFunctionEvent,
       "vmwUnderlayDeviceFexPsMalFunctionEvent": vmwUnderlayDeviceFexPsMalFunctionEvent,
       "vmwUnderlayDeviceModuleMalFunctionEvent": vmwUnderlayDeviceModuleMalFunctionEvent,
       "vmwUnderlayDevicePsMalFunctionEvent": vmwUnderlayDevicePsMalFunctionEvent,
       "vmwUnderlayDeviceBfdSessionRemovedEvent": vmwUnderlayDeviceBfdSessionRemovedEvent,
       "vmwUnderlayDeviceLldpNeighbourRemovedEvent": vmwUnderlayDeviceLldpNeighbourRemovedEvent,
       "vmwSwitchPortRPFPacketDropEvent": vmwSwitchPortRPFPacketDropEvent,
       "vmwThresholdExceededEventDataSourceCpuUsage": vmwThresholdExceededEventDataSourceCpuUsage,
       "vmwThresholdExceededEventDataSourceMemoryUsage": vmwThresholdExceededEventDataSourceMemoryUsage,
       "vmwThresholdExceededEventDataSourceTemperature": vmwThresholdExceededEventDataSourceTemperature,
       "vmwThresholdExceededEventDatastoreFreeSpaceWarning": vmwThresholdExceededEventDatastoreFreeSpaceWarning,
       "vmwThresholdExceededEventDatastoreFreeSpaceCritical": vmwThresholdExceededEventDatastoreFreeSpaceCritical,
       "vmwThresholdExceededEventDatastoreReadLatency": vmwThresholdExceededEventDatastoreReadLatency,
       "vmwThresholdExceededEventDatastoreWriteLatency": vmwThresholdExceededEventDatastoreWriteLatency,
       "vmwDistributedFirewallApplyHostEvent": vmwDistributedFirewallApplyHostEvent,
       "vmwDistributedFirewallApplyVMEvent": vmwDistributedFirewallApplyVMEvent,
       "vmwNsxEvent": vmwNsxEvent,
       "vmwFeatureImpactedEvent": vmwFeatureImpactedEvent,
       "vmwNSXComponentEvent": vmwNSXComponentEvent,
       "vmwNSXBackupEvent": vmwNSXBackupEvent,
       "vmwNSXBackupAuditLogExcludedEvent": vmwNSXBackupAuditLogExcludedEvent,
       "vmwNSXUnsecureBackupEvent": vmwNSXUnsecureBackupEvent,
       "vmwNSXBackupSystemEventsExcludedEvent": vmwNSXBackupSystemEventsExcludedEvent,
       "vmwNSXBackupNotScheduledEvent": vmwNSXBackupNotScheduledEvent,
       "vmwNSXBackupNotRecordedEvent": vmwNSXBackupNotRecordedEvent,
       "vmwNSXNtpServerEvent": vmwNSXNtpServerEvent,
       "vmwNSXSysLogServerEvent": vmwNSXSysLogServerEvent,
       "vmwControllerSysLogServerEvent": vmwControllerSysLogServerEvent,
       "vmwNSXIpV6EnabledEvent": vmwNSXIpV6EnabledEvent,
       "vmwNSXOspfNeighborDownEvent": vmwNSXOspfNeighborDownEvent,
       "vmwClusterFeatureVersionMismatchEvent": vmwClusterFeatureVersionMismatchEvent,
       "vmwHostFeatureVersionMismatchEvent": vmwHostFeatureVersionMismatchEvent,
       "vmwFeatureVersionMismatchEvent": vmwFeatureVersionMismatchEvent,
       "vmwHostFeatureEnabledMismatchEvent": vmwHostFeatureEnabledMismatchEvent,
       "vmwHostFeatureInstalledMismatchEvent": vmwHostFeatureInstalledMismatchEvent,
       "vmwHostVtepNotFoundEvent": vmwHostVtepNotFoundEvent,
       "vmwHostVtepDisconnectedEvent": vmwHostVtepDisconnectedEvent,
       "vmwHostVtepEvent": vmwHostVtepEvent,
       "vmwClusterHostsVtepMTUMismatchEvent": vmwClusterHostsVtepMTUMismatchEvent,
       "vmwFeatureUnhealthyEvent": vmwFeatureUnhealthyEvent,
       "vmwEdgeHANotConfiguredEvent": vmwEdgeHANotConfiguredEvent,
       "vmwEdgeInterfacesDownEvent": vmwEdgeInterfacesDownEvent,
       "vmwModuleUnhealthyEvent": vmwModuleUnhealthyEvent,
       "vmwModuleNotLoadedEvent": vmwModuleNotLoadedEvent,
       "vmwModuleNetworkConnectionFailureEvent": vmwModuleNetworkConnectionFailureEvent,
       "vmwHostNetworkControlPlaneMismatchEvent": vmwHostNetworkControlPlaneMismatchEvent,
       "vmwHostNetworkControlPlaneConnectionFailureEvent": vmwHostNetworkControlPlaneConnectionFailureEvent,
       "vmwHostNetworkControlPlaneNotSyncedEvent": vmwHostNetworkControlPlaneNotSyncedEvent,
       "vmwNSXControllerClusterMajorityEvent": vmwNSXControllerClusterMajorityEvent,
       "vmwNSXControllersVMOnSameHostEvent": vmwNSXControllersVMOnSameHostEvent,
       "vmwVxLanRangeExhaustEvent": vmwVxLanRangeExhaustEvent,
       "vmwNSXFirewallDefaultAllowAllRulesEvent": vmwNSXFirewallDefaultAllowAllRulesEvent,
       "vmwLogicalRouterNoUplinkEvent": vmwLogicalRouterNoUplinkEvent,
       "vmwEdgeNotHAEvent": vmwEdgeNotHAEvent,
       "vmwEdgeNotDeployedEvent": vmwEdgeNotDeployedEvent,
       "vmwEcmpIsEnabledAndStatefulServicesAreUpEvent": vmwEcmpIsEnabledAndStatefulServicesAreUpEvent,
       "vmwLogicalRouterDeployedOnEcmpEdgeHostEvent": vmwLogicalRouterDeployedOnEcmpEdgeHostEvent,
       "vmwEdgeMissingInterfaceOSPFAreaMappingEvent": vmwEdgeMissingInterfaceOSPFAreaMappingEvent,
       "vmwOspfInsecureAuthRouterEvent": vmwOspfInsecureAuthRouterEvent,
       "vmwNSXControllersDeployedCountEvent": vmwNSXControllersDeployedCountEvent,
       "vmwNSXControllerNotActiveCountEvent": vmwNSXControllerNotActiveCountEvent,
       "vmwNSXControllerEvent": vmwNSXControllerEvent,
       "vmwNSXEcmpEdgeDownEvent": vmwNSXEcmpEdgeDownEvent,
       "vmwNSXMajorityEcmpEdgesDownEvent": vmwNSXMajorityEcmpEdgesDownEvent,
       "vmwNSXAllEcmpEdgesDownEvent": vmwNSXAllEcmpEdgesDownEvent,
       "vmwNSXEdgeMtuMismatchEvent": vmwNSXEdgeMtuMismatchEvent,
       "vmwNSXEdgeSplitBrainEvent": vmwNSXEdgeSplitBrainEvent,
       "vmwVirtualDistributedRoutingEvent": vmwVirtualDistributedRoutingEvent,
       "vmwNSXEdgeBGPNeighbourDownEvent": vmwNSXEdgeBGPNeighbourDownEvent,
       "vmwAnalyticsEvent": vmwAnalyticsEvent,
       "vmwAnalyticsOutlierEvent": vmwAnalyticsOutlierEvent,
       "vmwAnalyticsThresholdEvent": vmwAnalyticsThresholdEvent,
       "vmwAnalyticsThresholdCompositeEvent": vmwAnalyticsThresholdCompositeEvent,
       "vmwAnalyticsThresholdCompositeProblemEvent": vmwAnalyticsThresholdCompositeProblemEvent,
       "vmwVMCEvent": vmwVMCEvent,
       "vmwVMCSDDCTGWConnectivityFailedEvent": vmwVMCSDDCTGWConnectivityFailedEvent,
       "vmwCriticalHostNotAccessibleEvent": vmwCriticalHostNotAccessibleEvent,
       "vmwGenericNSXSystemEvent": vmwGenericNSXSystemEvent,
       "vmwFilterConfigApplyOnHostFailedEvent": vmwFilterConfigApplyOnHostFailedEvent,
       "vmwRulesetLoadOnHostFailedEvent": vmwRulesetLoadOnHostFailedEvent,
       "vmwConfigUpdateOnHostFailedEvent": vmwConfigUpdateOnHostFailedEvent,
       "vmwSpoofguardConfigUpdateOnHostFailedEvent": vmwSpoofguardConfigUpdateOnHostFailedEvent,
       "vmwApplyRuleToVnicFailedEvent": vmwApplyRuleToVnicFailedEvent,
       "vmwContainerConfigUpdateOnVnicFailedEvent": vmwContainerConfigUpdateOnVnicFailedEvent,
       "vmwSpoofguardApplyToVnicFailedEvent": vmwSpoofguardApplyToVnicFailedEvent,
       "vmwHostMessagingConfigurationFailedEvent": vmwHostMessagingConfigurationFailedEvent,
       "vmwHostMessagingConnectionReconfigurationFailedEvent": vmwHostMessagingConnectionReconfigurationFailedEvent,
       "vmwHostMessagingConfigurationFailedNotificationSkippedEvent": vmwHostMessagingConfigurationFailedNotificationSkippedEvent,
       "vmwHostMessagingInfrastructureDownEvent": vmwHostMessagingInfrastructureDownEvent,
       "vmwEdgeVMNotRespondingEvent": vmwEdgeVMNotRespondingEvent,
       "vmwEdgeUnhealthyEvent": vmwEdgeUnhealthyEvent,
       "vmwEdgeVMCommunicationFailureEvent": vmwEdgeVMCommunicationFailureEvent,
       "vmwNSXEdgeEvent": vmwNSXEdgeEvent,
       "vmwOtherCriticalNSXEvent": vmwOtherCriticalNSXEvent,
       "vmwPanEvent": vmwPanEvent,
       "vmwPanNsxNotInRegisteredStateEvent": vmwPanNsxNotInRegisteredStateEvent,
       "vmwPanNsxDynamicUpdateDelayedEvent": vmwPanNsxDynamicUpdateDelayedEvent,
       "vmwPanDeviceInDisconnectedStateEvent": vmwPanDeviceInDisconnectedStateEvent,
       "vmwPanNsxServiceApplianceViewMismatchEvent": vmwPanNsxServiceApplianceViewMismatchEvent,
       "vmwPanNsxFabricAgentNotFoundOnHostEvent": vmwPanNsxFabricAgentNotFoundOnHostEvent,
       "vmwPanNsxServiceVMNotFoundOnHostEvent": vmwPanNsxServiceVMNotFoundOnHostEvent,
       "vmwPanLogInsightDroppedFlowEvent": vmwPanLogInsightDroppedFlowEvent,
       "vmwCPLogInsightDroppedFlowEvent": vmwCPLogInsightDroppedFlowEvent,
       "vmwCheckpointEvent": vmwCheckpointEvent,
       "vmwCheckpointNsxFabricAgentNotFoundOnHostEvent": vmwCheckpointNsxFabricAgentNotFoundOnHostEvent,
       "vmwCheckpointNsxServiceVMNotFoundOnHostEvent": vmwCheckpointNsxServiceVMNotFoundOnHostEvent,
       "vmwCheckpointGatewaySicStatusNotCommunicatingEvent": vmwCheckpointGatewaySicStatusNotCommunicatingEvent,
       "vmwCheckpointNsxServiceApplianceViewMismatchEvent": vmwCheckpointNsxServiceApplianceViewMismatchEvent,
       "vmwNSXTEvent": vmwNSXTEvent,
       "vmwNSXTVcNotAddedEvent": vmwNSXTVcNotAddedEvent,
       "vmwNSXTStandaloneHostsEvent": vmwNSXTStandaloneHostsEvent,
       "vmwNSXTSystemEvent": vmwNSXTSystemEvent,
       "vmwNSXTNoUplinkConnectivityEvent": vmwNSXTNoUplinkConnectivityEvent,
       "vmwNSXTRoutingAdvertisementEvent": vmwNSXTRoutingAdvertisementEvent,
       "vmwNSXTManagerConnectivityDownEvent": vmwNSXTManagerConnectivityDownEvent,
       "vmwNSXTControllerConnectivityDegradedEvent": vmwNSXTControllerConnectivityDegradedEvent,
       "vmwNSXTControllerConnectivityDownEvent": vmwNSXTControllerConnectivityDownEvent,
       "vmwNSXTMtuMismatchEvent": vmwNSXTMtuMismatchEvent,
       "vmwNSXTExcludedVmFlowEvent": vmwNSXTExcludedVmFlowEvent,
       "vmwNSXTDoubleVlanTaggingEvent": vmwNSXTDoubleVlanTaggingEvent,
       "vmwNSXTNoTzAttachedOnTnEvent": vmwNSXTNoTzAttachedOnTnEvent,
       "vmwNSXTVtepDeleteEvent": vmwNSXTVtepDeleteEvent,
       "vmwDuplicateL3SwitchEvent": vmwDuplicateL3SwitchEvent,
       "vmwLBPoolMemberDownEvent": vmwLBPoolMemberDownEvent,
       "vmwLBPoolDownEvent": vmwLBPoolDownEvent,
       "vmwLBPoolEmptyEvent": vmwLBPoolEmptyEvent,
       "vmwLBPoolMemberVMDownEvent": vmwLBPoolMemberVMDownEvent,
       "vmwLBVirtualServerDisableEvent": vmwLBVirtualServerDisableEvent,
       "vmwLBServiceNodeIPNotFoundEvent": vmwLBServiceNodeIPNotFoundEvent,
       "vmwLBServiceNodeMultipleNicFoundEvent": vmwLBServiceNodeMultipleNicFoundEvent,
       "vmwNSXTSwitchIpfixEnabledEvent": vmwNSXTSwitchIpfixEnabledEvent,
       "vmwNSXTStandaloneHostsWithoutVcEvent": vmwNSXTStandaloneHostsWithoutVcEvent,
       "vmwNSXTControllerNodeToControlClusterConnectivityEvent": vmwNSXTControllerNodeToControlClusterConnectivityEvent,
       "vmwNSXTControllerNodeToMgmtPlaneConnectivityEvent": vmwNSXTControllerNodeToMgmtPlaneConnectivityEvent,
       "vmwNSXTMPNodeToMgmtClusterConnectivityEvent": vmwNSXTMPNodeToMgmtClusterConnectivityEvent,
       "vmwNSXTHostNodePnicStatusDownEvent": vmwNSXTHostNodePnicStatusDownEvent,
       "vmwNSXTHostNodePnicStatusDegradedEvent": vmwNSXTHostNodePnicStatusDegradedEvent,
       "vmwNSXTHostNodePnicStatusUnknownEvent": vmwNSXTHostNodePnicStatusUnknownEvent,
       "vmwNSXTHostNodeTunnelStatusDownEvent": vmwNSXTHostNodeTunnelStatusDownEvent,
       "vmwNSXTHostNodeTunnelStatusDegradedEvent": vmwNSXTHostNodeTunnelStatusDegradedEvent,
       "vmwNSXTHostNodeTunnelStatusUnknownEvent": vmwNSXTHostNodeTunnelStatusUnknownEvent,
       "vmwNSXTHostNodeStatusDownEvent": vmwNSXTHostNodeStatusDownEvent,
       "vmwNSXTHostNodeStatusDegradedEvent": vmwNSXTHostNodeStatusDegradedEvent,
       "vmwNSXTHostNodeStatusUnknownEvent": vmwNSXTHostNodeStatusUnknownEvent,
       "vmwNSXTEdgeNodePnicStatusDownEvent": vmwNSXTEdgeNodePnicStatusDownEvent,
       "vmwNSXTEdgeNodePnicStatusDegradedEvent": vmwNSXTEdgeNodePnicStatusDegradedEvent,
       "vmwNSXTEdgeNodePnicStatusUnknownEvent": vmwNSXTEdgeNodePnicStatusUnknownEvent,
       "vmwNSXTEdgeNodeTunnelStatusDownEvent": vmwNSXTEdgeNodeTunnelStatusDownEvent,
       "vmwNSXTEdgeNodeTunnelStatusDegradedEvent": vmwNSXTEdgeNodeTunnelStatusDegradedEvent,
       "vmwNSXTEdgeNodeTunnelStatusUnknownEvent": vmwNSXTEdgeNodeTunnelStatusUnknownEvent,
       "vmwNSXTEdgeNodeStatusDownEvent": vmwNSXTEdgeNodeStatusDownEvent,
       "vmwNSXTEdgeNodeStatusDegradedEvent": vmwNSXTEdgeNodeStatusDegradedEvent,
       "vmwNSXTEdgeNodeStatusUnknownEvent": vmwNSXTEdgeNodeStatusUnknownEvent,
       "vmwNSXTHostNodeMgmtConnectivityStatusDownEvent": vmwNSXTHostNodeMgmtConnectivityStatusDownEvent,
       "vmwNSXTEdgeNodeCtlrConnectivityStatusUnknownEvent": vmwNSXTEdgeNodeCtlrConnectivityStatusUnknownEvent,
       "vmwNSXTHostNodeCtlrConnectivityStatusDownEvent": vmwNSXTHostNodeCtlrConnectivityStatusDownEvent,
       "vmwNSXTHostNodeCtlrConnectivityStatusDegradedEvent": vmwNSXTHostNodeCtlrConnectivityStatusDegradedEvent,
       "vmwNSXTHostNodeCtlrConnectivityStatusUnknownEvent": vmwNSXTHostNodeCtlrConnectivityStatusUnknownEvent,
       "vmwNSXTLogicalSwitchAdminStatusDownEvent": vmwNSXTLogicalSwitchAdminStatusDownEvent,
       "vmwNSXTLogicalPortOperationalStatusDownEvent": vmwNSXTLogicalPortOperationalStatusDownEvent,
       "vmwNSXTLogicalPortOperationalStatusUnknownEvent": vmwNSXTLogicalPortOperationalStatusUnknownEvent,
       "vmwNSXTComputeManagerConnectionStatusNotUpEvent": vmwNSXTComputeManagerConnectionStatusNotUpEvent,
       "vmwNSXTClusterBackUpDisabledEvent": vmwNSXTClusterBackUpDisabledEvent,
       "vmwNSXTDFWFirewallDisabledEvent": vmwNSXTDFWFirewallDisabledEvent,
       "vmwNSXTLogicalPortReceivedPacketDropEvent": vmwNSXTLogicalPortReceivedPacketDropEvent,
       "vmwNSXTLogicalPortTransmittedPacketDropEvent": vmwNSXTLogicalPortTransmittedPacketDropEvent,
       "vmwNSXTLogicalSwitchReceivedPacketDropEvent": vmwNSXTLogicalSwitchReceivedPacketDropEvent,
       "vmwNSXTLogicalSwitchTransmittedPacketDropEvent": vmwNSXTLogicalSwitchTransmittedPacketDropEvent,
       "vmwNSXTRxPacketDropOnMPNicEvent": vmwNSXTRxPacketDropOnMPNicEvent,
       "vmwNSXTRxPacketDropOnEdgeTnNicEvent": vmwNSXTRxPacketDropOnEdgeTnNicEvent,
       "vmwNSXTRxPacketDropOnHostTnNicEvent": vmwNSXTRxPacketDropOnHostTnNicEvent,
       "vmwNSXTTxPacketDropOnMPNicEvent": vmwNSXTTxPacketDropOnMPNicEvent,
       "vmwNSXTTxPacketDropOnEdgeTnNicEvent": vmwNSXTTxPacketDropOnEdgeTnNicEvent,
       "vmwNSXTTxPacketDropOnHostTnNicEvent": vmwNSXTTxPacketDropOnHostTnNicEvent,
       "vmwNatRuleLargeSubnetEvent": vmwNatRuleLargeSubnetEvent,
       "vmwNSXTEdgeNodeMaintenanceModeEvent": vmwNSXTEdgeNodeMaintenanceModeEvent,
       "vmwNSXTHostNodeMaintenanceModeEvent": vmwNSXTHostNodeMaintenanceModeEvent,
       "vmwNSXTEdgeDVPGsIPFIXDisabledEvent": vmwNSXTEdgeDVPGsIPFIXDisabledEvent,
       "vmwNSXTRouterInterfaceRPFPacketDropEvent": vmwNSXTRouterInterfaceRPFPacketDropEvent,
       "vmwNsxtIpfixMultipleCollectorConfigurationEvent": vmwNsxtIpfixMultipleCollectorConfigurationEvent,
       "vmwHardwareVTEPMismatchEvent": vmwHardwareVTEPMismatchEvent,
       "vmwHardwareVTEPPortDownEvent": vmwHardwareVTEPPortDownEvent,
       "vmwNSXTMPNodeServiceCmInventoryStatusEvent": vmwNSXTMPNodeServiceCmInventoryStatusEvent,
       "vmwNSXTMPNodeServiceControllerStatusEvent": vmwNSXTMPNodeServiceControllerStatusEvent,
       "vmwNSXTMPNodeServiceDataStoreStatusEvent": vmwNSXTMPNodeServiceDataStoreStatusEvent,
       "vmwNSXTMPNodeServiceHttpStatusEvent": vmwNSXTMPNodeServiceHttpStatusEvent,
       "vmwNSXTMPNodeServiceInstallUpgradeEvent": vmwNSXTMPNodeServiceInstallUpgradeEvent,
       "vmwNSXTMPNodeServiceLiagentStatusEvent": vmwNSXTMPNodeServiceLiagentStatusEvent,
       "vmwNSXTMPNodeServiceManagerStatusEvent": vmwNSXTMPNodeServiceManagerStatusEvent,
       "vmwNSXTMPNodeServiceMgmtPlaneBusStatusEvent": vmwNSXTMPNodeServiceMgmtPlaneBusStatusEvent,
       "vmwNSXTMPNodeServiceMigrationCoordinatorStatusEvent": vmwNSXTMPNodeServiceMigrationCoordinatorStatusEvent,
       "vmwNSXTMPNodeServiceNodeMgmtStatusEvent": vmwNSXTMPNodeServiceNodeMgmtStatusEvent,
       "vmwNSXTMPNodeServiceNodeStatsStatusEvent": vmwNSXTMPNodeServiceNodeStatsStatusEvent,
       "vmwNSXTMPNodeServiceNSXMessageBusStatusEvent": vmwNSXTMPNodeServiceNSXMessageBusStatusEvent,
       "vmwNSXTMPNodeServiceNSXPlatformClientStatusEvent": vmwNSXTMPNodeServiceNSXPlatformClientStatusEvent,
       "vmwNSXTMPNodeServiceNSXUpgradeAgentStatusEvent": vmwNSXTMPNodeServiceNSXUpgradeAgentStatusEvent,
       "vmwNSXTMPNodeServiceNTPStatusEvent": vmwNSXTMPNodeServiceNTPStatusEvent,
       "vmwNSXTMPNodeServicePolicyStatusEvent": vmwNSXTMPNodeServicePolicyStatusEvent,
       "vmwNSXTMPNodeServiceSearchStatusEvent": vmwNSXTMPNodeServiceSearchStatusEvent,
       "vmwNSXTMPNodeServiceSNMPStatusEvent": vmwNSXTMPNodeServiceSNMPStatusEvent,
       "vmwNSXTMPNodeServiceSSHStatusEvent": vmwNSXTMPNodeServiceSSHStatusEvent,
       "vmwNSXTMPNodeServiceSyslogStatusEvent": vmwNSXTMPNodeServiceSyslogStatusEvent,
       "vmwNSXTMPNodeServiceTelemetryStatusEvent": vmwNSXTMPNodeServiceTelemetryStatusEvent,
       "vmwNSXTMPNodeServiceUIServiceStatusEvent": vmwNSXTMPNodeServiceUIServiceStatusEvent,
       "vmwNSXTMPNodeServiceClusterManagerStatusEvent": vmwNSXTMPNodeServiceClusterManagerStatusEvent,
       "vmwIndexerLagEvent": vmwIndexerLagEvent,
       "vmwIPFIXFlowDPPausedEvent": vmwIPFIXFlowDPPausedEvent,
       "vmwGridProcessingStoppedEvent": vmwGridProcessingStoppedEvent,
       "vmwUnableToSendEmailsEvent": vmwUnableToSendEmailsEvent,
       "vmwSMTPNotConfiguredEvent": vmwSMTPNotConfiguredEvent,
       "vmwSNMPNotConfiguredEvent": vmwSNMPNotConfiguredEvent,
       "vmwReindexingInProgressEvent": vmwReindexingInProgressEvent,
       "vmwNodesVersionMismatchEvent": vmwNodesVersionMismatchEvent,
       "vmwNotAllServicesRunningEvent": vmwNotAllServicesRunningEvent,
       "vmwNotAllServicesHealthyEvent": vmwNotAllServicesHealthyEvent,
       "vmwExpandPartitionFailedEvent": vmwExpandPartitionFailedEvent,
       "vmwDiskCleanupFailedEvent": vmwDiskCleanupFailedEvent,
       "vmwVaccumFailedEvent": vmwVaccumFailedEvent,
       "vmwConfigStoreCleanupFailedEvent": vmwConfigStoreCleanupFailedEvent,
       "vmwHBaseRetentionToolFailedEvent": vmwHBaseRetentionToolFailedEvent,
       "vmwMetricStoreUpdaterFailedEvent": vmwMetricStoreUpdaterFailedEvent,
       "vmwCollectorLagEvent": vmwCollectorLagEvent,
       "vmwCollectionLagEvent": vmwCollectionLagEvent,
       "vmwGridProcessingLagEvent": vmwGridProcessingLagEvent,
       "vmwConnectionErrorEvent": vmwConnectionErrorEvent,
       "vmwNodeNotActiveEvent": vmwNodeNotActiveEvent,
       "vmwHighDiskUtilizationEvent": vmwHighDiskUtilizationEvent,
       "vmwIndexingAbortedEvent": vmwIndexingAbortedEvent,
       "vmwUpgradeFailedEvent": vmwUpgradeFailedEvent,
       "vmwFlowProcessingSuspendedEvent": vmwFlowProcessingSuspendedEvent,
       "vmwLargeSdmsDroppedEvent": vmwLargeSdmsDroppedEvent,
       "vmwApplianceNotConfiguredEvent": vmwApplianceNotConfiguredEvent,
       "vmwDiskAllocationInsufficientEvent": vmwDiskAllocationInsufficientEvent,
       "vmwFdbConfigStoreCleanupFailedEvent": vmwFdbConfigStoreCleanupFailedEvent,
       "vmwDeploymentDefMismatchEvent": vmwDeploymentDefMismatchEvent,
       "vmwLicenseExpiredEvent": vmwLicenseExpiredEvent,
       "vmwInGracePeriodEvent": vmwInGracePeriodEvent,
       "vmwUnableToSendSNMPTrapsEvent": vmwUnableToSendSNMPTrapsEvent,
       "vmwStreamProcessingFailedEvent": vmwStreamProcessingFailedEvent,
       "vmwIpfixFlowLagEvent": vmwIpfixFlowLagEvent,
       "vmwChangeEventsDroppedEvent": vmwChangeEventsDroppedEvent,
       "vmwServiceRestartCountExceededEvent": vmwServiceRestartCountExceededEvent,
       "vmwFailedEvent": vmwFailedEvent,
       "vmwTimeoutEvent": vmwTimeoutEvent,
       "vmwConnectionRefusedEvent": vmwConnectionRefusedEvent,
       "vmwSNOWMandatoryPrivilegesMissingEvent": vmwSNOWMandatoryPrivilegesMissingEvent,
       "vmwIncorrectConnectionStringEvent": vmwIncorrectConnectionStringEvent,
       "vmwInvalidCredentialsEvent": vmwInvalidCredentialsEvent,
       "vmwUnknownHostEvent": vmwUnknownHostEvent,
       "vmwSNMPConnectionInvalidEvent": vmwSNMPConnectionInvalidEvent,
       "vmwFailedCredsEncryptEvent": vmwFailedCredsEncryptEvent,
       "vmwPwdAuthModeDisabledEvent": vmwPwdAuthModeDisabledEvent,
       "vmwInsufficientPrivilegesEvent": vmwInsufficientPrivilegesEvent,
       "vmwNotFoundEvent": vmwNotFoundEvent,
       "vmwInvalidConfigEvent": vmwInvalidConfigEvent,
       "vmwWarnConfigEvent": vmwWarnConfigEvent,
       "vmwUnexpectedDSTypeOrVersionEvent": vmwUnexpectedDSTypeOrVersionEvent,
       "vmwNSXControllerNotFoundEvent": vmwNSXControllerNotFoundEvent,
       "vmwHostNotReachableEvent": vmwHostNotReachableEvent,
       "vmwInvalidResponseFromDatasourceEvent": vmwInvalidResponseFromDatasourceEvent,
       "vmwDataProviderNotRunningEvent": vmwDataProviderNotRunningEvent,
       "vmwPrimaryNSXNotAddedEvent": vmwPrimaryNSXNotAddedEvent,
       "vmwHostnameResolutionErrorEvent": vmwHostnameResolutionErrorEvent,
       "vmwNumVMsOrHostsNotFoundEvent": vmwNumVMsOrHostsNotFoundEvent,
       "vmwNSXIPFIXStatusMismatchEvent": vmwNSXIPFIXStatusMismatchEvent,
       "vmwFlowPhysicalNodeEvent": vmwFlowPhysicalNodeEvent,
       "vmwNotEmptyNodeEvent": vmwNotEmptyNodeEvent,
       "vmwUnsupportedNSXTVersionEvent": vmwUnsupportedNSXTVersionEvent,
       "vmwComputeManagersNotFoundEvent": vmwComputeManagersNotFoundEvent,
       "vmwComputeManagersNotAddedEvent": vmwComputeManagersNotAddedEvent,
       "vmwUnsupportedLogInsightVersionEvent": vmwUnsupportedLogInsightVersionEvent,
       "vmwUnsupportedVRNIContentPackVersionEvent": vmwUnsupportedVRNIContentPackVersionEvent,
       "vmwVRNIContentPackNotInstalledEvent": vmwVRNIContentPackNotInstalledEvent,
       "vmwWebhookNotEnabledOnAlertEvent": vmwWebhookNotEnabledOnAlertEvent,
       "vmwIncorrectWebhookConfiguredOnAlertEvent": vmwIncorrectWebhookConfiguredOnAlertEvent,
       "vmwWebhookNotRunningEvent": vmwWebhookNotRunningEvent,
       "vmwInfobloxRecordLimitExceededEvent": vmwInfobloxRecordLimitExceededEvent,
       "vmwIncorrectInfobloxCredentialEvent": vmwIncorrectInfobloxCredentialEvent,
       "vmwUnsupportedInfobloxVersionEvent": vmwUnsupportedInfobloxVersionEvent,
       "vmwUnknownInfobloxVersionEvent": vmwUnknownInfobloxVersionEvent,
       "vmwNoDVSAvailableEvent": vmwNoDVSAvailableEvent,
       "vmwVCNotOnSameProxyEvent": vmwVCNotOnSameProxyEvent,
       "vmwNSXTIPFixNoCollectorProfileEvent": vmwNSXTIPFixNoCollectorProfileEvent,
       "vmwNSXTIPFixNoNewCollectorProfileCanBeAddedEvent": vmwNSXTIPFixNoNewCollectorProfileCanBeAddedEvent,
       "vmwNSXTIPFixNoIPFixProfileEvent": vmwNSXTIPFixNoIPFixProfileEvent,
       "vmwNSXTIPFixIPFixProfilePriorityNotZeroEvent": vmwNSXTIPFixIPFixProfilePriorityNotZeroEvent,
       "vmwNSXTIPFixCollectorAndIPFixProfileMismatchEvent": vmwNSXTIPFixCollectorAndIPFixProfileMismatchEvent,
       "vmwNSXTIPFixPortIncorrectEvent": vmwNSXTIPFixPortIncorrectEvent,
       "vmwNSXTIPFixDFWStatusNotEnabledEvent": vmwNSXTIPFixDFWStatusNotEnabledEvent,
       "vmwPolicyManagerNoDfwIPFixProfile": vmwPolicyManagerNoDfwIPFixProfile,
       "vmwPolicyManagerVrniDfwIPFixCollectorAbsent": vmwPolicyManagerVrniDfwIPFixCollectorAbsent,
       "vmwDatasourceIdentificationChangedEvent": vmwDatasourceIdentificationChangedEvent,
       "vmwPKSKubernetesUnknownHostEvent": vmwPKSKubernetesUnknownHostEvent,
       "vmwKubernetesInsufficientPrivilegesEvent": vmwKubernetesInsufficientPrivilegesEvent,
       "vmwUANIFileNotProvidedEvent": vmwUANIFileNotProvidedEvent,
       "vmwUANIFileDoesNotExistEvent": vmwUANIFileDoesNotExistEvent,
       "vmwNSXTLatencyNotEnabledEvent": vmwNSXTLatencyNotEnabledEvent,
       "vmwNSXTLatencyMoreBFDProfileEvent": vmwNSXTLatencyMoreBFDProfileEvent,
       "vmwNSXTLatencyNoBFDProfileEvent": vmwNSXTLatencyNoBFDProfileEvent,
       "vmwNSXTLatencyCollectorMismatchEvent": vmwNSXTLatencyCollectorMismatchEvent,
       "vmwBigIpInsufficientShellAccessEvent": vmwBigIpInsufficientShellAccessEvent,
       "vmwBigIpInsufficientPartitionAccessEvent": vmwBigIpInsufficientPartitionAccessEvent,
       "vmwBigIpInsufficientRoleEvent": vmwBigIpInsufficientRoleEvent,
       "vmwNsxtLatencyStatProfileMismatchEvent": vmwNsxtLatencyStatProfileMismatchEvent,
       "vmwNsxtLatencyNodeGroupMismatchEvent": vmwNsxtLatencyNodeGroupMismatchEvent,
       "vmwNsxtLatencyServiceConfigMismatchEvent": vmwNsxtLatencyServiceConfigMismatchEvent,
       "vmwNsxtNotificationWebhookDisabledEvent": vmwNsxtNotificationWebhookDisabledEvent,
       "vmwFailedDatasourceOperationEvent": vmwFailedDatasourceOperationEvent,
       "vmwUnsupportedNsxAlbVersionEvent": vmwUnsupportedNsxAlbVersionEvent,
       "vmwTkgiKubernetesNotReachableEvent": vmwTkgiKubernetesNotReachableEvent,
       "vmwTkgiClustersInsufficientPriviledgesEvent": vmwTkgiClustersInsufficientPriviledgesEvent,
       "vmwVeloCloudEdgeDownEvent": vmwVeloCloudEdgeDownEvent,
       "vmwVeloCloudLinkDownEvent": vmwVeloCloudLinkDownEvent,
       "vmwVeloCloudLinkLostPacketEventTx": vmwVeloCloudLinkLostPacketEventTx,
       "vmwVeloCloudLinkDegradedVoiceQoeEvent": vmwVeloCloudLinkDegradedVoiceQoeEvent,
       "vmwVeloCloudLinkDegradedVideoQoeEvent": vmwVeloCloudLinkDegradedVideoQoeEvent,
       "vmwVeloCloudLinkDegradedTransQoeEvent": vmwVeloCloudLinkDegradedTransQoeEvent,
       "vmwVeloCloudEdgeDegradedVoiceQoeEvent": vmwVeloCloudEdgeDegradedVoiceQoeEvent,
       "vmwVeloCloudEdgeDegradedVideoQoeEvent": vmwVeloCloudEdgeDegradedVideoQoeEvent,
       "vmwVeloCloudEdgeDegradedTransQoeEvent": vmwVeloCloudEdgeDegradedTransQoeEvent,
       "vmwVeloCloudLinkLostPacketEventRx": vmwVeloCloudLinkLostPacketEventRx,
       "vmwSDWanLinkTrafficThresholdEvent": vmwSDWanLinkTrafficThresholdEvent,
       "vmwHcxIXServiceStatusEvent": vmwHcxIXServiceStatusEvent,
       "vmwHcxIXApplianceEncryptionTunnelStatusEvent": vmwHcxIXApplianceEncryptionTunnelStatusEvent,
       "vmwHcxNEServiceStatusEvent": vmwHcxNEServiceStatusEvent,
       "vmwHcxNEApplianceEncryptionTunnelStatusEvent": vmwHcxNEApplianceEncryptionTunnelStatusEvent,
       "vmwHcxIXApplianceServicePipelineStatusEvent": vmwHcxIXApplianceServicePipelineStatusEvent,
       "vmwHcxNEApplianceServicePipelineStatusEvent": vmwHcxNEApplianceServicePipelineStatusEvent,
       "vmwHcxIXApplianceServiceTransportStatusEvent": vmwHcxIXApplianceServiceTransportStatusEvent,
       "vmwHcxNEApplianceServiceTransportStatusEvent": vmwHcxNEApplianceServiceTransportStatusEvent,
       "vmwHcxIXApplianceServiceSystemStateEvent": vmwHcxIXApplianceServiceSystemStateEvent,
       "vmwHcxNEApplianceServiceSystemStateEvent": vmwHcxNEApplianceServiceSystemStateEvent,
       "vmwHcxWanOptServiceStatusEvent": vmwHcxWanOptServiceStatusEvent,
       "vmwHcxBMServiceStatusEvent": vmwHcxBMServiceStatusEvent,
       "vmwHcxVMotionServiceStatusEvent": vmwHcxVMotionServiceStatusEvent,
       "vmwHcxIXServiceNotRunningEvent": vmwHcxIXServiceNotRunningEvent,
       "vmwHcxNEServiceNotRunningEvent": vmwHcxNEServiceNotRunningEvent,
       "vmwHcxWanOptServiceNotRunningEvent": vmwHcxWanOptServiceNotRunningEvent,
       "vmwHcxApplianceAllTunnelDownEvent": vmwHcxApplianceAllTunnelDownEvent,
       "vmwHcxConnectionRuleViolationEvent": vmwHcxConnectionRuleViolationEvent,
       "vmwHcxMtuMismatchEvent": vmwHcxMtuMismatchEvent,
       "vmwHcxApplianceUnhealthyTunnelsEvent": vmwHcxApplianceUnhealthyTunnelsEvent,
       "vmwHcxManagerVersionMismatchEvent": vmwHcxManagerVersionMismatchEvent,
       "vmwHcxApplianceVersionMismatchEvent": vmwHcxApplianceVersionMismatchEvent,
       "vmwNSXVLatencyNoDataEvent": vmwNSXVLatencyNoDataEvent,
       "vmwVMCVMLimitExceededEvent": vmwVMCVMLimitExceededEvent,
       "vmwVMCHostLimitExceededEvent": vmwVMCHostLimitExceededEvent,
       "vmwVMCHostPerClusterLimitExceededEvent": vmwVMCHostPerClusterLimitExceededEvent,
       "vmwVMCVMPerHostLimitExceededEvent": vmwVMCVMPerHostLimitExceededEvent,
       "vmwVMCClusterLimitExceededEvent": vmwVMCClusterLimitExceededEvent,
       "vmwVMCCapacityThresholdBreachEvent": vmwVMCCapacityThresholdBreachEvent,
       "vmwProtectionEvent": vmwProtectionEvent,
       "vmwNativeVlanMismatchEvent": vmwNativeVlanMismatchEvent,
       "vmwNativeVlanTaggingMismatchEvent": vmwNativeVlanTaggingMismatchEvent,
       "vmwSnapshotNotBuildingEvent": vmwSnapshotNotBuildingEvent,
       "vmwProtectionActiveEvent": vmwProtectionActiveEvent,
       "vmwSNMPTrapEvent": vmwSNMPTrapEvent,
       "vmwFlowCollectionErrorEvent": vmwFlowCollectionErrorEvent,
       "vmwAWSThrottlingExceptionEvent": vmwAWSThrottlingExceptionEvent,
       "vmwAWSFlowLogAccessDeniedExceptionEvent": vmwAWSFlowLogAccessDeniedExceptionEvent,
       "vmwPwdAuthModeDisabledAristaEvent": vmwPwdAuthModeDisabledAristaEvent,
       "vmwUnsupportedNSXVersionEvent": vmwUnsupportedNSXVersionEvent,
       "vmwVRNIData": vmwVRNIData,
       "vmwAffectedObject": vmwAffectedObject,
       "vmwEventSeverity": vmwEventSeverity,
       "vmwVrniUrl": vmwVrniUrl,
       "vmwTimestamp": vmwTimestamp,
       "vmwOperatorDesc": vmwOperatorDesc,
       "vmwEventName": vmwEventName,
       "vmwNetworkInsightMIBConformance": vmwNetworkInsightMIBConformance,
       "vmwNetworkInsightMIBCompliances": vmwNetworkInsightMIBCompliances,
       "vmwNetworkInsightMIBBasicCompliance": vmwNetworkInsightMIBBasicCompliance,
       "vmwNetworkInsightMIBBasicCompliance2": vmwNetworkInsightMIBBasicCompliance2,
       "vmwNetworkInsightMIBBasicCompliance3": vmwNetworkInsightMIBBasicCompliance3,
       "vmwNetworkInsightMIBBasicCompliance4": vmwNetworkInsightMIBBasicCompliance4,
       "vmwNetworkInsightMIBBasicCompliance5": vmwNetworkInsightMIBBasicCompliance5,
       "vmwNetworkInsightMIBBasicCompliance6": vmwNetworkInsightMIBBasicCompliance6,
       "vmwNetworkInsightMIBBasicCompliance7": vmwNetworkInsightMIBBasicCompliance7,
       "vmwNetworkInsightMIBBasicCompliance8": vmwNetworkInsightMIBBasicCompliance8,
       "vmwNetworkInsightMIBBasicCompliance9": vmwNetworkInsightMIBBasicCompliance9,
       "vmwNetworkInsightMIBBasicCompliance10": vmwNetworkInsightMIBBasicCompliance10,
       "vmwNetworkInsightMIBBasicCompliance11": vmwNetworkInsightMIBBasicCompliance11,
       "vmwNetworkInsightMIBBasicCompliance12": vmwNetworkInsightMIBBasicCompliance12,
       "vmwNetworkInsightMIBBasicCompliance13": vmwNetworkInsightMIBBasicCompliance13,
       "vmwNetworkInsightMIBBasicCompliance14": vmwNetworkInsightMIBBasicCompliance14,
       "vmwNetworkInsightMIBBasicCompliance15": vmwNetworkInsightMIBBasicCompliance15,
       "vmwNetworkInsightMIBGroups": vmwNetworkInsightMIBGroups,
       "vmwNetworkInsightNotificationInfoGroup1": vmwNetworkInsightNotificationInfoGroup1,
       "vmwNetworkInsightNotificationGroup1": vmwNetworkInsightNotificationGroup1,
       "vmwNetworkInsightNotificationInfoGroup2": vmwNetworkInsightNotificationInfoGroup2,
       "vmwNetworkInsightNotificationGroup2": vmwNetworkInsightNotificationGroup2,
       "vmwNetworkInsightNotificationGroup3": vmwNetworkInsightNotificationGroup3,
       "vmwNetworkInsightNotificationGroup4": vmwNetworkInsightNotificationGroup4,
       "vmwNetworkInsightNotificationInfoGroup3": vmwNetworkInsightNotificationInfoGroup3,
       "vmwNetworkInsightNotificationGroup5": vmwNetworkInsightNotificationGroup5,
       "vmwNetworkInsightNotificationGroup6": vmwNetworkInsightNotificationGroup6,
       "vmwNetworkInsightNotificationGroup7": vmwNetworkInsightNotificationGroup7,
       "vmwNetworkInsightNotificationGroup8": vmwNetworkInsightNotificationGroup8,
       "vmwNetworkInsightNotificationGroup9": vmwNetworkInsightNotificationGroup9,
       "vmwNetworkInsightNotificationGroup10": vmwNetworkInsightNotificationGroup10,
       "vmwNetworkInsightNotificationGroup11": vmwNetworkInsightNotificationGroup11,
       "vmwNetworkInsightNotificationGroup12": vmwNetworkInsightNotificationGroup12,
       "vmwNetworkInsightNotificationGroup13": vmwNetworkInsightNotificationGroup13,
       "vmwNetworkInsightNotificationGroup14": vmwNetworkInsightNotificationGroup14,
       "vmwNetworkInsightNotificationGroup15": vmwNetworkInsightNotificationGroup15}
)
