# SNMP MIB module (VMWARE-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vmware\VMWARE-RESOURCES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:26 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(vmwResources,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwResources")

(VmwSubsystemStatus,) = mibBuilder.importSymbols(
    "VMWARE-TC-MIB",
    "VmwSubsystemStatus")


# MODULE-IDENTITY

vmwResourcesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 3, 10)
)
if mibBuilder.loadTexts:
    vmwResourcesMIB.setRevisions(
        ("2008-10-15 00:00",
         "2007-12-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwCPU_ObjectIdentity = ObjectIdentity
vmwCPU = _VmwCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 3, 1)
)
if mibBuilder.loadTexts:
    vmwCPU.setStatus("current")
_VmwNumCPUs_Type = Gauge32
_VmwNumCPUs_Object = MibScalar
vmwNumCPUs = _VmwNumCPUs_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 1, 1),
    _VmwNumCPUs_Type()
)
vmwNumCPUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwNumCPUs.setStatus("current")
_VmwMemory_ObjectIdentity = ObjectIdentity
vmwMemory = _VmwMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2)
)
_VmwMemSize_Type = Gauge32
_VmwMemSize_Object = MibScalar
vmwMemSize = _VmwMemSize_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2, 1),
    _VmwMemSize_Type()
)
vmwMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwMemSize.setStatus("current")
if mibBuilder.loadTexts:
    vmwMemSize.setUnits("kilobytes")
_VmwMemCOS_Type = Gauge32
_VmwMemCOS_Object = MibScalar
vmwMemCOS = _VmwMemCOS_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2, 2),
    _VmwMemCOS_Type()
)
vmwMemCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwMemCOS.setStatus("current")
if mibBuilder.loadTexts:
    vmwMemCOS.setUnits("kilobytes")
_VmwMemAvail_Type = Gauge32
_VmwMemAvail_Object = MibScalar
vmwMemAvail = _VmwMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2, 3),
    _VmwMemAvail_Type()
)
vmwMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwMemAvail.setStatus("current")
if mibBuilder.loadTexts:
    vmwMemAvail.setUnits("kilobytes")
_VmwStorage_ObjectIdentity = ObjectIdentity
vmwStorage = _VmwStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 3, 5)
)
_VmwHostBusAdapterNumber_Type = Integer32
_VmwHostBusAdapterNumber_Object = MibScalar
vmwHostBusAdapterNumber = _VmwHostBusAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 5, 1),
    _VmwHostBusAdapterNumber_Type()
)
vmwHostBusAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwHostBusAdapterNumber.setStatus("current")
_VmwHostBusAdapterTable_Object = MibTable
vmwHostBusAdapterTable = _VmwHostBusAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 5, 2)
)
if mibBuilder.loadTexts:
    vmwHostBusAdapterTable.setStatus("current")
_VmwHostBusAdapterEntry_Object = MibTableRow
vmwHostBusAdapterEntry = _VmwHostBusAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 5, 2, 1)
)
vmwHostBusAdapterEntry.setIndexNames(
    (0, "VMWARE-RESOURCES-MIB", "vmwHostBusAdapterIndex"),
)
if mibBuilder.loadTexts:
    vmwHostBusAdapterEntry.setStatus("current")


class _VmwHostBusAdapterIndex_Type(Integer32):
    """Custom type vmwHostBusAdapterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_VmwHostBusAdapterIndex_Type.__name__ = "Integer32"
_VmwHostBusAdapterIndex_Object = MibTableColumn
vmwHostBusAdapterIndex = _VmwHostBusAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 5, 2, 1, 1),
    _VmwHostBusAdapterIndex_Type()
)
vmwHostBusAdapterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmwHostBusAdapterIndex.setStatus("current")
_VmwHbaDeviceName_Type = DisplayString
_VmwHbaDeviceName_Object = MibTableColumn
vmwHbaDeviceName = _VmwHbaDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 5, 2, 1, 2),
    _VmwHbaDeviceName_Type()
)
vmwHbaDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwHbaDeviceName.setStatus("current")


class _VmwHbaBusNumber_Type(Integer32):
    """Custom type vmwHbaBusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1023),
    )


_VmwHbaBusNumber_Type.__name__ = "Integer32"
_VmwHbaBusNumber_Object = MibTableColumn
vmwHbaBusNumber = _VmwHbaBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 5, 2, 1, 3),
    _VmwHbaBusNumber_Type()
)
vmwHbaBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwHbaBusNumber.setStatus("current")
_VmwHbaStatus_Type = VmwSubsystemStatus
_VmwHbaStatus_Object = MibTableColumn
vmwHbaStatus = _VmwHbaStatus_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 5, 2, 1, 4),
    _VmwHbaStatus_Type()
)
vmwHbaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwHbaStatus.setStatus("current")
_VmwHbaModelName_Type = DisplayString
_VmwHbaModelName_Object = MibTableColumn
vmwHbaModelName = _VmwHbaModelName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 5, 2, 1, 5),
    _VmwHbaModelName_Type()
)
vmwHbaModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwHbaModelName.setStatus("current")
_VmwHbaDriverName_Type = DisplayString
_VmwHbaDriverName_Object = MibTableColumn
vmwHbaDriverName = _VmwHbaDriverName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 5, 2, 1, 6),
    _VmwHbaDriverName_Type()
)
vmwHbaDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwHbaDriverName.setStatus("current")
_VmwHbaPci_Type = DisplayString
_VmwHbaPci_Object = MibTableColumn
vmwHbaPci = _VmwHbaPci_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 5, 2, 1, 7),
    _VmwHbaPci_Type()
)
vmwHbaPci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwHbaPci.setStatus("current")
_VmwResourceMIBConformance_ObjectIdentity = ObjectIdentity
vmwResourceMIBConformance = _VmwResourceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 3, 10, 2)
)
_VmwResourceMIBCompliances_ObjectIdentity = ObjectIdentity
vmwResourceMIBCompliances = _VmwResourceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 3, 10, 2, 1)
)
_VmwResMIBGroups_ObjectIdentity = ObjectIdentity
vmwResMIBGroups = _VmwResMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 3, 10, 2, 2)
)

# Managed Objects groups

vmwResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 3, 10, 2, 2, 1)
)
vmwResourceGroup.setObjects(
      *(("VMWARE-RESOURCES-MIB", "vmwNumCPUs"),
        ("VMWARE-RESOURCES-MIB", "vmwMemSize"),
        ("VMWARE-RESOURCES-MIB", "vmwMemCOS"),
        ("VMWARE-RESOURCES-MIB", "vmwMemAvail"),
        ("VMWARE-RESOURCES-MIB", "vmwHostBusAdapterNumber"),
        ("VMWARE-RESOURCES-MIB", "vmwHbaDeviceName"),
        ("VMWARE-RESOURCES-MIB", "vmwHbaBusNumber"),
        ("VMWARE-RESOURCES-MIB", "vmwHbaStatus"),
        ("VMWARE-RESOURCES-MIB", "vmwHbaModelName"),
        ("VMWARE-RESOURCES-MIB", "vmwHbaDriverName"),
        ("VMWARE-RESOURCES-MIB", "vmwHbaPci"))
)
if mibBuilder.loadTexts:
    vmwResourceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vmwResourceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 3, 10, 2, 1, 2)
)
vmwResourceMIBCompliance.setObjects(
    ("VMWARE-RESOURCES-MIB", "vmwResourceGroup")
)
if mibBuilder.loadTexts:
    vmwResourceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-RESOURCES-MIB",
    **{"vmwCPU": vmwCPU,
       "vmwNumCPUs": vmwNumCPUs,
       "vmwMemory": vmwMemory,
       "vmwMemSize": vmwMemSize,
       "vmwMemCOS": vmwMemCOS,
       "vmwMemAvail": vmwMemAvail,
       "vmwStorage": vmwStorage,
       "vmwHostBusAdapterNumber": vmwHostBusAdapterNumber,
       "vmwHostBusAdapterTable": vmwHostBusAdapterTable,
       "vmwHostBusAdapterEntry": vmwHostBusAdapterEntry,
       "vmwHostBusAdapterIndex": vmwHostBusAdapterIndex,
       "vmwHbaDeviceName": vmwHbaDeviceName,
       "vmwHbaBusNumber": vmwHbaBusNumber,
       "vmwHbaStatus": vmwHbaStatus,
       "vmwHbaModelName": vmwHbaModelName,
       "vmwHbaDriverName": vmwHbaDriverName,
       "vmwHbaPci": vmwHbaPci,
       "vmwResourcesMIB": vmwResourcesMIB,
       "vmwResourceMIBConformance": vmwResourceMIBConformance,
       "vmwResourceMIBCompliances": vmwResourceMIBCompliances,
       "vmwResourceMIBCompliance": vmwResourceMIBCompliance,
       "vmwResMIBGroups": vmwResMIBGroups,
       "vmwResourceGroup": vmwResourceGroup}
)
