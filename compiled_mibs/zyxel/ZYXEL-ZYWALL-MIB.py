# SNMP MIB module (ZYXEL-ZYWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\zyxel\ZYXEL-ZYWALL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:36:09 2025
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
 NotificationType,
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
    "NotificationType",
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

(zywallCommon,) = mibBuilder.importSymbols(
    "ZYXEL-MIB",
    "zywallCommon")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZywallSystem_ObjectIdentity = ObjectIdentity
zywallSystem = _ZywallSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1)
)
_SysCPUUsage_Type = Integer32
_SysCPUUsage_Object = MibScalar
sysCPUUsage = _SysCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 1),
    _SysCPUUsage_Type()
)
sysCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCPUUsage.setStatus("mandatory")
_SysFlashUsage_Type = Integer32
_SysFlashUsage_Object = MibScalar
sysFlashUsage = _SysFlashUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 2),
    _SysFlashUsage_Type()
)
sysFlashUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFlashUsage.setStatus("mandatory")
_SysRAMUsage_Type = Integer32
_SysRAMUsage_Object = MibScalar
sysRAMUsage = _SysRAMUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 3),
    _SysRAMUsage_Type()
)
sysRAMUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRAMUsage.setStatus("mandatory")
_SysSessionUsage_Type = Integer32
_SysSessionUsage_Object = MibScalar
sysSessionUsage = _SysSessionUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 4),
    _SysSessionUsage_Type()
)
sysSessionUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSessionUsage.setStatus("mandatory")
_SysDeviceName_Type = DisplayString
_SysDeviceName_Object = MibScalar
sysDeviceName = _SysDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 5),
    _SysDeviceName_Type()
)
sysDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceName.setStatus("mandatory")
_SysDeviceType_Type = DisplayString
_SysDeviceType_Object = MibScalar
sysDeviceType = _SysDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 6),
    _SysDeviceType_Type()
)
sysDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceType.setStatus("mandatory")
_SysDeviceMACAddress_Type = DisplayString
_SysDeviceMACAddress_Object = MibScalar
sysDeviceMACAddress = _SysDeviceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 7),
    _SysDeviceMACAddress_Type()
)
sysDeviceMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceMACAddress.setStatus("mandatory")
_SysFirmwareVersion_Type = DisplayString
_SysFirmwareVersion_Object = MibScalar
sysFirmwareVersion = _SysFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 8),
    _SysFirmwareVersion_Type()
)
sysFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFirmwareVersion.setStatus("mandatory")
_SysLastEdit_Type = DisplayString
_SysLastEdit_Object = MibScalar
sysLastEdit = _SysLastEdit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 9),
    _SysLastEdit_Type()
)
sysLastEdit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLastEdit.setStatus("mandatory")
_SysDeviceInterfaceTable_Object = MibTable
sysDeviceInterfaceTable = _SysDeviceInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 10)
)
if mibBuilder.loadTexts:
    sysDeviceInterfaceTable.setStatus("mandatory")
_SysDeviceInterfaceEntry_Object = MibTableRow
sysDeviceInterfaceEntry = _SysDeviceInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 10, 1)
)
sysDeviceInterfaceEntry.setIndexNames(
    (0, "ZYXEL-ZYWALL-MIB", "sysDeviceInterfaceIndex"),
)
if mibBuilder.loadTexts:
    sysDeviceInterfaceEntry.setStatus("mandatory")
_SysDeviceInterfaceIndex_Type = Integer32
_SysDeviceInterfaceIndex_Object = MibTableColumn
sysDeviceInterfaceIndex = _SysDeviceInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 10, 1, 1),
    _SysDeviceInterfaceIndex_Type()
)
sysDeviceInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceInterfaceIndex.setStatus("mandatory")
_SysDeviceInterfaceName_Type = DisplayString
_SysDeviceInterfaceName_Object = MibTableColumn
sysDeviceInterfaceName = _SysDeviceInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 10, 1, 2),
    _SysDeviceInterfaceName_Type()
)
sysDeviceInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceInterfaceName.setStatus("mandatory")
_SysDeviceInterfaceIPAddress_Type = IpAddress
_SysDeviceInterfaceIPAddress_Object = MibTableColumn
sysDeviceInterfaceIPAddress = _SysDeviceInterfaceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 10, 1, 3),
    _SysDeviceInterfaceIPAddress_Type()
)
sysDeviceInterfaceIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceInterfaceIPAddress.setStatus("mandatory")
_SysDeviceInterfaceIPSubnetMask_Type = IpAddress
_SysDeviceInterfaceIPSubnetMask_Object = MibTableColumn
sysDeviceInterfaceIPSubnetMask = _SysDeviceInterfaceIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 10, 1, 4),
    _SysDeviceInterfaceIPSubnetMask_Type()
)
sysDeviceInterfaceIPSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceInterfaceIPSubnetMask.setStatus("mandatory")
_SysDeviceInterfaceTx_Type = Integer32
_SysDeviceInterfaceTx_Object = MibTableColumn
sysDeviceInterfaceTx = _SysDeviceInterfaceTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 10, 1, 5),
    _SysDeviceInterfaceTx_Type()
)
sysDeviceInterfaceTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceInterfaceTx.setStatus("mandatory")
_SysDeviceInterfaceRx_Type = Integer32
_SysDeviceInterfaceRx_Object = MibTableColumn
sysDeviceInterfaceRx = _SysDeviceInterfaceRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 10, 1, 6),
    _SysDeviceInterfaceRx_Type()
)
sysDeviceInterfaceRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceInterfaceRx.setStatus("mandatory")
_SysMaxSessionPerHost_Type = Integer32
_SysMaxSessionPerHost_Object = MibScalar
sysMaxSessionPerHost = _SysMaxSessionPerHost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 11),
    _SysMaxSessionPerHost_Type()
)
sysMaxSessionPerHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMaxSessionPerHost.setStatus("mandatory")
_SysHTTPPort_Type = DisplayString
_SysHTTPPort_Object = MibScalar
sysHTTPPort = _SysHTTPPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 12),
    _SysHTTPPort_Type()
)
sysHTTPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHTTPPort.setStatus("mandatory")
_SysDeviceARPTable_Object = MibTable
sysDeviceARPTable = _SysDeviceARPTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 13)
)
if mibBuilder.loadTexts:
    sysDeviceARPTable.setStatus("mandatory")
_SysDeviceARPEntry_Object = MibTableRow
sysDeviceARPEntry = _SysDeviceARPEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 13, 1)
)
sysDeviceARPEntry.setIndexNames(
    (0, "ZYXEL-ZYWALL-MIB", "sysDeviceARPIndex"),
)
if mibBuilder.loadTexts:
    sysDeviceARPEntry.setStatus("mandatory")
_SysDeviceARPIndex_Type = Integer32
_SysDeviceARPIndex_Object = MibTableColumn
sysDeviceARPIndex = _SysDeviceARPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 13, 1, 1),
    _SysDeviceARPIndex_Type()
)
sysDeviceARPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceARPIndex.setStatus("mandatory")
_SysDeviceARPIPAddress_Type = IpAddress
_SysDeviceARPIPAddress_Object = MibTableColumn
sysDeviceARPIPAddress = _SysDeviceARPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 13, 1, 2),
    _SysDeviceARPIPAddress_Type()
)
sysDeviceARPIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceARPIPAddress.setStatus("mandatory")
_SysDeviceARPMACAddress_Type = DisplayString
_SysDeviceARPMACAddress_Object = MibTableColumn
sysDeviceARPMACAddress = _SysDeviceARPMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 13, 1, 3),
    _SysDeviceARPMACAddress_Type()
)
sysDeviceARPMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceARPMACAddress.setStatus("mandatory")
_SysDeviceARPInterface_Type = DisplayString
_SysDeviceARPInterface_Object = MibTableColumn
sysDeviceARPInterface = _SysDeviceARPInterface_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 13, 1, 4),
    _SysDeviceARPInterface_Type()
)
sysDeviceARPInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceARPInterface.setStatus("mandatory")
_SysDeviceARPTTL_Type = Integer32
_SysDeviceARPTTL_Object = MibTableColumn
sysDeviceARPTTL = _SysDeviceARPTTL_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 13, 1, 5),
    _SysDeviceARPTTL_Type()
)
sysDeviceARPTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceARPTTL.setStatus("mandatory")
_SysLANDHCPTable_Object = MibTable
sysLANDHCPTable = _SysLANDHCPTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 14)
)
if mibBuilder.loadTexts:
    sysLANDHCPTable.setStatus("mandatory")
_SysLANDHCPEntry_Object = MibTableRow
sysLANDHCPEntry = _SysLANDHCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 14, 1)
)
sysLANDHCPEntry.setIndexNames(
    (0, "ZYXEL-ZYWALL-MIB", "sysLANDHCPIndex"),
)
if mibBuilder.loadTexts:
    sysLANDHCPEntry.setStatus("mandatory")
_SysLANDHCPIndex_Type = Integer32
_SysLANDHCPIndex_Object = MibTableColumn
sysLANDHCPIndex = _SysLANDHCPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 14, 1, 1),
    _SysLANDHCPIndex_Type()
)
sysLANDHCPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLANDHCPIndex.setStatus("mandatory")
_SysLANDHCPIPAddress_Type = IpAddress
_SysLANDHCPIPAddress_Object = MibTableColumn
sysLANDHCPIPAddress = _SysLANDHCPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 14, 1, 2),
    _SysLANDHCPIPAddress_Type()
)
sysLANDHCPIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLANDHCPIPAddress.setStatus("mandatory")
_SysLANDHCPMACAddress_Type = DisplayString
_SysLANDHCPMACAddress_Object = MibTableColumn
sysLANDHCPMACAddress = _SysLANDHCPMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 14, 1, 3),
    _SysLANDHCPMACAddress_Type()
)
sysLANDHCPMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLANDHCPMACAddress.setStatus("mandatory")
_SysLANDHCPHostname_Type = DisplayString
_SysLANDHCPHostname_Object = MibTableColumn
sysLANDHCPHostname = _SysLANDHCPHostname_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 14, 1, 4),
    _SysLANDHCPHostname_Type()
)
sysLANDHCPHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLANDHCPHostname.setStatus("mandatory")
_SysDMZDHCPTable_Object = MibTable
sysDMZDHCPTable = _SysDMZDHCPTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 15)
)
if mibBuilder.loadTexts:
    sysDMZDHCPTable.setStatus("mandatory")
_SysDMZDHCPEntry_Object = MibTableRow
sysDMZDHCPEntry = _SysDMZDHCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 15, 1)
)
sysDMZDHCPEntry.setIndexNames(
    (0, "ZYXEL-ZYWALL-MIB", "sysDMZDHCPIndex"),
)
if mibBuilder.loadTexts:
    sysDMZDHCPEntry.setStatus("mandatory")
_SysDMZDHCPIndex_Type = Integer32
_SysDMZDHCPIndex_Object = MibTableColumn
sysDMZDHCPIndex = _SysDMZDHCPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 15, 1, 1),
    _SysDMZDHCPIndex_Type()
)
sysDMZDHCPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDMZDHCPIndex.setStatus("mandatory")
_SysDMZDHCPIPAddress_Type = IpAddress
_SysDMZDHCPIPAddress_Object = MibTableColumn
sysDMZDHCPIPAddress = _SysDMZDHCPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 15, 1, 2),
    _SysDMZDHCPIPAddress_Type()
)
sysDMZDHCPIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDMZDHCPIPAddress.setStatus("mandatory")
_SysDMZDHCPMACAddress_Type = DisplayString
_SysDMZDHCPMACAddress_Object = MibTableColumn
sysDMZDHCPMACAddress = _SysDMZDHCPMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 15, 1, 3),
    _SysDMZDHCPMACAddress_Type()
)
sysDMZDHCPMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDMZDHCPMACAddress.setStatus("mandatory")
_SysDMZDHCPHostname_Type = DisplayString
_SysDMZDHCPHostname_Object = MibTableColumn
sysDMZDHCPHostname = _SysDMZDHCPHostname_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 15, 1, 4),
    _SysDMZDHCPHostname_Type()
)
sysDMZDHCPHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDMZDHCPHostname.setStatus("mandatory")
_SysWLANDHCPTable_Object = MibTable
sysWLANDHCPTable = _SysWLANDHCPTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 16)
)
if mibBuilder.loadTexts:
    sysWLANDHCPTable.setStatus("mandatory")
_SysWLANDHCPEntry_Object = MibTableRow
sysWLANDHCPEntry = _SysWLANDHCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 16, 1)
)
sysWLANDHCPEntry.setIndexNames(
    (0, "ZYXEL-ZYWALL-MIB", "sysWLANDHCPIndex"),
)
if mibBuilder.loadTexts:
    sysWLANDHCPEntry.setStatus("mandatory")
_SysWLANDHCPIndex_Type = Integer32
_SysWLANDHCPIndex_Object = MibTableColumn
sysWLANDHCPIndex = _SysWLANDHCPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 16, 1, 1),
    _SysWLANDHCPIndex_Type()
)
sysWLANDHCPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysWLANDHCPIndex.setStatus("mandatory")
_SysWLANDHCPIPAddress_Type = IpAddress
_SysWLANDHCPIPAddress_Object = MibTableColumn
sysWLANDHCPIPAddress = _SysWLANDHCPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 16, 1, 2),
    _SysWLANDHCPIPAddress_Type()
)
sysWLANDHCPIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysWLANDHCPIPAddress.setStatus("mandatory")
_SysWLANDHCPMACAddress_Type = DisplayString
_SysWLANDHCPMACAddress_Object = MibTableColumn
sysWLANDHCPMACAddress = _SysWLANDHCPMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 16, 1, 3),
    _SysWLANDHCPMACAddress_Type()
)
sysWLANDHCPMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysWLANDHCPMACAddress.setStatus("mandatory")
_SysWLANDHCPHostname_Type = DisplayString
_SysWLANDHCPHostname_Object = MibTableColumn
sysWLANDHCPHostname = _SysWLANDHCPHostname_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 16, 1, 4),
    _SysWLANDHCPHostname_Type()
)
sysWLANDHCPHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysWLANDHCPHostname.setStatus("mandatory")
_SysDeviceMode_Type = DisplayString
_SysDeviceMode_Object = MibScalar
sysDeviceMode = _SysDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 1, 17),
    _SysDeviceMode_Type()
)
sysDeviceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceMode.setStatus("mandatory")
_ZywallFirewall_ObjectIdentity = ObjectIdentity
zywallFirewall = _ZywallFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 2)
)
_FirewallDirTable_Object = MibTable
firewallDirTable = _FirewallDirTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    firewallDirTable.setStatus("mandatory")
_FirewallDirEntry_Object = MibTableRow
firewallDirEntry = _FirewallDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 2, 1, 1)
)
firewallDirEntry.setIndexNames(
    (0, "ZYXEL-ZYWALL-MIB", "firewallDirIndex"),
)
if mibBuilder.loadTexts:
    firewallDirEntry.setStatus("mandatory")


class _FirewallDirIndex_Type(Integer32):
    """Custom type firewallDirIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("LANTOWAN", 1),
          ("WANTOLAN", 2),
          ("DMZTOLAN", 3),
          ("DMZTOWAN", 4),
          ("WANTODMZ", 5),
          ("LANTODMZ", 6),
          ("LANTOLAN", 7),
          ("WANTOWAN", 8),
          ("DMZTODMZ", 9),
          ("LANTOROUTER", 10),
          ("WANTOROUTER", 11),
          ("DMZTOROUTER", 12))
    )


_FirewallDirIndex_Type.__name__ = "Integer32"
_FirewallDirIndex_Object = MibTableColumn
firewallDirIndex = _FirewallDirIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 2, 1, 1, 1),
    _FirewallDirIndex_Type()
)
firewallDirIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallDirIndex.setStatus("mandatory")
_FirewallDirForwardPktCnt_Type = Counter64
_FirewallDirForwardPktCnt_Object = MibTableColumn
firewallDirForwardPktCnt = _FirewallDirForwardPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 2, 1, 1, 2),
    _FirewallDirForwardPktCnt_Type()
)
firewallDirForwardPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallDirForwardPktCnt.setStatus("mandatory")
_FirewallDirForwardPktSize_Type = Counter64
_FirewallDirForwardPktSize_Object = MibTableColumn
firewallDirForwardPktSize = _FirewallDirForwardPktSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 2, 1, 1, 3),
    _FirewallDirForwardPktSize_Type()
)
firewallDirForwardPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallDirForwardPktSize.setStatus("mandatory")
_FirewallDirBlockPktCnt_Type = Counter64
_FirewallDirBlockPktCnt_Object = MibTableColumn
firewallDirBlockPktCnt = _FirewallDirBlockPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 2, 1, 1, 4),
    _FirewallDirBlockPktCnt_Type()
)
firewallDirBlockPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallDirBlockPktCnt.setStatus("mandatory")
_FirewallDirBlockPktSize_Type = Counter64
_FirewallDirBlockPktSize_Object = MibTableColumn
firewallDirBlockPktSize = _FirewallDirBlockPktSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 2, 1, 1, 5),
    _FirewallDirBlockPktSize_Type()
)
firewallDirBlockPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallDirBlockPktSize.setStatus("mandatory")
_FirewallTotalRules_Type = Integer32
_FirewallTotalRules_Object = MibScalar
firewallTotalRules = _FirewallTotalRules_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 2, 2),
    _FirewallTotalRules_Type()
)
firewallTotalRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallTotalRules.setStatus("mandatory")
_FirewallNewRules_Type = Integer32
_FirewallNewRules_Object = MibScalar
firewallNewRules = _FirewallNewRules_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 2, 3),
    _FirewallNewRules_Type()
)
firewallNewRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallNewRules.setStatus("mandatory")
_FirewallDelRules_Type = Integer32
_FirewallDelRules_Object = MibScalar
firewallDelRules = _FirewallDelRules_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 2, 4),
    _FirewallDelRules_Type()
)
firewallDelRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallDelRules.setStatus("mandatory")
_FirewallActRules_Type = Integer32
_FirewallActRules_Object = MibScalar
firewallActRules = _FirewallActRules_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 2, 5),
    _FirewallActRules_Type()
)
firewallActRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallActRules.setStatus("mandatory")
_FirewallDeActRules_Type = Integer32
_FirewallDeActRules_Object = MibScalar
firewallDeActRules = _FirewallDeActRules_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 2, 6),
    _FirewallDeActRules_Type()
)
firewallDeActRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallDeActRules.setStatus("mandatory")
_ZywallVPN_ObjectIdentity = ObjectIdentity
zywallVPN = _ZywallVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3)
)
_VpnTunnelTable_Object = MibTable
vpnTunnelTable = _VpnTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    vpnTunnelTable.setStatus("mandatory")
_VpnTunnelEntry_Object = MibTableRow
vpnTunnelEntry = _VpnTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1)
)
vpnTunnelEntry.setIndexNames(
    (0, "ZYXEL-ZYWALL-MIB", "vpnTunnelIndex"),
)
if mibBuilder.loadTexts:
    vpnTunnelEntry.setStatus("mandatory")
_VpnTunnelIndex_Type = Integer32
_VpnTunnelIndex_Object = MibTableColumn
vpnTunnelIndex = _VpnTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 1),
    _VpnTunnelIndex_Type()
)
vpnTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelIndex.setStatus("mandatory")
_VpnTunnelName_Type = DisplayString
_VpnTunnelName_Object = MibTableColumn
vpnTunnelName = _VpnTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 2),
    _VpnTunnelName_Type()
)
vpnTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelName.setStatus("mandatory")
_VpnTunnelTxPktCnt_Type = Counter64
_VpnTunnelTxPktCnt_Object = MibTableColumn
vpnTunnelTxPktCnt = _VpnTunnelTxPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 3),
    _VpnTunnelTxPktCnt_Type()
)
vpnTunnelTxPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelTxPktCnt.setStatus("mandatory")
_VpnTunnelTxPktSize_Type = Counter64
_VpnTunnelTxPktSize_Object = MibTableColumn
vpnTunnelTxPktSize = _VpnTunnelTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 4),
    _VpnTunnelTxPktSize_Type()
)
vpnTunnelTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelTxPktSize.setStatus("mandatory")
_VpnTunnelRxPktCnt_Type = Counter64
_VpnTunnelRxPktCnt_Object = MibTableColumn
vpnTunnelRxPktCnt = _VpnTunnelRxPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 5),
    _VpnTunnelRxPktCnt_Type()
)
vpnTunnelRxPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelRxPktCnt.setStatus("mandatory")
_VpnTunnelRxPktSize_Type = Counter64
_VpnTunnelRxPktSize_Object = MibTableColumn
vpnTunnelRxPktSize = _VpnTunnelRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 6),
    _VpnTunnelRxPktSize_Type()
)
vpnTunnelRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelRxPktSize.setStatus("mandatory")
_VpnTunnelDisPktCnt_Type = Counter64
_VpnTunnelDisPktCnt_Object = MibTableColumn
vpnTunnelDisPktCnt = _VpnTunnelDisPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 7),
    _VpnTunnelDisPktCnt_Type()
)
vpnTunnelDisPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelDisPktCnt.setStatus("mandatory")
_VpnTunnelDisPktSize_Type = Counter64
_VpnTunnelDisPktSize_Object = MibTableColumn
vpnTunnelDisPktSize = _VpnTunnelDisPktSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 8),
    _VpnTunnelDisPktSize_Type()
)
vpnTunnelDisPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelDisPktSize.setStatus("mandatory")
_VpnTunnelUpTime_Type = DisplayString
_VpnTunnelUpTime_Object = MibTableColumn
vpnTunnelUpTime = _VpnTunnelUpTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 9),
    _VpnTunnelUpTime_Type()
)
vpnTunnelUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelUpTime.setStatus("mandatory")
_VpnTunnelLaunchNum_Type = Integer32
_VpnTunnelLaunchNum_Object = MibTableColumn
vpnTunnelLaunchNum = _VpnTunnelLaunchNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 10),
    _VpnTunnelLaunchNum_Type()
)
vpnTunnelLaunchNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelLaunchNum.setStatus("mandatory")
_VpnTunnelCloseNum_Type = Integer32
_VpnTunnelCloseNum_Object = MibTableColumn
vpnTunnelCloseNum = _VpnTunnelCloseNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 11),
    _VpnTunnelCloseNum_Type()
)
vpnTunnelCloseNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelCloseNum.setStatus("mandatory")
_VpnTunnelFailReason_Type = DisplayString
_VpnTunnelFailReason_Object = MibTableColumn
vpnTunnelFailReason = _VpnTunnelFailReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 12),
    _VpnTunnelFailReason_Type()
)
vpnTunnelFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelFailReason.setStatus("mandatory")
_VpnTunnelFailTime_Type = DisplayString
_VpnTunnelFailTime_Object = MibTableColumn
vpnTunnelFailTime = _VpnTunnelFailTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 13),
    _VpnTunnelFailTime_Type()
)
vpnTunnelFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelFailTime.setStatus("mandatory")
_VpnTunnelRuleIndex_Type = Integer32
_VpnTunnelRuleIndex_Object = MibTableColumn
vpnTunnelRuleIndex = _VpnTunnelRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 14),
    _VpnTunnelRuleIndex_Type()
)
vpnTunnelRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelRuleIndex.setStatus("mandatory")
_VpnTunnelRuleName_Type = DisplayString
_VpnTunnelRuleName_Object = MibTableColumn
vpnTunnelRuleName = _VpnTunnelRuleName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 15),
    _VpnTunnelRuleName_Type()
)
vpnTunnelRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelRuleName.setStatus("mandatory")


class _VpnTunnelActivity_Type(Integer32):
    """Custom type vpnTunnelActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Off", 0),
          ("On", 1))
    )


_VpnTunnelActivity_Type.__name__ = "Integer32"
_VpnTunnelActivity_Object = MibTableColumn
vpnTunnelActivity = _VpnTunnelActivity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 16),
    _VpnTunnelActivity_Type()
)
vpnTunnelActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpnTunnelActivity.setStatus("mandatory")
_VpnTunnelLocalNetwork_Type = DisplayString
_VpnTunnelLocalNetwork_Object = MibTableColumn
vpnTunnelLocalNetwork = _VpnTunnelLocalNetwork_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 17),
    _VpnTunnelLocalNetwork_Type()
)
vpnTunnelLocalNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelLocalNetwork.setStatus("mandatory")
_VpnTunnelRemoteNetwork_Type = DisplayString
_VpnTunnelRemoteNetwork_Object = MibTableColumn
vpnTunnelRemoteNetwork = _VpnTunnelRemoteNetwork_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 18),
    _VpnTunnelRemoteNetwork_Type()
)
vpnTunnelRemoteNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelRemoteNetwork.setStatus("mandatory")
_VpnTunnelEncapsulation_Type = DisplayString
_VpnTunnelEncapsulation_Object = MibTableColumn
vpnTunnelEncapsulation = _VpnTunnelEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 19),
    _VpnTunnelEncapsulation_Type()
)
vpnTunnelEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelEncapsulation.setStatus("mandatory")
_VpnTunnelAlgorithm_Type = DisplayString
_VpnTunnelAlgorithm_Object = MibTableColumn
vpnTunnelAlgorithm = _VpnTunnelAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 20),
    _VpnTunnelAlgorithm_Type()
)
vpnTunnelAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelAlgorithm.setStatus("mandatory")
_VpnTunnelRemoteGateway_Type = DisplayString
_VpnTunnelRemoteGateway_Object = MibTableColumn
vpnTunnelRemoteGateway = _VpnTunnelRemoteGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 1, 1, 21),
    _VpnTunnelRemoteGateway_Type()
)
vpnTunnelRemoteGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelRemoteGateway.setStatus("mandatory")
_VpnUpTunnel_Type = Integer32
_VpnUpTunnel_Object = MibScalar
vpnUpTunnel = _VpnUpTunnel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 2),
    _VpnUpTunnel_Type()
)
vpnUpTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnUpTunnel.setStatus("mandatory")
_VpnPhase1ErrbyLocal_Type = Integer32
_VpnPhase1ErrbyLocal_Object = MibScalar
vpnPhase1ErrbyLocal = _VpnPhase1ErrbyLocal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 3),
    _VpnPhase1ErrbyLocal_Type()
)
vpnPhase1ErrbyLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnPhase1ErrbyLocal.setStatus("mandatory")
_VpnPhase1ErrbyRemote_Type = Integer32
_VpnPhase1ErrbyRemote_Object = MibScalar
vpnPhase1ErrbyRemote = _VpnPhase1ErrbyRemote_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 4),
    _VpnPhase1ErrbyRemote_Type()
)
vpnPhase1ErrbyRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnPhase1ErrbyRemote.setStatus("mandatory")
_VpnPhase2ErrbyLocal_Type = Integer32
_VpnPhase2ErrbyLocal_Object = MibScalar
vpnPhase2ErrbyLocal = _VpnPhase2ErrbyLocal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 5),
    _VpnPhase2ErrbyLocal_Type()
)
vpnPhase2ErrbyLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnPhase2ErrbyLocal.setStatus("mandatory")
_VpnPhase2ErrbyRemote_Type = Integer32
_VpnPhase2ErrbyRemote_Object = MibScalar
vpnPhase2ErrbyRemote = _VpnPhase2ErrbyRemote_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 6),
    _VpnPhase2ErrbyRemote_Type()
)
vpnPhase2ErrbyRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnPhase2ErrbyRemote.setStatus("mandatory")
_VpnLocalUserTable_Object = MibTable
vpnLocalUserTable = _VpnLocalUserTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 7)
)
if mibBuilder.loadTexts:
    vpnLocalUserTable.setStatus("mandatory")
_VpnLocalUserEntry_Object = MibTableRow
vpnLocalUserEntry = _VpnLocalUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 7, 1)
)
vpnLocalUserEntry.setIndexNames(
    (0, "ZYXEL-ZYWALL-MIB", "vpnLocalUserIndex"),
)
if mibBuilder.loadTexts:
    vpnLocalUserEntry.setStatus("mandatory")
_VpnLocalUserIndex_Type = Integer32
_VpnLocalUserIndex_Object = MibTableColumn
vpnLocalUserIndex = _VpnLocalUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 7, 1, 1),
    _VpnLocalUserIndex_Type()
)
vpnLocalUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnLocalUserIndex.setStatus("mandatory")
_VpnLocalUserName_Type = DisplayString
_VpnLocalUserName_Object = MibTableColumn
vpnLocalUserName = _VpnLocalUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 7, 1, 2),
    _VpnLocalUserName_Type()
)
vpnLocalUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnLocalUserName.setStatus("mandatory")
_VpnLocalUserFailCnt_Type = Counter64
_VpnLocalUserFailCnt_Object = MibTableColumn
vpnLocalUserFailCnt = _VpnLocalUserFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 3, 7, 1, 3),
    _VpnLocalUserFailCnt_Type()
)
vpnLocalUserFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnLocalUserFailCnt.setStatus("mandatory")
_ZywallIDP_ObjectIdentity = ObjectIdentity
zywallIDP = _ZywallIDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 4)
)
_IdpSigVersion_Type = DisplayString
_IdpSigVersion_Object = MibScalar
idpSigVersion = _IdpSigVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 4, 1),
    _IdpSigVersion_Type()
)
idpSigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idpSigVersion.setStatus("mandatory")
_IdpSigDate_Type = DisplayString
_IdpSigDate_Object = MibScalar
idpSigDate = _IdpSigDate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 4, 2),
    _IdpSigDate_Type()
)
idpSigDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idpSigDate.setStatus("mandatory")
_ZywallAV_ObjectIdentity = ObjectIdentity
zywallAV = _ZywallAV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 5)
)
_AvSigVersion_Type = DisplayString
_AvSigVersion_Object = MibScalar
avSigVersion = _AvSigVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 5, 1),
    _AvSigVersion_Type()
)
avSigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avSigVersion.setStatus("mandatory")
_AvSigDate_Type = DisplayString
_AvSigDate_Object = MibScalar
avSigDate = _AvSigDate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 5, 2),
    _AvSigDate_Type()
)
avSigDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avSigDate.setStatus("mandatory")
_ZywallTraps_ObjectIdentity = ObjectIdentity
zywallTraps = _ZywallTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1, 99)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ZYWALL-MIB",
    **{"zywallSystem": zywallSystem,
       "sysCPUUsage": sysCPUUsage,
       "sysFlashUsage": sysFlashUsage,
       "sysRAMUsage": sysRAMUsage,
       "sysSessionUsage": sysSessionUsage,
       "sysDeviceName": sysDeviceName,
       "sysDeviceType": sysDeviceType,
       "sysDeviceMACAddress": sysDeviceMACAddress,
       "sysFirmwareVersion": sysFirmwareVersion,
       "sysLastEdit": sysLastEdit,
       "sysDeviceInterfaceTable": sysDeviceInterfaceTable,
       "sysDeviceInterfaceEntry": sysDeviceInterfaceEntry,
       "sysDeviceInterfaceIndex": sysDeviceInterfaceIndex,
       "sysDeviceInterfaceName": sysDeviceInterfaceName,
       "sysDeviceInterfaceIPAddress": sysDeviceInterfaceIPAddress,
       "sysDeviceInterfaceIPSubnetMask": sysDeviceInterfaceIPSubnetMask,
       "sysDeviceInterfaceTx": sysDeviceInterfaceTx,
       "sysDeviceInterfaceRx": sysDeviceInterfaceRx,
       "sysMaxSessionPerHost": sysMaxSessionPerHost,
       "sysHTTPPort": sysHTTPPort,
       "sysDeviceARPTable": sysDeviceARPTable,
       "sysDeviceARPEntry": sysDeviceARPEntry,
       "sysDeviceARPIndex": sysDeviceARPIndex,
       "sysDeviceARPIPAddress": sysDeviceARPIPAddress,
       "sysDeviceARPMACAddress": sysDeviceARPMACAddress,
       "sysDeviceARPInterface": sysDeviceARPInterface,
       "sysDeviceARPTTL": sysDeviceARPTTL,
       "sysLANDHCPTable": sysLANDHCPTable,
       "sysLANDHCPEntry": sysLANDHCPEntry,
       "sysLANDHCPIndex": sysLANDHCPIndex,
       "sysLANDHCPIPAddress": sysLANDHCPIPAddress,
       "sysLANDHCPMACAddress": sysLANDHCPMACAddress,
       "sysLANDHCPHostname": sysLANDHCPHostname,
       "sysDMZDHCPTable": sysDMZDHCPTable,
       "sysDMZDHCPEntry": sysDMZDHCPEntry,
       "sysDMZDHCPIndex": sysDMZDHCPIndex,
       "sysDMZDHCPIPAddress": sysDMZDHCPIPAddress,
       "sysDMZDHCPMACAddress": sysDMZDHCPMACAddress,
       "sysDMZDHCPHostname": sysDMZDHCPHostname,
       "sysWLANDHCPTable": sysWLANDHCPTable,
       "sysWLANDHCPEntry": sysWLANDHCPEntry,
       "sysWLANDHCPIndex": sysWLANDHCPIndex,
       "sysWLANDHCPIPAddress": sysWLANDHCPIPAddress,
       "sysWLANDHCPMACAddress": sysWLANDHCPMACAddress,
       "sysWLANDHCPHostname": sysWLANDHCPHostname,
       "sysDeviceMode": sysDeviceMode,
       "zywallFirewall": zywallFirewall,
       "firewallDirTable": firewallDirTable,
       "firewallDirEntry": firewallDirEntry,
       "firewallDirIndex": firewallDirIndex,
       "firewallDirForwardPktCnt": firewallDirForwardPktCnt,
       "firewallDirForwardPktSize": firewallDirForwardPktSize,
       "firewallDirBlockPktCnt": firewallDirBlockPktCnt,
       "firewallDirBlockPktSize": firewallDirBlockPktSize,
       "firewallTotalRules": firewallTotalRules,
       "firewallNewRules": firewallNewRules,
       "firewallDelRules": firewallDelRules,
       "firewallActRules": firewallActRules,
       "firewallDeActRules": firewallDeActRules,
       "zywallVPN": zywallVPN,
       "vpnTunnelTable": vpnTunnelTable,
       "vpnTunnelEntry": vpnTunnelEntry,
       "vpnTunnelIndex": vpnTunnelIndex,
       "vpnTunnelName": vpnTunnelName,
       "vpnTunnelTxPktCnt": vpnTunnelTxPktCnt,
       "vpnTunnelTxPktSize": vpnTunnelTxPktSize,
       "vpnTunnelRxPktCnt": vpnTunnelRxPktCnt,
       "vpnTunnelRxPktSize": vpnTunnelRxPktSize,
       "vpnTunnelDisPktCnt": vpnTunnelDisPktCnt,
       "vpnTunnelDisPktSize": vpnTunnelDisPktSize,
       "vpnTunnelUpTime": vpnTunnelUpTime,
       "vpnTunnelLaunchNum": vpnTunnelLaunchNum,
       "vpnTunnelCloseNum": vpnTunnelCloseNum,
       "vpnTunnelFailReason": vpnTunnelFailReason,
       "vpnTunnelFailTime": vpnTunnelFailTime,
       "vpnTunnelRuleIndex": vpnTunnelRuleIndex,
       "vpnTunnelRuleName": vpnTunnelRuleName,
       "vpnTunnelActivity": vpnTunnelActivity,
       "vpnTunnelLocalNetwork": vpnTunnelLocalNetwork,
       "vpnTunnelRemoteNetwork": vpnTunnelRemoteNetwork,
       "vpnTunnelEncapsulation": vpnTunnelEncapsulation,
       "vpnTunnelAlgorithm": vpnTunnelAlgorithm,
       "vpnTunnelRemoteGateway": vpnTunnelRemoteGateway,
       "vpnUpTunnel": vpnUpTunnel,
       "vpnPhase1ErrbyLocal": vpnPhase1ErrbyLocal,
       "vpnPhase1ErrbyRemote": vpnPhase1ErrbyRemote,
       "vpnPhase2ErrbyLocal": vpnPhase2ErrbyLocal,
       "vpnPhase2ErrbyRemote": vpnPhase2ErrbyRemote,
       "vpnLocalUserTable": vpnLocalUserTable,
       "vpnLocalUserEntry": vpnLocalUserEntry,
       "vpnLocalUserIndex": vpnLocalUserIndex,
       "vpnLocalUserName": vpnLocalUserName,
       "vpnLocalUserFailCnt": vpnLocalUserFailCnt,
       "zywallIDP": zywallIDP,
       "idpSigVersion": idpSigVersion,
       "idpSigDate": idpSigDate,
       "zywallAV": zywallAV,
       "avSigVersion": avSigVersion,
       "avSigDate": avSigDate,
       "zywallTraps": zywallTraps}
)
