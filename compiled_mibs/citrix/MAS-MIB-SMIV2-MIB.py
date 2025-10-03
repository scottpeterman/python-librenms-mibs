# SNMP MIB module (MAS-MIB-SMIV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\citrix\MAS-MIB-SMIV2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:30:35 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

netScaler = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5951)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MasRoot_ObjectIdentity = ObjectIdentity
masRoot = _MasRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 7)
)
_MasEventGroup_ObjectIdentity = ObjectIdentity
masEventGroup = _MasEventGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1)
)
_EventVarBindOids_ObjectIdentity = ObjectIdentity
eventVarBindOids = _EventVarBindOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 1)
)
_Source_Type = OctetString
_Source_Object = MibScalar
source = _Source_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 1, 1),
    _Source_Type()
)
source.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    source.setStatus("current")
_EntityName_Type = OctetString
_EntityName_Object = MibScalar
entityName = _EntityName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 1, 2),
    _EntityName_Type()
)
entityName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    entityName.setStatus("current")
_EntityType_Type = OctetString
_EntityType_Object = MibScalar
entityType = _EntityType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 1, 3),
    _EntityType_Type()
)
entityType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    entityType.setStatus("current")
_EventMessage_Type = OctetString
_EventMessage_Object = MibScalar
eventMessage = _EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 1, 4),
    _EventMessage_Type()
)
eventMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventMessage.setStatus("current")
_ThresholdValue_Type = OctetString
_ThresholdValue_Object = MibScalar
thresholdValue = _ThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 1, 5),
    _ThresholdValue_Type()
)
thresholdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    thresholdValue.setStatus("current")
_CurrentValue_Type = OctetString
_CurrentValue_Object = MibScalar
currentValue = _CurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 1, 6),
    _CurrentValue_Type()
)
currentValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    currentValue.setStatus("current")
_Severity_Type = OctetString
_Severity_Object = MibScalar
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 1, 7),
    _Severity_Type()
)
severity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    severity.setStatus("current")
_MpsEvents_ObjectIdentity = ObjectIdentity
mpsEvents = _MpsEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2)
)
_SystemGroup_ObjectIdentity = ObjectIdentity
systemGroup = _SystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2)
)
_SystemPlatform_Type = OctetString
_SystemPlatform_Object = MibScalar
systemPlatform = _SystemPlatform_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 1),
    _SystemPlatform_Type()
)
systemPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPlatform.setStatus("current")
_SystemProduct_Type = OctetString
_SystemProduct_Object = MibScalar
systemProduct = _SystemProduct_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 2),
    _SystemProduct_Type()
)
systemProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemProduct.setStatus("current")
_SystemBuildNumber_Type = OctetString
_SystemBuildNumber_Object = MibScalar
systemBuildNumber = _SystemBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 3),
    _SystemBuildNumber_Type()
)
systemBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBuildNumber.setStatus("current")
_SystemIPAddressType_Type = InetAddressType
_SystemIPAddressType_Object = MibScalar
systemIPAddressType = _SystemIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 4),
    _SystemIPAddressType_Type()
)
systemIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemIPAddressType.setStatus("current")
_SystemIPAddress_Type = InetAddress
_SystemIPAddress_Object = MibScalar
systemIPAddress = _SystemIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 5),
    _SystemIPAddress_Type()
)
systemIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemIPAddress.setStatus("current")
_SystemNetmaskType_Type = InetAddressType
_SystemNetmaskType_Object = MibScalar
systemNetmaskType = _SystemNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 6),
    _SystemNetmaskType_Type()
)
systemNetmaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNetmaskType.setStatus("current")
_SystemNetmask_Type = InetAddress
_SystemNetmask_Object = MibScalar
systemNetmask = _SystemNetmask_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 7),
    _SystemNetmask_Type()
)
systemNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNetmask.setStatus("current")
_SystemGatewayType_Type = InetAddressType
_SystemGatewayType_Object = MibScalar
systemGatewayType = _SystemGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 8),
    _SystemGatewayType_Type()
)
systemGatewayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemGatewayType.setStatus("current")
_SystemGateway_Type = InetAddress
_SystemGateway_Object = MibScalar
systemGateway = _SystemGateway_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 9),
    _SystemGateway_Type()
)
systemGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemGateway.setStatus("current")
_SystemDnsType_Type = InetAddressType
_SystemDnsType_Object = MibScalar
systemDnsType = _SystemDnsType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 10),
    _SystemDnsType_Type()
)
systemDnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDnsType.setStatus("current")
_SystemDns_Type = InetAddress
_SystemDns_Object = MibScalar
systemDns = _SystemDns_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 11),
    _SystemDns_Type()
)
systemDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDns.setStatus("current")
_SystemSysId_Type = OctetString
_SystemSysId_Object = MibScalar
systemSysId = _SystemSysId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 12),
    _SystemSysId_Type()
)
systemSysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSysId.setStatus("current")
_SystemSerial_Type = OctetString
_SystemSerial_Object = MibScalar
systemSerial = _SystemSerial_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 13),
    _SystemSerial_Type()
)
systemSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSerial.setStatus("current")
_SystemCurrentTime_Type = Integer32
_SystemCurrentTime_Object = MibScalar
systemCurrentTime = _SystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 14),
    _SystemCurrentTime_Type()
)
systemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCurrentTime.setStatus("current")
_SystemUptime_Type = OctetString
_SystemUptime_Object = MibScalar
systemUptime = _SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 15),
    _SystemUptime_Type()
)
systemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUptime.setStatus("current")
_SystemBiosVersion_Type = OctetString
_SystemBiosVersion_Object = MibScalar
systemBiosVersion = _SystemBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 16),
    _SystemBiosVersion_Type()
)
systemBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBiosVersion.setStatus("current")
_SystemCustomID_Type = OctetString
_SystemCustomID_Object = MibScalar
systemCustomID = _SystemCustomID_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 17),
    _SystemCustomID_Type()
)
systemCustomID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCustomID.setStatus("current")
_SystemCpuUsage_Type = OctetString
_SystemCpuUsage_Object = MibScalar
systemCpuUsage = _SystemCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 18),
    _SystemCpuUsage_Type()
)
systemCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCpuUsage.setStatus("current")
_SystemMemoryUsage_Type = OctetString
_SystemMemoryUsage_Object = MibScalar
systemMemoryUsage = _SystemMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 19),
    _SystemMemoryUsage_Type()
)
systemMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMemoryUsage.setStatus("current")
_SystemDiskUsage_Type = OctetString
_SystemDiskUsage_Object = MibScalar
systemDiskUsage = _SystemDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 2, 20),
    _SystemDiskUsage_Type()
)
systemDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDiskUsage.setStatus("current")
_DeviceGroup_ObjectIdentity = ObjectIdentity
deviceGroup = _DeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3)
)
_NetscalerTable_Object = MibTable
netscalerTable = _NetscalerTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2)
)
if mibBuilder.loadTexts:
    netscalerTable.setStatus("current")
_NetscalerEntry_Object = MibTableRow
netscalerEntry = _NetscalerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1)
)
netscalerEntry.setIndexNames(
    (0, "MAS-MIB-SMIV2-MIB", "nsIpAddressType"),
    (0, "MAS-MIB-SMIV2-MIB", "nsIpAddress"),
    (0, "MAS-MIB-SMIV2-MIB", "nsHostIPAddressType"),
    (0, "MAS-MIB-SMIV2-MIB", "nsHostIPAddress"),
)
if mibBuilder.loadTexts:
    netscalerEntry.setStatus("current")
_NsIpAddressType_Type = InetAddressType
_NsIpAddressType_Object = MibTableColumn
nsIpAddressType = _NsIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 1),
    _NsIpAddressType_Type()
)
nsIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIpAddressType.setStatus("current")
_NsIpAddress_Type = InetAddress
_NsIpAddress_Object = MibTableColumn
nsIpAddress = _NsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 2),
    _NsIpAddress_Type()
)
nsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIpAddress.setStatus("current")
_NsHostIPAddressType_Type = InetAddressType
_NsHostIPAddressType_Object = MibTableColumn
nsHostIPAddressType = _NsHostIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 3),
    _NsHostIPAddressType_Type()
)
nsHostIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsHostIPAddressType.setStatus("current")
_NsHostIPAddress_Type = InetAddress
_NsHostIPAddress_Object = MibTableColumn
nsHostIPAddress = _NsHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 4),
    _NsHostIPAddress_Type()
)
nsHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsHostIPAddress.setStatus("current")
_NsProfileName_Type = OctetString
_NsProfileName_Object = MibTableColumn
nsProfileName = _NsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 5),
    _NsProfileName_Type()
)
nsProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsProfileName.setStatus("current")
_NsName_Type = OctetString
_NsName_Object = MibTableColumn
nsName = _NsName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 6),
    _NsName_Type()
)
nsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsName.setStatus("current")
_NsNetmaskType_Type = InetAddressType
_NsNetmaskType_Object = MibTableColumn
nsNetmaskType = _NsNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 7),
    _NsNetmaskType_Type()
)
nsNetmaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNetmaskType.setStatus("current")
_NsNetmask_Type = InetAddress
_NsNetmask_Object = MibTableColumn
nsNetmask = _NsNetmask_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 8),
    _NsNetmask_Type()
)
nsNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNetmask.setStatus("current")
_NsGatewayType_Type = InetAddressType
_NsGatewayType_Object = MibTableColumn
nsGatewayType = _NsGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 9),
    _NsGatewayType_Type()
)
nsGatewayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsGatewayType.setStatus("current")
_NsGateway_Type = InetAddress
_NsGateway_Object = MibTableColumn
nsGateway = _NsGateway_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 10),
    _NsGateway_Type()
)
nsGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsGateway.setStatus("current")
_NsHostname_Type = OctetString
_NsHostname_Object = MibTableColumn
nsHostname = _NsHostname_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 11),
    _NsHostname_Type()
)
nsHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsHostname.setStatus("current")
_NsDescription_Type = OctetString
_NsDescription_Object = MibTableColumn
nsDescription = _NsDescription_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 12),
    _NsDescription_Type()
)
nsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsDescription.setStatus("current")
_NsVersion_Type = OctetString
_NsVersion_Object = MibTableColumn
nsVersion = _NsVersion_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 13),
    _NsVersion_Type()
)
nsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVersion.setStatus("current")
_NsUuid_Type = OctetString
_NsUuid_Object = MibTableColumn
nsUuid = _NsUuid_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 14),
    _NsUuid_Type()
)
nsUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsUuid.setStatus("current")
_NsInstanceState_Type = OctetString
_NsInstanceState_Object = MibTableColumn
nsInstanceState = _NsInstanceState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 15),
    _NsInstanceState_Type()
)
nsInstanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsInstanceState.setStatus("current")
_NsVirtualFunctions_Type = OctetString
_NsVirtualFunctions_Object = MibTableColumn
nsVirtualFunctions = _NsVirtualFunctions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 16),
    _NsVirtualFunctions_Type()
)
nsVirtualFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVirtualFunctions.setStatus("current")
_NsSslVirtualFunctions_Type = OctetString
_NsSslVirtualFunctions_Object = MibTableColumn
nsSslVirtualFunctions = _NsSslVirtualFunctions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 17),
    _NsSslVirtualFunctions_Type()
)
nsSslVirtualFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSslVirtualFunctions.setStatus("current")
_NsVmState_Type = OctetString
_NsVmState_Object = MibTableColumn
nsVmState = _NsVmState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 18),
    _NsVmState_Type()
)
nsVmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVmState.setStatus("current")
_NsNumberOfCPU_Type = Integer32
_NsNumberOfCPU_Object = MibTableColumn
nsNumberOfCPU = _NsNumberOfCPU_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 19),
    _NsNumberOfCPU_Type()
)
nsNumberOfCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNumberOfCPU.setStatus("current")
_NsVmMemoryTotal_Type = OctetString
_NsVmMemoryTotal_Object = MibTableColumn
nsVmMemoryTotal = _NsVmMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 21),
    _NsVmMemoryTotal_Type()
)
nsVmMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVmMemoryTotal.setStatus("current")
_NsUptime_Type = OctetString
_NsUptime_Object = MibTableColumn
nsUptime = _NsUptime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 26),
    _NsUptime_Type()
)
nsUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsUptime.setStatus("current")
_NsNumberOfSSLCores_Type = Integer32
_NsNumberOfSSLCores_Object = MibTableColumn
nsNumberOfSSLCores = _NsNumberOfSSLCores_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 27),
    _NsNumberOfSSLCores_Type()
)
nsNumberOfSSLCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNumberOfSSLCores.setStatus("current")
_NsCpuCoreMgmt_Type = OctetString
_NsCpuCoreMgmt_Object = MibTableColumn
nsCpuCoreMgmt = _NsCpuCoreMgmt_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 28),
    _NsCpuCoreMgmt_Type()
)
nsCpuCoreMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCpuCoreMgmt.setStatus("current")
_NsCpuCorePE_Type = OctetString
_NsCpuCorePE_Object = MibTableColumn
nsCpuCorePE = _NsCpuCorePE_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 29),
    _NsCpuCorePE_Type()
)
nsCpuCorePE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCpuCorePE.setStatus("current")
_NsVmDescription_Type = OctetString
_NsVmDescription_Object = MibTableColumn
nsVmDescription = _NsVmDescription_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 30),
    _NsVmDescription_Type()
)
nsVmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVmDescription.setStatus("current")
_NsThroughput_Type = OctetString
_NsThroughput_Object = MibTableColumn
nsThroughput = _NsThroughput_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 31),
    _NsThroughput_Type()
)
nsThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsThroughput.setStatus("current")
_NsNumberOfCores_Type = Integer32
_NsNumberOfCores_Object = MibTableColumn
nsNumberOfCores = _NsNumberOfCores_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 32),
    _NsNumberOfCores_Type()
)
nsNumberOfCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNumberOfCores.setStatus("current")
_NsNsCPUUsage_Type = OctetString
_NsNsCPUUsage_Object = MibTableColumn
nsNsCPUUsage = _NsNsCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 33),
    _NsNsCPUUsage_Type()
)
nsNsCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNsCPUUsage.setStatus("current")
_NsNsMemoryUsage_Type = OctetString
_NsNsMemoryUsage_Object = MibTableColumn
nsNsMemoryUsage = _NsNsMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 35),
    _NsNsMemoryUsage_Type()
)
nsNsMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNsMemoryUsage.setStatus("current")
_NsNsTx_Type = OctetString
_NsNsTx_Object = MibTableColumn
nsNsTx = _NsNsTx_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 36),
    _NsNsTx_Type()
)
nsNsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNsTx.setStatus("current")
_NsNsRx_Type = OctetString
_NsNsRx_Object = MibTableColumn
nsNsRx = _NsNsRx_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 37),
    _NsNsRx_Type()
)
nsNsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNsRx.setStatus("current")
_NsHttpReq_Type = OctetString
_NsHttpReq_Object = MibTableColumn
nsHttpReq = _NsHttpReq_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 38),
    _NsHttpReq_Type()
)
nsHttpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsHttpReq.setStatus("current")
_NsUpsince_Type = OctetString
_NsUpsince_Object = MibTableColumn
nsUpsince = _NsUpsince_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 39),
    _NsUpsince_Type()
)
nsUpsince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsUpsince.setStatus("current")
_NsLicense_Type = OctetString
_NsLicense_Object = MibTableColumn
nsLicense = _NsLicense_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 40),
    _NsLicense_Type()
)
nsLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsLicense.setStatus("current")
_NsHaMasterState_Type = OctetString
_NsHaMasterState_Object = MibTableColumn
nsHaMasterState = _NsHaMasterState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 41),
    _NsHaMasterState_Type()
)
nsHaMasterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsHaMasterState.setStatus("current")
_NsHaIPAddressType_Type = InetAddressType
_NsHaIPAddressType_Object = MibTableColumn
nsHaIPAddressType = _NsHaIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 42),
    _NsHaIPAddressType_Type()
)
nsHaIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsHaIPAddressType.setStatus("current")
_NsHaIPAddress_Type = InetAddress
_NsHaIPAddress_Object = MibTableColumn
nsHaIPAddress = _NsHaIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 43),
    _NsHaIPAddress_Type()
)
nsHaIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsHaIPAddress.setStatus("current")
_NsNodeState_Type = OctetString
_NsNodeState_Object = MibTableColumn
nsNodeState = _NsNodeState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 44),
    _NsNodeState_Type()
)
nsNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNodeState.setStatus("current")
_NsHaSync_Type = OctetString
_NsHaSync_Object = MibTableColumn
nsHaSync = _NsHaSync_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 45),
    _NsHaSync_Type()
)
nsHaSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsHaSync.setStatus("current")
_NsPps_Type = OctetString
_NsPps_Object = MibTableColumn
nsPps = _NsPps_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 46),
    _NsPps_Type()
)
nsPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPps.setStatus("current")
_NsNumberOfSslCoresUp_Type = Integer32
_NsNumberOfSslCoresUp_Object = MibTableColumn
nsNumberOfSslCoresUp = _NsNumberOfSslCoresUp_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 47),
    _NsNumberOfSslCoresUp_Type()
)
nsNumberOfSslCoresUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNumberOfSslCoresUp.setStatus("current")
_NsIfOby1_Type = OctetString
_NsIfOby1_Object = MibTableColumn
nsIfOby1 = _NsIfOby1_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 48),
    _NsIfOby1_Type()
)
nsIfOby1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfOby1.setStatus("current")
_NsIf0by2_Type = OctetString
_NsIf0by2_Object = MibTableColumn
nsIf0by2 = _NsIf0by2_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 49),
    _NsIf0by2_Type()
)
nsIf0by2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIf0by2.setStatus("current")
_NsNsVLANId_Type = Integer32
_NsNsVLANId_Object = MibTableColumn
nsNsVLANId = _NsNsVLANId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 50),
    _NsNsVLANId_Type()
)
nsNsVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNsVLANId.setStatus("current")
_NsNsVLANTagged_Type = OctetString
_NsNsVLANTagged_Object = MibTableColumn
nsNsVLANTagged = _NsNsVLANTagged_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 51),
    _NsNsVLANTagged_Type()
)
nsNsVLANTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNsVLANTagged.setStatus("current")
_NsVlanType_Type = Integer32
_NsVlanType_Object = MibTableColumn
nsVlanType = _NsVlanType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 2, 1, 52),
    _NsVlanType_Type()
)
nsVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVlanType.setStatus("current")
_CloudBridgeTable_Object = MibTable
cloudBridgeTable = _CloudBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3)
)
if mibBuilder.loadTexts:
    cloudBridgeTable.setStatus("current")
_CloudBridgeEntry_Object = MibTableRow
cloudBridgeEntry = _CloudBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1)
)
cloudBridgeEntry.setIndexNames(
    (0, "MAS-MIB-SMIV2-MIB", "cbIpAddressType"),
    (0, "MAS-MIB-SMIV2-MIB", "cbIpAddress"),
    (0, "MAS-MIB-SMIV2-MIB", "cbHostIPAddressType"),
    (0, "MAS-MIB-SMIV2-MIB", "cbHostIPAddress"),
)
if mibBuilder.loadTexts:
    cloudBridgeEntry.setStatus("current")
_CbIpAddressType_Type = InetAddressType
_CbIpAddressType_Object = MibTableColumn
cbIpAddressType = _CbIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 1),
    _CbIpAddressType_Type()
)
cbIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbIpAddressType.setStatus("current")
_CbIpAddress_Type = InetAddress
_CbIpAddress_Object = MibTableColumn
cbIpAddress = _CbIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 2),
    _CbIpAddress_Type()
)
cbIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbIpAddress.setStatus("current")
_CbHostIPAddressType_Type = InetAddressType
_CbHostIPAddressType_Object = MibTableColumn
cbHostIPAddressType = _CbHostIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 3),
    _CbHostIPAddressType_Type()
)
cbHostIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbHostIPAddressType.setStatus("current")
_CbHostIPAddress_Type = InetAddress
_CbHostIPAddress_Object = MibTableColumn
cbHostIPAddress = _CbHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 4),
    _CbHostIPAddress_Type()
)
cbHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbHostIPAddress.setStatus("current")
_CbProfileName_Type = OctetString
_CbProfileName_Object = MibTableColumn
cbProfileName = _CbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 5),
    _CbProfileName_Type()
)
cbProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbProfileName.setStatus("current")
_CbName_Type = OctetString
_CbName_Object = MibTableColumn
cbName = _CbName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 6),
    _CbName_Type()
)
cbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbName.setStatus("current")
_CbNetmaskType_Type = InetAddressType
_CbNetmaskType_Object = MibTableColumn
cbNetmaskType = _CbNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 7),
    _CbNetmaskType_Type()
)
cbNetmaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbNetmaskType.setStatus("current")
_CbNetmask_Type = InetAddress
_CbNetmask_Object = MibTableColumn
cbNetmask = _CbNetmask_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 8),
    _CbNetmask_Type()
)
cbNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbNetmask.setStatus("current")
_CbGatewayType_Type = InetAddressType
_CbGatewayType_Object = MibTableColumn
cbGatewayType = _CbGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 9),
    _CbGatewayType_Type()
)
cbGatewayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbGatewayType.setStatus("current")
_CbGateway_Type = InetAddress
_CbGateway_Object = MibTableColumn
cbGateway = _CbGateway_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 10),
    _CbGateway_Type()
)
cbGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbGateway.setStatus("current")
_CbHostname_Type = OctetString
_CbHostname_Object = MibTableColumn
cbHostname = _CbHostname_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 11),
    _CbHostname_Type()
)
cbHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbHostname.setStatus("current")
_CbDescription_Type = OctetString
_CbDescription_Object = MibTableColumn
cbDescription = _CbDescription_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 12),
    _CbDescription_Type()
)
cbDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbDescription.setStatus("current")
_CbVersion_Type = OctetString
_CbVersion_Object = MibTableColumn
cbVersion = _CbVersion_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 13),
    _CbVersion_Type()
)
cbVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbVersion.setStatus("current")
_CbInstanceState_Type = OctetString
_CbInstanceState_Object = MibTableColumn
cbInstanceState = _CbInstanceState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 14),
    _CbInstanceState_Type()
)
cbInstanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbInstanceState.setStatus("current")
_CbUuid_Type = OctetString
_CbUuid_Object = MibTableColumn
cbUuid = _CbUuid_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 15),
    _CbUuid_Type()
)
cbUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbUuid.setStatus("current")
_CbVirtualFunctions_Type = OctetString
_CbVirtualFunctions_Object = MibTableColumn
cbVirtualFunctions = _CbVirtualFunctions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 16),
    _CbVirtualFunctions_Type()
)
cbVirtualFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbVirtualFunctions.setStatus("current")
_CbVmState_Type = OctetString
_CbVmState_Object = MibTableColumn
cbVmState = _CbVmState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 17),
    _CbVmState_Type()
)
cbVmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbVmState.setStatus("current")
_CbNumberOfCPU_Type = Integer32
_CbNumberOfCPU_Object = MibTableColumn
cbNumberOfCPU = _CbNumberOfCPU_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 18),
    _CbNumberOfCPU_Type()
)
cbNumberOfCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbNumberOfCPU.setStatus("current")
_CbVmCPUUsage_Type = OctetString
_CbVmCPUUsage_Object = MibTableColumn
cbVmCPUUsage = _CbVmCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 19),
    _CbVmCPUUsage_Type()
)
cbVmCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbVmCPUUsage.setStatus("current")
_CbVmMemoryTotal_Type = OctetString
_CbVmMemoryTotal_Object = MibTableColumn
cbVmMemoryTotal = _CbVmMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 20),
    _CbVmMemoryTotal_Type()
)
cbVmMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbVmMemoryTotal.setStatus("current")
_CbVmMemoryFree_Type = OctetString
_CbVmMemoryFree_Object = MibTableColumn
cbVmMemoryFree = _CbVmMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 21),
    _CbVmMemoryFree_Type()
)
cbVmMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbVmMemoryFree.setStatus("current")
_CbVmMemoryUsage_Type = OctetString
_CbVmMemoryUsage_Object = MibTableColumn
cbVmMemoryUsage = _CbVmMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 22),
    _CbVmMemoryUsage_Type()
)
cbVmMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbVmMemoryUsage.setStatus("current")
_CbUptime_Type = OctetString
_CbUptime_Object = MibTableColumn
cbUptime = _CbUptime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 25),
    _CbUptime_Type()
)
cbUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbUptime.setStatus("current")
_CbDiskAllocation_Type = OctetString
_CbDiskAllocation_Object = MibTableColumn
cbDiskAllocation = _CbDiskAllocation_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 30),
    _CbDiskAllocation_Type()
)
cbDiskAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbDiskAllocation.setStatus("current")
_CbAPAIPADDRESSType_Type = InetAddressType
_CbAPAIPADDRESSType_Object = MibTableColumn
cbAPAIPADDRESSType = _CbAPAIPADDRESSType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 47),
    _CbAPAIPADDRESSType_Type()
)
cbAPAIPADDRESSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAPAIPADDRESSType.setStatus("current")
_CbAPAIPADDRESS_Type = InetAddress
_CbAPAIPADDRESS_Object = MibTableColumn
cbAPAIPADDRESS = _CbAPAIPADDRESS_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 48),
    _CbAPAIPADDRESS_Type()
)
cbAPAIPADDRESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAPAIPADDRESS.setStatus("current")
_CbAPANetMaskType_Type = InetAddressType
_CbAPANetMaskType_Object = MibTableColumn
cbAPANetMaskType = _CbAPANetMaskType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 49),
    _CbAPANetMaskType_Type()
)
cbAPANetMaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAPANetMaskType.setStatus("current")
_CbAPANetMask_Type = InetAddress
_CbAPANetMask_Object = MibTableColumn
cbAPANetMask = _CbAPANetMask_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 50),
    _CbAPANetMask_Type()
)
cbAPANetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAPANetMask.setStatus("current")
_CbAPAGatewayType_Type = InetAddressType
_CbAPAGatewayType_Object = MibTableColumn
cbAPAGatewayType = _CbAPAGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 51),
    _CbAPAGatewayType_Type()
)
cbAPAGatewayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAPAGatewayType.setStatus("current")
_CbAPAGateway_Type = InetAddress
_CbAPAGateway_Object = MibTableColumn
cbAPAGateway = _CbAPAGateway_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 52),
    _CbAPAGateway_Type()
)
cbAPAGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAPAGateway.setStatus("current")
_CbPluginIPADDRESSType_Type = InetAddressType
_CbPluginIPADDRESSType_Object = MibTableColumn
cbPluginIPADDRESSType = _CbPluginIPADDRESSType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 53),
    _CbPluginIPADDRESSType_Type()
)
cbPluginIPADDRESSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbPluginIPADDRESSType.setStatus("current")
_CbPluginIPADDRESS_Type = InetAddress
_CbPluginIPADDRESS_Object = MibTableColumn
cbPluginIPADDRESS = _CbPluginIPADDRESS_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 54),
    _CbPluginIPADDRESS_Type()
)
cbPluginIPADDRESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbPluginIPADDRESS.setStatus("current")
_CbMgmtIPAddressType_Type = InetAddressType
_CbMgmtIPAddressType_Object = MibTableColumn
cbMgmtIPAddressType = _CbMgmtIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 57),
    _CbMgmtIPAddressType_Type()
)
cbMgmtIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbMgmtIPAddressType.setStatus("current")
_CbMgmtIPAddress_Type = InetAddress
_CbMgmtIPAddress_Object = MibTableColumn
cbMgmtIPAddress = _CbMgmtIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 3, 1, 58),
    _CbMgmtIPAddress_Type()
)
cbMgmtIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbMgmtIPAddress.setStatus("current")
_CloudBridgeAcceleratorTable_Object = MibTable
cloudBridgeAcceleratorTable = _CloudBridgeAcceleratorTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4)
)
if mibBuilder.loadTexts:
    cloudBridgeAcceleratorTable.setStatus("current")
_CloudBridgeAcceleratorEntry_Object = MibTableRow
cloudBridgeAcceleratorEntry = _CloudBridgeAcceleratorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1)
)
cloudBridgeAcceleratorEntry.setIndexNames(
    (0, "MAS-MIB-SMIV2-MIB", "cbAcceleratorIpAddressType"),
    (0, "MAS-MIB-SMIV2-MIB", "cbAcceleratorIpAddress"),
    (0, "MAS-MIB-SMIV2-MIB", "cbAcceleratorHostIPAddressType"),
    (0, "MAS-MIB-SMIV2-MIB", "cbAcceleratorHostIPAddress"),
)
if mibBuilder.loadTexts:
    cloudBridgeAcceleratorEntry.setStatus("current")
_CbAcceleratorIpAddressType_Type = InetAddressType
_CbAcceleratorIpAddressType_Object = MibTableColumn
cbAcceleratorIpAddressType = _CbAcceleratorIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 1),
    _CbAcceleratorIpAddressType_Type()
)
cbAcceleratorIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorIpAddressType.setStatus("current")
_CbAcceleratorIpAddress_Type = InetAddress
_CbAcceleratorIpAddress_Object = MibTableColumn
cbAcceleratorIpAddress = _CbAcceleratorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 2),
    _CbAcceleratorIpAddress_Type()
)
cbAcceleratorIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorIpAddress.setStatus("current")
_CbAcceleratorHostIPAddressType_Type = InetAddressType
_CbAcceleratorHostIPAddressType_Object = MibTableColumn
cbAcceleratorHostIPAddressType = _CbAcceleratorHostIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 3),
    _CbAcceleratorHostIPAddressType_Type()
)
cbAcceleratorHostIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorHostIPAddressType.setStatus("current")
_CbAcceleratorHostIPAddress_Type = InetAddress
_CbAcceleratorHostIPAddress_Object = MibTableColumn
cbAcceleratorHostIPAddress = _CbAcceleratorHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 4),
    _CbAcceleratorHostIPAddress_Type()
)
cbAcceleratorHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorHostIPAddress.setStatus("current")
_CbAcceleratorProfileName_Type = OctetString
_CbAcceleratorProfileName_Object = MibTableColumn
cbAcceleratorProfileName = _CbAcceleratorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 5),
    _CbAcceleratorProfileName_Type()
)
cbAcceleratorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorProfileName.setStatus("current")
_CbAcceleratorName_Type = OctetString
_CbAcceleratorName_Object = MibTableColumn
cbAcceleratorName = _CbAcceleratorName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 6),
    _CbAcceleratorName_Type()
)
cbAcceleratorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorName.setStatus("current")
_CbAcceleratorNetmaskType_Type = InetAddressType
_CbAcceleratorNetmaskType_Object = MibTableColumn
cbAcceleratorNetmaskType = _CbAcceleratorNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 7),
    _CbAcceleratorNetmaskType_Type()
)
cbAcceleratorNetmaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorNetmaskType.setStatus("current")
_CbAcceleratorNetmask_Type = InetAddress
_CbAcceleratorNetmask_Object = MibTableColumn
cbAcceleratorNetmask = _CbAcceleratorNetmask_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 8),
    _CbAcceleratorNetmask_Type()
)
cbAcceleratorNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorNetmask.setStatus("current")
_CbAcceleratorGatewayType_Type = InetAddressType
_CbAcceleratorGatewayType_Object = MibTableColumn
cbAcceleratorGatewayType = _CbAcceleratorGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 9),
    _CbAcceleratorGatewayType_Type()
)
cbAcceleratorGatewayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorGatewayType.setStatus("current")
_CbAcceleratorGateway_Type = InetAddress
_CbAcceleratorGateway_Object = MibTableColumn
cbAcceleratorGateway = _CbAcceleratorGateway_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 10),
    _CbAcceleratorGateway_Type()
)
cbAcceleratorGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorGateway.setStatus("current")
_CbAcceleratorHostname_Type = OctetString
_CbAcceleratorHostname_Object = MibTableColumn
cbAcceleratorHostname = _CbAcceleratorHostname_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 11),
    _CbAcceleratorHostname_Type()
)
cbAcceleratorHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorHostname.setStatus("current")
_CbAcceleratorDescription_Type = OctetString
_CbAcceleratorDescription_Object = MibTableColumn
cbAcceleratorDescription = _CbAcceleratorDescription_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 12),
    _CbAcceleratorDescription_Type()
)
cbAcceleratorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorDescription.setStatus("current")
_CbAcceleratorVersion_Type = OctetString
_CbAcceleratorVersion_Object = MibTableColumn
cbAcceleratorVersion = _CbAcceleratorVersion_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 13),
    _CbAcceleratorVersion_Type()
)
cbAcceleratorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorVersion.setStatus("current")
_CbAcceleratorInstanceState_Type = OctetString
_CbAcceleratorInstanceState_Object = MibTableColumn
cbAcceleratorInstanceState = _CbAcceleratorInstanceState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 14),
    _CbAcceleratorInstanceState_Type()
)
cbAcceleratorInstanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorInstanceState.setStatus("current")
_CbAcceleratorUuid_Type = OctetString
_CbAcceleratorUuid_Object = MibTableColumn
cbAcceleratorUuid = _CbAcceleratorUuid_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 15),
    _CbAcceleratorUuid_Type()
)
cbAcceleratorUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorUuid.setStatus("current")
_CbAcceleratorVmState_Type = OctetString
_CbAcceleratorVmState_Object = MibTableColumn
cbAcceleratorVmState = _CbAcceleratorVmState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 16),
    _CbAcceleratorVmState_Type()
)
cbAcceleratorVmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorVmState.setStatus("current")
_CbAcceleratorNumberOfCPU_Type = Integer32
_CbAcceleratorNumberOfCPU_Object = MibTableColumn
cbAcceleratorNumberOfCPU = _CbAcceleratorNumberOfCPU_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 17),
    _CbAcceleratorNumberOfCPU_Type()
)
cbAcceleratorNumberOfCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorNumberOfCPU.setStatus("current")
_CbAcceleratorVmCPUUsage_Type = OctetString
_CbAcceleratorVmCPUUsage_Object = MibTableColumn
cbAcceleratorVmCPUUsage = _CbAcceleratorVmCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 18),
    _CbAcceleratorVmCPUUsage_Type()
)
cbAcceleratorVmCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorVmCPUUsage.setStatus("current")
_CbAcceleratorVmMemoryTotal_Type = OctetString
_CbAcceleratorVmMemoryTotal_Object = MibTableColumn
cbAcceleratorVmMemoryTotal = _CbAcceleratorVmMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 19),
    _CbAcceleratorVmMemoryTotal_Type()
)
cbAcceleratorVmMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorVmMemoryTotal.setStatus("current")
_CbAcceleratorVmMemoryFree_Type = OctetString
_CbAcceleratorVmMemoryFree_Object = MibTableColumn
cbAcceleratorVmMemoryFree = _CbAcceleratorVmMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 20),
    _CbAcceleratorVmMemoryFree_Type()
)
cbAcceleratorVmMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorVmMemoryFree.setStatus("current")
_CbAcceleratorVmMemoryUsage_Type = OctetString
_CbAcceleratorVmMemoryUsage_Object = MibTableColumn
cbAcceleratorVmMemoryUsage = _CbAcceleratorVmMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 21),
    _CbAcceleratorVmMemoryUsage_Type()
)
cbAcceleratorVmMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorVmMemoryUsage.setStatus("current")
_CbAcceleratorUptime_Type = OctetString
_CbAcceleratorUptime_Object = MibTableColumn
cbAcceleratorUptime = _CbAcceleratorUptime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 24),
    _CbAcceleratorUptime_Type()
)
cbAcceleratorUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorUptime.setStatus("current")
_CbAcceleratorIpList_Type = OctetString
_CbAcceleratorIpList_Object = MibTableColumn
cbAcceleratorIpList = _CbAcceleratorIpList_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 31),
    _CbAcceleratorIpList_Type()
)
cbAcceleratorIpList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorIpList.setStatus("current")
_CbAcceleratorMgmtIPAddressType_Type = InetAddressType
_CbAcceleratorMgmtIPAddressType_Object = MibTableColumn
cbAcceleratorMgmtIPAddressType = _CbAcceleratorMgmtIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 38),
    _CbAcceleratorMgmtIPAddressType_Type()
)
cbAcceleratorMgmtIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorMgmtIPAddressType.setStatus("current")
_CbAcceleratorMgmtIPAddress_Type = InetAddress
_CbAcceleratorMgmtIPAddress_Object = MibTableColumn
cbAcceleratorMgmtIPAddress = _CbAcceleratorMgmtIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 7, 3, 4, 1, 39),
    _CbAcceleratorMgmtIPAddress_Type()
)
cbAcceleratorMgmtIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorMgmtIPAddress.setStatus("current")

# Managed Objects groups


# Notification objects

cpuUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 1)
)
cpuUsageHigh.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "currentValue"),
        ("MAS-MIB-SMIV2-MIB", "thresholdValue"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    cpuUsageHigh.setStatus(
        "current"
    )

cpuUsageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 2)
)
cpuUsageNormal.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "currentValue"),
        ("MAS-MIB-SMIV2-MIB", "thresholdValue"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    cpuUsageNormal.setStatus(
        "current"
    )

memoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 3)
)
memoryUsageHigh.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "currentValue"),
        ("MAS-MIB-SMIV2-MIB", "thresholdValue"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    memoryUsageHigh.setStatus(
        "current"
    )

memoryUsageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 4)
)
memoryUsageNormal.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "currentValue"),
        ("MAS-MIB-SMIV2-MIB", "thresholdValue"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    memoryUsageNormal.setStatus(
        "current"
    )

diskUtilizationHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 35)
)
diskUtilizationHigh.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "currentValue"),
        ("MAS-MIB-SMIV2-MIB", "thresholdValue"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    diskUtilizationHigh.setStatus(
        "current"
    )

diskUtilizationNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 36)
)
diskUtilizationNormal.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "currentValue"),
        ("MAS-MIB-SMIV2-MIB", "thresholdValue"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    diskUtilizationNormal.setStatus(
        "current"
    )

subSystemDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 43)
)
subSystemDown.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    subSystemDown.setStatus(
        "current"
    )

subSystemUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 44)
)
subSystemUp.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    subSystemUp.setStatus(
        "current"
    )

subSystemFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 45)
)
subSystemFailed.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    subSystemFailed.setStatus(
        "current"
    )

mpsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 46)
)
mpsDown.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    mpsDown.setStatus(
        "current"
    )

mpsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 47)
)
mpsUp.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    mpsUp.setStatus(
        "current"
    )

passwordRecoveryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 48)
)
passwordRecoveryFailed.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    passwordRecoveryFailed.setStatus(
        "current"
    )

passwordRecoverySuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 49)
)
passwordRecoverySuccess.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    passwordRecoverySuccess.setStatus(
        "current"
    )

deviceStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 54)
)
deviceStateChanged.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    deviceStateChanged.setStatus(
        "current"
    )

backupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 58)
)
backupFailed.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    backupFailed.setStatus(
        "current"
    )

loginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 71)
)
loginFailure.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    loginFailure.setStatus(
        "current"
    )

inventoryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 72)
)
inventoryFailed.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    inventoryFailed.setStatus(
        "current"
    )

trapConfigFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 78)
)
trapConfigFailure.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    trapConfigFailure.setStatus(
        "current"
    )

pooledLicenseGrace = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 80)
)
pooledLicenseGrace.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    pooledLicenseGrace.setStatus(
        "current"
    )

pooledLicenseGraceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 81)
)
pooledLicenseGraceNormal.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    pooledLicenseGraceNormal.setStatus(
        "current"
    )

licensePoolThresholdWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 84)
)
licensePoolThresholdWarning.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    licensePoolThresholdWarning.setStatus(
        "current"
    )

licensePoolThresholdNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 85)
)
licensePoolThresholdNormal.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    licensePoolThresholdNormal.setStatus(
        "current"
    )

vipLicenseLimitWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 86)
)
vipLicenseLimitWarning.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    vipLicenseLimitWarning.setStatus(
        "current"
    )

vipLicenseLimitNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 87)
)
vipLicenseLimitNormal.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    vipLicenseLimitNormal.setStatus(
        "current"
    )

remoteBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 88)
)
remoteBackupFailed.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    remoteBackupFailed.setStatus(
        "current"
    )

remoteBackupResumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 89)
)
remoteBackupResumed.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    remoteBackupResumed.setStatus(
        "current"
    )

perfCounterThresholdHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 90)
)
perfCounterThresholdHigh.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    perfCounterThresholdHigh.setStatus(
        "current"
    )

perfCounterThresholdNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 91)
)
perfCounterThresholdNormal.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    perfCounterThresholdNormal.setStatus(
        "current"
    )

devicebackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 92)
)
devicebackupFailed.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    devicebackupFailed.setStatus(
        "current"
    )

remoteDeviceBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 93)
)
remoteDeviceBackupFailed.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    remoteDeviceBackupFailed.setStatus(
        "current"
    )

dataStorageExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 94)
)
dataStorageExceeded.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    dataStorageExceeded.setStatus(
        "current"
    )

dataStorageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 95)
)
dataStorageNormal.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    dataStorageNormal.setStatus(
        "current"
    )

sslCertThresholdBreached = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 96)
)
sslCertThresholdBreached.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    sslCertThresholdBreached.setStatus(
        "current"
    )

sslCertThresholdNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 97)
)
sslCertThresholdNormal.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    sslCertThresholdNormal.setStatus(
        "current"
    )

haFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 98)
)
haFailover.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    haFailover.setStatus(
        "current"
    )

haNoHeartBeats = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 99)
)
haNoHeartBeats.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    haNoHeartBeats.setStatus(
        "current"
    )

haDatabaseOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 100)
)
haDatabaseOutOfSync.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    haDatabaseOutOfSync.setStatus(
        "current"
    )

inventoryUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 101)
)
inventoryUp.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    inventoryUp.setStatus(
        "current"
    )

deviceBooted = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 104)
)
deviceBooted.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    deviceBooted.setStatus(
        "current"
    )

deviceRebooted = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 105)
)
deviceRebooted.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    deviceRebooted.setStatus(
        "current"
    )

autoScaleGroupAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 106)
)
autoScaleGroupAdded.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    autoScaleGroupAdded.setStatus(
        "current"
    )

autoScaleGroupModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 107)
)
autoScaleGroupModified.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    autoScaleGroupModified.setStatus(
        "current"
    )

autoScaleGroupDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 108)
)
autoScaleGroupDeleted.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    autoScaleGroupDeleted.setStatus(
        "current"
    )

clusterProvisionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 109)
)
clusterProvisionStatus.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    clusterProvisionStatus.setStatus(
        "current"
    )

nodeProvisionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 110)
)
nodeProvisionStatus.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    nodeProvisionStatus.setStatus(
        "current"
    )

coolDownPeriodStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 111)
)
coolDownPeriodStatus.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    coolDownPeriodStatus.setStatus(
        "current"
    )

clusterDeprovisionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 112)
)
clusterDeprovisionStatus.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    clusterDeprovisionStatus.setStatus(
        "current"
    )

nodeDeprovisionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 113)
)
nodeDeprovisionStatus.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    nodeDeprovisionStatus.setStatus(
        "current"
    )

drainConnPeriodStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 114)
)
drainConnPeriodStatus.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    drainConnPeriodStatus.setStatus(
        "current"
    )

deployAppStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 115)
)
deployAppStatus.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    deployAppStatus.setStatus(
        "current"
    )

modifyAppStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 116)
)
modifyAppStatus.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    modifyAppStatus.setStatus(
        "current"
    )

deleteAppStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 117)
)
deleteAppStatus.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    deleteAppStatus.setStatus(
        "current"
    )

ipLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 118)
)
ipLimitReached.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    ipLimitReached.setStatus(
        "current"
    )

scaleOutStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 119)
)
scaleOutStatus.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    scaleOutStatus.setStatus(
        "current"
    )

scaleInStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 120)
)
scaleInStatus.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    scaleInStatus.setStatus(
        "current"
    )

addIPSetStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 121)
)
addIPSetStatus.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    addIPSetStatus.setStatus(
        "current"
    )

deleteIPSetStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 122)
)
deleteIPSetStatus.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    deleteIPSetStatus.setStatus(
        "current"
    )

addZone = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 123)
)
addZone.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    addZone.setStatus(
        "current"
    )

deleteZone = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 124)
)
deleteZone.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    deleteZone.setStatus(
        "current"
    )

addRecord = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 125)
)
addRecord.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    addRecord.setStatus(
        "current"
    )

deleteRecord = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 126)
)
deleteRecord.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    deleteRecord.setStatus(
        "current"
    )

addRRData = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 127)
)
addRRData.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    addRRData.setStatus(
        "current"
    )

deleteRRData = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 128)
)
deleteRRData.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    deleteRRData.setStatus(
        "current"
    )

instancePolicyReconfigurationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 131)
)
instancePolicyReconfigurationFailed.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    instancePolicyReconfigurationFailed.setStatus(
        "current"
    )

instancePolicyReconfigurationSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 132)
)
instancePolicyReconfigurationSucceeded.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    instancePolicyReconfigurationSucceeded.setStatus(
        "current"
    )

autoscalegroupUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 5951, 7, 1, 2, 133)
)
autoscalegroupUpgrade.setObjects(
      *(("MAS-MIB-SMIV2-MIB", "source"),
        ("MAS-MIB-SMIV2-MIB", "entityName"),
        ("MAS-MIB-SMIV2-MIB", "eventMessage"),
        ("MAS-MIB-SMIV2-MIB", "severity"))
)
if mibBuilder.loadTexts:
    autoscalegroupUpgrade.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAS-MIB-SMIV2-MIB",
    **{"netScaler": netScaler,
       "masRoot": masRoot,
       "masEventGroup": masEventGroup,
       "eventVarBindOids": eventVarBindOids,
       "source": source,
       "entityName": entityName,
       "entityType": entityType,
       "eventMessage": eventMessage,
       "thresholdValue": thresholdValue,
       "currentValue": currentValue,
       "severity": severity,
       "mpsEvents": mpsEvents,
       "cpuUsageHigh": cpuUsageHigh,
       "cpuUsageNormal": cpuUsageNormal,
       "memoryUsageHigh": memoryUsageHigh,
       "memoryUsageNormal": memoryUsageNormal,
       "diskUtilizationHigh": diskUtilizationHigh,
       "diskUtilizationNormal": diskUtilizationNormal,
       "subSystemDown": subSystemDown,
       "subSystemUp": subSystemUp,
       "subSystemFailed": subSystemFailed,
       "mpsDown": mpsDown,
       "mpsUp": mpsUp,
       "passwordRecoveryFailed": passwordRecoveryFailed,
       "passwordRecoverySuccess": passwordRecoverySuccess,
       "deviceStateChanged": deviceStateChanged,
       "backupFailed": backupFailed,
       "loginFailure": loginFailure,
       "inventoryFailed": inventoryFailed,
       "trapConfigFailure": trapConfigFailure,
       "pooledLicenseGrace": pooledLicenseGrace,
       "pooledLicenseGraceNormal": pooledLicenseGraceNormal,
       "licensePoolThresholdWarning": licensePoolThresholdWarning,
       "licensePoolThresholdNormal": licensePoolThresholdNormal,
       "vipLicenseLimitWarning": vipLicenseLimitWarning,
       "vipLicenseLimitNormal": vipLicenseLimitNormal,
       "remoteBackupFailed": remoteBackupFailed,
       "remoteBackupResumed": remoteBackupResumed,
       "perfCounterThresholdHigh": perfCounterThresholdHigh,
       "perfCounterThresholdNormal": perfCounterThresholdNormal,
       "devicebackupFailed": devicebackupFailed,
       "remoteDeviceBackupFailed": remoteDeviceBackupFailed,
       "dataStorageExceeded": dataStorageExceeded,
       "dataStorageNormal": dataStorageNormal,
       "sslCertThresholdBreached": sslCertThresholdBreached,
       "sslCertThresholdNormal": sslCertThresholdNormal,
       "haFailover": haFailover,
       "haNoHeartBeats": haNoHeartBeats,
       "haDatabaseOutOfSync": haDatabaseOutOfSync,
       "inventoryUp": inventoryUp,
       "deviceBooted": deviceBooted,
       "deviceRebooted": deviceRebooted,
       "autoScaleGroupAdded": autoScaleGroupAdded,
       "autoScaleGroupModified": autoScaleGroupModified,
       "autoScaleGroupDeleted": autoScaleGroupDeleted,
       "clusterProvisionStatus": clusterProvisionStatus,
       "nodeProvisionStatus": nodeProvisionStatus,
       "coolDownPeriodStatus": coolDownPeriodStatus,
       "clusterDeprovisionStatus": clusterDeprovisionStatus,
       "nodeDeprovisionStatus": nodeDeprovisionStatus,
       "drainConnPeriodStatus": drainConnPeriodStatus,
       "deployAppStatus": deployAppStatus,
       "modifyAppStatus": modifyAppStatus,
       "deleteAppStatus": deleteAppStatus,
       "ipLimitReached": ipLimitReached,
       "scaleOutStatus": scaleOutStatus,
       "scaleInStatus": scaleInStatus,
       "addIPSetStatus": addIPSetStatus,
       "deleteIPSetStatus": deleteIPSetStatus,
       "addZone": addZone,
       "deleteZone": deleteZone,
       "addRecord": addRecord,
       "deleteRecord": deleteRecord,
       "addRRData": addRRData,
       "deleteRRData": deleteRRData,
       "instancePolicyReconfigurationFailed": instancePolicyReconfigurationFailed,
       "instancePolicyReconfigurationSucceeded": instancePolicyReconfigurationSucceeded,
       "autoscalegroupUpgrade": autoscalegroupUpgrade,
       "systemGroup": systemGroup,
       "systemPlatform": systemPlatform,
       "systemProduct": systemProduct,
       "systemBuildNumber": systemBuildNumber,
       "systemIPAddressType": systemIPAddressType,
       "systemIPAddress": systemIPAddress,
       "systemNetmaskType": systemNetmaskType,
       "systemNetmask": systemNetmask,
       "systemGatewayType": systemGatewayType,
       "systemGateway": systemGateway,
       "systemDnsType": systemDnsType,
       "systemDns": systemDns,
       "systemSysId": systemSysId,
       "systemSerial": systemSerial,
       "systemCurrentTime": systemCurrentTime,
       "systemUptime": systemUptime,
       "systemBiosVersion": systemBiosVersion,
       "systemCustomID": systemCustomID,
       "systemCpuUsage": systemCpuUsage,
       "systemMemoryUsage": systemMemoryUsage,
       "systemDiskUsage": systemDiskUsage,
       "deviceGroup": deviceGroup,
       "netscalerTable": netscalerTable,
       "netscalerEntry": netscalerEntry,
       "nsIpAddressType": nsIpAddressType,
       "nsIpAddress": nsIpAddress,
       "nsHostIPAddressType": nsHostIPAddressType,
       "nsHostIPAddress": nsHostIPAddress,
       "nsProfileName": nsProfileName,
       "nsName": nsName,
       "nsNetmaskType": nsNetmaskType,
       "nsNetmask": nsNetmask,
       "nsGatewayType": nsGatewayType,
       "nsGateway": nsGateway,
       "nsHostname": nsHostname,
       "nsDescription": nsDescription,
       "nsVersion": nsVersion,
       "nsUuid": nsUuid,
       "nsInstanceState": nsInstanceState,
       "nsVirtualFunctions": nsVirtualFunctions,
       "nsSslVirtualFunctions": nsSslVirtualFunctions,
       "nsVmState": nsVmState,
       "nsNumberOfCPU": nsNumberOfCPU,
       "nsVmMemoryTotal": nsVmMemoryTotal,
       "nsUptime": nsUptime,
       "nsNumberOfSSLCores": nsNumberOfSSLCores,
       "nsCpuCoreMgmt": nsCpuCoreMgmt,
       "nsCpuCorePE": nsCpuCorePE,
       "nsVmDescription": nsVmDescription,
       "nsThroughput": nsThroughput,
       "nsNumberOfCores": nsNumberOfCores,
       "nsNsCPUUsage": nsNsCPUUsage,
       "nsNsMemoryUsage": nsNsMemoryUsage,
       "nsNsTx": nsNsTx,
       "nsNsRx": nsNsRx,
       "nsHttpReq": nsHttpReq,
       "nsUpsince": nsUpsince,
       "nsLicense": nsLicense,
       "nsHaMasterState": nsHaMasterState,
       "nsHaIPAddressType": nsHaIPAddressType,
       "nsHaIPAddress": nsHaIPAddress,
       "nsNodeState": nsNodeState,
       "nsHaSync": nsHaSync,
       "nsPps": nsPps,
       "nsNumberOfSslCoresUp": nsNumberOfSslCoresUp,
       "nsIfOby1": nsIfOby1,
       "nsIf0by2": nsIf0by2,
       "nsNsVLANId": nsNsVLANId,
       "nsNsVLANTagged": nsNsVLANTagged,
       "nsVlanType": nsVlanType,
       "cloudBridgeTable": cloudBridgeTable,
       "cloudBridgeEntry": cloudBridgeEntry,
       "cbIpAddressType": cbIpAddressType,
       "cbIpAddress": cbIpAddress,
       "cbHostIPAddressType": cbHostIPAddressType,
       "cbHostIPAddress": cbHostIPAddress,
       "cbProfileName": cbProfileName,
       "cbName": cbName,
       "cbNetmaskType": cbNetmaskType,
       "cbNetmask": cbNetmask,
       "cbGatewayType": cbGatewayType,
       "cbGateway": cbGateway,
       "cbHostname": cbHostname,
       "cbDescription": cbDescription,
       "cbVersion": cbVersion,
       "cbInstanceState": cbInstanceState,
       "cbUuid": cbUuid,
       "cbVirtualFunctions": cbVirtualFunctions,
       "cbVmState": cbVmState,
       "cbNumberOfCPU": cbNumberOfCPU,
       "cbVmCPUUsage": cbVmCPUUsage,
       "cbVmMemoryTotal": cbVmMemoryTotal,
       "cbVmMemoryFree": cbVmMemoryFree,
       "cbVmMemoryUsage": cbVmMemoryUsage,
       "cbUptime": cbUptime,
       "cbDiskAllocation": cbDiskAllocation,
       "cbAPAIPADDRESSType": cbAPAIPADDRESSType,
       "cbAPAIPADDRESS": cbAPAIPADDRESS,
       "cbAPANetMaskType": cbAPANetMaskType,
       "cbAPANetMask": cbAPANetMask,
       "cbAPAGatewayType": cbAPAGatewayType,
       "cbAPAGateway": cbAPAGateway,
       "cbPluginIPADDRESSType": cbPluginIPADDRESSType,
       "cbPluginIPADDRESS": cbPluginIPADDRESS,
       "cbMgmtIPAddressType": cbMgmtIPAddressType,
       "cbMgmtIPAddress": cbMgmtIPAddress,
       "cloudBridgeAcceleratorTable": cloudBridgeAcceleratorTable,
       "cloudBridgeAcceleratorEntry": cloudBridgeAcceleratorEntry,
       "cbAcceleratorIpAddressType": cbAcceleratorIpAddressType,
       "cbAcceleratorIpAddress": cbAcceleratorIpAddress,
       "cbAcceleratorHostIPAddressType": cbAcceleratorHostIPAddressType,
       "cbAcceleratorHostIPAddress": cbAcceleratorHostIPAddress,
       "cbAcceleratorProfileName": cbAcceleratorProfileName,
       "cbAcceleratorName": cbAcceleratorName,
       "cbAcceleratorNetmaskType": cbAcceleratorNetmaskType,
       "cbAcceleratorNetmask": cbAcceleratorNetmask,
       "cbAcceleratorGatewayType": cbAcceleratorGatewayType,
       "cbAcceleratorGateway": cbAcceleratorGateway,
       "cbAcceleratorHostname": cbAcceleratorHostname,
       "cbAcceleratorDescription": cbAcceleratorDescription,
       "cbAcceleratorVersion": cbAcceleratorVersion,
       "cbAcceleratorInstanceState": cbAcceleratorInstanceState,
       "cbAcceleratorUuid": cbAcceleratorUuid,
       "cbAcceleratorVmState": cbAcceleratorVmState,
       "cbAcceleratorNumberOfCPU": cbAcceleratorNumberOfCPU,
       "cbAcceleratorVmCPUUsage": cbAcceleratorVmCPUUsage,
       "cbAcceleratorVmMemoryTotal": cbAcceleratorVmMemoryTotal,
       "cbAcceleratorVmMemoryFree": cbAcceleratorVmMemoryFree,
       "cbAcceleratorVmMemoryUsage": cbAcceleratorVmMemoryUsage,
       "cbAcceleratorUptime": cbAcceleratorUptime,
       "cbAcceleratorIpList": cbAcceleratorIpList,
       "cbAcceleratorMgmtIPAddressType": cbAcceleratorMgmtIPAddressType,
       "cbAcceleratorMgmtIPAddress": cbAcceleratorMgmtIPAddress}
)
