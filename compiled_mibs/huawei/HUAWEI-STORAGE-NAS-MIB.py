# SNMP MIB module (HUAWEI-STORAGE-NAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\huawei\HUAWEI-STORAGE-NAS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:58:43 2025
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

hwStorage = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4)
)
if mibBuilder.loadTexts:
    hwStorage.setRevisions(
        ("2014-11-06 15:32",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NodeCodeString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 17),
    )



# MIB Managed Objects in the order of their OIDs

_Huaweistorage_ObjectIdentity = ObjectIdentity
huaweistorage = _Huaweistorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774)
)
_HwISM_ObjectIdentity = ObjectIdentity
hwISM = _HwISM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1)
)
_HwStorageDevice_ObjectIdentity = ObjectIdentity
hwStorageDevice = _HwStorageDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23)
)
_HwNasInfo_ObjectIdentity = ObjectIdentity
hwNasInfo = _HwNasInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7)
)
_HwInfoShareNFSTable_Object = MibTable
hwInfoShareNFSTable = _HwInfoShareNFSTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 1)
)
if mibBuilder.loadTexts:
    hwInfoShareNFSTable.setStatus("current")
_HwInfoShareNFSEntry_Object = MibTableRow
hwInfoShareNFSEntry = _HwInfoShareNFSEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 1, 1)
)
hwInfoShareNFSEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-NAS-MIB", "hwInfoShareNFSShareID"),
)
if mibBuilder.loadTexts:
    hwInfoShareNFSEntry.setStatus("current")
_HwInfoShareNFSShareID_Type = OctetString
_HwInfoShareNFSShareID_Object = MibTableColumn
hwInfoShareNFSShareID = _HwInfoShareNFSShareID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 1, 1, 1),
    _HwInfoShareNFSShareID_Type()
)
hwInfoShareNFSShareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoShareNFSShareID.setStatus("current")
_HwInfoShareNFSFileSystemID_Type = OctetString
_HwInfoShareNFSFileSystemID_Object = MibTableColumn
hwInfoShareNFSFileSystemID = _HwInfoShareNFSFileSystemID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 1, 1, 2),
    _HwInfoShareNFSFileSystemID_Type()
)
hwInfoShareNFSFileSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoShareNFSFileSystemID.setStatus("current")
_HwInfoShareNFSDescription_Type = OctetString
_HwInfoShareNFSDescription_Object = MibTableColumn
hwInfoShareNFSDescription = _HwInfoShareNFSDescription_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 1, 1, 3),
    _HwInfoShareNFSDescription_Type()
)
hwInfoShareNFSDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoShareNFSDescription.setStatus("current")
_HwInfoShareNFSLocalPath_Type = OctetString
_HwInfoShareNFSLocalPath_Object = MibTableColumn
hwInfoShareNFSLocalPath = _HwInfoShareNFSLocalPath_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 1, 1, 4),
    _HwInfoShareNFSLocalPath_Type()
)
hwInfoShareNFSLocalPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoShareNFSLocalPath.setStatus("current")
_HwInfoShareCIFSTable_Object = MibTable
hwInfoShareCIFSTable = _HwInfoShareCIFSTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 2)
)
if mibBuilder.loadTexts:
    hwInfoShareCIFSTable.setStatus("current")
_HwInfoShareCIFSEntry_Object = MibTableRow
hwInfoShareCIFSEntry = _HwInfoShareCIFSEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 2, 1)
)
hwInfoShareCIFSEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-NAS-MIB", "hwInfoShareCIFSID"),
)
if mibBuilder.loadTexts:
    hwInfoShareCIFSEntry.setStatus("current")
_HwInfoShareCIFSID_Type = OctetString
_HwInfoShareCIFSID_Object = MibTableColumn
hwInfoShareCIFSID = _HwInfoShareCIFSID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 2, 1, 1),
    _HwInfoShareCIFSID_Type()
)
hwInfoShareCIFSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoShareCIFSID.setStatus("current")
_HwInfoShareCIFSName_Type = OctetString
_HwInfoShareCIFSName_Object = MibTableColumn
hwInfoShareCIFSName = _HwInfoShareCIFSName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 2, 1, 2),
    _HwInfoShareCIFSName_Type()
)
hwInfoShareCIFSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoShareCIFSName.setStatus("current")
_HwInfoShareCIFSFileSystemID_Type = OctetString
_HwInfoShareCIFSFileSystemID_Object = MibTableColumn
hwInfoShareCIFSFileSystemID = _HwInfoShareCIFSFileSystemID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 2, 1, 3),
    _HwInfoShareCIFSFileSystemID_Type()
)
hwInfoShareCIFSFileSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoShareCIFSFileSystemID.setStatus("current")
_HwInfoShareCIFSDescription_Type = OctetString
_HwInfoShareCIFSDescription_Object = MibTableColumn
hwInfoShareCIFSDescription = _HwInfoShareCIFSDescription_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 2, 1, 4),
    _HwInfoShareCIFSDescription_Type()
)
hwInfoShareCIFSDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoShareCIFSDescription.setStatus("current")
_HwInfoShareCIFSLocalPath_Type = OctetString
_HwInfoShareCIFSLocalPath_Object = MibTableColumn
hwInfoShareCIFSLocalPath = _HwInfoShareCIFSLocalPath_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 2, 1, 5),
    _HwInfoShareCIFSLocalPath_Type()
)
hwInfoShareCIFSLocalPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoShareCIFSLocalPath.setStatus("current")
_HwInfoShareCIFSOplockEnabled_Type = Unsigned32
_HwInfoShareCIFSOplockEnabled_Object = MibTableColumn
hwInfoShareCIFSOplockEnabled = _HwInfoShareCIFSOplockEnabled_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 2, 1, 6),
    _HwInfoShareCIFSOplockEnabled_Type()
)
hwInfoShareCIFSOplockEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoShareCIFSOplockEnabled.setStatus("current")
_HwInfoShareCIFSNotifyEnabled_Type = Unsigned32
_HwInfoShareCIFSNotifyEnabled_Object = MibTableColumn
hwInfoShareCIFSNotifyEnabled = _HwInfoShareCIFSNotifyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 2, 1, 7),
    _HwInfoShareCIFSNotifyEnabled_Type()
)
hwInfoShareCIFSNotifyEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoShareCIFSNotifyEnabled.setStatus("current")
_HwInfoShareCIFSContAvailableEna_Type = Unsigned32
_HwInfoShareCIFSContAvailableEna_Object = MibTableColumn
hwInfoShareCIFSContAvailableEna = _HwInfoShareCIFSContAvailableEna_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 2, 1, 8),
    _HwInfoShareCIFSContAvailableEna_Type()
)
hwInfoShareCIFSContAvailableEna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoShareCIFSContAvailableEna.setStatus("current")
_HwInfoSharePermsNFSTable_Object = MibTable
hwInfoSharePermsNFSTable = _HwInfoSharePermsNFSTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 3)
)
if mibBuilder.loadTexts:
    hwInfoSharePermsNFSTable.setStatus("current")
_HwInfoSharePermsNFSEntry_Object = MibTableRow
hwInfoSharePermsNFSEntry = _HwInfoSharePermsNFSEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 3, 1)
)
hwInfoSharePermsNFSEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-NAS-MIB", "hwInfoSharePermsNFSID"),
)
if mibBuilder.loadTexts:
    hwInfoSharePermsNFSEntry.setStatus("current")
_HwInfoSharePermsNFSID_Type = OctetString
_HwInfoSharePermsNFSID_Object = MibTableColumn
hwInfoSharePermsNFSID = _HwInfoSharePermsNFSID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 3, 1, 1),
    _HwInfoSharePermsNFSID_Type()
)
hwInfoSharePermsNFSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoSharePermsNFSID.setStatus("current")
_HwInfoSharePermsNFSAccessName_Type = OctetString
_HwInfoSharePermsNFSAccessName_Object = MibTableColumn
hwInfoSharePermsNFSAccessName = _HwInfoSharePermsNFSAccessName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 3, 1, 2),
    _HwInfoSharePermsNFSAccessName_Type()
)
hwInfoSharePermsNFSAccessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoSharePermsNFSAccessName.setStatus("current")
_HwInfoSharePermsNFSShareID_Type = OctetString
_HwInfoSharePermsNFSShareID_Object = MibTableColumn
hwInfoSharePermsNFSShareID = _HwInfoSharePermsNFSShareID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 3, 1, 3),
    _HwInfoSharePermsNFSShareID_Type()
)
hwInfoSharePermsNFSShareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoSharePermsNFSShareID.setStatus("current")
_HwInfoSharePermsNFSAccessType_Type = Unsigned32
_HwInfoSharePermsNFSAccessType_Object = MibTableColumn
hwInfoSharePermsNFSAccessType = _HwInfoSharePermsNFSAccessType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 3, 1, 4),
    _HwInfoSharePermsNFSAccessType_Type()
)
hwInfoSharePermsNFSAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoSharePermsNFSAccessType.setStatus("current")
_HwInfoSharePermsNFSSyncEnabled_Type = Unsigned32
_HwInfoSharePermsNFSSyncEnabled_Object = MibTableColumn
hwInfoSharePermsNFSSyncEnabled = _HwInfoSharePermsNFSSyncEnabled_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 3, 1, 5),
    _HwInfoSharePermsNFSSyncEnabled_Type()
)
hwInfoSharePermsNFSSyncEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoSharePermsNFSSyncEnabled.setStatus("current")
_HwInfoSharePermsNFSAllSquashEna_Type = Unsigned32
_HwInfoSharePermsNFSAllSquashEna_Object = MibTableColumn
hwInfoSharePermsNFSAllSquashEna = _HwInfoSharePermsNFSAllSquashEna_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 3, 1, 6),
    _HwInfoSharePermsNFSAllSquashEna_Type()
)
hwInfoSharePermsNFSAllSquashEna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoSharePermsNFSAllSquashEna.setStatus("current")
_HwInfoSharePermsNFSRootSquashEna_Type = Unsigned32
_HwInfoSharePermsNFSRootSquashEna_Object = MibTableColumn
hwInfoSharePermsNFSRootSquashEna = _HwInfoSharePermsNFSRootSquashEna_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 3, 1, 7),
    _HwInfoSharePermsNFSRootSquashEna_Type()
)
hwInfoSharePermsNFSRootSquashEna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoSharePermsNFSRootSquashEna.setStatus("current")
_HwInfoSharePermsCIFSTable_Object = MibTable
hwInfoSharePermsCIFSTable = _HwInfoSharePermsCIFSTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 4)
)
if mibBuilder.loadTexts:
    hwInfoSharePermsCIFSTable.setStatus("current")
_HwInfoSharePermsCIFSEntry_Object = MibTableRow
hwInfoSharePermsCIFSEntry = _HwInfoSharePermsCIFSEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 4, 1)
)
hwInfoSharePermsCIFSEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-NAS-MIB", "hwInfoSharePermsCIFSID"),
)
if mibBuilder.loadTexts:
    hwInfoSharePermsCIFSEntry.setStatus("current")
_HwInfoSharePermsCIFSID_Type = OctetString
_HwInfoSharePermsCIFSID_Object = MibTableColumn
hwInfoSharePermsCIFSID = _HwInfoSharePermsCIFSID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 4, 1, 1),
    _HwInfoSharePermsCIFSID_Type()
)
hwInfoSharePermsCIFSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoSharePermsCIFSID.setStatus("current")
_HwInfoSharePermsCIFSAccessName_Type = OctetString
_HwInfoSharePermsCIFSAccessName_Object = MibTableColumn
hwInfoSharePermsCIFSAccessName = _HwInfoSharePermsCIFSAccessName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 4, 1, 2),
    _HwInfoSharePermsCIFSAccessName_Type()
)
hwInfoSharePermsCIFSAccessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoSharePermsCIFSAccessName.setStatus("current")
_HwInfoSharePermsCIFSShareID_Type = OctetString
_HwInfoSharePermsCIFSShareID_Object = MibTableColumn
hwInfoSharePermsCIFSShareID = _HwInfoSharePermsCIFSShareID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 4, 1, 3),
    _HwInfoSharePermsCIFSShareID_Type()
)
hwInfoSharePermsCIFSShareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoSharePermsCIFSShareID.setStatus("current")
_HwInfoSharePermsCIFSDomainType_Type = Unsigned32
_HwInfoSharePermsCIFSDomainType_Object = MibTableColumn
hwInfoSharePermsCIFSDomainType = _HwInfoSharePermsCIFSDomainType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 4, 1, 4),
    _HwInfoSharePermsCIFSDomainType_Type()
)
hwInfoSharePermsCIFSDomainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoSharePermsCIFSDomainType.setStatus("current")
_HwInfoSharePermsCIFSPermsType_Type = Unsigned32
_HwInfoSharePermsCIFSPermsType_Object = MibTableColumn
hwInfoSharePermsCIFSPermsType = _HwInfoSharePermsCIFSPermsType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 4, 1, 5),
    _HwInfoSharePermsCIFSPermsType_Type()
)
hwInfoSharePermsCIFSPermsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoSharePermsCIFSPermsType.setStatus("current")
_HwInfoLogicalPortTable_Object = MibTable
hwInfoLogicalPortTable = _HwInfoLogicalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5)
)
if mibBuilder.loadTexts:
    hwInfoLogicalPortTable.setStatus("current")
_HwInfoLogicalPortEntry_Object = MibTableRow
hwInfoLogicalPortEntry = _HwInfoLogicalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1)
)
hwInfoLogicalPortEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortID"),
)
if mibBuilder.loadTexts:
    hwInfoLogicalPortEntry.setStatus("current")
_HwInfoLogicalPortID_Type = OctetString
_HwInfoLogicalPortID_Object = MibTableColumn
hwInfoLogicalPortID = _HwInfoLogicalPortID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 1),
    _HwInfoLogicalPortID_Type()
)
hwInfoLogicalPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortID.setStatus("current")
_HwInfoLogicalPorttName_Type = OctetString
_HwInfoLogicalPorttName_Object = MibTableColumn
hwInfoLogicalPorttName = _HwInfoLogicalPorttName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 2),
    _HwInfoLogicalPorttName_Type()
)
hwInfoLogicalPorttName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPorttName.setStatus("current")
_HwInfoLogicalPortRunStatus_Type = Unsigned32
_HwInfoLogicalPortRunStatus_Object = MibTableColumn
hwInfoLogicalPortRunStatus = _HwInfoLogicalPortRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 3),
    _HwInfoLogicalPortRunStatus_Type()
)
hwInfoLogicalPortRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortRunStatus.setStatus("current")
_HwInfoLogicalPortIPv4Addr_Type = OctetString
_HwInfoLogicalPortIPv4Addr_Object = MibTableColumn
hwInfoLogicalPortIPv4Addr = _HwInfoLogicalPortIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 4),
    _HwInfoLogicalPortIPv4Addr_Type()
)
hwInfoLogicalPortIPv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortIPv4Addr.setStatus("current")
_HwInfoLogicalPortIPv4Mask_Type = OctetString
_HwInfoLogicalPortIPv4Mask_Object = MibTableColumn
hwInfoLogicalPortIPv4Mask = _HwInfoLogicalPortIPv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 5),
    _HwInfoLogicalPortIPv4Mask_Type()
)
hwInfoLogicalPortIPv4Mask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortIPv4Mask.setStatus("current")
_HwInfoLogicalPortIPv4Gateway_Type = OctetString
_HwInfoLogicalPortIPv4Gateway_Object = MibTableColumn
hwInfoLogicalPortIPv4Gateway = _HwInfoLogicalPortIPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 6),
    _HwInfoLogicalPortIPv4Gateway_Type()
)
hwInfoLogicalPortIPv4Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortIPv4Gateway.setStatus("current")
_HwInfoLogicalPortIPv6Addr_Type = OctetString
_HwInfoLogicalPortIPv6Addr_Object = MibTableColumn
hwInfoLogicalPortIPv6Addr = _HwInfoLogicalPortIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 7),
    _HwInfoLogicalPortIPv6Addr_Type()
)
hwInfoLogicalPortIPv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortIPv6Addr.setStatus("current")
_HwInfoLogicalPortIPv6Mask_Type = OctetString
_HwInfoLogicalPortIPv6Mask_Object = MibTableColumn
hwInfoLogicalPortIPv6Mask = _HwInfoLogicalPortIPv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 8),
    _HwInfoLogicalPortIPv6Mask_Type()
)
hwInfoLogicalPortIPv6Mask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortIPv6Mask.setStatus("current")
_HwInfoLogicalPortIPv6Gateway_Type = OctetString
_HwInfoLogicalPortIPv6Gateway_Object = MibTableColumn
hwInfoLogicalPortIPv6Gateway = _HwInfoLogicalPortIPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 9),
    _HwInfoLogicalPortIPv6Gateway_Type()
)
hwInfoLogicalPortIPv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortIPv6Gateway.setStatus("current")
_HwInfoLogicalPortRole_Type = Unsigned32
_HwInfoLogicalPortRole_Object = MibTableColumn
hwInfoLogicalPortRole = _HwInfoLogicalPortRole_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 10),
    _HwInfoLogicalPortRole_Type()
)
hwInfoLogicalPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortRole.setStatus("current")
_HwInfoLogicalPortSupportProt_Type = Unsigned32
_HwInfoLogicalPortSupportProt_Object = MibTableColumn
hwInfoLogicalPortSupportProt = _HwInfoLogicalPortSupportProt_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 11),
    _HwInfoLogicalPortSupportProt_Type()
)
hwInfoLogicalPortSupportProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortSupportProt.setStatus("current")
_HwInfoLogicalPortHomePortType_Type = Unsigned32
_HwInfoLogicalPortHomePortType_Object = MibTableColumn
hwInfoLogicalPortHomePortType = _HwInfoLogicalPortHomePortType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 12),
    _HwInfoLogicalPortHomePortType_Type()
)
hwInfoLogicalPortHomePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortHomePortType.setStatus("current")
_HwInfoLogicalPortHomePortID_Type = OctetString
_HwInfoLogicalPortHomePortID_Object = MibTableColumn
hwInfoLogicalPortHomePortID = _HwInfoLogicalPortHomePortID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 13),
    _HwInfoLogicalPortHomePortID_Type()
)
hwInfoLogicalPortHomePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortHomePortID.setStatus("current")
_HwInfoLogicalPortOwnerCtrlID_Type = OctetString
_HwInfoLogicalPortOwnerCtrlID_Object = MibTableColumn
hwInfoLogicalPortOwnerCtrlID = _HwInfoLogicalPortOwnerCtrlID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 14),
    _HwInfoLogicalPortOwnerCtrlID_Type()
)
hwInfoLogicalPortOwnerCtrlID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortOwnerCtrlID.setStatus("current")
_HwInfoLogicalPortCurrPortType_Type = Unsigned32
_HwInfoLogicalPortCurrPortType_Object = MibTableColumn
hwInfoLogicalPortCurrPortType = _HwInfoLogicalPortCurrPortType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 15),
    _HwInfoLogicalPortCurrPortType_Type()
)
hwInfoLogicalPortCurrPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortCurrPortType.setStatus("current")
_HwInfoLogicalPortCurrPortID_Type = OctetString
_HwInfoLogicalPortCurrPortID_Object = MibTableColumn
hwInfoLogicalPortCurrPortID = _HwInfoLogicalPortCurrPortID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 16),
    _HwInfoLogicalPortCurrPortID_Type()
)
hwInfoLogicalPortCurrPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortCurrPortID.setStatus("current")
_HwInfoLogicalPortWorkCtrlID_Type = OctetString
_HwInfoLogicalPortWorkCtrlID_Object = MibTableColumn
hwInfoLogicalPortWorkCtrlID = _HwInfoLogicalPortWorkCtrlID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 17),
    _HwInfoLogicalPortWorkCtrlID_Type()
)
hwInfoLogicalPortWorkCtrlID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortWorkCtrlID.setStatus("current")
_HwInfoLogicalPortActState_Type = Unsigned32
_HwInfoLogicalPortActState_Object = MibTableColumn
hwInfoLogicalPortActState = _HwInfoLogicalPortActState_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 18),
    _HwInfoLogicalPortActState_Type()
)
hwInfoLogicalPortActState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortActState.setStatus("current")
_HwInfoLogicalPortAddrFamily_Type = Unsigned32
_HwInfoLogicalPortAddrFamily_Object = MibTableColumn
hwInfoLogicalPortAddrFamily = _HwInfoLogicalPortAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 19),
    _HwInfoLogicalPortAddrFamily_Type()
)
hwInfoLogicalPortAddrFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortAddrFamily.setStatus("current")
_HwInfoLogicalPortIsPrivate_Type = Unsigned32
_HwInfoLogicalPortIsPrivate_Object = MibTableColumn
hwInfoLogicalPortIsPrivate = _HwInfoLogicalPortIsPrivate_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 20),
    _HwInfoLogicalPortIsPrivate_Type()
)
hwInfoLogicalPortIsPrivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortIsPrivate.setStatus("current")
_HwInfoLogicalPortFailOVGID_Type = OctetString
_HwInfoLogicalPortFailOVGID_Object = MibTableColumn
hwInfoLogicalPortFailOVGID = _HwInfoLogicalPortFailOVGID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 21),
    _HwInfoLogicalPortFailOVGID_Type()
)
hwInfoLogicalPortFailOVGID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortFailOVGID.setStatus("current")
_HwInfoLogicalPortFailOVEnable_Type = Unsigned32
_HwInfoLogicalPortFailOVEnable_Object = MibTableColumn
hwInfoLogicalPortFailOVEnable = _HwInfoLogicalPortFailOVEnable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 22),
    _HwInfoLogicalPortFailOVEnable_Type()
)
hwInfoLogicalPortFailOVEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortFailOVEnable.setStatus("current")
_HwInfoLogicalPortFailBackMode_Type = Unsigned32
_HwInfoLogicalPortFailBackMode_Object = MibTableColumn
hwInfoLogicalPortFailBackMode = _HwInfoLogicalPortFailBackMode_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 23),
    _HwInfoLogicalPortFailBackMode_Type()
)
hwInfoLogicalPortFailBackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortFailBackMode.setStatus("current")
_HwInfoLogicalPortFailOVGName_Type = OctetString
_HwInfoLogicalPortFailOVGName_Object = MibTableColumn
hwInfoLogicalPortFailOVGName = _HwInfoLogicalPortFailOVGName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 5, 1, 24),
    _HwInfoLogicalPortFailOVGName_Type()
)
hwInfoLogicalPortFailOVGName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicalPortFailOVGName.setStatus("current")
_HwInfoFileSysTable_Object = MibTable
hwInfoFileSysTable = _HwInfoFileSysTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6)
)
if mibBuilder.loadTexts:
    hwInfoFileSysTable.setStatus("current")
_HwInfoFileSysEntry_Object = MibTableRow
hwInfoFileSysEntry = _HwInfoFileSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1)
)
hwInfoFileSysEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysID"),
)
if mibBuilder.loadTexts:
    hwInfoFileSysEntry.setStatus("current")
_HwInfoFileSysID_Type = OctetString
_HwInfoFileSysID_Object = MibTableColumn
hwInfoFileSysID = _HwInfoFileSysID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 1),
    _HwInfoFileSysID_Type()
)
hwInfoFileSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysID.setStatus("current")
_HwInfoFileSysName_Type = OctetString
_HwInfoFileSysName_Object = MibTableColumn
hwInfoFileSysName = _HwInfoFileSysName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 2),
    _HwInfoFileSysName_Type()
)
hwInfoFileSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysName.setStatus("current")
_HwInfoFileSysHeathStatus_Type = Unsigned32
_HwInfoFileSysHeathStatus_Object = MibTableColumn
hwInfoFileSysHeathStatus = _HwInfoFileSysHeathStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 3),
    _HwInfoFileSysHeathStatus_Type()
)
hwInfoFileSysHeathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysHeathStatus.setStatus("current")
_HwInfoFileSysRunningStatus_Type = Unsigned32
_HwInfoFileSysRunningStatus_Object = MibTableColumn
hwInfoFileSysRunningStatus = _HwInfoFileSysRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 4),
    _HwInfoFileSysRunningStatus_Type()
)
hwInfoFileSysRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysRunningStatus.setStatus("current")
_HwInfoFileSysDescription_Type = OctetString
_HwInfoFileSysDescription_Object = MibTableColumn
hwInfoFileSysDescription = _HwInfoFileSysDescription_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 5),
    _HwInfoFileSysDescription_Type()
)
hwInfoFileSysDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysDescription.setStatus("current")
_HwInfoFileSysSubType_Type = Unsigned32
_HwInfoFileSysSubType_Object = MibTableColumn
hwInfoFileSysSubType = _HwInfoFileSysSubType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 6),
    _HwInfoFileSysSubType_Type()
)
hwInfoFileSysSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysSubType.setStatus("current")
_HwInfoFileSysAllocType_Type = Unsigned32
_HwInfoFileSysAllocType_Object = MibTableColumn
hwInfoFileSysAllocType = _HwInfoFileSysAllocType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 7),
    _HwInfoFileSysAllocType_Type()
)
hwInfoFileSysAllocType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysAllocType.setStatus("current")
_HwInfoFileSysCapacity_Type = Counter64
_HwInfoFileSysCapacity_Object = MibTableColumn
hwInfoFileSysCapacity = _HwInfoFileSysCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 8),
    _HwInfoFileSysCapacity_Type()
)
hwInfoFileSysCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysCapacity.setStatus("current")
_HwInfoFileSysSnapshotReservePer_Type = Unsigned32
_HwInfoFileSysSnapshotReservePer_Object = MibTableColumn
hwInfoFileSysSnapshotReservePer = _HwInfoFileSysSnapshotReservePer_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 9),
    _HwInfoFileSysSnapshotReservePer_Type()
)
hwInfoFileSysSnapshotReservePer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysSnapshotReservePer.setStatus("current")
_HwInfoFileSysSnapshotUseCapacity_Type = Counter64
_HwInfoFileSysSnapshotUseCapacity_Object = MibTableColumn
hwInfoFileSysSnapshotUseCapacity = _HwInfoFileSysSnapshotUseCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 10),
    _HwInfoFileSysSnapshotUseCapacity_Type()
)
hwInfoFileSysSnapshotUseCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysSnapshotUseCapacity.setStatus("current")
_HwInfoFileSysSectorSize_Type = Unsigned32
_HwInfoFileSysSectorSize_Object = MibTableColumn
hwInfoFileSysSectorSize = _HwInfoFileSysSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 11),
    _HwInfoFileSysSectorSize_Type()
)
hwInfoFileSysSectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysSectorSize.setStatus("current")
_HwInfoFileSysOwningContrller_Type = OctetString
_HwInfoFileSysOwningContrller_Object = MibTableColumn
hwInfoFileSysOwningContrller = _HwInfoFileSysOwningContrller_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 12),
    _HwInfoFileSysOwningContrller_Type()
)
hwInfoFileSysOwningContrller.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysOwningContrller.setStatus("current")
_HwInfoFileSysWorkingController_Type = OctetString
_HwInfoFileSysWorkingController_Object = MibTableColumn
hwInfoFileSysWorkingController = _HwInfoFileSysWorkingController_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 13),
    _HwInfoFileSysWorkingController_Type()
)
hwInfoFileSysWorkingController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysWorkingController.setStatus("current")
_HwInfoFileSysIOPriotiry_Type = Unsigned32
_HwInfoFileSysIOPriotiry_Object = MibTableColumn
hwInfoFileSysIOPriotiry = _HwInfoFileSysIOPriotiry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 14),
    _HwInfoFileSysIOPriotiry_Type()
)
hwInfoFileSysIOPriotiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysIOPriotiry.setStatus("current")
_HwInfoFileSysEnableCompression_Type = Unsigned32
_HwInfoFileSysEnableCompression_Object = MibTableColumn
hwInfoFileSysEnableCompression = _HwInfoFileSysEnableCompression_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 15),
    _HwInfoFileSysEnableCompression_Type()
)
hwInfoFileSysEnableCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysEnableCompression.setStatus("current")
_HwInfoFileSysCompression_Type = Unsigned32
_HwInfoFileSysCompression_Object = MibTableColumn
hwInfoFileSysCompression = _HwInfoFileSysCompression_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 16),
    _HwInfoFileSysCompression_Type()
)
hwInfoFileSysCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysCompression.setStatus("current")
_HwInfoFileSysIsShowSnapDir_Type = Unsigned32
_HwInfoFileSysIsShowSnapDir_Object = MibTableColumn
hwInfoFileSysIsShowSnapDir = _HwInfoFileSysIsShowSnapDir_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 17),
    _HwInfoFileSysIsShowSnapDir_Type()
)
hwInfoFileSysIsShowSnapDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysIsShowSnapDir.setStatus("current")
_HwInfoFileSysAvailableCapacity_Type = Counter64
_HwInfoFileSysAvailableCapacity_Object = MibTableColumn
hwInfoFileSysAvailableCapacity = _HwInfoFileSysAvailableCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 18),
    _HwInfoFileSysAvailableCapacity_Type()
)
hwInfoFileSysAvailableCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysAvailableCapacity.setStatus("current")
_HwInfoFileSysAvAndAllcCapRatio_Type = Unsigned32
_HwInfoFileSysAvAndAllcCapRatio_Object = MibTableColumn
hwInfoFileSysAvAndAllcCapRatio = _HwInfoFileSysAvAndAllcCapRatio_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 19),
    _HwInfoFileSysAvAndAllcCapRatio_Type()
)
hwInfoFileSysAvAndAllcCapRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysAvAndAllcCapRatio.setStatus("current")
_HwInfoFileSysSCCachedSize_Type = Counter64
_HwInfoFileSysSCCachedSize_Object = MibTableColumn
hwInfoFileSysSCCachedSize = _HwInfoFileSysSCCachedSize_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 20),
    _HwInfoFileSysSCCachedSize_Type()
)
hwInfoFileSysSCCachedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysSCCachedSize.setStatus("current")
_HwInfoFileSysSCHitRage_Type = Unsigned32
_HwInfoFileSysSCHitRage_Object = MibTableColumn
hwInfoFileSysSCHitRage = _HwInfoFileSysSCHitRage_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 21),
    _HwInfoFileSysSCHitRage_Type()
)
hwInfoFileSysSCHitRage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysSCHitRage.setStatus("current")
_HwInfoFileSysCompressSavedRatio_Type = Unsigned32
_HwInfoFileSysCompressSavedRatio_Object = MibTableColumn
hwInfoFileSysCompressSavedRatio = _HwInfoFileSysCompressSavedRatio_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 7, 6, 1, 22),
    _HwInfoFileSysCompressSavedRatio_Type()
)
hwInfoFileSysCompressSavedRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSysCompressSavedRatio.setStatus("current")
_IsoConformance_ObjectIdentity = ObjectIdentity
isoConformance = _IsoConformance_ObjectIdentity(
    (1, 6)
)
_IsoGroups_ObjectIdentity = ObjectIdentity
isoGroups = _IsoGroups_ObjectIdentity(
    (1, 6, 1)
)
_IsoCompliances_ObjectIdentity = ObjectIdentity
isoCompliances = _IsoCompliances_ObjectIdentity(
    (1, 6, 2)
)

# Managed Objects groups

currentObjectGroup = ObjectGroup(
    (1, 6, 1, 1)
)
currentObjectGroup.setObjects(
      *(("HUAWEI-STORAGE-NAS-MIB", "hwInfoShareCIFSContAvailableEna"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoSharePermsNFSID"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoSharePermsNFSAccessName"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoSharePermsNFSShareID"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoSharePermsNFSAccessType"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoSharePermsNFSSyncEnabled"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoSharePermsNFSAllSquashEna"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoSharePermsNFSRootSquashEna"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoSharePermsCIFSID"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoSharePermsCIFSAccessName"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoSharePermsCIFSShareID"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoSharePermsCIFSDomainType"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoSharePermsCIFSPermsType"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortSupportProt"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortHomePortType"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortFailBackMode"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysID"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysName"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysHeathStatus"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysRunningStatus"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysDescription"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysSubType"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysAllocType"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysCapacity"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysSnapshotReservePer"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysSnapshotUseCapacity"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysSectorSize"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysOwningContrller"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysWorkingController"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysIOPriotiry"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysEnableCompression"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysCompression"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysIsShowSnapDir"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysAvailableCapacity"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysAvAndAllcCapRatio"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysSCCachedSize"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysSCHitRage"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoFileSysCompressSavedRatio"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoShareNFSShareID"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoShareNFSFileSystemID"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoShareNFSDescription"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoShareCIFSID"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoShareCIFSFileSystemID"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoShareCIFSDescription"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortID"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoShareNFSLocalPath"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoShareCIFSName"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoShareCIFSLocalPath"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoShareCIFSOplockEnabled"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoShareCIFSNotifyEnabled"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPorttName"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortRunStatus"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortIPv4Addr"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortIPv4Mask"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortIPv4Gateway"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortIPv6Addr"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortIPv6Mask"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortIPv6Gateway"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortRole"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortHomePortID"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortOwnerCtrlID"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortCurrPortType"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortCurrPortID"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortWorkCtrlID"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortActState"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortAddrFamily"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortIsPrivate"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortFailOVGID"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortFailOVEnable"),
        ("HUAWEI-STORAGE-NAS-MIB", "hwInfoLogicalPortFailOVGName"))
)
if mibBuilder.loadTexts:
    currentObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

basicCompliance = ModuleCompliance(
    (1, 6, 2, 1)
)
basicCompliance.setObjects(
    ("HUAWEI-STORAGE-NAS-MIB", "currentObjectGroup")
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-STORAGE-NAS-MIB",
    **{"NodeCodeString": NodeCodeString,
       "huaweistorage": huaweistorage,
       "hwStorage": hwStorage,
       "hwISM": hwISM,
       "hwStorageDevice": hwStorageDevice,
       "hwNasInfo": hwNasInfo,
       "hwInfoShareNFSTable": hwInfoShareNFSTable,
       "hwInfoShareNFSEntry": hwInfoShareNFSEntry,
       "hwInfoShareNFSShareID": hwInfoShareNFSShareID,
       "hwInfoShareNFSFileSystemID": hwInfoShareNFSFileSystemID,
       "hwInfoShareNFSDescription": hwInfoShareNFSDescription,
       "hwInfoShareNFSLocalPath": hwInfoShareNFSLocalPath,
       "hwInfoShareCIFSTable": hwInfoShareCIFSTable,
       "hwInfoShareCIFSEntry": hwInfoShareCIFSEntry,
       "hwInfoShareCIFSID": hwInfoShareCIFSID,
       "hwInfoShareCIFSName": hwInfoShareCIFSName,
       "hwInfoShareCIFSFileSystemID": hwInfoShareCIFSFileSystemID,
       "hwInfoShareCIFSDescription": hwInfoShareCIFSDescription,
       "hwInfoShareCIFSLocalPath": hwInfoShareCIFSLocalPath,
       "hwInfoShareCIFSOplockEnabled": hwInfoShareCIFSOplockEnabled,
       "hwInfoShareCIFSNotifyEnabled": hwInfoShareCIFSNotifyEnabled,
       "hwInfoShareCIFSContAvailableEna": hwInfoShareCIFSContAvailableEna,
       "hwInfoSharePermsNFSTable": hwInfoSharePermsNFSTable,
       "hwInfoSharePermsNFSEntry": hwInfoSharePermsNFSEntry,
       "hwInfoSharePermsNFSID": hwInfoSharePermsNFSID,
       "hwInfoSharePermsNFSAccessName": hwInfoSharePermsNFSAccessName,
       "hwInfoSharePermsNFSShareID": hwInfoSharePermsNFSShareID,
       "hwInfoSharePermsNFSAccessType": hwInfoSharePermsNFSAccessType,
       "hwInfoSharePermsNFSSyncEnabled": hwInfoSharePermsNFSSyncEnabled,
       "hwInfoSharePermsNFSAllSquashEna": hwInfoSharePermsNFSAllSquashEna,
       "hwInfoSharePermsNFSRootSquashEna": hwInfoSharePermsNFSRootSquashEna,
       "hwInfoSharePermsCIFSTable": hwInfoSharePermsCIFSTable,
       "hwInfoSharePermsCIFSEntry": hwInfoSharePermsCIFSEntry,
       "hwInfoSharePermsCIFSID": hwInfoSharePermsCIFSID,
       "hwInfoSharePermsCIFSAccessName": hwInfoSharePermsCIFSAccessName,
       "hwInfoSharePermsCIFSShareID": hwInfoSharePermsCIFSShareID,
       "hwInfoSharePermsCIFSDomainType": hwInfoSharePermsCIFSDomainType,
       "hwInfoSharePermsCIFSPermsType": hwInfoSharePermsCIFSPermsType,
       "hwInfoLogicalPortTable": hwInfoLogicalPortTable,
       "hwInfoLogicalPortEntry": hwInfoLogicalPortEntry,
       "hwInfoLogicalPortID": hwInfoLogicalPortID,
       "hwInfoLogicalPorttName": hwInfoLogicalPorttName,
       "hwInfoLogicalPortRunStatus": hwInfoLogicalPortRunStatus,
       "hwInfoLogicalPortIPv4Addr": hwInfoLogicalPortIPv4Addr,
       "hwInfoLogicalPortIPv4Mask": hwInfoLogicalPortIPv4Mask,
       "hwInfoLogicalPortIPv4Gateway": hwInfoLogicalPortIPv4Gateway,
       "hwInfoLogicalPortIPv6Addr": hwInfoLogicalPortIPv6Addr,
       "hwInfoLogicalPortIPv6Mask": hwInfoLogicalPortIPv6Mask,
       "hwInfoLogicalPortIPv6Gateway": hwInfoLogicalPortIPv6Gateway,
       "hwInfoLogicalPortRole": hwInfoLogicalPortRole,
       "hwInfoLogicalPortSupportProt": hwInfoLogicalPortSupportProt,
       "hwInfoLogicalPortHomePortType": hwInfoLogicalPortHomePortType,
       "hwInfoLogicalPortHomePortID": hwInfoLogicalPortHomePortID,
       "hwInfoLogicalPortOwnerCtrlID": hwInfoLogicalPortOwnerCtrlID,
       "hwInfoLogicalPortCurrPortType": hwInfoLogicalPortCurrPortType,
       "hwInfoLogicalPortCurrPortID": hwInfoLogicalPortCurrPortID,
       "hwInfoLogicalPortWorkCtrlID": hwInfoLogicalPortWorkCtrlID,
       "hwInfoLogicalPortActState": hwInfoLogicalPortActState,
       "hwInfoLogicalPortAddrFamily": hwInfoLogicalPortAddrFamily,
       "hwInfoLogicalPortIsPrivate": hwInfoLogicalPortIsPrivate,
       "hwInfoLogicalPortFailOVGID": hwInfoLogicalPortFailOVGID,
       "hwInfoLogicalPortFailOVEnable": hwInfoLogicalPortFailOVEnable,
       "hwInfoLogicalPortFailBackMode": hwInfoLogicalPortFailBackMode,
       "hwInfoLogicalPortFailOVGName": hwInfoLogicalPortFailOVGName,
       "hwInfoFileSysTable": hwInfoFileSysTable,
       "hwInfoFileSysEntry": hwInfoFileSysEntry,
       "hwInfoFileSysID": hwInfoFileSysID,
       "hwInfoFileSysName": hwInfoFileSysName,
       "hwInfoFileSysHeathStatus": hwInfoFileSysHeathStatus,
       "hwInfoFileSysRunningStatus": hwInfoFileSysRunningStatus,
       "hwInfoFileSysDescription": hwInfoFileSysDescription,
       "hwInfoFileSysSubType": hwInfoFileSysSubType,
       "hwInfoFileSysAllocType": hwInfoFileSysAllocType,
       "hwInfoFileSysCapacity": hwInfoFileSysCapacity,
       "hwInfoFileSysSnapshotReservePer": hwInfoFileSysSnapshotReservePer,
       "hwInfoFileSysSnapshotUseCapacity": hwInfoFileSysSnapshotUseCapacity,
       "hwInfoFileSysSectorSize": hwInfoFileSysSectorSize,
       "hwInfoFileSysOwningContrller": hwInfoFileSysOwningContrller,
       "hwInfoFileSysWorkingController": hwInfoFileSysWorkingController,
       "hwInfoFileSysIOPriotiry": hwInfoFileSysIOPriotiry,
       "hwInfoFileSysEnableCompression": hwInfoFileSysEnableCompression,
       "hwInfoFileSysCompression": hwInfoFileSysCompression,
       "hwInfoFileSysIsShowSnapDir": hwInfoFileSysIsShowSnapDir,
       "hwInfoFileSysAvailableCapacity": hwInfoFileSysAvailableCapacity,
       "hwInfoFileSysAvAndAllcCapRatio": hwInfoFileSysAvAndAllcCapRatio,
       "hwInfoFileSysSCCachedSize": hwInfoFileSysSCCachedSize,
       "hwInfoFileSysSCHitRage": hwInfoFileSysSCHitRage,
       "hwInfoFileSysCompressSavedRatio": hwInfoFileSysCompressSavedRatio,
       "isoConformance": isoConformance,
       "isoGroups": isoGroups,
       "currentObjectGroup": currentObjectGroup,
       "isoCompliances": isoCompliances,
       "basicCompliance": basicCompliance}
)
